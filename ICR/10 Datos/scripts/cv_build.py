# -*- coding: utf-8 -*-
"""
Actividad B — Construcción de las cadenas de valor locales (Fases 1 y 3 de la Ruta).
PILOTO: cobre (tipo B truncado) y fluorita (caso límite A/B).

Produce dos salidas, table-driven desde MAPEO (extensible a los 10 minerales):
  processed/cv_arbol_mineral.csv        (Fase 1: árbol L1-L4 con HS/SCIAN/coef/atribuible)
  processed/cv_eslabones_cuantificado.csv (Fase 3: VBP/PIB/empleo (MIP) + X/M (comercio) por eslabón)

Cuantificación de eslabones aguas abajo: la MIP INEGI (tabla producto x producto, 834 clases
SCIAN) expone una columna por clase; se leen las filas P.1 (VBP), B.1bP (PIB), PT (empleo),
D.1 (remuneraciones) para la clase SCIAN de CADA eslabón (mismo método que peso_bloque.py).
  - atribuible=si  -> existe clase SCIAN dedicada al mineral (p.ej. 331411 fundición de cobre):
                      el VBP de la clase es atribuible a la cadena del mineral.
  - atribuible=no  -> la etapa cae en una clase SCIAN agregada (p.ej. HF en 325180 'quimicos
                      basicos inorganicos', que mezcla muchos productos) o es un uso multi-insumo
                      (cable, vidrio): el VBP de la clase NO es atribuible; se ancla con comercio.
Comercio por etapa (X/M en USD, promedio 2018-2023) desde comercio_por_etapa_1992_2024.csv.
"""
import csv, os
BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
MIPB = os.path.join(BASE, "Bases Originales", "10 MIP INEGI")
OUT  = os.path.join(BASE, "processed")
YEARS = {
    "2013": os.path.join(MIPB, "2013", "conjunto_de_datos", "mip_t_pb_pxp_4.csv"),
    "2018": os.path.join(MIPB, "2018", "conjunto de datos", "conjunto_de_datos_mip_t_pb_pxp_42018.csv"),
}

