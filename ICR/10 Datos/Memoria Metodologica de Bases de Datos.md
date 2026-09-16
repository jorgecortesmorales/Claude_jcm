---
title: Memoria Metodológica de Bases de Datos
type: datos
tags: [icr, datos, metodologia, memoria]
created: 2026-07-17
updated: 2026-07-17
status: documento-vivo
version: "1.0"
---

# Memoria metodológica de construcción de bases de datos

> [!info] Naturaleza de este documento
> Documento **vivo**: registra, en el orden lógico y secuencial de la investigación, el diseño, las fuentes, las decisiones metodológicas y las validaciones de cada base de datos del proyecto. Se actualiza con cada base nueva construida (ver §7, control de cambios). Su destino final es servir de insumo directo para la sección de datos del Capítulo VI y para el apéndice metodológico de la ICR — el texto está redactado para que pueda migrarse con edición mínima.

---

## 1. Diseño general del panel

**Unidad de observación**: el par mineral-año. El corpus son los diez minerales críticos definidos en el protocolo (barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice y zinc; justificación de selección en [[Corpus de Diez Minerales]]) y el horizonte es 1993-2025, con 1992 como año de referencia institucional (Ley Minera).

**Especificación que las bases deben alimentar** (ver [[Modelo Econometrico|Modelo Econométrico]]):

$$FL_{jt} = \beta_0 + \beta_1 HHI_{jt} + \beta_2 PrecioIntl_{jt} + \beta_3 CAPEX_{jt} + \beta_4 CapExtran_j + \alpha_j + \gamma_t + \varepsilon_{jt}$$

**Mapa de bases de datos → variables** (estado al 2026-07-17):

| # | Base | Variable(s) | Estado |
|---|---|---|---|
| B1 | Precios internacionales armonizados (USGS DS-140 + empalme) | `PrecioIntl` | ✅ Completa (§2) |
| B2 | Precios complementarios (Cochilco mensual; implícito nacional INEGI) | Robustez de `PrecioIntl`; insumo CCV | ✅ Completa (§3) |
| B3 | Producción nacional valor/volumen (INEGI) | Contexto; denominadores; validación cruzada | ✅ Completa 2000-2025 (§4.1) |
| B4 | Comercio exterior (CAMIMEX) | Insumo CCV tramo 2015-2024; Cap. IV | ✅ Completa (§4.2) |
| B5 | HHI por mineral-año | `HHI` (variable central) | ⏳ Pendiente (§5.1) |
| B6 | CAPEX de empresas dominantes | `CAPEX` | ⏳ Pendiente (§5.2) |
| B7 | Capital extranjero por mineral | `CapExtran` | ⏳ Pendiente (§5.3) |
| B8 | Matrices Insumo-Producto (INEGI, EORA/TiVA) | `FL` (Ghosh), Leontief, H-R | ⏳ Pendiente (§5.4) |
| B9 | Comtrade-BACI HS6 | Numerador del CCV | ⏳ Pendiente (§5.5) |

**Principio rector de diseño**: toda variable explicativa o de control debe ser **exógena a la estructura de mercado mexicana**, porque el poder de mercado doméstico es precisamente el mecanismo que la variable central (HHI) busca capturar. Este principio motivó las dos decisiones fundacionales de B1 (§2.2).

**Estándares de formato** (aplican a toda base procesada): CSV en UTF-8, separador coma, decimales con punto, sin separadores de miles, fechas ISO (YYYY-MM o YYYY-MM-DD), formato largo (una observación por fila) con columnas de trazabilidad (fuente, serie, método) cuando la base combina fuentes. Archivos finales en `10 Datos/processed/`; fuentes originales intactas en `10 Datos/Bases Originales/`; volcados CSV crudos de cada hoja fuente en `10 Datos/raw/csv/`.

---

## 2. B1 — Precios internacionales armonizados (`PrecioIntl`) ✅

