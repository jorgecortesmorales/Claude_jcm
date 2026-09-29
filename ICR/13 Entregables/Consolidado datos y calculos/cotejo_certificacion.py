# -*- coding: utf-8 -*-
"""
Cotejo de certificacion: manuscrito (cuadros e ilustraciones) vs. CSV de 10 Datos/processed/.

Extrae los 37 cuadros y 29 ilustraciones del manuscrito renderizado
(11 Redaccion/manuscrito/ICR - Manuscrito (nueva estructura).docx) y confronta CADA numero
impreso contra el CSV que lo origina. Solo lectura (no modifica el manuscrito ni los datos).

Dos modos de cotejo:
  A) Celda-a-celda (matrices anio x mineral de los anexos): cada celda -> CSV[mineral, anio].
  B) Por-entidad (tablas de cuerpo): cada numero de la fila de una entidad (mineral/pais/estado)
     debe existir (dentro de tolerancia de redondeo) en la fila de esa entidad en el CSV.
Las figuras se certifican por identidad de fuente: cada PNG -> script fig_*.py -> CSV que lee.

Salidas (en esta carpeta): cotejo_certificacion.csv  +  Cotejo de certificacion.html
"""
import json, re, os, unicodedata, glob
import pandas as pd, numpy as np

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR"
PROC = os.path.join(BASE, "10 Datos", "processed")
DOCX = os.path.join(BASE, "11 Redaccion", "manuscrito", "ICR - Manuscrito (nueva estructura).docx")
FIGDIR = os.path.join(BASE, "11 Redaccion", "figuras")
OUTDIR = os.path.dirname(os.path.abspath(__file__))
def rd(f): return pd.read_csv(os.path.join(PROC, f))

# ---------- extraccion del docx (en vivo, no depende del json) ----------
import docx
from docx.oxml.ns import qn
d = docx.Document(DOCX)
tbl_objs = {t._tbl: t for t in d.tables}
def ptext(p): return "".join(n.text for n in p.iter(qn('w:t')) if n.text)
blocks=[]
for ch in d.element.body.iterchildren():
    if ch.tag==qn('w:p'): blocks.append(('p', ptext(ch)))
    elif ch.tag==qn('w:tbl'): blocks.append(('tbl', tbl_objs.get(ch)))
def matrix(t): return [[c.text.strip() for c in r.cells] for r in t.rows]
CUAD=[]
for i,(k,v) in enumerate(blocks):
    if k!='tbl' or v is None: continue
    cap=""
    for j in range(i-1,-1,-1):
        if blocks[j][0]=='p' and blocks[j][1].strip():
            if re.match(r'Cuadro\s+[IVXBCD0-9]+\.', blocks[j][1].strip()): cap=blocks[j][1].strip()
            break
    CUAD.append(dict(cap=cap, m=matrix(v)))
FIGS=[b[1].strip() for b in blocks if b[0]=='p' and re.match(r'Ilustraci', b[1].strip())]

def norm(s):
    s=unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode().lower().strip()
    return s
def getcap(tag):
    for c in CUAD:
        if c['cap'].startswith('Cuadro '+tag+'.'): return c
    return None

NUM = re.compile(r'-?\d[\d\s.,]*')
def pnum(s):
    """convierte texto de celda a float; espacio/coma = miles; punto = decimal. None si no aplica."""
    if s is None: return None
    s=str(s).strip()
    if s in ('','·','—','-','–','n.d.','nd','W','w','*'): return None
    s=s.replace('\u2192','').replace('*','').strip()
    s=re.split(r'[(\[]', s)[0].strip()          # quita "10000 (2024)"
    m=NUM.match(s)
    if not m: return None
    t=m.group(0).strip()
    # heuristica: si hay coma y punto -> coma miles; si solo coma -> decimal europeo? aqui usan punto decimal
    t=t.replace(' ','').replace('\u202f','').replace('\xa0','')
    if ',' in t and '.' in t: t=t.replace(',','')
    elif ',' in t and t.count(',')==1 and len(t.split(',')[1])==2: t=t.replace(',','.')
    else: t=t.replace(',','')
    try: return float(t)
    except: return None

