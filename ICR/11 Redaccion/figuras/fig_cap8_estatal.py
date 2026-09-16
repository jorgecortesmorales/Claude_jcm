# -*- coding: utf-8 -*-
"""Ilustracion — encadenamiento hacia adelante por entidad (Ghosh estatal)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
AZUL, ROJO, GRIS = "#4f86b3", "#b04a3a", "#8a8a8a"

rows = list(csv.DictReader(open(os.path.join(PROC, "ghosh_estatal_mineria.csv"), encoding="utf-8-sig")))
for r in rows:
    r["f"] = float(r["forward_rasmussen"]); r["fuga"] = float(r.get("fuga_export_share") or 0)
rows.sort(key=lambda r: -r["f"])
top = rows[:12][::-1]
HUB = {"Coahuila", "Sonora", "San Luis Potosi"}
labels = [r["estado"].replace("San Luis Potosi", "San Luis Potosí") for r in top]
vals = [r["f"] for r in top]
cols = [ROJO if r["estado"] in HUB else (AZUL if r["f"] >= 1 else GRIS) for r in top]

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.barh(labels, vals, color=cols, edgecolor="#2b3a46", linewidth=0.6)
ax.axvline(1.0, color="#999", ls="--", lw=1)
for i, r in enumerate(top):
    ax.text(r["f"] + 0.015, i, f"{r['f']:.2f}  (fuga {r['fuga']*100:.0f}%)", va="center", fontsize=8)
ax.set_xlabel("Encadenamiento hacia adelante por entidad (Ghosh-Rasmussen estatal, 2018)")
ax.set_xlim(0, 2.05)
ax.text(0.02, 0.02, "En rojo, los hubs de transformación (Coahuila, Sonora, San Luis Potosí).",
        transform=ax.transAxes, fontsize=7.8, color="#777")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "viii3_ghosh_estatal.png"), dpi=200, bbox_inches="tight", facecolor="white")
print("ok ghosh estatal")