**Archivo**: `processed/precios_usgs_anual_empalmado.csv` · 10 minerales × 1993-2025 = 330 obs. · columnas: mineral, año, precio nominal USD/t, precio en USD constantes de 1998, método, serie fuente, factor de encadenamiento.

### 2.1 Papel en el modelo y requisitos

`PrecioIntl` controla el ciclo internacional de precios de materias primas, de modo que β₁ no atribuya al poder de mercado variaciones del encadenamiento que en realidad responden al ciclo de precios (el mecanismo histórico está documentado en el Cap. III: el superciclo 2003-2015 consolidó el modelo exportador). Requisitos que la base debía cumplir: (i) cobertura de los 10 minerales, (ii) horizonte 1993-2025 sin huecos, (iii) exogeneidad respecto al mercado mexicano, (iv) definición homogénea entre minerales para que β₂ sea interpretable en el panel.

### 2.2 Decisiones de diseño y alternativas descartadas

**Decisión 1 — Se descartó el precio implícito nacional (valor/volumen INEGI) como `PrecioIntl`.** Aunque disponible mensualmente para los 10 minerales, el precio implícito incorpora el poder de mercado doméstico: en los minerales monopolizados es, en buena medida, el precio que fija el propio monopolista (caso extremo: manganeso/Autlán). Usarlo como control filtraría parte del efecto del HHI hacia β₂ y sesgaría β₁ hacia cero — un problema de endogeneidad por construcción. Se conserva únicamente como operacionalización alternativa en pruebas de robustez, convertido a USD y declarado como tal.

**Decisión 2 — Se adoptó una fuente única y armonizada (USGS DS-140) en lugar del esquema mixto "cotizaciones de bolsa para metales + USGS para no metálicos".** El esquema mixto, aunque más convencional, haría que β₂ midiera conceptos distintos según la unidad del panel (cotización LME vs. valor unitario), reproduciendo en la variable de control la misma heterogeneidad de definición que motivó descartar el precio implícito. La serie DS-140 (*Historical Statistics for Mineral and Material Commodities*, National Minerals Information Center) ofrece una definición única para los ~90 commodities que cubre: **valor unitario del consumo aparente de EE. UU., en dólares por tonelada métrica**, nominal y en dólares constantes de 1998 (deflactor: CPI-U, promedio anual, base 1998 = 163.0 — verificado empíricamente contra los propios archivos DS-140). Las cotizaciones de bolsa (Cochilco/LME) se conservan como prueba de robustez para los cinco metales.

**Caveat de exogeneidad declarable**: el valor unitario DS-140 refleja el mercado estadounidense, no una "cotización mundial". Para efectos de identificación esto es suficiente — es externo a la estructura de mercado mexicana — y tiene una virtud adicional: EE. UU. es el principal destino de exportación de la mayoría del corpus, de modo que el valor unitario de su consumo aparente es una aproximación directa al precio de destino del mineral mexicano.

### 2.3 Construcción

**Etapa 1 — Extracción DS-140** (programática, desde los 10 XLSX oficiales en `Bases Originales/06 USGS DS-140/`): series anuales 1990-último año disponible por mineral (2019 barita, 2020 cobre, 2006 fluorita, 2021 plata y plomo, 2022 el resto). Resultado intermedio: `processed/precios_usgs_anual.csv`.

**Etapa 2 — Empalme de años recientes** por **encadenamiento de razón** (*ratio splicing*), método estándar para completar series con cambio de fuente:

$$P_{jt} = S_{jt} \cdot \phi_j \quad \text{con} \quad \phi_j = \frac{P^{DS140}_{j,T^*}}{S_{j,T^*}}$$

donde $S_{jt}$ es la serie fuente del crecimiento y $T^*$ el año ancla (último traslape entre ambas). El empalme conserva el **nivel** DS-140 y adopta las **tasas de crecimiento** de la serie fuente; el factor $\phi_j$ y la fuente quedan registrados en cada fila del CSV. Series fuente por mineral: promedios anuales Cochilco (metales, 2021-2024; validados en §3), MCS 2024/2026 (no metálicos y estimaciones 2025), y Minerals Yearbook T1 (fluorita 2007-2015). Tabla completa de anclas y factores en [[Definicion de Series USGS|Definición de Series USGS]].