# --- MAPEO: mineral -> lista de eslabones. Cada eslabon:
#   (nivel L, etapa E, descripcion, [SCIAN...], [HS...], atribuible, coef_tecnico, fuente_coef)
MAPEO = {
 "cobre": [
   ("L1","E1","Extracción y beneficio (mina -> concentrado ~28% Cu)",
        ["212231"], ["2603"], "si", "ley concentrado ~25-30% Cu", "USGS/CAMIMEX"),
   ("L2","E2","Fundición y refinación (concentrado -> ánodo/blister 98-99% -> cátodo 99.99%)",
        ["331411"], ["7401","7402","7403","7405"], "si", "~3.5 t concentrado (28%) / t cátodo", "USGS"),
   ("L3","E3","Semimanufactura (cátodo -> alambrón, laminados, tubos, alambre)",
        ["331420"], ["7407","7408","7409","7410","7411","7412","7413"], "si", "cátodo -> alambrón (rend. ~0.98)", "literatura"),
   ("L4","E4","Manufactura final / uso (alambrón -> cable y conductores; accesorios)",
        ["335999"], ["7415","7418","7419","8544"], "no", "no atribuible a un solo mineral", "Ruta caveat L4"),
 ],
 "fluorita": [
   ("L1","E1","Extracción y beneficio (mina -> espato flúor: grado metalúrgico ~85% / ácido >97% CaF2)",
        ["212395"], ["252921","252922"], "si", "grado ácido >97% CaF2", "USGS/CAMIMEX"),
   ("L2","E2","Fluoroquímica: ácido fluorhídrico HF (CaF2 + H2SO4 -> 2HF + CaSO4)",
        ["325180"], ["281111"], "no", "~2.1 t espato ácido / t HF", "estequiometría"),
   ("L3","E3","Fluoroquímicos intermedios (HF -> gases refrigerantes, sales de flúor)",
        ["325190"], ["282612","282619"], "no", "clase SCIAN agregada", "—"),
   ("L4","E4","Fluoropolímeros (PTFE) y usos finales — no se producen en México",
        ["325211"], ["390461"], "no", "eslabón ausente (importado)", "comercio (ausente)"),
 ],
 "oro": [
   ("L1","E1","Extracción y beneficio (mina -> mena/concentrado con oro)",
        ["212221"], ["261610"], "si", "oro se recupera junto a Cu/Ag", "USGS/CAMIMEX"),
   ("L2","E2","Fundición y refinación de metales preciosos (doré -> oro refinado)",
        ["331412"], ["7108"], "comp:oro+plata", "clase compartida oro+plata", "MIP"),
   ("L4","E4","Joyería y orfebrería (uso final) — importador neto",
        ["339910"], ["7113","7114","7115"], "no", "uso multi-insumo; importado", "comercio"),
 ],
 "plata": [
   ("L1","E1","Extracción y beneficio (mina -> mena/concentrado con plata)",
        ["212222"], ["261690"], "si", "plata subproducto de Pb-Zn y epitermales", "USGS/CAMIMEX"),
   ("L2","E2","Fundición y refinación de metales preciosos (doré -> plata refinada)",
        ["331412"], ["7106"], "comp:oro+plata", "clase compartida oro+plata", "MIP"),
   ("L4","E4","Joyería y orfebrería (uso final) — importador neto",
        ["339910"], ["7113","7114","7115"], "no", "uso multi-insumo; importado", "comercio"),
 ],
 "plomo": [
   ("L1","E1","Extracción y beneficio (mina -> concentrado de plomo; coextracción con zinc)",
        ["212232"], ["2607"], "comp:plomo+zinc", "L1 INEGI combina plomo-zinc", "USGS/CAMIMEX"),
   ("L2","E2","Fundición y refinación (concentrado -> plomo refinado)",
        ["331419"], ["7801"], "comp:plomo+zinc+otros no ferrosos", "clase compartida", "MIP"),
   ("L3","E3","Semimanufactura de plomo (barras, láminas, tubos)",
        ["331490"], ["7804"], "no", "clase compartida no ferrosos", "—"),
   ("L4","E4","Baterías plomo-ácido (uso final) — Clarios/LTH, con reciclaje",
        ["335910"], ["7806"], "no", "baterías; insumo mayormente reciclado", "empresas"),
 ],
 "zinc": [
   ("L1","E1","Extracción y beneficio (mina -> concentrado de zinc; coextracción con plomo)",
        ["212232"], ["2608"], "comp:plomo+zinc", "L1 INEGI combina plomo-zinc", "USGS/CAMIMEX"),
   ("L2","E2","Fundición y refinación (concentrado -> zinc refinado; IMMSA/Met-Mex)",
        ["331419"], ["7901"], "comp:plomo+zinc+otros no ferrosos", "clase compartida", "MIP"),
   ("L3","E3","Semimanufactura de zinc (planchas, polvo, aleaciones)",
        ["331490"], ["7903","7904","7905"], "no", "clase compartida no ferrosos", "—"),
   ("L4","E4","Galvanizado y usos finales",
        ["332810"], ["7907"], "no", "uso multi-insumo", "comercio"),
 ],
 "manganeso": [
   ("L1","E1","Extracción y beneficio (mina Molango -> mena/nódulos de Mn)",
        ["212291"], ["2602"], "si", "usar contenido de Mn", "USGS/CAMIMEX"),
   ("L2","E2","Ferroaleaciones: ferro- y silicomanganeso (Autlán)",
        ["331112"], ["720211","720219","720230"], "comp:ferroaleaciones+acero+ferrosilicio",
        "Autlán, clase compartida con siderurgia", "MIP/empresas"),
   ("L3","E3","Compuestos químicos y metal de Mn (dióxido, sulfato)",
        ["325180"], ["282010","8111"], "no", "clase SCIAN agregada", "—"),
 ],
 "grafito": [
   ("L1","E1","Extracción y beneficio (grafito natural en hojuela/amorfo)",
        ["212396"], ["250410","250490"], "si", "producción decreciente", "USGS/CAMIMEX"),
   ("L2","E2","Grafito artificial y preparaciones",
        ["325180"], ["3801"], "no", "clase agregada; mayormente importado", "comercio"),
   ("L3","E3","Electrodos y artículos de carbono/grafito — importador neto",
        ["327999"], ["8545"], "no", "sin clase dedicada; importado", "comercio"),
   ("L4","E4","Uso: acería por horno de arco eléctrico (EAF), refractarios, baterías",
        ["331111"], [], "no", "usuario multi-insumo (siderurgia)", "empresas"),
 ],
 "silice": [
   ("L1","E1","Extracción y beneficio (arena sílica / cuarzo)",
        ["212324"], ["250510","250610"], "si", "grados vidrio/fundición", "USGS/CAMIMEX"),
   ("L2","E2","Silicio metálico / ferrosilicio / sílice pirogénica — importador neto",
        ["331112"], ["280461","280469","720221","720229","281122"], "no",
        "silicio importado; clase compartida", "comercio"),
   ("L4","E4","Uso: vidrio (Vitro, O-I) y cemento/cerámica",
        ["327211"], [], "no", "usuario multi-insumo (vidrio/cemento)", "empresas"),
 ],
 "barita": [
   ("L1","E1","Extracción y beneficio (barita cruda/molida grado API)",
        ["212393"], ["251110"], "si", "grado perforación (densidad >4.2)", "USGS/CAMIMEX"),
   ("L2","E2","Químicos de bario (sulfato, carbonato) — mínimo/importado",
        ["325180"], ["281640","283660"], "no", "clase agregada; poco/importado", "comercio"),
   ("L4","E4","Uso: densificante de lodos de perforación petrolera (PEMEX)",
        ["213111"], [], "no", "usuario (perforación de pozos)", "empresas"),
 ],
}

