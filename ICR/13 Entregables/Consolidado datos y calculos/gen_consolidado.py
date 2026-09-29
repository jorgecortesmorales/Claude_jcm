# -*- coding: utf-8 -*-
"""
Genera el libro maestro:
  'Consolidado ICR - datos, calculos e indicadores.xlsx'

Objetivos:
 1) Consolidar en un mismo sitio toda la informacion estadistica, calculos e indicadores.
 2) Permitir identificar la realizacion de los calculos mediante FORMULAS vivas de Excel.

Diseno de trazabilidad:
 - Donde el calculo es aritmetico (CCV, HHI de participaciones, posicion comercial, peso del
   bloque, demanda intermedia, HHI geografico, normalizacion Rasmussen, identidad crudo+reproc),
   se escribe el VALOR ALMACENADO (del script Python) y, al lado, la MISMA cifra recomputada con
   FORMULA DE EXCEL sobre las celdas de insumo, mas una columna 'dif' que debe dar ~0.
   -> el libro se auto-audita.
 - Donde el calculo es algebra matricial (inversas de Leontief/Ghosh nacional, estatal, ICIO),
   no es practico incrustar la inversion en Excel: se presenta el resultado con procedencia
   completa (script, CSV, residual de validacion contra INEGI ~1e-15) y, cuando el ultimo paso
   es una normalizacion (Rasmussen = suma / media), ese paso SI se expone como formula viva.
"""
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
import os

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR"
PROC = os.path.join(BASE, "10 Datos", "processed")
OUTDIR = os.path.join(BASE, "13 Entregables", "Consolidado datos y calculos")
os.makedirs(OUTDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "Consolidado ICR - datos, calculos e indicadores.xlsx")

# ---------- estilos ----------
C_TITLE = "1F3864"; C_HDR = "2E5496"; C_SUB = "D9E1F2"; C_FORM = "E2EFDA"; C_PROV = "FCE4D6"
FONT_TITLE = Font(bold=True, size=15, color="FFFFFF")
FONT_HDR   = Font(bold=True, size=10, color="FFFFFF")
FONT_NOTE  = Font(italic=True, size=9, color="404040")
FILL_TITLE = PatternFill("solid", fgColor=C_TITLE)
FILL_HDR   = PatternFill("solid", fgColor=C_HDR)
FILL_SUB   = PatternFill("solid", fgColor=C_SUB)
FILL_FORM  = PatternFill("solid", fgColor=C_FORM)   # columnas con formula viva
FILL_PROV  = PatternFill("solid", fgColor=C_PROV)   # columnas de procedencia
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CTR = Alignment(horizontal="center", vertical="center", wrap_text=True)

def read(name):
    return pd.read_csv(os.path.join(PROC, name))

def title_row(ws, text, ncol, subtitle=None):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(ncol,1))
    c = ws.cell(1, 1, text); c.font = FONT_TITLE; c.fill = FILL_TITLE; c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[1].height = 24
    r = 2
    if subtitle:
        ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(ncol,1))
        c = ws.cell(2, 1, subtitle); c.font = FONT_NOTE; c.alignment = WRAP
        ws.row_dimensions[2].height = 40
        r = 3
    return r  # first free row

def write_headers(ws, headers, row, fills=None):
    for j, h in enumerate(headers, start=1):
        c = ws.cell(row, j, h); c.font = FONT_HDR; c.alignment = CTR; c.border = BORDER
        c.fill = (fills[j-1] if fills else FILL_HDR)
    ws.freeze_panes = ws.cell(row+1, 1)
    return row + 1

def style_data(ws, r0, r1, ncol, wrapcols=()):
    for r in range(r0, r1+1):
        for j in range(1, ncol+1):
            cell = ws.cell(r, j); cell.border = BORDER
            if j in wrapcols:
                cell.alignment = WRAP
            if r % 2 == 0:
                if cell.fill.fgColor.rgb in (None, "00000000"):
                    cell.fill = PatternFill("solid", fgColor="F2F6FB")

