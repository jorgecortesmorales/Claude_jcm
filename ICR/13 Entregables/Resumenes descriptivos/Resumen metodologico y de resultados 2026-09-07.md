---
title: "Resumen metodológico y de resultados — indicadores de la ICR"
type: resumen
tags:
  - icr
  - resumen
  - metodologia
  - resultados
  - indicadores
  - enclave-estructural
created: 2026-09-07
updated: 2026-09-07
status: activo
cssclasses:
  - wide-tables
---

# Resumen metodológico y de resultados

> [!abstract] Qué es este documento
> Referencia única y autocontenida de **todos los indicadores** construidos para la ICR *«Los mercados de los minerales críticos en México, 1992-2025»* (diseño **descriptivo** de cadenas de valor; concepto ordenador = **enclave estructural**). Para cada indicador se documenta: (a) qué mide, (b) **la matemática** que lo define, (c) **las bases de datos y su ubicación**, (d) **todos los resultados**, y (e) su interpretación y caveats. Los 10 minerales del corpus: **barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice, zinc**.

> [!info] Cómo actualizar este documento
> Es una nota Markdown del vault: se edita directamente en Obsidian. Cada sección termina con **«Reproducir / actualizar»**, que indica el script `py` y la base que la generan. Para refrescar un resultado: correr el script → regenerar el CSV en `10 Datos/processed/` → actualizar la tabla y el campo `updated` del frontmatter. Ver [[Ruta - Completar indicadores y series (seguimiento)]] para el estado vivo del proyecto.

---

## 0. Mapa de indicadores

| # | Indicador | Qué describe | Cobertura | Base (processed) |
|---|---|---|---|---|
| 1 | **HHI** | Concentración de la estructura extractiva | 2004-2024 | `hhi_consolidado.csv` |
| 2 | **Encadenamientos MIP** (Leontief, Ghosh, Rasmussen) | Arrastre hacia atrás/adelante por mineral | 2008·2013·2018 | `mip_encadenamientos_minerales.csv` |
| 3 | **CCV** (captura de valor) | Valor captado al exportar en bruto | 1992-2025 | `ccv_serie.csv` |
| 4 | **Comercio por etapa** | % exportado en crudo (mena/concentrado) | 1992-2024 | `comercio_posicion_1992_2024.csv` |
| 5 | **Destinos** | A dónde va la exportación (socio) | 1992-2024 | `comercio_destinos_serie_resumen.csv` |
| 6 | **Georreferenciación** | Geografía de extracción y transformación | 2024 | `georref_extraccion_mineral_estado_cuantitativo.csv` |
| 7 | **Comparación internacional (Ghosh)** | Minería MEX vs. CHL/AUS/FIN/SWE + CHN/BRA/PER (8 países) | 2008/2013/2018 | `icio_comparacion_mineria.csv` |
| 8 | **DVA / reprocesamiento** | Enclave *en dinero* (valor retenido vs. reprocesado afuera), 8 países | 1995-2020 | `icio_dva_mineria.csv` |
| 9 | **Regionalización** (Paso 8) | Concentración geográfica y desacople extracción→transformación | 2024 | `georref_regionalizacion.csv` |

Complementos cualitativos: mapa de **empresas de transformación** (`empresas_transformacion.csv`) y **nota grafito** (amorfo vs. criticidad).

---

## 1. Fuentes de datos y su ubicación

Todas dentro de `ICR/`. Originales en `10 Datos/Bases Originales/`; indicadores en `10 Datos/processed/`; rutinas en `10 Datos/scripts/`.

| Fuente | Uso | Ubicación |
|---|---|---|
| **CAMIMEX + USGS** (producción por mina/empresa) | HHI | `Bases Originales/01 Criticidad…`, `02 Producción…`; `processed/hhi_numeradores.csv` |
| **MIP INEGI** (matriz simétrica producto×producto, doméstica, Clase SCIAN) | Encadenamientos | `Bases Originales/10 MIP INEGI/{2013,2018}/`; 2008 en `…/2003_2008 historicas…` |
| **UN Comtrade** (fracciones HS, valor y peso; reporter 484) | CCV, comercio por etapa, destinos | `Bases Originales/11 Comercio Comtrade/` |
| **USGS DS-140 / MCS / Cochilco** (precios de referencia) | Denominador del CCV | `processed/precios_usgs_anual_empalmado.csv` |
| **SGM, Anuario Estadístico de la Minería Mexicana 2025** (leído como imagen) | Georreferenciación | `processed/georref_*` |
| **OECD ICIO, edición 2023** (77 economías × 45 industrias ISIC Rev.4) | Comparación internacional, DVA | `Bases Originales/12 OECD ICIO/` (procedencia); matrices completas no conservadas |

---

## 2. HHI — concentración de la estructura extractiva

**Qué mide.** El grado de concentración de la producción de cada mineral entre empresas/minas: de un mercado atomizado a un monopolio.

**Intuición.** Es un termómetro de "¿pocos o muchos?": si un solo grupo produce casi todo, marca cerca de 10 000; si hay muchos productores parecidos, baja. Como eleva las cuotas al cuadrado, un líder dominante pesa mucho más que varios pequeños.

**Matemática.** Índice de Herfindahl-Hirschman, suma de los cuadrados de las participaciones de mercado $s_i$ (en base 0-10 000):

$$ HHI = \sum_{i=1}^{N} s_i^{2}, \qquad s_i=\frac{q_i}{\sum_i q_i}\times 100 $$

Umbrales convencionales: <1 500 baja, 1 500-2 500 moderada, >2 500 alta, 10 000 monopolio.

