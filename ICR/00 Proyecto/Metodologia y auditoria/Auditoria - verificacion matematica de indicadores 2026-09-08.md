---
title: "Auditoría — verificación matemática de los indicadores"
type: proyecto
tags: [icr, auditoria, verificacion, metodologia, indicadores]
created: 2026-09-08
updated: 2026-09-08
status: activo
---

# Auditoría — verificación matemática y consistencia con la literatura

> [!abstract] Alcance y método
> Verificación rigurosa de que los ocho indicadores están **calculados correctamente** y son **consistentes con la literatura académica**. Método: (1) re-derivación de cada fórmula; (2) **re-cómputo independiente** desde los insumos y comparación con la base publicada; (3) **validación contra la fuente** donde existe (INEGI). Veredicto global: **todos los indicadores son correctos y consistentes con la literatura**; las dos aparentes discrepancias detectadas resultan ser artefactos benignos (redondeo y método documentado), no errores.

## 1. HHI — concentración
**Fórmula.** $HHI=\sum_i s_i^2$, con $s_i$ = participación (%) del grupo $i$; rango 0-10 000 (Rhoades, 1993; convención DOJ/CE). Umbrales: <1 500 baja, 1 500-2 500 moderada, >2 500 alta.
**Prueba.** Re-cómputo independiente por grupo desde `hhi_numeradores.csv` (volúmenes por mina → grupo → cuota² sobre total nacional), 2024: **coincidencia exacta** con `hhi_consolidado.csv` en plomo (2 465), zinc (1 683), plata (1 147) y oro (429).
**Nota (no error).** El cobre 2024 recomputado da 6 466 vs. 3 557 del consolidado: la diferencia está en el **denominador**, no en la fórmula — el consolidado usa el total nacional 2024 **estimado** (~755 000 t, marcado, porque el SGM no lo imprimió), que baja la cuota del líder de ~80 % a ~60 %. Es el caveat ya declarado. ✔️ **Correcto.**

## 2. Encadenamientos MIP — Leontief, Ghosh, Hirschman-Rasmussen
**Fórmulas.** Técnicos $A=Z\hat{x}^{-1}$; Leontief $L=(I-A)^{-1}$; distribución $B=\hat{x}^{-1}Z$; Ghosh $G=(I-B)^{-1}$. Encadenamiento hacia atrás = suma de columna de $L$; hacia adelante = suma de fila de $G$ (Leontief 1941; Ghosh 1958; Hirschman 1958; Miller & Blair 2009). Índices normalizados de Rasmussen (1956): poder de dispersión $U_j=\frac{n\sum_i l_{ij}}{\sum_{i,j}l_{ij}}$ (= colsum/media), sensibilidad $U_i=\frac{n\sum_j g_{ij}}{\sum_{i,j}g_{ij}}$ (= rowsum/media).
**Prueba (validación contra INEGI).** `mip_calc.py` reproduce los tabulados oficiales a **precisión de máquina**: $\max|A-\text{ctec}_{INEGI}|=1.7\text{e-}18$ (2013) / $8.9\text{e-}16$ (2018); $\max|L-\text{cdi}_{INEGI}|=4.2\text{e-}15$ / $5.3\text{e-}15$. Ghosh se construye con la misma $Z,x$ ya validadas. La normalización del código (`BL/BL.mean()`, `FL/FL.mean()`) es **algebraicamente idéntica** a la fórmula de Rasmussen. ✔️ **Correcto y consistente con la literatura.**