**Caso especial — fluorita**: EE. UU. retiene por confidencialidad ("W") el valor unitario DS-140 desde 2007. Se resolvió con doble anclaje en 2006 (único año con traslape triple): segmento 2007-2015 con el valor unitario de importaciones totales del Minerals Yearbook (factor 1.002 — la cercanía a 1 confirma que, para un mineral 100 % importado por EE. UU., el valor unitario DS-140 *es* esencialmente el de las importaciones), y segmento 2016-2025 con el valor unitario de importaciones de grado ácido de los MCS (factor 0.935). El cambio de definición se declara en el Cap. VI; nótese que el grado ácido es el relevante para México (≈70 % de la exportación mexicana de fluorita va a EE. UU.).

**Etapa 3 — Dólares constantes de los años empalmados**: deflactados con CPI-U anual del BLS (idéntico al deflactor DS-140, verificado); el CPI de 2025 (322.5) es estimación propia sujeta a revisión.

### 2.4 Validaciones realizadas

1. **Sanity de conversión**: el factor de encadenamiento del oro resultó 32,139 ≈ 32,150.7 (onzas troy por tonelada) — evidencia de que DS-140 y London Fix miden el mismo precio en unidades distintas. Plata: 32,227. Cobre: 22.59 vs. 22.05 teórico (¢/lb→USD/t; diferencia = mezcla refinado/premium).
2. **Cruce entre fuentes independientes** (Cochilco anual 2024 vs. MCS 2026): oro 2,387.4 vs. 2,388; plata 28.24 vs. 28.37; cobre LME 414.8 vs. 414.7; zinc 126.00 vs. 126.0.
3. **Flags de salto** (>±50 % anual): los 15 detectados corresponden a eventos de mercado documentados (superciclo 2004-2006, zinc 2006, plata 2011, grafito 2022, sílice 2015/2020), no a errores de extracción.
4. **Integridad**: 330 obs. exactas, sin huecos ni duplicados; continuidad verificada en todas las junturas de empalme.
5. **Spot-check manual del investigador**: 14 valores transcritos a mano (anclas y 2025e), lista en [[Definicion de Series USGS|Definición de Series USGS]]. *(Estado: en curso.)*

### 2.5 Limitaciones declarables

- **Grafito (2023-2025)**: incertidumbre de nivel elevada — la razón DS-140/flake fue 1.01 en 2021 pero 1.74 en 2022 (efecto composición por el precio del lump/chip); el anclaje estándar en el último traslape (2022) podría sobreestimar el nivel ~40 % si 2022 fue atípico. Sensibilidad disponible: anclar en 2021.
- **2025**: estimaciones oficiales USGS ("e"); revisar con el MCS 2027.
- **Fluorita 2007-2015**: el MYB advierte posible subreporte del valor de importaciones; mitigado por el anclaje, pero el nivel de ese segmento hereda la advertencia.
- La serie es **nominal por defecto** en el panel (los efectos fijos de año absorben la inflación común); la versión en constantes de 1998 está disponible para especificaciones alternativas.

---

## 3. B2 — Precios complementarios ✅

**Archivo**: `processed/precios_consolidados_mensual.csv` (6,488 obs., formato largo con serie/unidad/fuente por fila).

