# -*- coding: utf-8 -*-
"""Capitulo VIII - Sintesis, conclusiones y recomendaciones. python-docx.
Integra (C2) todos los hallazgos: tipologia A/B/C/D, contrafactual nordico (Paso 6),
recomendaciones diferenciadas por eslabon ausente y declaraciones de huecos."""
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

# ================= DOCUMENTO =================
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Times New Roman"; normal.font.size=Pt(12)
sec=doc.sections[0]
sec.page_width=Twips(12240); sec.page_height=Twips(15840)
for m in ("top_margin","bottom_margin","left_margin","right_margin"): setattr(sec,m,Twips(1701))

p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(2)
p.add_run("Capítulo VIII").bold=True; p.runs[0].font.size=Pt(16)
p2=doc.add_paragraph(); p2.paragraph_format.space_after=Pt(2)
r2=p2.add_run("Síntesis, conclusiones y recomendaciones"); r2.font.bold=True; r2.font.size=Pt(14)
p3=doc.add_paragraph(); p3.paragraph_format.space_after=Pt(12)
r3=p3.add_run("Integración de los hallazgos de los capítulos V, VI y VII — Jorge Cortés Morales, UAM Azcapotzalco"); r3.font.size=Pt(11)

para(doc,[B("Objetivo específico (síntesis). "),
 "Integrar la caracterización de los diez mercados —estructura extractiva, cadena local e inserción en las cadenas de valor globales— en una tipología descriptiva y derivar de ella las bases para una política industrial. No se diagnostica una jerarquía de fallas causales; se describe dónde cada cadena existe, dónde se detiene y dónde está ausente."])

H1(doc,"VIII.1  Síntesis de los hallazgos")
para(doc,["El trabajo reúne cinco indicadores construidos y validados: la estructura empresarial por mineral (capítulo IV y el HHI 2004-2024), los encadenamientos de Leontief y Ghosh de la matriz insumo-producto (capítulo V), el coeficiente de captura de valor como serie continua 1992-2025, el comercio por etapa de procesamiento y su geografía de destino, y el contexto institucional de la reforma con la referencia internacional (capítulo VII). El HHI y el Ghosh se integran como descriptores conjuntos de cada mercado, nunca como una relación causal estimada."],first=True)
para(doc,["El hilo que integra los hallazgos es descriptivo: cómo son los mercados de los diez minerales y en qué eslabón de sus cadenas de valor participa México. Cuatro resultados transversales lo resumen. Primero, los minerales críticos mexicanos tienen encadenamiento hacia atrás bajo (extracción intensiva en recursos). Segundo, su encadenamiento hacia adelante es heterogéneo, pero la lectura conjunta de los indicadores —no del Ghosh aislado— revela que la cadena, cuando existe, suele detenerse en el metal refinado. Tercero, el patrón se profundiza en el tiempo: se exporta en fases cada vez más crudas y con destino crecientemente concentrado en China. Cuarto, la comparación internacional con ocho países muestra que ni Chile, ni Australia, ni Brasil ni Perú superan ese patrón en el encadenamiento hacia adelante, y que el referente real de integración es China —el procesador global— y el modelo nórdico; la descomposición de valor agregado lo confirma en dinero —Chile y Perú exportan en crudo cerca del 98 % del valor de su minería, mientras China solo el 7 %— y revela que el agregado de México, como el de su índice de Ghosh, engaña porque promedia los metales que sí se funden con el cobre que sale en concentrado: México y China tienen un Ghosh casi idéntico (1.51 y 1.53) pero una captura de valor opuesta, y Perú, con la misma canasta polimetálica que México, es el enclave más profundo."])

H1(doc,"VIII.2  Tipología de los mercados y posición en la cadena de valor")
para(doc,["La caracterización integrada distingue cuatro tipos de mercado según su grado de transformación doméstica. ",
 B("Tipo A, cadena local desarrollada"),
 " (manganeso, fluorita): transformación de escala verticalmente integrada por el propio extractor. ",
 B("Tipo B, truncada en el metal refinado"),
 " (cobre, oro, plata, plomo, zinc): los grupos integran hasta la fundición y refinación y exportan el metal. ",
 B("Tipo C, usuario doméstico con eslabón importado"),
 " (sílice, grafito): existe industria usuaria, pero el eslabón intermedio de mayor valor se importa. ",
 B("Tipo D, exportación en bruto"),
 " (barita): sin eslabón manufacturero doméstico."],first=True)