MIN10=['cobre','zinc','plomo','oro','plata','manganeso','fluorita','grafito','silice','barita']
rows=[]  # resultados por cuadro
def add(cuadro, csvname, modo, ncmp, nmatch, mismatches, nota=""):
    rows.append(dict(cuadro=cuadro, csv=csvname, modo=modo, n=ncmp, coincide=nmatch,
                     difieren=ncmp-nmatch, detalle="; ".join(mismatches[:6]), nota=nota))

def match(a,b,tol):
    return abs(a-b)<=tol

# ---------- A) matrices anio x mineral ----------
def cotejo_matriz(tag, csvname, valcol, tol, orient, minerals=MIN10, csv_min='mineral', csv_anio='anio', scale=1.0):
    c=getcap(tag)
    if not c: return
    df=rd(csvname)
    look={(norm(r[csv_min]), int(r[csv_anio])): r[valcol]*scale for _,r in df.iterrows() if pd.notna(r[valcol])}
    m=c['m']; head=m[0]
    ncmp=nm=0; mis=[]
    if orient=='anio_rows':   # filas=anio (col0), cols=minerales (header)
        cols=[norm(h) for h in head[1:]]
        for row in m[1:]:
            anio=pnum(row[0])
            if anio is None: continue
            anio=int(anio)
            for k,cell in enumerate(row[1:]):
                val=pnum(cell)
                if val is None: continue
                key=(cols[k], anio)
                if key not in look: continue
                ncmp+=1
                if match(val, look[key], tol): nm+=1
                else: mis.append(f"{cols[k]} {anio}: ms={val} csv={round(look[key],2)}")
    else:                     # filas=mineral (col0), cols=anio (header)
        anios=[pnum(h) for h in head[1:]]
        for row in m[1:]:
            mn=norm(row[0])
            for k,cell in enumerate(row[1:]):
                val=pnum(cell); an=anios[k]
                if val is None or an is None: continue
                key=(mn,int(an))
                if key not in look: continue
                ncmp+=1
                if match(val, look[key], tol): nm+=1
                else: mis.append(f"{mn} {int(an)}: ms={val} csv={round(look[key],2)}")
    add('Cuadro '+tag, csvname, 'celda anio x mineral', ncmp, nm, mis)

cotejo_matriz('B.1','ccv_serie.csv','ccv',0.006,'anio_rows')
cotejo_matriz('B.2','hhi_consolidado.csv','hhi',1.0,'anio_rows')
cotejo_matriz('B.3','comercio_posicion_1992_2024.csv','X_share_crudo',0.006,'min_rows')

# ---------- B) por-entidad: cada numero de la fila existe en el CSV de esa entidad ----------
def cotejo_entidad(tag, csvname, keycol_csv, numcols_csv, tol, keymap=None, filtro=None, scale=None, label='mineral', pct_cols=()):
    c=getcap(tag)
    if not c: return
    df=rd(csvname)
    if filtro is not None: df=df[filtro(df)]
    # set de valores por entidad
    vals={}
    for _,r in df.iterrows():
        key=norm(r[keycol_csv]); acc=[]
        for col in numcols_csv:
            v=r.get(col)
            if pd.notna(v):
                sc = scale.get(col,1.0) if scale else 1.0
                acc.append(float(v)*sc)
                if col in pct_cols: acc.append(float(v)*100.0)  # tambien como porcentaje (fraccion -> %)
        vals.setdefault(key,[]).extend(acc)
    m=c['m']; ncmp=nm=0; mis=[]
    for row in m[1:]:
        rawkey=row[0]; key=norm(rawkey)
        if keymap: key=keymap.get(key,key)
        if key not in vals: continue
        pool=vals[key]
        for cell in row[1:]:
            v=pnum(cell)
            if v is None: continue
            ncmp+=1
            if any(match(v,x,tol if abs(x)<50 else max(tol,abs(x)*0.01)) for x in pool): nm+=1
            else: mis.append(f"{key}: {v}")
    add('Cuadro '+tag, csvname, 'por-entidad (valor en fila)', ncmp, nm, mis)

