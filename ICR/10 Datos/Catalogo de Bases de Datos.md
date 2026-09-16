---
title: Catálogo de Bases de Datos
type: datos
tags: [icr, datos, catalogo]
created: 2026-07-16
status: validado
updated: 2026-09-05
---

# Catálogo de Bases de Datos

9 archivos originales importados desde `Escritorio/Minerales críticos/Bases de datos/`, organizados por temática en `Bases Originales/` y clasificados aquí por utilidad para la ICR.

> [!tip] Versiones CSV y consolidados listos para usar
> - **Todas las hojas** (40) exportadas a CSV limpio en `raw/csv/<archivo>/<hoja>.csv` — UTF-8, decimales con punto, sin separadores de miles, fechas ISO.
> - **Precios consolidados** (Cochilco + implícito nacional recalculado): `processed/precios_consolidados_mensual.csv` (6,488 obs.).
> - **Comercio exterior consolidado**: `processed/comercio_exterior_2015_2024.csv` (510 obs.).
> - Auditoría de fuentes y flags de calidad: [[Validacion de Fuentes de Precios|Validación de Fuentes de Precios]].

**Leyenda de utilidad**: 🟢 Directa (alimenta una variable o sección específica ya definida) · 🟡 Indirecta (contexto, redacción, validación cruzada) · ⚪ Nula/auxiliar (hoja de trabajo interna, redundante, o fuera del corpus)

## 01 · Criticidad y Producción Histórica
`1. minerales críticos.xlsx`

| Hoja | Contenido | Utilidad | Nota |
|---|---|---|---|
| USA | Lista oficial de criticidad USGS/gobierno EE.UU. con clasificación de riesgo por mineral | 🟢 Directa | Fuente primaria de [[Definiciones - Mineral Critico]] y [[Corpus de Diez Minerales]] (criterio 1) |
| UE | Lista de criticidad de la Comisión Europea (Riesgo de Suministro, Importancia Económica) | 🟢 Directa | Mismo uso — criterio 1 del corpus |
| Producción | Producción minera nacional TODOS los minerales (no solo el corpus), 1998-2024, millones de pesos | 🟡 Indirecta | Útil para contextualizar el peso de los 10 minerales del corpus dentro del total minero nacional (Cap. I/II); no es fuente directa del panel (usar hoja específica del archivo 2 para eso) |
| Hoja16 | Duplicado parcial de "Producción" (12 filas) | ⚪ Nula | Parece copia de trabajo incompleta — no usar |
| 2002, 2004, 2006...2023 (11 hojas) | Cortes quinquenales/bienales de producción por mineral y tipo | 🟡 Indirecta | Series históricas útiles para validación cruzada o gráficas de evolución de largo plazo; redundantes con "Producción" consolidada |

## 02 · Producción y Precios Nacionales
`2. produccion y precios.xlsx` (convertido de .xls, fuente: INEGI Banco de Indicadores)

| Hoja | Contenido | Utilidad | Nota |
|---|---|---|---|
| Producción | Valor de producción **mensual**, 2000-2025, en millones de pesos — **los 10 minerales exactos del corpus** (Oro, Plata, Plomo, Cobre, Zinc, Manganeso, Grafito, Barita, Fluorita, Sílice) | 🟢 Directa | Insumo directo para CAPEX/valor de producción por mineral-año en [[Variables y Datos]] |
| Volumen | Volumen de producción mensual en toneladas, mismos 10 minerales | 🟢 Directa | Insumo directo — permite calcular precio implícito nacional (valor/volumen) como cruce de validación del CCV |
| Precios v1 | Precio implícito nacional (valor/volumen), MXN/ton | ⚠️ **No usar para oro/plata** | Error verificado: columnas de oro y plata infladas exactamente 1000×. El resto es correcto. Sustituida por el recálculo en `processed/precios_consolidados_mensual.csv` — ver [[Validacion de Fuentes de Precios\|Validación]] |
| Precios v2 | Consolidación mixta ya construida (Cochilco 5 metales + implícito 5 no metálicos) | 🟡 Indirecta | Valores verificados correctos; superada por el consolidado nuevo, que añade trazabilidad por serie/fuente y el histórico Cochilco completo desde 1960/1978/1989 |
| Aux. Produc. Vol. | Tabla auxiliar combinando producción y volumen | ⚪ Nula/auxiliar | Hoja de trabajo interna (formato mixto, probablemente para gráficas); usar las hojas primarias en su lugar |
| G2 Producción y volumen | Hoja auxiliar de graficación (28 filas) | ⚪ Nula/auxiliar | Solo insumo de un gráfico específico, no dataset reutilizable |

