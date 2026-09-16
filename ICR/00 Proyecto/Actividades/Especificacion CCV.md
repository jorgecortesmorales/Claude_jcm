---
title: Estimar especificación alternativa con CCV (panel ampliado)
tipo: subactividad
fase: "Fase 1 - Estructura extractiva y encadenamientos"
estado: hecho
prioridad: media
mes_objetivo: "M8"
tags: [icr, subactividad, panel, econometria]
created: 2026-07-16
updated: 2026-09-05
---
Robustez C — hasta 320 observaciones (10 minerales × 32 años). Prueba de [[Hipotesis|H3]].

> **Rediseño 2026-07-23:** el CCV es un **descriptor** de captura de valor, no una especificación de panel.

## Avance 2026-09-05 (hecho, en su forma descriptiva)
- **CCV construido como serie anual mineral-año 1992-2025** (no como panel causal): `10 Datos/processed/ccv_serie.csv` (299 celdas con dato). `CCV = valor unitario de exportación en bruto E1 ÷ precio del producto de referencia USGS`. Método y caveats en [[Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)]]. Scripts `ccv_download.py` / `ccv_calc.py`.
