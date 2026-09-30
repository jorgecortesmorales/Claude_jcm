---
title: "Handoff — Estado actual (HEM, consolidado y certificación) 2026-09-29"
type: handoff
tags: [icr, handoff, estado, hem, consolidado, certificacion, manuscrito]
created: 2026-09-29
updated: 2026-09-30
status: activo
---

# Handoff — arrancar un chat nuevo (ICR minerales críticos)

> [!info] Qué es esto
> Fuente única de verdad para continuar la tesis en un chat con contexto limpio. **Reemplaza** a [[Handoff - Manuscrito reestructurado (9 caps + anexos) 2026-09-16]]. **No confundir** con el otro proyecto (ICR de Diana, vivienda Colombia, en `ICR DIANA/`, fuera de git).

## 0. Reglas de trabajo (vigentes)
- Trabajar **solo dentro de `ICR/`**; usar `py` (no `python`); skills de Obsidian para `.md`/`.canvas`/`.base`.
- **Diseño descriptivo**, no causal. Concepto ordenador = **enclave estructural**. HHI, Ghosh, HEM, CCV son **descriptores**.
- **Pauta de redacción del alumno (2026-09-29):** la interpretación de resultados es **solo descriptiva** —describir y analizar resultados, **sin implicaciones ni búsqueda de relaciones**—. **Excepción:** los dos coeficientes de Ghosh (**Rasmussen** = intensidad; **HEM** = peso) se interpretan **por separado y en conjunto**.
- **Estilo matemático (Cap. III):** el de **Morales-López (2023)** — ecuaciones **numeradas (1)-(13)**, glosario "donde X es … de orden n×1" tras cada ecuación, identidad contable dual primero, referencias por número de ecuación. En Pandoc la numeración se escribe `$$ … \qquad\qquad (n)$$` (Pandoc→Word **ignora** `\tag`).
- **Referencias cruzadas del manuscrito:** escribir `{{cua:X}}` / `{{fig:X}}` **solos** (ya se expanden a "Cuadro N.M" / "Ilustración N.M"); nunca "Cuadro {{cua:X}}" ni "Ilustración {{fig:X}}" (producían "Cuadro Cuadro" e "Ilustración Ilustración"; ambos corregidos 2026-09-29).
- **Sin voz de IA**; versionar en git; handoff antes de agotar contexto.
- **No aceptar el control de cambios del PROTOCOLO** — espera al asesor (Dr. Jordy Micheli Thirion).
- Git: rama `main`, remoto `git@github.com:jorgecortesmorales/Claude_jcm.git`. Todo pusheado al cierre de este handoff (ver `git log`). El DOCX del manuscrito está en `.gitignore` y el PDF no se versiona (ambos se regeneran).

## 1. Estado actual

**Manuscrito** — `11 Redaccion/manuscrito/ICR - Manuscrito (nueva estructura).docx` (+ PDF, 178 pp.):
- 9 capítulos + Anexos B/C/D; **52 cuadros, 33 ilustraciones** (todos numerados y referenciados desde 2026-09-30), índices como campos de Word, citas y bibliografía APA, **0 referencias rotas**.
- Fuentes en `11 Redaccion/manuscrito/*.md`; figuras en `11 Redaccion/figuras/` (`fig_*.py`).

**Novedades desde el handoff del 2026-09-16:**
1. **Consolidado de datos y cálculos** (`13 Entregables/Consolidado datos y calculos/`): Excel de **31 hojas** con fórmulas vivas (`gen_consolidado.py`), **auditoría de consistencia** (`auditoria_consistencia.py`: 19 PASA · 8 validados por script · 0 a revisar) y **cotejo de certificación manuscrito↔datos** (`cotejo_certificacion.py`: 45 cuadros, **1 453 números, 1 453 coinciden, 0 difieren**).
2. **Extracción hipotética (HEM)** — Miller y Lahr (2001) casos 3/4, método de **Morales-López (2023)** — como segunda variante del encadenamiento hacia adelante, validada por Sherman-Morrison vs fuerza bruta (≤2.3e-14):

   | Nivel | Script → CSV | Manuscrito |
   |---|---|---|
   | Por mineral (2013/2018) | `mip_hem.py` → `mip_hem_minerales.csv` | §III.2 (ecs. 9-10), §VI.8 (Cuadro VI.7, Ilustr. VI.6), Anexo B.7 |
   | Por eslabón L1/L2/L3 (2013/2018) | `mip_hem_eslabones.py` → `mip_hem_eslabones.csv` | §VI.4.1 (Cuadro VI.5, Ilustr. VI.4), Anexo B.9 |
   | Por entidad (birregional 2018) | `hem_estatal.py` → `hem_estatal_mineria.csv` | §VIII.7.3 (Cuadro VIII.5, Ilustr. VIII.6), Anexo B.8 |
   | Por país (ICIO 2008/2013/2018/2020) | `icio_hem.py <SML.csv> <año>` → `icio_hem_mineria.csv` | §VII.4.1 (Cuadro VII.2, Ilustr. VII.4), Anexo B.10 |

   Resultado central (descriptivo): el HEM ordena de forma casi inversa al Rasmussen — nacional: cobre/oro/plata encabezan el peso, sílice/grafito/manganeso la intensidad; internacional 2018: Chile 6.74 %, Australia 5.23 %, Perú 4.49 % en peso, México 1.44 % (pero Rasmussen 1.51).