Dos componentes y dos papeles:
1. **Cochilco mensual (LME/COMEX/London Fix)**, 5 metales, desde 1960/1978/1989 hasta 2024. Papel: (i) fuente de crecimiento del empalme de B1; (ii) **prueba de robustez** de β₂ con la operacionalización convencional de la literatura (cotización de bolsa); (iii) frecuencia mensual disponible si alguna extensión la requiere. Fuente oficial chilena, citable.
2. **Precio implícito nacional (INEGI)**, 10 minerales, mensual 2000-2025, MXN/t, **recalculado desde las hojas primarias de valor y volumen** — la hoja "Precios v1" del archivo fuente contiene un error verificado de ×1000 en oro y plata que este recálculo corrige (ver [[Validacion de Fuentes de Precios|Validación de Fuentes de Precios]]). Papel: robustez secundaria (§2.2, Decisión 1) y validación cruzada del CCV.

---

## 4. Bases auxiliares construidas ✅

### 4.1 B3 — Producción nacional (INEGI Banco de Indicadores)
Valor (millones MXN corrientes) y volumen (t) mensuales, ene-2000 a oct-2025, exactamente los 10 minerales del corpus. CSV crudos en `raw/csv/2_produccion_y_precios/`. Limitación de cobertura: el panel inicia en 1993 pero la serie en 2000 — los años 1993-1999 requieren fuente complementaria (Anuarios SGM históricos; actividad pendiente en el tablero).

### 4.2 B4 — Comercio exterior (CAMIMEX/SGM)
**Archivo**: `processed/comercio_exterior_2015_2024.csv` (510 obs.: año, flujo, categoría, producto, marcador de agregado, USD). **Fuente primaria (precisada 2026-07-17)**: mixta — Informes Anuales de CAMIMEX **y** Anuarios Estadísticos SGM (ediciones 2016, 2020, 2024), transcripción manual del investigador desde extractos PDF, ahora archivados en `Bases Originales/04 Comercio Exterior/Extractos fuente PDF/`. Papel: insumo del CCV en el tramo reciente y de las secciones de destino de producción del Cap. IV.
**Flags**: (i) fila "Otros (No Metálicos)" de exportaciones con valores repetidos 2021-2024 (artefacto probable de transcripción); (ii) **revisiones entre ediciones detectadas**: el Informe CAMIMEX 2025 trae cifras revisadas 2021-2024 que difieren de la base (p. ej., total exportaciones 2021: 24,483.4M en el informe 2025 vs. 24,366.0M en la base, construida con ediciones anteriores) — recomendación: rehomologar todos los años a la edición más reciente disponible antes de usar B4 en el CCV; (iii) el histórico completo del CCV seguirá dependiendo de Comtrade-BACI (B9).

---

## 5. Bases pendientes (plantillas de diseño)

> [!todo] Cada subsección se completará al construir la base, siguiendo el mismo esquema de §2: papel en el modelo → decisiones de diseño → construcción → validaciones → limitaciones.

### 5.1 B5 — HHI por mineral-año (variable central) 🔨 En diseño (2026-07-17)

**Papel**: variable explicativa central; H1 predice β₁ < 0.

**Evaluación de la base existente** ("Base de Datos - Mercados Mineros"): fuentes confiables (62/71 filas de confiabilidad Alta, oficiales) pero **insuficiente como serie** — solo 11 observaciones de participación individual (casi siempre solo el líder → cota inferior s₁², no HHI), con cobertura de 0 a 4 años según mineral. **Rol reasignado**: set de validación (11 puntos con fuente), calendario de eventos corporativos (Anexo 1990-2020) para los escalones del HHI, y catálogo de empresas (universo de numeradores).

**Decisiones validadas por el usuario (2026-07-17)**:
1. **HHI de extracción como serie principal**; HHI de refinación como serie complementaria donde exista dato (plata, plomo, zinc, cobre) — el Cap. IV documenta que ambas etapas tienen estructuras radicalmente distintas.
2. Construcción **bottom-up**: participación = producción de la empresa ÷ producción nacional (volumen físico), no transcripción de porcentajes publicados (que se reservan para validación).

