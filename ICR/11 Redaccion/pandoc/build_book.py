# -*- coding: utf-8 -*-
"""Ensambla los 9 capitulos en un unico manuscrito DOCX:
- numeracion corrida de cuadros/figuras por capitulo,
- portada institucional,
- indice general + de cuadros + de ilustraciones como CAMPOS de Word (paginados),
- bibliografia maestra unica (APA).
Uso: py pandoc/build_book.py
"""
import os, re, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); RED = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from build import preprocess, split_front_matter, meta_get, read  # reutiliza el preprocesador

PANDOC = os.environ.get("PANDOC_BIN", r"C:\Users\Jorge\AppData\Local\Pandoc\pandoc.exe")

CHAPTERS = ["01-introduccion","02-marco","03-metodologia","04-contexto",
            "05-estructura","06-encadenamientos","07-insercion-global",
            "08-tipologia","09-sintesis"]
ANNEXES = ["10-anexo-B","11-anexo-C","12-anexo-D"]

# --- conversion de las citas @ a texto (bibliografia unica al final) ---
CITE_BRACKET = {
    "[@dietzenbacher1997; @oosterhaven1988]": "(Dietzenbacher, 1997; Oosterhaven, 1988)",
    "[@millerblair2009]": "(Miller y Blair, 2009)",
    "[@dietzenbacher1997]": "(Dietzenbacher, 1997)",
}
CITE_NARR = {
    "@leontief1941":"Leontief (1941)","@ghosh1958":"Ghosh (1958)",
    "@rasmussen1956":"Rasmussen (1956)","@hirschman1958":"Hirschman (1958)",
    "@dietzenbacher1997":"Dietzenbacher (1997)","@millerblair2009":"Miller y Blair (2009)",
    "@oosterhaven1988":"Oosterhaven (1988)",
}
def decite(t):
    for a,b in CITE_BRACKET.items(): t = t.replace(a,b)
    for a,b in CITE_NARR.items(): t = t.replace(a,b)
    return t

def strip_chapter_frontmatter_indices(body):
    # quita los mini-indices por capitulo (van consolidados al frente)
    body = re.sub(r"# Índice de cuadros\s*\n+\{\{LISTA_CUADROS\}\}\s*\n+", "", body)
    body = re.sub(r"# Índice de ilustraciones\s*\n+\{\{LISTA_FIGURAS\}\}\s*\n+", "", body)
    # quita el encabezado vacio de cierre
    body = re.sub(r"\n#{2}\s*Fuentes y referencias\s*$", "\n", body)
    return body

# --- portada + preliminares (raw openxml para portada, saltos y campos) ---
def field(instr, placeholder):
    return ('```{=openxml}\n'
            '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
            f'<w:r><w:instrText xml:space="preserve"> {instr} </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r><w:t xml:space="preserve">{placeholder}</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>\n'
            '```\n')

def pagebreak():
    return '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'

def centered(txt, bold=False, size=None):
    rpr = ""
    if bold or size:
        rpr = "<w:rPr>" + ("<w:b/>" if bold else "") + (f'<w:sz w:val="{size*2}"/>' if size else "") + "</w:rPr>"
    return ('```{=openxml}\n'
            '<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="160"/></w:pPr>'
            f'<w:r>{rpr}<w:t xml:space="preserve">{txt}</w:t></w:r></w:p>\n```\n')

PORTADA = (
    centered("UNIVERSIDAD AUTÓNOMA METROPOLITANA", bold=True, size=13) +
    centered("Unidad Azcapotzalco", size=12) +
    centered("División de Ciencias Sociales y Humanidades", size=12) +
    centered("Maestría en Economía · Campo EFI", size=12) +
    centered("&#160;") + centered("&#160;") + centered("&#160;") +
    centered("Los mercados de los minerales críticos en México, 1992–2025:", bold=True, size=16) +
    centered("estructura extractiva, cadenas de valor y bases para una política industrial", bold=True, size=16) +
    centered("&#160;") + centered("&#160;") +
    centered("Idónea Comunicación de Resultados", size=12) +
    centered("&#160;") + centered("&#160;") + centered("&#160;") +
    centered("Jorge Cortés Morales", bold=True, size=13) +
    centered("Asesor: Dr. Jordy Micheli Thirion", size=12) +
    centered("&#160;") + centered("&#160;") + centered("&#160;") +
    centered("Ciudad de México · Septiembre de 2026", size=12) +
    pagebreak()
)