**Datos y método.** Producción por mina/empresa (base B5, CAMIMEX + USGS). Para **2021-2024** se calcula por mina (nivel comparable); para **2004-2020** se reconstruye por régimen de mercado (líder + grupos conocidos, residual tratado como atomístico) → **cota inferior**, no comparable en nivel con 2021-2024. Ubicación: `processed/hhi_consolidado.csv` (+ `hhi_numeradores.csv`).

**Resultados — HHI por mineral y año (2004-2024).** Celda vacía = año sin dato utilizable.

| Mineral | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| Cobre | | 7500 | 6806 | | 2570 | | 2621 | 4356 | | 4147 | | | | | 5417 | 5625 | 6209 | 3841 | 3362 | 3764 | 3557 |
| Plomo | | | | | | | 524 | 986 | 858 | 812 | | 961 | 441 | | | | 973 | 1448 | 1090 | 1823 | 2465 |
| Zinc | | | | | | 1149 | 773 | 635 | 566 | | | 1024 | | | | | 692 | 1591 | 1199 | 1551 | 1683 |
| Plata | | 1318 | 1218 | 1109 | 1005 | 1102 | 640 | 610 | 562 | | | | | | 1109 | 762 | 864 | 926 | 820 | 914 | 1147 |
| Oro | 2043 | 1197 | | 702 | 1296 | 1296 | 708 | 590 | 676 | | | | | | | | | 771 | 409 | 312 | 429 |
| Manganeso | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 |
| Fluorita | 6001 | 6525 | 6525 | 6525 | 6525 | 6525 | 6525 | 6525 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 |
| Grafito | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | |
| Barita | 3069 | | 5655 | 3576 | | 6257 | | 5141 | 10000 | 7022 | 10000 | | | 4638 | 6400 | 8317 | 3982 | 6779 | 2479 | 1380 | 605 |
| Sílice | | | 5271 | 4409 | | 4147 | 4251 | 5242 | 2884 | 4356 | | | | | 10000 | 10000 | 8519 | 9742 | 5519 | 6670 | |

**Resultados — extensión 1994-2003 (Paso 7, régimen documentado, USGS MYB Tabla 2 + narrativa).** Solo se reconstruyen los minerales de régimen estructural inequívoco y consistente con la serie 2004+:

| Mineral | 1994 | 1995 | 1996 | 1997 | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | Base |
|---|--|--|--|--|--|--|--|--|--|--|---|
| Manganeso | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | 10000 | Monopolio Autlán (único operador, Tabla 2) |
| Fluorita | 6001 | 6001 | 6001 | 6001 | 6001 | 6001 | 6001 | 6001 | 6001 | 6001 | Líder Las Cuevas ~75-80 % + fringe (narrativa) |
| Grafito | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | 5848 | Duopolio documentado (mismo régimen 2004-2013) |
| Cobre | — | — | — | 6241 | 6724 | — | 6400 | 7225 | 6889 | 6400 | Grupo México (La Caridad+Cananea) 79-85 % del cobre-mina; cota inferior |

Para **oro, plata, plomo, zinc** las narrativas USGS documentan participaciones de líder —oro: Peñoles 35 % (2000), 32 % (2001); plata: Peñoles 56 % (1998), 53 % (2000), 59 % (2003); zinc: líder 60 % (2002) y duopolio ~45 %/44 % (2000); plomo: líder ~30 % (1998)— pero de **nivel grupo/empresa mixto**; se registran como **evidencia cualitativa** y sus celdas 1994-2003 se **declaran** (no se cuantifican) para no romper la comparabilidad con la serie por empresa 2004+. **Barita y sílice**: sin participación firme → declarados. **1992-1993**: sin solución (privatización en curso, sin estructura por empresa).

**Interpretación.** Tres patrones: (i) **monopolio persistente** — manganeso (Autlán) **desde antes de 1994** hasta 2024; fluorita (líder Las Cuevas ~75-80 % en los 1990s → monopolio de grupo tras la fusión de enero 2012); grafito (duopolio → productor único desde 2014). (ii) **alta y decreciente** — cobre (Grupo México dominante, ~80 % del cobre-mina en 1997-2003 → baja a ~3 550 en 2024); barita se **desconcentra** al final (6 779 en 2021 → 605 en 2024). (iii) **moderada al alza** — plomo y zinc suben (Peñasquito/Newmont). Oro es el más fragmentado. **La concentración extractiva y el grado de transformación no covarían** (§10).

