# -*- coding: utf-8 -*-
"""Genera los 4 graficos como PNG (matplotlib) para incrustar en el .docx del resumen.
Paleta 'ensayo mineral' consistente con la infografia/presentacion."""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

BASE=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\png_charts"
os.makedirs(OUT,exist_ok=True)
def rd(p): return list(csv.DictReader(open(os.path.join(BASE,p),encoding='utf-8-sig')))

INK="#211d18";MUT="#8a8175";HAIR="#d7d2c7";COP="#b0571e"
COBRE="#c85a1a";ZINC="#0f6fa8";PLOMO="#9a5ba0";CRUDO="#c85a1a";PROC="#0f6fa8"
plt.rcParams.update({
 "font.family":"DejaVu Sans","font.size":13,"text.color":INK,
 "axes.edgecolor":HAIR,"axes.labelcolor":INK,"xtick.color":MUT,"ytick.color":INK,
 "axes.linewidth":0.8,"figure.dpi":200,"savefig.dpi":200,
})
NAMES={'cobre':'Cobre','zinc':'Zinc','plomo':'Plomo','oro':'Oro','plata':'Plata','barita':'Barita','fluorita':'Fluorita','grafito':'Grafito','silice':'Sílice','manganeso':'Manganeso','plomo-zinc':'Plomo-zinc'}

def savefig(fig,name):
    fig.savefig(os.path.join(OUT,name),bbox_inches="tight",facecolor="white",pad_inches=0.15)
    plt.close(fig);print("escrito",name)

# 1) HHI 2023 horizontal bars
def hhi():
    rows=rd('hhi_consolidado.csv')
    d=sorted([(r['mineral'],int(r['hhi'])) for r in rows if r['anio']=='2023'],key=lambda x:x[1])
    def col(v): return "#8a3221" if v>=6000 else (COP if v>=2500 else ("#b98a1e" if v>=1500 else MUT))
    fig,ax=plt.subplots(figsize=(9.2,4.6))
    ys=range(len(d));vals=[v for _,v in d]
    ax.barh(list(ys),vals,color=[col(v) for _,v in d],height=0.62,zorder=3)
    ax.set_yticks(list(ys));ax.set_yticklabels([NAMES[m] for m,_ in d])
    for i,(m,v) in enumerate(d):
        ax.text(v+150,i,f"{v:,}",va="center",ha="left",fontsize=11,color=INK)
    for x in [2500,5000,7500,10000]:
        ax.axvline(x,color=HAIR,lw=0.8,zorder=1)
    ax.set_xlim(0,11000);ax.set_xticks([0,2500,5000,7500,10000])
    ax.set_xticklabels(["0","2 500","5 000","7 500","10 000"])
    ax.set_xlabel("Índice HHI (0–10 000)")
    for s in ["top","right","left"]:ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    savefig(fig,"hhi.png")

# 2) Ghosh 2018 horizontal bars
def ghosh():
    mip=rd('mip_encadenamientos_minerales.csv')
    d=sorted([(r['mineral'],float(r['forward_rasmussen'])) for r in mip if r['anio']=='2018'],key=lambda x:x[1])
    fig,ax=plt.subplots(figsize=(9.2,4.6))
    ys=range(len(d))
    ax.barh(list(ys),[v for _,v in d],color=[COP if v>=1 else MUT for _,v in d],height=0.62,zorder=3)
    ax.set_yticks(list(ys));ax.set_yticklabels([NAMES.get(m,m) for m,_ in d])
    for i,(m,v) in enumerate(d):
        ax.text(v+0.03,i,f"{v:.2f}",va="center",ha="left",fontsize=11,color=INK)
    ax.axvline(1.0,color=COP,lw=1.5,ls=(0,(5,4)),zorder=2)
    ax.set_xlim(0,3.3);ax.set_xlabel("Índice de encadenamiento hacia adelante (umbral = 1.0)")
    for s in ["top","right","left"]:ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    savefig(fig,"ghosh.png")

