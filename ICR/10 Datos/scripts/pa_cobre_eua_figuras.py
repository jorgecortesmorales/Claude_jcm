# -*- coding: utf-8 -*-
"""Pregunta A (piloto cobre) — figuras exploratorias (no forman parte del manuscrito).
Entradas: processed/cobre_eua_balance_usgs.csv, processed/cobre_eua_comercio_forma.csv
Salidas:  05 Diagnostico Insumo-Producto/Figuras - Pregunta A/pa1_balance_eua.png, pa2_socios.png
Uso: py "10 Datos/scripts/pa_cobre_eua_figuras.py"
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ICR = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR"
P = os.path.join(ICR, "10 Datos", "processed")
OUT = os.path.join(ICR, "05 Diagnostico Insumo-Producto", "Figuras - Pregunta A")
os.makedirs(OUT, exist_ok=True)
AZUL, ROJO, GRIS, VERDE, MOR, TINTA = "#4f86b3", "#b04a3a", "#8a8a8a", "#2b6e4f", "#7a5aa8", "#2b3a46"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#999", "axes.labelcolor": TINTA, "xtick.color": "#555", "ytick.color": "#555"})

# --- Figura 1: balance de cobre de EUA (miles de t de cobre contenido) ---
b = pd.read_csv(os.path.join(P, "cobre_eua_balance_usgs.csv"))
b = b[b.anio >= 1995]
fig, ax = plt.subplots(figsize=(8.4, 4.6))
series = [("consumo_aparente", "Consumo aparente", TINTA, "-"),
          ("ref_primaria", "Producción refinada primaria", AZUL, "-"),
          ("mina", "Producción minera", VERDE, "--"),
          ("imp_refinado", "Importaciones de refinado", ROJO, "-"),
          ("exp_concentrado", "Exportaciones de concentrado", MOR, ":")]
for col, lab, c, ls in series:
    ax.plot(b.anio, b[col], color=c, lw=2, ls=ls, label=lab)
    y = b[col].iloc[-1]
    ax.annotate(lab, (b.anio.iloc[-1], y), xytext=(6, 0), textcoords="offset points",
                fontsize=8, color=TINTA, va="center")
NOTAS = [(1999, 560, "1999: cierran 3 de 7\nfundiciones primarias"),
         (2019, 3000, "oct-2019: ASARCO Hayden\ny refinería Amarillo, inactivas")]
for yr, ytx, txt in NOTAS:
    ax.axvline(yr, color="#bbb", lw=1, ls="--")
    ax.text(yr + 0.3, ytx, txt, fontsize=7.5, color="#666", va="top")
ax.set_xlim(1995, 2031); ax.set_ylim(0, 3300)
ax.set_ylabel("miles de toneladas de cobre contenido")
fig.suptitle("Estados Unidos: producción, consumo y comercio de cobre, 1995-2025", fontsize=10, color=TINTA, x=0.01, ha="left")
ax.grid(axis="y", color="#eee"); ax.legend(frameon=False, fontsize=8, loc="lower center", bbox_to_anchor=(0.42, 1.02), ncol=3)
fig.text(0.01, -0.02, "Fuente: USGS, Mineral Commodity Summaries — Copper, ediciones 2000-2026 (2025 estimado). "
         "El consumo aparente cambia de definición en la edición 2020.", fontsize=7, color="#666")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "pa1_balance_eua.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)

# --- Figura 2: participación por socio (valor), tres paneles ---
r = pd.read_csv(os.path.join(P, "cobre_eua_comercio_forma.csv"))
paneles = [("M", "refinado", "Importaciones de EUA de cobre refinado\n(% del valor, por origen)",
            [("chile", "Chile", AZUL), ("canada", "Canadá", VERDE), ("peru", "Perú", MOR), ("mexico", "México", ROJO)]),
           ("M", "chatarra", "Importaciones de EUA de chatarra de cobre\n(% del valor, por origen)",
            [("canada", "Canadá", VERDE), ("mexico", "México", ROJO)]),
           ("X", "concentrado", "Exportaciones de EUA de concentrado\n(% del valor, por destino)",
            [("mexico", "México", ROJO), ("china", "China", GRIS)])]
fig, axs = plt.subplots(1, 3, figsize=(11, 3.7), sharey=True)
for ax, (fl, fo, tit, soc) in zip(axs, paneles):
    x = r[(r.flujo == fl) & (r.forma == fo)].sort_values("anio")
    for k, lab, c in soc:
        ax.plot(x.anio, 100 * x[f"share_valor_{k}"], color=c, lw=2, label=lab)
    ax.set_title(tit, fontsize=9, color=TINTA, loc="left"); ax.set_ylim(0, 100); ax.set_xlim(1992, 2024)
    ax.grid(axis="y", color="#eee"); ax.legend(frameon=False, fontsize=8, loc="upper left")
axs[0].set_ylabel("%")
fig.text(0.01, -0.03, "Fuente: cálculo propio con UN Comtrade (EUA como reportante; HS 7403, 7404 y 2603).", fontsize=7, color="#666")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "pa2_socios.png"), dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)
print("ok", OUT)
