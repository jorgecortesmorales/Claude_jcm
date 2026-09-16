# -*- coding: utf-8 -*-
"""Paso 3 (ruta) — destinos de exportacion como SERIE TEMPORAL.
Descarga de UN Comtrade (Mexico 484, flujo X) el desglose POR PAIS SOCIO de todas las
fracciones HS de la concordancia, POR AÑO 1992-2024, para ver como se desplazan los destinos
(p. ej. el auge de China en el concentrado de cobre). Agrega por (anio, mineral, etapa, pais).

Salida cruda: comercio_destinos_serie_crudo.csv. El resumen (top destino y shares por año) lo
arma comercio_destinos_serie_resumen.py.
NOTA: socio = pais DECLARADO por Mexico, no destino final (reexportacion/entrepot); caveat.
"""
import urllib.request, json, time, csv, os, sys

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
CONC = os.path.join(BASE, "processed", "concordancia_hs_etapa.csv")
conc = []
with open(CONC, encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        hs = [h.strip() for h in r["fracciones_hs"].split(";") if h.strip()]
        conc.append((r["mineral"], r["etapa"], hs))
hs2me = {h: (m, e) for m, e, hslist in conc for h in hslist}
codes = sorted(hs2me.keys())
YEARS = list(range(1992, 2025))
API = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

M49 = {
 156:"China",842:"Estados Unidos",392:"Japon",410:"Corea del Sur",356:"India",704:"Vietnam",
 764:"Tailandia",458:"Malasia",702:"Singapur",360:"Indonesia",158:"Taiwan",490:"Taiwan",
 344:"Hong Kong",124:"Canada",76:"Brasil",32:"Argentina",152:"Chile",604:"Peru",170:"Colombia",
 826:"Reino Unido",276:"Alemania",250:"Francia",251:"Francia",380:"Italia",724:"Espana",
 528:"Paises Bajos",56:"Belgica",40:"Austria",756:"Suiza",757:"Suiza",203:"Chequia",616:"Polonia",
 792:"Turquia",784:"Emiratos Arabes",682:"Arabia Saudita",818:"Egipto",710:"Sudafrica",36:"Australia",
 554:"Nueva Zelanda",484:"Mexico",320:"Guatemala",222:"El Salvador",340:"Honduras",558:"Nicaragua",
 591:"Panama",188:"Costa Rica",862:"Venezuela",218:"Ecuador",600:"Paraguay",858:"Uruguay",68:"Bolivia",
 643:"Rusia",752:"Suecia",578:"Noruega",246:"Finlandia",208:"Dinamarca",372:"Irlanda",348:"Hungria",
 100:"Bulgaria",192:"Cuba",214:"Rep. Dominicana",388:"Jamaica",780:"Trinidad y Tobago",84:"Belice",
 0:"Mundo",899:"Areas nep",
}
def pname(c):
    try: return M49.get(int(c), f"socio_{c}")
    except: return f"socio_{c}"

def fetch(year):
    out = []
    for i in range(0, len(codes), 20):
        chunk = codes[i:i+20]
        url = f"{API}?reporterCode=484&period={year}&cmdCode={','.join(chunk)}&flowCode=X"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        for attempt in range(10):
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    out += json.load(r).get("data") or []
                break
            except urllib.error.HTTPError as e:
                if e.code == 429: time.sleep(10); continue
                if e.code == 404: break
                time.sleep(6)
            except Exception as ex:
                print(f"    retry {year}: {ex}", file=sys.stderr); time.sleep(6)
        time.sleep(2)
    return out

agg = {}  # (anio,mineral,etapa,pais) -> valor
print("Descargando destinos por año (X, 1992-2024)...", file=sys.stderr)
for y in YEARS:
    data = fetch(y); n = 0
    for r in data:
        if r.get("motCode") != 0: continue
        p = r.get("partnerCode")
        if p in (0, None): continue
        cmd = str(r.get("cmdCode"))
        if cmd not in hs2me: continue
        m, e = hs2me[cmd]
        k = (y, m, e, pname(p))
        agg[k] = agg.get(k, 0.0) + (r.get("primaryValue") or 0.0)
        n += 1
    print(f"  {y}: {n} filas socio", file=sys.stderr)

raw_dir = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade")
f_out = os.path.join(raw_dir, "comercio_destinos_serie_crudo.csv")
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["anio", "mineral", "etapa", "pais_destino", "valor_usd"])
    for (y, m, e, p), v in sorted(agg.items()):
        if v > 0: w.writerow([y, m, e, p, round(v, 2)])
print(f"\nEscrito: {f_out}  ({len(agg)} combinaciones)", file=sys.stderr)
