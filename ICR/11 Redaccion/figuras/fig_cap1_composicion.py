# -*- coding: utf-8 -*-
"""Ilustracion I.2 — composicion del valor de produccion del bloque por mineral, 1992-2022."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PROC = os.path.normpath(os.path.join(HERE, "..", "..", "10 Datos", "processed"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})

NOM = {"cobre":"Cobre","oro":"Oro","plata":"Plata","zinc":"Zinc","plomo":"Plomo",
       "manganeso":"Manganeso","fluorita":"Fluorita","silice":"Sílice",
       "barita":"Barita","grafito":"Grafito"}
d = defaultdict(dict)
with open(os.path.join(PROC, "peso_bloque_hist_produccion.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        try: d[r["mineral"]][int(r["anio"])] = float(r["share_bloque_pct"])
        except Exception: pass

years = sorted(set(y for m in d.values() for y in m))
years = [y for y in years if 1992 <= y <= 2022]
orden = ["cobre","oro","plata","zinc","plomo","manganeso","fluorita","silice","barita","grafito"]
COL = ["#b04a3a","#c98a2b","#8a8a8a","#4f86b3","#2b6e4f","#7a5aa8","#5aa0a0","#a0a0d0","#c0a080","#708090"]

series = []
for m in orden:
    series.append([d[m].get(y, 0) for y in years])

fig, ax = plt.subplots(figsize=(10, 4.8))
ax.stackplot(years, *series, labels=[NOM[m] for m in orden], colors=COL, edgecolor="white", linewidth=0.2)
ax.set_ylabel("Participación en el valor de producción del bloque (%)")
ax.set_xlabel("Año"); ax.set_xlim(min(years), max(years)); ax.set_ylim(0, 100)
ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), frameon=False, fontsize=8.5)
# anotar el cruce cobre/oro
ax.annotate("El oro pasa de ~10 % a ~30 %;\nel cobre de ~41 % a ~30 %",
            xy=(2010, 55), fontsize=8.2, color="#3a3a3a",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#ccc", alpha=0.8))
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "i2_composicion_bloque.png"), dpi=200, bbox_inches="tight", facecolor="white")
print("ok composicion bloque")
