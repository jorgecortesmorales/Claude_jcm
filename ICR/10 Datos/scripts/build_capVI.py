# -*- coding: utf-8 -*-
"""Capitulo VI - Caracterizacion de los mercados (tipologia descriptiva). python-docx."""
import sys
import os
from docx import Document
from docx.shared import Pt, RGBColor, Twips, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

MAPA_CONJUNTO = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\mapas\mapa_conjunto.png"
def add_map(doc, path, cap, width_in=6.3):
    if not os.path.exists(path): return
    doc.add_picture(path, width=Inches(width_in))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    c=doc.add_paragraph(); c.alignment=WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after=Pt(8); r=c.add_run(cap); r.font.italic=True; r.font.size=Pt(8)
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def para(doc, runs, justify=True, first=False, after=6):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
    pf=p.paragraph_format; pf.space_after=Pt(after); pf.line_spacing=1.15
    if first: pf.first_line_indent=Pt(21)
    for r in runs:
        if isinstance(r,str): p.add_run(r)
        else:
            txt,opt=r; run=p.add_run(txt)
            run.font.italic=opt.get("i",False); run.font.bold=opt.get("b",False)
    return p
def H1(doc,text):
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(14); p.paragraph_format.space_after=Pt(6)
    r=p.add_run(text); r.font.bold=True; r.font.size=Pt(14); r.font.color.rgb=RGBColor(0x1A,0x1A,0x1A)
def H2(doc,text):
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(10); p.paragraph_format.space_after=Pt(4)
    r=p.add_run(text); r.font.bold=True; r.font.size=Pt(12); r.font.color.rgb=RGBColor(0x33,0x33,0x33)
def shade(cell,fill):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement("w:shd")
    shd.set(qn("w:val"),"clear"); shd.set(qn("w:color"),"auto"); shd.set(qn("w:fill"),fill); tcPr.append(shd)
def add_table(doc,widths,headers,rows,fs=9):
    tbl=doc.add_table(rows=1,cols=len(headers)); tbl.style="Table Grid"; tbl.alignment=WD_TABLE_ALIGNMENT.CENTER
    hdr=tbl.rows[0].cells
    for i,h in enumerate(headers):
        hdr[i].text=""; run=hdr[i].paragraphs[0].add_run(h); run.font.bold=True; run.font.size=Pt(fs)
        hdr[i].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.LEFT; shade(hdr[i],"E8E8E8")
    for r in rows:
        cells=tbl.add_row().cells
        for i,v in enumerate(r):
            cells[i].text=""; run=cells[i].paragraphs[0].add_run(str(v)); run.font.size=Pt(fs)
            cells[i].paragraphs[0].alignment=WD_ALIGN_PARAGRAPH.LEFT
    tbl.autofit=False
    for row in tbl.rows:
        for i,w in enumerate(widths): row.cells[i].width=Twips(w)
    return tbl
def caption(doc,text):
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(2); p.paragraph_format.space_after=Pt(8)
    r=p.add_run(text); r.font.italic=True; r.font.size=Pt(8)

B=lambda s:(s,{"b":True}); I=lambda s:(s,{"i":True})

