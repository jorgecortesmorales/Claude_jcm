---
title: "Memoria — Peso histórico del bloque de 10 minerales críticos (1992-2025): PIB, exportaciones, empleo, crecimiento"
type: resultados
tags: [icr, justificacion, peso-economico, historico, pib, exportaciones, empleo, mip, comtrade, bloque-10]
created: 2026-09-08
updated: 2026-09-08
status: activo
---

# Memoria — Peso histórico del bloque de 10 minerales críticos (Actividad A)

> [!info] Propósito
> Cuantificar, **a lo largo del periodo estudiado (1992-2025)**, el **peso del bloque** de 10 minerales (barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice, zinc) y el **peso relativo de cada mineral**, en cuatro dimensiones: **exportaciones**, **producción/PIB**, **crecimiento** y **desarrollo industrial (empleo + encadenamiento)**. El análisis es **histórico** (series anuales) donde la fuente lo permite, y se apoya en dos benchmarks de la MIP (2013/2018) para el valor agregado. Refuerza la **justificación de la elección de los 10 minerales**.

## 0. Método, fuentes, alcance temporal y caveats

| Dimensión | Serie | Cobertura | Fuente (numerador / denominador) |
|---|---|---|---|
| **Exportaciones** | anual continua | **1992-2024** | Comtrade (bloque) / Banco Mundial `TX.VAL.MRCH.CD.WT` (total nacional) |
| **Valor de producción** | anual continua | **1992-2022** (completa) | volumen nacional (USGS MYB 1992-2003 y 2019-2022; CAMIMEX 2004-2018) × precio USGS empalmado |
| **PIB (VAB), empleo** | 2 cortes | **2013 y 2018** | MIP INEGI (filas B.1bP, PT) — no existe PIB anual por clase SCIAN |

Scripts: `10 Datos/scripts/peso_bloque_historico.py` (series históricas → `peso_bloque_hist_exportaciones.csv`, `peso_bloque_hist_produccion.csv`), `myb_produccion_pre2004.py` (producción 1992-2003 desde USGS MYB → `produccion_nacional_myb_pre2004.csv`) y `peso_bloque.py` (cortes MIP → `peso_bloque_mineria.csv`). Gráfica: `13 Entregables/png_charts/peso_historico.png`.

> [!warning] Alcance y límites (rigor)
> 1. **PIB por mineral solo en 2013/2018**: INEGI **no** publica PIB (valor agregado) a nivel de clase SCIAN de forma anual; el peso en el PIB se ancla en los dos cortes de la MIP y se declara como tal (no es una serie).
> 2. **Valor de producción completo 1992-2022**: el tramo **1992-2003 y 2019-2022 se tomó de los USGS Minerals Yearbook** (Tabla 1: 1998-2003 de los `.xls`; 1992-1997 y 2019-2022 leídos como imagen de los PDF, método de la nota [[usgs_myb_table2_notes]] ante la mala alineación de `pdftotext`); **2004-2018 de CAMIMEX** (`hhi_numeradores`). Dos empalmes de fuente, ambos **validados en el año de solape**: 2003/2004 (USGS→CAMIMEX) y 2018/2019 (CAMIMEX→USGS), donde USGS 2018 coincide con CAMIMEX en 8 de 10 minerales (difieren solo cobre −7 %, base SGM, y oro −1 %). **2023-2024** aún **no están en el USGS MYB** (el capítulo 2022 es el último, *advance release*); ese tramo lo cubren las exportaciones (serie a 2024).
> 3. **Corrección de una unidad (rigor)**: el cotejo con USGS **detectó un error propio de conversión**: la plata (y el oro) en `hhi_numeradores` vienen en **millones de onzas troy**, no en toneladas; la función de normalización no lo contemplaba y subvaluaba la plata ~31× en 2004-2018. Corregido (1 M oz = 31.1035 t); la composición 2018 pasa a incluir a la plata en ~19 % (antes desaparecía). Es la razón por la que se prefiere USGS y se valida todo cruzando fuentes.
> 4. **Manganeso**: se usó la base **contenido de Mn** (no peso bruto) para empatar con CAMIMEX 2004+.
> 5. **No mezclar bases**: exportaciones (Comtrade, HS), producción (USGS/SCIAN, USD vía precio USGS) y PIB (MIP, pesos) tienen bases distintas → se leen por separado.
> 6. **Validación**: la MIP se validó contra INEGI a precisión de máquina; los denominadores del Banco Mundial coinciden con INEGI (2018: 450,713 MUSD; 2024: 617,677 vs. 617,100); los valores USGS 1998 **coinciden entre `.xls` e imagen**; y CAMIMEX 2018 = USGS 2018 en 8/10 minerales (empalme limpio).

## 1. Peso histórico en las EXPORTACIONES (1992-2024) — el eje del análisis