> [!warning] Caveats
> 1994-2003 y 2004-2020 **aproximados** (cota inferior por régimen); niveles no comparables con 2021-2024 (por mina) ni, en cobre/fluorita 1994-2003, con el nivel-empresa 2004+ (base grupo). Sílice y grafito **sin dato 2024** (falta distribución). 1992-1993 sin solución.

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/hhi_2024.py` (→2024), `hhi_consolidado_2004_2020.py` (2004-2020) y `hhi_1994_2003.py` (1994-2003, Paso 7). Salida: `processed/hhi_consolidado.csv`. Fuentes 1994-2003 en `Bases Originales/07 USGS MCS/MYB Mexico/` (capítulos re-descargables del S3 del USGS).

---

## 3. Encadenamientos MIP — Leontief, Ghosh, Hirschman-Rasmussen

**Qué mide.** La posición de cada mineral en la estructura productiva: cuánto arrastra a sus **proveedores** (hacia atrás) y cuánto alimenta a las industrias **aguas abajo** (hacia adelante).

**Intuición.** Dos preguntas espejo sobre el mismo cuadro insumo-producto: hacia atrás, ¿a cuántos proveedores jala el mineral al producirse?; hacia adelante, ¿a cuántas industrias alimenta como insumo? En minería lo primero suele ser bajo (extraer usa pocos insumos industriales) y lo relevante para la tesis es lo segundo.

**Matemática.** Con la matriz de flujos domésticos $Z$ ($z_{ij}$ = venta del sector $i$ al $j$) y la producción total $x$:

$$ A = Z\,\hat{x}^{-1}\;\;(a_{ij}=z_{ij}/x_j), \qquad L=(I-A)^{-1}\;\text{(inversa de Leontief)} $$
$$ B = \hat{x}^{-1}Z\;\;(b_{ij}=z_{ij}/x_i), \qquad G=(I-B)^{-1}\;\text{(inversa de Ghosh)} $$

Encadenamiento **hacia atrás** $BL_j=\sum_i l_{ij}$ (suma de columna de $L$); **hacia adelante** $FL_i=\sum_j g_{ij}$ (suma de fila de $G$). Índices de **Hirschman-Rasmussen** normalizados (media de la economía = 1):

$$ U_j=\frac{n\sum_i l_{ij}}{\sum_{i,j} l_{ij}} \quad(\text{atrás}), \qquad U_i=\frac{n\sum_j g_{ij}}{\sum_{i,j} g_{ij}} \quad(\text{adelante}) $$

Un valor **>1** indica encadenamiento por encima del promedio de la economía.

**Datos y método.** MIP INEGI simétrica producto×producto, base **doméstica**, nivel **Clase SCIAN** (6 díg.): 2013 (822 clases) y 2018 (834), más **2008** (814, SCIAN 2007) como referencia histórica no encadenada. Plomo y zinc comparten clase (212232, coextracción) → se reportan **combinados**. Validado contra INEGI a precisión de máquina ($|A-\text{ctec}|,|L-\text{cdi}|\sim10^{-15}$). Ubicación: `processed/mip_encadenamientos_minerales.csv` (+ `mip_demanda_intermedia_minerales.csv`; 2008 en `mip_encadenamientos_2008_referencia.csv`).

**Resultados 2018** (media nacional = 1; DI/VBP = fracción a demanda intermedia doméstica):

| Mineral | VBP (MM$) | DI/VBP | Atrás $U_j$ | Adelante $U_i$ |
|---|--:|--:|--:|--:|
| Sílice | 6 959 | 0.99 | 0.94 | **1.92** |
| Grafito | 720 | 0.88 | 0.87 | **1.71** |
| Manganeso | 635 | 0.78 | 1.05 | **1.54** |
| Cobre | 92 893 | 0.53 | 0.94 | **1.34** |
| Fluorita | 5 862 | 0.50 | 0.97 | **1.31** |
| Oro | 69 491 | 0.96 | 1.03 | **1.22** |
| Plata | 49 784 | 0.89 | 0.99 | **1.18** |
| Plomo-zinc | 34 725 | 0.14 | 0.99 | 0.71 |
| Barita | 686 | 0.03 | 0.96 | 0.64 |

**Resultados 2013** (822 clases):

| Mineral | VBP (MM$) | DI/VBP | Atrás | Adelante |
|---|--:|--:|--:|--:|
| Manganeso | 486 | 0.72 | 0.83 | **1.79** |
| Sílice | 4 898 | 0.99 | 0.91 | **1.80** |
| Oro | 49 607 | 1.00 | 0.92 | **1.35** |
| Plata | 44 680 | 0.96 | 0.91 | **1.30** |
| Grafito | 164 | 0.59 | 0.84 | **1.24** |
| Cobre | 39 971 | 0.46 | 0.89 | **1.18** |
| Fluorita | 2 218 | 0.22 | 0.85 | 0.87 |
| Barita | 368 | 0.18 | 0.96 | 0.76 |
| Plomo-zinc | 20 046 | 0.12 | 0.89 | 0.72 |

**Resultados 2008** (814 clases; referencia, leer por orden no por nivel):

| Mineral | VBP (MM$ 2008) | DI/VBP | Atrás | Adelante |
|---|--:|--:|--:|--:|
| Grafito | 404 | 0.91 | 0.97 | **1.69** |
| Cobre | 12 361 | 0.74 | 0.84 | **1.63** |
| Sílice | 1 217 | 0.81 | 0.90 | **1.60** |
| Oro | 12 804 | 0.98 | 0.95 | **1.48** |
| Plomo-zinc | 7 930 | 0.79 | 0.98 | **1.35** |
| Barita | 270 | 0.90 | 0.96 | **1.29** |
| Fluorita | 1 286 | 0.36 | 0.98 | **1.11** |
| Manganeso ⚠️ | 8 105 | 0.27 | 0.86 | 1.00 |
| Plata | 19 037 | 0.18 | 0.94 | 0.80 |

**Compradores domésticos (2018, demanda intermedia).** Oro 99.5 % y plata 99.0 % → *fundición y refinación de metales preciosos*; cobre 93.5 % → *fundición y refinación de cobre*; plomo-zinc 79.5 % → *fundición de no ferrosos* (+5 % baterías); grafito → ferroaleaciones/siderurgia (43 %/32 %); sílice → vidrio 43 %, cemento 39 %; manganeso → uso disperso (farmacéutica, alimentos animales, química); fluorita → cemento 82 % (metspar; la cadena fluoroquímica intra-firma —HF de Koura— no la capta el sector); barita → perforación de pozos 58 %.

> [!important] Cómo leer el Ghosh (cautela central)
> Un $U_i>1$ **no** equivale a cadena desarrollada: mide **arrastre estructural** (asignación a usos intermedios), no captura de valor. Sílice (1.92) es alto porque muchos sectores usan arena, pero el silicio de mayor valor se **importa**; oro/plata (>1) son **un solo eslabón** (refinación) que luego se exporta. Por eso el Ghosh **nunca se lee solo**: se cruza con el CCV, el comercio por etapa y el mapa de empresas.

> [!warning] Caveats
> Plomo-zinc combinado; años base distintos (niveles no comparables, índices normalizados sí); 2008 con clase de manganeso más amplia (212291 agrega mercurio/antimonio) → no comparable; Ghosh supone coeficientes fijos (descriptor, no predicción).

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/mip_calc.py` (2013/2018) y `mip2008_calc.py` (2008).

