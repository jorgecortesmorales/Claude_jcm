# -*- coding: utf-8 -*-
"""Comparacion internacional: las dos variantes del encadenamiento hacia adelante de la mineria
(Ghosh-Rasmussen, intensidad; HEM, peso), sector B07_08, corte 2018. Salida: vii5_hem_internacional.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.edgecolor": "#444", "axes.linewidth": 0.8})
AZUL, ROJO, GRIS = "#4f86b3", "#b04a3a", "#8a8a8a"

def load(fn):
    return list(csv.DictReader(open(os.path.join(PROC, fn), encoding="utf-8-sig")))

ras = {r["pais_nombre"]: float(r["forward_rasmussen"]) for r in load("icio_comparacion_mineria.csv")
       if r["anio"] == "2018" and r["sector"] == "B07_08"}
hemf = {r["pais_nombre"]: float(r["hem_forward_pct"]) for r in load("icio_hem_mineria.csv")
        if r["anio"] == "2018" and r["sector"] == "B07_08"}
hemt = {r["pais_nombre"]: float(r["hem_total_pct"]) for r in load("icio_hem_mineria.csv")
        if r["anio"] == "2018" and r["sector"] == "B07_08"}

fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.5, 4.7))
# Panel A: HEM total por pais
data = sorted(hemt.items(), key=lambda x: x[1])
labels = [d[0] for d in data]; vals = [d[1] for d in data]
cols = [ROJO if l == "Mexico" else AZUL for l in labels]
axA.barh(labels, vals, color=cols, edgecolor="#22374a", linewidth=0.6)
for i, v in enumerate(vals):
    axA.text(v + 0.08, i, f"{v:.2f}", va="center", fontsize=8.5)
axA.set_xlabel("HEM total de la minería (% del VBP doméstico, 2018)")
axA.set_xlim(0, 7.6); axA.set_title("Peso económico (extracción hipotética)", fontsize=10)
axA.spines[["top", "right"]].set_visible(False)
# Panel B: Rasmussen vs HEM forward
for p in ras:
    x = ras[p]; y = hemf.get(p)
    if y is None: continue
    c = ROJO if p == "Mexico" else "#2b6e4f"
    axB.scatter(x, y, s=48, color=c, edgecolor="#22374a", zorder=3)
    axB.annotate(p, (x, y), xytext=(5, 3), textcoords="offset points", fontsize=8.3)
axB.axvline(1.0, color=GRIS, lw=1.0, ls="--")
axB.set_xlabel("Ghosh-Rasmussen hacia adelante (intensidad, media país = 1)")
axB.set_ylabel("HEM hacia adelante (peso, % del VBP)")
axB.set_title("Intensidad vs. peso", fontsize=10)
axB.spines[["top", "right"]].set_visible(False)
fig.suptitle("Comparación internacional de la minería (B07_08), 2018 — dos variantes del encadenamiento",
             fontsize=12, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.96])
out = os.path.join(HERE, "vii5_hem_internacional.png")
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("ok ->", out)
