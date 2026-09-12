# -*- coding: utf-8 -*-
"""Socios comerciales por mineral y etapa: DESTINOS de exportacion (X) y ORIGENES de
importacion (M), UN Comtrade (Mexico 484), agregado 2019-2024. Complementa las fichas de
cadena de valor con 'a que paises se exporta' y 'de que paises se importa' por eslabon.
Salida: processed/cv_comercio_socios.csv (mineral, etapa, flujo, pais, m49, valor_usd, share).
"""
import urllib.request, json, time, csv, os, sys
from collections import defaultdict

BASE_DIR = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
CONC = os.path.join(BASE_DIR, "processed", "concordancia_hs_etapa.csv")

conc = []
with open(CONC, encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        hs = [h.strip() for h in r["fracciones_hs"].split(";") if h.strip()]
        conc.append((r["mineral"], r["etapa"], hs))
hs2me = {}
for m, e, hslist in conc:
    for h in hslist:
        hs2me[h] = (m, e)
codes = sorted(hs2me.keys())
YEARS = list(range(2019, 2025))
API = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

M49 = {
 156:"China",842:"Estados Unidos",392:"Japon",410:"Corea del Sur",356:"India",
 704:"Vietnam",764:"Tailandia",458:"Malasia",702:"Singapur",360:"Indonesia",
 158:"Taiwan",344:"Hong Kong",124:"Canada",76:"Brasil",32:"Argentina",
 152:"Chile",604:"Peru",170:"Colombia",826:"Reino Unido",276:"Alemania",
 250:"Francia",380:"Italia",724:"Espana",528:"Paises Bajos",56:"Belgica",
 40:"Austria",756:"Suiza",203:"Chequia",616:"Polonia",792:"Turquia",
 784:"Emiratos Arabes",682:"Arabia Saudita",818:"Egipto",710:"Sudafrica",
 36:"Australia",554:"Nueva Zelanda",484:"Mexico",320:"Guatemala",222:"El Salvador",
 528:"Paises Bajos",372:"Irlanda",348:"Hungria",0:"Mundo",
}
def pname(code):
    try: return M49.get(int(code), f"socio_{code}")
    except: return f"socio_{code}"

def fetch(year, flow):
    out = []
    for i in range(0, len(codes), 20):
        chunk = codes[i:i+20]
        url = (f"{API}?reporterCode=484&period={year}&cmdCode={','.join(chunk)}&flowCode={flow}")
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
                print(f"    retry {year} {flow}: {ex}", file=sys.stderr); time.sleep(5)
        time.sleep(1.5)
    return out

# agg[(mineral,etapa,flow,partner)] = valor 2019-2024
agg = defaultdict(float)
for flow in ("X", "M"):
    print(f"Descargando {flow} por socio (2019-2024)...", file=sys.stderr)
    for y in YEARS:
        data = fetch(y, flow); n = 0
        for r in data:
            if r.get("motCode") != 0: continue
            p = r.get("partnerCode")
            if p in (0, None): continue
            cmd = str(r.get("cmdCode"))
            if cmd not in hs2me: continue
            m, e = hs2me[cmd]
            agg[(m, e, flow, int(p))] += (r.get("primaryValue") or 0.0)
            n += 1
        print(f"  {flow} {y}: {n} filas", file=sys.stderr)

tot = defaultdict(float)
for (m, e, fl, p), v in agg.items():
    tot[(m, e, fl)] += v
rows = []
for (m, e, fl, p), v in agg.items():
    if v <= 0: continue
    rows.append(dict(mineral=m, etapa=e, flujo=fl, pais=pname(p), m49=p,
                     valor_usd_2019_2024=round(v, 2),
                     share=round(v / tot[(m, e, fl)], 4) if tot[(m, e, fl)] else 0))
rows.sort(key=lambda x: (x["mineral"], x["etapa"], x["flujo"], -x["valor_usd_2019_2024"]))
f_out = os.path.join(BASE_DIR, "processed", "cv_comercio_socios.csv")
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["mineral","etapa","flujo","pais","m49","valor_usd_2019_2024","share"])
    w.writeheader(); w.writerows(rows)
print(f"\nEscrito: {f_out}  ({len(rows)} filas)", file=sys.stderr)
