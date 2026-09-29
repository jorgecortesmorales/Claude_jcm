# -*- coding: utf-8 -*-
"""Encadenamiento por eslabon (L1/L2/L3) y mineral, DOS variantes:
Ghosh-Rasmussen (intensidad, barras) y extraccion hipotetica HEM (peso %, linea).
Small-multiples, corte 2018. Salida: hem_eslabones_2variantes.png (+ ruta scratchpad).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
AZUL, ROJO, GRIS = "#4f86b3", "#c0603f", "#9a9a9a"

def load(fn):
    return list(csv.DictReader(open(os.path.join(PROC, fn), encoding="utf-8-sig")))

ras = {(r["mineral"], r["eslabon"]): r for r in load("mip_encadenamientos_eslabones.csv") if r["anio"] == "2018"}
hem = {(r["mineral"], r["eslabon"]): r for r in load("mip_hem_eslabones.csv") if r["anio"] == "2018"}

NAME = {"plomo-zinc": "Plomo-zinc", "silice": "Sílice", "cobre": "Cobre", "oro": "Oro",
        "plata": "Plata", "fluorita": "Fluorita", "grafito": "Grafito",
        "manganeso": "Manganeso", "barita": "Barita"}
ORDER = ["cobre", "oro", "plata", "plomo-zinc", "manganeso", "silice", "grafito", "fluorita", "barita"]
ESL = ["L1", "L2", "L3"]
ESLLBL = {"L1": "L1\nextrac.", "L2": "L2\nrefin.", "L3": "L3\nsemis"}

def fnum(d, key):
    v = d.get(key, "") if d else ""
    try: return float(v)
    except: return None

fig, axes = plt.subplots(3, 3, figsize=(11.5, 9.2))
for ax, mn in zip(axes.flat, ORDER):
    xs = range(len(ESL))
    # barras Rasmussen (eje izq)
    rvals, rcols, hatches = [], [], []
    for e in ESL:
        r = ras.get((mn, e)); v = fnum(r, "forward_rasmussen")
        rvals.append(v if v is not None else 0)
        atr = (r or {}).get("atribuible", "")
        rcols.append(AZUL if v is not None else "none")
        hatches.append("" if atr == "si" else ("//" if atr == "comp" else "xx"))
    bars = ax.bar(xs, rvals, width=0.62, color=AZUL, edgecolor="#22374a", linewidth=0.6, zorder=2)
    for b, h in zip(bars, hatches):
        if h: b.set_hatch(h)
    ax.axhline(1.0, color=GRIS, ls="--", lw=1, zorder=1)
    ax.set_ylim(0, 2.05); ax.set_xticks(list(xs)); ax.set_xticklabels([ESLLBL[e] for e in ESL], fontsize=8)
    ax.set_title(NAME[mn], fontsize=11, fontweight="bold")
    ax.spines[["top"]].set_visible(False)
    for b, v in zip(bars, rvals):
        if v: ax.text(b.get_x()+b.get_width()/2, v+0.03, f"{v:.2f}", ha="center", fontsize=7.3, color="#22374a")
    # linea HEM (eje der)
    ax2 = ax.twinx()
    hvals = [fnum(hem.get((mn, e)), "hem_forward_pct") for e in ESL]
    px = [i for i, v in enumerate(hvals) if v is not None]
    py = [hvals[i] for i in px]
    ax2.plot(px, py, "-o", color=ROJO, lw=1.8, ms=5, zorder=3)
    for i, v in zip(px, py):
        ax2.annotate(f"{v:.3f}", (i, v), xytext=(0, 6), textcoords="offset points",
                     ha="center", fontsize=7, color=ROJO)
    ax2.set_ylim(0, 0.33); ax2.spines[["top"]].set_visible(False)
    ax2.tick_params(axis="y", colors=ROJO, labelsize=7.5)
    ax.tick_params(axis="y", colors=AZUL, labelsize=7.5)

fig.suptitle("Encadenamiento hacia adelante por eslabón y mineral, 2018 — dos variantes",
             fontsize=13, fontweight="bold", y=0.995)
leg = [Patch(facecolor=AZUL, edgecolor="#22374a", label="Ghosh-Rasmussen (intensidad, eje izq., línea = media 1)"),
       Line2D([0], [0], color=ROJO, marker="o", lw=1.8, label="HEM hacia adelante (peso, % del VBP, eje der.)"),
       Patch(facecolor="white", edgecolor="#22374a", hatch="//", label="clase compartida entre minerales"),
       Patch(facecolor="white", edgecolor="#22374a", hatch="xx", label="clase agregada no atribuible")]
fig.legend(handles=leg, loc="lower center", ncol=2, frameon=False, fontsize=9, bbox_to_anchor=(0.5, -0.01))
fig.text(0.5, 0.035, "Eje izquierdo (azul): Ghosh-Rasmussen, media de la economía = 1. Eje derecho (rojo): HEM, % del VBP nacional que se perdería al extraer las ventas de la clase.",
         ha="center", fontsize=7.8, color="#555")
fig.tight_layout(rect=[0, 0.06, 1, 0.98])
out = os.path.join(HERE, "hem_eslabones_2variantes.png")
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("ok ->", out)
