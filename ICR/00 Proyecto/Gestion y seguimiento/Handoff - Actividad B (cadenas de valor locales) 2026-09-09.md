---
title: "Handoff — Actividad B (construir las cadenas de valor locales) + estado al 2026-09-09"
type: handoff
tags: [icr, handoff, actividad-b, cadenas-de-valor]
created: 2026-09-09
updated: 2026-09-09
status: completado
---

> [!success] Ejecutado 2026-09-09
> Actividad B completada: 10 fichas de cadena en `05 Diagnóstico Insumo-Producto/Fichas de Cadena de Valor/` ([[Indice - Fichas de Cadena de Valor]]), datos `processed/cv_arbol_mineral.csv` · `cv_eslabones_cuantificado.csv` · `cv_tipologia.csv`, script `cv_build.py`, síntesis Fase 8 [[Sintesis - Patron agregado y bases de politica (cadenas de valor)]]. Ver [[Bitacora]] (2026-09-09).

# Handoff — Ejecutar la Actividad B (cadenas de valor locales) en un chat nuevo

> [!info] Por qué este handoff
> El chat anterior quedó largo tras cerrar varias tareas grandes (abajo). La **Actividad B** (construir las 10 cadenas de valor locales, 8 fases) es un trabajo extenso y conviene ejecutarlo con contexto limpio. Este documento es la **fuente única de verdad** para arrancar. Reglas de trabajo vigentes: trabajar solo dentro de `ICR/`, usar `py`, diseño **descriptivo**, concepto ordenador = **enclave estructural**, sin voz de IA, versionar entregables, **no aceptar el control de cambios del PROTOCOLO** (espera al asesor).

## 1. La tarea: Actividad B

**Guía completa y método paso a paso**: [[Ruta metodologica - Construccion de cadenas de valor locales por mineral]] (8 fases, ya diseñada y aprobada). Objetivo: para cada uno de los 10 minerales, construir su **cadena de valor local** (mapear eslabones L0-L4, cuantificarlos, ubicar dónde se detiene la cadena, clasificar en tipología A/B/C/D) e integrarla a la síntesis.

**Entregables nuevos que debe producir** (definidos en la Ruta):
1. `processed/cv_arbol_mineral.csv` (Fase 1: árbol de la cadena L1-L4 por mineral, con HS/SCIAN/coeficiente).
2. `empresas_transformacion.csv` ampliado a los eslabones L1-L4 (Fase 2).
3. `processed/cv_eslabones_cuantificado.csv` (Fase 3: volumen/valor/VA/empleo/X/M por eslabón).
4. `processed/cv_cierre_aguas_abajo.csv` (Fase 5: dónde se rompe la cadena + espejo + industria usuaria).
5. `processed/cv_tipologia.csv` + **10 fichas de cadena** (Fase 7) → alimentan Cap. VI y VIII.
6. Diagramas de cadena por mineral (SVG/Canvas) para entregables.

**Insumos ya construidos** (NO reconstruir — tabla en la Ruta §"Insumos ya disponibles"): concordancia HS/SCIAN, empresas de transformación (19 firmas), MIP encadenamientos + demanda intermedia por mineral, comercio por etapa, CCV, DVA, georreferenciación, y ahora peso del bloque + Ghosh estatal/inter-estatal.

**Arranque sugerido**: empezar por la Fase 1 (árbol de la cadena) con 1-2 minerales piloto (cobre y fluorita: uno tipo B truncado, uno tipo A integrado), validar el formato de ficha, y luego escalar a los 10.

## 2. Estado del proyecto (todo lo demás está hecho)

La **Ruta de indicadores** está completa: [[Ruta - Completar indicadores y series (seguimiento)]] (pasos 1-8, 6.5, 6.6, C2, +A, Actividades A/B-diseño). Lo cerrado en las últimas sesiones:

- **Paso 6.6** — comparación internacional a **8 países** (México, Chile, Australia, Finlandia, Suecia, **China, Brasil, Perú**); integrado a Caps VII/VIII y a todos los entregables. Hallazgo: México↔China Ghosh casi idéntico (1.51/1.53) pero crudo opuesto (0.38/0.07); Perú el enclave más profundo.
- **Actividad A (histórica)** — peso del bloque de 10 minerales en PIB/exportaciones/empleo/crecimiento, **1992-2024/2022**. Integrada a la **justificación** ([[Justificacion]] + inserto Word `11 Redaccion/Justificacion - peso del bloque (inserto Cap I) 2026-09-09.docx`). Hallazgos: peso en exportaciones oscila 1.2 %-5.5 % (pico 2011); producción ×9.4 (1992-2018) = volumen ×3.07 × precio ×3.06; oro 6 %→30 %, plata ~19 %; 4 metales = ~94 % del valor; bloque = ~0.7 % del PIB pero ~60-65 % de la minería no petrolera y ~77 % de exportaciones mineras. **Bug corregido**: plata/oro de `hhi_numeradores` están en *millones de onzas troy* (no toneladas) — el cotejo con USGS lo detectó; conversión corregida.
- **Hueco pre-2004 y 2019-2022 cerrados** — producción reconstruida de los **USGS MYB** (1992-2003 y 2019-2022; xls + lectura de imagen). Serie de producción continua **1992-2022**.
- **MIP nacional**: NO hay corte nuevo (sigue año base 2018).
- **Paso 8 numérico** — se descargó la **MIP Multi-Estatal 2018 de INEGI** (`Bases Originales/13 MIP Estatal INEGI/todos_2018.zip`, 398 MB). Ghosh de la minería **por estado** (`ghosh_estatal_mineria.csv`) e **inter-estatal** (`ghosh_interestatal_mineria.csv`). Hallazgo: el enclave real (exportación en bruto al extranjero) se concentra en **Chihuahua 76 %, Guerrero 59 %, Zacatecas 53 %**; buena parte de la "fuga" es **cadena metalúrgica nacional** (extractivos → fundición de Coahuila/SLP/NL). Memoria georref §3bis-3ter.

**Único pendiente del proyecto además de la Actividad B**: el control de cambios del **PROTOCOLO** (espera al asesor).

## 3. Archivos nuevos de esta sesión (para referencia)

**Scripts** (`10 Datos/scripts/`): `peso_bloque.py`, `peso_bloque_historico.py`, `myb_produccion_pre2004.py`, `build_justificacion_peso.py`, `ghosh_estatal.py`, `ghosh_interestatal.py`.
**Datos** (`10 Datos/processed/`): `peso_bloque_mineria.csv`, `peso_bloque_exportaciones.csv`, `peso_bloque_hist_exportaciones.csv`, `peso_bloque_hist_produccion.csv`, `produccion_nacional_myb_pre2004.csv`, `produccion_nacional_myb_2019_2022.csv`, `ghosh_estatal_mineria.csv`, `ghosh_interestatal_mineria.csv`.
**Gráficas** (`13 Entregables/png_charts/`): `peso_historico.png`, `ghosh_estatal.png`, `ghosh_interestatal.png` (+ `intl_ghosh.png`, `dva.png` actualizadas a 8 países).
**Memorias/notas**: [[Memoria - Peso del bloque de 10 minerales (PIB, exportaciones, empleo)]], [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]] (8 países), [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]] (§3bis-3ter), [[Justificacion]], [[Ruta metodologica - Construccion de cadenas de valor locales por mineral]]. Catálogo §18-22.

## 4. Notas técnicas / trampas conocidas
- `xlrd` ya instalado (para leer `.xls` viejos de USGS). `pandas`, `numpy`, `matplotlib`, `python-docx`, `markdown` disponibles. NO hay `python-pptx` ni Node.
- **USGS MYB**: `pdftotext` desalinea las tablas → leer Tabla 1 **como imagen** (`pdftoppm`), salvo 2002/2003 que tienen `.xls`. Ver [[usgs_myb_table2_notes]].
- **Unidades CAMIMEX** (`hhi_numeradores`): plata/oro en *millones de onzas* → convertir (1 M oz = 31.1035 t). Manganeso: usar contenido de Mn.
- **MIP estatal 2018**: matrices por estado `mip_ixi_e_<edo>_{intra,t,...}` (35 industrias); birregional `mip_ixi_br_<edo>_d` (2×35); minería = industria **21-2 (no petrolera)**. Multiestatal 1120×1120 disponible en el zip (para detalle estado-a-estado, no ejecutado).
- INEGI permite `curl` (a diferencia del WAF de la OCDE). El OECD ICIO pre-2011 se bajó manual.

← [[Home]] · [[Ruta - Completar indicadores y series (seguimiento)]] · [[Bitacora]]