# ============ CONTENIDO ============
# Productos por fase: (fase, productos, HS)
PROD = {
"Cobre":[
 ("Fase 1 · Extracción (mena/concentrado)","Mineral de cobre (sulfuros, calcopirita); concentrado de cobre (~25–30% Cu); cátodo SX-EW.","2603"),
 ("Fase 2 · Transformación primaria (metal refinado)","Mata de cobre; cobre blíster y ánodos; cátodo de cobre refinado (99.99%); aleaciones madre.","7401–7403, 7405"),
 ("Fase 3 · Semimanufactura","Alambrón; alambre; barras y perfiles; láminas, tiras y hojas; tubos y accesorios; cables trenzados.","7407–7413"),
 ("Fase 4 · Manufactura (bien final)","Conductores y cables eléctricos aislados; conexiones; artículos de cobre.","7415, 7418, 7419, 8544"),
],
"Plomo":[
 ("Fase 1 · Extracción","Concentrado de plomo (galena, PbS).","2607"),
 ("Fase 2 · Metal refinado","Plomo en bruto y refinado (lingote); plomo antimonial.","7801"),
 ("Fase 3 · Semimanufactura","Planchas, hojas, tiras, tubos y polvo de plomo.","7804"),
 ("Fase 4 · Manufactura","Acumuladores (baterías) plomo-ácido; óxidos (litargirio, minio); municiones y blindajes.","7806, 8507"),
],
"Zinc":[
 ("Fase 1 · Extracción","Concentrado de zinc (esfalerita, ZnS).","2608"),
 ("Fase 2 · Metal refinado","Zinc en bruto y refinado (SHG); aleaciones (zamak).","7901"),
 ("Fase 3 · Semimanufactura","Polvo y escamas de zinc; barras, perfiles y alambre; láminas y tiras.","7903–7905"),
 ("Fase 4 · Manufactura","Recubrimiento galvanizado de acero; óxido de zinc; artículos de zinc.","7907"),
],
"Manganeso":[
 ("Fase 1 · Extracción","Mineral de manganeso (óxidos y carbonatos); nódulos.","2602"),
 ("Fase 2 · Ferroaleaciones y químicos","Ferromanganeso (alto/bajo carbono); silicomanganeso; manganeso metálico; dióxido de manganeso (MnO₂).","720211/19/30, 8111, 282010"),
 ("Fase 3–4 · Usos","Acero (aleante y desoxidante); pilas secas (MnO₂); fertilizantes y químicos; aleaciones de aluminio.","(insumo)"),
],
"Oro":[
 ("Fase 1 · Extracción","Mineral y concentrado de metales preciosos.","261610"),
 ("Fase 2 · Metal refinado","Oro en bruto (doré, lingote); oro semilabrado y en polvo.","7108"),
 ("Fase 4 · Manufactura","Joyería y orfebrería; oro de inversión; oro para electrónica.","7113–7115"),
],
"Plata":[
 ("Fase 1 · Extracción","Mineral y concentrado de plata.","261690"),
 ("Fase 2 · Metal refinado","Plata en bruto y refinada; semilabrada y en polvo.","7106"),
 ("Fase 4 · Manufactura","Joyería y platería; monedas; plata industrial (fotovoltaica, electrónica, catálisis).","7113–7114"),
],
"Barita":[
 ("Fase 1 · Extracción","Barita cruda y molida: grado perforación (API, densidad ≥4.2) y grado químico.","251110"),
 ("Fase 2 · Químicos de bario","Carbonato de bario; sulfato de bario precipitado (blanc fixe); óxido/hidróxido de bario.","283660, 281640"),
 ("Fase 3–4 · Usos","Lodos de perforación; pigmentos y cargas; vidrio y cerámica; aditivos.","(insumo)"),
],
"Fluorita":[
 ("Fase 1 · Extracción","Espato flúor: grado metalúrgico (metspar, ≤97% CaF₂) y grado ácido (acidspar, >97%).","252921, 252922"),
 ("Fase 2 · Fluoroquímica primaria","Ácido fluorhídrico (HF); fluoruro de aluminio (AlF₃); criolita; otros fluoruros.","281111, 282612, 282619"),
 ("Fase 3–4 · Alto valor","Fluoropolímeros (PTFE); gases refrigerantes (HFC); fluoroelastómeros; sales de litio (LiPF₆) para baterías.","390461, 2903.7x"),
],
"Grafito":[
 ("Fase 1 · Extracción","Grafito natural: en hojuela (flake), amorfo y en polvo.","250410, 250490"),
 ("Fase 2 · Grafito procesado","Grafito artificial/sintético; grafito coloidal; pasta para electrodos.","3801"),
 ("Fase 3–4 · Manufactura","Electrodos de grafito (horno de arco eléctrico); refractarios; ánodos de grafito esferoidal (baterías Li-ion); lubricantes; frenos.","8545"),
],
"Sílice":[
 ("Fase 1 · Extracción","Arena sílica; cuarzo; cuarcita.","250510, 250610"),
 ("Fase 2 · Silicio y químicos","Dióxido de silicio (SiO₂); silicio metálico; ferrosilicio.","281122, 280461/69, 720221/29"),
 ("Fase 3–4 · Manufactura","Vidrio (envases y plano); cemento y cerámica; obleas de silicio (electrónica y fotovoltaica); sílice pirogénica.","(insumo)"),
],
}
# Caracterizacion: (concentracion, ghosh, posicion_comercio, cadena_local, veredicto)
CHAR = {
"Cobre":("Alta (HHI ≈ 3,650) — Grupo México dominante (~60% de la producción).","1.34 (sobre la media)","Exporta mena/concentrado (61%→80% de sus exportaciones 2018–2023) e importa semimanufacturas.","Fundición y refinación (Grupo México: La Caridad, Cananea; Cobre de México) y algo de semis (Viakable, Condumex).","Cadena parcial: llega al refinado y a algunos semis; la manufactura de conductores no absorbe todo el metal, que se exporta."),
"Plomo":("Baja-moderada (HHI ≈ 1,450) — liderazgo rotatorio (Newmont/Peñoles/Fresnillo).","0.71 (bajo; conjunto plomo-zinc en la MIP)","Exporta concentrado (78–87%); refina parte.","Refinación (Met-Mex Peñoles) y baterías (Clarios/LTH).","Exporta concentrado; refina; único vínculo manufacturero relevante (baterías)."),
"Zinc":("Baja-moderada (HHI ≈ 1,450) — Peñoles líder (~26%), varios productores.","0.71 (bajo; conjunto plomo-zinc)","Exporta concentrado y algo de zinc refinado (Torreón).","Refinación (Met-Mex Peñoles; IMMSA en S.L.P.); galvanizado del acero.","Refina parcialmente; el grueso se exporta en concentrado."),
"Manganeso":("Máxima — Autlán, productor único (HHI ≈ 10,000).","1.54 (alto)","Exporta poco; importa químicos de manganeso.","La más integrada: Autlán, de la mina (Molango) a ferroaleaciones (Tamós, Teziutlán, Gómez Palacio) → siderurgia.","Cadena local fuerte y vertical: es el caso con mayor transformación doméstica."),
"Oro":("Baja (HHI ≈ 500) — mercado fragmentado; muchos productores nacionales y extranjeros, líder ~12–17%.","1.22 (≈ media)","Exporta oro en bruto/doré (~95%).","Refinación de metales preciosos (Met-Mex Peñoles); la joyería es importadora neta.","Llega al metal refinado; no continúa a manufactura de valor."),
"Plata":("Baja (HHI ≈ 890) — Fresnillo líder (~24–27%).","1.18 (≈ media)","Exporta plata en bruto/refinada.","Refinación (Met-Mex Peñoles); usos industriales y joyería.","Hasta metal refinado; manufactura de valor limitada."),
"Barita":("Alta y decreciente (HHI 6,779 en 2021 → 1,380 en 2023) — Baramin pierde el liderazgo (82%→37%).","0.64 (el más bajo)","Se exporta en bruto; uso doméstico marginal.","Servicios petroleros: PEMEX se abastece de barita de Coahuila/Sonora para lodos de perforación.","Cadena mínima: sin eslabón manufacturero; exportación en bruto."),
"Fluorita":("Máxima — Koura/Orbia, monopolio de grupo desde 2012 (HHI ≈ 10,000).","1.31 (alto)","Exporta espato flúor y ácido fluorhídrico (HF); importa fluoropolímeros.","Koura opera en Matamoros la mayor planta de HF del mundo, integrada con la mina Las Cuevas.","Cadena hasta el HF (escala mundial); se trunca antes de los fluoropolímeros de mayor valor, que se importan."),
"Grafito":("Máxima — productor único desde 2014 (HHI ≈ 10,000).","1.71 (alto)","Exporta poco grafito; importa electrodos (importador neto).","Usuario siderúrgico (Ternium, ArcelorMittal, DeAcero, Gerdau vía CANACERO): 96.7% del acero por horno de arco eléctrico.","La industria usuaria existe, pero los electrodos de grafito se importan: eslabón intermedio ausente. La producción cae (≈2,150 t en 2024, −20 % anual) mientras la criticidad del grafito sube, sin paradoja: México produce grafito amorfo, no el grado batería (flake/esférico/sintético) cuyo auge monopoliza China."),
"Sílice":("Muy alta (HHI ≈ 7,300) — Covia/GMP dominante (74–99%).","1.92 (el más alto)","Exporta poco; importa silicio/ferrosilicio (importador neto).","Vidrio (Vitro, Owens-Illinois, con extracción propia de arena) y cemento/cerámica (CEMEX, Holcim, Cruz Azul, GCC).","Cadena de vidrio y construcción amplia, pero de baja gama; el silicio de mayor valor se importa."),
}
ORDER=["Cobre","Plomo","Zinc","Manganeso","Oro","Plata","Barita","Fluorita","Grafito","Sílice"]