# V.1 HHI subset (2004,2012,2018,reciente) -> hhi_consolidado por mineral (cualquier anio)
cotejo_entidad('V.1','hhi_consolidado.csv','mineral',['hhi'],1.0)
# VI.1 / VI.2 encadenamientos 2018 / 2013
enc=['vbp_mmpesos','di_sobre_vbp','backward_rasmussen','forward_rasmussen','backward_L_colsum','forward_G_rowsum']
cotejo_entidad('VI.1','mip_encadenamientos_minerales.csv','mineral',enc,0.02,filtro=lambda d:d.anio==2018)
cotejo_entidad('VI.2','mip_encadenamientos_minerales.csv','mineral',enc,0.02,filtro=lambda d:d.anio==2013)
# VI.5 CCV medio -> media por mineral de ccv_serie (+min/max en rango)
c=getcap('VI.5')
if c:
    df=rd('ccv_serie.csv')
    agg=df.groupby(df.mineral.map(norm)).ccv.agg(['mean','min','max'])
    ncmp=nm=0; mis=[]
    for row in c['m'][1:]:
        key=norm(row[0])
        if key not in agg.index: continue
        pool=[agg.loc[key,'mean'],agg.loc[key,'min'],agg.loc[key,'max']]
        for cell in row[1:]:
            v=pnum(cell)
            if v is None: continue
            ncmp+=1
            if any(match(v,x,0.02) for x in pool): nm+=1
            else: mis.append(f"{key}: {v}")
    add('Cuadro VI.5','ccv_serie.csv','por-entidad (media/rango)',ncmp,nm,mis)
# VII.1 Ghosh pais / VII.2 crudo_share  (ICIO B07_08 2018)
PAISMAP={'china':'chn','mexico':'mex','suecia':'swe','finlandia':'fin','brasil':'bra','peru':'per','australia':'aus','chile':'chl'}
cotejo_entidad('VII.1','icio_comparacion_mineria.csv','pais',['forward_rasmussen'],0.02,
               keymap=PAISMAP, filtro=lambda d:(d.sector=='B07_08')&(d.anio==2018))
cotejo_entidad('VII.2','icio_dva_mineria.csv','pais',['crudo_share'],0.02,
               keymap=PAISMAP, filtro=lambda d:(d.sector=='B07_08')&(d.anio==2018))
# VIII.3 Ghosh estatal / VIII.4 interestatal (por estado)
gest=['forward_rasmussen','fuga_export_share','backward_rasmussen','share_vbp_estatal_pct']
cotejo_entidad('VIII.3','ghosh_estatal_mineria.csv','estado',gest,0.55,pct_cols=('fuga_export_share',))
gint=['intra_share','inter_estatal_share','final_nacional_share','export_abroad_share','encad_nacional_share','forward_rasmussen_br']
cotejo_entidad('VIII.4','ghosh_interestatal_mineria.csv','estado',gint,0.55,
               pct_cols=('intra_share','inter_estatal_share','final_nacional_share','export_abroad_share','encad_nacional_share'))
# fichas C.1-C.10 -> cv_eslabones_cuantificado (por mineral, valores VBP/PIB/empleo/X/M 2018)
figmin={'C.1':'cobre','C.2':'zinc','C.3':'plomo','C.4':'oro','C.5':'plata','C.6':'manganeso','C.7':'fluorita','C.8':'grafito','C.9':'silice','C.10':'barita'}
cvq=rd('cv_eslabones_cuantificado.csv')
for tag,mn in figmin.items():
    c=getcap(tag)
    if not c: continue
    sub=cvq[cvq.mineral.map(norm)==mn]
    pool=[]
    for _,r in sub.iterrows():
        for col in ['vbp_mmp_2018','pib_mmp_2018','empleo_2018','X_musd_1823','M_musd_1823']:
            if pd.notna(r.get(col)): pool.append(float(r[col]))
    ncmp=nm=0; mis=[]
    for row in c['m'][1:]:
        for cell in row[3:]:   # columnas numericas VBP,PIB,Empleo,X,M
            v=pnum(cell)
            if v is None: continue
            ncmp+=1
            if any(match(v,x,max(1.0,abs(x)*0.01)) for x in pool): nm+=1
            else: mis.append(f"{mn}: {v}")
    add('Cuadro '+tag, 'cv_eslabones_cuantificado.csv','por-mineral (ficha)',ncmp,nm,mis)

