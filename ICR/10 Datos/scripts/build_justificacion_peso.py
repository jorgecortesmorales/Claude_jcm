# -*- coding: utf-8 -*-
"""Inserto de redaccion para el Cap. I (Justificacion): 'Relevancia economica del objeto —
peso historico del bloque de diez minerales' (Actividad A, cifras corregidas 2026-09-09).
Genera un .docx en 11 Redaccion con prosa + tablas + la grafica peso_historico.png.
Fuentes de datos: peso_bloque_mineria.csv, peso_bloque_hist_*.csv."""
import sys, os
from docx import Document
from docx.shared import Pt, RGBColor, Twips, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

CHART=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\png_charts\peso_historico.png"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\11 Redaccion\Justificacion - peso del bloque (inserto Cap I) 2026-09-09.docx"

def para(doc, runs, justify=True, first=False, after=6):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
    pf=p.paragraph_format; pf.space_after=Pt(after); pf.line_spacing=1.15
    if first: pf.first_line_indent=Pt(21)
    for r in runs:
        if isinstance(r,str): p.add_run(r)
        else:
            txt,opt=r; run=p.add_run(txt); run.font.italic=opt.get("i",False); run.font.bold=opt.get("b",False)
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

doc=Document()
doc.add_paragraph().add_run("Relevancia económica del objeto: peso histórico del bloque de diez minerales").bold=True
p=doc.paragraphs[-1]; p.runs[0].font.size=Pt(15)
para(doc,["Nota de integración para el Capítulo I (Justificación). Cifras propias 2026-09-09; detalle metodológico en la memoria «Peso del bloque de 10 minerales (PIB, exportaciones, empleo)». Todas las series se construyen con fuentes primarias: MIP INEGI para PIB y empleo; UN Comtrade y USGS Minerals Yearbook para exportaciones y producción."],after=8)

para(doc,["La elección de los diez minerales —barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice y zinc— se sostiene, en primer término, en el ",
 B("peso del bloque en la economía"), ", medido a lo largo del periodo estudiado. Aunque el conjunto aporta apenas alrededor del ",
 B("0.7 % del producto interno bruto nacional"), " (matriz insumo-producto de 2013 y 2018), concentra cerca del ",
 B("60-65 % del PIB de la minería no petrolera"), " y del ", B("77 % de las exportaciones mineras"),
 " del país. Describir estos diez es, en la práctica, describir la minería metálica y no metálica mexicana de relevancia."],first=True)

add_table(doc,[3400,1500,1500,2438],
 ["Dimensión (bloque de 10 minerales)","2013","2018","Lectura"],
 [["Peso en el PIB nacional","0.70 %","0.71 %","pequeño pero estable"],
  ["Peso en el PIB de la minería (212)","65.2 %","61.0 %","~⅔ de la minería no petrolera"],
  ["Peso en las exportaciones totales","—","2.6 %","~77 % de las exportaciones mineras"],
  ["Empleo (puestos de trabajo)","59,474","42,159","cae: intensivo en capital"],
  ["Empleo / empleo nacional","0.10 %","0.07 %","no es intensivo en trabajo"]],fs=9)
caption(doc,"Cuadro. Peso del bloque de diez minerales en el PIB, las exportaciones y el empleo (MIP INEGI 2013 y 2018; exportaciones UN Comtrade sobre total del Banco Mundial). Fuente: cálculo propio.")

para(doc,["Su participación en las exportaciones no es estática: ",
 B("oscila entre 1.2 % (mínimo, 2002) y 5.5 % (máximo, 2011)"),
 " siguiendo el ciclo internacional de precios de los metales, un rasgo propio de una economía primario-exportadora tomadora de precios. El valor de la producción del bloque se multiplica por cerca de ",
 B("nueve entre 1992 y 2018"), " (por trece hasta 2022), en proporciones ",
 B("casi iguales de mayor volumen (×3.1) y precios más altos (×3.1)"),
 ", con el empuje de los precios concentrado en el superciclo de 2004-2013. En contraste, el empleo del sector ",
 B("decrece"), " —de 59 mil a 42 mil puestos entre 2013 y 2018— y no rebasa el 0.1 % del empleo nacional: es una actividad intensiva en capital y recurso, no en trabajo, lo que anticipa el diagnóstico de enclave."])

doc.add_picture(CHART, width=Inches(6.3))
doc.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
caption(doc,"Figura. Peso del bloque en las exportaciones (1992-2024, con el pico de 5.5 % en 2011) y descomposición del valor de producción entre precio y volumen (1992-2022; la franja mide el efecto precio). Fuente: elaboración propia con UN Comtrade, Banco Mundial y USGS.")

H2(doc,"Composición y desplazamiento histórico")
para(doc,["Dentro del bloque, cuatro metales —",B("cobre, oro, plata y plomo-zinc"),
 "— concentran alrededor del 94 % del valor agregado y del 95 % de las exportaciones. A lo largo del periodo se observa un ",
 B("desplazamiento hacia los metales preciosos"), ": el oro pasa de cerca del 6 % al 30 % del valor de la producción entre 1992 y 2018, y la plata se sostiene en torno al 19 % (México es el primer productor mundial)."],first=True)
add_table(doc,[2200,1300,1300,1300,2238],
 ["Mineral","1992","2003","2018","Nota"],
 [["Cobre","38 %","33 %","30 %","primer lugar, cede peso"],
  ["Oro","6 %","12 %","30 %","el gran ascenso (post-2008)"],
  ["Plata","15 %","20 %","19 %","alto y estable"],
  ["Zinc","22 %","18 %","13 %","desciende"],
  ["Plomo","8 %","7 %","4 %","desciende"],
  ["Resto (5 minerales)","~11 %","~10 %","~4 %","marginal en valor"]],fs=9)
caption(doc,"Cuadro. Composición del valor de producción del bloque por mineral (participación %). Fuente: cálculo propio con volúmenes USGS/CAMIMEX y precios USGS.")

para(doc,["Los seis minerales restantes —sílice, fluorita, grafito, manganeso y barita— pesan poco en valor, pero se incorporan por su ",
 B("criticidad estratégica"), " como insumos industriales (flúor y fluoropolímeros, vidrio y electrónica, acero, baterías, perforación). La selección de los diez combina, por tanto, ",
 B("peso económico y criticidad"), ", y esa dualidad forma parte de la justificación del objeto."])
para(doc,["Este retrato cuantitativo no debilita la elección por el tamaño acotado del sector: la ",
 B("refuerza"), ". El aporte de la investigación no reside en la magnitud del sector, sino en la ",
 B("caracterización histórica de su inserción"), " en las cadenas de valor: un crecimiento traccionado por precios, sin generación proporcional de empleo ni de cadena doméstica —precisamente el enclave estructural que la tesis describe—."])

p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(10)
r=p.add_run("Fuentes: cálculo propio. MIP INEGI 2013/2018 (PIB B.1bP, empleo PT); UN Comtrade 1992-2024; Banco Mundial (exportaciones totales de México); USGS Minerals Yearbook (producción 1992-2003 y 2019-2022) y CAMIMEX (2004-2018); precios USGS empalmados. Detalle y validación en la memoria «Peso del bloque de 10 minerales (PIB, exportaciones, empleo)» y en el Catálogo de Bases de Datos, §21.")
r.font.italic=True; r.font.size=Pt(9)

doc.save(OUT); print("Guardado:",OUT)
