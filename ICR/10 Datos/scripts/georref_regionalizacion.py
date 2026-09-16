# -*- coding: utf-8 -*-
"""Paso 8 - Regionalizacion descriptiva de la cadena por mineral.

Objetivo del paso 8 (ruta): dimension regional del encadenamiento ("Ghosh por estado").
LIMITE DE DATOS: una regionalizacion nonsurvey completa (SLQ/FLQ/CHARM) de la MIP
nacional requiere una matriz sector x estado (PIB estatal por actividad, PIBE de INEGI),
que INEGI solo expone via un descargador interactivo (119 tabulados) -> no accesible por
script. Se DECLARA ese limite (no se imputa). Lo que SI es riguroso con los datos propios:

  1. Concentracion geografica de la extraccion (Herfindahl espacial de las cuotas por
     estado) por mineral, 2024 -> que tan localizada esta la extraccion.
  2. Co-localizacion extraccion<->transformacion: el nodo de transformacion (E2) esta
     en el mismo estado que la extraccion lider? -> mide integracion local vs. la
     "deslocalizacion" del valor agregado (dimension regional del enclave).
  3. Tipologia por estado.

Fuente: processed/georref_extraccion_mineral_estado_cuantitativo.csv (SGM Anuario 2025,
por mineral x estado, 2024) + georref_transformacion_nodos.csv.
Salida: processed/georref_regionalizacion.csv
"""
import csv, os
from collections import defaultdict

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
ext = list(csv.DictReader(open(os.path.join(BASE, "georref_extraccion_mineral_estado_cuantitativo.csv"), encoding="utf-8")))
nod = list(csv.DictReader(open(os.path.join(BASE, "georref_transformacion_nodos.csv"), encoding="utf-8")))

MIN = ["cobre","plomo","zinc","manganeso","oro","plata","fluorita","grafito","barita","silice"]

# nodo de transformacion E2 por mineral (acepta etiquetas combinadas oro-plata / plomo-zinc)
def nodos_e2(m):
    keys = {m}
    if m in ("oro","plata"): keys.add("oro-plata")
    if m in ("plomo","zinc"): keys.add("plomo-zinc")
    out = []
    for x in nod:
        if x["mineral"] in keys and x["eslabon"].startswith("E2"):
            out.append((x["estado"], x["eslabon"]))
    if not out:  # sin E2: registrar el eslabon disponible (usuario/E3/E4)
        for x in nod:
            if x["mineral"] in keys:
                out.append((x["estado"], x["eslabon"]))
    return out

def norm(s): return (s or "").strip().lower().replace("é","e").replace("í","i").replace("á","a").replace("ó","o").replace("ú","u")

rows = []
for m in MIN:
    er = [x for x in ext if x["mineral"] == m]
    sh = [float(x["share_2024_pct"] or 0) for x in er]
    hhi = round(sum(s*s for s in sh))
    lead = max(er, key=lambda z: float(z["share_2024_pct"] or 0))
    lead_est = lead["estado"]; lead_sh = round(float(lead["share_2024_pct"]))
    e2 = nodos_e2(m)
    e2_estados = sorted(set(e for e, _ in e2))
    tiene_e2 = any(es.startswith("E2") for _, es in e2)
    colocal = "si" if any(norm(e) == norm(lead_est) for e in e2_estados) and tiene_e2 else "no"
    rows.append(dict(
        mineral=m, hhi_geografico=hhi, n_estados=len(er),
        estado_extraccion_lider=lead_est, share_lider_pct=lead_sh,
        estados_transformacion="; ".join(e2_estados) if e2_estados else "(ninguno)",
        tiene_eslabon_E2="si" if tiene_e2 else "no",
        colocalizado_extraccion_E2=colocal,
    ))

f_out = os.path.join(BASE, "georref_regionalizacion.csv")
fields = list(rows[0].keys())
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(rows)

print("mineral      HHI_geo  lider(estado, %)          E2 en          coloc?")
for r in rows:
    print(f"{r['mineral']:11s} {r['hhi_geografico']:6d}  {r['estado_extraccion_lider']:14s} {r['share_lider_pct']:3d}%  {r['estados_transformacion'][:26]:26s} {r['colocalizado_extraccion_E2']}")
print(f"\nEscrito: {f_out}  ({len(rows)} filas)")
n_coloc = sum(1 for r in rows if r["colocalizado_extraccion_E2"] == "si")
print(f"Co-localizados extraccion<->E2: {n_coloc}/10  (resto: valor agregado deslocalizado a otros estados o ausente)")