def setw(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w

wb = Workbook()
wb.remove(wb.active)

# registro de hojas para el indice
INDEX = []  # (orden, hoja, contenido, fuente_csv, script, tipo_traza)

# ============================================================
# HOJA: Indice  (se rellena al final; creamos placeholder al inicio)
# ============================================================
ws_idx = wb.create_sheet("00 Indice")

# ============================================================
# HOJA 01: Bases de datos utilizadas
# ============================================================
BASES = [
 # bloque, fuente/archivo, contenido, periodo, utilidad, ubicacion
 ("01 Criticidad","USGS/Gobierno EE.UU. + Comision Europea (listas de criticidad)","Clasificacion oficial de criticidad por mineral (riesgo de suministro, importancia economica)","2018-2023","Directa (criterio 1 del corpus)","Bases Originales/01 Criticidad y Produccion Historica/1. minerales criticos.xlsx"),
 ("01 Produccion hist.","INEGI / SGM (hoja Produccion)","Valor de produccion minera nacional, todos los minerales, MDP","1998-2024","Indirecta (contexto peso del bloque)","idem, hoja 'Produccion'"),
 ("02 Prod. y precios","INEGI Banco de Indicadores","Valor y volumen de produccion MENSUAL de los 10 minerales del corpus","2000-2025","Directa (valor de produccion, precio implicito)","Bases Originales/02 Produccion y Precios Nacionales/2. produccion y precios.xlsx"),
 ("03 Precios Cochilco","Comision Chilena del Cobre (LME/COMEX)","Precios internacionales mensuales, USD, 5 metales (Cu, Ag, Au, Pb, Zn)","1960-2024","Directa (validacion de precios)","Bases Originales/03 Precios Internacionales Cochilco/ (5 archivos)"),
 ("04 Comercio ext.","CAMIMEX, Informe Anual (extraccion manual de PDF)","Exportaciones/importaciones/balanza por producto, USD","2015-2024","Directa (CCV tramo reciente)","Bases Originales/04 Comercio Exterior/4. balanza comercial.xlsx"),
 ("05 Reservas mundo","USGS / fuentes mundiales","Produccion y reservas por pais y mineral, % mundial (una foto)","corte unico","Indirecta (posicion mundial de Mexico)","Bases Originales/05 Reservas y Produccion Mundial/3. reservas y produccion mundial.xlsx"),
 ("06 USGS DS-140","USGS Historical Statistics for Mineral and Material Commodities","Valor unitario anual (USD/t nominal y constante 1998), desde 1900","1900-2019","Directa (denominador CCV, precios de referencia)","Bases Originales/06 USGS DS-140/ (10 archivos ds140-*.xlsx)"),
 ("07 USGS MCS/MYB","USGS Mineral Commodity Summaries + Minerals Yearbook Mexico","Estructura de la industria (empresas, capacidades) y produccion nacional; base del HHI 1994-2003","1994-2024","Directa (HHI regimen, estructura industria)","Bases Originales/07 USGS MCS/ (incl. MYB Mexico 1994-2003)"),
 ("08 CAMIMEX","Camara Minera de Mexico, Informes Anuales","Produccion por mina/empresa y total nacional; base del HHI 2004-2024","2004-2025","Directa (numeradores HHI)","Bases Originales/08 CAMIMEX Informes Anuales/"),
 ("09 SGM Anuarios","Servicio Geologico Mexicano, Anuario Estadistico de la Mineria","Produccion por entidad federativa (georreferenciacion) y valor minero por estado","2019-2025","Directa (georref cuantitativa 2024)","Bases Originales/09 SGM Anuarios/"),
 ("10 MIP INEGI","INEGI, Matriz Insumo-Producto simetrica producto x producto (clase SCIAN 6d)","Coef. tecnicos (ctec=A) y directos+indirectos (cdi=inversa Leontief); base 2013 y 2018 + ref. 2008","2008/2013/2018","Directa (Leontief, Ghosh, Rasmussen, demanda intermedia)","Bases Originales/10 MIP INEGI/"),
 ("11 Comtrade","UN Comtrade (API publica; reportante Mexico 484)","Comercio por fraccion HS por flujo y ano; valor y peso de la etapa E1 (numerador CCV)","1992-2025","Directa (comercio por etapa, destinos, numerador CCV)","Bases Originales/11 Comercio Comtrade/"),
 ("12 OECD ICIO","OECD Inter-Country Input-Output 2023 (77 economias x 45 industrias ISIC Rev.4)","Bloques domesticos de mineria; encadenamientos y descomposicion de valor agregado","1995-2020","Directa (comparacion internacional, DVA/crudo_share)","Bases Originales/12 OECD ICIO/ (bloques extraidos; CSV completos re-descargables)"),
 ("13 MIP Estatal","INEGI, COU y MIP Multi-Estatales de Mexico 2018 (com. 236/24)","MIP industria x industria intra-estatal y birregional por entidad (35 industrias)","2018","Directa (Ghosh estatal e interestatal de la mineria)","Bases Originales/13 MIP Estatal INEGI/todos_2018.zip"),
 ("14 Geo","SGM + directorio propio de empresas","Estados productores, nodos de transformacion, co-localizacion","2024","Directa (mapas, HHI geografico)","Bases Originales/14 Geo/"),
 ("15 Marco instit.","Normativa (Ley Minera, reforma 2023, etc.)","Marco institucional del sector (contexto Cap. IV/VII)","-","Indirecta (contexto)","Bases Originales/15 Marco Institucional/"),
]
ws = wb.create_sheet("01 Bases de datos")
hdr = ["Bloque","Fuente / archivo","Contenido","Periodo","Utilidad","Ubicacion en el repositorio"]
r0 = title_row(ws, "Bases de datos utilizadas en la ICR", len(hdr),
    "Inventario de todas las fuentes que alimentan los calculos. Detalle por hoja en 10 Datos/Catalogo de Bases de Datos.md. "
    "Ademas de estas bases originales, todas las hojas estan exportadas a CSV limpio en 10 Datos/raw/csv/ (40 archivos).")
hr = write_headers(ws, hdr, r0)
for i, row in enumerate(BASES):
    for j, v in enumerate(row, start=1):
        ws.cell(hr+i, j, v)
style_data(ws, hr, hr+len(BASES)-1, len(hdr), wrapcols=(2,3,6))
setw(ws, {"A":16,"B":34,"C":46,"D":14,"E":26,"F":50})
INDEX.append(("01 Bases de datos","Inventario de todas las fuentes originales","varias","-","Catalogo"))

# ============================================================
# HOJA 02: Catalogo de calculos (TODOS los indicadores)
# ============================================================
CALC = [
 # grupo, indicador, que mide, formula, insumos, script, csv, hoja libro, tipo traza
 ("0 Insumos","Precios USGS empalmados","Precio anual de referencia del producto refinado, USD/t (nominal y const. 1998)","Empalme de series USGS por factor de enlace en anios de traslape; deflactor a 1998","USGS DS-140 / MYB","(extraccion USGS)","precios_usgs_anual_empalmado.csv","10 Precios","Resultado + procedencia"),
 ("0 Insumos","Peso del bloque - produccion","Valor de produccion del bloque y descomposicion precio/volumen","V = Q x p ; indices de volumen y de precio entre t0 y t1","volumen (USGS/CAMIMEX) x precio empalmado","peso_bloque_historico.py","peso_bloque_hist_produccion.csv","11 Peso bloque prod","Formula viva"),
 ("0 Insumos","Peso del bloque - exportaciones","% del bloque en las exportaciones totales de Mexico","share = X_bloque / X_nacional","Comtrade + Banco Mundial TX.VAL.MRCH.CD.WT","peso_bloque_historico.py","peso_bloque_hist_exportaciones.csv","12 Peso bloque X","Formula viva"),
 ("0 Insumos","Peso del bloque - PIB / empleo","Participacion del bloque en PIB y empleo","pct = valor_bloque / total_nacional","MIP 2013/2018 (B.1bP, P.1, PT)","peso_bloque.py","peso_bloque_mineria.csv","13 Peso bloque PIB","Formula viva"),
 ("1 HHI","HHI de concentracion extractiva","Concentracion de la produccion por mineral (estructura de mercado)","HHI = sum_i (s_i)^2 , s_i en % (escala 0-10000)","participaciones empresa/mina y total nacional","hhi_2024.py, hhi_consolidado_2004_2020.py, hhi_1994_2003.py","hhi_numeradores.csv, hhi_consolidado.csv","07-08 HHI","Formula viva (participaciones) + resultado (residual/regimen)"),
 ("1 HHI","HHI geografico","Concentracion territorial de la extraccion entre entidades","HHI_geo = sum_estado (s_estado)^2","produccion por estado 2024 (SGM)","georref_regionalizacion.py","georref_regionalizacion.csv","17 Georref","Formula viva"),
 ("2 MIP nacional","Leontief (hacia atras)","Traccion a proveedores de cada mineral","a_ij=z_ij/x_j ; L=(I-A)^-1 ; hacia atras = suma de columna","MIP INEGI 2013/2018 (ctec/cdi)","mip_calc.py","mip_encadenamientos_minerales.csv","14 MIP encadenam.","Resultado validado (1e-15) + Rasmussen formula viva"),
 ("2 MIP nacional","Ghosh (hacia adelante) - central","Distribucion de la produccion; si alimenta industria domestica","b_ij=z_ij/x_i ; G=(I-B)^-1 ; hacia adelante = suma de fila","MIP INEGI 2013/2018","mip_calc.py","mip_encadenamientos_minerales.csv","14 MIP encadenam.","Resultado validado + Rasmussen formula viva"),
 ("2 MIP nacional","Hirschman-Rasmussen","Encadenamientos comparables entre ramas (media=1)","suma sectorial / promedio de todas las sumas","sumas de fila/columna de L y G","mip_calc.py","mip_encadenamientos_minerales.csv","14 MIP encadenam.","Formula viva (normalizacion)"),
 ("2 MIP nacional","Demanda intermedia (DI/VBP)","Fraccion a uso intermedio interno y sectores compradores","DI/VBP ; share de la fila del mineral","MIP INEGI","mip_calc.py","mip_demanda_intermedia_minerales.csv","16 Demanda interm.","Formula viva"),
 ("2 MIP nacional","Encadenamiento por eslabon","Si el arrastre se sostiene al descender L1->L2->L3","Ghosh-Rasmussen por clase SCIAN 331... por mineral","MIP INEGI","mip_eslabones.py","mip_encadenamientos_eslabones.csv","15 MIP eslabones","Resultado + Rasmussen formula viva"),
 ("2 MIP nacional","Corte de referencia 2008","Tercer punto historico no encadenado","idem MIP (base 2008 / SCIAN 2007)","MIP INEGI 2008","mip2008_calc.py","mip_encadenamientos_2008_referencia.csv","14 MIP encadenam.","Resultado validado"),
 ("3 CCV","Coeficiente de captura de valor","Cuanto del valor del refinado capta la forma bruta exportada","CCV = v_E1 / p_USGS ; v_E1 = valor_E1 / peso_E1","Comtrade E1 (valor y peso) / USGS empalmado","ccv_download.py, ccv_calc.py, ccv_fill_gaps.py","ccv_serie.csv","09 CCV","Formula viva"),
 ("4 Comercio","Concordancia HS x etapa","Asigna cada fraccion HS a una etapa E1-E4","(tabla de concordancia)","clasificacion propia","comercio_etapa.py","concordancia_hs_etapa.csv","18 Comercio etapa","Clasificacion"),
 ("4 Comercio","Comercio por etapa y posicion","Exportaciones por etapa y share exportado en crudo","X_share_crudo = X_E1 / X_total","Comtrade por HS","comercio_etapa*.py","comercio_por_etapa_1992_2024.csv, comercio_posicion_1992_2024.csv","18 Comercio etapa","Formula viva"),
 ("4 Comercio","Destinos de exportacion","A quien se exporta cada etapa y su desplazamiento","share por destino = valor_destino / valor_total","Comtrade por socio","comercio_destinos*.py","comercio_destinos_serie_resumen.csv","19 Comercio destinos","Resultado + procedencia"),
 ("5 Cadena local","Empresas de transformacion","Existe eslabon local? quien y donde","(directorio verificado)","USGS Tabla 2 + verificacion web","(fichado manual)","empresas_transformacion.csv","20 Cadena local","Dato base"),
 ("5 Cadena local","Fichas L0-L4 cuantificadas","Cada mercado por eslabon (VBP/PIB/empleo, X/M)","atribucion MIP + comercio por etapa","MIP + Comtrade","cv_build.py","cv_eslabones_cuantificado.csv, cv_arbol_mineral.csv","20 Cadena local","Resultado"),
 ("5 Cadena local","Tipologia A/B/C/D","Clasifica los 10 mercados por transformacion domestica","criterios: actores + espejo + Ghosh/DI","indicadores previos","cv_build.py","cv_tipologia.csv","20 Cadena local","Clasificacion"),
 ("6 Territorial","Georreferenciacion extraccion","Distribucion estatal de la extraccion (share 2024)","share_estado = prod_estado / prod_nacional","SGM Anuario 2025","georref_cuantitativo.py","georref_extraccion_mineral_estado_cuantitativo.csv","17 Georref","Formula viva"),
 ("6 Territorial","Ghosh estatal","Encadenamiento hacia adelante por entidad; fuga por exportacion","Ghosh-Rasmussen sobre MIP estatal (rank 35)","MIP Estatal 2018 (intra)","ghosh_estatal.py","ghosh_estatal_mineria.csv, ghosh_estatal_eslabones.csv","17 Georref","Resultado + Rasmussen/share formula viva"),
 ("6 Territorial","Ghosh interestatal","Descompone producto minero: intra / inter-estatal / export","Ghosh sobre MIP birregional (rank 70)","MIP Estatal 2018 (birregional)","ghosh_interestatal.py","ghosh_interestatal_mineria.csv, ghosh_interestatal_eslabones.csv","17 Georref","Resultado + procedencia"),
 ("7 Internacional","Ghosh por pais (ICIO)","Encadenamiento adelante de la mineria de 8 paises","Ghosh-Rasmussen (media pais=1) sobre bloque domestico","OECD ICIO 2023","icio_comparacion.py, icio_eslabones.py","icio_comparacion_mineria.csv, icio_eslabones_metal.csv","21 ICIO","Resultado + procedencia"),
 ("7 Internacional","DVA / crudo_share (ICIO)","El enclave en dinero: fraccion del VA minero exportado en crudo","descomposicion Leontief global: dva_share, crudo_share, foreign_abs","OECD ICIO 2023 (matriz global)","icio_dva.py","icio_dva_mineria.csv","21 ICIO","Resultado + identidad crudo+reproc=1 formula viva"),
 ("8 Criticidad","Criticidad por producto","Eslabon de mayor criticidad de cada mineral y si Mexico lo produce/exporta/importa","(clasificacion oficial USGS/UE/IEA)","listas oficiales","(fichado)","criticidad_productos.csv","22 Criticidad","Clasificacion"),
]
ws = wb.create_sheet("02 Catalogo de calculos")
hdr = ["Grupo","Indicador / calculo","Que mide","Formula / matematica","Insumos","Script","CSV fuente","Hoja en este libro","Tipo de traza"]
r0 = title_row(ws, "Catalogo de calculos e indicadores", len(hdr),
    "Todos los calculos del proyecto, con su formula, insumos, script reproducible y el tipo de trazabilidad ofrecido en este libro. "
    "Base metodologica: 00 Proyecto/Metodologia y auditoria/Auditoria de indicadores.md. "
    "VERDE = columna con formula viva de Excel; NARANJA = columna de procedencia (resultado de script validado).")
hr = write_headers(ws, hdr, r0)
for i, row in enumerate(CALC):
    for j, v in enumerate(row, start=1):
        ws.cell(hr+i, j, v)
style_data(ws, hr, hr+len(CALC)-1, len(hdr), wrapcols=(3,4,5,9))
setw(ws, {"A":15,"B":26,"C":40,"D":40,"E":26,"F":28,"G":40,"H":18,"I":30})
INDEX.append(("02 Catalogo de calculos","Todos los indicadores con formula, script y tipo de traza","varias","varios","Catalogo"))

# ============================================================
# helpers de escritura de datos + columnas de formula
# ============================================================
def dump(sheetname, csvname, title, subtitle, wrapcols=(), widths=None, tipo="Dato base",
         index_content=None, script="-", df_override=None):
    df = df_override if df_override is not None else read(csvname)
    ws = wb.create_sheet(sheetname)
    ncol = df.shape[1]
    r0 = title_row(ws, title, max(ncol,3), subtitle)
    hr = write_headers(ws, list(df.columns), r0)
    for i, (_, row) in enumerate(df.iterrows()):
        for j, col in enumerate(df.columns, start=1):
            v = row[col]
            ws.cell(hr+i, j, None if pd.isna(v) else (v.item() if hasattr(v,'item') else v))
    style_data(ws, hr, hr+len(df)-1, ncol, wrapcols=wrapcols)
    if widths: setw(ws, widths)
    INDEX.append((sheetname, index_content or title, csvname, script, tipo))
    return ws, df, hr  # hr = primera fila de datos

def col_letter(idx):  # 1-based
    return get_column_letter(idx)

def add_formula_cols(ws, df, hr, specs):
    """specs: list of (header, fill, builder) donde builder(rownum)->formula string ('=...')."""
    base = df.shape[1]
    for k,(h,fill,_) in enumerate(specs, start=1):
        c = ws.cell(hr-1, base+k, h); c.font = FONT_HDR; c.fill = fill; c.alignment = CTR; c.border = BORDER
    for i in range(len(df)):
        rn = hr + i
        for k,(h,fill,builder) in enumerate(specs, start=1):
            cell = ws.cell(rn, base+k, builder(rn))
            cell.border = BORDER; cell.fill = fill
    return base

# ============================================================
# 07 HHI numeradores (participaciones empresa/mina) + formula de share
# ============================================================
dfn = read("hhi_numeradores.csv")
ws = wb.create_sheet("07 HHI numeradores")
ncol = dfn.shape[1]
r0 = title_row(ws, "HHI - numeradores (participaciones por empresa/mina)", ncol+2,
  "Insumo del HHI: participacion de cada empresa/mina y total nacional, con FUENTE y PAGINA (CAMIMEX/USGS). "
  "La columna verde recomputa participacion = volumen / total_nacional x 100 SOLO cuando volumen y total estan en la MISMA unidad; "
  "una 'dif' grande marca filas donde la fuente narrativa mezcla unidades (p.ej. oro en 'miles oz' vs total en toneladas) o usa CAPACIDAD, no produccion "
  "(barita/fluorita duopolio => >100%). Por eso el HHI final por mineral-anio se arma con residual/'metodo' por fila en '08 HHI serie', no por division directa.")
hr = write_headers(ws, list(dfn.columns), r0)
for i,(_,row) in enumerate(dfn.iterrows()):
    for j,col in enumerate(dfn.columns, start=1):
        v=row[col]; ws.cell(hr+i,j,None if pd.isna(v) else (v.item() if hasattr(v,'item') else v))
style_data(ws, hr, hr+len(dfn)-1, ncol, wrapcols=(12,14))
# columnas de formula: participacion (=vol/total*100) y dif
cvol = col_letter(list(dfn.columns).index("volumen")+1)
ctot = col_letter(list(dfn.columns).index("total_nacional")+1)
cpar = col_letter(list(dfn.columns).index("participacion_pct")+1)
cuv  = col_letter(list(dfn.columns).index("unidad_volumen")+1)
cut  = col_letter(list(dfn.columns).index("unidad_total")+1)
def f_share(rn): return f'=IF(AND(ISNUMBER({cvol}{rn}),ISNUMBER({ctot}{rn}),{ctot}{rn}<>0,{cuv}{rn}={cut}{rn}),{cvol}{rn}/{ctot}{rn}*100,"")'
def f_difsh(rn): return f'=IF(AND(ISNUMBER({col_letter(ncol+1)}{rn}),ISNUMBER({cpar}{rn})),ROUND({col_letter(ncol+1)}{rn}-{cpar}{rn},2),"")'
add_formula_cols(ws, dfn, hr, [("participacion (=formula) %",FILL_FORM,f_share),("dif vs reportada",FILL_FORM,f_difsh)])
setw(ws, {"A":11,"B":9,"C":9,"D":16,"E":16,"F":10,"G":11,"H":13,"I":13,"J":13,"K":11,"L":24,"M":8,"N":40,"O":18,"P":13})
INDEX.append(("07 HHI numeradores","Participaciones empresa/mina con fuente y pagina; share recomputado","hhi_numeradores.csv","hhi_2024.py / hhi_1994_2003.py","Formula viva (share)"))

# ============================================================
# 08 HHI serie consolidada + no metalicos
# ============================================================
ws, dfh, hr = dump("08 HHI serie","hhi_consolidado.csv",
  "HHI - serie consolidada por mineral-anio (1994-2024)",
  "HHI = suma de cuotas al cuadrado (0-10000). Cada fila trae su 'metodo' y 'cobertura_pct': "
  "2021-2024 por mina (comparable); 2004-2020 por regimen (cota inferior); 1994-2003 reconstruido de USGS MYB. "
  "Los niveles 1994-2020 se leen por TRAYECTORIA, no por nivel exacto. Resultado del script (incluye residual atomistico).",
  wrapcols=(6,7), widths={"A":11,"B":7,"C":8,"D":12,"E":18,"F":34,"G":60},
  tipo="Resultado + metodo por fila", script="hhi_consolidado_2004_2020.py, hhi_2024.py, hhi_1994_2003.py",
  index_content="HHI por mineral-anio con metodo/cobertura por fila")
# no metalicos aparte, debajo
start = hr + len(dfh) + 2
dfnm = read("hhi_nometalicos_2020_2024.csv")
ws.cell(start,1,"HHI no metalicos 2020-2024 (barita/fluorita/grafito/silice) - lider + estructura").font=Font(bold=True,color=C_HDR)
start += 1
hr2 = write_headers(ws, list(dfnm.columns), start)
for i,(_,row) in enumerate(dfnm.iterrows()):
    for j,col in enumerate(dfnm.columns, start=1):
        v=row[col]; ws.cell(hr2+i,j,None if pd.isna(v) else (v.item() if hasattr(v,'item') else v))
style_data(ws, hr2, hr2+len(dfnm)-1, dfnm.shape[1], wrapcols=(9,))

# ============================================================
# 09 CCV  (formula viva)
# ============================================================
ws, dfc, hr = dump("09 CCV","ccv_serie.csv",
  "CCV - Coeficiente de captura de valor (serie 1992-2025)",
  "CCV = valor_unitario_E1 / precio_refinado_USGS ; valor_unitario_E1 = valor_export_E1 / peso_export_E1. "
  "Columnas verdes: recomputo con formula de Excel y diferencia vs valor almacenado. La columna 'dif vu' marca (>0) las ~5 filas "
  "en que el valor unitario se corrigio por tonelaje minimo/atipico (silice 2016, fluorita 2018/2020, grafito 2017/2018): ahi el vu limpio != valor/peso, a proposito. "
  "'dif CCV' debe ser ~0. Informativo en metales base (Cu~0.22, Zn~0.30); NO informativo en oro/plata (artefacto de ley). 'fuente_numerador': propio vs espejo (CIF).",
  wrapcols=(11,), widths={"A":10,"B":22,"C":7,"D":9,"E":18,"F":15,"G":18,"H":18,"I":9,"J":15,"K":26},
  tipo="Formula viva", script="ccv_download.py, ccv_calc.py, ccv_fill_gaps.py",
  index_content="CCV por mineral-anio; numerador y denominador con recomputo")
cval=col_letter(list(dfc.columns).index("valor_export_e1_usd")+1)
cpeso=col_letter(list(dfc.columns).index("peso_export_e1_t")+1)
cvu=col_letter(list(dfc.columns).index("valor_unitario_export_usd_t")+1)
cpre=col_letter(list(dfc.columns).index("precio_refinado_usgs_usd_t")+1)
cccv=col_letter(list(dfc.columns).index("ccv")+1)
b=dfc.shape[1]
fcol_vu=col_letter(b+1); fcol_ccv=col_letter(b+3)
add_formula_cols(ws, dfc, hr, [
  ("valor_unitario (=formula)",FILL_FORM, lambda rn: f'=IF({cpeso}{rn}=0,"",{cval}{rn}/{cpeso}{rn})'),
  ("dif vu",FILL_FORM, lambda rn: f'=IF(ISNUMBER({fcol_vu}{rn}),ROUND({fcol_vu}{rn}-{cvu}{rn},4),"")'),
  ("CCV (=formula)",FILL_FORM, lambda rn: f'=IF({cpre}{rn}=0,"",{cvu}{rn}/{cpre}{rn})'),
  ("dif CCV",FILL_FORM, lambda rn: f'=IF(ISNUMBER({fcol_ccv}{rn}),ROUND({fcol_ccv}{rn}-{cccv}{rn},4),"")'),
])

# ============================================================
# 10 Precios USGS empalmados
# ============================================================
dump("10 Precios","precios_usgs_anual_empalmado.csv",
  "Precios USGS anuales empalmados (denominador del CCV y valuacion de produccion)",
  "Precio de referencia del producto refinado, USD/t nominal y constante 1998. 'metodo'/'serie_fuente'/'factor' documentan el empalme "
  "entre ediciones del USGS. Resultado de la extraccion USGS (no aritmetico simple: enlace por factor).",
  wrapcols=(5,6), widths={"A":11,"B":7,"C":20,"D":22,"E":16,"F":24,"G":10},
  tipo="Resultado + procedencia", script="(extraccion USGS)",
  index_content="Precio anual de referencia por mineral con metodo de empalme")

# ============================================================
# 11 Peso bloque - produccion (formula viva: V=Q*p y share)
# ============================================================
ws, dfp, hr = dump("11 Peso bloque prod","peso_bloque_hist_produccion.csv",
  "Peso del bloque - valor de produccion (1992-2022)",
  "valor_prod = vol_t x precio_usd_t. share_bloque = valor_prod / (suma del bloque ese anio) x 100. "
  "Columnas verdes recomputan ambas con formula de Excel (SUMIFS por anio) y su diferencia vs script. "
  "Nota: 'precio_usd_t' se muestra redondeado a 1 decimal, por lo que 'dif valor' puede mostrar diferencias <0.02% (redondeo de despliegue, no error); el share cuadra exacto.",
  wrapcols=(), widths={"A":7,"B":11,"C":12,"D":13,"E":16,"F":16,"G":13},
  tipo="Formula viva", script="peso_bloque_historico.py",
  index_content="Valor de produccion del bloque; V=Q*p y share recomputados")
cols=list(dfp.columns)
canio=col_letter(cols.index("anio")+1); cvol=col_letter(cols.index("vol_t")+1)
cpre=col_letter(cols.index("precio_usd_t")+1); cvp=col_letter(cols.index("valor_prod_usd")+1)
cshare=col_letter(cols.index("share_bloque_pct")+1)
r_last=hr+len(dfp)-1
b=dfp.shape[1]; fvp=col_letter(b+1)
add_formula_cols(ws, dfp, hr, [
  ("valor_prod (=formula)",FILL_FORM, lambda rn: f'={cvol}{rn}*{cpre}{rn}'),
  ("dif valor",FILL_FORM, lambda rn: f'=ROUND({fvp}{rn}-{cvp}{rn},0)'),
  ("share_bloque (=formula) %",FILL_FORM, lambda rn: f'=ROUND({cvp}{rn}/SUMIFS(${cvp}${hr}:${cvp}${r_last},${canio}${hr}:${canio}${r_last},{canio}{rn})*100,2)'),
  ("dif share",FILL_FORM, lambda rn: f'=ROUND({col_letter(b+3)}{rn}-{cshare}{rn},2)'),
])

# ============================================================
# 12 Peso bloque - exportaciones
# ============================================================
ws, dfx, hr = dump("12 Peso bloque X","peso_bloque_hist_exportaciones.csv",
  "Peso del bloque - exportaciones (1992-2024)",
  "share_bloque = X_bloque / X_nacional x 100. Columna verde recomputa con formula de Excel y su diferencia. "
  "X_bloque de Comtrade; X_nacional del Banco Mundial (TX.VAL.MRCH.CD.WT, coincide con INEGI).",
  widths={"A":7,"B":16,"C":18,"D":16}, tipo="Formula viva", script="peso_bloque_historico.py",
  index_content="% del bloque en exportaciones nacionales; recomputado")
cols=list(dfx.columns)
cb=col_letter(cols.index("X_bloque_musd")+1); cn=col_letter(cols.index("X_nacional_musd")+1)
cs=col_letter(cols.index("share_bloque_pct")+1); b=dfx.shape[1]
add_formula_cols(ws, dfx, hr, [
  ("share (=formula) %",FILL_FORM, lambda rn: f'=ROUND({cb}{rn}/{cn}{rn}*100,2)'),
  ("dif",FILL_FORM, lambda rn: f'=ROUND({col_letter(b+1)}{rn}-{cs}{rn},2)'),
])

# ============================================================
# 13 Peso bloque - PIB / empleo  (pct vs totales de referencia)
# ============================================================
ws, dfpb, hr = dump("13 Peso bloque PIB","peso_bloque_mineria.csv",
  "Peso del bloque - PIB, VBP y empleo (MIP 2013 / 2018)",
  "Filas 'mineral' = cada mineral; 'BLOQUE_10' = suma; 'referencia' = TOTAL_economia / mineria_212 / mineria_21. "
  "pct_pib_economia = pib_mmp / PIB_total x 100 (columna verde recomputa contra la fila de referencia del mismo anio).",
  wrapcols=(), widths={"A":7,"B":12,"C":10,"D":20,"E":13,"F":13,"G":12,"H":11,"I":16,"J":18,"K":16,"L":18,"M":16,"N":18},
  tipo="Formula viva", script="peso_bloque.py",
  index_content="PIB/VBP/empleo del bloque y participaciones; recomputado")
cols=list(dfpb.columns)
canio=col_letter(cols.index("anio")+1); cniv=col_letter(cols.index("nivel")+1); cmin=col_letter(cols.index("mineral")+1)
cpib=col_letter(cols.index("pib_mmp")+1); cpct=col_letter(cols.index("pct_pib_economia")+1)
r_last=hr+len(dfpb)-1; b=dfpb.shape[1]
def f_pctpib(rn):
    # PIB_total = pib_mmp de la fila referencia TOTAL_economia del mismo anio
    return (f'=IFERROR(ROUND({cpib}{rn}/SUMIFS(${cpib}${hr}:${cpib}${r_last},'
            f'${canio}${hr}:${canio}${r_last},{canio}{rn},${cmin}${hr}:${cmin}${r_last},"TOTAL_economia")*100,4),"")')
add_formula_cols(ws, dfpb, hr, [
  ("pct_pib_economia (=formula)",FILL_FORM, f_pctpib),
  ("dif",FILL_FORM, lambda rn: f'=IF(ISNUMBER({col_letter(b+1)}{rn}),ROUND({col_letter(b+1)}{rn}-{cpct}{rn},4),"")'),
])

# ============================================================
# 14 MIP encadenamientos (2013/2018) + 2008 ref  -- Rasmussen formula viva
# ============================================================
ws, dfm, hr = dump("14 MIP encadenam","mip_encadenamientos_minerales.csv",
  "MIP nacional - encadenamientos por mineral (2013 y 2018)",
  "Leontief L=(I-A)^-1 y Ghosh G=(I-B)^-1 calculados en Python y VALIDADOS contra ctec/cdi de INEGI a 1e-15. "
  "Aqui se exponen las sumas (backward_L_colsum, forward_G_rowsum). El paso de normalizacion Rasmussen (media economia=1) SI es formula viva: "
  "Rasmussen = suma / media_economia, con la media documentada por anio abajo. di_sobre_vbp tambien es formula viva. Plomo-zinc van combinados (clase 212232).",
  wrapcols=(), widths={"A":6,"B":9,"C":12,"D":13,"E":18,"F":12,"G":16,"H":15,"I":16,"J":16,"K":12,"L":12,"M":10},
  tipo="Resultado validado + Rasmussen formula viva", script="mip_calc.py",
  index_content="VBP, DI/VBP, Leontief/Ghosh y Rasmussen por mineral (2013/2018)")
cols=list(dfm.columns)
cvbp=col_letter(cols.index("vbp_mmpesos")+1); cdi=col_letter(cols.index("di_domestica_mmpesos")+1)
cdiv=col_letter(cols.index("di_sobre_vbp")+1); ccol=col_letter(cols.index("backward_L_colsum")+1)
crow=col_letter(cols.index("forward_G_rowsum")+1); cbr=col_letter(cols.index("backward_rasmussen")+1)
cfr=col_letter(cols.index("forward_rasmussen")+1)
# medias de la economia por anio (rowsum/rasmussen) -> bloque de constantes debajo
media_row={}; media_col={}
for anio,g in dfm.groupby("anio"):
    media_row[anio]=round((g["forward_G_rowsum"]/g["forward_rasmussen"]).mean(),6)
    media_col[anio]=round((g["backward_L_colsum"]/g["backward_rasmussen"]).mean(),6)
b=dfm.shape[1]
# escribir bloque de medias documentadas al pie
mrow0 = hr+len(dfm)+2
ws.cell(mrow0,1,"Medias de la economia (denominador Rasmussen; = promedio de las sumas de las 822 clases, del script)").font=Font(bold=True,color=C_HDR)
ws.cell(mrow0+1,1,"anio"); ws.cell(mrow0+1,2,"media_forward_rowsum"); ws.cell(mrow0+1,3,"media_backward_colsum")
anios=sorted(media_row)
mediacell_row={}; mediacell_col={}
for k,anio in enumerate(anios):
    rr=mrow0+2+k
    ws.cell(rr,1,int(anio)); ws.cell(rr,2,media_row[anio]); ws.cell(rr,3,media_col[anio])
    mediacell_row[anio]=f"$B${rr}"; mediacell_col[anio]=f"$C${rr}"
canio=col_letter(cols.index("anio")+1)
def mref(rn, table):  # elige la celda de media segun el anio de la fila
    # usa una formula que busca la media por anio con INDEX/MATCH sobre el bloque
    tcol = 2 if table=='row' else 3
    blk_last=mrow0+2+len(anios)-1
    return f'INDEX(${col_letter(tcol)}${mrow0+2}:${col_letter(tcol)}${blk_last},MATCH({canio}{rn},$A${mrow0+2}:$A${blk_last},0))'
add_formula_cols(ws, dfm, hr, [
  ("DI/VBP (=formula)",FILL_FORM, lambda rn: f'=ROUND({cdi}{rn}/{cvbp}{rn},4)'),
  ("dif DI/VBP",FILL_FORM, lambda rn: f'=ROUND({col_letter(b+1)}{rn}-{cdiv}{rn},4)'),
  ("fwd Rasmussen (=formula)",FILL_FORM, lambda rn: f'=ROUND({crow}{rn}/{mref(rn,"row")},4)'),
  ("dif fwd",FILL_FORM, lambda rn: f'=ROUND({col_letter(b+3)}{rn}-{cfr}{rn},4)'),
  ("bwd Rasmussen (=formula)",FILL_FORM, lambda rn: f'=ROUND({ccol}{rn}/{mref(rn,"col")},4)'),
  ("dif bwd",FILL_FORM, lambda rn: f'=ROUND({col_letter(b+5)}{rn}-{cbr}{rn},4)'),
])
# 2008 referencia debajo del bloque de medias
dref = read("mip_encadenamientos_2008_referencia.csv")
s2 = mrow0+2+len(anios)+2
ws.cell(s2,1,"Corte de referencia 2008 (base 2008 / SCIAN 2007) - NO comparable en nivel, se lee por patron").font=Font(bold=True,color=C_HDR)
s2+=1
hh=write_headers(ws, list(dref.columns), s2)
for i,(_,row) in enumerate(dref.iterrows()):
    for j,col in enumerate(dref.columns, start=1):
        v=row[col]; ws.cell(hh+i,j,None if pd.isna(v) else (v.item() if hasattr(v,'item') else v))
style_data(ws, hh, hh+len(dref)-1, dref.shape[1], wrapcols=(16,))

# ============================================================
# 15 MIP por eslabon
# ============================================================
dump("15 MIP eslabones","mip_encadenamientos_eslabones.csv",
  "MIP nacional - encadenamiento por eslabon (extraccion / refinacion / semimanufactura)",
  "Ghosh-Rasmussen por clase SCIAN de cada eslabon: prueba si el arrastre hacia adelante se sostiene al descender por la cadena. "
  "'atribuible' indica si la clase SCIAN es propia del mineral o compartida. Resultado del script (mismo metodo validado que la hoja 14).",
  wrapcols=(6,), widths={"A":6,"B":10,"C":14,"D":10,"E":9,"F":22,"G":10,"H":13,"I":16,"J":16,"K":16,"L":12,"M":12,"N":11},
  tipo="Resultado validado", script="mip_eslabones.py",
  index_content="Ghosh por eslabon (L1/L2/L3) por mineral")

# ============================================================
# 16 Demanda intermedia (formula viva share_del_di)
# ============================================================
_di = read("mip_demanda_intermedia_minerales.csv")
_enc = read("mip_encadenamientos_minerales.csv")[["anio","mineral","di_domestica_mmpesos"]]
_di = _di.merge(_enc, on=["anio","mineral"], how="left").rename(columns={"di_domestica_mmpesos":"DI_total_mineral"})
ws, dfd, hr = dump("16 Demanda interm","mip_demanda_intermedia_minerales.csv",
  "MIP nacional - demanda intermedia domestica (sectores compradores)",
  "share_del_di = valor del comprador / DI_total del mineral (demanda intermedia total de ese mineral-anio, de la hoja 14). "
  "La columna 'DI_total_mineral' se trae como insumo; la verde recomputa share = valor / DI_total y su diferencia vs script (~0).",
  wrapcols=(5,), widths={"A":6,"B":12,"C":12,"D":13,"E":34,"F":15,"G":12,"H":15},
  tipo="Formula viva", script="mip_calc.py",
  index_content="Top compradores domesticos por mineral; share recomputado",
  df_override=_di)
cols=list(dfd.columns)
cval=col_letter(cols.index("valor_mmpesos")+1); csh=col_letter(cols.index("share_del_di")+1)
cdit=col_letter(cols.index("DI_total_mineral")+1); b=dfd.shape[1]
add_formula_cols(ws, dfd, hr, [
  ("share_del_di (=formula)",FILL_FORM, lambda rn: f'=IF({cdit}{rn}=0,"",ROUND({cval}{rn}/{cdit}{rn},4))'),
  ("dif",FILL_FORM, lambda rn: f'=IF(ISNUMBER({col_letter(b+1)}{rn}),ROUND({col_letter(b+1)}{rn}-{csh}{rn},4),"")'),
])

# ============================================================
# 17 Georref + Ghosh estatal/interestatal
# ============================================================
# 17a georref cuantitativo (share por estado, formula viva)  -> hoja propia porque alimenta HHI geografico
ws, dfg, hr = dump("17 Georref extraccion","georref_extraccion_mineral_estado_cuantitativo.csv",
  "Georreferenciacion cuantitativa de la extraccion (share estatal 2024, SGM)",
  "share_2024 = produccion_estado / (suma nacional del mineral) x 100. Columna verde recomputa con SUMIFS. "
  "Esta hoja alimenta el HHI geografico de la hoja '17b'.",
  wrapcols=(6,), widths={"A":11,"B":18,"C":16,"D":10,"E":14,"F":22},
  tipo="Formula viva", script="georref_cuantitativo.py",
  index_content="Produccion por mineral x estado 2024 y share; recomputado")
cols=list(dfg.columns)
cmin_g=col_letter(cols.index("mineral")+1); cprod=col_letter(cols.index("produccion_2024")+1)
cshr=col_letter(cols.index("share_2024_pct")+1); cest=col_letter(cols.index("estado")+1)
r_last_g=hr+len(dfg)-1; hr_g=hr; b=dfg.shape[1]
add_formula_cols(ws, dfg, hr, [
  ("share (=formula) %",FILL_FORM, lambda rn: f'=ROUND({cprod}{rn}/SUMIFS(${cprod}${hr_g}:${cprod}${r_last_g},${cmin_g}${hr_g}:${cmin_g}${r_last_g},{cmin_g}{rn})*100,2)'),
  ("dif",FILL_FORM, lambda rn: f'=ROUND({col_letter(b+1)}{rn}-{cshr}{rn},2)'),
])
GEO_SHEET="'17 Georref extraccion'"; GEO_MIN=f"{GEO_SHEET}!${cmin_g}${hr_g}:${cmin_g}${r_last_g}"; GEO_SHR=f"{GEO_SHEET}!${cshr}${hr_g}:${cshr}${r_last_g}"

# 17b regionalizacion: HHI geografico formula viva (SUMPRODUCT sobre shares de 17a)
ws, dfr, hr = dump("17b HHI geografico","georref_regionalizacion.csv",
  "HHI geografico de la extraccion + co-localizacion con transformacion",
  "hhi_geografico = suma_estado (share_estado)^2. Columna verde lo recomputa con SUMPRODUCT sobre los shares de la hoja "
  "'17 Georref extraccion' y lo compara con el valor del script. tiene_eslabon_E2 / colocalizado = mapa cualitativo.",
  wrapcols=(6,), widths={"A":11,"B":14,"C":10,"D":20,"E":14,"F":26,"G":14,"H":18},
  tipo="Formula viva", script="georref_regionalizacion.py",
  index_content="HHI geografico por mineral y co-localizacion; recomputado")
cols=list(dfr.columns)
cmin_r=col_letter(cols.index("mineral")+1); chhi=col_letter(cols.index("hhi_geografico")+1); b=dfr.shape[1]
add_formula_cols(ws, dfr, hr, [
  ("HHI_geo (=formula)",FILL_FORM, lambda rn: f'=ROUND(SUMPRODUCT(({GEO_MIN}={cmin_r}{rn})*({GEO_SHR})^2),0)'),
  ("dif",FILL_FORM, lambda rn: f'=ROUND({col_letter(b+1)}{rn}-{chhi}{rn},0)'),
])
# 17c ghosh estatal + interestatal (resultado + share_vbp formula viva)
ws, dfe, hr = dump("17c Ghosh estatal","ghosh_estatal_mineria.csv",
  "Ghosh estatal de la mineria (MIP Estatal INEGI 2018, intra-estatal)",
  "Ghosh-Rasmussen intra-estatal por entidad (metodo identico al nacional, inversa de Ghosh sobre la MIP estatal; media estado=1). "
  "fuga_export_share = fraccion del arrastre del producto minero que sale del estado (de la descomposicion Ghosh, no un cociente simple). "
  "share_vbp_estatal_pct = peso de la mineria en la economia de CADA estado (no cuota del total nacional). Resultado del script; validado como el nacional.",
  wrapcols=(), widths={"A":16,"B":8,"C":16,"D":18,"E":14,"F":16,"G":14,"H":16,"I":16,"J":18,"K":14},
  tipo="Resultado validado + procedencia", script="ghosh_estatal.py",
  index_content="Ghosh/fuga/peso por entidad (mineria 2018)")
# interestatal debajo
dii=read("ghosh_interestatal_mineria.csv")
s=hr+len(dfe)+2
ws.cell(s,1,"Ghosh INTER-ESTATAL (MIP birregional 2018): descompone en intra / inter-estatal / final / export_abroad").font=Font(bold=True,color=C_HDR)
s+=1; hh=write_headers(ws, list(dii.columns), s)
for i,(_,row) in enumerate(dii.iterrows()):
    for j,col in enumerate(dii.columns, start=1):
        v=row[col]; ws.cell(hh+i,j,None if pd.isna(v) else (v.item() if hasattr(v,'item') else v))
style_data(ws, hh, hh+len(dii)-1, dii.shape[1])
# check formula viva: shares suman 1
colnames=list(dii.columns)
ci=col_letter(colnames.index("intra_share")+1); cie=col_letter(colnames.index("inter_estatal_share")+1)
cfn=col_letter(colnames.index("final_nacional_share")+1); cea=col_letter(colnames.index("export_abroad_share")+1)
chk_col=dii.shape[1]+1
ws.cell(hh-1,chk_col,"suma shares (=1?)").font=FONT_HDR; ws.cell(hh-1,chk_col).fill=FILL_FORM
for i in range(len(dii)):
    rn=hh+i
    ws.cell(rn,chk_col,f'=ROUND({ci}{rn}+{cie}{rn}+{cfn}{rn}+{cea}{rn},4)').fill=FILL_FORM

# ============================================================
# 18 Comercio por etapa + posicion (formula viva X_share_crudo)
# ============================================================
ws, dfpos, hr = dump("18 Comercio posicion","comercio_posicion_1992_2024.csv",
  "Comercio - posicion por etapa (X_share_crudo, 1992-2024)",
  "X_share_crudo = X_crudo (E1) / X_total. Columna verde recomputa con formula y su diferencia. "
  "Evidencia del truncamiento: se exporta E1 y se importa E3-E4. La serie larga por etapa/flujo esta en la hoja '18b'.",
  widths={"A":7,"B":11,"C":16,"D":16,"E":14}, tipo="Formula viva", script="comercio_etapa_merge.py",
  index_content="Share exportado en crudo por mineral-anio; recomputado")
cols=list(dfpos.columns)
cxt=col_letter(cols.index("X_total_usd")+1); cxc=col_letter(cols.index("X_crudo_usd")+1); cxs=col_letter(cols.index("X_share_crudo")+1); b=dfpos.shape[1]
add_formula_cols(ws, dfpos, hr, [
  ("X_share_crudo (=formula)",FILL_FORM, lambda rn: f'=IF({cxt}{rn}=0,"",ROUND({cxc}{rn}/{cxt}{rn},4))'),
  ("dif",FILL_FORM, lambda rn: f'=IF(ISNUMBER({col_letter(b+1)}{rn}),ROUND({col_letter(b+1)}{rn}-{cxs}{rn},4),"")'),
])
dump("18b Comercio por etapa","comercio_por_etapa_1992_2024.csv",
  "Comercio por etapa (serie larga, valor por mineral x etapa x flujo, 1992-2024)",
  "Insumo de la posicion (hoja 18). Etapas E1-E4 segun la concordancia HS (hoja 18c). Caveat: cambian versiones HS a lo largo del periodo -> leer como tendencia.",
  widths={"A":7,"B":11,"C":8,"D":8,"E":16}, tipo="Dato base (Comtrade)", script="comercio_etapa_backseries.py",
  index_content="Valor de comercio por mineral/etapa/flujo/anio")
dump("18c Concordancia HS","concordancia_hs_etapa.csv",
  "Concordancia mineral x etapa x fraccion HS",
  "Operacionalizacion que asigna cada fraccion HS a una etapa E1-E4. Base de todo el analisis de comercio por grado de transformacion.",
  wrapcols=(3,), widths={"A":12,"B":8,"C":60}, tipo="Clasificacion", script="comercio_etapa.py",
  index_content="Asignacion HS -> etapa por mineral")

# ============================================================
# 19 Comercio destinos
# ============================================================
dump("19 Comercio destinos","comercio_destinos_serie_resumen.csv",
  "Comercio - destinos de exportacion (serie 1992-2024)",
  "Por mineral-etapa-anio: destino principal y share de China/EUA. Resultado a partir del crudo por socio de Comtrade (share = valor_destino/valor_total). "
  "Hallazgo: los concentrados se desplazan de Norteamerica (1990s) a China. Detalle acumulado por socio en la hoja '19b'.",
  widths={"A":6,"B":11,"C":8,"D":16,"E":16,"F":13,"G":12,"H":11,"I":11}, tipo="Resultado + procedencia", script="comercio_destinos_serie_resumen.py",
  index_content="Destino principal y share China/EUA por mineral-etapa-anio")
dump("19b Destinos acumulado","comercio_destinos_mineral_etapa.csv",
  "Comercio - destinos por mineral x etapa (acumulado 2019-2024)",
  "share_etapa = valor a ese destino / valor total de la etapa. Hallazgo: concentrado de cobre 94.7% a China.",
  widths={"A":11,"B":8,"C":18,"D":8,"E":18,"F":12}, tipo="Resultado", script="comercio_destinos.py",
  index_content="Share por destino, mineral y etapa (acumulado)")

# ============================================================
# 20 Cadena local: empresas + fichas + tipologia + criticidad
# ============================================================
dump("20 Empresas transform","empresas_transformacion.csv",
  "Cadena local - empresas de transformacion (19 firmas)",
  "Directorio de procesadoras/usuarias domesticas por eslabon, con rol, ubicacion, propiedad y nivel de CONFIANZA (sourced-USGS / verificado-web / preliminar). "
  "Corrige el dato sectorial: buena parte de la cadena ocurre intra-firma, invisible en la MIP.",
  wrapcols=(8,), widths={"A":11,"B":12,"C":20,"D":16,"E":16,"F":16,"G":16,"H":30}, tipo="Dato base", script="(fichado)",
  index_content="19 empresas de transformacion verificadas")
dump("20b Fichas por eslabon","cv_eslabones_cuantificado.csv",
  "Cadena local - fichas L0-L4 cuantificadas (VBP/PIB/empleo 2013-2018, X/M)",
  "Cada mercado por eslabon con VBP/PIB/empleo de la MIP donde la clase SCIAN es atribuible, y X/M por etapa. "
  "Solo el cobre tiene clases SCIAN dedicadas a su transformacion; el resto comparte clase -> ese valor NO se atribuye (nota).",
  wrapcols=(12,), widths={"A":11,"B":12,"C":8,"D":9,"E":11,"F":13,"G":13,"H":12,"I":13,"J":13,"K":12,"L":26,"M":12,"N":12}, tipo="Resultado", script="cv_build.py",
  index_content="Eslabones cuantificados por mineral")
dump("20c Tipologia ABCD","cv_tipologia.csv",
  "Cadena local - tipologia A/B/C/D",
  "Clasifica los 10 mercados por grado de transformacion domestica (A desarrollada / B truncada en refinado / C usuario con eslabon importado / D exportacion en bruto), "
  "con los criterios que la sustentan (actores, espejo, Ghosh/DI).",
  wrapcols=(4,5,6,7), widths={"A":11,"B":6,"C":16,"D":26,"E":26,"F":26,"G":40}, tipo="Clasificacion (sintesis)", script="cv_build.py",
  index_content="Tipologia descriptiva de los 10 mercados")

# ============================================================
# 21 ICIO comparacion + DVA
# ============================================================
dump("21 ICIO comparacion","icio_comparacion_mineria.csv",
  "Comparacion internacional - encadenamientos de mineria (OECD ICIO 2023, 8 paises)",
  "Ghosh (forward) y Leontief (backward) del sector mineria de 8 paises, 3-4 cortes. Sector comparable = B07_08 (mineria no energetica). "
  "Resultado del script sobre la matriz inter-pais; comparar POSICION relativa (ISIC != SCIAN), no niveles absolutos. Mexico 1.51 ~ China 1.53.",
  widths={"A":6,"B":7,"C":13,"D":9,"E":22,"F":13,"G":12,"H":16,"I":15,"J":16,"K":16,"L":12,"M":12,"N":13}, tipo="Resultado + procedencia", script="icio_comparacion.py",
  index_content="Ghosh/Leontief de mineria por pais (comparacion)")
ws, dfdva, hr = dump("21b ICIO DVA","icio_dva_mineria.csv",
  "Comparacion internacional - DVA / crudo_share (el enclave en dinero)",
  "Descomposicion del valor agregado minero exportado: crudo_share = fraccion que sale en bruto a reprocesarse afuera. "
  "Columna verde comprueba la identidad crudo_share + reproc_domestico_share = 1 (validacion del script: 0 violaciones). "
  "Clave: Mexico crudo 0.38 vs China 0.07 con Ghosh casi igual.",
  widths={"A":6,"B":7,"C":13,"D":9,"E":12,"F":11,"G":16,"H":20,"I":13,"J":16}, tipo="Resultado + identidad formula viva", script="icio_dva.py",
  index_content="DVA, crudo_share por pais/sector/anio; identidad verificada")
cols=list(dfdva.columns)
ccru=col_letter(cols.index("crudo_share")+1); crep=col_letter(cols.index("reproc_domestico_share")+1); b=dfdva.shape[1]
add_formula_cols(ws, dfdva, hr, [
  ("crudo+reproc (=1?)",FILL_FORM, lambda rn: f'=ROUND({ccru}{rn}+{crep}{rn},4)'),
])

# ============================================================
# 22 Criticidad por producto
# ============================================================
dump("22 Criticidad","criticidad_productos.csv",
  "Criticidad por producto",
  "Eslabon de mayor criticidad de cada mineral (estrategico > critico > medio > bajo) y si Mexico lo usa/exporta/importa. "
  "Base oficial USGS (2022/2025), UE (CRMA 2023), IEA. Muestra que la criticidad se concentra en productos y grados, no en el mineral.",
  wrapcols=(3,), widths={"A":11,"B":8,"C":28,"D":16,"E":16,"F":16,"G":8,"H":10,"I":10}, tipo="Clasificacion", script="(fichado)",
  index_content="Nivel de criticidad por producto/eslabon")

# ============================================================
# rellenar 00 Indice
# ============================================================
ws = ws_idx
hdr = ["Hoja","Contenido","CSV fuente","Script","Tipo de trazabilidad"]
r0 = title_row(ws, "Consolidado ICR - datos, calculos e indicadores", len(hdr),
  "Un solo libro con (1) el inventario de bases, (2) el catalogo de todos los calculos, y (3) una hoja por bloque de indicadores. "
  "Trazabilidad: las columnas VERDES contienen la FORMULA VIVA de Excel que recomputa el indicador desde sus insumos (con una columna 'dif' que debe dar ~0); "
  "las columnas NARANJAS son resultados de algebra matricial (inversas de Leontief/Ghosh) calculados en Python y validados contra INEGI a precision de maquina (~1e-15), "
  "con su script y CSV. Ninguna cifra es un numero suelto: o se recomputa aqui, o apunta a su script. Fecha de generacion: 2026-09-28.")
hr = write_headers(ws, hdr, r0)
for i,(hoja,cont,csv,scr,tipo) in enumerate(INDEX):
    ws.cell(hr+i,1,hoja); ws.cell(hr+i,2,cont); ws.cell(hr+i,3,csv); ws.cell(hr+i,4,scr); ws.cell(hr+i,5,tipo)
    # link interno
    ws.cell(hr+i,1).hyperlink = f"#'{hoja}'!A1"; ws.cell(hr+i,1).font=Font(color="0563C1", underline="single")
style_data(ws, hr, hr+len(INDEX)-1, len(hdr), wrapcols=(2,3,5))
setw(ws, {"A":22,"B":48,"C":40,"D":30,"E":32})

# orden de hojas: indice primero
wb.move_sheet("00 Indice", -(len(wb.sheetnames)-1))
wb.save(OUT)
print("OK ->", OUT)
print("hojas:", len(wb.sheetnames))

