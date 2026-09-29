# -*- coding: utf-8 -*-
"""Ilustracion VIII.5 — extraccion hipotetica (HEM) de la mineria por entidad, 2018."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
AZUL, AZULC = "#4f86b3", "#b8d0e3"

ACC = {"San Luis Potosi": "San Luis Potosí", "Nuevo Leon": "Nuevo León",
       "Mexico": "México", "Michoacan": "Michoacán", "Queretaro": "Querétaro",
       "Yucatan": "Yucatán", "Ciudad de Mexico": "Ciudad de México"}

rows = list(csv.DictReader(open(os.path.join(PROC, "hem_estatal_mineria.csv"), encoding="utf-8-sig")))
for r in rows:
    r["b"] = float(r["hem_backward_pct"]); r["f"] = float(r["hem_forward_pct"])
    r["t"] = float(r["hem_total_pct"])
rows.sort(key=lambda r: -r["t"])
top = rows[:12][::-1]
labels = [ACC.get(r["estado"], r["estado"]) for r in top]

fig, ax = plt.subplots(figsize=(9, 5.0))
ys = range(len(top))
fwd = [r["f"] for r in top]; bwd = [r["b"] for r in top]
ax.barh(ys, fwd, color=AZUL, edgecolor="#2b3a46", linewidth=0.5, label="Hacia adelante")
ax.barh(ys, bwd, left=fwd, color=AZULC, edgecolor="#2b3a46", linewidth=0.5, label="Hacia atrás")
for i, r in enumerate(top):
    ax.text(r["t"] + 0.006, i, f"{r['t']:.3f}", va="center", fontsize=8)
ax.set_yticks(list(ys)); ax.set_yticklabels(labels)
ax.set_xlabel("Extracción hipotética de la minería (% del VBP birregional, 2018)")
ax.set_xlim(0, 0.58)
ax.legend(frameon=False, fontsize=8.5, loc="lower right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "viii5_hem_estatal.png"), dpi=200, bbox_inches="tight", facecolor="white")
print("ok hem estatal")
