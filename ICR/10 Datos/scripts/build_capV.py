# -*- coding: utf-8 -*-
"""Capitulo V - Diagnostico de encadenamientos productivos. Word con python-docx + OMML."""
import sys
from lxml import etree
from docx import Document
from docx.shared import Pt, RGBColor, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
XML = "http://www.w3.org/XML/1998/namespace"

# ---------------- OMML builders ----------------
def _E(tag):
    return etree.Element("{%s}%s" % (M, tag), nsmap={"m": M})
def _val(tag, v):
    e = _E(tag); e.set("{%s}val" % M, v); return e
def mrun(text):
    r = _E("r"); tt = _E("t"); tt.text = text
    tt.set("{%s}space" % XML, "preserve"); r.append(tt); return r
def _el(x):
    return mrun(x) if isinstance(x, str) else x
def _wrap(tag, kids):
    e = _E(tag)
    if not isinstance(kids, (list, tuple)): kids = [kids]
    for k in kids: e.append(_el(k))
    return e
def ssub(base, s):
    return _wrap("sSub", []) if False else (lambda e: (e.append(_wrap("e", base)), e.append(_wrap("sub", s)), e)[-1])(_E("sSub"))
def ssup(base, s):
    e = _E("sSup"); e.append(_wrap("e", base)); e.append(_wrap("sup", s)); return e
def frac(num, den):
    e = _E("f"); e.append(_wrap("num", num)); e.append(_wrap("den", den)); return e
def nary(subtext, body):
    pr = _E("naryPr")
    for x in (_val("chr", "∑"), _val("limLoc", "undOvr"), _val("supHide", "1"), _val("grow", "1")):
        pr.append(x)
    e = _E("nary"); e.append(pr)
    e.append(_wrap("sub", subtext)); e.append(_E("sup")); e.append(_wrap("e", body))
    return e

def add_equation(doc, kids):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6); p.paragraph_format.space_after = Pt(6)
    opara = _E("oMathPara")
    opp = _E("oMathParaPr"); opp.append(_val("jc", "center")); opara.append(opp)
    om = _E("oMath")
    for k in kids: om.append(_el(k))
    opara.append(om)
    p._p.append(opara)
    return p

# ---------------- text helpers ----------------
def para(doc, runs, justify=True, first=False, after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.space_after = Pt(after); pf.line_spacing = 1.15
    if first: pf.first_line_indent = Pt(21)
    for r in runs:
        if isinstance(r, str):
            p.add_run(r)
        else:
            txt, opt = r
            run = p.add_run(txt)
            run.font.italic = opt.get("i", False)
            run.font.bold = opt.get("b", False)
            if opt.get("sub"): run.font.subscript = True
            if opt.get("sup"): run.font.superscript = True
    return p

def heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12); p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text); r.font.bold = True; r.font.size = Pt(13); r.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    return p

def title(doc):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
    r = p.add_run("Capítulo V"); r.font.bold = True; r.font.size = Pt(16)
    p2 = doc.add_paragraph(); p2.paragraph_format.space_after = Pt(12)
    r2 = p2.add_run("Diagnóstico de encadenamientos productivos de los minerales críticos")
    r2.font.bold = True; r2.font.size = Pt(14)

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    tcPr.append(shd)

def set_widths(table, widths):
    table.autofit = False
    for row in table.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Twips(w)

def add_table(doc, widths, headers, rows):
    tbl = doc.add_table(rows=1, cols=len(headers)); tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(h); run.font.bold = True; run.font.size = Pt(10)
        hdr[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT if i == 0 else WD_ALIGN_PARAGRAPH.CENTER
        shade(hdr[i], "E8E8E8")
    for r in rows:
        cells = tbl.add_row().cells
        for i, v in enumerate(r):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(str(v)); run.font.size = Pt(10)
            cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT if i == 0 else WD_ALIGN_PARAGRAPH.CENTER
    set_widths(tbl, widths)
    return tbl

def caption(doc, text):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text); r.font.italic = True; r.font.size = Pt(9)

def refpara(doc, text):
    p = doc.add_paragraph(); pf = p.paragraph_format
    pf.space_after = Pt(3); pf.left_indent = Pt(21); pf.first_line_indent = Pt(-21); pf.line_spacing = 1.0
    r = p.add_run(text); r.font.size = Pt(10)

# ================================================================
doc = Document()
# estilo por defecto
normal = doc.styles["Normal"]; normal.font.name = "Times New Roman"; normal.font.size = Pt(12)
# pagina Carta + margenes 3 cm
sec = doc.sections[0]
sec.page_width = Twips(12240); sec.page_height = Twips(15840)
sec.top_margin = Twips(1701); sec.bottom_margin = Twips(1701)
sec.left_margin = Twips(1701); sec.right_margin = Twips(1701)

