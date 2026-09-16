# -*- coding: utf-8 -*-
"""Construye el .docx del RESUMEN DESCRIPTIVO (python-docx).
Descriptivo: explica que se calculo, con que formula, en que se basa, de donde salio cada
dato, y muestra los graficos. No interpreta. Formato tesis: Times New Roman 12, Carta, 3 cm."""
import csv, os
from collections import defaultdict
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PROC=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
PNG=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\png_charts"
# Historial de resumenes fechados: subir FECHA para generar una version nueva sin borrar las previas.
FECHA="2026-09-08"
OUTDIR=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\Resumenes descriptivos"
os.makedirs(OUTDIR, exist_ok=True)
OUT=os.path.join(OUTDIR, f"Resumen descriptivo - datos e indicadores {FECHA}.docx")
def rd(p): return list(csv.DictReader(open(os.path.join(PROC,p),encoding='utf-8-sig')))
NAMES={'cobre':'Cobre','zinc':'Zinc','plomo':'Plomo','oro':'Oro','plata':'Plata','barita':'Barita','fluorita':'Fluorita','grafito':'Grafito','silice':'Sílice','manganeso':'Manganeso','plomo-zinc':'Plomo-zinc'}
COP=RGBColor(0xb0,0x57,0x1e); INK=RGBColor(0x21,0x1d,0x18); MUT=RGBColor(0x6b,0x64,0x5a)

# ---------- datos para el cuadro resumen ----------
ccv=rd('ccv_serie.csv'); ccvmean=defaultdict(list)
for r in ccv:
    if r['ccv']!='': ccvmean[r['mineral']].append(float(r['ccv']))
ccvmean={m:sum(v)/len(v) for m,v in ccvmean.items()}
hhi=rd('hhi_consolidado.csv'); hhi23={r['mineral']:int(r['hhi']) for r in hhi if r['anio']=='2023'}
mip=rd('mip_encadenamientos_minerales.csv'); gh18={r['mineral']:float(r['forward_rasmussen']) for r in mip if r['anio']=='2018'}
com=rd('comercio_posicion_resumen.csv'); crudo=defaultdict(list)
for r in com:
    if r['X_share_crudo']!='' and int(r['anio'])>=2020: crudo[r['mineral']].append(float(r['X_share_crudo']))
crudo={m:sum(v)/len(v) for m,v in crudo.items()}

# ---------- documento ----------
doc=Document()
st=doc.styles['Normal']; st.font.name='Times New Roman'; st.font.size=Pt(12)
st.element.rPr.rFonts.set(qn('w:eastAsia'),'Times New Roman')
st.paragraph_format.space_after=Pt(6); st.paragraph_format.line_spacing=1.15
sec=doc.sections[0]
sec.page_width=Cm(21.59); sec.page_height=Cm(27.94)  # Carta
for m in ('top_margin','bottom_margin','left_margin','right_margin'): setattr(sec,m,Cm(3))

def style_heading(level):
    h=doc.styles['Heading %d'%level]; h.font.name='Times New Roman'
    h.font.color.rgb=INK
for l in (1,2): style_heading(l)

def para(text=None,size=12,bold=False,italic=False,color=None,align=None,after=6,before=0):
    p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(after); p.paragraph_format.space_before=Pt(before)
    if align is not None: p.alignment=align
    if text is not None:
        r=p.add_run(text); r.font.size=Pt(size); r.bold=bold; r.italic=italic
        if color is not None: r.font.color.rgb=color
    return p

def h1(t):
    p=doc.add_heading(level=1); r=p.add_run(t); r.font.size=Pt(15); r.bold=True; r.font.color.rgb=INK
    return p
def h2(t):
    p=doc.add_heading(level=2); r=p.add_run(t); r.font.size=Pt(13); r.bold=True; r.font.color.rgb=COP
    return p

def formula(runs):
    """runs: lista de (texto, modo) con modo in ('','sub','sup')"""
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before=Pt(4); p.paragraph_format.space_after=Pt(8)
    for txt,mode in runs:
        r=p.add_run(txt); r.font.size=Pt(12.5); r.italic=True; r.font.name='Cambria Math'
        if mode=='sub': r.font.subscript=True
        if mode=='sup': r.font.superscript=True
    # borde izquierdo tenue
    return p

def caption(t):
    para(t,size=9.5,italic=True,color=MUT,after=12)

def add_chart(fname,cap):
    doc.add_picture(os.path.join(PNG,fname),width=Cm(15.5))
    doc.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
    caption(cap)

def shade(cell,hexcolor):
    tcPr=cell._tc.get_or_add_tcPr(); sh=OxmlElement('w:shd')
    sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),hexcolor); tcPr.append(sh)

def set_cell(cell,text,bold=False,size=10,color=None,align=None):
    cell.text=''; p=cell.paragraphs[0]
    if align is not None: p.alignment=align
    r=p.add_run(text); r.font.size=Pt(size); r.bold=bold; r.font.name='Times New Roman'
    if color is not None: r.font.color.rgb=color

# ================= PORTADA =================
para('ICR · Maestría en Economía · UAM Azcapotzalco',size=10.5,color=COP,after=2)
p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(2)
r=p.add_run('Los mercados de los minerales críticos en México'); r.bold=True; r.font.size=Pt(20); r.font.name='Times New Roman'; r.font.color.rgb=INK
p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(10)
r=p.add_run('Qué medimos y qué encontramos — resumen descriptivo de la fase de datos'); r.font.size=Pt(13.5); r.italic=True; r.font.color.rgb=MUT
para('Diez minerales: barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice y zinc. Periodo 1992–2025.',size=11,color=MUT,after=2)
# regla
pr=doc.add_paragraph(); pPr=pr._p.get_or_add_pPr(); pbdr=OxmlElement('w:pBdr'); bot=OxmlElement('w:bottom')
bot.set(qn('w:val'),'single'); bot.set(qn('w:sz'),'12'); bot.set(qn('w:space'),'6'); bot.set(qn('w:color'),'b0571e')
pbdr.append(bot); pPr.append(pbdr); pr.paragraph_format.space_after=Pt(10)