**Serie completa** en `peso_bloque_hist_exportaciones.csv`; síntesis por año-ancla:

| Año | Exportaciones del bloque (MUSD) | Exportaciones nacionales (MUSD) | **Peso del bloque (%)** | Fase |
|---|---:|---:|---:|---|
| 1992 | 1,140 | 46,196 | **2.47 %** | punto de partida |
| 2002 | 1,894 | 160,682 | **1.18 %** | **mínimo** (dilución por manufactura TLCAN) |
| 2008 | 7,952 | 291,265 | 2.73 % | ascenso |
| 2011 | 19,290 | 349,569 | **5.52 %** | **pico** (superciclo de materias primas) |
| 2013 | 15,349 | 380,015 | 4.04 % | — |
| 2018 | 11,939 | 450,713 | 2.65 % | descenso |
| 2024 | 13,726 | 617,677 | 2.22 % | meseta reciente |

**Tres fases históricas** (ver `peso_historico.png`, panel izquierdo):
- **1992-2003 — dilución**: el bloque crece 5.2 % anual, pero las exportaciones nacionales crecen más rápido con el auge manufacturero del TLCAN; el peso minero **cae de 2.5 % a ~1.2 %** (mínimo en 2002).
- **2003-2013 — superciclo**: las exportaciones del bloque se multiplican por ~8 (**CAGR 22.6 %**) con el alza mundial de precios de metales; el peso **sube al máximo de 5.5 % (2011)**.
- **2013-2024 — meseta / reversión**: el valor exportado **se estanca** (CAGR −1.0 % en dólares corrientes) y el peso **regresa a ~2.2 %**, mientras la manufactura vuelve a dominar la canasta exportadora.

> [!important] Lectura para la justificación
> El peso del bloque en las exportaciones **no es estático: oscila entre 1.2 % y 5.5 %** siguiendo el ciclo de precios de metales. Esa **volatilidad cíclica** es en sí un rasgo del objeto (una economía primario-exportadora tomadora de precios, à la Prebisch-Singer). Aun en su mínimo, el bloque representa **~77 % de las exportaciones mineras** del país (2024): describir estos diez es describir la exportación minera de México.

## 2. Peso histórico en la PRODUCCIÓN (1992-2022) y su descomposición

**Serie** en `peso_bloque_hist_produccion.csv` (valor = volumen nacional × precio USGS; 1992-2003 y 2019-2022 USGS MYB, 2004-2018 CAMIMEX).

- El valor de producción del bloque es **plano en los años noventa** (~1,650-2,600 MUSD, 1992-2003), **despega con el superciclo** (2005-2012) y se sostiene alto después, hasta **~22,800 MUSD (2021-2022)**: de punta a punta **×13** (1,745 → 22,842 MUSD 1992-2022; ×9.4 a 2018).
- **Descomposición precio vs. volumen (1992→2018)**: valor ×9.39 = **volumen ×3.07 × precio ×3.06**. El crecimiento se reparte **casi por igual entre más producción y precios más altos** (cada factor ~×3), pero el **empuje de precios se concentra en 2004-2013** (superciclo): en ese tramo el valor sube mucho más rápido que el volumen (panel derecho de `peso_historico.png`, la franja = efecto precio). La lectura de fondo se mantiene: buena parte del "auge minero" fue **precio internacional** —una economía tomadora de precios (Prebisch-Singer)—, no solo expansión de capacidad.

## 3. Peso RELATIVO de cada mineral y su desplazamiento histórico

**Composición del valor de producción del bloque** (1992 → 2003 → 2018):

| | 1992 | 2003 | 2018 | Desplazamiento |
|---|---:|---:|---:|---|
| Cobre | 38 % | 33 % | 30 % | sigue #1, cede peso |
| **Oro** | 6 % | 12 % | **30 %** | **el gran ascenso** (boom del oro post-2008) |
| Plata | 15 % | 20 % | 19 % | alto y estable (México es 1.º mundial) |
| Zinc | 22 % | 18 % | 13 % | desciende |
| Plomo | 8 % | 7 % | 4 % | desciende |
| Resto (5 minerales) | ~11 % | ~10 % | ~4 % | marginal en valor |

En **exportaciones 2024**: cobre 33.5 %, oro 27.1 %, plata 20.3 %, plomo-zinc 14.5 % → los **cuatro metales concentran ~95 % de las exportaciones del bloque** y, en el PIB de la MIP 2018, **~94 % del valor agregado del bloque**. El desplazamiento histórico clave es el **ascenso del oro** (de ~6 % del valor en 1992 a ~30 % en 2018), que junto con la plata (19 %, estable) reconfigura el bloque hacia los **metales preciosos** a lo largo del periodo, mientras cobre, zinc y plomo ceden peso relativo.

