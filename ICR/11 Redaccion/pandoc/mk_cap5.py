# -*- coding: utf-8 -*-
"""Construye 05-estructura.md a partir del texto aceptado (viejo Cap. IV) del
manuscrito consolidado, renumerando IV->V y remapeando referencias cruzadas."""
import re, os, csv
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RED = os.path.dirname(HERE)
SRC = os.path.join(HERE, "consolidado_extraido.md")
PROC = os.path.normpath(os.path.join(RED, "..", "10 Datos", "processed"))

lines = open(SRC, encoding="utf-8").read().split("\n")
# slice viejo Cap IV: desde "# Capítulo IV. Estructura" hasta antes de "# Referencias"
start = next(i for i, l in enumerate(lines) if l.startswith("# Capítulo IV. Estructura"))
end = next(i for i, l in enumerate(lines) if l.startswith("# Referencias bibliográficas"))
body = lines[start+1:end]           # sin el H1 viejo
txt = "\n".join(body)

# (los '---' de texto los convierte pandoc a raya automáticamente; NO tocarlos
#  para no romper las tablas grid del origen)

# --- caja de 1 celda (manganeso) -> blockquote ---
txt = re.sub(r"\+[-=+]{5,}.*?\+\n\n", "", txt, flags=re.S, count=0)  # limpia bordes sueltos si quedan
txt = re.sub(
    r"\|\s*\*\*Dato confirmado por fuentes oficiales\*\*.*?Autlán, 2024\)\.\s*\|",
    "", txt, flags=re.S)
# insertar blockquote limpio donde iba la caja (tras IV.6.2)
caja = ("> **Dato confirmado por fuentes oficiales.** El Servicio Geológico Mexicano "
        "y la Secretaría de Economía documentan en sus perfiles de mercado más recientes "
        "que «el único productor mexicano de manganeso es la Cía. Minera Autlán», situación "
        "que se mantiene sin cambios desde la privatización de 1993 hasta la actualidad "
        "(2024-2025) (Servicio Geológico Mexicano, 2024).")
# quitar restos de la tabla grid de una sola celda
txt = re.sub(r"^\s*\+[-=+]{10,}\+\s*$", "", txt, flags=re.M)
txt = re.sub(r"^\s*\|\s*\*\*Dato confirmado.*$", caja, txt, flags=re.M)
txt = re.sub(r"^\s*\|\s*El Servicio Geológico Mexicano.*$", "", txt, flags=re.M)
txt = re.sub(r"^\s*\|\s*$", "", txt, flags=re.M)

# --- renumerar encabezados IV -> V ---
def h_min(m):   return f"## V.{m.group(1)} {m.group(2)}"
def h_sub(m):   return f"### V.{m.group(1)}.{m.group(2)} {m.group(3)}"
def h_one(m):   return f"## V.{m.group(1)} {m.group(2)}"
txt = re.sub(r"^## IV\.(\d+)\.(\d+) (.+)$", h_sub, txt, flags=re.M)
txt = re.sub(r"^# IV\.(\d+) (.+)$", h_min, txt, flags=re.M)
txt = re.sub(r"^## IV\.(\d+) (.+)$", h_one, txt, flags=re.M)

# --- suavizar frase causal del intro ---
txt = txt.replace(
    "antes de estimar la relación estadística entre HHI y encadenamientos productivos en el Capítulo VI",
    "antes de describir la relación entre la concentración de mercado (HHI) y los encadenamientos productivos (Capítulo VI)")

# --- remapeo de referencias a capítulos (viejo -> nuevo), sin cascada ---
# III->IV, IV->V, V->VI, VI->VIII, VII->VII, VIII->IX
ph = [("Capítulo VIII","\x01"),("Capítulo VII","\x02"),("Capítulo VI","\x03"),
      ("Capítulo V","\x04"),("Capítulo IV","\x05"),("Capítulo III","\x06")]
for a,b in ph: txt = txt.replace(a,b)
# refs internas a secciones IV.n -> V.n (ya no queda 'Capítulo IV' literal)
txt = re.sub(r"\bIV\.(\d)", r"V.\1", txt)
back = {"\x01":"Capítulo IX","\x02":"Capítulo VII","\x03":"Capítulo VIII",
        "\x04":"Capítulo VI","\x05":"Capítulo V","\x06":"Capítulo IV"}