---

## 4. CCV — coeficiente de captura de valor

**Qué mide.** Serie **continua** del encadenamiento hacia adelante: qué fracción del valor del producto de referencia (refinado) capta México cuando exporta el mineral en su **forma bruta** (mena/concentrado). Un CCV bajo y persistente es el descriptor de serie del enclave.

**Intuición.** Es la versión "película" (anual, 1992-2025) de lo que el Ghosh ve en "fotos" (dos o tres años): qué tan cerca del producto terminado vende México lo que saca en bruto. Cerca de 1, la forma exportada ya vale casi como el refinado; cerca de 0, se está vendiendo prácticamente la roca.

**Matemática.** Para cada mineral $m$ y año $t$:

$$ CCV_{m,t}=\frac{VU^{X,E1}_{m,t}}{P^{USGS}_{m,t}}, \qquad VU^{X,E1}_{m,t}=\frac{\sum_{h\in E1_m}\text{valor}^{X}_{h,t}}{\sum_{h\in E1_m}\text{peso}_{h,t}}\;[\text{USD/t}] $$

Numerador = valor unitario de exportación en frontera de las fracciones **E1** (Comtrade); denominador = precio de referencia refinado (USGS empalmado). $CCV\to1$: se exporta casi al valor del refinado; $CCV\to0$: se capta poco (más distancia al eslabón procesado).

**Datos y método.** Comtrade (reporter 484, valor + peso `netWgt`); huecos completados por **datos espejo** (importaciones de socios desde México, marcados `fuente_numerador='espejo'`, **CIF** → posible sesgo al alza). Cobertura tras espejo: 7 minerales completos 1992-2025; plomo 33/34 (falta 1994, **declarado, no imputado**). Ubicación: `processed/ccv_serie.csv` (340 filas).

**Resultados — CCV por mineral (media y rango de todos los años con dato):**

| Mineral | Grupo | CCV medio | Mín | Máx | Lectura |
|---|---|--:|--:|--:|---|
| **Cobre** | metal base | **0.224** | 0.125 | 0.364 | Estable ~0.22 en 33 años: concentrado ≪ cobre refinado. Descriptor de enclave. |
| **Zinc** | metal base | **0.296** | 0.180 | 0.444 | Estable ~0.30. |
| Plomo | metal base | 1.051 | 0.069 | 2.690 | >1 por créditos de Ag/Au en concentrado argentífero (no leer como captura). |
| Oro | precioso | 0.000 | 0.000 | 0.000 | **Artefacto de ley** (mena bruta ÷ metal puro); no informativo. |
| Plata | precioso | 0.301 | 0.000 | 1.355 | Igual artefacto; ruidoso. |
| Barita | no metálico | 1.589 | 0.662 | 4.404 | ~1 o >1: prima de frontera (grado perforación). |
| Fluorita | no metálico | 0.851 | 0.471 | 1.704 | ~1: espato flúor vs. referencia. |
| Grafito | no metálico | 0.465 | 0.216 | 2.876 | Ruidoso (natural vs. flake importada). |
| Sílice | no metálico | 1.976 | 0.157 | 14.380 | Muy ruidoso (mezcla de grados). |
| Manganeso | no metálico | 0.222 | 0.111 | 0.524 | Mena vs. referencia. |

**Interpretación.** Informativo sobre todo en **metales base** (cobre ~0.22, zinc ~0.30 estables tres décadas = enclave: se exporta concentrado, no cátodo). En **oro/plata** no aplica (artefacto de ley → usar comercio por etapa). En **no metálicos** mide prima/descuento de frontera. **Complementa** al Ghosh (discreto) aportando la dimensión temporal continua.

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/ccv_download.py` → `ccv_fill_gaps.py` (espejo) → `ccv_calc.py`. Salida: `processed/ccv_serie.csv`.

---

## 5. Comercio por etapa de procesamiento

**Qué mide.** Qué fracción del **valor exportado** de cada mineral sale como **mena/concentrado (etapa 1, crudo)** frente a etapas procesadas — descriptor directo de dónde se corta la participación en la cadena.

**Intuición.** De todo lo que México exporta de un mineral, ¿qué parte es "piedra" (mena/concentrado) y qué parte ya lleva proceso? Es la forma más directa de ver en qué escalón de la cadena se baja el país; el patrón espejo —exportar en bruto e importar procesado— lo confirma.

**Matemática.** $X\text{-share crudo}_{m,t} = X^{E1}_{m,t}\,/\,X^{\text{total}}_{m,t}$, con concordancia mineral × etapa × fracción HS (`concordancia_hs_etapa.csv`).

**Datos.** Comtrade 1992-2024 (versiones HS empalmadas → leer como tendencia). Ubicación: `processed/comercio_posicion_1992_2024.csv` y `comercio_por_etapa_1992_2024.csv`.

**Resultados — % exportado en crudo (mena/concentrado), años seleccionados:**

| Mineral | 1995 | 2000 | 2005 | 2010 | 2015 | 2020 | 2024 |
|---|--:|--:|--:|--:|--:|--:|--:|
| Cobre | 2 % | 15 % | 9 % | 33 % | 42 % | 68 % | **81 %** |
| Plomo | 17 % | 52 % | 10 % | 51 % | 84 % | 90 % | 86 % |
| Zinc | 32 % | 35 % | 26 % | 41 % | 57 % | 65 % | **80 %** |
| Manganeso | 22 % | 7 % | 4 % | 10 % | 0 % | 0 % | 0 % |
| Oro | 0 % | 7 % | 0 % | 0 % | 9 % | 8 % | 1 % |
| Plata | 2 % | 0 % | 0 % | 2 % | 0 % | 6 % | 7 % |
| Fluorita | 21 % | 21 % | 35 % | 39 % | 25 % | 35 % | 26 % |
| Grafito | 5 % | 3 % | 3 % | 2 % | 0 % | 0 % | 3 % |
| Barita | 59 % | 11 % | 79 % | 97 % | 100 % | — | 100 % |
| Sílice | 28 % | 8 % | 13 % | 32 % | 30 % | 16 % | 16 % |

**Interpretación.** Hallazgo central: el **cobre pasa de exportarse 2 % en crudo (1995) a 81 % (2024)** y el **zinc de 32 % a 80 %** — una **profundización del enclave**: cada vez se exporta en una fase más cruda. El manganeso a la inversa (0 % crudo: se transforma en ferroaleaciones dentro del país). Oro/plata y grafito casi no salen en crudo (se refinan/usan localmente, o el CCV no aplica).

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/comercio_etapa_backseries.py` → `comercio_etapa_merge.py`.