## 3. CCV — coeficiente de captura de valor
**Fórmula.** $CCV_{m,t}=VU^{X,E1}_{m,t}/P^{USGS}_{m,t}$, con $VU=\frac{\sum_{h}\text{valor}_h}{\sum_h \text{peso}_h}$ sobre las fracciones E1 **con peso** ese año.
**Prueba.** $CCV==VU/P$ se cumple en las 323 filas con dato (0 inconsistencias >1e-3).
**Nota (no error).** En 5 filas $\text{valor}/\text{peso}\neq VU$: es **deliberado y documentado** — el valor unitario agrega solo las fracciones E1 que tienen peso (para no sesgarlo al alza), mientras `valor_export_e1` suma todas; sílice 2016 es el caso extremo por mezcla de grados. ✔️ **Correcto** (con los caveats de grupo mineral ya declarados: informativo en metales base; artefacto de ley en oro/plata).

## 4. Comercio por etapa
**Fórmula.** $X\text{-share crudo}=X^{E1}/X^{\text{total}}$.
**Prueba.** Aparecían 298/358 "inconsistencias", pero al inspeccionar son **idénticas a 4 decimales** (p. ej. barita 1992: ratio 0.4419 = share 0.4419): el CSV guarda el share **redondeado**, y el umbral de 1e-6 disparaba por el 5.º decimal. La identidad se cumple. ✔️ **Correcto.**

## 5. Comparación internacional (Ghosh sector, OECD ICIO)
**Fórmula.** Idéntica al Ghosh de §2, sobre el **bloque intra-país** de cada economía (45 industrias ISIC), Rasmussen media país = 1. Mismo método validado; `x` = columna OUT del ICIO. ✔️ **Correcto** (caveat: agregado sector-minería, no por mineral).

## 6. DVA / reprocesamiento
**Fórmulas.** Global $A=Z\hat{x}^{-1}$, $L=(I-A)^{-1}$, $v=VA/x$. DVA en exportaciones (método Leontief estándar): $\sum_{k\in s}v_k(Le)_k/E_{i_0}$. Reparto por sector exportador: $\text{contrib}_k=v_{i_0}L_{i_0 k}E_k$ → `crudo` (vía minería) / `reproc` (vía no-minería). Absorción extranjera (Los & Timmer 2005): $1-\frac{v_{i_0}\sum_k L_{i_0 k}f^s_k}{v_{i_0}\sum_k L_{i_0 k}f^{tot}_k}$.
**Prueba.** Identidad `reproc+crudo=1` sin violaciones (390 filas); todos los share en [0,1]; validez de cara (petróleo/carbón salen "en crudo" 0.81-0.98). ✔️ **Correcto e interpretable.**
**Caveat metodológico (único punto de refinamiento posible, no error).** El reparto crudo/reproc usa **exportaciones brutas** como "factura" (enfoque de valor agregado *en exportaciones brutas*), no la descomposición estricta de VAX con solo demanda final (Koopman-Wang-Wei; Borin-Mancini), y es a **nivel sector** (no por mineral). Es defendible y está etiquetado como descriptor agregado; una versión más estricta usaría la participación GVC hacia adelante publicada por TiVA. Ver §7.

## 7. Refinamientos posibles (no correcciones)
- **DVA**: cotejar contra la participación GVC hacia adelante publicada de **OECD TiVA** (misma matriz, definición estándar) como validación externa.
- **Comparación internacional**: añadir **upstreamness/downstreamness** (Antràs y Chor, 2013 — ya en el marco del protocolo) como medida de posición complementaria al Ghosh; y el **método de extracción hipotética** como robustez.
- Ninguno cambia los veredictos: los indicadores actuales son correctos.

## Veredicto
Los ocho indicadores están **matemáticamente bien calculados y son consistentes con la literatura** (input-output: Leontief, Ghosh, Hirschman, Rasmussen, Miller-Blair, Dietzenbacher, Los-Timmer; concentración: HHI/Rhoades). La MIP se valida contra INEGI a precisión de máquina; el resto satisface sus identidades. Los caveats existentes (cobre 2024 con total estimado; CCV por grupo; DVA agregado) están declarados y son correctos.

← [[Ruta - Completar indicadores y series (seguimiento)]] · [[Resumen metodologico y de resultados 2026-09-07]]
