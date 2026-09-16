---
title: Calcular Leontief y Ghosh por mineral y corte
tipo: subactividad
fase: "Fase 1 - Estructura extractiva y encadenamientos"
estado: hecho
prioridad: alta
mes_objetivo: "M3-M6"
tags: [icr, subactividad, insumo-producto]
created: 2026-07-16
updated: 2026-09-05
---
Produce la variable dependiente principal del [[Modelo Econometrico|modelo de panel]]. Depende de obtener las MIP.

> **Rediseño 2026-07-23:** Ghosh/CCV se usan como **descriptores** del encadenamiento por mineral, no como variable dependiente de un panel.

## Avance (2026-09-05) — HECHO
- **Leontief (A, L) y Ghosh (B, G) por mineral** calculados sobre la MIP INEGI doméstica nivel Clase, cortes **2013 y 2018**, **validados contra INEGI a precisión de máquina** (`ctec`/`cdi`). Script `10 Datos/scripts/mip_calc.py`.
- **Corte de referencia 2008** añadido (no encadenado): `mip_encadenamientos_2008_referencia.csv`; validado 4.9e-15/1.6e-15. Scripts `mip2008_extract.py`/`mip2008_calc.py`.
- Salidas: `10 Datos/processed/mip_encadenamientos_minerales.csv` (+2008 aparte). Memoria: [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]].
