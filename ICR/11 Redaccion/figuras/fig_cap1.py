# -*- coding: utf-8 -*-
"""Figura del Capitulo I: peso del bloque en las exportaciones (1992-2024)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
AZUL, ROJO = "#4f86b3", "#b04a3a"

rows = []
with open(os.path.join(PROC, "peso_bloque_hist_exportaciones.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        try: rows.append((int(r["anio"]), float(r["share_bloque_pct"])))
        except Exception: pass
rows.sort()
xs = [a for a, _ in rows]; ys = [s for _, s in rows]
fig, ax = plt.subplots(figsize=(9.5, 4.0))
ax.fill_between(xs, ys, color=AZUL, alpha=0.15)
ax.plot(xs, ys, color=AZUL, lw=2, marker="o", ms=3)
pa, pv = max(rows, key=lambda x: x[1])
ax.scatter([pa], [pv], color=ROJO, zorder=4)
ax.annotate(f"pico {pv:.1f} % ({pa})", (pa, pv), xytext=(pa+1, pv-0.05),
            fontsize=9, color=ROJO)
ax.set_ylabel("Participación del bloque en las\nexportaciones totales de México (%)")
ax.set_xlabel("Año"); ax.set_ylim(0, 6)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "i1_peso_exportaciones.png"), dpi=200, bbox_inches="tight", facecolor="white")
print("ok peso exportaciones")