I = lambda s: (s, {"i": True})
B = lambda s: (s, {"b": True})
SUB = lambda s: (s, {"sub": True, "i": True})
SUP = lambda s: (s, {"sup": True})
IB = lambda s: (s, {"i": True, "b": True})

title(doc)

heading(doc, "V.1  Propósito y enfoque")
para(doc, ["Este capítulo caracteriza la posición de cada uno de los diez minerales críticos dentro de la estructura productiva nacional a partir de la Matriz de Insumo-Producto (MIP) del INEGI. El análisis es ", I("descriptivo"),
  ": los coeficientes y los índices que se construyen —Leontief, Ghosh e Hirschman-Rasmussen— se emplean como ", I("descriptores"),
  " del grado y la dirección de los encadenamientos de cada mineral, no como parámetros de un modelo causal. El aporte reside en construir estos indicadores desagregados por mineral, que no estaban disponibles, y en usarlos para describir dónde se articula —y dónde se trunca— la cadena de valor de cada recurso dentro del país."], first=True)
para(doc, ["La exposición procede en tres planos. Primero se define la contabilidad insumo-producto y se derivan formalmente los dos modelos duales: el de demanda (Leontief), que mide los encadenamientos ", I("hacia atrás"),
  ", y el de oferta (Ghosh), que mide los encadenamientos ", I("hacia adelante"),
  ". Segundo, se normalizan ambos mediante los índices de Hirschman-Rasmussen para hacerlos comparables entre ramas. Tercero, se aplican a los minerales del corpus y se interpretan a la luz de la demanda intermedia doméstica: qué sectores compran cada mineral dentro de México."], first=True)

para(doc, ["Un apunte de notación, común a los capítulos VI y VIII: la cadena de valor de cada mineral se describe por ",
  B("eslabones"), ", denotados ", B("L0 a L4"),
  " —L0 (recurso), L1 (extracción y beneficio), L2 (fundición-refinación o química primaria), L3 (semimanufactura) y L4 (manufactura final y uso)—. Los eslabones L1 a L4 coinciden con las cuatro fases de transformación y con las etapas comerciales E1–E4 del comercio por etapa; L0 se añade para ubicar la dotación. El encadenamiento hacia adelante que aquí se mide describe, en esos términos, hasta qué eslabón se prolonga la cadena dentro del país (la notación se desarrolla en VI.2.1)."], first=True)

heading(doc, "V.2  La matriz de insumo-producto: notación e identidad contable")
para(doc, ["La MIP registra, para una economía de ", I("n"), " sectores, el valor de las transacciones intermedias entre ellos en un año. Sea ",
  I("z"), SUB("ij"), " el flujo del sector ", I("i"), " (que vende) al sector ", I("j"), " (que compra) como insumo intermedio; ",
  I("x"), SUB("i"), " el valor bruto de la producción del sector ", I("i"), "; y ", I("f"), SUB("i"),
  " su demanda final (consumo, inversión, exportaciones). La identidad contable por filas establece que toda la producción de un sector se destina a usos intermedios o finales:"], first=True)
add_equation(doc, [ssub("x", "i"), " = ", nary("j", ssub("z", "ij")), " + ", ssub("f", "i")])
para(doc, ["De manera simétrica, leída por columnas, la producción de cada sector se descompone en el valor de sus insumos intermedios y el valor agregado (remuneraciones, impuestos netos y excedente de operación). Sobre esta doble lectura se levantan, respectivamente, el modelo de oferta y el modelo de demanda."])

heading(doc, "V.3  Encadenamientos hacia atrás: el modelo de demanda (Leontief)")
para(doc, ["El modelo de Leontief (1941) supone que cada sector emplea insumos en proporciones técnicas fijas. Se define el ", B("coeficiente técnico"),
  " ", I("a"), SUB("ij"), " como el valor del insumo del sector ", I("i"), " requerido por unidad de producción del sector ", I("j"), ":"], first=True)
add_equation(doc, [ssub("a", "ij"), " = ", frac(ssub("z", "ij"), ssub("x", "j"))])
para(doc, ["Reuniendo los coeficientes en la matriz ", I("A"), ", la identidad contable se reescribe en forma matricial como ",
  I("x"), " = ", I("A"), I("x"), " + ", I("f"), ". Despejando el vector de producción se obtiene la solución fundamental del modelo:"])
add_equation(doc, ["x = ", ssup(mrun("(I − A)"), "−1"), " f = L f"])
para(doc, ["La matriz ", I("L"), " = (", I("I"), " − ", I("A"), ")", SUP("−1"), ", ", B("inversa de Leontief"),
  " o matriz de requerimientos totales, tiene elementos ", I("l"), SUB("ij"),
  " que miden la producción total del sector ", I("i"), " —directa e indirecta— necesaria para satisfacer una unidad de demanda final del sector ", I("j"),
  ". El ", B("encadenamiento hacia atrás"), " del sector ", I("j"), " es la suma de su columna en ", I("L"), ":"])
