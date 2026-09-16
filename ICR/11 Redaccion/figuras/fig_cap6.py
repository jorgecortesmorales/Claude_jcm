# -*- coding: utf-8 -*-
"""Figuras del Capitulo VI (Encadenamientos productivos)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.edgecolor": "#444", "axes.linewidth": 0.8})
AZUL, ROJO, GRIS = "#4f86b3", "#b04a3a", "#8a8a8a"
CAP = "−"  # no usado; placeholder

def cargar(fn):
    with open(os.path.join(PROC, fn), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

NOMBRE = {"plomo-zinc": "Plomo-zinc", "silice": "Sílice", "cobre": "Cobre",
          "oro": "Oro", "plata": "Plata", "fluorita": "Fluorita",
          "grafito": "Grafito", "manganeso": "Manganeso", "barita": "Barita",
          "plomo": "Plomo", "zinc": "Zinc"}

# ---------- VI.1: Ghosh hacia adelante por mineral, 2018 ----------
def fig1():
    rows = [r for r in cargar("mip_encadenamientos_minerales.csv") if r["anio"] == "2018"]
    data = sorted(((NOMBRE[r["mineral"]], float(r["forward_rasmussen"])) for r in rows),
                  key=lambda x: x[1])
    labels = [d[0] for d in data]; vals = [d[1] for d in data]
    cols = [AZUL if v >= 1 else GRIS for v in vals]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.barh(labels, vals, color=cols, edgecolor="#2b3a46", linewidth=0.6)
    ax.axvline(1.0, color=ROJO, lw=1.3, ls="--")
    ax.text(1.01, -0.6, "media de la economía = 1", color=ROJO, fontsize=8.5, va="top")
    for i, v in enumerate(vals):
        ax.text(v + 0.02, i, f"{v:.2f}", va="center", fontsize=8.5)
    ax.set_xlabel("Índice de Ghosh-Rasmussen hacia adelante (2018)")
    ax.set_xlim(0, 2.15)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "vi1_ghosh_mineral_2018.png"), dpi=200,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ---------- VI.2: encadenamiento por eslabon (L1/L2/L3) ----------
def fig2():
    rows = [r for r in cargar("mip_encadenamientos_eslabones.csv") if r["anio"] == "2018"]
    d = defaultdict(dict)
    for r in rows:
        v = r["forward_rasmussen"]
        d[r["mineral"]][r["eslabon"]] = float(v) if v else None
    orden = ["cobre", "manganeso", "oro", "plata", "plomo-zinc"]
    L = ["L1", "L2", "L3"]
    Lname = {"L1": "L1 extracción", "L2": "L2 refinación", "L3": "L3 semimanufactura"}
    colL = {"L1": AZUL, "L2": "#7fabcb", "L3": "#cfe0ec"}
    fig, ax = plt.subplots(figsize=(9.5, 4.4))
    w = 0.26
    for j, esl in enumerate(L):
        xs = [i + (j - 1) * w for i in range(len(orden))]
        ys = [d[m].get(esl) or 0 for m in orden]
        bars = ax.bar(xs, ys, w, label=Lname[esl], color=colL[esl],
                      edgecolor="#2b3a46", linewidth=0.6)
        for x, y, m in zip(xs, ys, orden):
            atrib = next((r["atribuible"] for r in rows if r["mineral"] == m and r["eslabon"] == esl), "")
            if y:
                ax.text(x, y + 0.02, f"{y:.2f}", ha="center", fontsize=7.3,
                        color="#333" if atrib == "si" else "#999")
    ax.axhline(1.0, color=ROJO, lw=1.2, ls="--")
    ax.set_xticks(range(len(orden)))
    ax.set_xticklabels([NOMBRE[m] for m in orden])
    ax.set_ylabel("Ghosh-Rasmussen hacia adelante (2018)")
    ax.set_ylim(0, 1.75)
    ax.legend(frameon=False, fontsize=8.5, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.1))
    ax.spines[["top", "right"]].set_visible(False)
    ax.text(0.0, -0.34, "Etiquetas en gris: clase de transformación no atribuible al mineral (agregada).",
            transform=ax.transAxes, fontsize=7.2, color="#777")
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "vi2_ghosh_eslabon_2018.png"), dpi=200,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ---------- VI.3: serie CCV metales base ----------
def fig3():
    g = defaultdict(list)
    for r in cargar("ccv_serie.csv"):
        try:
            g[r["mineral"]].append((int(r["anio"]), float(r["ccv"])))
        except Exception:
            pass
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    estilos = {"cobre": (AZUL, "o"), "zinc": ("#2b6e4f", "s")}
    for m, (c, mk) in estilos.items():
        s = sorted(g[m])
        ax.plot([a for a, _ in s], [v for _, v in s], marker=mk, ms=3.5,
                color=c, lw=1.6, label=NOMBRE[m])
    ax.axhspan(0.22, 0.30, color=GRIS, alpha=0.15)
    ax.text(1992.5, 0.315, "banda estable ≈ 0.22–0.30", fontsize=8, color="#555")
    ax.set_ylabel("Coeficiente de captura de valor (CCV)")
    ax.set_xlabel("Año")
    ax.set_ylim(0, 0.55)
    ax.legend(frameon=False, fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "vi3_ccv_metales_base.png"), dpi=200,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)

# ---------- VI.4: dispersion atras vs adelante 2018 ----------
def fig4():
    rows = [r for r in cargar("mip_encadenamientos_minerales.csv") if r["anio"] == "2018"]
    fig, ax = plt.subplots(figsize=(7.8, 5.6))
    for r in rows:
        x = float(r["backward_rasmussen"]); y = float(r["forward_rasmussen"])
        ax.scatter(x, y, s=42, color=AZUL, edgecolor="#2b3a46", zorder=3)
        ax.annotate(NOMBRE[r["mineral"]], (x, y), xytext=(5, 4),
                    textcoords="offset points", fontsize=8.5)
    ax.axhline(1.0, color=ROJO, lw=1.0, ls="--")
    ax.axvline(1.0, color=ROJO, lw=1.0, ls="--")
    ax.set_xlabel("Encadenamiento hacia atrás (Uj, Rasmussen)")
    ax.set_ylabel("Encadenamiento hacia adelante (Ui, Rasmussen)")
    ax.set_xlim(0.85, 1.10); ax.set_ylim(0.55, 2.05)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "vi4_dispersion_2018.png"), dpi=200,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)

for f in (fig1, fig2, fig3, fig4):
    f(); print("ok", f.__name__)
