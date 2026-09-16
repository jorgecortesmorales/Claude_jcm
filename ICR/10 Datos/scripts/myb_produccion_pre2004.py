# -*- coding: utf-8 -*-
"""Extrae la produccion nacional 1998-2003 de los 10 minerales desde los USGS MYB Mexico
(Tabla 1) en formato .xls (2002 = 1998-2002; 2003 = 2003), normaliza a toneladas y escribe
processed/produccion_nacional_myb_pre2004.csv (mineral, anio, vol_t, fuente, nota).
Unidades USGS: oro/plata en kilogramos; fluorita en miles de toneladas; resto en toneladas.
Manganeso: se usa 'Mn content' (no gross weight) para empatar con la base CAMIMEX 2004+.
"""
import pandas as pd, os, re

MYB=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\Bases Originales\07 USGS MCS\MYB Mexico"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

def num(c):
    s=str(c).strip().replace(",","")
    if re.fullmatch(r"-?\d+(\.\d+)?", s): return float(s)
    return None

def rightmost_n(cells, n=5):
    vals=[num(c) for c in cells]
    vals=[v for v in vals if v is not None]
    return vals[-n:] if len(vals)>=n else vals

def find_row(df, pred):
    for i in range(len(df)):
        c0=str(df.iloc[i,0]).strip()
        if pred(c0): return i
    return None

def extract(path, years):
    df=pd.read_excel(path, sheet_name=0, header=None)
    n=len(years)
    out={}
    def grab(idx, unit=1.0):
        row=[df.iloc[idx,j] for j in range(df.shape[1])]
        vals=rightmost_n(row, n)
        return [v*unit for v in vals] if len(vals)==n else None
    # cobre: Total de mine output (fila siguiente a 'Leaching, electrowon')
    i=find_row(df, lambda c: c.startswith("Leaching, electrowon"));  out["cobre"]=grab(i+1) if i else None
    # oro / plata: 'Mine output, Au/Ag content' (kilogramos -> t)
    i=find_row(df, lambda c: c.startswith("Mine output, Au content")); out["oro"]=grab(i,0.001) if i else None
    i=find_row(df, lambda c: c.startswith("Mine output, Ag content")); out["plata"]=grab(i,0.001) if i else None
    # plomo / zinc
    i=find_row(df, lambda c: c.startswith("Mine output, Pb content")); out["plomo"]=grab(i) if i else None
    i=find_row(df, lambda c: c.startswith("Mine output, Zn content")); out["zinc"]=grab(i) if i else None
    # barita
    i=find_row(df, lambda c: c=="Barite"); out["barita"]=grab(i) if i else None
    # fluorita: 'Total' tras 'Metallurgical-grade' (miles de t -> t)
    i=find_row(df, lambda c: c.startswith("Metallurgical-grade")); out["fluorita"]=grab(i+1,1000.0) if i else None
    # grafito amorfo (2003: 'Graphite, natural, amorphous' en una fila; 2002: 'Amorphous' bajo 'Graphite, natural:')
    i=find_row(df, lambda c: c.startswith("Graphite, natural, amorphous"))
    if i is None:
        g=find_row(df, lambda c: c.startswith("Graphite, natural"))
        i=find_row(df, lambda c: c.startswith("Amorphous")) if g is not None else None
    out["grafito"]=grab(i) if i else None
    # manganeso: 'Mn content' (empata base CAMIMEX)
    i=find_row(df, lambda c: c.startswith("Mn content")); out["manganeso"]=grab(i) if i else None
    # silice: 'Quartz, quartzite, glass sand (silica)'
    i=find_row(df, lambda c: "silica" in c.lower()); out["silice"]=grab(i) if i else None
    rows=[]
    for m,vals in out.items():
        if not vals: print("  FALTA", m, "en", os.path.basename(path)); continue
        for y,v in zip(years, vals):
            rows.append((m,y,round(v,1)))
    return rows

# 1992-1997 transcritos de imagen de la Tabla 1 (pdftoppm) — capitulo 1996 (1992-93) y 1998 (1994-97).
# Unidades ya normalizadas a toneladas: oro/plata de kg->t; fluorita de miles t->t; manganeso = Mn content.
IMG = {
 # mineral: {anio: vol_t}
 "cobre":    {1992:279000,1993:301100,1994:294688,1995:333565,1996:340710,1997:390536},
 "oro":      {1992:9.89,1993:9.77,1994:13.888,1995:20.292,1996:24.477,1997:26.001},
 "plata":    {1992:2100.0,1993:2110.0,1994:2214.638,1995:2324.348,1996:2527.875,1997:2679.09},
 "plomo":    {1992:170000,1993:149000,1994:170322,1995:164348,1996:173831,1997:174661},
 "zinc":     {1992:294000,1993:369000,1994:381689,1995:363658,1996:377599,1997:379252},
 "barita":   {1992:188000,1993:136000,1994:86605,1995:248367,1996:470028,1997:236606},
 "fluorita": {1992:287000,1993:283000,1994:235000,1995:522000,1996:524000,1997:553000},
 "grafito":  {1992:30500,1993:42600,1994:29903,1995:32938,1996:38967,1997:46707},
 "manganeso":{1992:153000,1993:135000,1994:112300,1995:174200,1996:173380,1997:192825},
 "silice":   {1992:1130000,1993:1310000,1994:1360549,1995:1292265,1996:1424825,1997:1564348},
}