# ============ DOCUMENTO ============
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Times New Roman"; normal.font.size=Pt(12)
sec=doc.sections[0]
sec.page_width=Twips(12240); sec.page_height=Twips(15840)
for m in ("top_margin","bottom_margin","left_margin","right_margin"): setattr(sec,m,Twips(1701))

p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(2)
p.add_run("Capítulo VI").bold=True; p.runs[0].font.size=Pt(16)
p2=doc.add_paragraph(); p2.paragraph_format.space_after=Pt(12)
r2=p2.add_run("Caracterización de los mercados de los minerales críticos"); r2.font.bold=True; r2.font.size=Pt(14)

H1(doc,"VI.1  Propósito y enfoque")
para(doc,["Este capítulo caracteriza, mineral por mineral, los diez mercados de minerales críticos y construye una ",
 B("tipología descriptiva"),
 " de su posición en las cadenas de valor. Integra los tres objetivos previos —la estructura extractiva y los encadenamientos (Cap. V), la cadena de valor local (empresas de transformación) y la inserción en las cadenas globales (comercio por etapa)— en un retrato único por mineral. No es un modelo de panel ni una estimación causal: los índices (HHI, coeficiente de Ghosh, participación por etapa) se emplean como ",
 B("descriptores"),
 " para situar cada mineral en la escala que va de la exportación en bruto a la transformación de mayor valor, bajo la lente del enclave estructural."],first=True)
