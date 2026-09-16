# -*- coding: utf-8 -*-
"""Grafica historica del peso del bloque: exportaciones 1992-2024 (valor + share nacional)
y valor de produccion 2004-2018 (efecto precio vs volumen). -> png_charts/peso_historico.png"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

P=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\png_charts"
COBRE="#c85a1a"; AZUL="#0f6fa8"; GRIS="#8a8175"; TINTA="#211d18"

def load(f): return list(csv.DictReader(open(os.path.join(P,f),encoding="utf-8")))

exp=load("peso_bloque_hist_exportaciones.csv")
yrs=[int(r["anio"]) for r in exp]
xb=[float(r["X_bloque_musd"])/1000 for r in exp]              # miles de MUSD (billion USD)
sh=[float(r["share_bloque_pct"]) if r["share_bloque_pct"] else None for r in exp]

prod=load("peso_bloque_hist_produccion.csv")
compl=sorted({int(r["anio"]) for r in prod if r["anio_completo"]=="si"})
pv={a:0.0 for a in compl}
for r in prod:
    a=int(r["anio"])
    if a in pv: pv[a]+=float(r["valor_prod_usd"])/1e9
pyr=sorted(pv); pval=[pv[a] for a in pyr]

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.edgecolor":GRIS,
                     "axes.labelcolor":TINTA,"text.color":TINTA,"xtick.color":GRIS,"ytick.color":GRIS})
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(15,5.6))

# Panel A: exportaciones bloque (barras) + share nacional (linea)
ax1.bar(yrs,xb,color=COBRE,alpha=.85,width=.7,label="Valor exportado (miles MUSD)")
ax1.set_ylabel("Exportaciones del bloque (miles de MUSD)",color=COBRE)
ax1.tick_params(axis="y",colors=COBRE)
ax1b=ax1.twinx()
ax1b.plot(yrs,sh,color=TINTA,lw=2.2,marker="o",ms=3,label="% de las exportaciones nacionales")
ax1b.set_ylabel("Peso en las exportaciones totales de México (%)",color=TINTA)
ax1b.set_ylim(0,6)
ax1.set_title("Peso del bloque en las exportaciones · 1992–2024",fontsize=13,color=TINTA,weight="bold")
ax1.set_xlim(1991,2025)
ax1.annotate("pico 2011\n5.5%",(2011,xb[yrs.index(2011)]),xytext=(2004,17),
             fontsize=10,color=TINTA,arrowprops=dict(arrowstyle="->",color=GRIS))
ax1.annotate("mín. 2002\n1.2%",(2002,xb[yrs.index(2002)]),xytext=(1994,9),
             fontsize=10,color=GRIS,arrowprops=dict(arrowstyle="->",color=GRIS))

# Panel B: valor de produccion 1992-2018 (efecto precio vs volumen)
prices={}; vols={}
for r in prod:
    a=int(r["anio"])
    if a in compl:
        prices.setdefault(a,{})[r["mineral"]]=float(r["precio_usd_t"])
        vols.setdefault(a,{})[r["mineral"]]=float(r["vol_t"])
base=min(pyr); pv_vol=[]
for a in pyr:
    v=sum(vols[a][m]*prices[base][m] for m in vols[a] if m in prices[base])/1e9  # volumen a precios base
    pv_vol.append(v)
ax2.plot(pyr,pval,color=COBRE,lw=2.4,marker="o",ms=3,label="Valor de producción (corriente)")
ax2.plot(pyr,pv_vol,color=AZUL,lw=2.0,ls="--",marker="s",ms=2.5,label=f"Solo efecto volumen (a precios {base})")
ax2.fill_between(pyr,pv_vol,pval,color=COBRE,alpha=.12)
ax2.set_ylabel("Valor de la producción del bloque (miles de MUSD)")
ax2.set_title("Valor de producción: precio vs. volumen · 1992–2022",fontsize=13,color=TINTA,weight="bold")
ax2.legend(loc="upper left",fontsize=10,frameon=False)
ax2.text(2004,3.0,"la franja = efecto precio",fontsize=9.5,color=GRIS)
for ax in (ax1,ax2):
    ax.spines["top"].set_visible(False)
ax1b.spines["top"].set_visible(False)
plt.tight_layout()
f=os.path.join(OUT,"peso_historico.png")
plt.savefig(f,dpi=140,bbox_inches="tight"); print("escrito",f)