add_equation(doc, [ssub(mrun("BL"), "j"), " = ", nary("i", ssub("l", "ij"))])
para(doc, ["Un encadenamiento hacia atrás elevado indica que el sector tracciona a muchos proveedores. En la minería suele ser bajo, porque la extracción es intensiva en el recurso natural y demanda pocos insumos industriales."])

heading(doc, "V.4  Encadenamientos hacia adelante: el modelo de oferta (Ghosh)")
para(doc, ["El modelo de Ghosh (1958) es el dual del anterior: en lugar de preguntar de dónde provienen los insumos, describe hacia dónde se distribuye la producción. Se define el ", B("coeficiente de distribución"),
  " ", I("b"), SUB("ij"), " como la proporción de la producción del sector ", I("i"), " que se vende al sector ", I("j"), " como insumo intermedio:"], first=True)
add_equation(doc, [ssub("b", "ij"), " = ", frac(ssub("z", "ij"), ssub("x", "i"))])
para(doc, ["Con la matriz ", I("B"), " y el vector de valor agregado ", I("v"), ", la lectura por columnas conduce a ",
  I("x"), "′ = ", I("v"), "′ + ", I("x"), "′", I("B"), ", cuya solución es:"])
add_equation(doc, ["x′ = v′ ", ssup(mrun("(I − B)"), "−1"), " = v′ G"])
para(doc, ["La ", B("inversa de Ghosh"), " ", I("G"), " = (", I("I"), " − ", I("B"), ")", SUP("−1"),
  " tiene elementos ", I("g"), SUB("ij"), " que miden el valor de producción del sector ", I("j"),
  " inducido, directa e indirectamente, por una unidad de valor agregado del sector ", I("i"),
  ". El ", B("encadenamiento hacia adelante"), " del sector ", I("i"), " es la suma de su fila en ", I("G"), ":"])
add_equation(doc, [ssub(mrun("FL"), "i"), " = ", nary("j", ssub("g", "ij"))])
para(doc, ["Para un mineral, un encadenamiento hacia adelante elevado significa que su producción alimenta a una industria transformadora doméstica amplia; uno bajo indica que se destina a la demanda final —típicamente la exportación en bruto— sin apenas procesamiento interno. Es el indicador central de este trabajo, pues describe si existe cadena de valor local aguas abajo del recurso."])

heading(doc, "V.5  Índices de Hirschman-Rasmussen")
para(doc, ["Las sumas anteriores dependen de las unidades y de la estructura de cada matriz, por lo que no son comparables sin normalizar. Rasmussen (1956), sobre la idea de eslabonamientos de Hirschman (1958), divide cada suma sectorial entre el promedio de todas las sumas de la economía. El ", B("poder de dispersión"),
  " (encadenamiento hacia atrás normalizado) del sector ", I("j"), " es:"], first=True)
add_equation(doc, [ssub("U", "j"), " = ", frac(["n ", nary("i", ssub("l", "ij"))], nary("i,j", ssub("l", "ij")))])
para(doc, ["y la ", B("sensibilidad de dispersión"), " (encadenamiento hacia adelante normalizado) del sector ", I("i"), " es:"])
add_equation(doc, [ssub("U", "i"), " = ", frac(["n ", nary("j", ssub("g", "ij"))], nary("i,j", ssub("g", "ij")))])
para(doc, ["Estas expresiones equivalen a la definición clásica como cociente entre el promedio de la columna (o fila) y el promedio general de la matriz. Su lectura es directa: un valor ", B("mayor que 1"),
  " indica que el encadenamiento supera el promedio de la economía, y uno ", B("menor que 1"), " que se sitúa por debajo. La media de cada índice sobre todos los sectores es, por construcción, igual a la unidad, lo que hace comparables las posiciones relativas entre minerales y entre los dos cortes."])

heading(doc, "V.6  Fuente de datos y operacionalización")
para(doc, ["Se emplean las matrices simétricas producto por producto de la MIP del INEGI para ", B("2013"), " (año base 2013) y ", B("2018"),
  " (año base 2018), en su máximo nivel de desagregación: la ", B("clase de actividad SCIAN a seis dígitos"),
  " (822 clases en 2013 y 834 en 2018). Los cortes 2003, 2008 y 2012 se descartan por no estar disponibles en datos abiertos y por corresponder a años base y clasificaciones anteriores, no comparables."], first=True)
para(doc, ["Los coeficientes se calculan sobre la matriz de ", B("origen doméstico"),
  ", de modo que los encadenamientos reflejan la articulación con la producción nacional. A ese nivel, ocho de los diez minerales tienen clase propia; ", B("plomo y zinc comparten una sola clase"),
  " (212232), lo que corresponde a su coextracción geológica, por lo que sus encadenamientos se reportan de forma conjunta. La correspondencia es la siguiente:"])