para('Este documento resume los datos que se construyeron para describir los mercados de diez minerales críticos en México. Para cada indicador se explica qué mide, con qué fórmula se calcula —incluida la matemática con algo más de detalle—, en qué fuentes se basa y de dónde se extrajo cada dato, cómo evoluciona a lo largo del tiempo, y se muestra el resultado en gráficos. Además de los cuatro indicadores nacionales (concentración, encadenamiento, captura de valor y comercio por etapa), se incorpora la comparación internacional de la minería (México frente a Chile, Australia, Finlandia, Suecia, China, Brasil y Perú), la descomposición del valor agregado que mide el enclave “en dinero”, y la dimensión regional de la cadena. Está escrito para una persona con formación en economía que no sea especialista en el tema: cada concepto técnico se explica al introducirlo. Es un documento descriptivo: presenta los hallazgos, sin construir un modelo causal. La última sección acompaña, diapositiva por diapositiva, la presentación del protocolo de investigación. Para el detalle metodológico exhaustivo (toda la matemática y todos los resultados) véase el documento complementario “Resumen metodológico y de resultados”.')

# ================= 1. FASES =================
h1('1. Punto de partida: las cuatro fases de la cadena de valor')
para('Cada mineral recorre una cadena de valor, de lo más simple a lo más elaborado. Para ordenar los datos, esa cadena se divide en cuatro etapas:')
t=doc.add_table(rows=5,cols=2); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
t.columns[0].width=Cm(3); t.columns[1].width=Cm(12.5)
fases=[('Etapa','Qué incluye',True),('E1 — Mena / concentrado','El mineral en bruto o su concentrado (lo que sale de la mina).',False),
('E2 — Refinado / procesado','Metal refinado, o el mineral ya procesado o convertido en químico.',False),
('E3 — Semimanufactura','Un producto intermedio ya elaborado (por ejemplo, alambre o lámina).',False),
('E4 — Bien final','Una manufactura terminada atribuible al mineral.',False)]
for i,(a,b,hd) in enumerate(fases):
    for j,val in enumerate((a,b)):
        set_cell(t.rows[i].cells[j],val,bold=hd,size=10)
        if hd: shade(t.rows[i].cells[j],'211d18'); t.rows[i].cells[j].paragraphs[0].runs[0].font.color.rgb=RGBColor(0xff,0xff,0xff)
        elif j==0: set_cell(t.rows[i].cells[j],val,bold=True,size=10,color=COP)
para('',after=2)
para('Los cuatro indicadores que siguen describen dónde se ubica México en esta cadena para cada mineral.',italic=True,color=MUT)

# ================= 2. HHI =================
h1('2. Concentración de la extracción (HHI)')
h2('Qué mide')
para('Qué tan concentrada está la producción de cada mineral en pocas empresas o grupos. Si un solo grupo produce casi todo, el mercado está muy concentrado; si hay muchos productores parecidos, está poco concentrado.')
h2('Intuición')
para('Es un termómetro de "¿pocos o muchos?": si un solo grupo produce casi todo, el índice se acerca a 10 000; si hay muchos productores parecidos, baja. Como eleva las participaciones al cuadrado, un líder dominante pesa mucho más que varios productores pequeños; por eso distingue un mercado con un dominante de otro repartido entre iguales.')
h2('Fórmula')
formula([('HHI = ',''),('Σ ',''),('s',''),('i','sub'),('2','sup')])
para('Se toma la participación de cada grupo en la producción nacional (s, en %), se eleva al cuadrado y se suman todos los grupos. El resultado va de 0 a 10 000. Como referencia: por encima de 2 500 se considera alta concentración; entre 1 500 y 2 500, moderada; por debajo de 1 500, baja. Un solo productor da 10 000.')
h2('En qué nos basamos y de dónde salen los datos')
para('Las participaciones por empresa y por mina se tomaron de la Tabla 2 (“Structure of the Mineral Industry”) del USGS Minerals Yearbook de México —leída directamente en imagen edición por edición— y de los Informes Anuales de la CAMIMEX. Para 2021–2023 se usó el detalle por mina (producción de cada mina, consolidada por grupo, frente a la producción nacional); para 2004–2020 solo existe la participación por empresa, por lo que la cifra de esos años es una aproximación (se lee como nivel de concentración general, no como un valor exacto). Los monopolios documentados (manganeso, fluorita desde 2012 y grafito desde 2014) se fijan en 10 000. Datos consolidados en el archivo hhi_consolidado.csv.')
add_chart('hhi.png','Gráfico 1. Índice HHI de concentración de la extracción por mineral, 2023. Fuente: elaboración propia con USGS Minerals Yearbook (Tabla 2) y CAMIMEX.')
h2('La matemática con más detalle')
para('El HHI es simplemente la suma de los cuadrados de las cuotas de mercado. Conviene manejarlo primero con las cuotas expresadas como fracción (entre 0 y 1): si hay N productores del mismo tamaño, cada uno tiene cuota 1/N y el índice vale N·(1/N)² = 1/N. Así, dos empresas iguales dan 1/2 = 0.50; cuatro iguales, 0.25; un monopolio, 1. Para pasar a la escala habitual de 0 a 10 000 se multiplica por 10 000 (equivale a usar las cuotas en porcentaje): dos empresas iguales = 5 000, un monopolio = 10 000.')
formula([('HHI = ',''),('Σ',''),(' ',''),('s',''),('i','sub'),('2','sup'),('    ·    número efectivo de competidores = 1 ÷ HHI','')])
para('Una lectura útil es el “número efectivo de competidores”, igual a 1 dividido entre el HHI (en fracción). Un HHI de 0.25 equivale a 4 competidores efectivos; uno de 0.50, a 2. Elevar las cuotas al cuadrado hace que el índice pese mucho más a los grandes que a los pequeños: por eso distingue bien un mercado con un líder dominante de otro repartido entre iguales, aunque el número de empresas sea el mismo. Al elevar al cuadrado, las cuotas pequeñas (un productor con 2–3 %) casi no cambian el resultado; el índice lo determinan los líderes.')
h2('Cómo evoluciona en el tiempo')
para('La serie ahora cubre 1994–2024. Los años 1994–2003 se reconstruyeron a partir de la Tabla 2 y la narrativa del USGS Minerals Yearbook de México para los minerales de régimen estructural inequívoco: manganeso (monopolio de Autlán, 10 000, desde antes de 1994), grafito (duopolio, ~5 848), fluorita (líder Las Cuevas ~75–80 %, ~6 000) y cobre (Grupo México con 79–85 % del cobre-mina). La concentración no es estática: la fluorita salta a monopolio (10 000) en enero de 2012, cuando la fusión que dio origen a Koura/Orbia dejó un solo grupo; la barita se desconcentra al final del periodo (su líder, Baramin, cae de 82 % en 2021 a 37 % en 2023, y el índice baja de ~6 800 a ~605 en 2024); y el cobre se mantiene alto con oscilaciones. La línea vertical de 2020/21 marca un cambio de método: hasta 2020 el índice se aproximó con la participación del líder (se lee como el régimen de concentración, no como cifra exacta) y desde 2021 se calculó con el detalle de producción por mina.')
add_chart('hhi_traj.png','Gráfico 1b. Trayectoria del HHI, 1994–2024 (cuatro minerales ilustrativos). El sombreado y la línea de 2020/21 separan el tramo de régimen (aproximado) del cálculo por mina. Fuente: elaboración propia con USGS Minerals Yearbook y CAMIMEX.')

