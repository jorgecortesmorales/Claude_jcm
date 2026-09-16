# -*- coding: utf-8 -*-
"""Figuras del Capitulo V (Estructura empresarial): HHI."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.edgecolor": "#444", "axes.linewidth": 0.8})
AZUL, ROJO, GRIS, VERDE = "#4f86b3", "#b04a3a", "#8a8a8a", "#2b6e4f"
NOMBRE = {"plomo": "Plomo", "silice": "Sílice", "cobre": "Cobre", "oro": "Oro",
          "plata": "Plata", "fluorita": "Fluorita", "grafito": "Grafito",
          "manganeso": "Manganeso", "barita": "Barita", "zinc": "Zinc"}

def cargar():
    d = defaultdict(dict); lider = {}
    with open(os.path.join(PROC, "hhi_consolidado.csv"), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            try: d[r["mineral"]][int(r["anio"])] = float(r["hhi"])
            except Exception: pass
            if r.get("lider"): lider[r["mineral"]] = r["lider"]
    return d, lider

D, LIDER = cargar()

# ---- V.1: HHI por mineral, dato mas reciente ----
def fig1():
    latest = {}
    for m, s in D.items():
        y = max(s); latest[m] = (y, s[y])
    data = sorted(((NOMBRE[m], v[1], v[0]) for m, v in latest.items()), key=lambda x: x[1])
    labels = [f"{d[0]} ({d[2]})" for d in data]; vals = [d[1] for d in data]
    def col(v): return ROJO if v >= 2500 else (AZUL if v >= 1500 else GRIS)
    fig, ax = plt.subplots(figsize=(9, 4.6))
    ax.barh(labels, vals, color=[col(v) for v in vals], edgecolor="#2b3a46", linewidth=0.6)
    for x in (1500, 2500):
        ax.axvline(x, color="#999", lw=1.0, ls=":")
    ax.text(1500, len(vals)-0.3, " moderada", fontsize=7.5, color="#777", rotation=90, va="top")
    ax.text(2500, len(vals)-0.3, " alta", fontsize=7.5, color="#777", rotation=90, va="top")
    for i, v in enumerate(vals):
        ax.text(v + 90, i, f"{v:.0f}", va="center", fontsize=8)
    ax.set_xlabel("Índice HHI (año más reciente con dato entre paréntesis)")
    ax.set_xlim(0, 11200)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "v1_hhi_mineral.png"), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ---- V.2: evolucion HHI seleccionados ----
def fig2():
    sel = {"barita": (ROJO, "o"), "cobre": (AZUL, "s"), "fluorita": (VERDE, "^"),
           "oro": ("#7a5aa8", "D"), "plata": ("#c98a2b", "v")}
    fig, ax = plt.subplots(figsize=(9.5, 4.4))
    for m, (c, mk) in sel.items():
        s = sorted((y, v) for y, v in D[m].items() if 2004 <= y <= 2024)
        ax.plot([y for y, _ in s], [v for _, v in s], marker=mk, ms=4, color=c, lw=1.5, label=NOMBRE[m])
    ax.axhline(10000, color="#bbb", lw=0.8, ls="--")
    ax.text(2004, 10050, "monopolio (10 000)", fontsize=7.5, color="#999", va="bottom")
    ax.set_ylabel("Índice HHI")
    ax.set_xlabel("Año")
    ax.set_ylim(0, 10800)
    ax.legend(frameon=False, fontsize=8.5, ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.12))
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "v2_hhi_evolucion.png"), dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

for f in (fig1, fig2):
    f(); print("ok", f.__name__)
