# -*- coding: utf-8 -*-
"""
Actividad A — Peso del bloque de 10 minerales criticos en la economia.
Fuente PRIMARIA y autoconsistente: MIP INEGI 2013 y 2018 (tabla TOTAL producto x producto).
De la MIP se leen, por sector-columna (producto SCIAN Clase):
  B.1bP  = Producto interno bruto (PIB, valor agregado a precios basicos)  -> peso en el PIB
  P.1    = Produccion bruta (VBP)                                          -> peso en produccion
  PT     = Puestos de trabajo (empleo)                                     -> peso en el empleo (desarrollo industrial)
  D.1    = Remuneracion de asalariados
Denominadores autoconsistentes (misma MIP):
  economia total = suma sobre TODAS las columnas-producto
  mineria 212    = columnas cuyo codigo empieza en 212 (mineria de min. metalicos y no metalicos, excl. petroleo/gas)
  mineria 21     = columnas 21x (incluye 211 petroleo/gas, 213 servicios) -> contexto
Los 10 minerales = 9 clases SCIAN (plomo-zinc combinado, coextraccion INEGI).
Exportaciones: serie Comtrade in-vault (comercio_posicion_1992_2024.csv); los denominadores
nacionales de exportacion son EXTERNOS (INEGI/Banxico) -> se anotan aparte (peso_bloque_exportaciones).
Salidas: processed/peso_bloque_mineria.csv (por mineral, bloque y totales, 2013/2018)
         processed/peso_bloque_exportaciones.csv (bloque y por mineral, serie 1992-2024)
"""
import csv, os
import numpy as np

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\Bases Originales\10 MIP INEGI"
OUT  = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

YEARS = {
    "2013": os.path.join(BASE, "2013", "conjunto_de_datos", "mip_t_pb_pxp_4.csv"),
    "2018": os.path.join(BASE, "2018", "conjunto de datos", "conjunto_de_datos_mip_t_pb_pxp_42018.csv"),
}
MINERALES = [("212393","barita"),("212231","cobre"),("212395","fluorita"),("212396","grafito"),
             ("212291","manganeso"),("212221","oro"),("212222","plata"),("212232","plomo-zinc"),
             ("212324","silice")]
MIN_CODES = {c for c,_ in MINERALES}

def code_of(lab): return lab.split("---")[0].strip().lstrip("\ufeff")
def num(x):
    x=(x or "").strip().replace(",","")
    try: return float(x)
    except: return 0.0

def load_year(path):
    rows=list(csv.reader(open(path,encoding="cp1252")))
    hdr=rows[0]
    # columnas-producto: 'DI---Demanda intermedia|<code>---<name>' (excluye |Total)
    prodcol={}  # code -> col index
    for j,h in enumerate(hdr):
        if h.startswith("DI---Demanda intermedia|"):
            rest=h.split("|",1)[1]
            if rest.strip()=="Total": continue
            prodcol[code_of(rest)]=j
    # localizar filas de interes por prefijo del descriptor
    def find_row(prefix):
        for r in rows[1:]:
            if r[0].startswith(prefix): return r
        return None
    row_pib=find_row("B.1bP---")   # PIB
    row_vab=find_row("B.1bV---")   # VAB
    row_p1 =find_row("P.1---")     # produccion bruta
    row_pt =find_row("PT---Puestos")
    row_d1 =find_row("D.1---")     # remuneraciones
    def val(row,code): return num(row[prodcol[code]]) if (row is not None and code in prodcol) else 0.0
    # totales economia = suma sobre todas las columnas-producto
    def total(row): return sum(num(row[j]) for j in prodcol.values()) if row is not None else 0.0
    def total_pref(row,pref): return sum(num(row[j]) for c,j in prodcol.items() if c.startswith(pref)) if row is not None else 0.0
    return dict(rows=rows, prodcol=prodcol,
                pib=row_pib, vab=row_vab, p1=row_p1, pt=row_pt, d1=row_d1,
                val=val, total=total, total_pref=total_pref)

