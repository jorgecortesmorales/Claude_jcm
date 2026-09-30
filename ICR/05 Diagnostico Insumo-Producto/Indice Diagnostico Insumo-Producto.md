---
title: Índice — Diagnóstico Insumo-Producto
type: resultados
tags: [icr, insumo-producto, indice]
created: 2026-07-16
updated: 2026-09-29
status: vigente
---

# Índice — Diagnóstico insumo-producto (encadenamientos)

Carpeta de **memorias de cálculo** de los encadenamientos productivos. En el manuscrito (estructura de 9 capítulos) el método vive en el **Cap. III** (§III.2-III.3, III.8-III.9; ecuaciones numeradas 1-10) y los resultados en los **Caps. VI, VII y VIII**; las series completas en el **Anexo B**. Diseño descriptivo: los coeficientes son descriptores, no variables de un modelo causal.

## Dos variantes del encadenamiento hacia adelante
- **Intensidad — Ghosh-Rasmussen** (media de la economía = 1): cuán articulado está un sector por unidad de producto.
- **Peso — extracción hipotética (HEM)** (Miller y Lahr, 2001; método de Morales-López, 2023): % del VBP que se perdería al extraer las compras o ventas del sector.
- Pauta de lectura (del alumno): interpretación **descriptiva**; los dos coeficientes se leen **por separado y en conjunto**.

## Memorias
| Memoria | Qué contiene | Manuscrito | Datos |
|---|---|---|---|
| [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] | Leontief, Ghosh, Rasmussen y demanda intermedia por mineral (2013/2018 + 2008 ref.); **§9 HEM por mineral** | §VI.2-VI.3, VI.7, **VI.8** | `mip_encadenamientos_minerales`, `mip_demanda_intermedia_minerales`, `mip_hem_minerales` |
| [[Memoria - Encadenamientos por eslabon (extraccion, refinacion, semimanufactura)]] | Ghosh por eslabón L1/L2/L3 (nacional, estatal, internacional); **§4 HEM por eslabón** | §VI.4, **VI.4.1**, VII | `mip_encadenamientos_eslabones`, `mip_hem_eslabones`, `icio_eslabones_metal` |
| [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]] | Ghosh por país (8 países, OECD ICIO), DVA/crudo_share; **§5bis HEM por país 2008-2020** | §VII.4, **VII.4.1**, VII.5 | `icio_comparacion_mineria`, `icio_dva_mineria`, `icio_hem_mineria` |
| [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]] | Extracción por estado, nodos, destinos; Ghosh estatal e interestatal; **§3quater HEM estatal** | §VIII.7 (incl. **VIII.7.3**) | `georref_*`, `ghosh_estatal_mineria`, `ghosh_interestatal_mineria`, `hem_estatal_mineria` |
| [[Memoria - Peso del bloque de 10 minerales (PIB, exportaciones, empleo)]] | Relevancia económica del bloque | §I | `peso_bloque_*` |
| [[Indice - Fichas de Cadena de Valor]] | 10 fichas L0-L4 (incluyen Rasmussen y HEM 2018 en su §4) | Cap. VIII, Anexo C | `cv_*` |

## Verificación
- Matemática y validación de cada indicador: [[Auditoria de indicadores (justificacion, matematica, limites)]] (§2.1-2.7, 6, 7.1-7.3).
- Reproducción y cotejo manuscrito ↔ datos: `13 Entregables/Consolidado datos y calculos/` (ver [[Historial de entregables]] §6).

← [[Home]] · [[Catalogo de Bases de Datos]] · [[Arquitectura del documento (estructura expositiva)]]
