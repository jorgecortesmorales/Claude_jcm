# -*- coding: utf-8 -*-
"""
Actividad A (version HISTORICA) — Peso del bloque de 10 minerales en el periodo estudiado.
Dos series propias (in-vault) expresadas contra denominadores nacionales:
  (1) EXPORTACIONES 1992-2024: valor del bloque (Comtrade) / exportaciones totales de Mexico
      (Banco Mundial, TX.VAL.MRCH.CD.WT, current US$)  -> share historico del bloque.
  (2) VALOR DE PRODUCCION 2004-2024: volumen nacional (hhi_numeradores) x precio USGS empalmado,
      normalizado a toneladas -> serie propia; descomposicion precio vs. volumen.
El peso en el PIB (VAB) queda en los cortes de la MIP (2013/2018) por no existir PIB anual
por clase SCIAN; se declara. Salidas:
  processed/peso_bloque_hist_exportaciones.csv  (anio, X_bloque_musd, X_nacional_musd, share_pct, y por mineral)
  processed/peso_bloque_hist_produccion.csv     (anio, mineral, vol_t, precio, valor_prod_usd, share_bloque)
"""
import csv, os, collections

OUT = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

# Exportaciones totales de Mexico (Banco Mundial, current US$) 1992-2024
X_NAC = {1992:46196,1993:51886,1994:60882,1995:79542,1996:96000,1997:110431,1998:117460,
 1999:136391,2000:166367,2001:158547,2002:160682,2003:165396,2004:187980,2005:214207,
 2006:249961,2007:271821,2008:291265,2009:229712,2010:298305,2011:349569,2012:370770,
 2013:380015,2014:396912,2015:380550,2016:373948,2017:409433,2018:450713,2019:460604,
 2020:417171,2021:494949,2022:577697,2023:593001,2024:617677}  # en MUSD

def to_tonnes(val, unidad):
    u=(unidad or "").strip().lower()
    if u in ("toneladas","t"): return val
    if u in ("miles oz","miles de onzas","koz"): return val*0.0311034768        # 1000 oz troy = 0.0311035 t
    if u in ("millones oz","millones de onzas","moz"): return val*31.1034768     # 1e6 oz troy = 31.1035 t
    if u in ("kg","kilogramos"): return val/1000.0
    return val  # asume toneladas

def load_prices():
    p=collections.defaultdict(dict)
    for r in csv.DictReader(open(os.path.join(OUT,"precios_usgs_anual_empalmado.csv"),encoding="utf-8-sig")):
        try: p[r["mineral"].lower()][int(r["anio"])]=float(r["precio_usd_t_nominal"])
        except: pass
    return p

def load_natvol():
    # produccion nacional por mineral-anio (t). 1992-2003 = USGS MYB (pre2004);
    # 2004-2018 = CAMIMEX (hhi_numeradores). Empalme declarado en 2003/2004.
    seen={}
    # 1992-2003: USGS MYB
    pre=os.path.join(OUT,"produccion_nacional_myb_pre2004.csv")
    if os.path.exists(pre):
        for r in csv.DictReader(open(pre,encoding="utf-8")):
            seen[(r["mineral"].lower(), int(r["anio"]))]=float(r["vol_t"])
    # 2004-2018: CAMIMEX (hhi_numeradores), con conversion de unidades correcta
    for r in csv.DictReader(open(os.path.join(OUT,"hhi_numeradores.csv"),encoding="utf-8")):
        if not r["total_nacional"]: continue
        a=int(r["anio_dato"])
        if not (2004<=a<=2018): continue
        k=(r["mineral"].lower(), a)
        try: v=float(r["total_nacional"])
        except: continue
        seen[k]=to_tonnes(v, r["unidad_total"])
    # 2019-2022: USGS MYB 2022 (completo y homogeneo; CAMIMEX tiene huecos ahi)
    rec=os.path.join(OUT,"produccion_nacional_myb_2019_2022.csv")
    if os.path.exists(rec):
        for r in csv.DictReader(open(rec,encoding="utf-8")):
            seen[(r["mineral"].lower(), int(r["anio"]))]=float(r["vol_t"])
    return seen

def export_series():
    byyear=collections.defaultdict(dict)
    for r in csv.DictReader(open(os.path.join(OUT,"comercio_posicion_1992_2024.csv"),encoding="utf-8")):
        a=int(r["anio"]); byyear[a][r["mineral"]]=float(r["X_total_usd"] or 0)
    return byyear

