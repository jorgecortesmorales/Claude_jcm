---
title: "Handoff — Incorporar la MIP 2008 como referencia (2026-09-05)"
type: proyecto
tags: [icr, proyecto, handoff, mip, ghosh, 2008, referencia]
created: 2026-09-05
updated: 2026-09-05
status: ejecutado
---

# Handoff — para el chat nuevo (2026-09-05)

> [!important] Fuente única de verdad para la siguiente tarea. Léela completa antes de tocar nada. Todo el trabajo es **dentro de `ICR/`**. Usar **`py`** (no `python`). El diseño es **descriptivo**, concepto ordenador = **enclave estructural**. La especificación detallada paso a paso está en [[Plan - Incorporar MIP 2008 como referencia]] — este handoff es el arranque.

## 1. Tarea
Incorporar la **MIP 2008** (base 2008, SCIAN 2007) como **corte de referencia histórica** de los indicadores de encadenamiento hacia adelante (Leontief, Ghosh, Hirschman-Rasmussen, demanda intermedia doméstica), dando profundidad **2008 → 2013 → 2018**. **No se encadena** con la serie comparable 2013/2018: es un punto de referencia con caveats explícitos.

## 2. Decisiones firmes (del alumno, 2026-09-05)
1. **2012 NO entra por mineral**: se descargó y se verificó que la MIP 2012 (actualización) **solo llega a nivel Rama** (minería agregada en "metálicos"/"no metálicos"), sin desglose por mineral. → Se procede **solo con 2008**. Opcional: contexto a nivel Rama agregado (otra granularidad), no por mineral.
2. **Base doméstica** (como 2013/2018).
3. **Salida en archivo separado** (no contaminar la serie comparable 2013/2018).

## 3. Estado del cotejo previo (ya hecho)
- **Concordancia SCIAN 2007 ↔ 2013**: **9/10 minerales 1:1** (oro 212221, plata 212222, cobre 212231, plomo-zinc 212232 [combinada], sílice 212324, barita 212393, fluorita 212395, grafito 212396). **Manganeso 212291 con caveat**: en 2008 la clase agrega 212292 (mercurio/antimonio) y 212299 (otros metálicos); en 2018 son clases aparte. Registrado en `10 Datos/processed/concordancia_scian_2007_2013_minerales.csv`.

## 4. Insumos ya disponibles
- Carpeta `10 Datos/Bases Originales/10 MIP INEGI/2003_2008 historicas (no comparables)/`:
  - `Tabulados_mip2008.zip` — **usar**. Nivel **Clase (`_4`)**, producto×producto, doméstica: `mipdctcpxp_4.XLSX` (A), `mipdcdipxp_4.XLSX` (inversa de Leontief), `mipdpb_pxp_4.XLSX` (flujos → Ghosh, VBP, DI). Dimensión ~835 clases (≈ 2013/2018).
  - `Tabulados_amip2012_2008.zip` — solo Rama; no usable por mineral.
  - `mip2003_SECTORySUBSECTOR.zip` — descartado.
- **Herramientas confirmadas**: `openpyxl 3.1.5` + `numpy 2.2.5` (mismo stack que `mip_calc.py`). **No requiere Node ni pandas.**
- **Método de referencia**: `10 Datos/scripts/mip_calc.py` (calcula A, L, Ghosh, Hirschman-Rasmussen, DI para 2013/2018; validado contra INEGI).

## 5. Qué ejecutar (resumen; detalle en el Plan)
1. `mip2008_extract.py` — openpyxl: leer los 3 `.XLSX` `_4` domésticos, ubicar **dinámicamente** encabezados (el .XLSX trae filas de título y el código de clase en columna propia, distinto del CSV abierto de 2013/2018), construir matrices cuadradas por código de clase, volcar a CSV con el formato de 2013/2018.
2. `mip2008_calc.py` — A, L=(I−A)⁻¹, Ghosh G=(I−B)⁻¹, Rasmussen (atrás/adelante), demanda intermedia doméstica, por mineral.
3. **Validar** reproduciendo la A (desde ctec) y la L (desde cdi) de INEGI a **precisión de máquina** (~1e-15) — igual que 2013/2018. Si valida, la extracción es correcta.
4. Guardar **`10 Datos/processed/mip_encadenamientos_2008_referencia.csv`** (archivo separado), columnas como `mip_encadenamientos_minerales.csv` + `base_scian` y `comparabilidad=referencia`.
5. **Caveats obligatorios**: año base 2008 / precios de 2008 (niveles no comparables, coeficientes sí); índices Rasmussen normalizados no comparables en nivel entre añadas → reportar también Ghosh crudo (suma de fila) y DI/VBP, leer patrón no nivel; nota de manganeso.
6. **Integrar**: sección "corte de referencia 2008" en [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]]; nota en [[Catalogo de Bases de Datos]] §10; actualizar [[Bitacora]]. Opcional: gráfico Ghosh 2008→2013→2018 rotulado "2008 = referencia".

## 6. Cuidados técnicos
- **`py`** (no `python`). Validar CSVs con `py`+`csv` (0 malformadas). No sobrescribir; versionar/archivar.
- **Trabajar solo dentro de `ICR/`**. **PROTOCOLO**: conserva control de cambios a la espera del asesor — **NO aceptar**.
- Actualizar la [[Bitacora]] al cerrar. Sin redacción "de IA": solo lo necesario.

← [[Home]] · [[Plan - Incorporar MIP 2008 como referencia]] · [[Mapa del Proyecto]] · [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]]
