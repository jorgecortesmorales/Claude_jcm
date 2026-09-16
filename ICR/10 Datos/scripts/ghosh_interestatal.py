# -*- coding: utf-8 -*-
"""Paso 8+ — Ghosh INTER-ESTATAL de la mineria con la MIP BIRREGIONAL 2018 de INEGI.
Cada archivo mip_ixi_br_<edo>_d_2018.xlsx es una MIP de 2 regiones (la entidad + 'Resto del Pais'),
70 industrias (35+35). Los flujos inter-estatales son ENDOGENOS (bloque RestoPais->entidad y viceversa);
solo el resto del mundo es externo. Permite descomponer el producto minero (21-2) de cada entidad en:
  - intra   : usado como insumo por industrias de LA MISMA entidad
  - inter   : usado como insumo por industrias del RESTO DEL PAIS (encadenamiento NACIONAL, no perdida)
  - final   : demanda final nacional (consumo/inversion, ambas regiones)
  - abroad  : exportaciones al extranjero (d P.6)  = FUGA REAL fuera de la economia nacional
Y un Ghosh hacia adelante birregional (rowsum de G, Rasmussen media 70=1) que SI capta el eslabon inter-estatal.
Salida: processed/ghosh_interestatal_mineria.csv
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
    df=pd.read_excel(path,sheet_name=0,header=None); n=len(df)
    hr=next(i for i in range(n) if str(df.iloc[i,1]).strip()=="Actividad")
    tr=next(i for i in range(n) if str(df.iloc[i,1]).strip()=="Total")
    # columnas industria de ambas regiones (antes de la 1a col de demanda final)
    ind_cols=[];
    for j in range(2,df.shape[1]):
        h=str(df.iloc[hr,j]).strip()
        if h.startswith(("CP","CG","P.51","P.52","d P.6","Exportaciones")):
            if not ind_cols: continue
            break
        if h in ("nan",""): continue
        ind_cols.append(j)
    K=len(ind_cols)                     # debe ser 70
    ind_rows=list(range(hr+1,hr+1+K))
    # columnas de export al extranjero (fuga real): las 'd P.6' de ambas regiones
    exp_cols=[j for j in range(2,df.shape[1]) if str(df.iloc[hr,j]).strip().startswith("d P.6")]
    # columnas de demanda final nacional (consumo/inversion): CP,CG,P.51b,P.52 de ambas regiones
    fd_cols=[j for j in range(2,df.shape[1]) if str(df.iloc[hr,j]).strip().startswith(("CP","CG","P.51","P.52"))]
    Z=np.array([[val(df.iloc[r,c]) for c in ind_cols] for r in ind_rows])
    x=np.array([val(df.iloc[tr,c]) for c in ind_cols])
    # mineria 21-2 de la REGION 1 (entidad) = primer 21-2 en el orden de filas
    mi=next(k for k in range(K) if str(df.iloc[ind_rows[k],1]).strip().startswith("21-2"))
    half=K//2
    minrow=ind_rows[mi]
    intra=sum(val(df.iloc[minrow,ind_cols[c]]) for c in range(0,half))     # cols R1
    inter=sum(val(df.iloc[minrow,ind_cols[c]]) for c in range(half,K))     # cols R2 (resto del pais)
    final=sum(val(df.iloc[minrow,c]) for c in fd_cols)
    abroad=sum(val(df.iloc[minrow,c]) for c in exp_cols)
    return dict(Z=Z,x=x,mi=mi,K=K,x_min=x[mi],intra=intra,inter=inter,final=final,abroad=abroad)

def ghosh_fwd(Z,x):
    xs=np.where(x==0,1.0,x); B=Z/xs[:,None]
    G=np.linalg.inv(np.eye(len(x))-B); FL=G.sum(axis=1)
    return FL, FL/FL.mean()

def main():
    rows=[]
    for path in sorted(glob.glob(os.path.join(BASE,"mip_ixi_br_*_d_2018.xlsx"))):
        edo=os.path.basename(path).split("_")[3]
        d=load(path)
        FL,Ui=ghosh_fwd(d["Z"],d["x"]); mi=d["mi"]
        xm=d["x_min"]
        tot_uso=d["intra"]+d["inter"]+d["final"]+d["abroad"]
        base=xm if xm else 1.0
        rows.append(dict(
            estado=NOMBRE.get(edo,edo),abrev=edo,
            vbp_mineria_mdp=round(xm,1),
            intra_share=round(d["intra"]/base,4),
            inter_estatal_share=round(d["inter"]/base,4),
            final_nacional_share=round(d["final"]/base,4),
            export_abroad_share=round(d["abroad"]/base,4),
            encad_nacional_share=round((d["intra"]+d["inter"])/base,4),
            forward_rasmussen_br=round(float(Ui[mi]),4),
        ))
    rows.sort(key=lambda r:-(r["vbp_mineria_mdp"] or 0))
    f=os.path.join(OUT,"ghosh_interestatal_mineria.csv")
    with open(f,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("Escrito:",f)
    print(f"\n{'estado':18s}{'VBPmin':>9s}{'intra':>7s}{'inter':>7s}{'final':>7s}{'abroad':>7s}{'fwd_br':>7s}")
    for r in rows[:14]:
        print(f"{r['estado']:18s}{r['vbp_mineria_mdp']:>9.0f}"
              f"{100*r['intra_share']:>7.0f}{100*r['inter_estatal_share']:>7.0f}"
              f"{100*r['final_nacional_share']:>7.0f}{100*r['export_abroad_share']:>7.0f}{r['forward_rasmussen_br']:>7.2f}")

if __name__=="__main__":
    main()