# 3) CCV line
def ccv():
    rows=rd('ccv_serie.csv')
    ser={'cobre':COBRE,'zinc':ZINC,'plomo':PLOMO}
    data={k:[] for k in ser}
    for r in rows:
        if r['mineral'] in ser and r['ccv']!='':
            data[r['mineral']].append((int(r['anio']),float(r['ccv'])))
    fig,ax=plt.subplots(figsize=(9.2,4.4))
    for m,col in ser.items():
        xs=[a for a,_ in data[m]];yv=[b for _,b in data[m]]
        ax.plot(xs,yv,color=col,lw=2.4,marker="o",ms=4,label=NAMES[m],zorder=3)
    ax.axhline(1.0,color=COP,lw=1.5,ls=(0,(5,4)),zorder=2)
    ax.text(2025,1.03,"paridad 1.0",ha="right",va="bottom",color=COP,fontsize=10)
    ax.set_ylim(0,2.8);ax.set_xlim(1992,2025)
    ax.set_ylabel("CCV (exportación bruta ÷ referencia)")
    ax.grid(axis="y",color=HAIR,lw=0.7);ax.set_axisbelow(True)
    for s in ["top","right"]:ax.spines[s].set_visible(False)
    ax.legend(frameon=False,loc="upper left",fontsize=11)
    ax.tick_params(length=0)
    savefig(fig,"ccv.png")

# 4) comercio 100% stacked
def comercio():
    rows=rd('comercio_posicion_resumen.csv')
    from collections import defaultdict
    acc=defaultdict(list)
    for r in rows:
        if r['X_share_crudo']!='' and int(r['anio'])>=2020:
            acc[r['mineral']].append(float(r['X_share_crudo']))
    order=['manganeso','grafito','plata','oro','silice','zinc','fluorita','cobre','plomo','barita']
    d=[(m,sum(acc[m])/len(acc[m])) for m in order if acc[m]]
    fig,ax=plt.subplots(figsize=(9.2,4.6))
    ys=range(len(d))
    cr=[v for _,v in d];pr=[1-v for _,v in d]
    ax.barh(list(ys),cr,color=CRUDO,height=0.62,zorder=3,label="Bruto (E1)")
    ax.barh(list(ys),pr,left=cr,color=PROC,height=0.62,zorder=3,label="Procesado / refinado (E2+)")
    ax.set_yticks(list(ys));ax.set_yticklabels([NAMES[m] for m,_ in d])
    for i,(m,v) in enumerate(d):
        if v>0.13: ax.text(0.01,i,f"{round(v*100)}%",va="center",ha="left",fontsize=10.5,color="white",fontweight="bold")
        if v<0.87: ax.text(0.99,i,f"{round((1-v)*100)}%",va="center",ha="right",fontsize=10.5,color="white",fontweight="bold")
    ax.set_xlim(0,1);ax.set_xticks([0,.25,.5,.75,1]);ax.set_xticklabels(["0%","25%","50%","75%","100%"])
    ax.set_xlabel("Composición de las exportaciones (promedio 2020–2024)")
    for s in ["top","right","left"]:ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    ax.legend(frameon=False,loc="lower center",bbox_to_anchor=(0.5,-0.22),ncol=2,fontsize=11)
    savefig(fig,"comercio.png")