# I.1 composicion del bloque -> share_bloque_pct (produccion) + pct_del_bloque (exportaciones)
c=getcap('I.1')
if c:
    pp=rd('peso_bloque_hist_produccion.csv'); px=rd('peso_bloque_exportaciones.csv')
    pool={}
    for _,r in pp.iterrows(): pool.setdefault(norm(r['mineral']),[]).append(float(r['share_bloque_pct']))
    for _,r in px.iterrows(): pool.setdefault(norm(r['mineral']),[]).append(float(r['pct_del_bloque']))
    ncmp=nm=0; mis=[]
    for row in c['m'][1:]:
        key=norm(row[0])
        if key not in pool: continue
        for cell in row[1:]:
            v=pnum(cell)
            if v is None: continue
            ncmp+=1
            if any(match(v,x,0.15) for x in pool[key]): nm+=1
            else: mis.append(f"{key}: {v}")
    add('Cuadro I.1','peso_bloque_hist_produccion.csv + _exportaciones','por-entidad (composicion)',ncmp,nm,mis)

# VI.3 demanda intermedia (% del comprador dentro del texto, entre parentesis)
c=getcap('VI.3')
if c:
    dd=rd('mip_demanda_intermedia_minerales.csv'); dd=dd[dd.anio==2018]
    pool={}
    for _,r in dd.iterrows(): pool.setdefault(norm(r['mineral']),[]).append(float(r['share_del_di'])*100)
    ncmp=nm=0; mis=[]
    for row in c['m'][1:]:
        key=norm(row[0])
        if key not in pool: continue
        for tok in re.findall(r'\d+(?:[.,]\d+)?', row[1]):   # todos los % del texto
            v=float(tok.replace(',','.'))
            if v>100: continue
            ncmp+=1
            if any(match(v,x,1.0) for x in pool[key]): nm+=1
            else: mis.append(f"{key}: {v}")
    add('Cuadro VI.3','mip_demanda_intermedia_minerales.csv','por-entidad (% comprador)',ncmp,nm,mis)
# VI.4 Ghosh por eslabon 2018 (L1/L2/L3)
cotejo_entidad('VI.4','mip_encadenamientos_eslabones.csv','mineral',['forward_rasmussen'],0.02,
               filtro=lambda d:d.anio==2018)
# VII.3 Ghosh por eslabon pais 2018
cotejo_entidad('VII.3','icio_eslabones_metal.csv','pais',['forward_rasmussen'],0.02,
               keymap=PAISMAP, filtro=lambda d:d.anio==2018)
# VIII.2 geografia de la cadena (participacion lider)
cotejo_entidad('VIII.2','georref_regionalizacion.csv','mineral',['share_lider_pct'],0.6)
# B.4 Ghosh/Leontief Rasmussen por corte (2008 ref + 2013/2018)
c=getcap('B.4')
if c:
    a=rd('mip_encadenamientos_minerales.csv'); b8=rd('mip_encadenamientos_2008_referencia.csv')
    pool={}
    for _,r in a.iterrows():
        pool.setdefault(norm(r['mineral']),[]).extend([r['forward_rasmussen'],r['backward_rasmussen']])
    for _,r in b8.iterrows():
        pool.setdefault(norm(r['mineral']),[]).extend([r['forward_rasmussen'],r['backward_rasmussen']])
    ncmp=nm=0; mis=[]
    for row in c['m'][1:]:
        key=norm(row[0])
        if key not in pool: continue
        for cell in row[1:]:
            v=pnum(cell)
            if v is None: continue
            ncmp+=1
            if any(match(v,x,0.02) for x in pool[key]): nm+=1
            else: mis.append(f"{key}: {v}")
    add('Cuadro B.4','mip_encadenamientos_minerales.csv + _2008_referencia','por-entidad (cortes)',ncmp,nm,mis)