add_table(doc, [2200, 2219, 2200, 2219], ["Mineral", "Clase SCIAN", "Mineral", "Clase SCIAN"],
  [["Oro", "212221", "Barita", "212393"], ["Plata", "212222", "Fluorita", "212395"],
   ["Cobre", "212231", "Grafito", "212396"], ["Plomo-zinc", "212232", "Sílice", "212324"],
   ["Manganeso", "212291", "—", "—"]])
caption(doc, "Cuadro V.1. Correspondencia entre los minerales del corpus y las clases SCIAN de la MIP.")
para(doc, ["El cálculo se programó de forma reproducible y se ", B("validó contra los tabulados del propio INEGI"),
  ": la matriz de coeficientes técnicos ", I("A"), " reproduce el archivo publicado y la inversa de Leontief ", I("L"),
  " reproduce el archivo de coeficientes directos e indirectos, con diferencias del orden de 10", SUP("−15"),
  " (precisión de máquina). La inversa de Ghosh se construye a partir de la misma matriz de flujos ya validada."])

heading(doc, "V.7  Resultados: encadenamientos por mineral")
para(doc, ["El Cuadro V.2 presenta, para cada mineral, el valor bruto de producción (VBP, en millones de pesos), la fracción destinada a demanda intermedia doméstica (DI/VBP) y los índices normalizados de encadenamiento hacia atrás (",
  I("U"), SUB("j"), ") y hacia adelante (", I("U"), SUB("i"), "). Un índice superior a la unidad señala un encadenamiento por encima del promedio de la economía."], first=True)
W = [1780, 1360, 1360, 1440, 1440]
head5 = ["Mineral", "VBP (MM$)", "DI/VBP", "Atrás (Uj)", "Adelante (Ui)"]
add_table(doc, W, head5, [
  ["Sílice", "6 959", "0.99", "0.94", "1.92"], ["Grafito", "720", "0.88", "0.87", "1.71"],
  ["Manganeso", "635", "0.78", "1.05", "1.54"], ["Cobre", "92 893", "0.53", "0.94", "1.34"],
  ["Fluorita", "5 862", "0.50", "0.97", "1.31"], ["Oro", "69 491", "0.96", "1.03", "1.22"],
  ["Plata", "49 784", "0.89", "0.99", "1.18"], ["Plomo-zinc", "34 725", "0.14", "0.99", "0.71"],
  ["Barita", "686", "0.03", "0.96", "0.64"]])
caption(doc, "Cuadro V.2. Encadenamientos productivos de los minerales críticos, 2018 (base doméstica, clase SCIAN). Ordenado por encadenamiento hacia adelante.")
add_table(doc, W, head5, [
  ["Manganeso", "486", "0.72", "0.83", "1.79"], ["Sílice", "4 898", "0.99", "0.91", "1.80"],
  ["Oro", "49 607", "1.00", "0.92", "1.35"], ["Plata", "44 680", "0.96", "0.91", "1.30"],
  ["Grafito", "164", "0.59", "0.84", "1.24"], ["Cobre", "39 971", "0.46", "0.89", "1.18"],
  ["Fluorita", "2 218", "0.22", "0.85", "0.87"], ["Barita", "368", "0.18", "0.96", "0.76"],
  ["Plomo-zinc", "20 046", "0.12", "0.89", "0.72"]])
caption(doc, "Cuadro V.3. Encadenamientos productivos de los minerales críticos, 2013 (base doméstica, clase SCIAN). Ordenado por encadenamiento hacia adelante.")
para(doc, ["Dos regularidades destacan. En el ", I("eslabonamiento hacia atrás"),
  ", todos los minerales se sitúan cerca o por debajo del promedio (índices en torno a 0.8–1.05): la extracción demanda pocos insumos industriales y arrastra poco a sus proveedores. En el ", I("eslabonamiento hacia adelante"),
  ", la dispersión es amplia. En un extremo, sílice y manganeso —y de forma creciente el grafito— superan ampliamente la unidad, señal de que alimentan una industria transformadora doméstica. En el otro, barita y plomo-zinc quedan por debajo del promedio, con una fracción mínima de su producción destinada a demanda intermedia interna: se exportan en bruto."])

heading(doc, "V.8  Interpretación: la demanda intermedia doméstica de cada mineral")
para(doc, ["El índice hacia adelante gana sentido al identificar ", I("qué sectores"),
  " compran cada mineral dentro del país. El Cuadro V.4 resume los principales compradores domésticos en 2018, a partir de la fila de cada mineral en la matriz de flujos."], first=True)
