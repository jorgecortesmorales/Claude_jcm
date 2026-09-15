# -*- coding: utf-8 -*-
"""Capitulo VII - Reforma 2023 (contexto) + referencia internacional. python-docx.
Reproduce el andamio reencuadrado (descriptivo) e integra la comparacion internacional
del Paso 6 (OECD ICIO 2020): reencuadre del 'caso de exito'. Fuente de datos:
processed/icio_comparacion_mineria.csv; memoria comparativa en 05 Diagnostico Insumo-Producto."""
import sys
from docx import Document
from docx.shared import Pt, RGBColor, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH
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
def checklist(doc,items):
    for it in items:
        p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(2); p.paragraph_format.left_indent=Pt(14)
        r=p.add_run("[ ]  "+it); r.font.size=Pt(11)

B=lambda s:(s,{"b":True}); I=lambda s:(s,{"i":True})

# ================= DOCUMENTO =================
doc=Document()
normal=doc.styles["Normal"]; normal.font.name="Times New Roman"; normal.font.size=Pt(12)
sec=doc.sections[0]
sec.page_width=Twips(12240); sec.page_height=Twips(15840)
for m in ("top_margin","bottom_margin","left_margin","right_margin"): setattr(sec,m,Twips(1701))

p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(2)
p.add_run("Capítulo VII").bold=True; p.runs[0].font.size=Pt(16)
p2=doc.add_paragraph(); p2.paragraph_format.space_after=Pt(2)
r2=p2.add_run("La reforma a la Ley Minera de 2023 como contexto institucional, y la referencia internacional"); r2.font.bold=True; r2.font.size=Pt(13)
p3=doc.add_paragraph(); p3.paragraph_format.space_after=Pt(12)
r3=p3.add_run("Jorge Cortés Morales — Maestría en Economía, UAM Azcapotzalco"); r3.font.size=Pt(11)

para(doc,[B("Objetivo específico (contexto institucional). "),
 "Describir la reforma a la Ley Minera de 2023 como parte del marco institucional que enmarca los mercados de los minerales críticos, y contrastar la trayectoria mexicana con la de países usados como referencia. El propósito declarado de la reforma fue reforzar la rectoría estatal sobre el recurso y acotar la especulación, no la industrialización; por ello se trata como contexto y no como una intervención cuyo impacto causal se estime."])
para(doc,[B("Encuadre (diseño descriptivo). "),
 "Este capítulo es contextual. La reforma se describe por su contenido y su coyuntura; el análisis documental de las disposiciones es la vía principal y el ",
 I("event study")," queda como complemento opcional que mide la reacción del mercado al anuncio, no un efecto de industrialización. La sección VII.5 añade la referencia internacional, que reencuadra el supuesto del protocolo sobre los 'casos de éxito'."])

H1(doc,"VII.1  La reforma de 2023: contenido y coyuntura")
para(doc,["Cuatro disposiciones (abril de 2023): exclusividad del Servicio Geológico Mexicano sobre la exploración; reducción de las concesiones de 50 a 30 años, con prórroga única de 25; fin de la minería como actividad preferente; y un nuevo régimen de licitaciones con evaluación de impacto social y ambiental. A mediados de 2026 el panorama es de litigio constitucional activo ante la SCJN, con exploración a la baja (−11.5 % en 2024) e inversión extranjera directa sectorial en caída (−56.3 % en 2025), pese a un valor de producción récord (312,461 millones de pesos en 2024, +19.6 %)."],first=True)

H1(doc,"VII.2  Estrategia empírica")
H2(doc,"VII.2.1  Análisis de escritorio (vía principal)")
para(doc,["Análisis documental diferencial de la reforma —qué disposiciones afectan de distinta forma a las concesiones vigentes de los incumbentes frente a las nuevas de los entrantes— y lectura sistemática de reportes anuales, informes a la bolsa y transcripciones de ",
 I("earnings calls")," de las mineras, para reconstruir dónde procesan o refinan y qué dicen sobre integrar aguas abajo. Se apoya en el ",
 I("process tracing")," (Beach y Pedersen, 2013) y el análisis temático (Braun y Clarke, 2006), que operan sobre evidencia documental y no requieren trabajo de campo."],first=True)
