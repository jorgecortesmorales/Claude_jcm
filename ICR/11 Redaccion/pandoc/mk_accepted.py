# -*- coding: utf-8 -*-
"""Construye 01-introduccion.md, 02-marco.md y 04-contexto.md a partir del
texto aceptado del manuscrito consolidado, reorganizando a la nueva estructura,
fusionando los insertos del 'Anexo — borradores' y limpiando el andamiaje."""
import re, os
HERE = os.path.dirname(os.path.abspath(__file__)); RED = os.path.dirname(HERE)
L = open(os.path.join(HERE, "consolidado_extraido.md"), encoding="utf-8").read().split("\n")

def find(pred, start=0):
    return next(i for i, l in enumerate(L) if pred(l) and i >= start)

def slice_between(a_pred, b_pred):
    a = find(a_pred); b = find(b_pred, a+1)
    return "\n".join(L[a+1:b])

def clean_scaffold(t):
    out = []
    for ln in t.split("\n"):
        s = ln.strip()
        if s.startswith("> *"): continue                      # notas "Qué es esto/Dónde va"
        if s.startswith("← "): continue                        # nav links
        if re.match(r"^\*\*A\.\d Cap", s): continue            # títulos de anexo
        if s == "**Borrador para integrar en el Cap. II**": continue
        if s.startswith("*Nota de integración"): continue
        out.append(ln)
    return "\n".join(out)

def remap_caps(t):
    ph = [("Capítulo VIII","\x01"),("Capítulo VII","\x02"),("Capítulo VI","\x03"),
          ("Capítulo V","\x04"),("Capítulo IV","\x05"),("Capítulo III","\x06"),
          ("Cap. VIII","\x11"),("Cap. VII","\x12"),("Cap. VI","\x13"),
          ("Cap. V","\x14"),("Cap. IV","\x15"),("Cap. III","\x16")]
    for a,b in ph: t = t.replace(a,b)
    back = {"\x01":"Capítulo IX","\x02":"Capítulo VII","\x03":"Capítulo VIII",
            "\x04":"Capítulo VI","\x05":"Capítulo V","\x06":"Capítulo IV",
            "\x11":"Cap. IX","\x12":"Cap. VII","\x13":"Cap. VIII",
            "\x14":"Cap. VI","\x15":"Cap. V","\x16":"Cap. IV"}
    for a,b in back.items(): t = t.replace(a,b)
    # "capítulos VI y VII" (minúscula) -> "VIII y VII"
    t = t.replace("capítulos VI y VII", "capítulos VIII y VII")
    return t

# ============ CAP I ============
capI = slice_between(lambda l: l.startswith("# Capítulo I. Introducción"),
                     lambda l: l.startswith("# Capítulo II."))
# reemplazar el párrafo de estructura (viejo 8 caps) por el nuevo (9 caps)
nueva_estructura = ("La tesis se organiza en nueve capítulos. El Capítulo I plantea el problema, "
 "las preguntas, los objetivos, las hipótesis descriptivas y la justificación del objeto. El "
 "Capítulo II desarrolla el marco conceptual y teórico —mineral crítico, criticidad por producto, "
 "enclave estructural, cadenas de valor globales e instituciones—. El Capítulo III expone el marco "
 "metodológico y analítico, reuniendo en un solo lugar todos los indicadores y su matemática. El "
 "Capítulo IV reconstruye el contexto histórico e institucional de la minería mexicana, incluida la "
 "reforma de 2023 y la referencia internacional. El Capítulo V documenta la estructura empresarial y "
 "la concentración por mineral; el Capítulo VI, los encadenamientos productivos; el Capítulo VII, la "
 "inserción en las cadenas de valor globales. El Capítulo VIII integra los hallazgos en una tipología "
 "de los mercados, y el Capítulo IX sintetiza y deriva las bases de una política industrial.")
capI = remap_caps(clean_scaffold(capI))
# la substitución va DESPUÉS del remapeo, para no desplazar los números ya correctos
capI = re.sub(r"## I\.1 Estructura de la tesis\n\n.*?\n\n## I\.2",
              f"## I.1 Estructura de la tesis\n\n{nueva_estructura}\n\n## I.2", capI, flags=re.S)