para(doc,["Esta tipología se apoya en diez ",
 B("fichas de cadena de valor"),
 " que descomponen cada mercado en cinco eslabones —",
 B("L0"),
 " (recurso en el suelo), ",
 B("L1"),
 " (extracción y beneficio: mina → concentrado), ",
 B("L2"),
 " (fundición-refinación o química primaria: concentrado → metal o químico básico), ",
 B("L3"),
 " (semimanufactura) y ",
 B("L4"),
 " (manufactura final y uso)— y localizan el ",
 B("punto de ruptura"),
 ", el eslabón a partir del cual el país deja de agregar valor. Leída así, la posición de México se ordena con nitidez: los metales de tipo B se rompen en L2→L3 o antes (se exporta concentrado o metal refinado y se importan las semimanufacturas); los de tipo C, en L1→L2 (falta el eslabón intermedio pese a existir la industria usuaria); la barita (D) no pasa de L1; y aun los dos casos de tipo A se detienen en el intermedio —el manganeso en L2→L3, antes de la química fina, y la fluorita en el ácido fluorhídrico, antes de los fluoropolímeros—."])
para(doc,["Un ",B("hallazgo metodológico"),
 " refuerza el diagnóstico: al cuantificar los eslabones aguas abajo con la matriz insumo-producto (834 clases), ",
 B("solo el cobre posee clases estadísticas (SCIAN) dedicadas a su transformación"),
 "; el oro y la plata comparten una sola clase de metales preciosos, el plomo y el zinc otra, el manganeso comparte la suya con la siderurgia y el ácido fluorhídrico se diluye en «químicos básicos inorgánicos». La invisibilidad estadística de los eslabones de transformación —imposibles de aislar por mineral— es, ella misma, una marca del enclave. A ello se suma que buena parte de la cadena local ocurre dentro de las firmas extractivas (integración vertical), lo que el dato sectorial subestima, y que solo el cobre está co-localizado (fundición junto a la mina). La descripción no atribuye la falta de industrialización a una causa única: sitúa cada mineral en su cadena, y de ese retrato se derivan las bases de política del apartado VIII.3."])
add_map(doc, MAPA_CONJUNTO,
 "Figura VIII.1. Geografía de las cadenas de valor del bloque. Izquierda: estados extractores y hubs de "
 "transformación; derecha: ejes de exportación (rojo, sobre todo concentrados a Asia) e importación (azul). "
 "El valor sale con el concentrado hacia el procesador asiático y regresa, procesado, desde Estados Unidos. "
 "Elaboración propia (SGM 2024; UN Comtrade 2019-2024).")

H1(doc,"VIII.3  Recomendaciones de política")
para(doc,["Las recomendaciones son diferenciadas por tipo de mercado y se enuncian como ",
 B("bases descriptivas"),
 " —dónde intervendría una política que quisiera prolongar la cadena—, no como un plan cuya efectividad se estime aquí. La referencia internacional orienta el criterio: el contraste con Finlandia, Suecia y China indica que la palanca no es la escala ni la dotación extractiva (Chile y Perú las tienen y no integran), sino la ",
 B("capacidad de transformación doméstica"),
 " acompañada de arreglos de propiedad y política que la retengan en el país."],first=True)
add_table(doc,[1950,2400,4488],
 ["Tipo","Eslabón ausente / margen","Base de política"],
 [["A · Manganeso, fluorita","Escalar al eslabón de mayor valor (fluorita: del HF a los fluoropolímeros).","Sostener la integración existente y apoyar el salto a productos de mayor valor (química del flúor); es el tipo más cercano al modelo nórdico."],
  ["B · Cobre, oro, plata, plomo, zinc","Prolongar más allá del metal refinado hacia semimanufacturas y manufactura, hoy parcialmente importadas.","Incentivar la fundición y la manufactura aguas abajo; el cobre —94.7 % exportado como concentrado a China— es el caso emblemático donde la política de contenido nacional tendría más margen."],
  ["C · Sílice, grafito","Sustituir el eslabón intermedio importado (silicio/ferrosilicio; electrodos de grafito) por producción nacional.","Aprovechar la extracción y la industria usuaria ya existentes para cerrar el eslabón intermedio; en grafito, atender que el grado batería (no producido en México) es otra cadena."],
  ["D · Barita","No hay eslabón manufacturero doméstico.","Condicionar el aprovechamiento del recurso a algún grado de agregación de valor; política más exigente por la ausencia de base industrial."]],fs=9)
caption(doc,"Cuadro VIII.1. Bases de política diferenciadas por tipo de mercado (eslabón ausente).")
para(doc,["Un corolario del capítulo VII: la reforma de 2023 opera sobre la ",
 I("rectoría")," del recurso (concesiones, exploración), no sobre el eslabón donde se decide la agregación de valor. Una política industrial de minerales críticos coherente con este diagnóstico tendría que actuar sobre la ",
 B("capacidad de transformación"),
 " —el lado que ni la reforma ni el patrón exportador vigente tocan—, siguiendo el criterio nórdico de integrar mina → fundición → producto con arreglos domésticos, más que replicar la escala extractiva de Chile o Australia."])