H2(doc,"VII.2.2  Event study (MacKinlay, 1997) — complemento opcional")
para(doc,["Retornos anormales acumulados (CAR) de las empresas mineras cotizadas en torno a la fecha de la reforma: se define la ventana de evento y de estimación, el modelo de mercado y la muestra de emisoras. Es una vía de gabinete, viable sin trabajo de campo."],first=True)
H2(doc,"VII.2.3  Entrevistas semiestructuradas (complemento opcional)")
para(doc,["Siete actores (CAMIMEX, SGM, LitioMx, una empresa grande establecida, una empresa o proyecto entrante, un despacho de derecho minero y un académico), con análisis de contenido temático y reconstrucción causal. Las entrevistas dejan de ser pieza de carga: la distinción oferta/demanda que planteaba la observación del asesor —los actores tradicionales no son actores industriales— se resuelve con evidencia documental (matriz insumo-producto, comercio exterior y reportes de empresas del lado aguas abajo), sin depender del trabajo de campo."],first=True)

H1(doc,"VII.3  Resultados")
para(doc,[B("Event study preliminar (insumo, no resultado definitivo). "),
 "Con cierres diarios ajustados de Yahoo Finance para GMEXICOB.MX y PE&OLES.MX contra el IPC (^MXX), modelo de mercado con ventana de estimación del 28 de septiembre de 2022 al 4 de abril de 2023 y evento en la aprobación en Diputados (20-21 de abril de 2023), Grupo México registra un retorno anormal de −4.07 % el día de la votación (t = −1.64) y de −4.73 % tras la entrada en vigor (t = −1.90), con un CAR[−1,+10] cercano a −8.3 %; Peñoles resulta más ruidosa. La señal económica tiene el signo esperado, pero no alcanza significancia al 5 % con una sola emisora: confirma que el procedimiento funciona y que el valor del ejercicio está en agrupar empresas en cartera y en el contraste entrantes vs. establecidos, no en el signo. Limitación: Grupo México pesa mucho en el IPC, lo que sesga su beta."],first=True)

H1(doc,"VII.4  Discusión: alcance temporal del análisis")
para(doc,["Conviene acotar el alcance, siguiendo la observación del asesor de que la reforma no ofrece todavía la escala de tiempo para analizar efectos estructurales. El capítulo se encuadra como análisis de impacto de ",
 B("corto plazo / de anuncio"),
 " (reacción de mercados e inversión), no de efectos de industrialización de largo plazo. La reforma es, en el argumento de la tesis, un cambio en la ",
 I("rectoría")," del recurso que no toca el eslabón donde se decide la agregación de valor: no crea capacidad de transformación ni incentivos a integrarla, de modo que, por sí sola, no modifica el patrón de enclave descrito en los capítulos V y VI."])

H1(doc,"VII.5  La referencia internacional: ¿casos de éxito?")
para(doc,["El protocolo toma a Chile y Australia como referencias de 'casos de éxito' en generar cadenas de valor a partir de la minería. Puesto a prueba con una fuente comparable —las tablas insumo-producto inter-país de la OCDE (edición 2023, corte 2018, el mismo año del Ghosh de la matriz nacional en el capítulo V)—, ese supuesto se matiza. Sobre el bloque doméstico de cada país se calculó el encadenamiento hacia adelante del sector-minería no energética (menas metálicas y otra minería) con el mismo método del capítulo V (índice de Ghosh-Rasmussen, media de cada economía = 1). Además de Chile y Australia se incorporaron siete comparables elegidos con una lógica explícita: dos referentes del clúster nórdico —Finlandia y Suecia— que la literatura reconoce por su integración metalúrgica; ", B("China"), ", el procesador global al que se dirige el 94.7 % del concentrado de cobre mexicano (el extremo opuesto, donde el valor se captura); ", B("Brasil"), ", el par latinoamericano por tamaño y estructura industrial; y ", B("Perú"), ", el vecino andino con la misma canasta polimetálica que México, para distinguir si el enclave es un rasgo nacional o regional."])
add_table(doc,[2100,1750,1500,3438],
 ["País","Fwd (Rasmussen)","Rango (de 45)","Lectura"],
 [["China","1.53","3","El más alto: su complejo metalúrgico funde y refina minerales de medio mundo (integración doméstica genuina, véase el texto)."],
  ["México","1.51","2","Alto en el agregado, pero engañoso (véase el texto): promedia los metales fundidos con el cobre exportado en bruto."],
  ["Finlandia","1.31","7","Por encima del promedio: fundición/refinación de níquel y cobalto (Harjavalta, Kokkola)."],
  ["Suecia","1.27","6","Alto: modelo mina-fundición integrado (Boliden Rönnskär)."],
  ["Brasil","0.99","25","En el promedio de su economía: siderurgia parcial, pero exporta hierro sobre todo en bruto."],
  ["Australia","0.83","31","Por debajo del promedio propio; hierro y litio se exportan en bruto."],
  ["Chile","0.73","36","Minería enorme (>9 % del PIB) pero forward débil, por debajo del promedio de su propia economía: patrón de enclave."],
  ["Perú","0.62","39","El más bajo: enclave polimetálico casi puro (misma canasta que México, sin transformación doméstica)."]],fs=9)