para(doc,["La exposición procede por pasos. Primero se definen las cuatro fases de la cadena de valor y los productos que las componen (VI.2). Luego se traza el perfil de cada mineral —productos por fase, concentración, encadenamiento, posición comercial y cadena local (VI.3)—. A continuación se añaden tres cortes transversales que dan profundidad a la caracterización: la evolución de la concentración extractiva (VI.4), la geografía de la extracción y la transformación (VI.5) y el destino de las exportaciones (VI.6). Después se agrupan los diez mercados en una tipología (VI.7) y se sintetizan las diez fichas de cadena de valor —cuantificación por eslabón y punto de ruptura— (VI.8), para derivar por último las bases de una política industrial (VI.9)."])

H1(doc,"VI.2  Las cuatro fases de la cadena de valor")
para(doc,["La cadena de valor de un mineral se organiza en cuatro fases de transformación creciente, en las que el valor por unidad física aumenta a cada paso:"],first=True)
add_table(doc,[1700,5238,1900],
 ["Fase","Qué comprende","Ejemplo (cobre)"],
 [["1 · Extracción","Mena y concentrado; producto de la actividad minera.","Concentrado de cobre (~28% Cu)"],
  ["2 · Transformación primaria","Metal refinado o mineral procesado/químico básico.","Cátodo de cobre (99.99%)"],
  ["3 · Semimanufactura","Productos intermedios semielaborados.","Alambrón, alambre, tubo"],
  ["4 · Manufactura","Bienes finales que incorporan el mineral.","Cable eléctrico, conexiones"]],fs=10)
caption(doc,"Cuadro VI.1. Las cuatro fases de la cadena de valor de un mineral (valor creciente de la 1 a la 4).")
para(doc,["El lugar donde un país deja de participar en esta secuencia define su posición: exportar en la fase 1 e importar en las fases 3–4 es el patrón del enclave estructural. Las secciones siguientes detallan, para cada mineral, qué productos concretos componen cada fase y hasta cuál llega México."])

H2(doc,"VI.2.1  De las fases a los eslabones (notación L0–L4)")
para(doc,["Para el análisis por cadena, cada mercado se descompone en cinco ",
 B("eslabones"),", denotados ",B("L0 a L4"),
 ", que precisan las cuatro fases anteriores añadiendo el recurso en el suelo. La notación de eslabones (L#) y la de etapas comerciales (E1–E4, empleada en el comercio por etapa) son ",
 B("equivalentes de L1 a L4"),
 "; se añade L0 para ubicar la dotación previa a toda actividad. La ",I("ele"),
 " de cada eslabón se lee, entonces, así:"],first=True)
add_table(doc,[3050,1550,4238],
 ["Eslabón","Equivale a","Qué comprende"],
 [["L0 · Recurso","—","Dotación geológica (reservas, yacimiento), previa a toda actividad."],
  ["L1 · Extracción y beneficio","Fase 1 / E1","Mina → mena y concentrado."],
  ["L2 · Fundición-refinación o química primaria","Fase 2 / E2","Concentrado → metal refinado o compuesto químico básico."],
  ["L3 · Semimanufactura","Fase 3 / E3","Metal → productos semielaborados."],
  ["L4 · Manufactura final y uso","Fase 4 / E4","Bien que incorpora el mineral; industria usuaria."]],fs=9)