**Esta es la base de datos más directamente aprovechable del lote** — cubre exactamente el corpus de 10 minerales con periodicidad mensual 2000-2025.

## 03 · Precios Internacionales (Cochilco)
5 archivos `Precios-*-Mensual.xlsx` — Comisión Chilena del Cobre, series 1960-2024, mensuales, en USD (BML = London Metal Exchange, COMEX)

| Archivo | Mineral | Utilidad |
|---|---|---|
| Precios-del-Cobre-Refinado-Mensual.xlsx | Cobre | 🟢 Directa — candidato principal para `PrecioIntl` en el [[Modelo Econometrico\|modelo de panel]] |
| Precios-de-la-Plata-Mensual.xlsx | Plata | 🟢 Directa |
| Precios-del-Oro-Mensual.xlsx | Oro | 🟢 Directa |
| Precios-del-Plomo-Mensual.xlsx | Plomo | 🟢 Directa |
| Precios-del-Zinc-Mensual.xlsx | Zinc | 🟢 Directa |

**Cobertura parcial del corpus**: solo 5 de 10 minerales (los transados en bolsas de metales — LME/COMEX). **Manganeso, grafito, barita, fluorita y sílice no tienen serie Cochilco** — para esos 5, el protocolo ya prevé recurrir a USGS Mineral Commodity Summaries como fuente de `PrecioIntl` (ver [[Diseno Metodologico|Diseño Metodológico]]).

## 04 · Comercio Exterior
`4. balanza comercial.xlsx` — **Fuente primaria: Informes Anuales de CAMIMEX**, datos extraídos manualmente por el usuario desde los PDF (citable como Cámara Minera de México, *Informe Anual*, ediciones por año). Pendiente: spot-check de valores contra los PDF por tratarse de transcripción manual — ver [[Validacion de Fuentes de Precios|Validación]].

| Hoja | Contenido | Utilidad | Nota |
|---|---|---|---|
| Exportaciones | Exportaciones mexicanas por producto/mineral, 2015-2024, USD | 🟢 Directa | Complementa Comtrade-BACI para el [[Diseno Metodologico\|cálculo del CCV]] y las secciones "destino de la producción" del Cap. IV |
| Importaciones | Importaciones por producto, 2015-2024, USD | 🟡 Indirecta | Contexto — el corpus es de minerales que México exporta, pero útil para dimensionar dependencia en insumos relacionados |
| Balanza comercial | Saldo neto por mineral, 2015-2024 | 🟡 Indirecta | Contexto/redacción |
| EXP por producto / IMP por producto | Desagregación por producto específico, 2020-2024 | 🟢 Directa | Mayor granularidad para el CCV en el periodo reciente |
| BC por producto | Hoja con estructura irregular (encabezado "exportaciones" en cols de balanza) | ⚪ Nula/auxiliar | Revisar antes de usar — posible error de formato en el archivo original |

**Nota de cobertura temporal**: solo 2015-2024 — no cubre el horizonte completo 1992-2025 del protocolo. Sirve para el tramo reciente del CCV; el histórico completo seguirá dependiendo de Comtrade-BACI.