caption(doc,"Cuadro VII.1. Encadenamiento hacia adelante del sector-minería no energética (Ghosh-Rasmussen, media país = 1), OECD ICIO, corte 2018. Fuente: cálculo propio; base icio_comparacion_mineria.csv. Caveat: comparación a nivel sector-minería agregado, no por mineral; clasificación ISIC.")
para(doc,["Cuatro lecturas se derivan. Primera: ",
 B("Chile, Australia, Brasil y Perú no son casos de éxito en el encadenamiento hacia adelante"),
 ". Su minería se sitúa en o por debajo del promedio de su propia economía (0.73, 0.83, 0.99 y 0.62); comparten con México el patrón de exportar concentrado o mineral en bruto —Perú, con la misma canasta polimetálica, es el caso más extremo—. Lo que distingue a algunos no es una cadena manufacturera lograda, sino la respuesta institucional: la propiedad estatal y la captura fiscal (Codelco) en Chile, los servicios y la tecnología minera (el sector METS) en Australia, la siderurgia en Brasil."])
para(doc,["Segunda: el ", B("referente en integración aguas adelante es China y el modelo nórdico"),
 ". China por su complejo metalúrgico de escala global; Finlandia y Suecia por su fundición y refinación domésticas (Boliden, Harjavalta) pese a una minería pequeña. Es el contrafactual útil para la política del capítulo VIII: no 'ser Chile', sino integrar la secuencia mina → fundición → metal con arreglos de propiedad y política domésticos; y China marca a dónde se va el valor que México no retiene."])
para(doc,["Tercera: el coeficiente agregado de México (1.51) ", B("engaña si se lee solo"),
 ". Es alto porque el agregado promedia los metales que sí se funden en el país (que van a la industria de metales básicos) con el cobre, del que se exporta el 94.7 % como concentrado a China. El enclave estructural no aparece en el promedio del sector, sino al desagregar por mineral (capítulo V) y observar el comercio por etapa: es el ",
 B("caveat de agregación"),
 ", y una confirmación empírica de que un índice de Ghosh alto no equivale a una cadena de valor desarrollada."])
para(doc,["Cuarta, y la más ilustrativa: ",
 B("México (1.51) y China (1.53) tienen un Ghosh casi idéntico, pero significan cosas opuestas"),
 ". La descomposición de valor agregado de la subsección siguiente los separa nítidamente —China transforma en casa casi todo lo que extrae; México exporta el cobre en concentrado— y demuestra por qué la referencia internacional desplaza la pregunta de política de 'cómo replicar a Chile o Australia' a 'qué arreglos de propiedad, fiscales y de capacidad de transformación acompañan a la extracción', que es donde ni la reforma de 2023 ni el patrón exportador vigente intervienen."])

H2(doc,"VII.5.1  El enclave en dinero: descomposición de valor agregado")
para(doc,["El índice de Ghosh es un coeficiente de asignación; no mide cuánto valor retiene el país. Para verlo se descompone, sobre la matriz global de la OCDE, el valor agregado minero que cada país exporta, distinguiendo la parte que sale ",
 B("ya transformada en casa"), " (embebida en exportaciones de otros sectores, como los metales básicos) de la que sale como ",
 B("producto minero en crudo"), " —concentrado— para reprocesarse en el extranjero (",
 I("crudo_share"), "). Un valor alto es la firma del enclave en dinero."],first=True)
add_table(doc,[1550,1500,1400,4138],
 ["País","crudo (2018)","serie","Lectura"],
 [["Perú","0.98","0.92→0.98","Empata a Chile como enclave más profundo en dinero: misma canasta que México, sin transformación doméstica."],
  ["Chile","0.98","1.00 → 0.96","Enclave extremo y constante 26 años: casi todo el VA de su cobre sale en concentrado a reprocesar afuera. El Ghosh (0.73) solo lo insinuaba."],
  ["Brasil","0.82","0.87→0.82","Alto pese a un Ghosh ≈1: exporta hierro sobre todo en bruto, con siderurgia parcial."],
  ["Australia","0.77","0.52 → 0.74","Se deteriora: cada vez más crudo (hierro y litio a China)."],
  ["Suecia","0.48","0.42 → 0.46","Integra cerca de la mitad (Boliden)."],
  ["Finlandia","0.45","0.31 → 0.51","El más integrado en promedio de los nórdicos (níquel, cobalto)."],
  ["México","0.38","0.24 → 0.48","Agregado bajo —parece integrado— pero engañoso, con repunte reciente y absorción extranjera al alza (véase el texto)."],
  ["China","0.07","0.08→0.07","El procesador: transforma en casa casi todo lo que extrae; capta el valor que los demás exportan en crudo."]],fs=9)
