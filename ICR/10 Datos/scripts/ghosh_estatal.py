# -*- coding: utf-8 -*-
"""Paso 8 (numerico) — Ghosh hacia adelante de la MINERIA por ENTIDAD FEDERATIVA.
Fuente: INEGI, MIP Multi-Estatal 2018, matrices industria x industria INTRA-estatales
(mip_ixi_e_<edo>_intra_2018.xlsx: 35 industrias, flujos producidos y usados en la entidad).
Sector minero comparable = '21-2 Mineria no petrolera' (analogo a B07_08 de la ICIO y a los 10 minerales).
Metodo identico al nacional: B=Z/x(fila), G=(I-B)^-1, forward=rowsum(G), Rasmussen=indice/media (media estado=1).
Ademas: 'fuga' = share del producto minero del estado que sale como EXPORTACION (interestatal + internacional)
frente al que se usa como insumo intra-estatal -> firma del enclave regional en el propio dato I-O.
Salida: processed/ghosh_estatal_mineria.csv
CAVEAT: 35 industrias (mineria agregada, no por mineral); intra-estatal (no capta encadenamiento inter-estatal;
para eso estan las MIP birregionales/multiestatales).
"""
import pandas as pd, numpy as np, os, glob, csv

BASE=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\Bases Originales\13 MIP Estatal INEGI\extract"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
NOMBRE={"ags":"Aguascalientes","bc":"Baja California","bcs":"Baja California Sur","camp":"Campeche",
 "cdmx":"Ciudad de Mexico","chih":"Chihuahua","chis":"Chiapas","coah":"Coahuila","col":"Colima",
 "dgo":"Durango","gro":"Guerrero","gto":"Guanajuato","hgo":"Hidalgo","jal":"Jalisco","mex":"Mexico",
 "mich":"Michoacan","mor":"Morelos","nay":"Nayarit","nl":"Nuevo Leon","oax":"Oaxaca","pue":"Puebla",
 "qr":"Quintana Roo","qro":"Queretaro","sin":"Sinaloa","slp":"San Luis Potosi","son":"Sonora",
 "tab":"Tabasco","tamps":"Tamaulipas","tlax":"Tlaxcala","ver":"Veracruz","yuc":"Yucatan","zac":"Zacatecas"}

def val(c):
    try: return float(c)
    except: return 0.0

def load(path):
    df=pd.read_excel(path,sheet_name=0,header=None)
    n=len(df)
    # fila de encabezado de actividades
    hr=next(i for i in range(n) if str(df.iloc[i,1]).strip()=="Actividad")
    # columnas industria: en la fila hr, cols>=2 cuyo texto tiene ' - ' y no es demanda final
    ind_cols=[]; ind_names=[]
    for j in range(2,df.shape[1]):
        h=str(df.iloc[hr,j]).strip()
        if h in ("nan","") : continue
        if h.startswith(("CP","CG","P.51","P.52","Exportaciones","d P.6")): break
        ind_cols.append(j); ind_names.append(h)
    # filas industria: hr+1 .. hr+len(ind_cols)
    ind_rows=list(range(hr+1,hr+1+len(ind_cols)))
    # fila Total (output)
    tr=next(i for i in range(n) if str(df.iloc[i,1]).strip()=="Total")
    # columnas de exportacion (fuga)
    exp_cols=[j for j in range(2,df.shape[1]) if str(df.iloc[hr,j]).strip().startswith(("Exportaciones","d P.6"))]
    N=len(ind_cols)
    Z=np.array([[val(df.iloc[r,c]) for c in ind_cols] for r in ind_rows])   # NxN intra
    x=np.array([val(df.iloc[tr,c]) for c in ind_cols])                      # output por industria
    # indice de mineria no petrolera
    mi=next(k for k,nm in enumerate(ind_names) if nm.startswith("21-2"))
    # fila de mineria: usos por destino
    minrow=ind_rows[mi]
    intra_interm=sum(val(df.iloc[minrow,c]) for c in ind_cols)              # a industrias intra-estatales
    exports=sum(val(df.iloc[minrow,c]) for c in exp_cols)                   # inter-estatal + internacional
    x_min=x[mi]
    return dict(N=N,Z=Z,x=x,mi=mi,ind_names=ind_names,x_min=x_min,
                intra_interm=intra_interm,exports=exports,tr=tr)

def ghosh(Z,x):
    xs=np.where(x==0,1.0,x)
    B=Z/xs[:,None]; A=Z/xs[None,:]
    I=np.eye(len(x))
    G=np.linalg.inv(I-B); L=np.linalg.inv(I-A)
    FL=G.sum(axis=1); BL=L.sum(axis=0)
    return FL, FL/FL.mean(), BL, BL/BL.mean()

def main():
    rows=[]
    for path in sorted(glob.glob(os.path.join(BASE,"mip_ixi_e_*_intra_2018.xlsx"))):
        edo=os.path.basename(path).split("_")[3]
        d=load(path)
        FL,Ui,BL,U=ghosh(d["Z"],d["x"])
        mi=d["mi"]
        rank_f=int((-Ui).argsort().argsort()[mi]+1)
        vbp_tot=d["x"].sum()
        fuga=d["exports"]/d["x_min"] if d["x_min"] else None
        rows.append(dict(
            estado=NOMBRE.get(edo,edo), abrev=edo,
            vbp_mineria_mdp=round(d["x_min"],1),
            share_vbp_estatal_pct=round(100*d["x_min"]/vbp_tot,3) if vbp_tot else None,
            forward_rowsum=round(float(FL[mi]),4),
            forward_rasmussen=round(float(Ui[mi]),4),
            rank_forward_de_35=rank_f,
            backward_rasmussen=round(float(U[mi]),4),
            fuga_export_share=round(fuga,4) if fuga is not None else None,
            usa_intra_interm_mdp=round(d["intra_interm"],1),
            exporta_mdp=round(d["exports"],1),
        ))
    rows.sort(key=lambda r:-(r["vbp_mineria_mdp"] or 0))
    f=os.path.join(OUT,"ghosh_estatal_mineria.csv")
    with open(f,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("Escrito:",f,"| estados:",len(rows))
    print(f"\n{'estado':20s}{'VBP_min':>10s}{'%VBP':>7s}{'fwd_ras':>8s}{'rk/35':>6s}{'fuga%':>7s}")
    for r in rows[:16]:
        print(f"{r['estado']:20s}{r['vbp_mineria_mdp']:>10.0f}{(r['share_vbp_estatal_pct'] or 0):>7.2f}"
              f"{r['forward_rasmussen']:>8.2f}{r['rank_forward_de_35']:>6d}{100*(r['fuga_export_share'] or 0):>7.0f}")

if __name__=="__main__":
    main()
