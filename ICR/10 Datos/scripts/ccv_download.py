# -*- coding: utf-8 -*-
"""Tarea 1 - CCV (coeficiente de captura de valor), paso 1: descarga de insumos.

Descarga de UN Comtrade (API publica preview, sin clave) el VALOR y el PESO NETO de las
fracciones E1 (mena/concentrado o mineral crudo) de exportacion de Mexico (reporter 484,
socio Mundo 0), anual, para 1992-2025. Con esto se calcula el valor unitario de exportacion
en frontera (USD/t) = numerador del CCV.

El archivo crudo previo (comercio_hs_comtrade_mx_2015_2024.csv) solo guardo valor_usd, sin
peso; por eso se re-descarga toda la serie capturando netWgt. No sobreescribe ese archivo.
"""
import urllib.request, json, time, csv, os, sys

# ---- Fracciones E1 por mineral (de concordancia_hs_etapa.csv) ----
E1 = {
 "cobre":     ["2603"],
 "plomo":     ["2607"],
 "zinc":      ["2608"],
 "manganeso": ["2602"],
 "oro":       ["261610"],
 "plata":     ["261690"],
 "barita":    ["251110"],
 "fluorita":  ["252921","252922"],
 "grafito":   ["250410","250490"],
 "silice":    ["250510","250610"],
}
codes = sorted({c for lst in E1.values() for c in lst})
YEARS = list(range(1992, 2026))
BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

def fetch(year):
    url = (f"{BASE}?reporterCode=484&period={year}&cmdCode={','.join(codes)}"
           f"&flowCode=X&partnerCode=0")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r).get("data") or []
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(8); continue
            if e.code == 404:
                return []
            time.sleep(5)
        except Exception as ex:
            print(f"    retry {year}: {ex}", file=sys.stderr); time.sleep(5)
    raise RuntimeError(f"fallo {year}")

rows = []  # anio, hs, valor_usd, peso_neto_kg, qty, qty_unit
print("Descargando Comtrade E1 (Mexico 484, Mundo, flujo X, 1992-2025)...", file=sys.stderr)
for y in YEARS:
    data = fetch(y)
    n = 0
    for r in data:
        if r.get("motCode") == 0 and r.get("partnerCode") == 0:
            cmd = str(r.get("cmdCode"))
            if cmd not in codes:
                continue
            rows.append(dict(
                anio=y, hs=cmd,
                valor_usd=r.get("primaryValue") or 0.0,
                peso_neto_kg=r.get("netWgt") if r.get("netWgt") is not None else "",
                qty=r.get("qty") if r.get("qty") is not None else "",
                qty_unit=r.get("qtyUnitAbbr") or r.get("qtyUnitCode") or "",
            ))
            n += 1
    print(f"  {y}: {n} filas E1", file=sys.stderr)
    time.sleep(3)

outdir = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
raw_dir = os.path.join(outdir, "Bases Originales", "11 Comercio Comtrade")
os.makedirs(raw_dir, exist_ok=True)
f_out = os.path.join(raw_dir, "comercio_e1_valor_peso_comtrade_mx_1992_2025.csv")
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["anio","hs","valor_usd","peso_neto_kg","qty","qty_unit"])
    w.writeheader()
    for r in sorted(rows, key=lambda x: (x["anio"], x["hs"])):
        r = dict(r)
        r["valor_usd"] = round(float(r["valor_usd"]), 2)
        if r["peso_neto_kg"] != "":
            r["peso_neto_kg"] = round(float(r["peso_neto_kg"]), 1)
        w.writerow(r)

print(f"\nEscrito: {f_out}  ({len(rows)} filas)", file=sys.stderr)
# resumen de cobertura por anio
by_year = {}
for r in rows:
    by_year.setdefault(r["anio"], 0)
    by_year[r["anio"]] += 1
print("Cobertura filas E1 por anio:", file=sys.stderr)
print("  " + ", ".join(f"{y}:{by_year.get(y,0)}" for y in YEARS), file=sys.stderr)