RESUMEN = (
    "# Resumen\n\n"
    "Esta investigación caracteriza los mercados de diez minerales críticos en México "
    "(barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice y zinc) entre 1992 y 2025, "
    "en sus eslabones extractivo e industrial, y describe la inserción del país en las cadenas de valor "
    "locales y globales. A partir de bases de datos e indicadores construidos y desagregados por mineral "
    "—concentración (HHI), encadenamientos de insumo-producto (Leontief, Ghosh, Hirschman-Rasmussen), "
    "coeficiente de captura de valor, comercio por etapa de procesamiento y comparación internacional con "
    "descomposición de valor agregado—, el trabajo documenta un patrón de **enclave estructural**: una minería "
    "concentrada y desarticulada de la transformación doméstica, cuya cadena se trunca en el metal refinado y "
    "cuya criticidad se concentra en los eslabones que el país no produce. El aporte central es la construcción "
    "de esos indicadores y su lectura conjunta como base para una discusión de política industrial.\n\n"
    "**Palabras clave:** minerales críticos, cadenas de valor, enclave estructural, encadenamientos, "
    "insumo-producto, política industrial, México.\n\n"
    + pagebreak() +
    "# Índice general\n\n" + field('TOC \\o "1-3" \\h \\z \\u',
        "Actualice este campo en Word (clic derecho → Actualizar campos, o F9) para generar el índice.") +
    pagebreak() +
    "# Índice de cuadros\n\n" + field('TOC \\h \\z \\t "Table Caption,1"',
        "Actualice los campos en Word (F9) para generar el índice de cuadros.") +
    pagebreak() +
    "# Índice de ilustraciones\n\n" + field('TOC \\h \\z \\t "Image Caption,1"',
        "Actualice los campos en Word (F9) para generar el índice de ilustraciones.") +
    pagebreak()
)

def bibliografia():
    txt = read(os.path.join(RED, "..", "12 Referencias", "Bibliografia.md"))
    _, body = split_front_matter(txt)
    # tomar desde la primera '## ' (secciones de fuentes)
    i = body.find("## Fuentes")
    body = body[i:] if i >= 0 else body
    return "# Referencias bibliográficas\n\n" + body.strip() + "\n"

# --- ensamblar ---
parts = [PORTADA, RESUMEN]
for name in CHAPTERS:
    text = read(os.path.join(RED, "manuscrito", name + ".md"))
    front, body = split_front_matter(text)
    chap = meta_get(front, "chapter", "X")
    body = strip_chapter_frontmatter_indices(body)
    body = decite(body)
    body_p, _, _ = preprocess(body, chap)
    parts.append(body_p.strip() + "\n\n" + pagebreak())
parts.append(bibliografia() + "\n\n" + pagebreak())
# anexos al final
for name in ANNEXES:
    text = read(os.path.join(RED, "manuscrito", name + ".md"))
    front, body = split_front_matter(text)
    chap = meta_get(front, "chapter", "X")
    body = strip_chapter_frontmatter_indices(decite(body))
    body_p, _, _ = preprocess(body, chap)
    parts.append(body_p.strip() + "\n\n" + pagebreak())

combined = "\n\n".join(parts)
tmp = os.path.join(RED, "_manuscrito_libro.md")
open(tmp, "w", encoding="utf-8").write(combined)

out = os.path.join(RED, "manuscrito", "ICR - Manuscrito (nueva estructura).docx")
cmd = [PANDOC, os.path.basename(tmp), "-o", out,
       "--reference-doc", os.path.join("pandoc", "reference.docx"),
       "--resource-path", RED,
       "-f", "markdown+pipe_tables+table_captions+implicit_figures+raw_attribute"]
r = subprocess.run(cmd, cwd=RED, capture_output=True, text=True)
sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
os.unlink(tmp)
print("\n[book] ->", out, "| rc", r.returncode)