H1(doc,"VIII.4  Limitaciones y declaración de vacíos")
para(doc,["Fiel al criterio de no imputar, la investigación declara los vacíos de sus series y cómo se intentó llenar cada uno; ninguno se rellenó con supuestos. Se agrupan por indicador."],first=True)
add_table(doc,[2350,4200,2288],
 ["Indicador","Vacío declarado","Tratamiento"],
 [["CCV (captura de valor)","Plomo 1994 sin dato (no hay comercio espejo). Oro y plata no informativos (artefacto de ley: mena en bruto ÷ metal puro).","Plomo 1994 se declara como cero estructural, no se imputa; oro/plata se describen por el comercio por etapa (doré/joyería)."],
  ["CCV — relleno por espejo","Los huecos completados con datos espejo son valores CIF (flete y seguro incluidos).","Pueden sobrestimar el valor unitario frente al FOB propio; los años rellenados se leen con esa reserva y se marcan en la base."],
  ["HHI (concentración)","1994-2003 no incluido en la serie; 1992-1993 no reconstruible (privatización en curso, sin estructura por empresa).","2004-2020 es aproximado (por régimen, cota inferior); 1994-2003 sería recuperable con la Tabla 2 del USGS (tarea pendiente); 1992-1993 se declara irrecuperable."],
  ["Encadenamientos MIP","La MIP combina plomo y zinc (coextracción); los cortes son años base distintos; el corte 2008 no es comparable en nivel (y su clase de manganeso es más amplia).","Plomo-zinc se reporta conjunto; los niveles no se comparan, solo los índices normalizados; 2008 se usa como patrón, con caveats explícitos."],
  ["RAS por mineral","La MIP a nivel Clase solo existe para años base (2013, 2018); lo anual son cuadros de oferta-utilización con la minería agregada.","El RAS por mineral para años recientes es inviable; la necesidad se cubre con el CCV (anual, por mineral) y el agregado observado de la OCDE (capítulo VII). No se fabrica un RAS falso."],
  ["Comercio por destino","Comtrade reporta el socio declarado, no el consumo final (reexportación y entrepôt no depurados).","El desplazamiento hacia China se reporta con ese caveat, que no altera su dirección."],
  ["Comparación internacional","Las tablas OCDE dan 'minería' agregada, no por mineral; corte 2018 y clasificación ISIC. Ocho países (China, Brasil y Perú se computaron en los cortes 2008/2013/2018).","La comparación es a nivel sector-minería, no por mineral (caveat de agregación); se compara la posición relativa, no los niveles absolutos."],
  ["DVA / reprocesamiento","La ventana del ICIO (edición 2023) es 1995-2020; queda fuera 1992-94 y 2021-2025.","La descomposición de valor agregado cubre 1995-2020 completo (incluye los tres cortes de la MIP: 2008, 2013, 2018); las colas se siguen con el comercio por etapa (1992-2024)."],
  ["Cierre temporal","Los datos de 2025 (HHI/estructura) aún no se publican.","Las series duras se cierran en 2024; el CCV llega a 2025 solo donde el comercio ya está disponible."]],fs=8)
caption(doc,"Cuadro VIII.2. Declaración de vacíos por indicador y su tratamiento (criterio: declarar, no imputar).")
para(doc,["Estas limitaciones no comprometen el retrato descriptivo, que se sostiene en la ",
 B("convergencia de cinco indicadores independientes"),
 " (estructura, encadenamientos, captura de valor, comercio por etapa y comparación internacional). La agenda futura es clara: recuperar el HHI 1994-2003 con las tablas históricas del USGS; regionalizar los encadenamientos por estado (cocientes de localización); y, cuando el dato lo permita, desagregar la comparación internacional por debajo del sector-minería. El aporte central de la tesis —la construcción de las bases de datos y los indicadores desagregados por mineral, y su lectura conjunta bajo el concepto de enclave estructural— queda disponible para esa continuación."])

p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(10)
r=p.add_run("Fuentes: síntesis propia de los capítulos IV-VII. Bases e indicadores en 10 Datos/processed (hhi_consolidado.csv, mip_encadenamientos_minerales.csv, ccv_serie.csv, comercio_*_1992_2024.csv, georref_*.csv, icio_comparacion_mineria.csv); memorias en 05 Diagnóstico Insumo-Producto y 10 Datos.")
r.font.italic=True; r.font.size=Pt(9)

out=sys.argv[1]; doc.save(out); print("Guardado:",out)