def main():
    # ---- (1) EXPORTACIONES ----
    byyear=export_series()
    rows=[]
    for a in sorted(byyear):
        blk=sum(byyear[a].values())/1e6  # MUSD
        nac=X_NAC.get(a)
        share=100*blk/nac if nac else None
        row=dict(anio=a, X_bloque_musd=round(blk,1), X_nacional_musd=nac,
                 share_bloque_pct=round(share,3) if share else "")
        rows.append(row)
    f1=os.path.join(OUT,"peso_bloque_hist_exportaciones.csv")
    with open(f1,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    # sub-periodos CAGR
    def cagr(a0,a1):
        v0=sum(byyear[a0].values()); v1=sum(byyear[a1].values())
        return (v1/v0)**(1/(a1-a0))-1
    print("=== EXPORTACIONES bloque (MUSD) y share del total nacional ===")
    for a in [1992,2000,2003,2008,2013,2018,2020,2024]:
        r=[x for x in rows if x["anio"]==a][0]
        print(f"  {a}: bloque {r['X_bloque_musd']:>10,.0f}  nacional {r['X_nacional_musd']:>8,} MUSD  share {r['share_bloque_pct']}%")
    print(f"  CAGR 1992-2024 {100*cagr(1992,2024):.1f}% | 1992-2003 {100*cagr(1992,2003):.1f}% | 2003-2013 {100*cagr(2003,2013):.1f}% | 2013-2024 {100*cagr(2013,2024):.1f}%")
    print(f"  share min {min(x['share_bloque_pct'] for x in rows if x['share_bloque_pct']!='')}% ; max {max(x['share_bloque_pct'] for x in rows if x['share_bloque_pct']!='')}%")

    # ---- (2) VALOR DE PRODUCCION 2004-2024 ----
    prices=load_prices(); vols=load_natvol()
    NM={"cobre":"cobre","oro":"oro","plata":"plata","plomo":"plomo","zinc":"zinc","barita":"barita",
        "fluorita":"fluorita","grafito":"grafito","manganeso":"manganeso","silice":"silice"}
    MINS10=set(NM.keys())
    complete=set()
    tmp=collections.defaultdict(set)
    for (m,a) in vols:
        if m in MINS10: tmp[a].add(m)
    complete={a for a,ms in tmp.items() if ms>=MINS10}  # anios con los 10 minerales
    prod=[]
    byyr_prod=collections.defaultdict(dict)
    for (m,a),vt in sorted(vols.items()):
        pm=NM.get(m)
        if not pm: continue
        pr=prices.get(pm,{}).get(a)
        if pr is None: continue
        val=vt*pr
        byyr_prod[a][m]=val
        prod.append(dict(anio=a,mineral=m,vol_t=round(vt,2),precio_usd_t=round(pr,2),
                         valor_prod_usd=round(val), anio_completo=("si" if a in complete else "no")))
    # shares por mineral dentro del bloque (solo informativo; leer con cuidado en anios no completos)
    for r in prod:
        tot=sum(byyr_prod[r["anio"]].values())
        r["share_bloque_pct"]=round(100*r["valor_prod_usd"]/tot,2) if tot else ""
    f2=os.path.join(OUT,"peso_bloque_hist_produccion.csv")
    with open(f2,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["anio","mineral","vol_t","precio_usd_t","valor_prod_usd","share_bloque_pct","anio_completo"])
        w.writeheader(); w.writerows(prod)
    print("\n=== VALOR DE PRODUCCION del bloque (MUSD) — anios COMPLETOS (los 10 minerales) ===")
    for a in sorted(complete):
        tot=sum(byyr_prod[a].values())/1e6
        print(f"  {a}: {tot:>10,.0f} MUSD")
    print(f"  anios completos: {min(complete)}-{max(complete)} ; incompletos (gaps de volumen): {sorted(set(byyr_prod)-complete)}")
    for a in (1992,2003,2018):
        if a not in byyr_prod: continue
        tot=sum(byyr_prod[a].values())
        comp=sorted(byyr_prod[a].items(),key=lambda kv:-kv[1])[:5]
        print(f"  comp {a}: "+", ".join(f"{m} {100*v/tot:.0f}%" for m,v in comp))
    # descomposicion precio vs volumen del bloque, base 1992
    b=1992; e=2018
    vb=sum(byyr_prod[b].values()); ve=sum(byyr_prod[e].values())
    volidx=sum(vols[(m,e)]*prices[NM[m]][b] for m in MINS10 if (m,e) in vols and b in prices.get(NM[m],{}))
    print(f"  {b}->{e}: valor x{ve/vb:.2f} ; volumen (a precios {b}) x{volidx/vb:.2f} ; efecto precio x{ve/volidx:.2f}")
    print("\nEscritos:\n ",f1,"\n ",f2)

if __name__=="__main__":
    main()