# 5) HHI trayectoria temporal (line) con quiebre de metodo 2020/21
def hhi_traj():
    rows=rd('hhi_consolidado.csv')
    from collections import defaultdict
    S=defaultdict(list)
    for r in rows:
        try: S[r['mineral']].append((int(r['anio']),int(round(float(r['hhi'])))))
        except: pass
    sel={'barita':'#e69f00','fluorita':'#009e73','cobre':COBRE,'silice':'#56b4e9'}
    fig,ax=plt.subplots(figsize=(9.2,4.6))
    for x in [2500,5000,7500,10000]: ax.axhline(x,color=HAIR,lw=0.7,zorder=1)
    ax.axvspan(1994,2020.5,color=MUT,alpha=0.05,zorder=0)
    ax.axvline(2020.5,color=INK,lw=1,ls=(0,(4,3)),zorder=2)
    ax.text(2020.4,10500,"régimen ← | → por mina",ha="right",va="top",fontsize=9,color=MUT)
    for m,col in sel.items():
        d=sorted(S[m]); xs=[a for a,_ in d]; ys=[b for _,b in d]
        ax.plot(xs,ys,color=col,lw=2.2,marker="o",ms=3.5,label=NAMES[m],zorder=3)
    ax.set_ylim(0,11000);ax.set_xlim(1994,2024);ax.set_yticks([0,2500,5000,7500,10000])
    ax.set_yticklabels(["0","2 500","5 000","7 500","10 000"])
    ax.set_xticks([1994,1998,2002,2006,2010,2014,2018,2022])
    ax.set_ylabel("HHI (0–10 000)");ax.set_xlabel("")
    for s in ["top","right"]:ax.spines[s].set_visible(False)
    ax.tick_params(length=0);ax.legend(frameon=False,loc="lower left",fontsize=10,ncol=2)
    savefig(fig,"hhi_traj.png")

# 6) Ghosh en 3 cortes 2008 -> 2013 -> 2018 (slope)
def ghosh_cortes():
    a=rd('mip_encadenamientos_minerales.csv'); b=rd('mip_encadenamientos_2008_referencia.csv')
    G={'2008':{},'2013':{},'2018':{}}
    for r in b: G['2008'][r['mineral']]=float(r['forward_rasmussen'])
    for r in a: G[r['anio']][r['mineral']]=float(r['forward_rasmussen'])
    mins=['silice','grafito','cobre','oro','fluorita','manganeso','plata','barita']
    xs=[0,1,2]; labs=['2008\n(ref)','2013','2018']
    fig,ax=plt.subplots(figsize=(9.2,4.8))
    ax.axhline(1.0,color=COP,lw=1.3,ls=(0,(5,4)),zorder=2)
    pal={'silice':'#56b4e9','grafito':'#8a6d3b','cobre':COBRE,'oro':'#b58900','fluorita':'#009e73','manganeso':'#5b6770','plata':'#7d7d7d','barita':'#e69f00'}
    for m in mins:
        ys=[G['2008'].get(m),G['2013'].get(m),G['2018'].get(m)]
        if None in ys: continue
        ax.plot(xs,ys,color=pal[m],lw=2,marker="o",ms=5,zorder=3)
        ax.text(2.03,ys[2],NAMES[m],va="center",ha="left",fontsize=10,color=pal[m])
    ax.set_xticks(xs);ax.set_xticklabels(labs,fontsize=11)
    ax.set_xlim(-0.15,2.6);ax.set_ylim(0.4,2.05)
    ax.set_ylabel("Índice de encadenamiento hacia adelante")
    ax.text(0,1.02,"umbral 1.0",color=COP,fontsize=9,va="bottom")
    for s in ["top","right"]:ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    savefig(fig,"ghosh_cortes.png")

# 7) comercio por etapa: evolucion 2015-2024 (line)
def comercio_evo():
    rows=rd('comercio_posicion_resumen.csv')
    from collections import defaultdict
    S=defaultdict(list)
    for r in rows:
        if r['X_share_crudo']!='': S[r['mineral']].append((int(r['anio']),float(r['X_share_crudo'])))
    sel={'cobre':COBRE,'zinc':ZINC,'fluorita':'#009e73','silice':'#56b4e9'}
    fig,ax=plt.subplots(figsize=(9.2,4.5))
    for m,col in sel.items():
        d=sorted(S[m]); xs=[a for a,_ in d]; ys=[b*100 for _,b in d]
        ax.plot(xs,ys,color=col,lw=2.2,marker="o",ms=4,label=NAMES[m],zorder=3)
    ax.set_ylim(0,105);ax.set_xlim(2015,2024);ax.set_xticks([2015,2017,2019,2021,2023])
    ax.set_ylabel("% exportado en bruto (E1)")
    ax.grid(axis="y",color=HAIR,lw=0.7);ax.set_axisbelow(True)
    for s in ["top","right"]:ax.spines[s].set_visible(False)
    ax.legend(frameon=False,loc="upper left",fontsize=10,ncol=2)
    ax.tick_params(length=0)
    savefig(fig,"comercio_evo.png")