## 06 · USGS DS-140 (descargado 2026-07-17)
10 archivos `ds140-*.xlsx` — USGS Historical Statistics for Mineral and Material Commodities. Valor unitario del consumo aparente EE.UU., USD/t, nominal y constantes 1998, desde 1900. **Serie primaria de `PrecioIntl` para los 10 minerales** (decisión validada por el usuario). Extraído a `processed/precios_usgs_anual.csv`. Ver definiciones, cobertura por mineral y el caso especial de fluorita en [[Definicion de Series USGS|Definición de Series USGS]].

## 05 · Reservas y Producción Mundial
`3. reservas y producción mundial.xlsx`

| Hoja                            | Contenido                                                                                                           | Utilidad     | Nota                                                                                                                                                                                                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| % producción y reservas mundial | Por mineral y país: producción minera, % mundial, reservas, % reservas mundiales (un solo corte, no serie temporal) | 🟡 Indirecta | No es insumo del panel (es una foto de un año, no serie mineral-año), pero es **muy valioso para redacción**: contexto de posición mundial de México (Cap. I/IV) y para identificar los datos de Chile/Australia que requiere la comparación internacional (H2, Cap. V) |

## 10 · Matriz Insumo-Producto (MIP) INEGI (descargado 2026-07-30)
`10 MIP INEGI/` — MIP simétrica producto×producto, nivel máximo = **Clase SCIAN (6 díg.)**. Serie comparable = **2013** (base 2013) y **2018** (base 2018), datos abiertos CSV. Corte **2008** (base 2008 / **SCIAN 2007**, tabulados **Excel** en `2003_2008 historicas (no comparables)/Tabulados_mip2008.zip`) incorporado **aparte, como referencia histórica no encadenada** (814 clases; ver más abajo). **2003** (solo Sector/Subsector) y **2012** (actualización, solo llega a Rama) **descartados por mineral**. Variantes por archivo: `t`/`d`/`m` (total/doméstica/importada, precios básicos), `ctec` (coef. técnicos = A, Leontief) y `cdi` (directos+indirectos = inversa de Leontief), a 4 niveles de agregación (`_1` Sector … `_4` Clase).

| Uso | Detalle |
|---|---|
| 🟢 Encadenamientos (Obj. 1) | Leontief/Ghosh + índices Hirschman-Rasmussen por mineral — 8/10 con clase propia, plomo-zinc combinado (coextracción) |
| 🟢 Demanda intermedia doméstica (Obj. 2) | ¿qué sectores compran cada mineral? |

**Indicadores construidos** (validados contra `ctec`/`cdi` de INEGI a precisión de máquina):
- `processed/mip_encadenamientos_minerales.csv` — 9 minerales × 2 años: VBP, DI/VBP, encadenamiento atrás/adelante (Hirschman-Rasmussen normalizado), rangos.
- `processed/mip_demanda_intermedia_minerales.csv` — top compradores domésticos por mineral/año.
- Script: `scripts/mip_calc.py`. Método y resultados: [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]].
- **Referencia 2008 (archivo separado, no encadenado)**: `processed/mip_encadenamientos_2008_referencia.csv` y `processed/mip_demanda_intermedia_2008_referencia.csv` (con banderas `base_scian=SCIAN2007_base2008` y `comparabilidad=referencia`). Extraído de los `.XLSX` `_4` domésticos con `scripts/mip2008_extract.py` (intermedios en `processed/mip2008_intermedios/`) y calculado con `scripts/mip2008_calc.py`. **Validado a precisión de máquina**: `(I−A)⁻¹` vs `cdi` = 4.9e-15; `A` vs `Z/x` = 1.6e-15. ⚠️ **Caveats**: niveles no comparables (año base/precios 2008), Rasmussen no comparable en nivel entre añadas (leer patrón; se reporta Ghosh crudo y DI/VBP), manganeso 212291 más amplia en 2008. Ver §8 de la Memoria.

