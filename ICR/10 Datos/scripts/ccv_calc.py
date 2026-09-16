# -*- coding: utf-8 -*-
"""Tarea 1 - CCV (coeficiente de captura de valor), paso 2: calculo de la serie.

CCV[mineral,anio] = valor unitario de exportacion E1 en frontera (USD/t, forma bruta)
                    / precio del producto refinado de referencia (USD/t, USGS).

Numerador: sum(valor_usd de fracciones E1) / sum(peso de esas fracciones, en t), de
           comercio_e1_valor_peso_comtrade_mx_1992_2025.csv (UN Comtrade, Mexico 484, X, Mundo).
           Peso = netWgt (kg); respaldo qty cuando qty_unit=8 (kg). Solo se agregan las
           fracciones que tienen peso (evita sesgar el valor unitario).
Denominador: precio_usd_t_nominal de precios_usgs_anual_empalmado.csv (USGS DS-140 / MCS /
           empalme Cochilco), por mineral-anio.

Un CCV bajo = la forma exportada en bruto captura poca parte del valor del producto de
referencia (rasgo de enclave). Caveats de interpretacion por grupo mineral en la memoria.
"""
import csv, os, sys

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
f_e1   = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade",
                      "comercio_e1_valor_peso_comtrade_mx_1992_2025.csv")
f_prec = os.path.join(BASE, "processed", "precios_usgs_anual_empalmado.csv")
f_out  = os.path.join(BASE, "processed", "ccv_serie.csv")

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
# grupo interpretativo del CCV (para memoria y salida)
GRUPO = {
 "cobre":"metal base", "plomo":"metal base", "zinc":"metal base",
 "oro":"metal precioso", "plata":"metal precioso",
 "barita":"no metalico/industrial", "fluorita":"no metalico/industrial",
 "grafito":"no metalico/industrial", "silice":"no metalico/industrial",
 "manganeso":"no metalico/industrial",
}
HS2MIN = {c: m for m, lst in E1.items() for c in lst}

# ---- numerador: valor y peso de E1 por (mineral, anio) ----
# dedup por (anio,hs): preferir fila con peso; si empatan, el mayor valor.
best = {}  # (anio,hs) -> (valor, peso_kg)
for r in csv.DictReader(open(f_e1, encoding="utf-8")):
    hs = r["hs"]; anio = int(r["anio"])
    if hs not in HS2MIN:
        continue
    val = float(r["valor_usd"] or 0)
    wt = r["peso_neto_kg"]
    wt = float(wt) if wt not in ("", None) else 0.0
    if wt == 0.0:  # respaldo: qty cuando la unidad es kg (codigo 8)
        if str(r.get("qty_unit")) == "8" and (r.get("qty") not in ("", None)):
            try: wt = float(r["qty"])
            except ValueError: wt = 0.0
    key = (anio, hs)
    cand = (val, wt)
    if key not in best:
        best[key] = cand
    else:
        ov, ow = best[key]
        # preferir la que tenga peso; luego mayor valor
        if (wt > 0) > (ow > 0) or (((wt > 0) == (ow > 0)) and val > ov):
            best[key] = cand

# agregar fracciones por mineral-anio (solo las que tienen peso)
num = {}  # (mineral, anio) -> (valor_con_peso, peso_kg, valor_total, n_frac_con_peso, n_frac_total)
for (anio, hs), (val, wt) in best.items():
    m = HS2MIN[hs]
    d = num.setdefault((m, anio), [0.0, 0.0, 0.0, 0, 0])
    d[2] += val; d[4] += 1
    if wt > 0:
        d[0] += val; d[1] += wt; d[3] += 1

# ---- denominador: precio USGS ----
prec = {}  # (mineral_lower, anio) -> precio_usd_t_nominal
for r in csv.DictReader(open(f_prec, encoding="utf-8-sig")):
    prec[(r["mineral"].strip().lower(), int(r["anio"]))] = float(r["precio_usd_t_nominal"])

# ---- respaldo ESPEJO para el numerador (huecos donde Mexico no reporto peso/export) ----
# (paso 1 de la ruta; ver scripts/ccv_fill_gaps.py). CIF -> posible sesgo al alza; se marca.
esp = {}  # (mineral, anio) -> (valor, peso_kg)
f_esp = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade",
                     "comercio_e1_espejo_huecos.csv")
if os.path.exists(f_esp):
    for r in csv.DictReader(open(f_esp, encoding="utf-8")):
        w = float(r["peso_neto_kg_espejo"] or 0)
        if w > 0:
            esp[(r["mineral"], int(r["anio"]))] = (float(r["valor_usd_espejo"] or 0), w)

# ---- construir serie ----
rows = []
for m in E1:
    for anio in range(1992, 2026):
        d = num.get((m, anio))
        p = prec.get((m, anio))
        uv = ""      # valor unitario exportacion USD/t
        ccv = ""
        nota = ""
        fuente = ""
        val_col = round(d[2], 2) if d else ""
        peso_col = ""
        if d and d[1] > 0:                         # 1) reporte propio con peso
            uv = d[0] / (d[1] / 1000.0)
            fuente = "propio"
            peso_col = round(d[1] / 1000.0, 3)
            if d[3] < d[4]:
                nota = f"valor unit. sobre {d[3]}/{d[4]} fracciones E1 con peso"
        elif (m, anio) in esp:                     # 2) respaldo por espejo
            ev, ew = esp[(m, anio)]
            uv = ev / (ew / 1000.0)
            fuente = "espejo"
            val_col = round(ev, 2); peso_col = round(ew / 1000.0, 3)
            nota = "numerador por ESPEJO (importaciones de socios desde Mexico; CIF, posible sesgo al alza)"
        else:                                      # 3) sin exportacion en bruto (cero estructural)
            nota = "sin exportacion E1 (no imputado)"
        if uv != "" and p:
            ccv = uv / p
        elif uv != "" and not p:
            nota = (nota + "; " if nota else "") + "sin precio USGS este anio"
        rows.append(dict(
            mineral=m, grupo_ccv=GRUPO[m], anio=anio,
            hs_e1=";".join(E1[m]),
            valor_export_e1_usd=val_col,
            peso_export_e1_t=peso_col,
            valor_unitario_export_usd_t=round(uv, 2) if uv != "" else "",
            precio_refinado_usgs_usd_t=round(p, 2) if p else "",
            ccv=round(ccv, 4) if ccv != "" else "",
            fuente_numerador=fuente,
            nota=nota,
        ))

rows.sort(key=lambda x: (x["mineral"], x["anio"]))
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

# ---- reporte ----
ok = [r for r in rows if r["ccv"] != ""]
print(f"Escrito: {f_out}")
print(f"Filas totales: {len(rows)}  |  con CCV calculado: {len(ok)}")
print("\nCobertura CCV por mineral (anios con dato / rango):")
for m in E1:
    ys = [r["anio"] for r in rows if r["mineral"] == m and r["ccv"] != ""]
    print(f"  {m:10s} n={len(ys):2d}  {min(ys) if ys else '-'}-{max(ys) if ys else '-'}")
print("\nCCV medio y rango por mineral (todos los anios con dato):")
for m in E1:
    vs = [float(r["ccv"]) for r in rows if r["mineral"] == m and r["ccv"] != ""]
    if vs:
        print(f"  {m:10s} [{GRUPO[m]:22s}] media={sum(vs)/len(vs):.3f}  min={min(vs):.3f}  max={max(vs):.3f}")
