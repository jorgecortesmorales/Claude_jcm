# -*- coding: utf-8 -*-
"""Empalma comercio por etapa 1992-2014 (crudo, back-series) con 2015-2024 (existente) a nivel
(anio, mineral, etapa, flujo) y produce:
  - comercio_por_etapa_1992_2024.csv  (serie larga mineral-etapa)
  - comercio_posicion_1992_2024.csv   (X_share_crudo por mineral-anio, serie larga)
NOTA: cambios de version HS a lo largo del periodo pueden introducir saltos en años de revision;
leer como tendencia. 2015-2024 viene del pull previo (comercio_por_etapa.csv, nivel HS)."""
import csv, os
from collections import defaultdict

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
PROC = os.path.join(BASE, "processed")
RAW = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade", "comercio_etapa_1992_2014_crudo.csv")

# 1) back-series 1992-2014 (ya a nivel mineral-etapa, flujo X/M)
rows = defaultdict(float)  # (anio,mineral,etapa,flujo) -> valor
for r in csv.DictReader(open(RAW, encoding="utf-8")):
    rows[(int(r["anio"]), r["mineral"], r["etapa"], r["flujo"])] += float(r["valor_usd"])

# 2) 2015-2024 desde comercio_por_etapa.csv (nivel HS) -> agregar a mineral-etapa, flujo X/M
FL = {"Exportacion": "X", "Importacion": "M"}
for r in csv.DictReader(open(os.path.join(PROC, "comercio_por_etapa.csv"), encoding="utf-8-sig")):
    fl = FL.get(r["flujo"], r["flujo"])
    rows[(int(r["anio"]), r["mineral"], r["etapa"], fl)] += float(r["valor_usd"])

# salida serie larga
out1 = os.path.join(PROC, "comercio_por_etapa_1992_2024.csv")
with open(out1, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["anio", "mineral", "etapa", "flujo", "valor_usd"])
    for (a, m, e, fl), v in sorted(rows.items()):
        w.writerow([a, m, e, fl, round(v, 2)])

# X_share_crudo por mineral-anio (E1 sobre total X)
xtot = defaultdict(float); xcru = defaultdict(float)
for (a, m, e, fl), v in rows.items():
    if fl != "X":
        continue
    xtot[(a, m)] += v
    if e.startswith("E1"):
        xcru[(a, m)] += v
out2 = os.path.join(PROC, "comercio_posicion_1992_2024.csv")
with open(out2, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["anio", "mineral", "X_total_usd", "X_crudo_usd", "X_share_crudo"])
    for (a, m) in sorted(xtot):
        t = xtot[(a, m)]; c = xcru[(a, m)]
        w.writerow([a, m, round(t, 2), round(c, 2), round(c / t, 4) if t else ""])

yrs = sorted({a for (a, m, e, fl) in rows})
print(f"escrito {out1}  ({len(rows)} filas, {yrs[0]}-{yrs[-1]})")
print(f"escrito {out2}")
