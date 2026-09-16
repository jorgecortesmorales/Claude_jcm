# -*- coding: utf-8 -*-
"""Ilustracion — destino de la produccion minera por entidad (Ghosh interestatal)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})

def fl(x):
    try: return float(x)
    except Exception: return 0.0

rows = list(csv.DictReader(open(os.path.join(PROC, "ghosh_interestatal_mineria.csv"), encoding="utf-8-sig")))
rows.sort(key=lambda r: -fl(r["vbp_mineria_mdp"]))
top = rows[:10]
top.sort(key=lambda r: fl(r["export_abroad_share"]))  # menor fuga arriba
labels = [r["estado"].replace("San Luis Poto", "San Luis Potosí").replace("Baja Californ", "Baja California")[:16] for r in top]

intra = [fl(r["intra_share"]) for r in top]
inter = [fl(r["inter_estatal_share"]) for r in top]
final = [fl(r["final_nacional_share"]) for r in top]
export = [fl(r["export_abroad_share"]) for r in top]

C_INTRA, C_INTER, C_FINAL, C_EXP = "#2b6e4f", "#7fabcb", "#cfe0ec", "#b04a3a"
fig, ax = plt.subplots(figsize=(9.5, 4.8))
y = range(len(top))
ax.barh(y, intra, color=C_INTRA, label="Intra-estatal", edgecolor="white", linewidth=0.3)
left = list(intra)
ax.barh(y, inter, left=left, color=C_INTER, label="Inter-estatal (otras entidades)", edgecolor="white", linewidth=0.3)
left = [a+b for a, b in zip(left, inter)]
ax.barh(y, final, left=left, color=C_FINAL, label="Demanda final nacional", edgecolor="white", linewidth=0.3)
left = [a+b for a, b in zip(left, final)]
ax.barh(y, export, left=left, color=C_EXP, label="Exportación al exterior", edgecolor="white", linewidth=0.3)
for i, r in enumerate(top):
    e = fl(r["export_abroad_share"])
    ax.text(1.01, i, f"fuga {e*100:.0f}%", va="center", fontsize=8, color=C_EXP)
ax.set_yticks(list(y)); ax.set_yticklabels(labels)
ax.set_xlim(0, 1.18); ax.set_xlabel("Destino de la producción minera de la entidad (participación)")
ax.legend(frameon=False, fontsize=8, ncol=2, loc="upper center", bbox_to_anchor=(0.5, 1.13))
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "viii4_interestatal.png"), dpi=200, bbox_inches="tight", facecolor="white")
print("ok interestatal")