add_table(doc, [1900, 6938], ["Mineral", "Principales compradores domésticos (2018)"], [
  ["Oro", "Fundición y refinación de metales preciosos (99.5%)."],
  ["Plata", "Fundición y refinación de metales preciosos (99.0%)."],
  ["Cobre", "Fundición y refinación de cobre (93.5%)."],
  ["Plomo-zinc", "Fundición y refinación de otros metales no ferrosos (79.5%); acumuladores y pilas (5.2%)."],
  ["Grafito", "Ferroaleaciones (43.0%); complejos siderúrgicos (32.4%); moldeo de hierro y acero (13.6%)."],
  ["Sílice", "Envases de vidrio (43.4%); cemento (38.6%); azulejos y losetas (3.1%)."],
  ["Manganeso", "Farmacéutica (23.0%); alimentos para animales (22.2%); ladrillos (21.4%); química inorgánica (8.6%)."],
  ["Fluorita", "Cemento (82.3%); otros productos minerales no metálicos (12.6%)."],
  ["Barita", "Perforación de pozos petroleros (58.3%); partes de frenos (15.2%); extracción de petróleo y gas (14.5%)."]])
caption(doc, "Cuadro V.4. Destino intermedio doméstico de cada mineral (participación en su demanda intermedia). Fuente: MIP INEGI 2018, cálculo propio.")
para(doc, ["La lectura por mineral matiza el significado de los índices y revela dónde se interrumpe la cadena de valor:"], first=True)
para(doc, [B("Metales preciosos y cobre. "), "Oro, plata y cobre destinan casi la totalidad de su demanda intermedia a un único eslabón: la fundición y refinación. La cadena doméstica llega hasta el metal refinado y, salvo en plomo-zinc —con un vínculo menor con la fabricación de acumuladores—, no continúa hacia la manufactura. Un valor alto de DI/VBP indica aquí procesamiento metalúrgico interno, no una cadena larga: conviene no confundir ambos."])
para(doc, [B("Fluorita. "), "En la matriz insumo-producto, el 82% de su demanda intermedia va a la industria del cemento (grado metalúrgico). Esa cifra, sin embargo, subestima la cadena fluoroquímica, que a nivel de empresa sí existe: Koura (Orbia) opera en Matamoros la mayor planta de ácido fluorhídrico (HF) del mundo, integrada con la mina Las Cuevas, por lo que la transferencia mina→HF es intra-firma y no se observa en el flujo sectorial. El comercio lo confirma: México exportó cerca de 161 millones de dólares de HF en 2018. La cadena local llega, pues, hasta el HF, pero se detiene antes de los fluoropolímeros de mayor valor (PTFE), que se importan. El caso ilustra por qué el análisis a nivel de empresa (Objetivo 2) corrige la lectura del dato agregado."])
para(doc, [B("Grafito. "), "Se dirige a la siderurgia y la fundición —ferroaleaciones, complejos siderúrgicos, moldeo de hierro y acero—, un eslabonamiento industrial genuino (refractarios, electrodos, recarburación) que explica su índice hacia adelante creciente entre 2013 y 2018."])
para(doc, [B("Sílice. "), "Alimenta la industria del vidrio (envases) y la construcción (cemento, azulejos), la cadena doméstica más amplia del corpus, lo que sostiene el mayor índice hacia adelante."])
para(doc, [B("Manganeso. "), "Presenta el destino más disperso —farmacéutica, alimentos para animales, cerámica, química, fertilizantes, pilas—, lo que se traduce en una elevada sensibilidad de dispersión pese a su reducido tamaño."])
para(doc, [B("Barita. "), "Su uso intermedio se concentra en la perforación de pozos petroleros (agente densificante de lodos), no en una cadena manufacturera; y apenas alrededor del 3% de su producción se transforma en el país en 2018, frente al 18% en 2013: el grueso se exporta en bruto."])

heading(doc, "V.9  Síntesis descriptiva")
para(doc, ["El diagnóstico describe un patrón común y una diferenciación relevante. El patrón: los minerales críticos mexicanos arrastran poco a sus proveedores (encadenamiento hacia atrás bajo), rasgo de una actividad extractiva intensiva en recursos. La diferenciación está aguas abajo. Un primer grupo —sílice, grafito, manganeso— alimenta cadenas industriales domésticas (vidrio, acero, química) y muestra encadenamientos hacia adelante muy por encima del promedio. Un segundo grupo —oro, plata, cobre— sostiene un eslabón metalúrgico interno robusto (fundición y refinación) pero sin continuidad manufacturera. Un tercer grupo —barita y plomo-zinc— se exporta esencialmente en bruto. La fluorita ocupa una posición intermedia: tiene industria compradora, pero de bajo valor. Este mapa de eslabonamientos —dónde la cadena existe, dónde se detiene en el refinado y dónde está ausente— es la base descriptiva sobre la que los capítulos siguientes discuten la inserción internacional y las opciones de política industrial."], first=True)