caption(doc,"Cuadro VI.1bis. Los cinco eslabones de la cadena (notación L0–L4) y su equivalencia con las fases y las etapas comerciales E1–E4.")
para(doc,["El eslabón de la secuencia donde México deja de agregar valor —el ",
 B("punto de ruptura"),
 "— es el descriptor central de la posición de cada mineral. Sobre esta notación se construyen las diez fichas de cadena de valor, que cuantifican cada eslabón y localizan ese punto (VI.8), y de ella se deriva la tipología (VI.7)."])

H1(doc,"VI.3  Perfil de cada mercado")
for i,m in enumerate(ORDER,1):
    H2(doc,f"VI.3.{i}  {m}")
    add_table(doc,[2450,4938,1450],["Fase","Productos principales","Fracción HS"],
              [[f[0],f[1],f[2]] for f in PROD[m]],fs=9)
    caption(doc,f"Cuadro VI.{i+1}. Productos por fase de la cadena de valor — {m}.")
    c=CHAR[m]
    para(doc,[B("Estructura extractiva. "),c[0]," ",B("Encadenamiento hacia adelante (Ghosh): "),c[1],"."])
    para(doc,[B("Posición comercial. "),c[2]])
    para(doc,[B("Cadena local. "),c[3]])
    para(doc,[B("Lectura. "),c[4]])

H1(doc,"VI.4  Evolución de la concentración extractiva (HHI, 2004–2024)")
para(doc,["El índice de Herfindahl-Hirschman (HHI) de la producción por mineral, reconstruido para 2004-2024, muestra que la concentración no es estática. El nivel de ",
 B("2004-2020 es aproximado"),
 " (reconstruido por régimen de mercado a partir del líder y los grupos conocidos, con el residual tratado de forma atomística: es una cota inferior) y no es estrictamente comparable en nivel con ",
 B("2021-2024"),
 ", calculado por mina. Con esa cautela, se distinguen tres trayectorias:"],first=True)
add_table(doc,[1700,1150,1150,1150,3288],
 ["Mineral","2004","2012","2018","2021→2024 y lectura"],
 [["Fluorita","6,001","10,000","10,000","10,000 · monopolio de grupo consolidado tras la fusión de enero de 2012 (Koura/Orbia)."],
  ["Grafito","5,848","5,848","10,000","10,000 · productor único desde 2014."],
  ["Manganeso","10,000","10,000","10,000","10,000 · Autlán, productor único en toda la serie."],
  ["Cobre","—","(alta)","5,417","3,841→3,557 · alta pero decreciente; Grupo México sigue dominante."],
  ["Barita","3,069","10,000","6,400","6,779→605 · fuerte desconcentración reciente (nuevos entrantes; Baramin pierde el liderazgo)."],
  ["Plomo","—","858","—","1,448→2,465 · al alza (Peñasquito/Newmont)."],
  ["Zinc","—","566","—","1,591→1,683 · al alza."],
  ["Plata","—","562","1,109","926→1,147 · moderada (Fresnillo líder)."],
  ["Oro","2,043","676","—","771→429 · mercado fragmentado y cada vez más atomizado."]],fs=8)
caption(doc,"Cuadro VI.12. Índice HHI de la producción por mineral, años seleccionados 2004-2024. 2004-2020 aproximado (por régimen; cota inferior); 2021-2024 por mina. Fuente: base B5 (CAMIMEX + USGS), cálculo propio. Sílice sin dato 2024 (falta distribución).")
para(doc,["La lectura conjunta con el encadenamiento (V) es importante: la concentración extractiva y el grado de transformación doméstica ",
 B("no covarían"),
 " de forma simple. Minerales con HHI máximo (manganeso, fluorita, grafito) tienen encadenamientos hacia adelante altos, mientras que otros muy concentrados o poco concentrados se exportan en bruto. La estructura de mercado, por sí sola, no determina si la cadena se desarrolla: es un descriptor más, no la causa."])

H1(doc,"VI.5  Geografía de la extracción y la transformación")
para(doc,["La cadena de valor tiene una dimensión territorial que refuerza la lectura de enclave. La ",
 B("extracción está muy concentrada geográficamente"),
 " (producción 2024 por entidad, SGM): Zacatecas domina los metales (plata 50 %, plomo 71 %, zinc 56 %); Sonora, el cobre (70 %), el oro (32 %) y el grafito (100 %); San Luis Potosí, la fluorita (96 %); Hidalgo, el manganeso (100 %); Nuevo León y Sonora, la barita (97 %); Coahuila y Puebla, la sílice (91 %). Es una geografía extractiva de ",
 B("especialización regional aguda"),"."],first=True)
