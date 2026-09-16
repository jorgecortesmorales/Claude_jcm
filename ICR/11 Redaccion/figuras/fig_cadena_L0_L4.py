# -*- coding: utf-8 -*-
"""Ilustracion III.1 — esquema conceptual de la cadena de valor L0-L4."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

HERE = os.path.dirname(os.path.abspath(__file__))

esl = [
    ("L0", "Recurso\nen el suelo", "Dotacion / reservas"),
    ("L1", "Extraccion\ny beneficio", "Mina -> concentrado"),
    ("L2", "Fundicion-refinacion\no quimica primaria", "Concentrado -> metal /\nquimico basico"),
    ("L3", "Semimanufactura", "Laminados, aleaciones,\nintermedios"),
    ("L4", "Manufactura\nfinal y uso", "Producto de uso final"),
]
etapas = ["", "E1", "E2", "E3", "E4"]

fig, ax = plt.subplots(figsize=(11, 3.4))
ax.set_xlim(0, 5); ax.set_ylim(0, 3); ax.axis("off")

# gradiente de color (valor creciente)
cols = ["#e8eef3", "#cfe0ec", "#a9c8de", "#7fabcb", "#4f86b3"]
for i, (code, name, desc) in enumerate(esl):
    x = i + 0.06
    box = FancyBboxPatch((x, 1.15), 0.88, 1.15,
                         boxstyle="round,pad=0.02,rounding_size=0.06",
                         linewidth=1.1, edgecolor="#2b3a46", facecolor=cols[i])
    ax.add_patch(box)
    tcol = "#0d1b26" if i < 3 else "white"
    ax.text(x + 0.44, 1.98, code, ha="center", va="center",
            fontsize=13, fontweight="bold", color=tcol)
    ax.text(x + 0.44, 1.55, name, ha="center", va="center",
            fontsize=8.3, color=tcol)
    ax.text(x + 0.44, 0.86, desc, ha="center", va="top",
            fontsize=7.2, color="#3a3a3a")
    if etapas[i]:
        ax.text(x + 0.44, 2.42, etapas[i], ha="center", va="center",
                fontsize=8, style="italic", color="#6a6a6a")
    if i < 4:
        ar = FancyArrowPatch((x + 0.9, 1.72), (x + 1.04, 1.72),
                             arrowstyle="-|>", mutation_scale=13,
                             linewidth=1.3, color="#2b3a46")
        ax.add_patch(ar)

ax.annotate("", xy=(4.94, 0.42), xytext=(0.06, 0.42),
            arrowprops=dict(arrowstyle="-|>", color="#b04a3a", lw=1.6))
ax.text(2.5, 0.20, "valor por unidad fisica creciente",
        ha="center", va="center", fontsize=8.5, color="#b04a3a", style="italic")
ax.text(0.06, 2.72, "Etapas comerciales E1–E4  ≙  eslabones L1–L4",
        ha="left", va="center", fontsize=7.6, color="#6a6a6a")

fig.tight_layout(pad=0.4)
out = os.path.join(HERE, "cadena_L0_L4.png")
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("guardado:", out)
