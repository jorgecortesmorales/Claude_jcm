---
title: Construir serie histórica de HHI por mineral-año (1993-2025)
tipo: subactividad
fase: "Fase 1 - Estructura extractiva y encadenamientos"
estado: hecho
prioridad: alta
mes_objetivo: "M1-M4"
tags: [icr, subactividad, insumo-producto, hhi]
created: 2026-07-16
updated: 2026-09-05
---
A partir de series de participación de mercado (Cámara Minera de México, SGM). Ver estimaciones iniciales en [[Sintesis Comparativa]] y cifras cruzadas en [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]] (archivo 3, reservas y producción mundial).

## Avance 2026-07-21
- Numeradores en `10 Datos/processed/hhi_numeradores.csv` (493 filas, cobertura 2004-2024).
- Estructura de la industria por mineral-año extraída del USGS MYB (Tabla 2) a `10 Datos/processed/myb_estructura_industria.csv` (816 filas, 17 ediciones) — fuente para contar productores y fechar fusiones. Ver [[Bitacora]] 2026-07-21.
- **Fluorita recalculada** como duopolio 2004-2011 (HHI ≈6,525) → monopolio 2012+ (HHI 10,000), con la fecha de fusión corregida a enero 2012.
- **Pendientes**: (a) regla de participaciones >100%; (b) consolidar cobre por grupo (la desagregación USGS 2021-22 no es entrada de empresas); (c) resolver el doble conteo de Fresnillo plc en oro/plata desde 2015; (d) decidir el caso de contraste tras el hallazgo de que el grafito está concentrado (C-17 en [[Ediciones Pendientes Documentos Word]]); (e) numerador de sílice (falta desglose por empresa); (f) fluorita 2019-2020 sin participación.

## Avance 2026-09-05 (hecho)
- **HHI consolidado por mineral-año construido y cerrado, 2004-2023**: `10 Datos/processed/hhi_consolidado.csv`. Resueltos (b) cobre consolidado por grupo, (c) doble conteo oro/plata (se excluyen filas agregadas), (f) fluorita 2019-2020 (monopolio de grupo = 10,000). **2021-2023** con detalle por mina; **2004-2020** aproximado por participación de líder (se lee como **régimen**, no comparable en nivel). Cada fila etiquetada con su `metodo`. Detalle en [[Catalogo de Bases de Datos]] §13 y [[Bitacora]] (2026-08-01 y 2026-09-05).