## 11 · Comercio por fracción HS — UN Comtrade (descargado 2026-07-30)
`11 Comercio Comtrade/` — comercio de México (reportante 484) por fracción **HS**, socio Mundo, 2015-2024, X y M, de la **API pública de UN Comtrade** (sin clave). Insumo del **Objetivo 3** (inserción por etapa de procesamiento), donde los agregados CAMIMEX (sección 04) no distinguen etapa.

| Archivo | Contenido |
|---|---|
| `Bases Originales/11 Comercio Comtrade/comercio_hs_comtrade_mx_2015_2024.csv` | crudo: anio, flujo, hs, valor_usd |
| `processed/comercio_por_etapa.csv` | mineral × etapa × flujo × año |
| `processed/comercio_posicion_resumen.csv` | totales, participación cruda vs procesada, saldo (espejo) |
| `processed/concordancia_hs_etapa.csv` | concordancia mineral × etapa × fracción HS (**revisable**) |

Scripts: `scripts/comercio_etapa.py`, `scripts/comercio_summary.py`. Método, resultados y cuidados (huecos de reporte, vintages 2019, doré≠manufactura): [[Memoria - Comercio por etapa de procesamiento (Obj 3)]].

## 12 · Empresas de transformación (Obj. 2, construido 2026-08-01)
`processed/empresas_transformacion.csv` — 19 firmas procesadoras/usuarias domésticas por mineral (eslabón, empresa, rol, ubicación, propiedad, **confianza**: sourced-USGS / verificado-web / preliminar-por-verificar). Insumo del Objetivo 2 (¿existe cadena local?). Eslabón metalúrgico desde USGS Tabla 2; Autlán (Mn) y Koura (fluorita) verificados. Veredicto por mineral en [[Memoria - Empresas de transformacion (Obj 2 - cadena local)]].

## 13 · HHI consolidado (2004-2023 el 2026-09-05; **extendido a 2024** el 2026-09-06; **a 1994-2003** el 2026-09-07)
`processed/hhi_consolidado.csv` — HHI por mineral-año **1994-2024** (188 filas). **2021-2024**: detalle por mina→grupo frente a la producción nacional (Σ cuota², residual atomístico; excluye filas agregadas → resuelve doble conteo oro/plata). **2004-2020**: solo hay participación por empresa → método aproximado (participaciones conocidas² + residual atomístico; fluorita duopolio por capacidades hasta 2011; grafito duopolio hasta 2013; monopolios manganeso/fluorita/grafito = 10,000). **1994-2003 (Paso 7)**: régimen documentado en **USGS MYB Mexico 1994-2003** (`Bases Originales/07 USGS MCS/MYB Mexico/myb-mexico-1994..2003`; `pdftotext`); reconstruidos manganeso (10000), fluorita (~6001, líder Las Cuevas ~75-80%), grafito (5848, duopolio) y cobre (grupo GM 79-85%, años con dato); oro/plata/plomo/zinc con shares de líder documentadas pero **declaradas** (nivel grupo/empresa mixto); barita/silice y 1992-93 ⛔. Script `scripts/hhi_1994_2003.py`. **Cada fila etiquetada con su `metodo`**; los niveles 1994-2020 se leen como **régimen**, no comparables en nivel con 2021-2024. Scripts `scripts/hhi_consolidado_2004_2020.py`, `hhi_2024.py`, `hhi_1994_2003.py`. Numeradores en `hhi_numeradores.csv`.
- **2024 (paso 2 ruta, 2026-09-06)**: 8 minerales (cobre, oro, plata, plomo, zinc por mina; fluorita y manganeso monopolios=10,000; **barita solo por líder → cota inferior**). **Sin 2024: sílice y grafito** (sin distribución usable → hueco declarado). ⚠️ **cobre 2024**: total nacional no impreso en el Anuario (gráfico SGM ~750-760k t) → se usó **755,000 t estimado** (marcado). Hallazgos 2024: plomo↑ (2,465) y plata↑ (1,147) por Peñasquito (Newmont); barita sigue desconcentrándose (605, solo líder).

