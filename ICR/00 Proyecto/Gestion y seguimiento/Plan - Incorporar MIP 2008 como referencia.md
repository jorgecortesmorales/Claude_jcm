---
title: "Plan — Incorporar la MIP 2008 como corte de referencia"
type: plan
tags: [icr, plan, mip, insumo-producto, ghosh, 2008, referencia]
created: 2026-09-05
updated: 2026-09-05
status: ejecutado
---

> [!check] Decisiones confirmadas por el alumno (2026-09-05)
> **(1)** Se pidió añadir 2012, pero al descargarlo se verificó que la **MIP 2012 (actualización) solo llega a nivel Rama** —minería agregada en "metálicos" y "no metálicos", sin desglose por mineral—, por lo que **NO es incorporable por mineral** (misma limitación que 2003). Se procede **solo con la MIP 2008** como corte de referencia. Opcional: mostrar 2012 a nivel Rama agregado como contexto (no por mineral). **(2)** Base **doméstica**. **(3)** Salida en **archivo separado**.

# Plan — Incorporar la MIP 2008 como corte de referencia (no encadenado)

> [!goal] Objetivo
> Añadir la **MIP 2008** (base 2008, SCIAN 2007) como un **tercer corte de referencia histórica** de los indicadores de encadenamiento hacia adelante (Leontief, Ghosh, demanda intermedia doméstica), para dar profundidad temporal descriptiva (**2008 → 2013 → 2018**). **No se encadena** con la serie comparable 2013/2018: se presenta con caveats explícitos de año base y clasificación.

## 1. Encuadre y decisiones firmes
- El corte 2008 es **referencia**, no serie comparable: los movimientos 2008→2013 mezclan cambio real con cambio de año base/añada SCIAN. Se reporta como punto ilustrativo con caveat, no como tendencia.
- **2003 queda fuera** (solo Sector/Subsector; sin minería por mineral).
- La continuidad del período 1992-2025 la sigue aportando el **CCV**; la MIP 2008 solo alimenta Ghosh/Leontief/DI.
- **Concordancia ya cotejada**: 9/10 minerales 1:1 entre SCIAN 2007 y 2013; **manganeso (212291) con caveat** (en 2008 la clase agrega 212292 y 212299; en 2018 son clases aparte). Ver `10 Datos/processed/concordancia_scian_2007_2013_minerales.csv`.

## 2. Insumos ya disponibles
Carpeta: `10 Datos/Bases Originales/10 MIP INEGI/2003_2008 historicas (no comparables)/` (contiene también 2003 y 2012; el nombre de carpeta es provisional).
- **Datos 2008 descargados** (Excel): `Tabulados_mip2008.zip`. Contiene, a nivel **Clase** (`_4`), producto×producto, base **doméstica** (los insumos que se usarán):
  - `mipdctcpxp_4.XLSX` — coeficientes técnicos = matriz **A**.
  - `mipdcdipxp_4.XLSX` — directos+indirectos = **inversa de Leontief L**.
  - `mipdpb_pxp_4.XLSX` — MIP doméstica a precios básicos (**flujos** → para Ghosh, VBP y demanda intermedia).
- **Datos 2012 descargados** (`Tabulados_amip2012_2008.zip`) — **VERIFICADO: solo llega a Rama (`_3`)**; la minería aparece como "Minería de minerales metálicos" y "…no metálicos", sin desglose por mineral. **No usable por mineral.** Se conserva por si se quiere un contexto agregado a nivel Rama (metálicos vs no metálicos), que es otra granularidad.
- **Datos 2003** (`mip2003_SECTORySUBSECTOR.zip`) — solo Sector/Subsector; descartado.
- **Herramientas**: `openpyxl 3.1.5` (leer .XLSX) + `numpy 2.2.5` (álgebra) — mismo stack que `mip_calc.py`.
- **Método de referencia**: `10 Datos/scripts/mip_calc.py` (ya calcula A, L, Ghosh, Hirschman-Rasmussen y demanda intermedia para 2013/2018, validado contra INEGI).

## 3. Fases del plan