---

## 6. Destinos de las exportaciones

**Qué mide.** A qué país socio se dirige la exportación de cada mineral-etapa, y su desplazamiento en el tiempo.

**Intuición.** El "¿a quién le vende?": seguir a dónde va el concentrado revela quién hace la transformación que no ocurre aquí. Si el destino se concentra en un solo comprador (crecientemente China), el eslabón que falta en México se agrega allá.

**Datos.** Comtrade por país socio, todas las HS, 1992-2024 (`comercio_destinos_serie_resumen.csv`, 893 filas; crudo 12 677 combos). El destino es el **socio declarado**, no el consumo final (reexportación/entrepôt no depurados → caveat).

**Resultados — desplazamiento hacia Asia/China (etapa 1, concentrados):**

| Flujo | Años 1990 | Reciente |
|---|---|---|
| Cobre concentrado (E1) | EUA 100 % (1995) | **China 94 %** (2022) |
| Plomo / zinc / oro concentrado (E1) | Norteamérica/Europa | Corea y China |
| Ácido fluorhídrico (E2, procesado) | EUA | EUA (estable toda la serie) |

**Interpretación.** **Doble profundización del enclave**: no solo se exporta más crudo (§5), sino que ese crudo se concentra crecientemente en **un solo comprador (China)**, donde ocurre la transformación que no se hace en México. Los productos con algo de proceso (HF) mantienen su mercado tradicional.

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/comercio_destinos_serie.py` → `comercio_destinos_serie_resumen.py`.

---

## 7. Georreferenciación — extracción y transformación

**Qué mide.** La geografía de la cadena: dónde se **extrae** (por estado, 2024) y dónde se **transforma** (nodos metalúrgicos).

**Intuición.** El mapa de la cadena: en qué estados sale el mineral y en cuáles (pocos) se transforma. Cuando extracción y transformación caen en estados distintos, el valor "viaja" fuera del estado extractor en vez de quedarse cerca de la mina.

**Datos.** SGM, *Anuario 2025* (10 tablas «Producción minera por entidad federativa», leídas como imagen); `processed/georref_extraccion_mineral_estado_cuantitativo.csv` (93 filas) y `georref_transformacion_nodos.csv`.

**Resultados — extracción 2024, estados líderes (share de la producción nacional):**

| Mineral | 1º estado | 2º estado |
|---|---|---|
| Cobre | Sonora 70 % | Zacatecas 16 % |
| Plomo | Zacatecas 71 % | Chihuahua 17 % |
| Zinc | Zacatecas 56 % | Chihuahua 11 % |
| Plata | Zacatecas 50 % | Chihuahua 14 % |
| Oro | Sonora 32 % | Zacatecas 32 % |
| Manganeso | Hidalgo 100 % | — |
| Fluorita | San Luis Potosí 96 % | Durango 3 % |
| Grafito | Sonora 100 % | — |
| Barita | Nuevo León 59 % | Sonora 38 % |
| Sílice | Coahuila 52 % | Puebla 39 % |

**Resultados — nodos de transformación (integración vertical del extractor):** cobre → Nacozari/Cananea (Grupo México: fundición/refinación) + semis Viakable/Condumex; oro-plata y plomo-zinc → **Torreón** (Met-Mex Peñoles) + zinc en SLP (IMMSA) + baterías Clarios/LTH (NL); manganeso → Tamós/Teziutlán/Gómez Palacio (Autlán, ferroaleaciones); fluorita → Matamoros (Koura, HF).

**Interpretación.** Extracción de **especialización regional aguda**; transformación en **pocos nodos**, casi siempre de la misma firma que extrae. La distancia entre la geografía extractiva y la escasez de nodos de transformación es la **expresión espacial del enclave**.

### 7bis. Regionalización de la cadena (Paso 8)

**Qué mide.** La dimensión regional del encadenamiento: qué tan localizada está la extracción y si el valor agregado (transformación, eslabón E2) ocurre **en el mismo estado** que la extracción o se **deslocaliza**.

**Intuición.** Lleva el enclave al plano del mapa: ¿la fundición está donde está la mina, o el valor agregado se muda a otro estado (o simplemente no existe)? Es el enclave visto como distancia entre "de dónde sale" y "dónde se transforma".

**Matemática.** (i) Concentración geográfica = **Herfindahl espacial** de las cuotas estatales de extracción por mineral, $HHI_{geo,m}=\sum_r (s_{m,r})^2$ (0-10 000), con $s_{m,r}$ = share del estado $r$ en la producción nacional del mineral $m$ (2024). (ii) **Co-localización** = ¿el nodo E2 (fundición/transformación) está en el estado líder de extracción?

> [!warning] Límite de datos (declarado, no imputado)
> Una regionalización *nonsurvey* completa de la MIP nacional (cocientes de localización SLQ/FLQ/CHARM → Ghosh por estado numérico) requiere una **matriz sector × estado** (PIB estatal por actividad, PIBE de INEGI). INEGI solo la expone vía un **descargador interactivo** (119 tabulados XLSX), no accesible por script; el archivo SGM «producción minera por entidades» corresponde a **minería ampliada** (lidera Guerrero/Chiapas — incluye no metálicos/energéticos), no a los 10 minerales críticos, por lo que **no** sirve como denominador. Se entrega la regionalización **descriptiva** por mineral (rigurosa con los datos propios) y se declara pendiente el Ghosh-por-estado numérico (completable si se descarga el PIBE, como se hizo con la ICIO).

**Resultados — regionalización por mineral (2024).** Base: `processed/georref_regionalizacion.csv`.

| Mineral | HHI geográfico | Estado líder extracción | Nodo(s) E2 (transformación) | ¿E2 co-localizado? |
|---|--:|---|---|:--:|
| Grafito | 10 000 | Sonora (100 %) | Michoacán (uso siderúrgico) | no |
| Manganeso | 10 000 | Hidalgo (100 %) | Veracruz, Puebla, Durango | no |
| Fluorita | 9 158 | San Luis Potosí (96 %) | Tamaulipas (HF) | no |
| Plomo | 5 318 | Zacatecas (71 %) | Coahuila, San Luis Potosí | no |
| Cobre | 5 186 | Sonora (70 %) | **Sonora** (+ CDMX, NL) | **sí** |
| Barita | 4 907 | Nuevo León (59 %) | Campeche (uso perforación) | no |
| Sílice | 4 258 | Coahuila (52 %) | Nuevo León (vidrio) | no |
| Zinc | 3 436 | Zacatecas (56 %) | Coahuila, San Luis Potosí | no |
| Plata | 3 022 | Zacatecas (50 %) | Coahuila (Torreón) | no |
| Oro | 2 476 | Sonora (32 %) | Coahuila (Torreón) | no |

**Interpretación.** La extracción es **muy localizada** (Herfindahl espacial ≥ 5 000 en la mitad de los minerales; monopolios estatales en grafito, manganeso, fluorita). Pero **solo en el cobre** el eslabón de transformación (E2) está **en el mismo estado** que la extracción (Sonora: La Caridad/Cananea). En los **otros nueve**, el valor agregado —cuando existe— se **deslocaliza** a unos pocos hubs metalúrgicos (Torreón-Coahuila para metales preciosos y plomo-zinc; Nuevo León; Tamaulipas para el HF) o simplemente **no ocurre** (barita, grafito). Esa **desconexión espacial extracción→transformación** es la dimensión regional del enclave: los estados extractivos exportan concentrado/mineral fuera del estado, y la escasa agregación de valor se concentra en enclaves metalúrgicos distintos.

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/georref_cuantitativo.py` (extracción) y `georref_regionalizacion.py` (Paso 8). Salidas: `processed/georref_*` y `georref_regionalizacion.csv`.