## 14 · CCV — coeficiente de captura de valor (serie anual, construido 2026-09-05)
`processed/ccv_serie.csv` — CCV por mineral-año **1992-2025**. **Actualizado 2026-09-06 (paso 1 ruta)**: huecos rellenados por **datos espejo** (columna `fuente_numerador`=propio/espejo; caveat CIF) → 7 minerales completos 1992-2025 + plomo 33/34 (falta 1994, declarado); oro/plata sin CCV (artefacto de ley). Scripts `ccv_download.py`, `ccv_fill_gaps.py`, `ccv_calc.py`. `CCV = valor unitario de exportación en bruto E1 (USD/t) ÷ precio del producto de referencia USGS (USD/t)`. **Numerador**: `Bases Originales/11 Comercio Comtrade/comercio_e1_valor_peso_comtrade_mx_1992_2025.csv` (valor **y peso** de las fracciones E1, descargado de UN Comtrade para toda la serie). **Denominador**: `precios_usgs_anual_empalmado.csv`. Informativo en metales base (cobre ~0.22, zinc ~0.30); no informativo en oro/plata (artefacto de ley); ~1 en no metálicos. Scripts `scripts/ccv_download.py` y `scripts/ccv_calc.py`. Método y caveats: [[Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)]].

## 15 · Georreferenciación y destinos (construido 2026-09-06)
- `processed/georref_extraccion_mineral_estado.csv` — estados productores por mineral (cualitativo, líder + otros).
- **`processed/georref_extraccion_mineral_estado_cuantitativo.csv` (paso 5, 2026-09-06)** — producción por mineral×entidad **2024** con participación (%); del SGM Anuario 2025 (tablas "Producción por entidad", leídas como imagen). Script `scripts/georref_cuantitativo.py`. **Hallazgo**: extracción muy concentrada geográficamente (Zacatecas plata/plomo/zinc; Sonora cobre/oro/grafito; SLP fluorita 96%; Hidalgo manganeso 100%; NL+Sonora barita; Coahuila+Puebla sílice). Corrige líderes de barita (NL) y sílice (Coahuila/Puebla). `sgm_6_...csv` da valor minero total por estado 2019-2023.
- `processed/georref_transformacion_nodos.csv` — nodos de transformación por mineral/eslabón/estado (derivado del directorio de 19 empresas).
- `processed/comercio_destinos_mineral_etapa.csv` — **destinos de exportación** por mineral×etapa (UN Comtrade, socio, acum. 2019-2024). Hallazgo: concentrado de cobre **94.7% a China**; concentrados de plomo/zinc/preciosos a Asia/Europa; procesados y no metálicos a EUA. Script `scripts/comercio_destinos.py`.
- **Serie temporal de destinos 1992-2024 (paso 3 ruta, 2026-09-06)**: `processed/comercio_destinos_serie_resumen.csv` (top destino y share China/EUA por año) + crudo `Bases Originales/11 Comercio Comtrade/comercio_destinos_serie_crudo.csv`. Scripts `comercio_destinos_serie.py` + `comercio_destinos_serie_resumen.py`. **Hallazgo**: los concentrados se desplazaron de Norteamérica/Europa (1990s) a **Asia/China** (cobre E1: EUA 100% 1995 → China 94% 2022); HF sigue a EUA. Ver [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]] §3.1.

## 16 · Comercio por etapa — serie larga 1992-2024 (construido 2026-09-06)
- `processed/comercio_por_etapa_1992_2024.csv` y `processed/comercio_posicion_1992_2024.csv` (X_share_crudo por mineral-año). Rellena el vacío pre-2015 del comercio por etapa (antes 2015-2024). Scripts `scripts/comercio_etapa_backseries.py` (descarga) + `comercio_etapa_merge.py` (empalme). **Caveat**: versiones HS a lo largo del periodo → leer como tendencia.