for a,b in back.items(): txt = txt.replace(a,b)

# --- cuadro cuantitativo de HHI (todos los minerales, años clave) ---
D = defaultdict(dict); LID = {}
with open(os.path.join(PROC, "hhi_consolidado.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        try: D[r["mineral"]][int(r["anio"])] = float(r["hhi"])
        except Exception: pass
        if r.get("lider"): LID[r["mineral"]] = r["lider"]
NOM = {"manganeso":"Manganeso","fluorita":"Fluorita","grafito":"Grafito","silice":"Sílice",
       "cobre":"Cobre","barita":"Barita","plomo":"Plomo","zinc":"Zinc","plata":"Plata","oro":"Oro"}
def val(m, y):
    s = D[m]
    if y in s: return f"{s[y]:.0f}"
    # más cercano <= y
    cand = [yy for yy in s if yy <= y]
    return f"{s[max(cand)]:.0f}*" if cand else "·"
orden = sorted(NOM, key=lambda m: -max(D[m].values()))
filas = []
for m in orden:
    ult = max(D[m]);
    filas.append(f"| {NOM[m]} | {val(m,2004)} | {val(m,2012)} | {val(m,2018)} | {D[m][ult]:.0f} ({ult}) | {LID.get(m,'—')} |")
cuadro = ("Cuadro {#cua:hhi}: Índice HHI de la producción por mineral, años seleccionados. "
          "El valor 2004-2020 es aproximado (reconstruido por régimen de mercado; cota inferior) y "
          "no es estrictamente comparable en nivel con 2021-2024 (por mina). * = dato del año previo "
          "más cercano. Fuente: cálculo propio con base B5 (CAMIMEX y USGS).\n\n"
          "| Mineral | 2004 | 2012 | 2018 | Reciente | Líder |\n"
          "|---|---:|---:|---:|---:|---|\n" + "\n".join(filas))

# --- bloque de HHI (figuras + cuadro), se inserta al inicio de V.12 ---
hhi_block = f"""
La síntesis cuantitativa de la estructura extractiva es el índice HHI por mineral, cuya definición y cautelas de comparabilidad se exponen en el Capítulo III (III.4). La Ilustración {{{{fig:hhiesp}}}} ordena los diez mercados por su concentración reciente y la Ilustración {{{{fig:hhievo}}}} muestra su evolución; el Cuadro {{{{cua:hhi}}}} reúne los valores.

![Ilustración {{#fig:hhiesp}}: Índice HHI de la producción por mineral (año más reciente con dato). En rojo, concentración alta (HHI ≥ 2 500); en azul, moderada; en gris, baja. Fuente: cálculo propio, base B5 (CAMIMEX y USGS).](figuras/v1_hhi_mineral.png){{width=90%}}

![Ilustración {{#fig:hhievo}}: Evolución del índice HHI de minerales seleccionados, 2004-2024. El tramo 2004-2020 es aproximado (por régimen); 2021-2024, por mina. Fuente: cálculo propio, base B5.](figuras/v2_hhi_evolucion.png){{width=95%}}

{cuadro}

"""

# insertar el bloque justo después del encabezado V.12 y su primer párrafo
txt = txt.replace(
    "## V.12 Síntesis comparativa de la estructura empresarial",
    "## V.12 Síntesis comparativa de la estructura empresarial\n" + hhi_block, 1)

front = """---
title: "Capítulo V. Estructura empresarial y de mercado de los diez minerales críticos, 1993–2025"
chapter: "V"
lang: es-ES
---

# Índice de cuadros

{{LISTA_CUADROS}}

# Índice de ilustraciones

{{LISTA_FIGURAS}}

# Capítulo V. Estructura empresarial y de mercado de los diez minerales críticos, 1993–2025

"""

out = front + txt.strip() + "\n\n## Fuentes y referencias\n"
open(os.path.join(RED, "manuscrito", "05-estructura.md"), "w", encoding="utf-8").write(out)
print("05-estructura.md escrito:", len(out), "chars")