**Decisión validada por el usuario (2026-07-20) — base MINERA para la plata (y todos los metales)**: las participaciones del líder de plata se calculan contra la **producción minera** nacional (INEGI serie minera / USGS Minerals Yearbook T1), no contra la minero-metalúrgica. Justificación: (1) el HHI de B5 mide concentración de la **extracción** — la etapa cuya estructura de mercado es la variable central del modelo; la refinación es una serie complementaria distinta (decisión 1 de 2026-07-17), dominada casi monopólicamente por Met-Mex Peñoles, y mezclarlas contaminaría el HHI de extracción con la estructura de otra etapa; (2) **consistencia numerador/denominador**: los numeradores (producción por empresa o mina reportada por CAMIMEX/informes corporativos) son producción de mina — dividirlos entre el total metalúrgico infla las participaciones (plata 2007: mina Proaño = 45 % del total metalúrgico pero 33.3 % del minero; 2009: 36 % vs 33.2 %); (3) es la misma base ya usada en los denominadores 2010-2024 del panel (CAMIMEX narrativa minera) y en los 2004-2009 (USGS MYB), evitando un quiebre de serie en 2007-2010. **Ambas bases quedan registradas en la nota de cada fila afectada** (`Plata 2007-2010` en `hhi_numeradores.csv`, marcadas "BASE MINERA (decision 2026-07-20)"), y el % publicado por CAMIMEX se conserva como validación — divergencias entre ambos se declaran en el Cap. VI como parte de la discusión de fuentes. Cautela documentada: la serie B3 (`Volumen.csv`, segundo bloque) es minero-metalúrgica para los 5 metales pero sí minera para los no metálicos (verificado dígito a dígito contra USGS).

**Refinamiento de la Fase 3 tras el bloque 2021-2024 (2026-07-17)**: la extracción reveló que **la tabla de minas top-15 subestima a las empresas con muchas minas pequeñas**. Ejemplo verificado: cobre 2021, las minas de Grupo México en el top-15 suman 452,600 t (61.7 % nacional), pero CAMIMEX declara que la empresa produce 76.3 % (559,833 t) — la diferencia son minas menores fuera del top-15. **Regla adoptada**: el numerador del HHI por empresa se toma del **porcentaje por empresa publicado** por CAMIMEX (participación de mercado directa) cuando existe; la tabla de minas se usa para (a) derivar la participación cuando no hay % explícito (sumando minas por empresa ÷ total nacional, reconociendo que es cota inferior), (b) contar el número de jugadores, (c) validación cruzada. Esto convierte los `participacion_pct` de nivel "empresa" en la fuente primaria del cálculo.