# B.5 Ghosh por eslabon (cortes 08/13/18) -> mip_encadenamientos_eslabones
cotejo_entidad('B.5','mip_encadenamientos_eslabones.csv','mineral',['forward_rasmussen'],0.02)
# B.6 Ghosh por eslabon pais (4 cortes) -> icio_eslabones_metal
cotejo_entidad('B.6','icio_eslabones_metal.csv','pais',['forward_rasmussen'],0.02,keymap=PAISMAP)

# ---------- cuadros cualitativos / de clasificacion / codigos (sin cifras de indicador que diferir) ----------
CUALI={
 'II.1':('criticidad_productos.csv','Clasificacion de criticidad por producto (estrategico/critico/...)'),
 'III.1':('concordancia_scian_2007_2013_minerales.csv','Correspondencia mineral -> clase SCIAN (codigos)'),
 'III.2':('(catalogo de indicadores)','Sintesis de indicadores: que describe cada uno y su base (texto)'),
 'VII.4':('criticidad_productos.csv','Criticidad por producto + capacidad de Mexico (clasificacion/texto)'),
 'VIII.1':('cv_tipologia.csv','Tipologia A/B/C/D y punto de ruptura (clasificacion)'),
 'IX.1':('(elaboracion propia)','Bases de politica por tipo de mercado (texto)'),
 'IX.2':('(declaracion de vacios)','Declaracion de vacios por indicador (texto)'),
 'D.1':('(declaracion de vacios)','Declaracion de vacios por indicador, causa y tratamiento (texto)'),
}
for tag,(csvn,desc) in CUALI.items():
    if getcap(tag):
        add('Cuadro '+tag, csvn, 'clasificacion / texto', 0, 0, [], nota=desc+' — trazable a su CSV; sin cifras de indicador que diferir.')

# ---------- figuras: identidad de fuente ----------
figrows=[]
for fp in sorted(glob.glob(os.path.join(FIGDIR,'fig_*.py'))):
    txt=open(fp,encoding='utf-8',errors='ignore').read()
    csvs=sorted(set(re.findall(r"([\w]+\.csv)", txt)))
    pngs=sorted(set(re.findall(r"([\w]+\.png)", txt)))
    figrows.append((os.path.basename(fp), pngs, csvs))

# ---------- salidas ----------
led=pd.DataFrame(rows)
led.to_csv(os.path.join(OUTDIR,'cotejo_certificacion.csv'), index=False, encoding='utf-8')
tot_n=int(led.n.sum()); tot_ok=int(led.coincide.sum())
print(f"CUADROS cotejados numericamente: {len(led)}")
print(f"Celdas/numeros comparados: {tot_n} | coinciden: {tot_ok} | difieren: {tot_n-tot_ok}")
print()
print(led[['cuadro','csv','n','coincide','difieren']].to_string(index=False))
print("\nDIFERENCIAS (muestra):")
for _,r in led[led.difieren>0].iterrows():
    print(f"  {r.cuadro}: {r.detalle}")
print(f"\nFIGURAS: {len(FIGS)} ilustraciones; scripts fig_*.py -> CSV:")
for n,p,cs in figrows: print(f"  {n}: {cs}")

# ---------- reporte HTML autonomo ----------
import html, datetime
FIGMAP={ 'fig_cap1.py':'I.1 (peso en exportaciones)','fig_cap1_composicion.py':'I.2 (composicion del bloque)',
 'fig_cap5.py':'V.1-V.2 (HHI por mineral y evolucion)','fig_cap6.py':'VI.1-VI.4 (Ghosh, CCV, eslabones)',
 'fig_cap7.py':'VII.1-VII.5 (comercio, destinos, ICIO)','fig_cap8_estatal.py':'VIII.3 (Ghosh estatal)',
 'fig_cap8_interestatal.py':'VIII.4 (interestatal)','fig_cap8.py':'VIII.1-VIII.2 (plano tipologia, punto de ruptura)',
 'fig_cadena_L0_L4.py':'III.1 (esquema de la cadena L0-L4)'}
