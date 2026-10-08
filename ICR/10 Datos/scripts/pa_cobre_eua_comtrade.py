# -*- coding: utf-8 -*-
"""Pregunta A (piloto cobre) — comercio de cobre de ESTADOS UNIDOS por socio, 1992-2024.
Descarga de UN Comtrade (API publica preview, sin clave) con EUA (842) como reportante:
  - importaciones (M) y exportaciones (X) de 2603 (mena/concentrado), 7401 (matas, cobre de
    cementacion), 7402 (sin refinar: blister/anodos), 7403 (refinado: catodos), 7404 (desperdicios
    y chatarra), 7405 (aleaciones madre);
  - importaciones (M) de semimanufacturas 7407-7413.
Valor (primaryValue, USD) y peso neto (netWgt, kg). Solo filas totales (customsCode C00, motCode 0,
partner2Code 0). partnerCode 0 = Mundo.

Salida cruda: Bases Originales/11 Comercio Comtrade/comercio_cobre_eua_1992_2024_crudo.csv
Uso: py "10 Datos/scripts/pa_cobre_eua_comtrade.py"
NOTA: socio = pais de origen declarado por EUA; contrastar con las X de Mexico (comercio espejo).
"""
import urllib.request, urllib.error, json, time, csv, os, sys

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
OUT = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade", "comercio_cobre_eua_1992_2024_crudo.csv")
API = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
YEARS = list(range(1992, 2025))
GRUPOS = [  # (codigos, flujo)
    ("2603,7401,7402,7403,7404,7405", "M"),
    ("2603,7401,7402,7403,7404,7405", "X"),
    ("7407,7408,7409", "M"),
    ("7410,7411,7412,7413", "M"),
]

def fetch(year, codes, flow):
    url = f"{API}?reporterCode=842&period={year}&cmdCode={codes}&flowCode={flow}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for _ in range(10):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.load(r)
            rows = d.get("data") or []
            if len(rows) >= 500:
                print(f"  AVISO {year} {codes} {flow}: 500 filas (limite de la API)", file=sys.stderr)
            return rows
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(10); continue
            if e.code == 404: return []
            time.sleep(6)
        except Exception as ex:
            print(f"  reintento {year}: {ex}", file=sys.stderr); time.sleep(6)
    print(f"  FALLA {year} {codes} {flow}", file=sys.stderr)
    return []

campos = ["anio", "flujo", "hs4", "socio_m49", "socio_iso", "valor_usd", "peso_kg"]
n = 0
with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(campos)
    for y in YEARS:
        for codes, flow in GRUPOS:
            for r in fetch(y, codes, flow):
                if r.get("customsCode") != "C00" or r.get("motCode") != 0 or r.get("partner2Code") != 0:
                    continue
                w.writerow([y, flow, r["cmdCode"], r["partnerCode"], r.get("partnerISO") or "",
                            r.get("primaryValue"), r.get("netWgt")])
                n += 1
            time.sleep(2)
        print(y, "ok", n, flush=True)
print("Escrito:", OUT, "| filas:", n)
