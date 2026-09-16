# -*- coding: utf-8 -*-
"""Figuras del Capitulo VII (Insercion en las cadenas de valor globales)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.edgecolor": "#444", "axes.linewidth": 0.8})
AZUL, ROJO, GRIS, VERDE, MOR = "#4f86b3", "#b04a3a", "#8a8a8a", "#2b6e4f", "#7a5aa8"

# ---- series de comercio ----
def serie_crudo():
    tot = defaultdict(lambda: [0.0, 0.0])
    with open(os.path.join(PROC, "comercio_posicion_1992_2024.csv"), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            try:
                a = int(r["anio"]); tot[a][0] += float(r["X_total_usd"]); tot[a][1] += float(r["X_crudo_usd"])
            except Exception: pass
    return {a: v[1]/v[0] for a, v in tot.items() if v[0] > 0}

def serie_cobre_crudo():
    s = {}
    with open(os.path.join(PROC, "comercio_posicion_1992_2024.csv"), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["mineral"] == "cobre":
                try: s[int(r["anio"])] = float(r["X_crudo_usd"])/float(r["X_total_usd"])
                except Exception: pass
    return s

def serie_china():
    d = defaultdict(lambda: [0.0, 0.0])
    with open(os.path.join(PROC, "comercio_destinos_serie_resumen.csv"), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            try:
                a = int(r["anio"]); v = float(r["valor_total_usd"]); sc = float(r.get("share_china") or 0)
                d[a][0] += v; d[a][1] += v*sc
            except Exception: pass
    return {a: v[1]/v[0] for a, v in d.items() if v[0] > 0}

def fig1():
    cr = serie_crudo(); cu = serie_cobre_crudo()
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    xs = sorted(cr)
    ax.plot(xs, [cr[a] for a in xs], color=AZUL, lw=2, marker="o", ms=3, label="Bloque de 10 minerales")
    xc = sorted(cu)
    ax.plot(xc, [cu[a] for a in xc], color=ROJO, lw=1.6, ls="--", marker="s", ms=3, label="Cobre")
    ax.set_ylabel("Fracción de la exportación en bruto (etapa 1)")
    ax.set_xlabel("Año"); ax.set_ylim(0, 0.9)
    ax.legend(frameon=False, fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "vii1_crudo_share.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)

def fig2():
    ch = serie_china(); xs = sorted(ch)
    fig, ax = plt.subplots(figsize=(9.5, 4.0))
    ax.fill_between(xs, [ch[a] for a in xs], color=ROJO, alpha=0.15)
    ax.plot(xs, [ch[a] for a in xs], color=ROJO, lw=2, marker="o", ms=3)
    ax.set_ylabel("Participación de China en las exportaciones del bloque")
    ax.set_xlabel("Año"); ax.set_ylim(0, 0.45)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "vii2_china_share.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)

# ---- ICIO cross-section 2018 (sector B07_08) ----
GHOSH = {"China":1.53,"Suecia":1.27,"Finlandia":1.31,"Mexico":1.51,"Brasil":0.99,"Chile":0.73,"Australia":0.83,"Peru":0.62}
CRUDO = {"China":0.07,"Suecia":0.48,"Finlandia":0.45,"Mexico":0.38,"Brasil":0.82,"Chile":0.97,"Australia":0.77,"Peru":0.98}

def fig3():
    data = sorted(GHOSH.items(), key=lambda x: x[1])
    labels = [d[0] for d in data]; vals = [d[1] for d in data]
    cols = [ROJO if l == "Mexico" else (AZUL if v >= 1 else GRIS) for l, v in zip(labels, vals)]
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    ax.barh(labels, vals, color=cols, edgecolor="#2b3a46", linewidth=0.6)
    ax.axvline(1, color="#999", ls="--", lw=1)
    for i, v in enumerate(vals): ax.text(v+0.02, i, f"{v:.2f}", va="center", fontsize=8.5)
    ax.set_xlabel("Índice de Ghosh-Rasmussen hacia adelante (minería no energética, 2018)")
    ax.set_xlim(0, 1.85); ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "vii3_ghosh_paises.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)

def fig4():
    fig, ax = plt.subplots(figsize=(8.2, 5.6))
    for p in GHOSH:
        x, y = GHOSH[p], CRUDO[p]
        c = ROJO if p == "Mexico" else (VERDE if p == "China" else AZUL)
        ax.scatter(x, y, s=70, color=c, edgecolor="#2b3a46", zorder=3)
        ax.annotate(p, (x, y), xytext=(6, 4), textcoords="offset points", fontsize=9)
    ax.annotate("mismo arrastre,\ncaptura opuesta", xy=(1.52, 0.22), xytext=(1.15, 0.55),
                fontsize=8.5, color="#555", arrowprops=dict(arrowstyle="->", color="#999"))
    ax.set_xlabel("Encadenamiento hacia adelante (Ghosh-Rasmussen, 2018)")
    ax.set_ylabel("Fracción del valor minero exportado en crudo (crudo_share)")
    ax.set_xlim(0.5, 1.75); ax.set_ylim(0, 1.05)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "vii4_ghosh_vs_crudo.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)

def fig5():
    ES = {"China":[1.53,1.30,1.02],"Mexico":[1.51,1.17,1.12],"Chile":[0.73,1.23,1.12]}
    L = ["L1 extracción","L2 refinación","L3 semimanufactura"]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    w = 0.25
    colp = {"China":VERDE,"Mexico":ROJO,"Chile":AZUL}
    for j,(p,vs) in enumerate(ES.items()):
        xs=[i+(j-1)*w for i in range(3)]
        ax.bar(xs, vs, w, label=p, color=colp[p], edgecolor="#2b3a46", linewidth=0.6)
        for x,v in zip(xs,vs): ax.text(x, v+0.02, f"{v:.2f}", ha="center", fontsize=7.5)
    ax.axhline(1, color="#999", ls="--", lw=1)
    ax.set_xticks(range(3)); ax.set_xticklabels(L)
    ax.set_ylabel("Ghosh-Rasmussen hacia adelante (2018)"); ax.set_ylim(0,1.75)
    ax.legend(frameon=False, fontsize=9, ncol=3, loc="upper center", bbox_to_anchor=(0.5,1.1))
    ax.spines[["top","right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(os.path.join(HERE,"vii5_eslabones_intl.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)

for f in (fig1,fig2,fig3,fig4,fig5):
    f(); print("ok", f.__name__)
