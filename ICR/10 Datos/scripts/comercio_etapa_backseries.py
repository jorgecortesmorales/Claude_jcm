# -*- coding: utf-8 -*-
"""Rellenar vacio: comercio por etapa 1992-2014 (la serie construida solo cubria 2015-2024).
Descarga de UN Comtrade (Mexico 484, socio Mundo) el VALOR de exportacion (X) e importacion (M)
de TODAS las fracciones HS de la concordancia mineral-etapa, anual 1992-2014, y agrega por
(anio, mineral, etapa, flujo). Salida cruda para empalmar con comercio_por_etapa.csv.

NOTA de comparabilidad: a lo largo de 1992-2024 cambian las versiones del Sistema Armonizado
(HS1992/1996/2002/2007/2012/2017). Las fracciones a 4-6 digitos de la concordancia son en su
mayoria estables, pero algunas pueden reasignarse; por eso la serie larga se lee como tendencia,
con posibles saltos en años de revision HS (a validar por fraccion si se usa un año puntual).
"""
import urllib.request, json, time, csv, os, sys

BASE_DIR = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
CONC = os.path.join(BASE_DIR, "processed", "concordancia_hs_etapa.csv")

# mineral, etapa, [hs...]
conc = []
with open(CONC, encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        hs = [h.strip() for h in r["fracciones_hs"].split(";") if h.strip()]
        conc.append((r["mineral"], r["etapa"], hs))
# mapa hs -> (mineral, etapa)  (un hs puede mapear a un solo mineral-etapa en esta concordancia)
hs2me = {}
for m, e, hslist in conc:
    for h in hslist:
        hs2me[h] = (m, e)
codes = sorted(hs2me.keys())
YEARS = list(range(1992, 2015))
API = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

def fetch(year, flow):
    # Comtrade preview: max ~ cmdCodes por llamada; troceamos de a 20
    out = []
    for i in range(0, len(codes), 20):
        chunk = codes[i:i+20]
        url = (f"{API}?reporterCode=484&period={year}&cmdCode={','.join(chunk)}"
               f"&flowCode={flow}&partnerCode=0")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        for attempt in range(8):
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    out += json.load(r).get("data") or []
                break
            except urllib.error.HTTPError as e:
                if e.code == 429: time.sleep(8); continue
                if e.code == 404: break
                time.sleep(5)
            except Exception as ex:
                print(f"    retry {year}/{flow}: {ex}", file=sys.stderr); time.sleep(5)
        time.sleep(2)
    return out

rows = []  # anio, mineral, etapa, flujo, valor_usd
print("Descargando comercio por etapa 1992-2014 (X y M, Mundo)...", file=sys.stderr)
for y in YEARS:
    for flow in ("X", "M"):
        data = fetch(y, flow)
        agg = {}
        for r in data:
            if r.get("motCode") == 0 and r.get("partnerCode") == 0:
                cmd = str(r.get("cmdCode"))
                if cmd not in hs2me: continue
                m, e = hs2me[cmd]
                agg[(m, e)] = agg.get((m, e), 0.0) + (r.get("primaryValue") or 0.0)
        for (m, e), v in agg.items():
            rows.append(dict(anio=y, mineral=m, etapa=e, flujo=flow, valor_usd=round(v, 2)))
        print(f"  {y}/{flow}: {len(agg)} pares mineral-etapa", file=sys.stderr)

raw_dir = os.path.join(BASE_DIR, "Bases Originales", "11 Comercio Comtrade")
f_out = os.path.join(raw_dir, "comercio_etapa_1992_2014_crudo.csv")
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["anio", "mineral", "etapa", "flujo", "valor_usd"])
    w.writeheader()
    for r in sorted(rows, key=lambda x: (x["anio"], x["mineral"], x["etapa"], x["flujo"])):
        w.writerow(r)
print(f"\nEscrito: {f_out}  ({len(rows)} filas)", file=sys.stderr)