# 8) Comparacion internacional: Ghosh hacia adelante del sector-mineria, 8 paises (corte 2018; 2008 anotado)
def intl():
    rows=[r for r in rd('icio_comparacion_mineria.csv') if r['sector']=='B07_08']
    PN={'MEX':'México','CHL':'Chile','AUS':'Australia','FIN':'Finlandia','SWE':'Suecia','CHN':'China','BRA':'Brasil','PER':'Perú'}
    G={}
    for r in rows:
        G[(r['pais'],r['anio'])]=float(r['forward_rasmussen'])
    paises=[p for p in PN if (p,'2018') in G]
    d=sorted(paises, key=lambda p:G[(p,'2018')])
    fig,ax=plt.subplots(figsize=(9.2,5.0))
    ys=range(len(d))
    def col(p,v):
        if p=='MEX': return COBRE
        if p=='CHN': return "#b5342b"
        return "#0f6fa8" if v>=1 else MUT
    ax.barh(list(ys),[G[(p,'2018')] for p in d],color=[col(p,G[(p,'2018')]) for p in d],height=0.62,zorder=3)
    ax.set_yticks(list(ys)); ax.set_yticklabels([PN[p]+(' *' if p=='MEX' else '') for p in d])
    for i,p in enumerate(d):
        v=G[(p,'2018')]; v08=G.get((p,'2008'))
        lab=f"{v:.2f}"+(f"  (2008: {v08:.2f})" if v08 else "")
        ax.text(v+0.03,i,lab,va="center",ha="left",fontsize=10,color=INK)
    ax.axvline(1.0,color=COP,lw=1.5,ls=(0,(5,4)),zorder=2)
    ax.set_xlim(0,2.1);ax.set_xlabel("Ghosh hacia adelante de la minería (media país = 1) · corte 2018")
    for s in ["top","right","left"]:ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    savefig(fig,"intl_ghosh.png")

# 9) DVA / reprocesamiento: % del VA minero exportado en crudo (B07_08, corte 2018, 8 paises)
def dva():
    rows=[r for r in rd('icio_dva_mineria.csv') if r['sector']=='B07_08' and r['anio']=='2018']
    PN={'MEX':'México','CHL':'Chile','AUS':'Australia','FIN':'Finlandia','SWE':'Suecia','CHN':'China','BRA':'Brasil','PER':'Perú'}
    vals={r['pais']:float(r['crudo_share']) for r in rows if r['crudo_share']!=''}
    d=sorted([(PN[p],v,p) for p,v in vals.items()],key=lambda x:x[1])
    fig,ax=plt.subplots(figsize=(9.2,5.0))
    ys=range(len(d));cr=[v for _,v,_ in d];pr=[1-v for _,v,_ in d]
    ax.barh(list(ys),cr,color=CRUDO,height=0.62,zorder=3,label="Exportado en crudo (a reprocesar afuera)")
    ax.barh(list(ys),pr,left=cr,color=PROC,height=0.62,zorder=3,label="Transformado en casa antes de exportar")
    ax.set_yticks(list(ys));ax.set_yticklabels([p+(' *' if pc=='MEX' else '') for p,_,pc in d])
    for i,(p,v,pc) in enumerate(d):
        ax.text(0.012 if v>0.12 else v+0.012, i, f"{round(v*100)}%", va="center",
                ha="left", fontsize=10.5, color=("white" if v>0.12 else INK), fontweight="bold")
    ax.set_xlim(0,1);ax.set_xticks([0,.25,.5,.75,1]);ax.set_xticklabels(["0%","25%","50%","75%","100%"])
    ax.set_xlabel("% del valor agregado minero exportado en crudo · corte 2018")
    for s in ["top","right","left"]:ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(0.5,1.12),ncol=1,fontsize=10)
    savefig(fig,"dva.png")


