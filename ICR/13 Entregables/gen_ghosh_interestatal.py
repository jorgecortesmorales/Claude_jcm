# -*- coding: utf-8 -*-
"""Grafica: descomposicion del destino del producto minero por estado (MIP birregional 2018):
intra-estatal / inter-estatal (cadena nacional) / demanda final / exportado al extranjero (fuga real).
Barras apiladas, estados con mineria relevante, ordenados por 'exportado al extranjero'.
-> png_charts/ghosh_interestatal.png"""
import csv, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

P=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed\ghosh_interestatal_mineria.csv"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\png_charts\ghosh_interestatal.png"
VERDE="#2e7d5b"; AZUL="#4a90c2"; GRIS="#c9c3b6"; ROJO="#b5342b"; TINTA="#211d18"; GR2="#8a8175"

r=[x for x in csv.DictReader(open(P,encoding="utf-8")) if float(x["vbp_mineria_mdp"])>5000]
r.sort(key=lambda x:float(x["export_abroad_share"]))
est=[x["estado"] for x in r]
intra=[100*float(x["intra_share"]) for x in r]
inter=[100*float(x["inter_estatal_share"]) for x in r]
final=[100*float(x["final_nacional_share"]) for x in r]
abroad=[100*float(x["export_abroad_share"]) for x in r]

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.edgecolor":GR2,
                     "text.color":TINTA,"axes.labelcolor":TINTA,"xtick.color":GR2,"ytick.color":TINTA})
fig,ax=plt.subplots(figsize=(11.5,7.6))
y=list(range(len(est)))
l1=ax.barh(y,intra,color=VERDE,height=.74,label="usado en el propio estado")
left=intra[:]
l2=ax.barh(y,inter,left=left,color=AZUL,height=.74,label="a industria de otros estados (cadena nacional)")
left=[a+b for a,b in zip(left,inter)]
l3=ax.barh(y,final,left=left,color=GRIS,height=.74,label="demanda final nacional")
left=[a+b for a,b in zip(left,final)]
l4=ax.barh(y,abroad,left=left,color=ROJO,height=.74,label="exportado al extranjero (fuga real)")
ax.set_yticks(y); ax.set_yticklabels(est,fontsize=11)
ax.set_xlim(0,100); ax.set_xlabel("Destino del producto minero del estado (%) · MIP birregional INEGI 2018")
for i,a in enumerate(abroad):
    if a>=3: ax.text(100.5,i,f"{a:.0f}% afuera",va="center",fontsize=9,color=ROJO)
ax.set_title("A dónde va el mineral de cada estado: gran parte de la «fuga» es cadena nacional\n"
             "(concentrado que alimenta fundiciones de otros estados), no pérdida al extranjero",
             fontsize=13,weight="bold",color=TINTA,loc="left",pad=12)
ax.legend(loc="upper center",bbox_to_anchor=(0.5,-0.09),ncol=2,frameon=False,fontsize=10)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig(OUT,dpi=140,bbox_inches="tight"); print("escrito",OUT)
