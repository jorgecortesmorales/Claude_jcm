# -*- coding: utf-8 -*-
"""Tarea 2 - Completar el HHI consolidado por mineral 2004-2020.

El HHI 2021-2023 (hhi_consolidado.csv) se calculo con detalle POR MINA (mina->grupo vs
produccion nacional). Ese detalle solo existe 2021-2024. Para 2004-2020 hhi_numeradores.csv
solo trae participaciones a nivel EMPRESA (casi siempre el lider). Por eso 2004-2020 se
construye con el metodo documentado en la Bitacora (2026-08-01):
  - monopolios documentados = 10,000 (manganeso toda la serie; grafito desde 2014;
    fluorita monopolio de grupo desde 2012);
  - fluorita duopolio 2004-2011 por capacidades (77.61/22.39) -> ~6,524;
  - grafito duopolio 2004-2013 documentado -> ~5,848;
  - resto de minerales: HHI = suma de (participaciones de grupo conocidas)^2, con el
    residual tratado como atomistico (aproximacion; cota inferior del HHI real).
Cada fila queda etiquetada con su metodo. NO se recalculan 2021-2023 (se conservan).
Salida: hhi_consolidado.csv (serie completa 2004-2023).
"""
import csv, os
from collections import defaultdict

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
f_num = os.path.join(BASE, "hhi_numeradores.csv")
f_out = os.path.join(BASE, "hhi_consolidado.csv")

def num(s):
    s = (s or "").replace(",", "").strip()
    try: return float(s)
    except ValueError: return None

# ---- participaciones a nivel empresa por mineral-anio (2004-2020) ----
part = defaultdict(list)  # (mineral_lower, anio) -> [(empresa, pct)]
for r in csv.DictReader(open(f_num, encoding="utf-8-sig")):
    if r["nivel"] != "empresa":
        continue
    p = num(r["participacion_pct"])
    if p is None:
        continue
    part[(r["mineral"].strip().lower(), int(r["anio_dato"]))].append((r["empresa"].strip(), p))

MIN = ["cobre","zinc","plomo","oro","plata","barita","silice","fluorita","grafito","manganeso"]
rows_new = []

for m in MIN:
    for a in range(2004, 2021):
        hhi = cob = lider = metodo = nota = None
        # --- regimenes estructurales documentados ---
        if m == "manganeso":
            hhi, cob, lider, metodo = 10000, 100, "Cia. Minera Autlan 100%", "monopolio documentado"
            nota = "Autlan, productor unico toda la serie"
        elif m == "grafito":
            if a <= 2013:
                hhi, cob, lider, metodo = 5848, 100, "Grafitos Mexicanos (duopolio)", "duopolio documentado"
                nota = "duopolio Grafitos Mexicanos / Grafito Superior hasta 2013 (Bitacora 2026-07-21)"
            else:
                hhi, cob, lider, metodo = 10000, 100, "Grafitos Mexicanos 100%", "monopolio documentado"
                nota = "unico desde 2014 (sale Grafito Superior)"
        elif m == "fluorita":
            if a >= 2012:
                hhi, cob, lider, metodo = 10000, 100, "Koura/Orbia (Mexichem) 100%", "monopolio documentado"
                nota = "monopolio de grupo desde ene-2012 (fusion Fluorita de Mexico); cubre hueco 2019-2020"
            else:
                lst = part.get((m, a), [])
                if lst:
                    cob = sum(p for _, p in lst)
                    hhi = sum(p*p for _, p in lst)
                    top = max(lst, key=lambda x: x[1])
                    lider = f"{top[0]} {top[1]:.1f}%"
                    metodo = "duopolio (capacidades USGS Tabla 2)"
                    nota = "reparto por capacidad 77.61/22.39 (Bitacora 2026-07-21)"
        # --- resto: suma de participaciones conocidas ^2 (residual atomistico) ---
        if hhi is None:
            lst = part.get((m, a), [])
            if lst:
                cob = sum(p for _, p in lst)
                hhi = sum(p*p for _, p in lst)
                top = max(lst, key=lambda x: x[1])
                lider = f"{top[0]} {top[1]:.1f}%"
                metodo = "lider/grupos conocidos + residual atomistico (aprox.)"
                nota = "cota inferior: solo participaciones documentadas; residual tratado como atomistico"
        if hhi is not None:
            rows_new.append(dict(mineral=m, anio=a, hhi=round(hhi), cobertura_pct=round(cob),
                                 lider=lider or "", metodo=metodo, nota=nota or ""))

# ---- conservar 2021-2023 existentes (detalle por mina) ----
rows_keep = []
if os.path.exists(f_out):
    for r in csv.DictReader(open(f_out, encoding="utf-8-sig")):
        if int(r["anio"]) >= 2021:
            rows_keep.append(r)

allrows = rows_new + rows_keep
order = {mm: i for i, mm in enumerate(MIN)}
allrows.sort(key=lambda r: (order.get(r["mineral"], 99), int(r["anio"])))

with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["mineral","anio","hhi","cobertura_pct","lider","metodo","nota"])
    w.writeheader()
    for r in allrows:
        w.writerow({k: r.get(k, "") for k in ["mineral","anio","hhi","cobertura_pct","lider","metodo","nota"]})

print(f"Escrito: {f_out}  ({len(allrows)} filas: {len(rows_new)} nuevas 2004-2020 + {len(rows_keep)} 2021-2023)")
print("\nCobertura por mineral (anios 2004-2023 con HHI):")
by = defaultdict(list)
for r in allrows: by[r["mineral"]].append(int(r["anio"]))
for m in MIN:
    ys = sorted(by[m]); miss = [y for y in range(2004,2024) if y not in ys]
    print(f"  {m:10s} n={len(ys):2d}  huecos: {miss if miss else 'ninguno'}")
print("\nSerie cobre (verif. continuidad 2020->2021):")
for r in allrows:
    if r["mineral"]=="cobre": print(f"  {r['anio']} hhi={r['hhi']:>6} cob={r['cobertura_pct']}%  [{r['metodo']}]")