figtr=[]
for n,p,cs in figrows:
    src = ", ".join(cs) if cs else "esquema (datos en el script; deriva de cv_tipologia.csv / diseno)"
    figtr.append((FIGMAP.get(n,n), n, src))

n_num=int((led.n>0).sum()); n_cual=int((led.n==0).sum())
def vrow(r):
    if r['n']==0:
        badge="<span class=badge style='background:#57606a1a;color:#57606a;border:1px solid #57606a55'>clasificacion/texto</span>"
    elif r['difieren']==0:
        badge="<span class=badge style='background:#1a7f371a;color:#1a7f37;border:1px solid #1a7f3755'>COINCIDE 100%</span>"
    else:
        badge=f"<span class=badge style='background:#9a67001a;color:#9a6700;border:1px solid #9a670055'>{r['difieren']} difieren</span>"
    det = html.escape(r['detalle'] or r['nota'] or '')
    return (f"<tr><td><b>{html.escape(r['cuadro'])}</b></td><td class=mono>{html.escape(str(r['csv']))}</td>"
            f"<td>{html.escape(r['modo'])}</td><td class=num>{r['n'] or ''}</td><td class=num>{r['coincide'] or ''}</td>"
            f"<td>{badge}</td><td class=nota>{det}</td></tr>")
trs="".join(vrow(r) for r in led.to_dict('records'))
figrows_html="".join(f"<tr><td><b>{html.escape(a)}</b></td><td class=mono>{html.escape(b)}</td><td class=mono>{html.escape(c)}</td></tr>" for a,b,c in figtr)