# 10) HEM por mineral (peso) + dispersion Rasmussen (intensidad) vs HEM, corte 2018
def hem():
    h={r['mineral']:r for r in rd('mip_hem_minerales.csv') if r['anio']=='2018'}
    ras={r['mineral']:float(r['forward_rasmussen']) for r in rd('mip_encadenamientos_minerales.csv') if r['anio']=='2018'}
    fig,(a1,a2)=plt.subplots(1,2,figsize=(12.5,5.0))
    d=sorted(((m,float(h[m]['hem_total_pct'])) for m in h),key=lambda x:x[1])
    ys=range(len(d))
    a1.barh(list(ys),[v for _,v in d],color=COP,height=0.62,zorder=3)
    a1.set_yticks(list(ys));a1.set_yticklabels([NAMES.get(m,m) for m,_ in d])
    for i,(m,v) in enumerate(d): a1.text(v+0.004,i,f"{v:.3f}",va="center",fontsize=10,color=INK)
    a1.set_xlim(0,0.38);a1.set_xlabel("HEM total (% del VBP nacional)");a1.set_title("Peso económico",fontsize=12)
    for s_ in ["top","right","left"]:a1.spines[s_].set_visible(False)
    a1.tick_params(length=0)
    for m in h:
        x=ras[m];y=float(h[m]['hem_forward_pct'])
        a2.scatter(x,y,s=55,color=COP,edgecolor=INK,zorder=3)
        a2.annotate(NAMES.get(m,m),(x,y),xytext=(5,3),textcoords="offset points",fontsize=10)
    a2.axvline(1.0,color=MUT,lw=1.2,ls=(0,(5,4)))
    a2.set_yscale("log");a2.set_xlabel("Ghosh-Rasmussen hacia adelante (intensidad)")
    a2.set_ylabel("HEM hacia adelante (% del VBP, log)");a2.set_title("Intensidad frente a peso",fontsize=12)
    for s_ in ["top","right"]:a2.spines[s_].set_visible(False)
    fig.tight_layout();savefig(fig,"hem.png")

# 11) HEM hacia adelante por eslabon (L1/L2/L3), corte 2018
def hem_eslabon():
    rows=[r for r in rd('mip_hem_eslabones.csv') if r['anio']=='2018']
    orden=['cobre','oro','plata','plomo-zinc','manganeso','silice','grafito','fluorita','barita']
    E=['L1','L2','L3'];CL={'L1':COP,'L2':"#0f6fa8",'L3':"#7fb3d5"};NM={'L1':'L1 extracción','L2':'L2 refinación','L3':'L3 semimanufactura'}
    fig,ax=plt.subplots(figsize=(12.5,5.0));w=0.27
    for j,e in enumerate(E):
        xs=[i+(j-1)*w for i in range(len(orden))];ys_=[];hat=[]
        for m in orden:
            r=next((x for x in rows if x['mineral']==m and x['eslabon']==e),None)
            ys_.append(float(r['hem_forward_pct']) if r and r['hem_forward_pct']!='' else 0)
            hat.append('' if (r and r['atribuible']=='si') else '//')
        bars=ax.bar(xs,ys_,w,color=CL[e],edgecolor=INK,linewidth=0.5,label=NM[e],zorder=3)
        for b,hh in zip(bars,hat):
            if hh: b.set_hatch(hh)
    ax.set_xticks(range(len(orden)));ax.set_xticklabels([NAMES.get(m,m) for m in orden],fontsize=11,rotation=15,ha="right")
    ax.set_ylabel("HEM hacia adelante (% del VBP nacional)")
    ax.legend(frameon=False,fontsize=10,ncol=3,loc="lower center",bbox_to_anchor=(0.5,1.0))
    for s_ in ["top","right"]:ax.spines[s_].set_visible(False)
    ax.text(0,-0.22,"Tramado: clase de transformación compartida o agregada (el valor es de la clase completa, no del mineral).",transform=ax.transAxes,fontsize=9,color=MUT)
    savefig(fig,"hem_eslabon.png")