**Procedimiento (5 fases)**:
- **Fase 0 — Inventario documental**: ✅ Informes Anuales CAMIMEX 2005-2025 disponibles en camimex.org.mx (21 ediciones; cada una reporta el año previo → anclas para 2004-2024). Los PDFs del usuario en `Minerales críticos/Exportaciones e importaciones/` resultaron ser extractos X-M (fuente de B4), no los informes completos. Pendiente: Anuarios SGM (1993-1999 y complemento), reportes corporativos (Grupo México, Peñoles, Fresnillo, Autlán en BMV/LSE; Newmont, Torex, Alamos, Equinox en TSX/NYSE).
- **Fase 1 — Denominadores**: producción nacional mineral-año. ✅ 2000-2025 (INEGI, B3); ⏳ 1993-1999 (Anuarios SGM).
- **Fase 2 — Numeradores**: producción empresa-mineral-año desde capítulos por mineral de los informes CAMIMEX + reportes corporativos (volúmenes por mina, auditados) + Anuarios SGM.
- **Fase 3 — Cálculo con convenciones declaradas**: HHI = Σsᵢ² sobre empresas identificadas; **franja residual**: cota inferior top-k, con sensibilidad (franja atomística vs. franja como una empresa); **años sin dato**: interpolación por escalones anclados en el calendario de eventos (el HHI se mueve con entradas/salidas/fusiones, no continuamente); **fusiones a mitad de año** (Newmont-Goldcorp, abril 2019): la empresa compradora hereda la participación desde el año siguiente completo, año del evento marcado con flag.
- **Casos de los no metálicos (revisado 2026-07-17 con datos año por año, a petición del usuario)**: se descartó la convención estática; se verificó la estructura en cada Informe CAMIMEX. Resultados: **manganeso** = 10,000 constante (Autlán monopolio); **fluorita** = ⟳ **duopolio hasta 2011** (Las Cuevas + Fluorita de México, reparto ~78/22) → **monopolio de grupo desde enero de 2012** (Mexichem/Orbia adquiere Fluorita de México); HHI ≈6,525 (2004-2011) → 10,000 (2012 en adelante). La fusión fue en **enero de 2012**, no 2013 (el Informe Anual CAMIMEX del año N reporta el año-dato N−1); ver [[Fluorita]]; **sílice** = ⟳ **concentrado** (Covia/GMP 74-99 %, ver §5.1.1), no fragmentado como suponía el protocolo → HHI ~5,600-9,700; **barita** = líder decreciente (Baramin 82 %→24.6 % en 2021-2024) → HHI decreciente; **grafito** = ⟳ **concentrado** (Tabla 2 del USGS: duopolio Grafitos Mexicanos + Grafito Superior hasta 2013, HHI ≈5,848; monopolio de Grafitos Mexicanos desde 2014, HHI = 10,000), no atomizado como se supuso; el numerador sale de la Tabla 2 del USGS MYB, no del Anuario SGM. El caso de contraste de baja concentración queda como decisión abierta (C-17). Denominadores nacionales de los cuatro tomados de INEGI B3 (coincidencia exacta con CAMIMEX verificada). Datos en `processed/hhi_nometalicos_2020_2024.csv`.

#### 5.1.1 Hallazgo: reclasificación de la sílice
La correspondencia INEGI "Sílice" ↔ CAMIMEX "arena sílica" es **exacta** (2021: 2,664,642 vs 2,665,000; 2022: 4,038,190 vs 4,038,200; 2023: 3,675,666 vs 3,675,600 — misma serie). Grupo Materias Primas (subsidiaria de Covia Corp., 8 plantas en México) domina 74-99 % de la producción nacional de arena sílica. Decisión validada por el usuario: sílice se reclasifica como concentrada. (El grafito, considerado inicialmente como reemplazo del caso de contraste, también resultó concentrado —ver [[Grafito]]—, por lo que el caso de contraste de baja concentración queda como decisión abierta, C-17.) Matiz: la concentración es del submercado de **sílice industrial de alta pureza** (lo que capturan las estadísticas formales); la arena común de construcción sí es fragmentada pero no aparece en INEGI/CAMIMEX. Impacto en el marco teórico documentado en [[Silice]], [[Grafito]], [[Corpus de Diez Minerales]], [[Sintesis Comparativa]].
- **Fase 4 — Validación**: contra los 11 puntos de la base del usuario y la tabla síntesis del Cap. IV.

**Granularidad de la extracción por época (decisión operativa 2026-07-18)**: dado el volumen (21 informes × 10 minerales), se adoptaron dos niveles de detalle. Para **2021-2024** (los 4 años más recientes y relevantes para la coyuntura) se capturó el **detalle por mina** (tablas top-10/15 verificadas contra imagen de página) además de la participación por empresa. Para **2020 hacia atrás**, se registra la **participación por empresa de la narrativa** (líder con %, orden de los siguientes y total top-N), que es el insumo directo del HHI y evita renderizar ~75 imágenes; los denominadores nacionales se toman de INEGI B3 salvo oro y plata (que INEGI reporta en toneladas y CAMIMEX en onzas — para esos dos se usa el % de participación publicado directamente por CAMIMEX). Consecuencia para el cálculo: el HHI de 2021-2024 se computa de la distribución completa; el de años anteriores, del líder + top-N + supuesto declarado sobre la franja residual (dominado por s₁² en los minerales concentrados, con banda de sensibilidad en los oligopolios moderados).