caption(doc,"Cuadro VII.2. Fracción del valor agregado minero exportado que sale en crudo (crudo_share), minería no energética. Columna 'serie': 1995→2020 para los cinco países originales, 2008→2018 para China, Brasil y Perú. Fuente: cálculo propio sobre OECD ICIO 2023; base icio_dva_mineria.csv.")
para(doc,["La descomposición confirma cuatro cosas. En términos de valor, ",
 B("Chile y Perú son los enclaves más profundos"), " (≈0.98 de su VA minero exportado sale en crudo): el 'referente' del protocolo es, en dinero, uno de los casos menos integrados, y Perú —con la misma canasta que México— muestra que el enclave no es idiosincrásico, sino resultado de la falta de transformación doméstica. En el extremo opuesto, ",
 B("China exporta en crudo apenas el 7 %"), ": funde casi todo, y es a donde va el valor que los demás no retienen. En México, el ",
 B("agregado vuelve a engañar"), ": su crudo_share (0.38) es incluso menor que el de Suecia porque promedia los metales preciosos que sí se funden en el país con el cobre que sale 94.7 % en concentrado —el enclave del cobre solo aparece al desagregar—. La comparación ",
 B("México (Ghosh 1.51, crudo 0.38) frente a China (1.53, crudo 0.07)"), " —índice de asignación casi idéntico, captura de valor opuesta— es la prueba más clara de por qué el Ghosh no debe leerse solo. Con todo, de punta a punta el patrón mexicano se ",
 B("profundiza"), ": el crudo_share pasa de 0.24 (1995) a 0.48 (2020) —con oscilación cíclica— y, sobre todo, el valor de su minería absorbido en el extranjero se triplica (0.21 → 0.65), coherente con el desplazamiento de destinos hacia China. La comparación es a nivel minería agregada; para el detalle por mineral se remite al comercio por etapa."])

H2(doc,"VII.5.2  Criticidad y dependencia: el eslabón estratégico se importa")
para(doc,["La comparación internacional se agudiza al recordar que las listas oficiales de criticidad no señalan minerales genéricos, sino ",
 B("productos y grados específicos"), ": la Unión Europea (Critical Raw Materials Act, 2023) designa estratégicos el ",
 I("silicio metálico"), ", el ", I("grafito natural grado batería"), " y el ", I("manganeso grado batería"),
 ", y el USGS (2025) añadió el silicio, el cobre, el plomo y la plata a su lista. Cruzando esa criticidad producto por producto (Cap. II) con lo que México efectivamente produce, aparece un patrón nítido: en los minerales cuyo eslabón de mayor criticidad es de ",
 B("grado batería o electrónico"), ", México extrae y exporta el crudo de baja criticidad e ",
 B("importa —o no accede a— el producto estratégico"), "."],first=True)
add_table(doc,[1700,2950,1450,2238],
 ["Mineral","Producto de mayor criticidad (estratégico)","¿México lo produce?","Dependencia"],
 [["Silicio (sílice)","Silicio metálico (semiconductores, fotovoltaica)","No","Importa (EE.UU., China)"],
  ["Grafito","Grado batería / sintético, electrodos","No","Importa (China)"],
  ["Manganeso","Sulfato de Mn grado batería (cátodos)","No","Importa"],
  ["Fluorita","Fluoropolímeros y LiPF₆ (baterías) a partir del HF","HF sí; derivados no","Importa los derivados"],
  ["Cobre","Cátodo refinado (electrificación)","Sí","Exporta cada vez más concentrado"],
  ["Plata","Plata refinada (fotovoltaica)","Sí","Exporta refinada"],
  ["Oro","Oro refinado (seguridad nacional EE.UU.)","Sí","Exporta refinado"]],fs=9)
