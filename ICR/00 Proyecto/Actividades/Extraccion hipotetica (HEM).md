---
title: Calcular la extracción hipotética (HEM) — segunda variante del encadenamiento
tipo: subactividad
fase: "Fase 1 - Estructura extractiva y encadenamientos"
estado: hecho
prioridad: media
mes_objetivo: "M3"
tags: [icr, subactividad, insumo-producto]
created: 2026-09-29
updated: 2026-09-29
---
Método de extracción hipotética (Miller y Lahr, 2001, casos 3 y 4), incorporado a partir de Morales-López (2023) como **segunda variante** del encadenamiento hacia adelante: mide el **peso económico** (% del VBP que se perdería al extraer el sector), frente a la **intensidad** del Ghosh-Rasmussen.

## Avance (2026-09-29) — HECHO
- Por mineral, 2013/2018: `mip_hem_minerales.csv` (`mip_hem.py`).
- Por eslabón L1/L2/L3, 2013/2018: `mip_hem_eslabones.csv` (`mip_hem_eslabones.py`).
- Por entidad (MIP birregional 2018): `hem_estatal_mineria.csv` (`hem_estatal.py`).
- Por país (OECD ICIO, 2008/2013/2018/2020): `icio_hem_mineria.csv` (`icio_hem.py`).
- Validación: Sherman-Morrison vs extracción por fuerza bruta a ≤2.3e-14.
- Manuscrito: §III.2 (ecs. 9-10), §VI.4.1, §VI.8, §VII.4.1, §VIII.7.3; Anexo B.7-B.10. Lectura descriptiva; Rasmussen y HEM por separado y en conjunto.
