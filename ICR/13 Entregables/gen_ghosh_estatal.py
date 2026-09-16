# -*- coding: utf-8 -*-
"""Grafica Paso 8 numerico: fuga del producto minero por estado (MIP estatal 2018).
Barra horizontal de la 'fuga' (share exportado fuera del estado) para los estados con
mineria relevante, coloreada por integracion; anota el peso de la mineria en el estado.
-> png_charts/ghosh_estatal.png"""
import csv, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

P=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed\ghosh_estatal_mineria.csv"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\png_charts\ghosh_estatal.png"
COBRE="#c85a1a"; AZUL="#0f6fa8"; ROJO="#b5342b"; VERDE="#2e7d5b"; GRIS="#8a8175"; TINTA="#211d18"

r=[x for x in csv.DictReader(open(P,encoding="utf-8")) if float(x["vbp_mineria_mdp"])>5000]
r.sort(key=lambda x:float(x["fuga_export_share"]))
est=[x["estado"] for x in r]
fuga=[100*float(x["fuga_export_share"]) for x in r]
share=[float(x["share_vbp_estatal_pct"]) for x in r]
fwd=[float(x["forward_rasmussen"]) for x in r]
def col(f):
    return VERDE if f<50 else (ROJO if f>=80 else GRIS)
cols=[col(f) for f in fuga]

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":GRIS,
                     "text.color":TINTA,"axes.labelcolor":TINTA,"xtick.color":GRIS,"ytick.color":TINTA})
fig,ax=plt.subplots(figsize=(11,7.4))
y=range(len(est))
ax.barh(list(y),fuga,color=cols,alpha=.88,height=.72)
ax.set_yticks(list(y)); ax.set_yticklabels(est,fontsize=11)
ax.set_xlim(0,105); ax.set_xlabel("Fuga: % del producto minero del estado que sale como exportación (inter-estatal + internacional) · MIP estatal 2018")
ax.axvline(50,color=GRIS,ls=":",lw=1)
for i,(f,s,fw) in enumerate(zip(fuga,share,fwd)):
    ax.text(f+1.5,i,f"{f:.0f}%  ·  minería {s:.1f}% del edo.  ·  fwd {fw:.2f}",va="center",fontsize=9,color=TINTA)
ax.set_title("El enclave, por estado: casi todos exportan su mineral en bruto;\nsólo donde hay fundición local (Coahuila, Sonora, SLP) la cadena se queda",
             fontsize=13.5,weight="bold",color=TINTA,loc="left",pad=12)
# leyenda de color (abajo, horizontal, fuera del area de barras)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=VERDE,label="integrado (<50% fuga)"),Patch(color=GRIS,label="intermedio"),
                   Patch(color=ROJO,label="enclave (≥80% fuga)")],loc="upper center",
          bbox_to_anchor=(0.5,-0.10),ncol=3,frameon=False,fontsize=10)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT,dpi=140,bbox_inches="tight"); print("escrito",OUT)