# ================= 3. GHOSH =================
h1('3. Encadenamiento hacia adelante (índice de Ghosh)')
h2('Qué mide')
para('Cuánto “empuja” cada actividad la producción de las actividades que están más adelante en la cadena (las que usan ese mineral como insumo), comparado con el promedio de la economía. Un valor mayor que 1 indica un empuje superior al promedio.')
h2('Intuición')
para('Dos preguntas espejo sobre el mismo cuadro insumo-producto: hacia atrás, ¿a cuántos proveedores jala el mineral al producirse?; hacia adelante, ¿a cuántas industrias alimenta como insumo? En la minería lo primero suele ser bajo (extraer usa pocos insumos industriales); lo relevante para esta investigación es lo segundo: si el mineral sostiene una cadena industrial dentro del país. Con la cautela de que un valor alto indica arrastre estructural, no necesariamente captura de valor.')
h2('Fórmula')
formula([('G = (I − B)',''),('−1','sup')])
para('G es la matriz inversa de Ghosh, que se calcula a partir de la matriz B de coeficientes de distribución de la economía (I es la matriz identidad). El índice de cada mineral es el promedio de su fila en G, dividido entre el promedio general de la matriz; por eso el umbral de comparación es 1.')
h2('En qué nos basamos y de dónde salen los datos')
para('Se usó la Matriz Insumo-Producto (MIP) del INEGI, a nivel de Clase SCIAN (seis dígitos), en sus dos versiones de datos abiertos comparables: 2013 y 2018. Ocho de los diez minerales tienen una clase propia en la matriz; plomo y zinc comparten una sola clase (se extraen juntos), por lo que su índice es conjunto. Los cálculos se validaron reproduciendo las matrices del propio INEGI. Datos en el archivo mip_encadenamientos_minerales.csv.')
add_chart('ghosh.png','Gráfico 2. Índice de encadenamiento hacia adelante por mineral, corte 2018. La línea marca el umbral 1.0. Fuente: elaboración propia con la MIP del INEGI (2018).')
h2('La matemática con más detalle')
para('La Matriz Insumo-Producto (MIP) registra, para toda la economía, cuánto le vende cada actividad a cada otra. Llamemos Z a esa matriz de flujos (el elemento z de la fila i, columna j, es lo que la actividad i le vende a la j como insumo) y x al vector de producción total de cada actividad. A partir de ahí se construyen dos lecturas complementarias del mismo cuadro:')
para('• Encadenamiento hacia ATRÁS (modelo de Leontief). Se divide cada flujo entre la producción de quien compra: a = z ÷ (producción de j). Eso da la matriz de coeficientes técnicos A (cuánto insumo de i necesita j por cada unidad que produce). Invirtiendo I − A se obtiene la matriz de Leontief L, cuya suma por columnas mide cuánto “jala” cada actividad a sus proveedores.',after=3)
formula([('A: a',''),('ij','sub'),(' = z',''),('ij','sub'),(' ÷ x',''),('j','sub'),('     L = (I − A)',''),('−1','sup'),('     (encadenamiento hacia atrás = suma de columnas de L)','')])
para('• Encadenamiento hacia ADELANTE (modelo de Ghosh). Ahora se divide cada flujo entre la producción de quien vende: b = z ÷ (producción de i). Eso da la matriz de coeficientes de distribución B (a dónde va la producción de i). Invirtiendo I − B se obtiene la matriz de Ghosh G, cuya suma por filas mide cuánto “empuja” cada actividad a las que la usan como insumo aguas abajo. Este es el indicador central para la pregunta de la tesis: ¿el mineral alimenta una cadena industrial dentro del país?',after=3)
formula([('B: b',''),('ij','sub'),(' = z',''),('ij','sub'),(' ÷ x',''),('i','sub'),('     G = (I − B)',''),('−1','sup'),('     (encadenamiento hacia adelante = suma de filas de G)','')])
para('Para poder comparar entre sectores de tamaños muy distintos, el índice se normaliza (Hirschman-Rasmussen): se divide el promedio de la fila del mineral entre el promedio de toda la matriz. Así, 1.0 es exactamente el promedio de la economía; por encima de 1, el mineral empuja más que el sector típico; por debajo, menos.')
formula([('índice adelante',''),('i','sub'),(' = [ (1/n) Σ',''),('j','sub'),(' g',''),('ij','sub'),(' ] ÷ [ (1/n²) Σ',''),('i,j','sub'),(' g',''),('ij','sub'),(' ]','')])
para('Se trabajó con la matriz doméstica (solo la producción de origen nacional, que es la relevante para preguntar por la cadena local) a nivel de Clase SCIAN (la mayor desagregación: ~820–830 actividades). La correctitud de la extracción se verificó reproduciendo, a precisión de máquina, las matrices de coeficientes que el propio INEGI publica.',italic=True,color=MUT)
h2('Tres cortes en el tiempo (2008 → 2013 → 2018)')
para('El índice de Ghosh es una “foto” del año de la matriz, no una serie anual. Se dispone de tres cortes: 2013 y 2018 son comparables entre sí (datos abiertos, bases contiguas); 2008 se incorpora como referencia histórica, en una base y clasificación anteriores, por lo que su nivel no es estrictamente comparable —se lee el orden, no la cifra exacta—. Aun así, el patrón es estable: sílice, grafito, cobre y oro empujan por encima del promedio en los tres cortes, y barita queda abajo. El manganeso aparece bajo en 2008 (1.00) porque en esa clasificación su clase agrupa actividades vecinas más amplias; en 2013 y 2018, ya separado, sube por encima de 1.5.')
add_chart('ghosh_cortes.png','Gráfico 2b. Evolución del índice de encadenamiento hacia adelante en los tres cortes de la MIP (2008 de referencia, 2013 y 2018). Fuente: elaboración propia con la MIP del INEGI.')