para(doc,["La ",B("transformación"),
 ", en cambio, se concentra en unos pocos nodos metalúrgicos —Torreón (Met-Mex Peñoles: plomo, zinc, plata, oro), La Caridad y Cananea (Grupo México: cobre), Molango-Tamós-Teziutlán (Autlán: ferromanganeso), Matamoros (Koura: HF)—, casi siempre bajo la misma firma que extrae (integración vertical). El resto del mineral sale del país en bruto. La distancia entre la geografía de la extracción y la escasez de nodos de transformación es la expresión espacial del enclave: el valor que no se agrega adentro se va con el concentrado."])

H1(doc,"VI.6  Destinos de las exportaciones: el desplazamiento hacia Asia")
para(doc,["El destino de las exportaciones en bruto se ha desplazado a lo largo de la serie 1992-2024, de Norteamérica y Europa (años noventa) a ",
 B("Asia, y en particular China"),
 ". El giro es nítido en los concentrados de la fase 1: el cobre en concentrado pasó de destinarse 100 % a Estados Unidos (1995) a 94 % a China (2022); los concentrados de plomo, zinc y oro se orientan a Corea y China. En contraste, los productos con algo de transformación mantienen su mercado tradicional: el ácido fluorhídrico (fase 2) va a Estados Unidos en toda la serie."])
para(doc,["El patrón describe una ",B("doble profundización del enclave"),
 ": no solo se exporta cada vez en una fase más cruda (más concentrado), sino que ese concentrado se dirige crecientemente a un solo comprador —China—, donde ocurre la transformación que no se hace en México. El destino se reporta como socio declarado de Comtrade (reexportación y entrepôt no depurados), un caveat que no altera la dirección del desplazamiento."])

H1(doc,"VI.7  Tipología comparativa de los diez mercados")
para(doc,["El Cuadro VI.15 reúne los tres indicadores construidos —concentración extractiva (HHI), encadenamiento hacia adelante (Ghosh, media = 1) y posición comercial (participación de la exportación en fase 1, mena/concentrado)— y el tipo resultante para cada mineral:"],first=True)
add_table(doc,[1900,1400,1500,1500,2538],
 ["Mineral","HHI","Ghosh adel.","X cruda","Tipo"],
 [["Manganeso","10,000","1.54","0%","A"],
  ["Fluorita","10,000","1.31","61%","A"],
  ["Cobre","≈3,650","1.34","68%","B"],
  ["Oro","≈500","1.22","4%","B"],
  ["Plata","≈890","1.18","3%","B"],
  ["Plomo","≈1,450","0.71","83%","B"],
  ["Zinc","≈1,450","0.71","55%","B"],
  ["Sílice","≈7,300","1.92","20%","C"],
  ["Grafito","10,000","1.71","1%","C"],
  ["Barita","6,779→1,380","0.64","100%","D"]],fs=9)
caption(doc,"Cuadro VI.15. Indicadores por mineral: concentración (HHI, 2021-2023), encadenamiento hacia adelante (Ghosh normalizado, MIP 2018) y exportación en bruto (Comtrade, prom. 2018-2023). Tipo según la tipología.")
para(doc,["Del cruce entre estructura extractiva y grado de transformación doméstica emergen cuatro tipos de mercado:"])
add_table(doc,[2500,2100,4238],
 ["Tipo","Minerales","Rasgo"],
 [["A · Cadena local desarrollada","Manganeso; Fluorita","Transformación doméstica de escala (Autlán→acero; Koura→HF); integración vertical del extractor."],
  ["B · Truncada en el metal refinado","Cobre; Oro; Plata; Plomo; Zinc","Los grupos integran hasta fundición/refinación y exportan el metal; poca manufactura aguas abajo."],
  ["C · Usuario doméstico con eslabón importado","Sílice; Grafito","Existe industria usuaria (vidrio, acero) pero el eslabón intermedio de mayor valor (silicio, electrodos) se importa."],
  ["D · Exportación en bruto","Barita","Sin eslabón manufacturero doméstico; uso interno marginal (perforación)."]],fs=9)
caption(doc,"Cuadro VI.16. Tipología de los mercados según su posición en la cadena de valor.")
para(doc,["La tipología muestra que el enclave estructural no es uniforme. En un extremo, ",I("manganeso"),
 " y ",I("fluorita")," exhiben cadenas locales verticalmente integradas de escala internacional (tipo A). En el grueso de los metales (tipo B), la transformación existe pero se detiene en el metal refinado, controlada por los mismos grupos extractivos. ",
 I("Sílice")," y ",I("grafito")," (tipo C) tienen industria usuaria doméstica, pero importan el eslabón intermedio de mayor valor. Y la ",
 I("barita")," (tipo D) se exporta esencialmente en bruto. Un hallazgo transversal, revelado por el análisis a nivel de empresa, es que buena parte de la cadena local ocurre ",
 B("dentro de las firmas extractivas"),
 " (integración vertical), lo que el dato sectorial subestima —el caso de la fluorita, cuyo eslabón de HF quedaba oculto, es ilustrativo—."])
