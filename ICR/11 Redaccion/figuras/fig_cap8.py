# -*- coding: utf-8 -*-
"""Figuras del Capitulo VIII (Caracterizacion integrada y tipologia)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import os

HERE = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.edgecolor": "#444", "axes.linewidth": 0.8})
TIPO_COL = {"A": "#2b6e4f", "B": "#4f86b3", "C": "#c98a2b", "D": "#b04a3a"}
TIPO_LBL = {"A": "A: cadena desarrollada", "B": "B: truncada en refinado",
            "C": "C: usuario con eslabón importado", "D": "D: exportación en bruto"}

# mineral: (HHI reciente, Ghosh 2018, tipo, eslabon alcanzado 1..4)
M = {
 "Manganeso": (10000, 1.54, "A", 2), "Fluorita": (10000, 1.31, "A", 2),
 "Cobre": (3557, 1.34, "B", 2), "Oro": (429, 1.22, "B", 2),
 "Plata": (1147, 1.17, "B", 2), "Plomo": (2465, 0.71, "B", 1),
 "Zinc": (1683, 0.71, "B", 1), "Grafito": (10000, 1.71, "C", 1),
 "Sílice": (9742, 1.92, "C", 1), "Barita": (605, 0.64, "D", 1),
}

def fig1():
    fig, ax = plt.subplots(figsize=(8.6, 5.8))
    for m, (hhi, gh, tp, _) in M.items():
        ax.scatter(hhi, gh, s=80, color=TIPO_COL[tp], edgecolor="#2b3a46", zorder=3)
        ax.annotate(m, (hhi, gh), xytext=(6, 4), textcoords="offset points", fontsize=8.7)
    ax.axhline(1.0, color="#999", ls="--", lw=1)
    ax.text(200, 1.02, "media de la economía", fontsize=7.5, color="#999")
    ax.set_xlabel("Concentración extractiva (HHI, año reciente)")
    ax.set_ylabel("Encadenamiento hacia adelante (Ghosh-Rasmussen, 2018)")
    ax.set_xlim(-300, 10800); ax.set_ylim(0.4, 2.05)
    ax.legend(handles=[Patch(facecolor=TIPO_COL[t], label=TIPO_LBL[t]) for t in "ABCD"],
              frameon=False, fontsize=8, loc="lower left")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "viii1_plano_tipologia.png"), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

def fig2():
    # orden por tipo y eslabon alcanzado
    orden = sorted(M.items(), key=lambda kv: ("ABCD".index(kv[1][2]), -kv[1][3], kv[0]))
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    esl_lbl = ["L0\nrecurso", "L1\nextracción", "L2\nrefinación", "L3\nsemis", "L4\nmanufactura"]
    for i, (m, (_, _, tp, reach)) in enumerate(orden):
        y = len(orden) - 1 - i
        ax.plot([0, 4], [y, y], color="#ddd", lw=8, solid_capstyle="round", zorder=1)
        ax.plot([0, reach], [y, y], color=TIPO_COL[tp], lw=8, solid_capstyle="round", zorder=2)
        ax.scatter([reach], [y], marker="|", s=400, color="#b04a3a", zorder=4, linewidths=2.2)
        ax.text(-0.15, y, m, ha="right", va="center", fontsize=9)
        ax.text(4.15, y, f"tipo {tp}", ha="left", va="center", fontsize=8, color=TIPO_COL[tp])
    ax.set_xticks(range(5)); ax.set_xticklabels(esl_lbl, fontsize=8.5)
    ax.set_yticks([]); ax.set_xlim(-1.4, 4.9); ax.set_ylim(-0.6, len(orden)-0.4)
    for s in ["top", "right", "left"]: ax.spines[s].set_visible(False)
    ax.text(2, len(orden)-0.15, "La barra llega hasta el último eslabón donde México agrega valor; la marca roja es el punto de ruptura.",
            ha="center", fontsize=7.6, color="#666")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "viii2_punto_ruptura.png"), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

for f in (fig1, fig2):
    f(); print("ok", f.__name__)