---

## 8. Comparación internacional (Ghosh) — Paso 6

**Qué mide.** El encadenamiento hacia adelante del **sector-minería agregado** de México frente a **siete comparables** —Chile y Australia (los del protocolo), el clúster nórdico (Finlandia, Suecia) y, desde el Paso 6.6, **China, Brasil y Perú**—, *like-for-like*.

**Intuición.** Poner a México en la misma vara que los "referentes": ¿Chile y Australia realmente encadenan más hacia adelante, o solo son más grandes? Y con los tres añadidos: ¿a dónde va el valor que México exporta (China), es el enclave un rasgo regional (Perú, Brasil) o mexicano? Mismo método (Ghosh), mismo sector (minería), fuente homogénea — para comparar manzanas con manzanas.

**Matemática.** Idéntica al Ghosh de §3, aplicada al **bloque intra-país** (país→mismo país) de cada economía en la matriz OECD ICIO: $B=\hat{x}^{-1}Z_{cc}$, $G=(I-B)^{-1}$, $FL_i=\sum_j g_{ij}$, Rasmussen normalizado (media país = 1). Sector comparable = **B07_08** (minería no energética = menas metálicas + otra minería).

**Datos.** OECD ICIO 2023, **tres cortes 2008 · 2013 · 2018** (los mismos del Ghosh de la MIP, §3; +2020 para los 5 originales); `processed/icio_comparacion_mineria.csv`; procedencia en `Bases Originales/12 OECD ICIO/`. Script `icio_comparacion.py`.

**Por qué estos ocho países (Paso 6.6).** **China** = procesador global (destino del 94.7 % del concentrado de cobre mexicano; el extremo opuesto — dónde se captura el valor); **Brasil** = par latinoamericano por tamaño, estructura industrial y federalismo (controla efecto región y tamaño); **Perú** = vecino andino con la misma canasta polimetálica (cobre-plata-zinc-plomo-oro), para ver si el enclave es mexicano o regional.

**Resultados — encadenamiento hacia adelante de la minería no energética (B07_08; Rasmussen, media país = 1) en los tres cortes:**