## 17 · Comparación internacional Chile/Australia (construido 2026-09-06)
- Memoria [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]]: documentación de extracción/transformación y evidencia de encadenamientos (literatura citada). Hallazgo: ni Chile ni Australia son "éxito" en encadenamiento hacia adelante (Chile exporta ~94% de concentrado; Australia fuerte hacia atrás/METS, débil adelante). **Coeficientes propios computados en §18 (Paso 6).**

## 18 · OECD ICIO 2023 — coeficientes de minería comparados (Paso 6, construido 2026-09-06; **3 cortes 2026-09-07**; **8 países 2026-09-08**)
- Fuente **OECD ICIO 2023** (77 economías × 45 industrias ISIC Rev.4). Procedencia y extracto en `Bases Originales/12 OECD ICIO/` (`README…` + `bloques_domesticos_mineria_{2008,2013,2018,2020}.csv`). **CSV completos (~68 MB c/u) NO conservados** (re-descargables del S3/fileview del OCDE).
- `processed/icio_comparacion_mineria.csv` (87 filas): encadenamientos (Ghosh forward / Leontief backward, Rasmussen media país=1) del sector-minería para **8 países: MEX, CHL, AUS, FIN, SWE (2008/2013/2018/2020) + CHN, BRA, PER (2008/2013/2018)** — Paso 6.6, sectores B05_06/B07_08/B09. Script `scripts/icio_comparacion.py <csv> <año>` (upsert por año; `PAISES` con 8 códigos).
- **Sector comparable = B07_08 (minería no energética)**. Forward Rasmussen 2008/2013/2018: CHN 1.56/1.56/1.53, MEX 1.65/1.58/1.51, FIN 1.41/1.41/1.31, SWE 1.26/1.26/1.27, BRA 0.97/0.90/0.99, AUS 0.96/0.82/0.83, CHL 0.89/0.85/0.73, PER 0.67/0.63/0.62. **Justificación de los 3 añadidos**: China (procesador global, destino del Cu), Brasil (par latinoamericano por tamaño), Perú (vecino andino, misma canasta polimetálica). **Caveat**: agregado, no por mineral; ISIC ≠ SCIAN → comparar posición relativa, no niveles absolutos.

## 19 · OECD ICIO — DVA / reprocesamiento (Paso 6.5, construido 2026-09-06, serie completa 2026-09-07; **8 países 2026-09-08**)
- `processed/icio_dva_mineria.csv`: descomposición de valor agregado de la minería (B05_06/B07_08/B09) para **8 países: MEX, CHL, AUS, FIN, SWE anual 1995-2020 + CHN, BRA, PER en 2008/2013/2018/2020**. Columnas: `exgr_musd`, `dva_share`, `vax_mineria_musd`, **`crudo_share`** / `reproc_domestico_share`, `foreign_abs_share`. Auto-computado de la matriz **global** ICIO 2023 (método Leontief global), script `scripts/icio_dva.py`. Bloques ICIO 1995-2010 obtenidos por descarga manual del navegador (curl bloqueado por WAF de la OCDE); CSVs completos (~62-68 MB c/u) NO conservados.
- Mide el enclave **en dinero**: `crudo_share` = fracción del VA minero exportado que sale como producto minero directo (concentrado) a reprocesarse afuera. **B07_08, corte 2018**: Perú 0.98, Chile 0.98, Brasil 0.82, Australia 0.77, Suecia 0.48, Finlandia 0.45, México 0.38 (crudo 0.24→0.48 1995-2020; absorción extranjera 0.21→0.65), **China 0.07** (procesa casi todo). **Clave**: México (Ghosh 1.51, crudo 0.38) ↔ China (1.53, crudo 0.07) = Ghosh casi igual, realidad opuesta.
- **Cobertura**: serie ICIO completa 1995-2020; fuera de ventana 1992-94 y 2021-25 → proxy `comercio_por_etapa_1992_2024.csv`. Validación: `reproc+crudo=1` (390 filas, 0 violaciones) + validez de cara (petróleo/carbón en crudo). Ver [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]] §5.