add_map(doc, MAPA_CONJUNTO,
 "Figura VI.1. Visión de conjunto. Izquierda: estados extractores (número de minerales con ≥5% de participación) "
 "y hubs de transformación. Derecha: ejes comerciales del bloque —destino de exportación (rojo) y origen de "
 "importación (azul)—. Elaboración propia con SGM 2024 y UN Comtrade 2019-2024. Mapas por mineral en 13 Entregables/mapas.")

H1(doc,"VI.8  Las cadenas de valor locales: cuantificación por eslabón y punto de ruptura")
para(doc,["La caracterización anterior se formaliza en ",
 B("diez fichas de cadena de valor"),
 " (una por mineral), que aplican la notación de eslabones L0–L4 (VI.2.1): mapean cada eslabón, lo cuantifican —valor de producción y empleo desde la matriz insumo-producto; exportaciones e importaciones por etapa— y localizan el ",
 B("punto de ruptura"),
 ", el eslabón a partir del cual la cadena deja de agregar valor dentro del país. El Cuadro VI.17 resume, por mineral, ese punto y el tipo resultante."],first=True)
add_table(doc,[1700,900,1650,5288],
 ["Mineral","Tipo","Ruptura","Lectura"],
 [["Cobre","B","L2→L3","Refina, pero exporta concentrado (61→81 %) e importa semis."],
  ["Plomo","B","L1→L2","Exporta concentrado (86 %); refinación y baterías desacopladas del primario."],
  ["Zinc","B","L1→L2","Refina (IMMSA/Peñoles) pero exporta concentrado (64→80 %); semis importados."],
  ["Manganeso","A","L2→L3","Autlán exporta ferroaleación, no mena; falta la química fina de Mn."],
  ["Oro","B","L2→L4","Exporta metal refinado (doré); joyería importada."],
  ["Plata","B","L2→L4","1.º mundial; se cierra en el lingote, no en la manufactura."],
  ["Barita","D","L1→L2","Uso en bruto (perforación); sin química del bario."],
  ["Fluorita","A","L2→L3","HF de clase mundial (Koura), pero fluoropolímeros importados; enclave de exportación."],
  ["Grafito","C","L1→L2","Siderurgia usuaria fuerte, pero electrodos importados; mina decreciente."],
  ["Sílice","C","L1→L2","Vidrio y cemento locales; silicio de alto valor importado."]],fs=9)
caption(doc,"Cuadro VI.17. Punto de ruptura de la cadena y tipo por mineral (fichas de cadena de valor, Fases 1–7 de la ruta). Fuente: processed/cv_tipologia.csv y cv_eslabones_cuantificado.csv.")
para(doc,["Un ",B("hallazgo metodológico"),
 " refuerza la lectura de enclave. Al cuantificar los eslabones aguas abajo con la matriz insumo-producto (834 clases SCIAN), ",
 B("solo el cobre cuenta con clases estadísticas dedicadas a su transformación"),
 " (fundición y refinación de cobre, 331411; laminación, 331420). El oro y la plata comparten una única clase de metales preciosos (331412); el plomo, el zinc y los demás no ferrosos, otra (331419); el manganeso comparte su clase con la siderurgia (331112); y el ácido fluorhídrico de la fluorita se diluye en «químicos básicos inorgánicos» (325180). La propia ",
 B("invisibilidad estadística"),
 " de los eslabones de transformación —imposibles de aislar por mineral— es, en sí misma, un síntoma del enclave: donde no hay cadena diferenciada, tampoco hay categoría que la mida. Por eso, en las fichas, el valor de esos eslabones no se atribuye al mineral y se ancla con el comercio y la capacidad instalada."])
para(doc,["La cuantificación confirma, además, un rasgo territorial: ",
 B("solo el cobre está co-localizado"),
 " —fundición y refinería (La Caridad) junto a la mina en Nacozari—; en los nueve minerales restantes la transformación, cuando existe, está deslocalizada de la extracción (Torreón, San Luis Potosí, Matamoros), lo que agrava la desconexión aguas abajo. Las diez fichas completas obran en 05 Diagnóstico Insumo-Producto/Fichas de Cadena de Valor."])