# ================= 4. CCV =================
h1('4. Captura de valor en frontera (CCV)')
h2('Qué mide')
para('Qué proporción del valor del producto de referencia se alcanza con lo que México exporta en bruto. Es la versión anual y continua (1992–2025) del encadenamiento hacia adelante. Un valor cercano a 1 significa que lo exportado ya vale casi como el producto de referencia; cercano a 0, que se exporta el recurso muy poco elaborado.')
h2('Intuición')
para('Es la versión "película" (año con año) de lo que el índice de Ghosh ve en "fotos" (dos o tres cortes): qué tan cerca del producto terminado vende México lo que extrae en bruto. Cerca de 1, la forma exportada ya vale casi como el refinado; cerca de 0, se está vendiendo prácticamente la roca. Su virtud es la continuidad: permite ver si la posición del país se mueve o no con los ciclos de precios.')
h2('Fórmula')
formula([('CCV = valor unitario de exportación en bruto (USD/t)  ÷  precio del producto de referencia (USD/t)','')])
para('El numerador es el valor de la exportación dividido entre su peso (valor por tonelada) de la etapa E1 de cada mineral. El denominador es el precio del producto de referencia por tonelada.')
h2('En qué nos basamos y de dónde salen los datos')
para('El numerador se descargó de UN Comtrade (comercio internacional; México como reportante, código 484; flujo de exportación; socio “Mundo”), tomando el valor y el peso neto de las fracciones arancelarias de la etapa E1 de cada mineral, año por año de 1992 a 2025. El denominador son los precios anuales del USGS (serie DS-140, valor unitario de consumo aparente, empalmada con Mineral Commodity Summaries y Cochilco para los años recientes). Numerador y denominador se emparejan por mineral y año. Datos en el archivo ccv_serie.csv.')
para('Nota sobre la lectura del indicador: el CCV es directamente comparable en los metales base (cobre y zinc), donde el concentrado y el metal refinado son productos distintos. En oro y plata no es informativo, porque la fracción exportada es mena o concentrado en toneladas brutas y la referencia es el metal puro (el cociente queda cercano a cero por diferencia de ley, no por captura de valor). En los minerales no metálicos el numerador y la referencia son productos cercanos, por lo que el valor oscila alrededor de 1.',italic=True,color=MUT)
h2('La matemática con más detalle')
para('El numerador es un “valor unitario”: el valor exportado dividido entre el peso exportado, es decir, cuántos dólares vale cada tonelada de lo que México manda al exterior en su forma más cruda (E1). El denominador es el precio internacional por tonelada del producto de referencia (por ejemplo, el metal refinado). El cociente dice qué fracción del valor del producto terminado alcanza ya la forma que se exporta.')
formula([('CCV',''),('m,t','sub'),(' = ( valor exportado',''),('E1','sup'),(' ÷ peso exportado',''),('E1','sup'),(' )  ÷  P',''),('ref','sup'),('     [ USD/t ÷ USD/t → adimensional ]','')])
para('Al ser un cociente entre dos precios por tonelada, el CCV no tiene unidades y es comparable en el tiempo aunque los precios suban o bajen: si el concentrado de cobre vale 22 % de lo que vale el cobre refinado, el CCV es 0.22 lo mismo en 1995 que en 2020. Su poder informativo depende del grupo mineral: en los metales base (cobre, zinc) el concentrado y el metal refinado son productos realmente distintos, y el CCV mide bien la brecha; en oro y plata el cociente queda cerca de cero por una diferencia de ley (se exporta mena en toneladas brutas frente a metal puro), no por falta de captura de valor, por lo que ahí no es informativo; en los no metálicos, numerador y referencia son productos cercanos y el valor oscila alrededor de 1.')
add_chart('ccv.png','Gráfico 3. CCV anual de los metales base, 1992–2025. La línea punteada marca la paridad 1.0. Fuente: elaboración propia con UN Comtrade y precios del USGS.')
para('Cómo evoluciona en el tiempo: la gráfica anual (1992–2025) es, junto con el HHI, la serie más larga del trabajo. El hallazgo es la estabilidad: el CCV del cobre se mantiene alrededor de 0.22 durante más de tres décadas —se exporta concentrado, no cátodo— y el del zinc alrededor de 0.30. Esa persistencia es, precisamente, la firma del enclave estructural: la posición de México en la cadena no se mueve con los ciclos de precios.',italic=True,color=MUT)