## 20 · Regionalización de la cadena (Paso 8, construido 2026-09-07)
- `processed/georref_regionalizacion.csv` (10 filas): por mineral, **Herfindahl geográfico** de la extracción (Σ cuota estatal², 2024), estado líder, nodos de transformación E2 y bandera de **co-localización** extracción↔E2. Script `scripts/georref_regionalizacion.py`; fuentes `georref_extraccion_mineral_estado_cuantitativo.csv` + `georref_transformacion_nodos.csv`.
- Hallazgo: extracción muy localizada; **solo el cobre** tiene E2 co-localizado (Sonora); 9/10 con transformación deslocalizada (Torreón-Coahuila, NL, Tamaulipas) o ausente = enclave regional.
- **⛔ Declarado**: el Ghosh-por-estado numérico (FLQ/CHARM) requiere la matriz **PIBE sector×estado** de INEGI (descargador interactivo, 119 tabulados); no accesible por script. El SGM `09 SGM Anuarios/sgm_6_Produccion_Minera_Por_Entidades…csv` es minería **ampliada** (no los 10 minerales) → no sirve de denominador para el LQ. Ver resumen metodológico §7bis.

## 21 · Peso HISTÓRICO del bloque de 10 minerales — exportaciones/producción/PIB/empleo (Actividad A, construido 2026-09-08)
- **Series históricas** (`scripts/peso_bloque_historico.py`):
  - `processed/peso_bloque_hist_exportaciones.csv`: **1992-2024**, valor del bloque (Comtrade) y **% de las exportaciones totales de México** (denominador Banco Mundial `TX.VAL.MRCH.CD.WT`, coincide con INEGI). Peso oscila **1.18 % (mín. 2002) → 5.52 % (pico 2011) → 2.22 % (2024)**; tres fases (dilución TLCAN / superciclo / meseta). CAGR 8.1 % (1992-2024); 22.6 % (2003-2013); −1.0 % (2013-2024).
  - `processed/peso_bloque_hist_produccion.csv`: **valor de producción 1992-2022** (volumen × precio USGS empalmado, normalizado a t; col `anio_completo`). Volúmenes: **1992-2003 y 2019-2022 USGS MYB**, **2004-2018 CAMIMEX** (`hhi_numeradores`); empalmes validados en 2003/2004 y 2018/2019 (USGS 2018 = CAMIMEX en 8/10 minerales). ×9.4 (1992→2018) = **volumen ×3.07 × precio ×3.06** (aporte parejo; empuje de precio en 2004-2013); ×13 a 2022. Composición: **oro 6%→30%** (1992→2018, gran ascenso), plata alta y estable ~19%, cobre 38%→30%, zinc/plomo descienden. **2023-2024** aún no publicados en USGS MYB (cubiertos por exportaciones). **⚠ CORRECCIÓN 2026-09-09**: la plata/oro de `hhi_numeradores` están en **millones de onzas troy** (no toneladas); el cotejo con USGS lo detectó y se corrigió la conversión (1 M oz = 31.1035 t) — antes subvaluaba la plata ~31×.
  - `processed/produccion_nacional_myb_pre2004.csv` (120 filas, 1992-2003) y `produccion_nacional_myb_2019_2022.csv` (2019-2022): producción nacional USGS MYB Tabla 1 (t; oro/plata de kg, fluorita de miles t = acid+metalúrgico, manganeso = contenido Mn), col `fuente` (xls vs imagen). Script `scripts/myb_produccion_pre2004.py`. Validado: 1998 coincide entre `.xls` e imagen; 1999-2002 entre capítulos 2002 y 2003; 2018 USGS = CAMIMEX en 8/10.