justif = """
## I.3 Justificación del objeto: el peso del bloque de diez minerales

La elección de los diez minerales —barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice y zinc— y su condición de críticos se argumentan conceptualmente en el Capítulo II (definición y criterios de selección). Aquí se justifica el objeto por su **peso económico**: cuánto representa el bloque en la economía y en el sector, y cómo se reparte ese peso entre los diez minerales. Ambas cifras acotan el alcance del estudio y muestran que describir estos diez equivale, en la práctica, a describir la minería metálica y no metálica mexicana de relevancia.

### I.3.1 El peso del bloque en la economía y en el sector

Aunque el conjunto aporta apenas alrededor del 0.7 % del producto interno bruto nacional (matriz insumo-producto de 2013 y 2018), concentra cerca del 60-65 % del PIB de la minería no petrolera y del 77 % de las exportaciones mineras del país. Su participación en las exportaciones totales no es estática: oscila entre 1.2 % (mínimo, 2002) y 5.5 % (máximo, 2011) siguiendo el ciclo internacional de precios de los metales (Ilustración {{fig:peso}}), rasgo de una economía primario-exportadora tomadora de precios.

![Ilustración {#fig:peso}: Participación del bloque de diez minerales en las exportaciones totales de México, 1992-2024. Fuente: cálculo propio con UN Comtrade y Banco Mundial.](figuras/i1_peso_exportaciones.png){width=95%}

El valor de la producción del bloque se multiplica por cerca de nueve entre 1992 y 2018 (por trece hasta 2022), en proporciones casi iguales de mayor volumen y precios más altos, con el empuje de los precios concentrado en el superciclo de 2004-2013. En contraste, el empleo del sector decrece —de 59 mil a 42 mil puestos entre 2013 y 2018— y no rebasa el 0.1 % del empleo nacional: es una actividad intensiva en capital y recurso, no en trabajo, lo que anticipa el diagnóstico de enclave.

### I.3.2 La composición del bloque: el peso de cada mineral

El peso del bloque está muy desigualmente repartido entre sus diez componentes (Cuadro {{cua:comp}}, Ilustración {{fig:comp}}). Cinco metales —cobre, oro, plata, zinc y plomo— concentran alrededor del 95 % del valor de producción y de las exportaciones del bloque; los cinco minerales industriales y no metálicos restantes —manganeso, fluorita, sílice, barita y grafito— suman en conjunto menos del 5 % del valor. Dentro del grupo dominante hay, además, un **desplazamiento histórico hacia los metales preciosos**: la participación del oro en el valor de producción del bloque pasó de cerca del 10 % en los años noventa a alrededor del 30 % en 2018-2022, mientras la del cobre descendió de más del 41 % a cerca del 30 %, y la plata se sostuvo en torno al 19 %.

Cuadro {#cua:comp}: Composición del bloque por mineral: participación en el valor de producción (años seleccionados) y en las exportaciones del bloque (2024). Fuente: cálculo propio con volúmenes USGS/CAMIMEX, precios USGS y UN Comtrade.

| Mineral | Valor 1995 | Valor 2005 | Valor 2018 | Export. 2024 |
|---|---:|---:|---:|---:|
| Cobre | 41.2 | 41.3 | 30.2 | 33.5 |
| Oro | 10.2 | 11.4 | 29.5 | 27.1 |
| Plata | 15.6 | 17.2 | 18.7 | 20.2 |
| Zinc | 18.1 | 17.0 | 13.1 | 5.3 |
| Plomo | 6.2 | 4.6 | 3.6 | 9.3 |
| Manganeso | 4.2 | 2.4 | 1.9 | 0.1 |
| Fluorita | 2.6 | 4.3 | 1.9 | 0.7 |
| Sílice | 0.7 | 1.3 | 0.9 | 0.1 |
| Barita | 0.4 | 0.4 | 0.2 | 0.1 |
| Grafito | 0.7 | 0.2 | 0.0 | 0.8 |

![Ilustración {#fig:comp}: Composición del valor de producción del bloque por mineral, 1992-2022. Fuente: cálculo propio con volúmenes USGS/CAMIMEX y precios USGS.](figuras/i2_composicion_bloque.png){width=100%}

Esta desigualdad es, en sí misma, parte de la justificación. Los cinco minerales de mayor peso económico dan cuenta de la relevancia macroeconómica del objeto; los cinco de menor peso se incorporan no por su magnitud, sino por su **criticidad estratégica** como insumos industriales —flúor y fluoropolímeros, vidrio y electrónica, acero, baterías, perforación— (Capítulo II). La selección combina así **peso económico y criticidad**, y esa dualidad es la que fija el corpus. El retrato no debilita la elección por el tamaño acotado del sector: la refuerza, pues el aporte de la investigación no reside en la magnitud del sector, sino en la caracterización de su inserción, mineral por mineral, en las cadenas de valor.
"""
frontI = ('---\ntitle: "Capítulo I. Introducción"\nchapter: "I"\nlang: es-ES\n---\n\n'
          '# Índice de cuadros\n\n{{LISTA_CUADROS}}\n\n'
          '# Índice de ilustraciones\n\n{{LISTA_FIGURAS}}\n\n# Capítulo I. Introducción\n\n')