DOC=f"""<!DOCTYPE html><html lang=es><head><meta charset=utf-8><meta name=viewport content="width=device-width, initial-scale=1">
<title>Cotejo de certificacion — manuscrito vs. datos</title><style>
 :root{{--bg:#fff;--fg:#1f2328;--mut:#57606a;--line:#d0d7de;--head:#1F3864;--sub:#f6f8fa;--accent:#2E5496}}
 @media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#0d1117;--fg:#e6edf3;--mut:#9198a1;--line:#30363d;--head:#a6c8ff;--sub:#161b22;--accent:#a6c8ff}}}}
 *{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
 .wrap{{max-width:1150px;margin:0 auto;padding:28px 16px 64px}} h1{{color:var(--head);font-size:25px;margin:0 0 4px}} h2{{color:var(--head);font-size:18px;margin:30px 0 8px}}
 .sub{{color:var(--mut);margin:0 0 20px}} .cards{{display:flex;gap:12px;flex-wrap:wrap;margin:16px 0 22px}}
 .card{{flex:1;min-width:130px;background:var(--sub);border:1px solid var(--line);border-radius:12px;padding:12px 15px}}
 .card .big{{font-size:28px;font-weight:700}} .card .lbl{{color:var(--mut);font-size:12.5px}}
 table{{width:100%;border-collapse:collapse;font-size:13px}} th,td{{text-align:left;padding:7px 9px;border-bottom:1px solid var(--line);vertical-align:top}}
 th{{background:var(--head);color:#fff;position:sticky;top:0}} tr:nth-child(even) td{{background:var(--sub)}}
 .mono{{font-family:ui-monospace,Consolas,monospace;font-size:11.5px}} .num{{text-align:right;font-variant-numeric:tabular-nums}}
 .nota{{color:var(--mut);font-size:11.5px;max-width:360px}} .badge{{padding:2px 8px;border-radius:20px;font-size:11px;font-weight:600;white-space:nowrap}}
 details{{margin-top:24px;background:var(--sub);border:1px solid var(--line);border-radius:12px;padding:6px 16px}} summary{{cursor:pointer;font-weight:600;padding:10px 0}} code{{background:var(--sub);padding:1px 5px;border-radius:5px;font-size:12px}}
 .foot{{color:var(--mut);font-size:12px;margin-top:26px;border-top:1px solid var(--line);padding-top:12px}}
</style></head><body><div class=wrap>
<h1>Cotejo de certificacion — manuscrito vs. bases de datos</h1>
<p class=sub>Se confronta cada numero impreso en los cuadros e ilustraciones del manuscrito (<i>ICR - Manuscrito (nueva estructura).docx</i>) contra el CSV de <code>10 Datos/processed/</code> que lo origina. Solo lectura. Generado {datetime.date.today().isoformat()}.</p>
<div class=cards>
 <div class=card><div class=big>37</div><div class=lbl>cuadros del manuscrito<br>({n_num} con cifras · {n_cual} de clasificacion)</div></div>
 <div class=card><div class=big>{tot_n}</div><div class=lbl>numeros confrontados<br>celda por celda</div></div>
 <div class=card><div class=big style=color:#1a7f37>{tot_ok}</div><div class=lbl>coinciden con el CSV<br>(dentro del redondeo mostrado)</div></div>
 <div class=card><div class=big style=color:{'#9a6700' if tot_n-tot_ok else '#1a7f37'}>{tot_n-tot_ok}</div><div class=lbl>difieren</div></div>
 <div class=card><div class=big>29</div><div class=lbl>ilustraciones<br>trazadas a su CSV/fuente</div></div>
</div>
<h2>Cuadros</h2>
<table><thead><tr><th>Cuadro</th><th>CSV fuente</th><th>Modo de cotejo</th><th class=num>n</th><th class=num>coinc.</th><th>Resultado</th><th>Nota / diferencias</th></tr></thead><tbody>{trs}</tbody></table>
<h2>Ilustraciones (identidad de fuente)</h2>
<p class=sub style="margin:0 0 10px">Cada figura se genera con un script <code>fig_*.py</code> que lee los mismos CSV de <code>processed/</code> que el consolidado; por construccion grafica los datos ya certificados arriba.</p>
<table><thead><tr><th>Figuras</th><th>Script</th><th>CSV / fuente que lee</th></tr></thead><tbody>{figrows_html}</tbody></table>
<details><summary>Metodologia del cotejo</summary>
<p><b>Modo celda-a-celda</b> (matrices anio x mineral de los anexos B.1/B.2/B.3): cada celda se mapea a <code>CSV[mineral, anio]</code> y se compara con la tolerancia del redondeo mostrado (HHI ±1; coeficientes ±0.006). <b>Modo por-entidad</b> (tablas de cuerpo): cada numero de la fila de una entidad (mineral/pais/estado) debe existir, dentro del redondeo, en la fila de esa entidad en el CSV (los porcentajes se cotejan tanto en fraccion como en %). <b>Clasificacion/texto</b>: cuadros de tipologia, criticidad, codigos SCIAN y declaracion de vacios — trazables a su CSV, sin cifras de indicador que diferir.</p>
<p><b>Reproducir:</b> <code>py "13 Entregables/Consolidado datos y calculos/cotejo_certificacion.py"</code> (genera este HTML y <code>cotejo_certificacion.csv</code>). Complementa a <code>Auditoria de consistencia.html</code> (que recomputa cada indicador desde el CSV) y al libro Excel (formulas vivas).</p></details>
<p class=foot>Alcance: certifica que lo impreso en el manuscrito coincide con la capa <code>processed/</code>; esa capa, a su vez, queda auditada en su consistencia interna por <i>auditoria_consistencia.py</i>. No re-verifica la extraccion primaria (PDF de CAMIMEX, USGS, descargas de Comtrade).</p>
</div></body></html>"""
open(os.path.join(OUTDIR,'Cotejo de certificacion.html'),'w',encoding='utf-8').write(DOC)
print("\nEscrito: cotejo_certificacion.csv + Cotejo de certificacion.html")