**Producto esperado**: `processed/hhi_anual.csv` — mineral, año, HHI_extracción, HHI_refinación (si aplica), método (directo/escalón/convención), n empresas identificadas, share del líder, cobertura de la suma de shares, fuente.

**Riesgo principal**: numeradores de los metales 1993-2004 (reportes corporativos antiguos, informes CAMIMEX no disponibles antes de 2005) — se documentará la densidad de anclas por mineral y los tramos interpolados quedarán marcados en la columna método.

### 5.2 B6 — CAPEX de empresas dominantes ⏳
- **Fuentes previstas**: informes anuales/estados financieros (Grupo México y Peñoles en BMV; Fresnillo en LSE; Newmont, Torex, Alamos, Equinox en TSX).
- **Decisiones pendientes**: asignación de CAPEX corporativo a mineral (empresas multimetal — el problema de coextracción del Cap. IV, sección IV.1); moneda y deflactación; empresas privadas sin reportes (Frisco parcial, bariteras).

### 5.3 B7 — Capital extranjero por mineral ⏳
- Proporción de capital extranjero de las empresas dominantes; en la especificación base es invariante en el tiempo (CapExtranⱼ). Decisión pendiente: si la evidencia del Cap. III (ola junior 1994-2010, Newmont 2019) justifica volverla variante en t.

### 5.4 B8 — Matrices Insumo-Producto ⏳
- **Fuentes**: MIP INEGI (2003, 2008, 2012, 2018; actualización RAS a 2020/2023); EORA/OECD TiVA para Chile y Australia (H2).
- Produce la variable dependiente principal (Ghosh) — dependencia técnica: debe completarse antes de estimar el panel.
- **Decisiones pendientes**: correspondencia entre las clases SCIAN de la MIP y los 10 minerales (la MIP no desagrega mineral por mineral en todos los casos — este será el reto central de B8).

### 5.5 B9 — Comtrade-BACI (numerador del CCV) ⏳
- Precio de exportación mexicano en frontera, HS a 6 dígitos, 1992-2025. Decisión pendiente: tabla de correspondencia HS6 → mineral (bruto vs. procesado) — insumo también para validar B4.

---

## 6. Criterios transversales de calidad

1. **Trazabilidad por fila**: toda base combinada lleva fuente/serie/método/factor en columnas.
2. **Recalcular antes que confiar**: cuando una hoja fuente trae valores derivados, se recalculan desde las columnas primarias (así se detectó el error ×1000 de "Precios v1").
3. **Validación cruzada entre fuentes independientes** siempre que exista traslape.
4. **Flags automáticos** de saltos anuales >±50 % con verificación contra eventos de mercado documentados.
5. **Spot-check humano estratificado** sobre los valores de transcripción manual (anclas y extremos), no sobre el total.
6. **Errores y advertencias se documentan, no se ocultan** — este documento y [[Validacion de Fuentes de Precios|Validación de Fuentes de Precios]] son el registro público de ambos.

---

## 7. Control de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-07-17 | Creación. §1 diseño del panel; §2 B1-PrecioIntl completa; §3 B2 complementarios; §4 B3/B4 auxiliares; §5 plantillas B5-B9. |
| 1.1 | 2026-07-17 | §5.1 B5-HHI: evaluación de la base existente (insuficiente como serie; reasignada a validación/eventos/catálogo), decisiones validadas por el usuario (extracción como principal; bottom-up), procedimiento en 5 fases, inventario Fase 0 (21 informes CAMIMEX 2005-2025 disponibles). §4.2 B4: fuente precisada (mixta CAMIMEX+SGM), flag de revisiones entre ediciones. |

← [[Home]] · [[Variables y Datos]] · [[Definicion de Series USGS|Definición de Series USGS]] · [[Catalogo de Bases de Datos|Catálogo]] · [[Validacion de Fuentes de Precios|Validación de Fuentes]]