- **Benchmarks PIB/empleo** (`scripts/peso_bloque.py` → `peso_bloque_mineria.csv`): MIP 2013/2018, filas B.1bP (PIB), P.1 (VBP), PT (empleo). Bloque = **0.70-0.71 % del PIB nacional**, **~60-65 % del PIB de minería 212**; empleo **0.07-0.10 % y decreciente** (59.5k→42.2k). 4 metales = ~94 % del PIB del bloque; 6 minerales entran por criticidad.
- **Gráfica**: `13 Entregables/png_charts/peso_historico.png` (2 paneles: exportaciones+share 1992-2024; producción precio vs volumen 2004-2018).
- **Caveat clave**: PIB por mineral solo en cortes MIP (no hay serie anual por clase SCIAN); producción completa 1992-2022. Memoria: [[Memoria - Peso del bloque de 10 minerales (PIB, exportaciones, empleo)]].

## 22 · MIP Multi-Estatal INEGI 2018 — Ghosh por estado de la minería (Paso 8 numérico, construido 2026-09-09)
- **Base original**: INEGI, *COU y MIP Multi-Estatales de México 2018* (comunicado 236/24, abr-2024). `Bases Originales/13 MIP Estatal INEGI/todos_2018.zip` (398 MB, 677 tablas; 35 industrias × 78 productos por entidad; versiones estatal/birregional/multiestatal). Descargado con `curl` de `inegi.org.mx/contenidos/investigacion/coumip/tabulados/todos_2018.zip`. Extraídas las 32 `mip_ixi_e_<edo>_intra_2018.xlsx` (industria×industria intra-estatal).
- `processed/ghosh_estatal_mineria.csv` (32 filas): por entidad, del sector **21-2 minería no petrolera**: `vbp_mineria_mdp`, `share_vbp_estatal_pct`, **`forward_rasmussen`** (Ghosh hacia adelante intra-estatal, media estado=1) + rango/35, `backward_rasmussen`, y **`fuga_export_share`** (% del producto minero exportado fuera del estado = inter-estatal + internacional). Script `scripts/ghosh_estatal.py`; método idéntico al nacional (B=Z/x fila, G=(I−B)⁻¹, forward=rowsum). Gráfica `13 Entregables/png_charts/ghosh_estatal.png`.
- **Hallazgo (enclave regional, con dato I-O)**: solo **Coahuila (fuga 32 %, fwd 1.61), Sonora (39 %, 1.41) y San Luis Potosí (53 %, 1.40)** integran localmente (fundición co-localizada); **Zacatecas (10.2 % de su economía, fuga 84 %) y Durango (7.0 %, 77 %)** —los estados más mineros— y el resto exportan **76-95 % en bruto**. Confirma numéricamente la co-localización de georref (§20).
- `processed/ghosh_interestatal_mineria.csv` (32 filas): **Ghosh INTER-ESTATAL** con la **MIP birregional** (`mip_ixi_br_<edo>_d`, entidad + resto del país, 2×35 industrias, flujos inter-estatales endógenos). Script `scripts/ghosh_interestatal.py`; gráfica `ghosh_interestatal.png`. Descompone el producto minero de cada estado en `intra_share` / `inter_estatal_share` (a industria de otros estados = cadena nacional) / `final_nacional_share` / **`export_abroad_share`** (fuga real al extranjero), + `forward_rasmussen_br`. **Reencuadre**: la fuga intra-estatal exagera el enclave; el **enclave real (al extranjero)** se concentra en **Chihuahua 76 %, Guerrero 59 %, Zacatecas 53 %**; Durango manda 46 % a otros estados (cadena nacional), SLP 48 % con solo 1 % afuera. Existe una **cadena metalúrgica nacional inter-estatal** (extractivos → fundición de Coahuila/SLP/NL).
- **Caveat**: 35 industrias (minería agregada, no por mineral); el birregional agrega el «resto del país» (no dice a qué estado; el detalle estado-a-estado requiere la MIP multiestatal 1120×1120 del mismo `.zip`, pendiente). Ver [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]] §3bis-3ter.

← [[Home]] · [[Variables y Datos]] · [[Diccionario de Variables]]