# 2018-2022 transcritos de imagen de la Tabla 1 del capitulo USGS MYB 2022 (cubre 2018-2022).
# 2018 se incluye solo para VALIDAR el empalme contra CAMIMEX (no se usa en la serie).
# Unidades ya en toneladas: oro/plata kg->t; fluorita = acid+metallurgical (miles t)->t; manganeso = Mn content.
IMG_RECENT = {
 "cobre":    {2018:696600,2019:713700,2020:732900,2021:734100,2022:753900},
 "oro":      {2018:117.323,2019:111.404,2020:101.631,2021:120.0,2022:120.0},
 "plata":    {2018:6049.626,2019:5841.233,2020:5604.847,2021:6096.281,2022:6195.813},
 "plomo":    {2018:240304,2019:259457,2020:260390,2021:272231,2022:273000},
 "zinc":     {2018:690895,2019:676677,2020:688461,2021:742926,2022:744341},
 "barita":   {2018:366234,2019:378295,2020:372262,2021:320642,2022:315736},
 "fluorita": {2018:1180000,2019:1230000,2020:910000,2021:1000000,2022:1000000},  # acid+metallurgical
 "grafito":  {2018:4130,2019:2300,2020:2033,2021:1800,2022:2000},
 "manganeso":{2018:209023,2019:219046,2020:218606,2021:220560,2022:221123},
 "silice":   {2018:2511246,2019:2671422,2020:2514378,2021:2500000,2022:2700000},
}

def main():
    r02=extract(os.path.join(MYB,"myb-mexico-2002.xls"), [1998,1999,2000,2001,2002])
    r03=extract(os.path.join(MYB,"myb-mexico-2003.xls"), [1999,2000,2001,2002,2003])
    # 1998-2002 de 2002.xls ; 2003 de 2003.xls ; usar 2003.xls solo para 2003
    data={}; src={}
    for m,ys in IMG.items():
        for y,v in ys.items(): data[(m,y)]=v; src[(m,y)]="USGS MYB Table 1 (imagen)"
    for m,y,v in r02: data[(m,y)]=v; src[(m,y)]="USGS MYB Table 1 (xls 2002)"
    for m,y,v in r03:
        if y==2003: data[(m,y)]=v; src[(m,y)]="USGS MYB Table 1 (xls 2003)"
    # control de consistencia: 1999-2002 deben coincidir entre ambos capitulos
    disc=[]
    d03={(m,y):v for m,y,v in r03}
    for (m,y),v in list(data.items()):
        if 1999<=y<=2002 and (m,y) in d03 and abs(v-d03[(m,y)])/max(v,1)>0.02:
            disc.append((m,y,v,d03[(m,y)]))
    outp=os.path.join(OUT,"produccion_nacional_myb_pre2004.csv")
    import csv
    with open(outp,"w",encoding="utf-8",newline="") as fh:
        w=csv.writer(fh); w.writerow(["mineral","anio","vol_t","fuente"])
        for (m,y),v in sorted(data.items()):
            w.writerow([m,y,round(v,3),src.get((m,y),"USGS MYB")])
    print("Escrito:",outp,"filas:",len(data),"| años",min(y for _,y in data),"-",max(y for _,y in data))
    print("Discrepancias 2002vs2003 (>2%):", disc if disc else "ninguna")

    # --- Bloque reciente 2019-2022 (USGS MYB 2022) + validacion de empalme 2018 vs CAMIMEX ---
    OZ_T=lambda v,u: v*0.0311034768 if u.strip().lower().startswith("miles oz") else (v if "tonel" in u.lower() else v)
    cam2018={}
    for r in csv.DictReader(open(os.path.join(OUT,"hhi_numeradores.csv"),encoding="utf-8")):
        if r["anio_dato"]=="2018" and r["total_nacional"]:
            m=r["mineral"].lower()
            try: cam2018[m]=OZ_T(float(r["total_nacional"]), r["unidad_total"])
            except: pass
    print("\nEmpalme 2018 (USGS vs CAMIMEX):")
    for m in ["cobre","oro","plata","plomo","zinc","barita","fluorita","grafito","manganeso","silice"]:
        u=IMG_RECENT[m][2018]; c=cam2018.get(m)
        d=f"{100*(u-c)/c:+.0f}%" if c else "s/d"
        print(f"  {m:10s} USGS {u:>10.1f}  CAMIMEX {(c or 0):>10.1f}  dif {d}")
    outr=os.path.join(OUT,"produccion_nacional_myb_2019_2022.csv")
    with open(outr,"w",encoding="utf-8",newline="") as fh:
        w=csv.writer(fh); w.writerow(["mineral","anio","vol_t","fuente"])
        for m,ys in IMG_RECENT.items():
            for y,v in ys.items():
                if y>=2019: w.writerow([m,y,round(v,3),"USGS MYB 2022 Table 1 (imagen)"])
    print("Escrito:",outr)
    mins=["cobre","oro","plata","plomo","zinc","barita","fluorita","grafito","manganeso","silice"]
    print("\nmineral    "+" ".join(f"{y:>9}" for y in range(1992,2004)))
    for m in mins:
        print(f"{m:10s} "+" ".join(f"{data.get((m,y),0):>9.0f}" for y in range(1992,2004)))

if __name__=="__main__":
    main()
