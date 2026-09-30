# -*- coding: utf-8 -*-
"""Actualiza los campos (índices TOC de contenido, cuadros e ilustraciones) del manuscrito
y reexporta el PDF con Word (COM). Requiere Microsoft Word y pywin32.
Uso (tras `py pandoc/build_book.py`):  py pandoc/update_pdf.py
Si queda un WINWORD.EXE colgado tras exportar, el PDF ya está escrito: cerrar ese proceso.
"""
import os
import win32com.client as win32

HERE = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.normpath(os.path.join(HERE, "..", "manuscrito", "ICR - Manuscrito (nueva estructura).docx"))
PDF = DOCX[:-5] + ".pdf"

word = win32.DispatchEx("Word.Application"); word.Visible = False; word.DisplayAlerts = 0
try:
    doc = word.Documents.Open(DOCX, ReadOnly=False)
    doc.Fields.Update()
    for i in range(1, doc.TablesOfContents.Count + 1):
        doc.TablesOfContents(i).Update()
    doc.Fields.Update()
    doc.Save()
    doc.ExportAsFixedFormat(PDF, 17)          # 17 = wdExportFormatPDF
    pages = doc.ComputeStatistics(2)          # 2 = wdStatisticPages
    doc.Close(SaveChanges=True)
    print("PDF actualizado:", PDF, "| paginas:", pages)
finally:
    word.Quit()