| País | 2008 | 2013 | 2018 | (2020) | Lectura |
|---|--:|--:|--:|--:|---|
| **China** | 1.56 | 1.56 | **1.53** | — | el más alto: complejo metalúrgico global |
| **México** | 1.65 | 1.58 | **1.51** | 1.42 | alto los tres cortes (agregado; ver abajo) |
| **Finlandia** | 1.41 | 1.41 | **1.31** | 1.23 | integra (Ni/Co) |
| **Suecia** | 1.26 | 1.26 | **1.27** | 1.35 | integra (Boliden) |
| **Brasil** | 0.97 | 0.90 | **0.99** | — | ≈1: en el promedio propio |
| **Australia** | 0.96 | 0.82 | **0.83** | 0.91 | por debajo del promedio propio |
| **Chile** | 0.89 | 0.85 | **0.73** | 0.79 | **<1 y bajando** = enclave |
| **Perú** | 0.67 | 0.63 | **0.62** | — | **el más bajo**: enclave polimetálico |

Referencia (corte 2018) energéticos (B05_06) y servicios de apoyo (B09) en `icio_comparacion_mineria.csv`.

**Interpretación.** En los **tres cortes**, **Chile, Australia, Brasil y Perú NO son casos de éxito** en encadenamiento hacia adelante (en o por debajo del promedio de su propia economía; Chile cae 0.89→0.73; Perú es el mínimo, ~0.62). El referente real de integración es **China** (complejo metalúrgico global) y el **modelo nórdico** (Finlandia, Suecia, >1 estable). El índice de México es **alto pero engañoso**: el agregado promedia los metales que sí se funden (→ C24 metales básicos) con el cobre exportado 94.7 % en concentrado; el enclave solo aparece al desagregar (§3-§5) y en la descomposición de valor (§9). La comparación **México (1.51) ↔ China (1.53)** —Ghosh casi idéntico— es la más ilustrativa: solo el DVA (§9) los separa (crudo 0.38 vs 0.07). **Caveat de agregación**: minería agregada, no por mineral; clasificación ISIC.

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/icio_comparacion.py <ruta AAAA_SML.csv> <año>` (upsert por año; cortes 2008/2013/2018; 8 países en `PAISES`).

---

## 9. DVA / reprocesamiento — el enclave en dinero (Paso 6.5)

**Qué mide.** Cuánto valor **retiene** cada país y cuánto exporta en **crudo para reprocesarse en el extranjero** — el enclave expresado en valor agregado, sobre la matriz **global** ICIO.

**Intuición.** El enclave "en dinero": de cada unidad de valor que genera la minería y termina exportándose, ¿cuánto sale ya transformado dentro del país y cuánto sale en crudo para que otro lo procese? Un `crudo_share` alto y sostenido es el enclave medido en valor.

**Matemática.** Global: $A=Z\hat{x}^{-1}$, $L=(I-A)^{-1}$, coeficientes de VA $v_j=VA_j/x_j$. Exportaciones brutas del sector $i$: $E_i=\sum_{j\notin s} z_{ij}+\sum_{c\neq s} f_i^{c}$. Indicadores del sector minero $i_0$ del país $s$:

$$ \text{DVASH}=\frac{\sum_{k\in s} v_k (L\,e_{i_0})_k}{E_{i_0}}, \qquad
\text{crudo}=\frac{\sum_{k\in\text{minería}(s)} v_{i_0} L_{i_0 k} E_k}{\sum_{k\in s} v_{i_0} L_{i_0 k} E_k},\quad \text{reproc}=1-\text{crudo} $$

$$ \text{foreign\_abs}=1-\frac{v_{i_0}\sum_k L_{i_0 k}\,f_k^{s}}{v_{i_0}\sum_k L_{i_0 k}\,f_k^{\text{tot}}} $$

**`crudo`** = fracción del VA minero exportado que sale como producto minero directo (concentrado); **`reproc`** = la que sale ya transformada en casa (vía exportaciones de otros sectores); **`foreign_abs`** = fracción del VA minero absorbida en demanda final extranjera.

**Datos.** OECD ICIO 2023: **anual 1995-2020** para los 5 países originales (26 años × 5 × 3 sectores mineros); **China, Brasil y Perú** en los cortes 2008/2013/2018 (+2020). `processed/icio_dva_mineria.csv`. Script `icio_dva.py`. Bloques ICIO pre-2011 obtenidos por descarga manual del navegador (WAF de la OCDE bloquea `curl`).

**Resultados — `crudo_share` de la minería no energética (B07_08), ordenado del enclave más profundo al menor:**

| País | Prom. serie | Cortes MIP 08/13/18 | Lectura |
|---|--:|--:|---|
| **Perú** | **~0.96** | 0.92/0.97/0.98 | Empata a Chile: misma canasta que México, sin transformar. |
| **Chile** | **0.97** | 0.95/0.98/0.97 | Enclave extremo y **constante 26 años**. |
| Brasil | ~0.86 | 0.87/0.90/0.82 | Alto pese a Ghosh ≈1 (hierro en bruto). |
| Australia | 0.67 | 0.66/0.76/0.77 | **Se deteriora** (hierro/litio a China). |
| Suecia | 0.41 | 0.34/0.48/0.48 | Integra ~la mitad (Boliden). |
| **México** | 0.38 | 0.34/0.34/0.38 | Agregado bajo/engañoso; cíclico, repunte reciente. |
| Finlandia | 0.29 | 0.20/0.27/0.45 | El más integrado de los originales (Ni/Co). |
| **China** | **~0.07** | 0.08/0.06/0.07 | **El procesador**: funde casi todo. Extremo opuesto. |

**Resultado — México, serie anual completa `crudo_share` (B07_08):**

| Año | 1995 | 1996 | 1997 | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 |
|---|--|--|--|--|--|--|--|--|--|--|--|--|--|
| crudo | 0.24 | 0.29 | 0.32 | 0.35 | 0.39 | 0.41 | 0.41 | 0.42 | 0.41 | 0.50 | 0.51 | 0.32 | 0.33 |

| Año | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 |
|---|--|--|--|--|--|--|--|--|--|--|--|--|--|
| crudo | 0.34 | 0.37 | 0.32 | 0.36 | 0.39 | 0.34 | 0.37 | 0.38 | 0.36 | 0.35 | 0.38 | 0.43 | 0.48 |

Además, la **absorción extranjera** del VA minero de México sube de **0.21 (1995) a 0.65 (2020)**; la `dva_share` de las exportaciones mineras es alta en todos los países (~0.80-0.92) por ser minería intensiva en recurso — **no** discrimina (lo hace `crudo_share`).

**Interpretación.** En dinero, **Chile y Perú son los enclaves más profundos** (~0.97-0.98 constante); en el extremo opuesto, **China funde casi todo (0.07)** — es a donde va el valor que los demás exportan en crudo. México vuelve a ser **engañoso en el agregado** (bajo porque funde metales preciosos; oculta el cobre), pero de punta a punta se **profundiza** (crudo 0.24→0.48; absorción extranjera 0.21→0.65), coherente con §5-§6. La pareja **México (Ghosh 1.51, crudo 0.38) ↔ China (1.53, crudo 0.07)** —Ghosh casi igual, realidad opuesta— es la mejor prueba de por qué el Ghosh agregado engaña; y **Perú (misma canasta que México, crudo 0.98)** muestra que el enclave no es idiosincrásico: lo hace la (falta de) integración aguas abajo, no la dotación. El DVA **confirma el caveat de agregación**: el enclave se ve al desagregar, no en el promedio del sector.

> [!note] Reproducir / actualizar
> `py 10 Datos/scripts/icio_dva.py <ruta AAAA_SML.csv> <año>` (upsertea la fila). Requiere el CSV ICIO del año (edición 2023).

---

## 10. Síntesis — el enclave estructural en cinco indicadores

La convergencia de indicadores independientes, no un dato aislado, sostiene el diagnóstico:

1. **Encadenamiento hacia atrás bajo** en todos (extracción intensiva en recurso).
2. **Hacia adelante heterogéneo** (Ghosh), pero alto ≠ cadena (cautela §3).
3. **CCV bajo y estable** en metales base (cobre ~0.22): se exporta concentrado, no metal.
4. **% en crudo creciente** (cobre 2 %→81 %) y **destino concentrado en China**: doble profundización.
5. **DVA**: el valor se **reprocesa afuera** (Chile/Perú ~0.97-0.98; México con absorción extranjera 0.21→0.65; China lo capta, 0.07).

**Tipología descriptiva de los 10 mercados** (Cap. VI): **A** cadena local desarrollada (manganeso, fluorita); **B** truncada en el metal refinado (cobre, oro, plata, plomo, zinc); **C** usuario doméstico con eslabón importado (sílice, grafito); **D** exportación en bruto (barita). La comparación internacional (8 países) **reencuadra el «éxito»**: el referente no es Chile/Australia (ni Perú/Brasil) sino la integración mina→fundición del modelo nórdico y, en la captura de valor, China.

---

## 11. Declaración de vacíos (criterio: declarar, no imputar)

| Indicador | Vacío | Tratamiento |
|---|---|---|
| CCV | Plomo 1994 (sin espejo); oro/plata (artefacto de ley) | Declarado; oro/plata vía comercio por etapa |
| CCV (espejo) | Años rellenados son CIF | Posible sesgo al alza; marcados en la base |
| HHI | 1994-2003 solo régimen; 1992-93 no reconstruible | **Paso 7 cerrado**: 1994-2003 reconstruido para manganeso/fluorita/grafito/cobre (USGS MYB); oro/plata/plomo/zinc documentados pero declarados; 1992-93 sin solución |
| MIP | Plomo-zinc combinado; años base distintos; 2008 no comparable | Reportado conjunto; solo índices normalizados; 2008 como patrón |
| RAS por mineral | MIP a nivel Clase solo en años base | Inviable; cubierto por CCV + 3 cortes + agregado ICIO |
| Destinos | Comtrade da socio declarado | Reportado con caveat |
| Comparación internacional / DVA | ICIO agregado (no por mineral); ventana 1995-2020 | Sector-minería; colas vía comercio por etapa |
| Regionalización (Paso 8) | Ghosh-por-estado numérico requiere PIBE sector×estado (descargador interactivo INEGI) | Entregada la regionalización descriptiva (concentración geográfica + co-localización); FLQ/CHARM declarado no factible sin PIBE |
| Cierre temporal | 2025 (HHI) no publicado | Series duras cierran en 2024 |

**Pasos de la ruta:** todos cerrados (1-8, 6.5, C2, +A). El **8** (regionalización) se cerró el 2026-09-07 en su versión descriptiva rigurosa (§7bis); el **Ghosh-por-estado numérico** (FLQ/CHARM) queda declarado como no factible sin la matriz PIBE sector×estado de INEGI (descargador interactivo). El **PROTOCOLO** conserva control de cambios a la espera del asesor — único pendiente del proyecto.

---

← [[Resumen descriptivo de la investigacion (datos e indicadores)]] · [[Ruta - Completar indicadores y series (seguimiento)]] · [[Catalogo de Bases de Datos]] · [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]]