def main():
    allrows=[]
    for year,path in YEARS.items():
        Y=load_year(path)
        econ_pib=Y["total"](Y["pib"]); econ_vbp=Y["total"](Y["p1"]); econ_pt=Y["total"](Y["pt"])
        m212_pib=Y["total_pref"](Y["pib"],"212"); m212_vbp=Y["total_pref"](Y["p1"],"212"); m212_pt=Y["total_pref"](Y["pt"],"212")
        m21_pib =Y["total_pref"](Y["pib"],"21");  m21_vbp =Y["total_pref"](Y["p1"],"21")
        # por mineral
        blk=dict(pib=0.0,vbp=0.0,pt=0.0,d1=0.0)
        for code,mineral in MINERALES:
            pib=Y["val"](Y["pib"],code); vbp=Y["val"](Y["p1"],code)
            pt =Y["val"](Y["pt"],code);  d1 =Y["val"](Y["d1"],code)
            blk["pib"]+=pib; blk["vbp"]+=vbp; blk["pt"]+=pt; blk["d1"]+=d1
            allrows.append(dict(anio=year,nivel="mineral",codigo=code,mineral=mineral,
                pib_mmp=round(pib,1), vbp_mmp=round(vbp,1), pt_empleos=int(round(pt)), remun_mmp=round(d1,1),
                pct_pib_economia=round(100*pib/econ_pib,4), pct_pib_mineria212=round(100*pib/m212_pib,3) if m212_pib else None,
                pct_vbp_economia=round(100*vbp/econ_vbp,4), pct_vbp_mineria212=round(100*vbp/m212_vbp,3) if m212_vbp else None,
                pct_empleo_economia=round(100*pt/econ_pt,4) if econ_pt else None, pct_empleo_mineria212=round(100*pt/m212_pt,3) if m212_pt else None))
        # bloque
        allrows.append(dict(anio=year,nivel="BLOQUE_10",codigo="",mineral="bloque 10 minerales",
            pib_mmp=round(blk["pib"],1), vbp_mmp=round(blk["vbp"],1), pt_empleos=int(round(blk["pt"])), remun_mmp=round(blk["d1"],1),
            pct_pib_economia=round(100*blk["pib"]/econ_pib,4), pct_pib_mineria212=round(100*blk["pib"]/m212_pib,3) if m212_pib else None,
            pct_vbp_economia=round(100*blk["vbp"]/econ_vbp,4), pct_vbp_mineria212=round(100*blk["vbp"]/m212_vbp,3) if m212_vbp else None,
            pct_empleo_economia=round(100*blk["pt"]/econ_pt,4) if econ_pt else None, pct_empleo_mineria212=round(100*blk["pt"]/m212_pt,3) if m212_pt else None))
        # totales de referencia
        for nom,pib,vbp,pt in [("TOTAL_economia",econ_pib,econ_vbp,econ_pt),
                               ("mineria_212",m212_pib,m212_vbp,m212_pt),
                               ("mineria_21",m21_pib,m21_vbp,0)]:
            allrows.append(dict(anio=year,nivel="referencia",codigo="",mineral=nom,
                pib_mmp=round(pib,1), vbp_mmp=round(vbp,1), pt_empleos=int(round(pt)), remun_mmp="",
                pct_pib_economia=round(100*pib/econ_pib,3), pct_pib_mineria212="",
                pct_vbp_economia=round(100*vbp/econ_vbp,3), pct_vbp_mineria212="",
                pct_empleo_economia=round(100*pt/econ_pt,3) if econ_pt else "", pct_empleo_mineria212=""))
        print(f"\n===== MIP {year} (mmpesos) =====")
        print(f"  PIB economia total  = {econ_pib:,.0f}")
        print(f"  PIB mineria 212     = {m212_pib:,.0f}  ({100*m212_pib/econ_pib:.3f}% del PIB)")
        print(f"  PIB bloque 10       = {blk['pib']:,.0f}  ({100*blk['pib']/econ_pib:.4f}% del PIB nacional; {100*blk['pib']/m212_pib:.2f}% de mineria212)")
        print(f"  VBP bloque 10       = {blk['vbp']:,.0f}  ({100*blk['vbp']/econ_vbp:.4f}% del VBP nacional)")
        print(f"  Empleo bloque 10    = {blk['pt']:,.0f} puestos ({100*blk['pt']/econ_pt:.4f}% del empleo nacional)")
    f1=os.path.join(OUT,"peso_bloque_mineria.csv")
    with open(f1,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(allrows[0].keys())); w.writeheader(); w.writerows(allrows)
    print("\nEscrito:",f1)

    # ---- Exportaciones (Comtrade in-vault) ----
    pos=list(csv.DictReader(open(os.path.join(OUT,"comercio_posicion_1992_2024.csv"),encoding="utf-8")))
    exp=[]
    byyear={}
    for r in pos:
        a=int(r["anio"]); v=float(r["X_total_usd"] or 0)
        byyear.setdefault(a,{})[r["mineral"]]=v
    for a in sorted(byyear):
        tot=sum(byyear[a].values())
        for m,v in sorted(byyear[a].items(),key=lambda kv:-kv[1]):
            exp.append(dict(anio=a,mineral=m,X_usd=round(v),X_musd=round(v/1e6,2),
                            pct_del_bloque=round(100*v/tot,2) if tot else None))
        exp.append(dict(anio=a,mineral="BLOQUE_10",X_usd=round(tot),X_musd=round(tot/1e6,2),pct_del_bloque=100.0))
    f2=os.path.join(OUT,"peso_bloque_exportaciones.csv")
    with open(f2,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(exp[0].keys())); w.writeheader(); w.writerows(exp)
    # CAGR del bloque 1992-2024
    b1992=sum(byyear[1992].values()); b2024=sum(byyear[2024].values())
    cagr=(b2024/b1992)**(1/(2024-1992))-1
    print(f"Exportaciones bloque: 1992 = {b1992/1e6:,.0f} MUSD  ->  2024 = {b2024/1e6:,.0f} MUSD  (CAGR {100*cagr:.1f}%)")
    print("Escrito:",f2)

if __name__=="__main__":
    main()
