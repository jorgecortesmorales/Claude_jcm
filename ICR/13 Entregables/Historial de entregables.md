---
title: "Historial de entregables"
type: indice
tags: [icr, entregables, historial]
created: 2026-09-06
updated: 2026-09-28
---

# Historial de entregables

Cada entregable se archiva **fechado** en su subcarpeta (no se borran versiones previas). Para una versión nueva: subir la constante `FECHA` en el generador (donde exista) y volver a correr, o copiar el archivo más reciente a la fecha nueva y editar. Los `.dc.html`, `png_charts/`, `slide_svgs/`, `canvas.json` y los scripts quedan en la **raíz** de `13 Entregables/` como taller (no se versionan).

> [!done] Refresco 2026-09-08 (Paso 6.6): la comparación internacional pasó de **5 a 8 países** (se añadieron **China, Brasil y Perú**). Se regeneraron `intl_ghosh.png` y `dva.png` (8 países, corte 2018) y se propagó a: Resumen metodológico (§8/§9, md+**HTML**), **Resumen descriptivo docx 2026-09-08**, infografía §05, deck (slide Internacional), y ambas presentaciones del protocolo (HTML+**PDF**). Hallazgo estrella: **México (Ghosh 1.51) y China (1.53) casi idénticos, pero crudo 0.38 vs 0.07** — el Ghosh agregado engaña; **Perú (misma canasta que México) es el enclave más profundo (0.98)**.

> [!done] Refresco 2026-09-07: todos los entregables se actualizaron con lo nuevo (pasos 6, 6.5, 7, 8): HHI 1994-2024, comparación internacional (ICIO), DVA/reprocesamiento (enclave en dinero) y regionalización. Gráficos nuevos `intl_ghosh.png` y `dva.png` (+ HHI extendido). Ver también el nuevo **Resumen metodológico y de resultados 2026-09-07.md** (todos los indicadores con su matemática y resultados completos).

## 1. Resumen descriptivo
- **Carpeta**: `Resumenes descriptivos/`
- **Versión actual**: `Resumen descriptivo - datos e indicadores 2026-09-08.docx` (previas: 2026-09-07, 2026-09-05). **Nuevo 2026-09-08**: sección 6 «Comparación internacional» ampliada a **8 países** (China, Brasil, Perú añadidos con su justificación). Base (2026-09-07): Ghosh sector + DVA + regionalización; HHI 1994-2024; fuentes con OECD ICIO; guion del protocolo.
- **Generador**: `build_resumen_docx.py` (constante `FECHA`; usa `png_charts/` vía `gen_png_charts.py`)
- **Complemento (metodológico)**: `Resumenes descriptivos/Resumen metodológico y de resultados 2026-09-07.md` (nota del vault, editable en Obsidian) + **versión HTML autónoma** `…2026-09-07.html` (mismo contenido, matemática renderizada con MathJax, gráficos embebidos, callouts/tablas estilizados). Generador HTML: `build_resumen_metodologico_html.py` (convierte el .md; requiere `markdown` de Python; MathJax por CDN → necesita internet para renderizar la matemática). Los 8 indicadores con toda la matemática, fuentes/ubicación y TODOS los resultados.

## 2. Infografía (datos, interactiva)
- **Carpeta**: `Infografias/`
- **Versión actual**: `infografia_indicadores 2026-09-07.html` (previa: 2026-09-05). **Nuevo**: sección «05 · Comparación internacional y valor retenido» (barras estáticas Ghosh + DVA) y HHI 1994-2024.
- **Generador**: ninguno (HTML autónomo, se edita a mano; para versión nueva copiar a fecha nueva)
- **Artifact (versión previa)**: https://claude.ai/code/artifact/ea144363-0650-4784-8961-cfe71bf01f64 (republicar si se desea publicar la 2026-09-07)