def code_of(lab): return lab.split("---")[0].strip().lstrip("\ufeff")
def num(x):
    x=(x or "").strip().replace(",","")
    try: return float(x)
    except: return 0.0

def load_year(path):
    rows=list(csv.reader(open(path,encoding="cp1252")))
    hdr=rows[0]; prodcol={}
    for j,h in enumerate(hdr):
        if h.startswith("DI---Demanda intermedia|"):
            rest=h.split("|",1)[1]
            if rest.strip()=="Total": continue
            prodcol[code_of(rest)]=j
    def find_row(prefix):
        for r in rows[1:]:
            if r[0].startswith(prefix): return r
        return None
    R=dict(pib=find_row("B.1bP---"), p1=find_row("P.1---"),
           pt=find_row("PT---Puestos"), d1=find_row("D.1---"))
    def val(rowkey, codes):
        row=R[rowkey]; s=0.0
        for c in codes:
            if row is not None and c in prodcol: s+=num(row[prodcol[c]])
        return s
    return val, prodcol

def load_comercio():
    """X/M promedio 2018-2023 por mineral y etapa (E1..E4), en MUSD."""
    agg={}
    for r in csv.DictReader(open(os.path.join(OUT,"comercio_por_etapa_1992_2024.csv"),encoding="utf-8")):
        a=int(r["anio"])
        if not (2018<=a<=2023): continue
        et=r["etapa"].split()[0]  # 'E1'..'E4'
        key=(r["mineral"], et, r["flujo"])
        agg.setdefault(key,[]).append(float(r["valor_usd"]))
    prom={k: (sum(v)/len(v)) for k,v in agg.items()}
    return prom

def main():
    vals={y:load_year(p) for y,p in YEARS.items()}
    com=load_comercio()
    arbol=[]; cuant=[]
    for mineral, eslabones in MAPEO.items():
        for (L,E,desc,scian,hs,atrib,coef,fte) in eslabones:
            arbol.append(dict(mineral=mineral, eslabon=L, etapa=E, descripcion=desc,
                scian=";".join(scian), hs=";".join(hs), atribuible_mip=atrib,
                coef_tecnico=coef, fuente_coef=fte))
            row=dict(mineral=mineral, eslabon=L, etapa=E, scian=";".join(scian),
                     atribuible_mip=atrib)
            nota_clase=""
            es_comp = atrib.startswith("comp")
            for y,(val,pc) in vals.items():
                vbp=round(val("p1",scian),1); pib=round(val("pib",scian),1); pt=int(round(val("pt",scian)))
                if atrib=="si" or es_comp:
                    # 'si' = clase dedicada al mineral; 'comp' = clase compartida (se muestra con nota)
                    row[f"vbp_mmp_{y}"]=vbp; row[f"pib_mmp_{y}"]=pib; row[f"empleo_{y}"]=pt
                else:
                    # clase SCIAN agregada o uso multi-insumo: NO atribuible a la cadena del mineral
                    row[f"vbp_mmp_{y}"]=""; row[f"pib_mmp_{y}"]=""; row[f"empleo_{y}"]=""
                    nota_clase+=f"VBP clase agregada {y}={vbp:,.0f} mmp; "
            if es_comp:
                nota_clase = "CLASE COMPARTIDA (" + atrib.split(":",1)[1] + "): VBP no separable por mineral"
            row["nota_clase_no_atribuible"]=nota_clase.strip()
            # comercio (promedio 2018-2023, MUSD)
            X=com.get((mineral,E,"X")); M=com.get((mineral,E,"M"))
            row["X_musd_1823"]=round(X/1e6,2) if X is not None else ""
            row["M_musd_1823"]=round(M/1e6,2) if M is not None else ""
            cuant.append(row)
    fa=os.path.join(OUT,"cv_arbol_mineral.csv")
    with open(fa,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(arbol[0].keys())); w.writeheader(); w.writerows(arbol)
    fc=os.path.join(OUT,"cv_eslabones_cuantificado.csv")
    with open(fc,"w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(cuant[0].keys())); w.writeheader(); w.writerows(cuant)
    print("Escrito:",fa); print("Escrito:",fc)
    # resumen en consola
    for r in cuant:
        vbp=f"{r['vbp_mmp_2018']:,.1f}" if r['vbp_mmp_2018']!="" else "n/a(agreg)"
        pt =f"{r['empleo_2018']:,d}" if r['empleo_2018']!="" else "n/a"
        print(f"{r['mineral']:9s} {r['eslabon']} {r['etapa']} atrib={r['atribuible_mip']:3s} "
              f"VBP18={vbp:>12} PT18={pt:>9} "
              f"X={str(r['X_musd_1823']) or '-':>8} M={str(r['M_musd_1823']) or '-':>8}  scian={r['scian']}")

if __name__=="__main__":
    main()
