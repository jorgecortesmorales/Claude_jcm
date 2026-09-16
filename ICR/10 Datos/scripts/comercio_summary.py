# -*- coding: utf-8 -*-
"""Resumen de posicion por etapa (espejo exportar-bruto / importar-procesado) + concordancia."""
import csv, os, sys
from collections import defaultdict

proc = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
etapa_f = os.path.join(proc, "comercio_por_etapa.csv")
rows = list(csv.DictReader(open(etapa_f, encoding="utf-8")))

# indexar: (mineral,anio,flujo,etapa) -> valor ; y concordancia (mineral,etapa)->hs
val = defaultdict(float); conc = {}
minerales = []
for r in rows:
    m, a, fl, e = r["mineral"], int(r["anio"]), r["flujo"], r["etapa"]
    val[(m, a, fl, e)] += float(r["valor_usd"])
    conc[(m, e)] = r["hs"]
    if m not in minerales: minerales.append(m)
etapas_de = defaultdict(list)
for (m, e) in conc:
    if e not in etapas_de[m]: etapas_de[m].append(e)

years = sorted({int(r["anio"]) for r in rows})

def is_e1(e): return e.startswith("E1")

# 1) concordancia CSV (revisable)
f_conc = os.path.join(proc, "concordancia_hs_etapa.csv")
with open(f_conc, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["mineral", "etapa", "fracciones_hs"])
    for m in minerales:
        for e in etapas_de[m]:
            w.writerow([m, e, conc[(m, e)]])

# 2) resumen por mineral-anio: totales, share crudo vs procesado, espejo
summary = []
for m in minerales:
    for a in years:
        X = {e: val[(m, a, "Exportacion", e)] for e in etapas_de[m]}
        Mi = {e: val[(m, a, "Importacion", e)] for e in etapas_de[m]}
        tx, tm = sum(X.values()), sum(Mi.values())
        if tx + tm == 0: continue
        x_e1 = sum(v for e, v in X.items() if is_e1(e))
        x_proc = tx - x_e1
        m_e1 = sum(v for e, v in Mi.items() if is_e1(e))
        m_proc = tm - m_e1
        summary.append(dict(
            mineral=m, anio=a,
            X_total_musd=round(tx/1e6, 2), M_total_musd=round(tm/1e6, 2),
            saldo_neto_musd=round((tx - tm)/1e6, 2),
            X_share_crudo=round(x_e1/tx, 3) if tx else None,
            X_share_procesado=round(x_proc/tx, 3) if tx else None,
            M_share_procesado=round(m_proc/tm, 3) if tm else None,
        ))
f_sum = os.path.join(proc, "comercio_posicion_resumen.csv")
with open(f_sum, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(summary[0].keys())); w.writeheader(); w.writerows(summary)

# validacion
for f in (f_conc, f_sum, etapa_f):
    rr = list(csv.reader(open(f, encoding="utf-8")))
    nc = len(rr[0]); bad = sum(1 for x in rr if len(x) != nc)
    print(f"{os.path.basename(f)}: {len(rr)-1} filas, {nc} cols, malformadas={bad}")

print("\n=== Posicion por mineral (promedio 2018-2023, %) ===")
print(f"{'mineral':26s} {'Xcrudo':>7s} {'Xproc':>7s} {'Mproc':>7s}  saldo(MUSD, prom)")
for m in minerales:
    sub = [s for s in summary if s["mineral"] == m and 2018 <= s["anio"] <= 2023]
    if not sub: continue
    xc = sum(s["X_share_crudo"] or 0 for s in sub)/len(sub)
    xp = sum(s["X_share_procesado"] or 0 for s in sub)/len(sub)
    mp = sum(s["M_share_procesado"] or 0 for s in sub)/len(sub)
    sal = sum(s["saldo_neto_musd"] for s in sub)/len(sub)
    print(f"{m:26s} {xc*100:6.0f}% {xp*100:6.0f}% {mp*100:6.0f}%  {sal:12,.0f}")
print("\nEscritos:\n ", f_conc, "\n ", f_sum)