# ================= 5. COMERCIO =================
h1('5. Inserción en el comercio mundial por etapa')
h2('Qué mide')
para('En qué forma exporta México cada mineral: como materia en bruto (E1) o ya procesada (E2 en adelante). Muestra en qué eslabón de la cadena se inserta el país en el mercado internacional.')
h2('Intuición')
para('De todo lo que México exporta de un mineral, ¿qué parte es materia en bruto y qué parte ya lleva proceso? Es la forma más directa de ver en qué escalón de la cadena se baja el país. Comparar lo que se exporta con lo que se importa —el análisis espejo— confirma el patrón: exportar en bruto e importar el producto procesado del mismo mineral es la señal de que la transformación ocurre fuera.')
h2('Fórmula')
formula([('Participación del crudo = exportación en bruto (E1)  ÷  exportación total','')])
para('Se calcula qué parte del valor total exportado de cada mineral corresponde a la forma en bruto; el resto corresponde a las formas procesadas.')
h2('En qué nos basamos y de dónde salen los datos')
para('Los flujos de comercio provienen de UN Comtrade (México como reportante, código 484; socio “Mundo”), para el periodo 2015–2024. Cada fracción arancelaria (HS) se clasificó en su etapa de procesamiento mediante una tabla de correspondencia mineral–etapa–fracción elaborada para el proyecto. Datos en los archivos comercio_posicion_resumen.csv y concordancia_hs_etapa.csv.')
add_chart('comercio.png','Gráfico 4. Composición de las exportaciones por etapa (promedio 2020–2024). Fuente: elaboración propia con UN Comtrade. Nota: en oro y plata la parte “procesada” corresponde a doré o bullion, la forma habitual de exportación.')
h2('La matemática con más detalle')
para('El indicador es una proporción simple: del total exportado de un mineral (sumando todas sus etapas), qué parte corresponde a la forma en bruto. La misma cuenta se hace del lado de las importaciones para obtener el “análisis espejo”: si un país exporta el mineral crudo e importa la forma procesada del mismo mineral, es señal de que la transformación ocurre fuera. Comparar las dos composiciones —lo que se exporta frente a lo que se importa— revela en qué eslabón se inserta el país.')
formula([('participación del crudo',''),('m,t','sub'),(' = X',''),('E1','sup'),(' ÷ X',''),('total','sup'),('     (espejo: se compara con la composición de las importaciones)','')])
h2('Cómo evoluciona en el tiempo')
para('La serie 2015–2024 muestra que la composición se mueve. En el cobre, la parte exportada en bruto sube (de ~42 % a ~80 %): se refina proporcionalmente menos dentro del país. En la fluorita, el pico de 2021–2023 y la caída de 2024 acompañan el colapso de las exportaciones de ácido fluorhídrico (de ~160 millones de dólares antes de 2020 a casi cero), el único eslabón avanzado del mineral. Sílice y zinc oscilan sin tendencia clara.')
add_chart('comercio_evo.png','Gráfico 4b. Participación del bruto (E1) en las exportaciones, evolución 2015–2024. Fuente: elaboración propia con UN Comtrade.')

# ================= 6. COMPARACION INTERNACIONAL Y VALOR RETENIDO =================
h1('6. Comparación internacional y valor retenido')
h2('Qué mide y por qué se añade')
para('Los cuatro indicadores anteriores describen a México por dentro. Para poner a prueba la etiqueta de “casos de éxito” que el protocolo atribuye a Chile y Australia, se compara el encadenamiento hacia adelante de la minería de México con el de otros siete países: Chile y Australia (los del protocolo), el clúster nórdico (Finlandia y Suecia) y —para completar el cuadro— China, Brasil y Perú. La selección tiene una lógica: China es el procesador global (a donde va el 94.7 % del concentrado de cobre mexicano: el extremo opuesto, donde se captura el valor); Brasil es el par latinoamericano por tamaño y estructura industrial; y Perú, el vecino andino con la misma canasta polimetálica que México (sirve para ver si el enclave es un rasgo mexicano o regional). Se usa una fuente homogénea: las tablas insumo-producto inter-país de la OCDE (edición 2023). Para que sea comparable con los encadenamientos de la sección 3, se calcula en los mismos tres cortes: 2008, 2013 y 2018. Es una comparación a nivel del sector-minería agregado —no por mineral—, por lo que se lee como contraste, con ese matiz.')
h2('Intuición')
para('Poner a México en la misma vara que los países que el protocolo llama "casos de éxito": ¿de veras encadenan más hacia adelante, o solo son economías mineras más grandes? Y, en dinero, ¿cuánto del valor de su minería se queda transformado en casa y cuánto se va en crudo para procesarse afuera? Es el enclave mirado desde afuera (comparación) y desde el valor (descomposición).')
h2('Encadenamiento de la minería: México frente a los referentes (2008 · 2013 · 2018)')
ig={}
for r in rd('icio_comparacion_mineria.csv'):
    if r['sector']=='B07_08': ig[(r['pais'],r['anio'])]=float(r['forward_rasmussen'])