### Fase A — Extracción (Excel 2008 → CSV)
1. Escribir `mip2008_extract.py`: con openpyxl, leer los tres `.XLSX` `_4` (doméstica), localizar el bloque de datos (fila de encabezado con códigos de clase; códigos de fila en la columna correspondiente), y construir las matrices cuadradas indexadas por **código de clase** (~835 clases).
2. Guardar en CSV la matriz A, L y los flujos domésticos, con el mismo formato que las MIP 2013/2018 del proyecto (para reutilizar el cálculo).
3. **Cuidado de formato**: el .XLSX de 2008 trae filas de título y el código/nombre en columnas propias (distinto del CSV abierto de 2013/2018). El parser debe ubicar dinámicamente encabezados y no asumir posiciones fijas.

### Fase B — Cálculo y validación
4. Adaptar `mip_calc.py` → `mip2008_calc.py`: calcular **A**, **L = (I − A)⁻¹**, **Ghosh G = (I − B)⁻¹** (B = coef. de distribución de los flujos domésticos), índices **Hirschman-Rasmussen** (atrás/adelante, normalizados) y **demanda intermedia doméstica** por mineral.
5. **Validación (misma prueba que 2013/2018)**: reproducir la `A` de INEGI desde ctec y la `L` desde cdi a **precisión de máquina** (max dif ~1e-15). Si valida, la extracción es correcta.
6. Extraer los indicadores por mineral para los 9 con concordancia 1:1 + manganeso con nota.

### Fase C — Comparabilidad y caveats (obligatorio declararlos)
7. Marcar el corte 2008 con: **año base 2008 / SCIAN 2007**; **precios en pesos de 2008** (los niveles no comparables; los coeficientes, al ser ratios, sí robustos).
8. **Índices Rasmussen normalizados**: su nivel no es estrictamente comparable entre añadas (la normalización usa el promedio de toda la economía, cuya clasificación cambia). → Reportar también el **Ghosh crudo (suma de fila)** y **DI/VBP**, y apoyar la lectura en el **patrón/orden**, no en el nivel exacto.
9. **Manganeso**: nota per-mineral (212291 más amplia en 2008).

### Fase D — Salidas e integración
10. Guardar `10 Datos/processed/mip_encadenamientos_2008_referencia.csv` **como archivo separado** (no contaminar la serie comparable 2013/2018); columnas iguales a `mip_encadenamientos_minerales.csv` + `base_scian` y `comparabilidad=referencia`.
11. Actualizar [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] con una sección "Corte de referencia 2008" y sus caveats.
12. Actualizar [[Catalogo de Bases de Datos]] §10 (MIP) señalando 2008 como referencia histórica (Excel, base distinta).
13. (Opcional) Gráfico Ghosh **2008 → 2013 → 2018** por mineral (3 puntos), rotulado "2008 = referencia, base distinta".
14. Actualizar [[Bitacora]].

## 4. Decisiones (ya resueltas — ver callout al inicio)
- **2012**: descartada por mineral (solo Rama). Opcional: contexto a nivel Rama.
- **Base doméstica** · **archivo separado**. Confirmadas.

## 5. Riesgo y esfuerzo
- **Riesgo principal**: parseo del .XLSX (filas de título, ubicación de códigos). Mitigado porque ya leímos celdas del archivo por XML y openpyxl está disponible; la validación contra INEGI (paso 5) detecta cualquier error de extracción.
- **Esfuerzo**: una sesión enfocada (extracción + cálculo + validación + integración).
- **Sin bloqueos de herramientas**: openpyxl + numpy disponibles; no requiere Node ni pandas.

## 6. Checklist ordenado
1. [ ] `mip2008_extract.py` (Excel → CSV, con ubicación dinámica de encabezados).
2. [ ] `mip2008_calc.py` (A, L, Ghosh, Rasmussen, DI).
3. [ ] Validar A/L contra INEGI a precisión de máquina.
4. [ ] `mip_encadenamientos_2008_referencia.csv` (con banderas de comparabilidad).
5. [ ] Caveats declarados (base, precios, Rasmussen, manganeso).
6. [ ] Memoria + Catálogo + Bitácora actualizados.
7. [ ] (Opcional) gráfico 2008→2013→2018 y/o corte 2012.

← [[Home]] · [[Mapa del Proyecto]] · [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]]