heading(doc, "V.10  El índice de Ghosh: por qué un valor mayor que 1 debe leerse con cautela")
para(doc, ["Resulta tentador leer un índice de Ghosh mayor que 1 como evidencia de que un mineral tiene una cadena de valor local desarrollada. ",
  B("No lo es"), ", y la distinción es central para el diseño descriptivo de esta investigación. El índice mide cuánto se conecta la producción del sector con los sectores situados aguas abajo en la estructura insumo-producto doméstica, en relación con el promedio de la economía: es un ",
  I("potencial"), " de arrastre estructural observado en el año de la matriz, no una medida de desarrollo de cadena ni de captura de valor. Cinco razones lo justifican."], first=True)
para(doc, [B("Primera: refleja la amplitud de las industrias usuarias, no el valor que México retiene. "),
  "La sílice tiene el índice hacia adelante más alto (1.92 en 2018) porque el vidrio, el cemento, la cerámica y la construcción usan arena sílica ampliamente; eso indica que la economía doméstica ",
  I("consume"), " sílice en muchos sectores, no que el país capture valor —de hecho el insumo procesado de mayor valor, el silicio metálico, se importa—."])
para(doc, [B("Segunda: un índice alto puede ser un solo eslabón, no una cadena. "),
  "El oro (1.22) y la plata (1.18) superan la unidad porque casi toda su producción va a un único destino —fundición y refinación de metales preciosos (≈99 %)— y de ahí se exporta. El encadenamiento estructural alto convive con una cadena ",
  I("truncada"), " en el metal refinado."])
para(doc, [B("Tercera: no distingue el insumo de origen nacional del importado. "),
  "El grafito (1.71) y la sílice alimentan una industria usuaria nacional (siderurgia, vidrio) que, sin embargo, corre con insumo procesado importado (electrodos de grafito, silicio); el índice de la matriz doméstica no captura esa fuga."])
para(doc, [B("Cuarta: es sensible a la clasificación y al año base. "),
  "El manganeso pasa de 1.00 en el corte de referencia 2008 a 1.79 en 2013, en parte porque en 2008 su clase agrupa actividades vecinas más amplias (véase V.12). El nivel del índice depende de cómo se define la clase y de la añada de la matriz, no solo del desarrollo real de la cadena."])
para(doc, [B("Quinta: descansa en supuestos del modelo. "),
  "El modelo de Ghosh supone coeficientes de distribución fijos; su interpretación más defendible es como modelo de precios (Dietzenbacher, 1997). Aquí se emplea como descriptor de posición estructural, no como mecanismo causal."])
para(doc, ["En consecuencia, el índice de Ghosh es una condición ", B("necesaria pero no suficiente"),
  " para hablar de cadena local: señala dónde existen conexiones aguas abajo, pero no si México capta valor ni si la cadena se detiene pronto. Por eso en esta investigación ",
  B("nunca se lee solo"), ": se cruza con el coeficiente de captura de valor (V.11), el comercio por etapa y el mapa de empresas de transformación. El enclave estructural aparece en la ",
  I("combinación"), " de los indicadores, no en el Ghosh aislado; de hecho, la co-ocurrencia esperada entre alta concentración y bajo encadenamiento hacia adelante no se observa —varios minerales muy concentrados (manganeso, fluorita, grafito, sílice) tienen índices de Ghosh altos—, lo que confirma que el índice mide arrastre estructural, no truncamiento de la cadena."])

heading(doc, "V.10.1  El encadenamiento por eslabón: extracción, refinación y semimanufactura")
para(doc, ["La cautela anterior se vuelve visible al calcular el índice de Ghosh no solo para el eslabón ",
  B("extractivo"), ", sino también para la ", B("refinación"), " y la ", B("semimanufactura"),
  " de cada mineral (clases SCIAN 331 aguas abajo). Si el arrastre hacia adelante fuera prueba de cadena desarrollada, debería sostenerse o crecer al descender por la cadena; lo que se observa es lo contrario: ",
  B("el arrastre se debilita o se corta"), " en cada paso (Cuadro V.4bis; corte 2018)."], first=True)
add_table(doc, [1560, 1140, 1140, 1140, 2660],
  ["Mineral", "L1 extrac.", "L2 refin.", "L3 semis", "Clases L2 / L3 (atribuibilidad)"],
  [["Cobre", "1.34", "1.37", "0.95", "331411 / 331420 (atribuible)"],
   ["Oro", "1.22", "0.62", "1.02", "331412 / 331490 (compartida Au+Ag)"],
   ["Plata", "1.18", "0.62", "1.02", "331412 / 331490 (compartida)"],
   ["Plomo-zinc", "0.71", "0.63", "1.02", "331419 / 331490 (compartida)"],
   ["Manganeso", "1.54", "1.34", "—", "331112 ferroaleaciones (comp. con acero)"],
   ["Fluorita", "1.31", "1.44*", "1.31", "325180 / 325211 (agregado)"],
   ["Grafito", "1.71", "1.44*", "1.24", "325180 / 327999 (agregado)"],
   ["Sílice", "1.92", "1.44*", "1.34", "325180 / 327211 (agregado)"],
   ["Barita", "0.64", "1.44*", "—", "325180 (agregado)"]])