def g3(p): return ig.get((p,'2008'),0),ig.get((p,'2013'),0),ig.get((p,'2018'),0)
mx=g3('MEX'); ch=g3('CHL'); au=g3('AUS'); fi=g3('FIN'); sw=g3('SWE'); cn=g3('CHN'); br=g3('BRA'); pe=g3('PER')
para(f"Sobre el bloque doméstico de cada país se calcula el mismo índice de Ghosh de la sección 3 (media de la economía = 1), en los tres cortes. El patrón es estable: Chile ({ch[0]:.2f}→{ch[2]:.2f}), Australia ({au[0]:.2f}→{au[2]:.2f}), Brasil ({br[0]:.2f}→{br[2]:.2f}) y Perú ({pe[0]:.2f}→{pe[2]:.2f}) quedan en o por debajo del promedio de su propia economía —no son casos de éxito en encadenamiento hacia adelante; Perú es el más bajo—; China ({cn[0]:.2f}→{cn[2]:.2f}), Finlandia ({fi[0]:.2f}→{fi[2]:.2f}) y Suecia ({sw[0]:.2f}→{sw[2]:.2f}) se mantienen por encima (China por su complejo metalúrgico global; los nórdicos por fundición doméstica: Boliden, Harjavalta). México aparece alto ({mx[0]:.2f}→{mx[2]:.2f}) —casi idéntico a China—, pero ese número engaña, como explica el indicador siguiente: con un Ghosh casi igual al chino, la realidad es opuesta.")
add_chart('intl_ghosh.png','Gráfico 5. Encadenamiento hacia adelante del sector-minería no energética (corte 2018, con el valor de 2008 anotado), ocho países (OECD ICIO). Fuente: elaboración propia. La comparación es a nivel sector, no por mineral.')
h2('El enclave “en dinero”: valor retenido frente a reprocesado en el extranjero')
para('Sobre la misma matriz global se descompone el valor agregado que la minería de cada país exporta, separando la parte que sale ya transformada dentro del país de la que sale en crudo (concentrado) para reprocesarse en el extranjero. Un valor alto de “exportado en crudo” es la firma del enclave, ahora medida en valor.')
dser={}
for r in rd('icio_dva_mineria.csv'):
    if r['sector']=='B07_08' and r['crudo_share']!='': dser.setdefault(r['pais'],[]).append((int(r['anio']),float(r['crudo_share'])))
mx=dict(dser.get('MEX',[])); chl=dict(dser.get('CHL',[])); cnd=dict(dser.get('CHN',[])); ped=dict(dser.get('PER',[]))
para(f"Chile y Perú exportan en crudo casi todo el valor de su minería (≈{ped.get(2018,0)*100:.0f} % Perú, ≈{chl.get(2018,0)*100:.0f} % Chile en 2018) —los enclaves más profundos; Perú comparte la canasta polimetálica de México, lo que muestra que el enclave no es un rasgo idiosincrásico sino de la (falta de) integración aguas abajo—. En el extremo opuesto, China exporta en crudo solo el {cnd.get(2018,0)*100:.0f} %: funde casi todo, es a donde va el valor que los demás no capturan. México aparece bajo en el agregado (≈{round(100*sum(v for _,v in dser['MEX'])/len(dser['MEX']))} %), pero por la misma razón que su índice de Ghosh alto: promedia los metales preciosos que sí se funden en el país con el cobre que sale 94.7 % en concentrado. Que México (Ghosh 1.51, crudo 38 %) y China (1.53, crudo 7 %) tengan un Ghosh casi idéntico pero una realidad opuesta es la prueba más clara de que el enclave del cobre solo se ve al desagregar. Además, de punta a punta el patrón mexicano se profundiza: el crudo pasa de {mx.get(1995,0)*100:.0f} % (1995) a {mx.get(2020,0)*100:.0f} % (2020), y el valor de su minería absorbido en el extranjero sube del 21 % al 65 %.")
add_chart('dva.png','Gráfico 6. Fracción del valor agregado minero exportado en crudo (a reprocesar en el extranjero), corte 2018, ocho países. Fuente: elaboración propia con OECD ICIO.')
h2('La dimensión regional (geografía de la cadena)')
reg=rd('georref_regionalizacion.csv'); ncol=sum(1 for r in reg if r['colocalizado_extraccion_E2']=='si')
para(f"La cadena también tiene una dimensión territorial. La extracción está muy localizada (grafito y manganeso son monopolios de un solo estado; la fluorita, 96 % en San Luis Potosí), pero la transformación se concentra en unos pocos nodos metalúrgicos que casi nunca coinciden con el estado extractor: de los diez minerales, solo el cobre tiene su fundición en el mismo estado que la mina (Sonora); en los otros nueve el valor agregado —cuando existe— se deslocaliza a hubs como Torreón (Coahuila), Nuevo León o Tamaulipas, o simplemente no ocurre. Esa desconexión espacial entre extracción y transformación es la expresión geográfica del enclave. (El cálculo del encadenamiento por estado con cocientes de localización requiere la matriz de PIB por entidad y sector de INEGI, sólo disponible por descarga interactiva; se documenta como pendiente.)")

# ================= 7. CUADRO RESUMEN =================
h1('7. Cuadro resumen de los datos')
para('Las cifras principales de los cuatro indicadores, por mineral.')
orden=['cobre','zinc','plomo','oro','plata','barita','fluorita','grafito','silice','manganeso']
t=doc.add_table(rows=1,cols=5); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
widths=[Cm(3.3),Cm(3.1),Cm(3.4),Cm(2.9),Cm(3.3)]
hdr=['Mineral','HHI (2023)','Ghosh adelante (2018)','CCV (media)','% exportado en bruto (2020–24)']
for j,htxt in enumerate(hdr):
    set_cell(t.rows[0].cells[j],htxt,bold=True,size=9.5,color=RGBColor(0xff,0xff,0xff),align=WD_ALIGN_PARAGRAPH.CENTER)
    shade(t.rows[0].cells[j],'211d18'); t.rows[0].cells[j].width=widths[j]
for m in orden:
    row=t.add_row()
    ghv=gh18.get(m);
    if ghv is None and m in ('plomo','zinc'): ghv=gh18.get('plomo-zinc')
    gh_txt=(f"{ghv:.2f}"+(" *" if m in ('plomo','zinc') else "")) if ghv else "—"
    vals=[NAMES[m], f"{hhi23.get(m,'—'):,}" if m in hhi23 else "—", gh_txt,
          f"{ccvmean[m]:.2f}" if m in ccvmean else "—",
          f"{round(crudo[m]*100)}%" if m in crudo else "—"]
    for j,v in enumerate(vals):
        set_cell(row.cells[j],v,size=9.5,align=(WD_ALIGN_PARAGRAPH.LEFT if j==0 else WD_ALIGN_PARAGRAPH.CENTER))
        row.cells[j].width=widths[j]