# 12) HEM internacional (peso) + dispersion Rasmussen vs HEM, B07_08 corte 2018
def hem_intl():
    PN={'MEX':'México','CHL':'Chile','AUS':'Australia','FIN':'Finlandia','SWE':'Suecia','CHN':'China','BRA':'Brasil','PER':'Perú'}
    h={r['pais']:r for r in rd('icio_hem_mineria.csv') if r['anio']=='2018' and r['sector']=='B07_08'}
    ras={r['pais']:float(r['forward_rasmussen']) for r in rd('icio_comparacion_mineria.csv') if r['anio']=='2018' and r['sector']=='B07_08'}
    fig,(a1,a2)=plt.subplots(1,2,figsize=(12.5,5.0))
    d=sorted(((p,float(h[p]['hem_total_pct'])) for p in h),key=lambda x:x[1])
    ys=range(len(d))
    a1.barh(list(ys),[v for _,v in d],color=[COBRE if p=='MEX' else "#0f6fa8" for p,_ in d],height=0.62,zorder=3)
    a1.set_yticks(list(ys));a1.set_yticklabels([PN[p] for p,_ in d])
    for i,(p,v) in enumerate(d): a1.text(v+0.08,i,f"{v:.2f}",va="center",fontsize=10,color=INK)
    a1.set_xlim(0,7.8);a1.set_xlabel("HEM total de la minería (% del VBP doméstico)");a1.set_title("Peso económico",fontsize=12)
    for s_ in ["top","right","left"]:a1.spines[s_].set_visible(False)
    a1.tick_params(length=0)
    for p in h:
        x=ras[p];y=float(h[p]['hem_forward_pct'])
        a2.scatter(x,y,s=55,color=(COBRE if p=='MEX' else "#0f6fa8"),edgecolor=INK,zorder=3)
        a2.annotate(PN[p],(x,y),xytext=((5,-13) if p=="FIN" else (5,3)),textcoords="offset points",fontsize=10)
    a2.axvline(1.0,color=MUT,lw=1.2,ls=(0,(5,4)))
    a2.set_xlabel("Ghosh-Rasmussen hacia adelante (media país = 1)");a2.set_ylabel("HEM hacia adelante (% del VBP)")
    a2.set_title("Intensidad frente a peso",fontsize=12)
    for s_ in ["top","right"]:a2.spines[s_].set_visible(False)
    fig.tight_layout();savefig(fig,"hem_intl.png")

# 13) HEM estatal (top 10 entidades), corte 2018
def hem_estatal():
    ACC={"San Luis Potosi":"San Luis Potosí","Nuevo Leon":"Nuevo León","Mexico":"México","Michoacan":"Michoacán"}
    r=sorted(rd('hem_estatal_mineria.csv'),key=lambda x:-float(x['hem_total_pct']))[:10][::-1]
    fig,ax=plt.subplots(figsize=(9.2,5.0));ys=range(len(r))
    f=[float(x['hem_forward_pct']) for x in r];b=[float(x['hem_backward_pct']) for x in r]
    ax.barh(list(ys),f,color=COP,height=0.62,zorder=3,label="Hacia adelante")
    ax.barh(list(ys),b,left=f,color="#0f6fa8",height=0.62,zorder=3,label="Hacia atrás")
    ax.set_yticks(list(ys));ax.set_yticklabels([ACC.get(x['estado'],x['estado']) for x in r])
    for i,x in enumerate(r): ax.text(float(x['hem_total_pct'])+0.006,i,f"{float(x['hem_total_pct']):.3f}",va="center",fontsize=10)
    ax.set_xlim(0,0.6);ax.set_xlabel("HEM de la minería (% del VBP birregional, 2018)")
    ax.legend(frameon=False,fontsize=10,loc="lower right")
    for s_ in ["top","right","left"]:ax.spines[s_].set_visible(False)
    ax.tick_params(length=0)
    savefig(fig,"hem_estatal.png")

hhi();ghosh();ccv();comercio();hhi_traj();ghosh_cortes();comercio_evo();intl();dva();hem();hem_eslabon();hem_intl();hem_estatal()
print("OK")