caption(doc,"Cuadro VII.3. El producto de mayor criticidad de cada mineral frente a la capacidad productiva de México. Fuente: USGS (2022/2025), UE (CRMA 2023) e IEA; clasificación propia en processed/criticidad_productos.csv.")
para(doc,["La lectura de política es directa y refuerza la del capítulo: México no solo exporta con menos transformación que China o los nórdicos (VII.5–VII.5.1), sino que ",
 B("el eslabón de mayor valor y criticidad —el que una política de seguridad de suministro o de captura de valor buscaría asegurar— es justo el ausente"),
 " en grafito, sílice y manganeso, y el que se exporta como intermedio en la fluorita. La dependencia crítica de México no está en la mina, sino en el producto transformado de la transición energética, que compra al exterior mientras vende su materia prima. El detalle por mineral y sector obra en [[Clasificacion de productos por criticidad]] (Cap. II) y en las fichas de cadena (Cap. VI)."])

H2(doc,"VII.5.3  El encadenamiento por eslabón: dónde se sostiene el arrastre")
para(doc,["La comparación del encadenamiento hacia adelante gana precisión al calcularlo no solo para el eslabón ",
 B("extractivo"), ", sino también para la ", B("refinación"), " (industrias metálicas básicas, C24) y la ",
 B("semimanufactura"), " (productos metálicos, C25) de cada país (OECD ICIO, corte 2018). Revela ",
 B("hasta qué eslabón cada país sostiene el arrastre"), "."],first=True)
add_table(doc,[2000,1880,1880,1880],
 ["País","L1 extracción","L2 refinación","L3 semimanufactura"],
 [["China","1.53","1.30","1.02"],
  ["México","1.51","1.17","1.12"],
  ["Finlandia","1.31","1.06","1.14"],
  ["Suecia","1.27","1.08","1.06"],
  ["Brasil","0.99","1.19","1.24"],
  ["Australia","0.83","0.83","1.24"],
  ["Chile","0.73","1.23","1.12"],
  ["Perú","0.62","0.98","1.06"]])
caption(doc,"Cuadro VII.4. Índice de Ghosh hacia adelante (Rasmussen, media país=1) por eslabón de la cadena metálica, 2018. "
 "Cortes 2008/2013/2018/2020 en processed/icio_eslabones_metal.csv (script icio_eslabones.py). C24/C25 son toda la industria metálica, no solo los 10 minerales.")
para(doc,["El contraste es nítido. ", B("China sostiene el arrastre de la extracción a la refinación (1.53 → 1.30)"),
 ": es el procesador integrado. ", B("México cae más (1.51 → 1.17)"),
 ": su alto arrastre extractivo no se prolonga con la misma fuerza a la transformación. En el otro extremo, ",
 B("Chile —con una extracción de arrastre bajísimo (0.73)— tiene la refinación más integrada (1.23)"),
 ": su poca fundición sí alimenta industria, lo que confirma que el índice extractivo aislado engaña en ambos sentidos. Este mismo patrón se observa por mineral en México (Cap. V, V.10.1: la refinación de metales preciosos cae a 0.62) y por entidad —la transformación metálica con más arrastre se concentra en Coahuila y Nuevo León, el eje siderúrgico, no donde más se extrae (base ghosh_estatal_eslabones.csv)—. El detalle obra en la memoria de encadenamientos por eslabón."])

H1(doc,"VII.6  Pendientes concretos (event study y entrevistas, opcionales)")
checklist(doc,[
 "Diseñar la guía de entrevistas.",
 "Contactar y agendar a los siete actores clave.",
 "Transcribir y codificar las entrevistas.",
 "Definir la ventana de evento y la cartera de empresas cotizadas para el event study.",
 "Calcular los CAR por cartera y el contraste entrantes vs. establecidos.",
])

p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(10)
r=p.add_run("Fuentes: reforma a la Ley Minera (DOF, 2023); reportes corporativos e IPC (Yahoo Finance) para el event study; OECD (2023), Inter-Country Input-Output Database, para los coeficientes internacionales de ocho países (corte 2018) y la descomposición de valor agregado (1995-2020, y cortes 2008/2013/2018 para China, Brasil y Perú); Aroca (2018), Atienza et al. (2018) y Weldegiorgis et al. (2024) para Chile y Australia; Nordic Innovation (2026) y OECD (Mining Regions) para el clúster nórdico. Memoria [[Memoria - Comparacion internacional]] y bases icio_comparacion_mineria.csv e icio_dva_mineria.csv en 10 Datos/processed.")
r.font.italic=True; r.font.size=Pt(9)

out=sys.argv[1]; doc.save(out); print("Guardado:",out)