caption('* Plomo y zinc comparten una sola clase en la MIP (se extraen juntos): el índice de Ghosh es conjunto. El CCV de oro y plata no es informativo (ver sección 4). El HHI de 2004–2020 es aproximado; aquí se muestra el dato de 2023.')

# ================= 7. FUENTES =================
h1('8. De dónde salen los datos (fuentes)')
fuentes=[
 ('UN Comtrade','Comercio internacional por fracción arancelaria (HS). México como reportante (código 484), socio “Mundo”. Se usó para el CCV (valor y peso de las exportaciones en bruto, 1992–2025) y para el comercio por etapa (2015–2024).'),
 ('USGS — Minerals Yearbook (Tabla 2)','Estructura de la industria minera de México (empresas, propietarios, capacidad), leída edición por edición 1994–2024. Base del HHI de concentración, incluida la reconstrucción 1994–2003.'),
 ('OECD — ICIO (edición 2023)','Tablas insumo-producto inter-país (77 economías × 45 industrias, 1995–2020). Base de la comparación internacional del encadenamiento de la minería y de la descomposición de valor agregado (enclave “en dinero”).'),
 ('USGS — DS-140 y Mineral Commodity Summaries','Precios anuales de los productos de referencia por mineral, empalmados con Cochilco para los años recientes. Denominador del CCV.'),
 ('INEGI — Matriz Insumo-Producto','Versiones 2013 y 2018 (datos abiertos, nivel Clase SCIAN) para la serie comparable, y 2008 (tabulados en Excel, base y clasificación anteriores) como corte de referencia histórica. Base del índice de encadenamiento hacia adelante (Ghosh).'),
 ('CAMIMEX','Informes Anuales de la Cámara Minera de México. Complemento para participaciones de mercado (HHI). Convención: el Informe del año N reporta el dato del año N−1.'),
]
for nom,desc in fuentes:
    p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(6)
    r=p.add_run('• '+nom+'. '); r.bold=True; r.font.size=Pt(11); r.font.name='Times New Roman'
    r2=p.add_run(desc); r2.font.size=Pt(11); r2.font.name='Times New Roman'
para('',after=2)
para('Todos los indicadores son de elaboración propia a partir de estas fuentes. Los archivos de datos procesados (hhi_consolidado.csv, mip_encadenamientos_minerales.csv, ccv_serie.csv, comercio_posicion_resumen.csv) están en la carpeta 10 Datos/processed del proyecto.',size=10.5,italic=True,color=MUT)

# ================= 8. GUION DE LA PRESENTACION DEL PROTOCOLO =================
doc.add_page_break()
h1('9. Guion de la presentación del protocolo (diapositiva por diapositiva)')
para('Esta sección acompaña la presentación del protocolo de investigación (18 diapositivas). Para cada una se indica qué muestra y qué conviene decir al exponerla. Donde una decisión del protocolo tuvo que ajustarse en la práctica, se explica cómo se planteaba al inicio, cómo se aborda ahora y por qué; en la presentación esas diapositivas van agrupadas al final (“Ajustes metodológicos”).')

def slide(n,title,text,extra=None):
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(8); p.paragraph_format.space_after=Pt(2)
    r=p.add_run('Diapositiva %d — %s'%(n,title)); r.bold=True; r.font.size=Pt(11.5); r.font.name='Times New Roman'; r.font.color.rgb=COP
    para(text,size=11,after=(3 if extra else 8))
    if extra:
        pe=doc.add_paragraph(); pe.paragraph_format.space_after=Pt(8); pe.paragraph_format.left_indent=Cm(0.5)
        r=pe.add_run('Ajuste (planteado → ahora → por qué): '); r.bold=True; r.italic=True; r.font.size=Pt(10.5); r.font.name='Times New Roman'; r.font.color.rgb=MUT
        r2=pe.add_run(extra); r2.italic=True; r2.font.size=Pt(10.5); r2.font.name='Times New Roman'; r2.font.color.rgb=MUT