3. **Redacción matemática del Cap. III** homologada a Morales-López (ecuaciones numeradas 1-13).
4. **Referencias nuevas**: Morales-López (2023), Miller y Lahr (2001), Dietzenbacher y Van der Linden (1997) — en `pandoc/references.bib`, `12 Referencias/Bibliografia.md` y el mapa de citas de `pandoc/build_book.py`.
5. Cuadro III.2 (síntesis de indicadores), Anexo D y Cuadro IX.2 (vacíos) y la síntesis (VI.9, IX) ya incluyen el HEM.
6. **Pauta descriptiva aplicada (2026-09-30)** a los pasajes que interpretaban cálculos en V.12.1, VI.2-VI.7, VI.9, VII.2-VII.8, VIII.2, VIII.5-VIII.8, IX.1 y IX.2; dos inconsistencias de HHI corregidas (sílice en la ilustración del plano; fluorita 2004). Detalle en [[Bitacora]] (2026-09-30). **No se tocaron** y quedan a decisión del alumno: IX.3-IX.4 (bases de política), dos frases de método en §III.2 y §III.7, la columna «Lectura» del cuadro del CCV y V.2-V.11.
7. **Cuadros sin número (2026-09-30)**: siete cuadros no tenían pie ni número (Cap. II espectro de concentración; Cap. IV contraste institucional; Cap. V cobre-Grupo México, oro top-5, plata por eslabón, zinc por líder y síntesis comparativa) y II.2.5 decía «Cuadro II.x». Corregidos; la numeración de los cuadros del Cap. V se recorre (el HHI pasa de V.1 a V.5) y el cotejo se re-apuntó. Detalle y conflictos pendientes en [[Bitacora]] (2026-09-30 b).

## 2. Cómo regenerar todo (orden)
Desde `ICR/`:
```
py "10 Datos/scripts/mip_hem.py"                 # (solo si cambian las MIP)
py "10 Datos/scripts/mip_hem_eslabones.py"
py "10 Datos/scripts/hem_estatal.py"
py "10 Datos/scripts/icio_hem.py" <AAAA_SML.csv> <año>   # requiere los zips ICIO (ver abajo)
cd "11 Redaccion" && py figuras/fig_cap6.py && py figuras/fig_hem_eslabones.py && py figuras/fig_hem_internacional.py && py figuras/fig_cap8_hem.py
py pandoc/build_book.py && py pandoc/update_pdf.py   # DOCX + índices + PDF (Word)
cd .. && py "13 Entregables/Consolidado datos y calculos/gen_consolidado.py"
py "13 Entregables/Consolidado datos y calculos/auditoria_consistencia.py"
py "13 Entregables/Consolidado datos y calculos/cotejo_certificacion.py"   # debe dar 0 difieren
```
- **ICIO**: los CSV completos no se conservan. Los zips de la edición 2023 están en `C:\Users\Jorge\Downloads\` (`2006-2010_SML.zip`, `2011-2015_SML.zip`; el de 2016-2020 se descarga con la URL del README de ICIO). Procedencia: `10 Datos/Bases Originales/12 OECD ICIO/README - OECD ICIO 2023 (procedencia).md`.
- **Cotejo**: los cuadros documentales (II.1, IV.1, V.1-V.4, V.6) están registrados como «fuentes documentales» en el diccionario `CUALI` del script. Si se inserta un cuadro nuevo, la numeración de los siguientes se recorre; los cuadros HEM se localizan por texto del caption, pero los demás por número → re-apuntar tras recompilar.
- **Word**: si `update_pdf.py` deja un `WINWORD.EXE` colgado, el PDF ya está escrito; cerrar ese proceso.

## 3. Qué sigue (todo opcional salvo 1)
1. **Versión de entrega del alumno** (voz propia) de los Caps. **III y V-IX** (+ §II.2.5). La versión base ya sigue la pauta descriptiva (2026-09-30); sigue la primera revisión del alumno. Guía de lecturas: [[Recomendaciones de lectura por capitulo]].
2. **Protocolo**: control de cambios en espera del asesor (no aceptar antes).
3. ~~Entregables sin HEM~~ → **hecho 2026-09-29 (d)**: todos los entregables tienen versión 2026-09-29 con el HEM (ver [[Historial de entregables]]). Queda: (i) las secciones anteriores de esos entregables conservan su redacción interpretativa previa (solo lo nuevo sigue la pauta descriptiva); alinearlas si se van a presentar. (ii) El cotejo certifica **números**, no afirmaciones de dirección u orden («supera», «en todos»); al preparar los entregables se encontraron y corrigieron cuatro de ese tipo, así que conviene revisarlas a mano en cada texto nuevo. (iii) El canvas de Claude Design sigue en 2026-09-06 (requiere Node).
4. **Bibliografía**: migrar [[Bibliografia]] a Zotero → `.bib` gestionado.
5. **Agenda de datos** (Cap. IX): HHI 1994-2003 con USGS histórico; cocientes de localización por entidad; desagregar la comparación internacional por mineral si el dato lo permite.

## 4. Para orientarte al arrancar
- Estado y avance: [[Estructura y Cronograma de la ICR]] · [[Tablero de Actividades]] · [[Bitacora]] (entradas 2026-09-28 y 2026-09-29).
- Mapa: [[Mapa del Proyecto]] · [[Home]] · [[Arquitectura del documento (estructura expositiva)]] (rige el manuscrito).
- Indicadores: [[Auditoria de indicadores (justificacion, matematica, limites)]] · [[Catalogo de Bases de Datos]] · [[Diccionario de Variables]] · [[Indice Diagnostico Insumo-Producto]].
- Arranque en chat nuevo: [[Mensaje de arranque - nuevo chat 2026-09-29]].

← [[Home]] · [[Mapa del Proyecto]] · [[Bitacora]] · [[Estructura y Cronograma de la ICR]]