> [!important] Doble criterio de selección (no solo peso)
> Los **cuatro metales** (cobre, oro, plata, plomo-zinc) son la columna vertebral **económica**. Los **seis restantes** (sílice, fluorita, grafito, manganeso, barita) pesan poco en valor —juntos <10 %— pero entran por **criticidad estratégica/industrial**: fluorita→HF y fluoropolímeros, sílice→vidrio y electrónica, grafito→acero y baterías, manganeso→acero, barita→perforación. La elección de los diez combina **peso económico + criticidad**, y esa dualidad es parte de la justificación.

## 4. Peso en el PIB y el empleo (benchmarks MIP 2013/2018)

Del corte de la MIP (valor agregado a precios básicos, `peso_bloque_mineria.csv`):

| | 2013 | 2018 |
|---|---:|---:|
| PIB del bloque / **PIB nacional** | 0.70 % | 0.71 % |
| PIB del bloque / **PIB minería 212** | 65.2 % | 61.0 % |
| PIB minería 212 / PIB nacional | 1.08 % | 1.16 % |
| Empleo del bloque (puestos) | 59,474 | 42,159 |
| Empleo del bloque / empleo nacional | 0.10 % | 0.07 % |

Aunque no hay serie anual de PIB por mineral, los dos cortes muestran un peso **pequeño y estable (~0.7 % del PIB) pero mayoritario dentro de la minería no petrolera (~60-65 %)**. El **empleo cae** entre los dos cortes (−29 %) mientras el valor sube: **más valor, menos empleo**, rasgo de una actividad **intensiva en capital**, coherente con el enclave.

## 5. Crecimiento (síntesis histórica)

- **Exportaciones**: CAGR **8.1 % (1992-2024)**, con el arco 5.2 % (1992-2003) → 22.6 % (2003-2013, superciclo) → −1.0 % (2013-2024).
- **Producción**: ×9.4 (1992-2018) = **volumen ×3.07 × precio ×3.06** → aporte **casi parejo** de volumen y precio en el total, pero el empuje de **precio** se concentra en 2004-2013; ×13 a 2022. Plana en los noventa, despega con el superciclo.
- **PIB del bloque**: +49 % nominal (2013→2018), algo por encima de la economía.
- **Empleo**: **decreciente**. El crecimiento del bloque **no se traduce en empleo** ni, como muestran CCV/DVA, en captura de valor doméstica.

## 6. Desarrollo industrial (aproximación)

Se aproxima con descriptores ya construidos (ver memorias): **encadenamiento hacia adelante y demanda intermedia** (MIP: sílice/grafito/manganeso alimentan industria; cobre/oro/plata sostienen metalurgia sin continuidad manufacturera; barita/plomo-zinc en bruto), **captura de valor** (CCV, comercio por etapa, DVA: el valor se reprocesa afuera) y **empleo** (bajo y decreciente en la extracción; transformación deslocalizada). Ver [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]], [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]] §5 y [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]].

> [!note] Cierre — qué justifica estudiar estos diez (histórico)
> (1) **Cobertura**: son ~60-65 % del PIB minero no petrolero y ~77 % de las exportaciones mineras. (2) **Doble criterio**: peso económico (4 metales) + criticidad estratégica (6 minerales). (3) **Pertinencia histórica del problema**: su peso **oscila con el ciclo de precios** (1.2 %-5.5 % de las exportaciones), su crecimiento fue **mayormente de precio** y **no generó empleo ni cadena doméstica** — exactamente el enclave estructural que la tesis describe. El peso pequeño en el PIB **no** debilita la elección: la refuerza, porque el aporte de la tesis no es el tamaño del sector, sino **la caracterización histórica de su inserción** en las cadenas de valor.

## 7. Fuentes
- **INEGI.** MIP 2013 y 2018 (tabla total pxp): filas B.1bP (PIB), P.1 (VBP), PT (empleo). `10 Datos/Bases Originales/10 MIP INEGI/`.
- **UN Comtrade** (re-descarga 2026): exportaciones por mineral y etapa 1992-2024. `processed/comercio_posicion_1992_2024.csv`.
- **Banco Mundial.** *Merchandise exports (current US$)*, indicador TX.VAL.MRCH.CD.WT, México 1992-2024. https://data.worldbank.org/indicator/TX.VAL.MRCH.CD.WT?locations=MX (coincide con INEGI/Banxico en años solapados).
- **USGS** (precios) y **CAMIMEX/SGM** (volúmenes de producción nacional). `precios_usgs_anual_empalmado.csv`, `hhi_numeradores.csv`.
- **SGM.** Anuario Estadístico de la Minería Mexicana 2024 (ed. 2025): minería = 6.º generador de divisas; exportaciones mineras 2024 ≈ 17,800 MUSD. https://www.sgm.gob.mx/productos/pdf/Anuario_2024_Edicion_2025.pdf

← [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] · [[Catalogo de Bases de Datos]] · [[Ruta - Completar indicadores y series (seguimiento)]]
