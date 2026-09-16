---
title: Obtener y depurar Matrices Insumo-Producto INEGI (2003-2023)
tipo: subactividad
fase: "Fase 1 - Estructura extractiva y encadenamientos"
estado: hecho
prioridad: alta
mes_objetivo: "M2-M4"
tags: [icr, subactividad, insumo-producto]
created: 2026-07-16
updated: 2026-07-30
---
Cortes 2003, 2008, 2012, 2018; actualización con método RAS a 2020/2023. Ver [[Indice Diagnostico Insumo-Producto|Índice Cap. V]] (05 Diagnostico Insumo-Producto/).

## Avance (2026-07-30)
- **Descarga OBTENIDA y validada**: MIP INEGI **2013** (base 2013) y **2018** (base 2018), datos abiertos CSV, en `10 Datos/Bases Originales/10 MIP INEGI/`. Son los dos únicos cortes publicados en formato abierto legible; **2003/2008/2012 no están** en datos abiertos (solo tabulador interactivo) y son de años base distintos → no comparables, se descartan salvo indicación.
- **Resolución confirmada — nivel Clase SCIAN (6 díg.), matriz producto×producto**: 8/10 minerales del corpus tienen **clase propia** (oro 212221, plata 212222, cobre 212231, manganeso 212291, sílice 212324, barita 212393, fluorita 212395, grafito 212396). **Plomo+zinc comparten una sola clase** (212232, coextracción) → los indicadores basados en MIP se reportan como "plomo-zinc" combinado. Misma resolución en 2013 y 2018.
- Archivos por variante: `t/d/m` (total/doméstica/importada), `ctec` (coef. técnicos = A, Leontief), `cdi` (directos+indirectos = inversa de Leontief). Ghosh se construye desde los flujos domésticos.
- **CÁLCULO COMPLETADO**: Leontief, Ghosh e índices Hirschman-Rasmussen normalizados + demanda intermedia doméstica por mineral, base doméstica, nivel Clase, 2013 y 2018. **Validado contra `ctec`/`cdi` de INEGI a precisión de máquina.** Salidas en `10 Datos/processed/mip_encadenamientos_minerales.csv` y `mip_demanda_intermedia_minerales.csv`; script `10 Datos/scripts/mip_calc.py`; método y hallazgos en [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]].
- **Pendiente (opcional, no bloquea Cap. V)**: actualización RAS 2020/2023 y matrices Chile/Australia (comparación internacional opcional en el diseño descriptivo).