caption(doc, "Cuadro V.4bis. Índice de Ghosh hacia adelante (Rasmussen, media=1) por eslabón, corte 2018. "
  "* clase agregada de químicos, no atribuible al mineral. Cortes 2008 y 2013 en processed/mip_encadenamientos_eslabones.csv "
  "(script mip_eslabones.py).")
para(doc, ["El caso del ", B("cobre"), " es ilustrativo: la refinación (1.37) supera incluso a la extracción, porque la fundición sí alimenta industria doméstica; pero la ",
  B("semimanufactura cae a 0.95"), ", justo donde se agregaría más valor. En los ", B("metales preciosos"),
  " el corte es más agudo: la refinación (331412) tiene un Ghosh de ", B("0.62"),
  ", de los más bajos de la economía, porque el metal refinado no alimenta industria nacional sino que se exporta como lingote —el enclave estructural aparece en el propio índice, sin necesidad de otro indicador—. Sólo el ",
  I("manganeso"), " sostiene el arrastre hasta la ferroaleación (1.34), coherente con su cadena local (Autlán). En los no metálicos, el eslabón aguas abajo cae en una clase agregada de químicos (325180), no separable por mineral. El mismo ejercicio a nivel ",
  B("estatal e internacional"), " se recoge en el Cap. VII y en la memoria de encadenamientos por eslabón."])

heading(doc, "V.11  El coeficiente de captura de valor (CCV): una serie continua del encadenamiento hacia adelante")
para(doc, ["El índice de Ghosh es discreto: está atado a los dos cortes de la MIP (2013 y 2018). Para darle profundidad temporal al encadenamiento hacia adelante se construye un segundo descriptor, el ",
  B("coeficiente de captura de valor (CCV)"),
  ", como serie anual mineral-año 1992-2025. Para cada mineral y año, el CCV es el cociente entre el valor unitario de exportación del mineral en su forma bruta (mena o concentrado, etapa 1) y el precio del producto de referencia refinado del USGS:"], first=True)
add_equation(doc, [ssub(mrun("CCV"), "m,t"), " = ", frac(ssub(ssup(mrun("VU"), "X,E1"), "m,t"), ssub(ssup(mrun("P"), "USGS"), "m,t"))])
para(doc, ["Un CCV cercano a 1 indica que la forma exportada en bruto ya vale casi como el producto de referencia; un CCV cercano a 0, que la exportación bruta capta poco de ese valor —mayor distancia al eslabón procesado—. Un CCV ",
  B("bajo y persistente"), " es el descriptor de serie del enclave estructural. El numerador procede de UN Comtrade (fracciones de exportación E1 de México, con valor y peso); el denominador, de los precios del USGS empalmados. Los huecos de la serie se completaron con ",
  B("datos espejo"), " (lo que los socios reportan importar desde México, que sí traen peso), marcados como tales; el resto se declara y no se imputa."])
add_table(doc, [1780, 1360, 1360, 3140],
  ["Mineral", "CCV medio", "Rango", "Lectura"],
  [["Cobre", "0.22", "0.13–0.36", "Estable ~0.20–0.30 en tres décadas: el concentrado capta ~22 % del cobre refinado en frontera. Descriptor de enclave."],
   ["Zinc", "0.30", "0.18–0.44", "Estable ~0.30: concentrado de zinc frente a zinc refinado."],
   ["Plomo", "1.05", "0.07–2.69", "Volátil y a veces >1: los créditos de plata/oro del concentrado argentífero inflan el valor/t; no se lee como captura pura."],
   ["Fluorita", "0.85", "0.47–1.70", "≈1: espato flúor exportado frente a la referencia; prima/descuento de frontera."],
   ["Barita", "1.59", "0.66–4.40", "≈1 o >1: la barita de perforación supera el valor de consumo aparente de referencia."],
   ["Grafito", "0.47", "0.22–2.88", "Ruidoso: grafito natural frente a referencia flake importada."],
   ["Sílice", "1.98", "0.16–14.4", "Muy ruidoso: mezcla de grados; descriptor sólo relativo."],
   ["Manganeso", "0.22", "0.11–0.52", "Mena de manganeso frente a referencia; el grueso se transforma en el país."],
   ["Oro / Plata", "≈0", "—", "No informativo: artefacto de ley (mena en bruto ÷ metal puro). Su encadenamiento se describe por el comercio por etapa (doré/joyería), no por el CCV."]])