slide(1,'Portada','Presenta el tema: la extracción de minerales críticos y el encadenamiento productivo en México, 1992–2025, para diez minerales. Se enmarca en la Maestría en Economía (campo Empresas, Finanzas e Innovación) y se nombra al asesor. Conviene anticipar la idea central: describir en qué eslabón de la cadena de valor participa México.')
slide(2,'Planteamiento del problema','Entre 1988 y 1994 se privatizaron y concentraron las reservas mineras; tres décadas después México es primer productor mundial de plata y actor central en varios minerales, con capital mayoritariamente nacional. Punto clave: distinguir el hecho (se exporta en bruto) del problema de investigación (describir con rigor cómo son esos mercados), y mencionar la reforma a la Ley Minera de 2023 como contexto.')
slide(3,'Justificación','Existen tres literaturas que casi no se cruzan: la economía minera (mide producción, no cadena), el extractivismo crítico (describe, mide poco) y el análisis insumo-producto/cadenas de valor (herramientas poco aplicadas por mineral). La tesis tiende el puente construyendo datos e indicadores por mineral. Se ancla en la tradición estructuralista (Prebisch) y responde al campo EFI.')
slide(4,'Preguntas de investigación','Una pregunta central —cómo son estos mercados y cómo se inserta México en sus cadenas globales— y tres subsidiarias, una por objetivo: estructura y concentración (P1), cadenas locales e industria usuaria (P2), inserción global (P3).')
slide(5,'Objetivos','El objetivo general (caracterizar los mercados y las cadenas de valor) se despliega en tres específicos que corresponden uno a uno con las preguntas: describir la estructura extractiva y el encadenamiento; mapear la cadena local; situar a México en las cadenas globales.')
slide(6,'Hipótesis','La hipótesis general nombra el rasgo que se espera describir: estructura extractiva concentrada y débil articulación con la industria local —el enclave estructural—. Las tres subsidiarias (H1, H2, H3) se enuncian como co-ocurrencias descriptivas, no como relaciones causales; conviene subrayar ese matiz.')
slide(7,'Marco teórico — enclave estructural','Es el concepto que ordena todo el trabajo. Se llega a él por contraste: el enclave clásico (Cardoso y Faletto) se define por la propiedad extranjera del capital; aquí el capital es mayoritariamente nacional, pero la cadena se desconecta aguas abajo. Ese es el enclave estructural, con respaldo en el neo-extractivismo (Svampa). El mensaje: el problema no es de quién es la mina, sino dónde se detiene la cadena.')
slide(8,'Enfoque y horizonte temporal','El enfoque es descriptivo y de métodos mixtos; la unidad de observación es el mineral-año. El horizonte es 1992–2025 (de la Ley Minera al cierre de datos). Punto importante para el público: el detalle temporal depende de la fuente —unos indicadores son series anuales, otros son cortes puntuales de la matriz insumo-producto—.')
slide(9,'Fuentes de información','Enumera de dónde sale cada dato: MIP del INEGI, comercio de UN Comtrade, estructura y precios del USGS, participaciones de CAMIMEX, reportes corporativos para la cadena, y el marco legal (Ley Minera 1992 y reforma 2023). TiVA/ICIO y entrevistas quedan como complementos opcionales.')
slide(10,'Técnicas de análisis','Presenta los cuatro descriptores y a qué objetivo sirve cada uno: HHI (concentración), Leontief/Ghosh/CCV (encadenamiento), demanda intermedia (cadena local), comercio por etapa (inserción global). Aquí se puede remitir a las secciones 2–5 de este documento para la matemática.')
slide(11,'Ajustes metodológicos (portada de sección)','Diapositiva de transición: anuncia que, al ejecutar el trabajo, algunas decisiones del protocolo se ajustaron a lo que los datos y el asesor hicieron posible, y que el protocolo conserva esas marcas a la espera del visto bueno del asesor. Sirve para dar transparencia metodológica.')
slide(12,'Ajuste 1 — de causal a descriptivo','Es el cambio de fondo. Explicar el giro y por qué mejora la investigación.',
      'Se planteaba un modelo causal de panel (la concentración explicaría el encadenamiento) con un event study de la reforma. Ahora es una descripción de las cadenas de valor: HHI, Ghosh y CCV se usan como descriptores, no como variables de un modelo, y el aporte es la construcción de datos e indicadores por mineral. Por qué: se acordó con el asesor (jul-2026) y se afinó en el análisis de consistencia; con tan pocos cortes de matriz no hay base para una identificación causal creíble, y la contribución novedosa —ausente en la literatura— es medir y describir la desconexión.')
slide(13,'Ajuste 2 — cortes de la Matriz Insumo-Producto','Qué años de MIP se pueden usar realmente por mineral.',
      'Se planteaban cuatro cortes (2003, 2008, 2012, 2018) actualizables con el método RAS a 2020 y 2023. Ahora se usan 2013 y 2018 como serie comparable y 2008 como referencia histórica, validada a precisión de máquina; 2003 (solo Sector) y 2012 (solo Rama) quedan fuera por mineral, y RAS 2020/2023 es opcional. Por qué: en datos abiertos solo 2013 y 2018 llegan al nivel de Clase (el mineral); la MIP 2008 baja a Clase pero en base distinta, por lo que se incorpora con caveats. Aun así se logra profundidad 2008 → 2013 → 2018.')
slide(14,'Ajuste 3 — el CCV como serie anual','Cómo se dio continuidad temporal al encadenamiento hacia adelante.',
      'El coeficiente de captura de valor se planteaba junto a Leontief/Ghosh, ligado a los cortes discretos de la matriz. Ahora se construye como serie anual 1992–2025, con el valor unitario de exportación en bruto (Comtrade) sobre el precio de referencia (USGS). Por qué: el Ghosh es una foto de dos o tres años y el periodo elegido abarca 34; el CCV aporta la continuidad anual y funciona como segunda medida del encadenamiento hacia adelante (informativa en metales base; no informativa en oro/plata).')
slide(15,'Ajuste 4 — cobertura real de las series','Hasta dónde llega efectivamente cada dato.',
      'Se planteaban series continuas 1992–2025 para HHI y comercio. En la práctica el HHI cubre 1994–2024 (los años 1994–2003 se reconstruyeron por régimen con el USGS Minerals Yearbook para manganeso, fluorita, grafito y cobre; 1994–2020 es aproximado y no comparable en nivel con 2021–2024), el comercio por etapa 1992–2024, y el CCV todo el periodo. Por qué: donde el dato de estructura por empresa no existe se declara el hueco (1992–1993) y el quiebre de método, y el HHI se lee como indicador de régimen.')
slide(16,'Cobertura del periodo elegido','Responde directamente si están cubiertos los cálculos para 1992–2025. Sí: las series continuas cubren el periodo (CCV 1992–2025; HHI 1994–2024; comercio por etapa 1992–2024) y los encadenamientos tienen tres cortes de matriz (2008/2013/2018), complementados con la comparación internacional (ICIO, cortes 2008/2013/2018) y la descomposición de valor agregado (1995–2020). Quedan como opcionales/pendientes el RAS 2020/2023 y el encadenamiento por estado con la matriz PIB estatal por sector de INEGI.')
slide(17,'Cronograma','Muestra las fases sobre doce meses (jul 2026 – jun 2027). Al exponer, situar el avance real: la fase de datos está completa, el frente activo es la inserción global, la síntesis y la redacción, y las revisiones con el asesor son continuas.')
slide(18,'Contribución (cierre)','Cierra con el mensaje central: el valor de la tesis no está en un modelo econométrico, sino en construir y describir datos e indicadores que no existían por mineral —HHI 1994–2024, encadenamientos en tres cortes, CCV de 34 años, comercio por etapa, la comparación internacional (que reencuadra el “éxito”: el referente real es el modelo nórdico, no Chile/Australia) y la descomposición de valor agregado que mide el enclave en dinero—, ordenados por el concepto de enclave estructural y con bases para pensar una política industrial.')

doc.save(OUT)
print('escrito:',OUT)
print('parrafos:',len(doc.paragraphs))