open(os.path.join(RED,"manuscrito","01-introduccion.md"),"w",encoding="utf-8").write(
    frontI + capI.strip() + "\n" + justif)
print("01-introduccion.md ok")

# ============ CAP II ============
capII = slice_between(lambda l: l.startswith("# Capítulo II."),
                      lambda l: l.startswith("# Capítulo III."))
# inserto II.2.5 (A.2)
a2 = slice_between(lambda l: l.startswith("**A.2 Cap. II"),
                   lambda l: l.startswith("**A.3 Cap. VII"))
a2 = clean_scaffold(a2)
a2 = a2.replace("**II.2.5 La criticidad se concentra en productos y grados, no en el mineral**",
                "### II.2.5 La criticidad se concentra en productos y grados, no en el mineral")
a2 = a2.replace("**Cuadro II.x --- Producto de mayor criticidad por mineral y su base oficial**",
    "Cuadro {#cua:critII}: Producto de mayor criticidad por mineral y su base oficial. Escala: estratégico > crítico > medio > bajo. Fuente: USGS (2022, 2025), UE (CRMA, 2023) e IEA; clasificación en criticidad_productos.csv.")
# quitar la nota de escala duplicada al pie
a2 = re.sub(r"\*Escala de criticidad.*?criticidad_productos\.csv\.\*", "", a2, flags=re.S)
# insertar A.2 antes de "## II.3"
capII = capII.replace("## II.3 Factores que impulsan",
                      a2.strip() + "\n\n## II.3 Factores que impulsan", 1)
capII = remap_caps(clean_scaffold(capII))
frontII = ('---\ntitle: "Capítulo II. Marco conceptual y teórico"\nchapter: "II"\nlang: es-ES\n---\n\n'
           '# Índice de cuadros\n\n{{LISTA_CUADROS}}\n\n# Capítulo II. Marco conceptual y teórico\n\n')
open(os.path.join(RED,"manuscrito","02-marco.md"),"w",encoding="utf-8").write(
    frontII + capII.strip() + "\n\n## Fuentes y referencias\n")
print("02-marco.md ok")

# ============ CAP IV ============
capIII = slice_between(lambda l: l.startswith("# Capítulo III. La minería"),
                       lambda l: l.startswith("# Capítulo IV."))
# tomar solo III.1..III.5 (quitar III.6 reforma, se cubre con A.3)
cut = capIII.find("## III.6")
if cut > 0: capIII = capIII[:cut]
capIII = re.sub(r"^## III\.(\d) ", lambda m: f"## IV.{m.group(1)} ", capIII, flags=re.M)
# A.3 -> IV.6 ; A.4 -> IV.7
a3 = slice_between(lambda l: l.startswith("**A.3 Cap. VII"),
                   lambda l: l.startswith("**A.4 Cap. VII"))
a4 = slice_between(lambda l: l.startswith("**A.4 Cap. VII"),
                   lambda l: l.startswith("← Indice Impacto Reforma 2023 · Marco institucional"))
def conv(a, pref, titulo):
    a = clean_scaffold(a)
    # primer bold tras limpiar = título de sección, lo quitamos
    a = re.sub(r"^\*\*[^*]+\*\*\s*$", "", a, count=1, flags=re.M)
    a = re.sub(r"^\*\*(\d+)\.\s*(.+?)\*\*$", lambda m: f"### {pref}.{m.group(1)} {m.group(2)}", a, flags=re.M)
    a = re.sub(r"^\*\*Fuentes\*\*\s*$", f"**Fuentes ({titulo}):**", a, flags=re.M)
    return f"## {pref} {titulo}\n\n" + a.strip()
capIV = capIII.strip() + "\n\n" + conv(a3, "IV.6", "La reforma de 2023 y el marco institucional")
capIV += "\n\n" + conv(a4, "IV.7", "La referencia institucional internacional")
capIV = remap_caps(capIV)
frontIV = ('---\ntitle: "Capítulo IV. Contexto histórico e institucional de la minería mexicana"\nchapter: "IV"\nlang: es-ES\n---\n\n'
           '# Capítulo IV. Contexto histórico e institucional de la minería mexicana\n\n')
open(os.path.join(RED,"manuscrito","04-contexto.md"),"w",encoding="utf-8").write(
    frontIV + capIV.strip() + "\n\n## Fuentes y referencias\n")
print("04-contexto.md ok")