H2(doc,"VI.8.1  Criticidad de los productos por eslabón")
para(doc,["La cadena de cada mineral no tiene una sola criticidad: la criticidad se concentra en ",
 B("productos y grados específicos"), " —los que las listas oficiales (USGS 2025; Unión Europea, CRMA 2023) señalan como estratégicos por su papel en la transición energética, la electrónica y la defensa (Cap. II)—. Situar esa criticidad sobre los eslabones L0–L4 muestra ",
 B("dónde la capta México y dónde se le escapa"), ": en varios minerales el eslabón estratégico coincide con el punto de ruptura de la cadena."],first=True)
add_table(doc,[1650,3050,2100,2038],
 ["Mineral","Producto de mayor criticidad (🔴 estratégico)","Sector","¿México lo produce?"],
 [["Cobre","Cátodo de cobre refinado","Electrificación, EV, red","Sí (exporta concentrado)"],
  ["Fluorita","HF → fluoropolímeros / LiPF₆","Baterías, semiconductores","HF sí; derivados no"],
  ["Grafito","Grafito grado batería / sintético","Ánodos de baterías, acero EAF","No (solo amorfo)"],
  ["Manganeso","Sulfato de Mn grado batería","Cátodos de baterías (NMC)","No (produce ferroaleación)"],
  ["Sílice","Silicio metálico","Semiconductores, fotovoltaica","No (produce arena)"],
  ["Plata","Plata refinada","Fotovoltaica, electrónica","Sí (exporta refinada)"],
  ["Oro","Oro refinado","Seguridad nacional, electrónica","Sí (exporta refinado)"],
  ["Plomo / Zinc","Refinado, baterías, galvanizado","Almacenamiento, acero","Parcial (semis importados)"],
  ["Barita","Químicos de bario","Química, pinturas","No (uso en bruto)"]],fs=8)
caption(doc,"Cuadro VI.18. Producto de mayor criticidad por mineral y su presencia en México. Base oficial: USGS (2022/2025), UE (CRMA 2023) e IEA; clasificación en processed/criticidad_productos.csv y en [[Clasificacion de productos por criticidad]].")
para(doc,["El patrón es revelador: en los tres minerales cuyo producto estratégico es de ",
 B("grado batería o electrónico"), " —grafito, sílice y manganeso—, ese producto ",
 B("no se fabrica en el país"), ", que exporta el crudo de baja criticidad e importa el eslabón crítico. La criticidad, así, ",
 B("se fuga junto con el valor"), ": el enclave estructural no solo deja fuera la transformación de mayor valor, sino precisamente la de mayor importancia estratégica. Solo en cobre, oro, plata y —parcialmente— fluorita México alcanza a producir el eslabón más crítico. Esta lectura alimenta las bases de política (VI.9) y la síntesis del Cap. VIII."])

H1(doc,"VI.9  Bases para una política industrial")
para(doc,["La caracterización sienta bases concretas y diferenciadas por tipo. En los mercados de tipo B (metales), el margen está en ",
 B("prolongar la cadena más allá del metal refinado"),
 " hacia semimanufacturas y manufactura, hoy parcialmente importadas. En los de tipo C (sílice, grafito), en ",
 B("sustituir el eslabón intermedio importado"),
 " —silicio/ferrosilicio, electrodos de grafito— por producción nacional que aproveche la extracción existente. En la fluorita (tipo A parcial), en ",
 B("escalar del HF a los fluoropolímeros"),
 " de mayor valor. Y en la barita (tipo D), la política realista pasa por condicionar el aprovechamiento del recurso a algún grado de agregación de valor. En todos los casos, la descripción —no un diagnóstico causal— es la que delimita dónde la cadena existe, dónde se trunca y dónde está ausente. La síntesis integral y las recomendaciones se desarrollan en el Cap. VIII."],first=True)

p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(10)
r=p.add_run("Fuentes: elaboración propia con base en HHI (base B5, CAMIMEX + USGS), coeficientes de Ghosh (MIP INEGI 2013/2018), comercio por etapa (UN Comtrade) y el mapa de empresas de transformación (USGS Tabla 2 + reportes corporativos). Bases e indicadores en 10 Datos/processed; memorias en 05 Diagnóstico Insumo-Producto y 10 Datos.")
r.font.italic=True; r.font.size=Pt(9)

out=sys.argv[1]; doc.save(out); print("Guardado:",out)
