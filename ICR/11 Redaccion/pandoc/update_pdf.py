# -*- coding: utf-8 -*-
"""Actualiza los campos (índices TOC de contenido, cuadros e ilustraciones) del manuscrito
y reexporta el PDF con Word (COM). Requiere Microsoft Word y pywin32.
Uso (tras `py pandoc/build_book.py`):  py pandoc/update_pdf.py
Reintenta las llamadas que Word rechaza por estar ocupado. Si aun así queda un WINWORD.EXE colgado, cerrarlo.
"""
import os
import win32com.client as win32

HERE = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.normpath(os.path.join(HERE, "..", "manuscrito", "ICR - Manuscrito (nueva estructura).docx"))
PDF = DOCX[:-5] + ".pdf"

import time
import pywintypes

def com(fn, *a, intentos=60):
    """Reintenta mientras Word rechaza la llamada por estar ocupado (RPC_E_CALL_REJECTED)."""
    for _ in range(intentos):
        try:
            return fn(*a)
        except pywintypes.com_error as e:
            if e.args[0] != -2147418111:
                raise
            time.sleep(2)
    return fn(*a)

word = win32.DispatchEx("Word.Application"); word.Visible = False; word.DisplayAlerts = 0
try:
    doc = com(word.Documents.Open, DOCX, False, False)   # (archivo, ConfirmConversions, ReadOnly)
    com(doc.Fields.Update)
    for i in range(1, com(lambda: doc.TablesOfContents.Count) + 1):
        com(lambda: doc.TablesOfContents(i).Update())
    com(doc.Fields.Update)
    com(doc.Save)
    com(doc.ExportAsFixedFormat, PDF, 17)     # 17 = wdExportFormatPDF
    pages = com(doc.ComputeStatistics, 2)     # 2 = wdStatisticPages
    com(doc.Close, 0)                         # ya guardado: cerrar sin volver a guardar
    print("PDF actualizado:", PDF, "| paginas:", pages)
finally:
    com(word.Quit, 0)