## 3. Presentación de avances (protocolo)
- **Carpeta**: `Presentaciones de avances/`
- **Versión actual**: `presentacion_protocolo 2026-09-07.html` (+ **PDF** `presentacion_protocolo 2026-09-07.pdf`, 19 páginas landscape 13.33×7.5"; previa: 2026-09-05). **19 diapositivas**. **Nuevo**: diapositiva 2 menciona la **Ley Minera de 1992** (concesiones 50 años sin condicionar valor agregado; Sariego 2009, Delgado Wise y Del Pozo 2001); **marco teórico y brecha alineados a la literatura del PROTOCOLO** (Prebisch-Singer; Mason/Bain, Williamson/Klein, North, Gereffi/Kaplinsky-Morris, Antràs y Chor; Sariego, Delgado Wise, Azamar y Ponce, Aliphat) — se **retiraron** Cardoso-Faletto/Svampa (no están en el protocolo); **diapositiva 19 de Referencias** = bibliografía real del protocolo (4 grupos) + fuentes del avance; cobertura HHI 1994-2024, comparación internacional (3 cortes) y DVA; cierre con reencuadre nórdico. **Se quitaron** las menciones a cambios pendientes de aprobación del asesor.
  - **Dos variantes** (misma estructura, distinto marco teórico):
    - `presentacion_protocolo 2026-09-07.{html,pdf}` — **fiel al protocolo**: marco = estructuralismo (Prebisch) + organización industrial/CVG; sin enclave estructural.
    - `presentacion_protocolo (enclave estructural) 2026-09-07.{html,pdf}` — **estado actual de la tesis**: marco = del enclave clásico (Cardoso-Faletto) al **enclave estructural** (Svampa), con Prebisch y las herramientas analíticas como base; referencias incluyen Cardoso-Faletto y Svampa.
  - **Generador de PDF**: Chrome headless `--print-to-pdf` con `@media print` (una diapositiva por página, `@page 13.333in 7.5in`; 19 páginas). Requiere Chrome/Edge. El PDF se genera en scratchpad y se copia (Chrome no escribe directo en OneDrive); verificar el conteo con `pdfinfo` (no con `file`, que cuenta mal).
- **Generador**: ninguno (HTML autónomo, 18 diapositivas; para versión nueva copiar a fecha nueva)
- **Artifact (versión previa)**: https://claude.ai/code/artifact/b76e5f8e-d6cd-492a-8ed6-54fab720c29b

## 4. Presentación de la infografía (datos en formato presentación)
- **Carpeta**: `Presentaciones de infografia/`
- **Versión actual (deck autónomo)**: `presentacion_enclave 2026-09-07.html` — **10 diapositivas**: añade «09 · Internacional» (comparación Ghosh + DVA + nota de regionalización). Previas: `…2026-09-06.html` (9), `…2026-09-05.html` (8).
  - **Generador**: `build_deck.py` (constante `FECHA`; ensambla los `.dc.html`, incl. `Evolucion.dc.html` y la nueva `Internacional.dc.html` de `gen_internacional_slide.py`, que embebe los PNG como data-URI)
  - **Artifact (versión previa)**: https://claude.ai/code/artifact/9b3361d6-2cc7-4837-9ced-fb317523a3aa
- **Canvas Claude Design (editable)**: **NO reseeded en este refresco** (requiere Node + skill design + publicación). El deck autónomo 2026-09-07 cubre el mismo contenido actualizado; el canvas queda en su versión 2026-09-06 hasta un reseed dedicado.
- **Versión actual (canvas Claude Design, editable)**: `presentacion-enclave-estructural 2026-09-06.html` — **9 artboards, con evolución temporal**. Versión previa en historial: `…2026-09-05.html` (8 artboards).
  - **Archivos de trabajo del canvas**: `canvas_src/` (los 8 artboards base + `Evolucion.dc.html` en modo *nombres de archivo* generado con `gen_evolucion_slide.py --filenames`, + 3 PNG downsampled + `canvas.json` de 9 artboards). Reseed: `node "<skill design>/seed-canvas.mjs" --template <payload> --out <archivo>.html --title "Enclave estructural (presentacion)" --artboard …(los 9)… --image hhi_traj.png --image comercio_evo.png --image ghosh_cortes.png --canvas canvas.json`, luego publicar con `contract 0.1.31` y **sin** `capabilities` (conserva el guardado). Requiere Node.
  - **Artifact**: https://claude.ai/code/artifact/8c1c2e64-7f52-43c2-b05e-9a0d2e02e31f

## 5. Apoyos para explicar (2026-09-07 / 08)
- **Guion de la exposición**: `Resumenes descriptivos/Guion de la exposicion (desde diapo 2) 2026-09-08.docx` (generador `build_guion_docx.py`) — solo el guion hablado, en registro oral, desde la diapositiva 2 hasta la 19, con transiciones y más detalle en 3/7/8/10/16. ≤ 2 min por diapositiva (≈16-20 min en total). La diapositiva 7 asume la versión con enclave estructural (nota al inicio para la variante protocolo).
- **Guía de exposición**: `Resumenes descriptivos/Guia de exposicion - diapositivas 3,7,8,10,16 2026-09-07.docx` (generador `build_guia_diapositivas.py`) — para las diapositivas 3 (justificación/brecha), 7 (marco teórico, ambas versiones), 8 (enfoque y horizonte), 10 (técnicas) y 16 (cobertura). Cada una con: qué muestra · marco a fondo (autores, mecanismos, supuestos y críticas, más allá del proyecto) · cómo exponerla (guion) · preguntas probables del jurado con respuesta · errores a evitar.
- **Mapa conceptual (Canvas)**: `00 Proyecto/Mapa conceptual - columna vertebral (indicadores y enclave).canvas` — columna vertebral de la tesis (los 8 indicadores agrupados por objetivo → enclave estructural → tipología → bases de política). Se abre en Obsidian (Canvas).
- **Skill `explicar-icr`** (en `~/.claude/skills/explicar-icr/SKILL.md`): fija un formato de explicación para la tesis (qué es → intuición → matemática → datos/fuente → interpretación → caveats), anclado a las fuentes reales. Se activa sola al pedir explicar/aclarar cualquier tema de la ICR.

## 6. Consolidado de datos y cálculos (Excel) + auditoría de consistencia + cotejo de certificación (2026-09-28)
- **Carpeta**: `Consolidado datos y calculos/`
- **Libro maestro**: `Consolidado ICR - datos, calculos e indicadores.xlsx` — **31 hojas** (ampliado 2026-09-29 con HEM nacional, estatal, por eslabón e internacional): `00 Índice`, `01 Bases de datos` (inventario de las fuentes usadas), `02 Catálogo de calculos` (todos los indicadores con fórmula, insumos, script y CSV) y **23 hojas de indicadores** por bloque (HHI numeradores/serie, CCV, precios, peso del bloque, MIP nacional/eslabones/demanda intermedia, comercio posición/etapa/destinos, georref + HHI geográfico + Ghosh estatal/interestatal, ICIO comparación/DVA, cadena local + tipología, criticidad, **HEM nacional, estatal, por eslabón e internacional**). Reúne todo en un mismo sitio para consulta y para armar tablas propias.
- **Trazabilidad (fórmulas)**: columnas **verdes** = fórmula viva de Excel que recomputa el indicador desde sus insumos, con columna `dif`≈0 (el libro se auto-audita); columnas **naranjas** = resultado de inversión matricial (Leontief/Ghosh nacional/estatal/ICIO) validado contra INEGI (~1e-15), con su script y CSV.
- **Generador**: `gen_consolidado.py` (solo LEE `10 Datos/processed/`, no lo modifica). Regenerar: `py "13 Entregables/Consolidado datos y calculos/gen_consolidado.py"`.
- **Auditoría de consistencia (formato reproducible)**: `auditoria_consistencia.py` → `Auditoria de consistencia.html` (reporte autónomo para navegador) + `ledger_auditoria.csv` (tabla máquina-legible). Recomputa cada indicador desde los CSV y emite veredicto. **Dictamen 2026-09-29: 19 indicadores reproducidos exactos (PASA) · 8 inversiones matriciales validadas por script · 0 a revisar.** Correr: `py "13 Entregables/Consolidado datos y calculos/auditoria_consistencia.py"`.
- **Cotejo de certificación (manuscrito ↔ datos)**: `cotejo_certificacion.py` → `Cotejo de certificacion.html` + `cotejo_certificacion.csv`. Extrae los **45 cuadros y 33 ilustraciones** del manuscrito renderizado (`11 Redaccion/manuscrito/ICR - Manuscrito (nueva estructura).docx`) y confronta cada número impreso contra el CSV que lo origina (celda a celda en los anexos B.1/B.2/B.3; por-entidad en las tablas de cuerpo, incl. HEM VI.5/VI.7/VII.2/VIII.5/B.7-B.10 —HEM internacional con cortes 2008/2013/2018/2020—; las figuras por identidad de fuente vía sus `fig_*.py`). **Resultado 2026-09-29: 1 453 números confrontados, 1 453 coinciden, 0 difieren** (auditoría de consistencia: 19 PASA · 8 validados por script · 0 a revisar). Certifica que lo impreso en el manuscrito = la capa `processed/`. Correr: `py "13 Entregables/Consolidado datos y calculos/cotejo_certificacion.py"`.
- **Nota**: todo el paquete es una **reexposición/verificación** de lo ya calculado (solo lectura); no altera ningún dato, indicador ni capítulo. Alcance del cotejo: certifica manuscrito ↔ `processed/`; no re-verifica la extracción primaria (PDF CAMIMEX, USGS, Comtrade).

---
← [[Bitacora]] · [[Resumen descriptivo de la investigacion (datos e indicadores)]] · [[Mapa conceptual - columna vertebral (indicadores y enclave)]] · [[Catalogo de Bases de Datos]]