caption(doc, "Cuadro V.5. Coeficiente de captura de valor por mineral, 1992-2025 (media y rango de los años con dato). Fuente: cálculo propio con UN Comtrade y precios USGS empalmados; base ccv_serie.csv.")
para(doc, ["El poder descriptivo del CCV depende del grupo mineral. En los ", B("metales base (cobre y zinc)"),
  " funciona como se pretende: el concentrado y el metal refinado son productos distintos y la brecha estable (≈0.22–0.30) mide captura no realizada —es el hallazgo fuerte, coherente con el enclave: se exporta concentrado, no cátodo—. En el ",
  B("plomo"), " el concentrado argentífero contamina el cociente con créditos de plata. En ", B("oro y plata"),
  " el CCV no es informativo (artefacto de ley) y el encadenamiento se describe con el comercio por etapa. En los ", B("no metálicos"),
  " la referencia es un producto cercano a la forma exportada, así que el CCV oscila alrededor de 1 y capta primas o descuentos de grado más que un salto de eslabón. Un caveat adicional: los años completados por espejo son valores ",
  B("CIF"), " (incluyen flete y seguro) y pueden sobrestimar el valor unitario frente al FOB propio; se leen con esa reserva. El único hueco no completable —plomo 1994, sin comercio espejo— se declara, no se imputa. Así, el CCV ",
  I("complementa"), " al Ghosh sin sustituirlo: aporta la dimensión temporal continua que los dos cortes de la MIP no dan."])

heading(doc, "V.12  Profundidad temporal: el corte de referencia 2008")
para(doc, ["A los dos cortes comparables (2013 y 2018) se añade un tercer punto, la MIP de ", B("2008"),
  " (base 2008, clasificación SCIAN 2007), como ", B("referencia histórica no encadenada"),
  ". No forma serie comparable —los movimientos 2008→2013 mezclan cambio real con cambio de año base y de añada de clasificación—, por lo que se lee por el ",
  I("patrón y el orden"), ", no por el nivel exacto. La extracción de los tabulados se validó contra el propio INEGI a precisión de máquina."], first=True)
para(doc, ["El orden del encadenamiento hacia adelante en 2008 es coherente con el de 2013/2018 en la parte alta —grafito (1.69), cobre (1.63), sílice (1.60) y oro (1.48) por encima de la media— y en la baja —plata (0.80)—, y los compradores domésticos replican la misma estructura de eslabón único (metales preciosos y plomo-zinc a fundición y refinación; grafito a siderurgia; sílice a vidrio; barita a perforación de pozos). Dos caveats acotan su uso: los ",
  I("niveles"), " de VBP están en precios de 2008 y no son comparables; y el ", B("manganeso"),
  " no es comparable en 2008, porque su clase (212291) agrupa entonces actividades vecinas —mercurio, antimonio y otros metálicos— que inflan su VBP y contaminan su índice (1.00 frente a 1.79 en 2013). Con estas reservas, el corte de 2008 confirma que el mapa de eslabonamientos descrito es ",
  B("estructural y persistente"), ", no un rasgo de un solo año."])

heading(doc, "V.13  Límites metodológicos")
para(doc, ["Cuatro cautelas acotan la interpretación. Primera, la MIP no separa plomo de zinc, por lo que sus encadenamientos son conjuntos, a diferencia del índice de concentración, que sí los distingue. Segunda, los dos cortes corresponden a años base distintos; los ", I("niveles"),
  " de VBP no están deflactados, pero los índices normalizados, al medir posición relativa respecto al promedio de cada año, sí son comparables. Tercera, un valor alto de DI/VBP en los metales refleja fundición doméstica —un solo eslabón—, no necesariamente una cadena larga. Cuarta, el modelo de Ghosh supone coeficientes de distribución fijos y se emplea como descriptor de la posición del mineral, no como predicción."], first=True)

heading(doc, "Fuentes y referencias")
for s in [
  "Ghosh, A. (1958). Input-output approach in an allocation system. Economica, 25(97), 58–64.",
  "Hirschman, A. O. (1958). The Strategy of Economic Development. Yale University Press.",
  "INEGI. Sistema de Cuentas Nacionales de México. Matriz de Insumo-Producto, años base 2013 y 2018. Aguascalientes: INEGI.",
  "Leontief, W. (1941). The Structure of American Economy, 1919–1929. Harvard University Press.",
  "Miller, R. E. y Blair, P. D. (2009). Input-Output Analysis: Foundations and Extensions (2ª ed.). Cambridge University Press.",
  "Rasmussen, P. N. (1956). Studies in Inter-Sectoral Relations. North-Holland.",
]:
    refpara(doc, s)
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(6)
r = p.add_run("Cálculo propio a partir de la MIP del INEGI. Bases construidas: mip_encadenamientos_minerales.csv y mip_demanda_intermedia_minerales.csv (10 Datos/processed); rutina mip_calc.py (10 Datos/scripts).")
r.font.italic = True; r.font.size = Pt(9)

out = sys.argv[1]
doc.save(out)
print("Guardado:", out)
