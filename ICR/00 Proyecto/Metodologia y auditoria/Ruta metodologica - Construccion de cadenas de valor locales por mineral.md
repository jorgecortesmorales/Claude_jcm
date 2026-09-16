---
title: "Ruta metodológica — Construcción de las cadenas de valor locales por mineral"
type: metodologia
tags: [icr, cadenas-de-valor, metodologia, ruta, filiere, gvc, insumo-producto, enclave]
created: 2026-09-08
updated: 2026-09-08
status: activo
---

# Ruta metodológica — Construcción de las cadenas de valor locales por mineral (Actividad B)

> [!info] Objetivo
> Definir un procedimiento **paso a paso, replicable y con metodología precisa** para **construir la cadena de valor local** de cada uno de los 10 minerales (barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice, zinc): mapear sus eslabones, cuantificar cada uno, ubicar **dónde la cadena se detiene dentro del país** (el punto de enclave) y clasificar el resultado en la tipología descriptiva A/B/C/D. La ruta **integra y formaliza** lo ya construido —concordancia HS por etapa, mapa de empresas de transformación, georreferenciación, encadenamientos MIP, comercio por etapa, CCV y DVA— en un método único y ordenado.

## 0. Marco y unidad de análisis

- **Enfoque**: combinación de (a) *filière* / cadena de valor sectorial (Gereffi; Kaplinsky y Morris, *Handbook for Value Chain Research*), (b) enfoque de **etapas de procesamiento** insumo-producto (Leontief/Ghosh + comercio por etapa), y (c) mapeo de actores (organización industrial). El concepto ordenador es el **enclave estructural**: capital nacional, desconexión aguas abajo.
- **Cadena de referencia (5 eslabones)**, homogénea para los 10 minerales:
  - **L0 Reservas / recurso** (dotación, ubicación).
  - **L1 Extracción y beneficio** (mina → mena/**concentrado**) = etapa comercial **E1**.
  - **L2 Fundición / refinación** (concentrado → **metal en bruto/refinado** o compuesto químico primario) = **E2**.
  - **L3 Semi-manufactura** (metal → laminados, alambrón, aleaciones, químicos intermedios) = **E3**.
  - **L4 Manufactura final / uso** (producto que incorpora el mineral: cable, batería, vidrio, acero, HF/fluoropolímeros…) = **E4** + **industrias usuarias domésticas**.
- **Unidad**: cada mineral por separado (plomo y zinc se tratan juntos donde la fuente los una, p. ej. MIP 212232). Año de referencia del *mapa*: **2024** (foto estructural); series donde existan.
- **Producto final por mineral**: una **ficha de cadena** (diagrama L0→L4 + tabla de actores + indicadores por eslabón + punto de ruptura + tipo A/B/C/D).

## Fase 1 — Definición del árbol de la cadena (concordancia física y comercial)

**Objetivo.** Fijar, para cada mineral, qué producto corresponde a cada eslabón L1-L4, con su código.
1. Partir de la **concordancia mineral×etapa×HS** existente (`processed/concordancia_hs_etapa.csv`): asigna fracciones HS a E1/E2/E3/E4. Revisar y **completar E3/E4** donde falten (p. ej. cobre: alambrón 7408, cables 8544; zinc: galvanizado; fluorita: HS 2811 HF, 3904 fluoropolímeros).
2. Mapear cada etapa HS a su **clase SCIAN** de producción (concordancia `concordancia_scian_2007_2013_minerales.csv` para L1; para L2-L4, identificar las clases SCIAN 331/325 correspondientes: 331411 fundición de cobre, 325180 químicos básicos, etc.).
3. Definir la **secuencia técnica** (qué insumo se transforma en qué producto) con coeficientes físicos de referencia (ley del concentrado, rendimiento de fundición) tomados de USGS/CAMIMEX/literatura.

**Salida.** `processed/cv_arbol_mineral.csv` (mineral, eslabón L1-L4, descripción, HS, SCIAN, coeficiente técnico, fuente).
**Validación.** Que cada fracción HS del comercio quede asignada a un solo eslabón (sin traslapes); revisar contra el análisis espejo.

## Fase 2 — Mapeo de actores por eslabón

**Objetivo.** Identificar **quién** opera cada eslabón dentro del país (empresa, capacidad, propiedad, ubicación).
1. Extender `processed/empresas_transformacion.csv` (columnas mineral, eslabón, empresa, rol, ubicación, propiedad, confianza, fuente) para cubrir **todos los eslabones L1-L4** de los 10 minerales, no solo la transformación.
2. Fuentes: informes CAMIMEX, Anuario SGM, reportes corporativos (Grupo México, Peñoles, Autlán, Baramin, Mexichem/Orbia…), directorios industriales, DENUE (INEGI) para plantas.
3. Registrar por actor: **capacidad instalada** (t/año) cuando exista, **propiedad** (nacional/extranjera/estatal — clave para "enclave clásico vs estructural"), y **estado** (ubicación).
4. Marcar **confianza** (alta/media/declarada) por dato.

**Salida.** `empresas_transformacion.csv` ampliado + `georref_transformacion_nodos.csv` (nodo, estado, empresa) por eslabón.
**Validación.** Triangular al menos dos fuentes por empresa/capacidad; declarar los eslabones sin actor identificado (= ausencia de eslabón, hallazgo).

## Fase 3 — Cuantificación de cada eslabón

**Objetivo.** Poner número a cada L1-L4: volumen, valor, valor agregado, empleo, comercio.
1. **Producción y valor** por eslabón: L1 desde USGS/CAMIMEX (volumen × precio USGS empalmado, ya en `precios_usgs_anual_empalmado.csv`); L2-L4 desde la MIP (VBP/PIB de la clase SCIAN correspondiente, método de `peso_bloque.py`) y estadística industrial (EMIM/INEGI si se requiere serie).
2. **Valor agregado y empleo** por eslabón: filas B.1bP y PT de la MIP (ya operacionalizadas en `peso_bloque.py`) para las clases SCIAN de cada eslabón.
3. **Comercio por etapa**: `comercio_por_etapa_1992_2024.csv` (X y M por E1-E4) → cuánto se exporta/importa en cada eslabón, y el **análisis espejo** (exporto crudo / importo procesado).
4. **Captura de valor**: CCV (`ccv_serie.csv`) y DVA (`icio_dva_mineria.csv`) como el valor retenido vs. reprocesado afuera.

**Salida.** `processed/cv_eslabones_cuantificado.csv` (mineral, eslabón, volumen, valor_prod, VA, empleo, X, M, año).
**Validación.** Coherencia producción↔exportación (no exportar más de lo producido + importado); reusar validaciones MIP/comercio ya hechas.

## Fase 4 — Encadenamientos y demanda intermedia (dónde se conecta la cadena)

**Objetivo.** Ver, con la MIP, **a qué industrias domésticas vende** cada mineral y con qué intensidad.
1. Tomar la **fila del mineral en la matriz Z doméstica** (`mip_demanda_intermedia_minerales.csv`): top compradores domésticos y su participación → identifica el eslabón L2/L3 real dentro del país.
2. Ghosh hacia adelante (`mip_encadenamientos_minerales.csv`) como intensidad de conexión aguas adelante; Leontief hacia atrás como conexión con proveedores.
3. Cruce con la comparación internacional (8 países, `icio_comparacion_mineria.csv`) para leer la posición relativa.

**Salida.** Para cada mineral, la lista de industrias usuarias domésticas con su peso (ya disponible; se ordena por mineral en la ficha).
**Validación.** Que el comprador principal sea consistente con el mapa de actores de la Fase 2 (p. ej. cobre → metales básicos C24 = fundición de Sonora).

## Fase 5 — Industrias usuarias y dependencia de importación (cierre aguas abajo)

**Objetivo.** Determinar si el eslabón siguiente **existe en México** o se cubre con importación.
1. **Análisis espejo** por mineral (ya en `comercio_posicion_resumen.csv`: X_share_crudo, M_share_procesado): si exporta E1 e importa E2/E3, la transformación está fuera.
2. Estimar el **tamaño de las industrias usuarias domésticas** (acero, vidrio, química, electrónica, baterías) con la MIP (VBP de las clases usuarias) para dimensionar el mercado potencial del eslabón faltante.
3. Documentar **dependencia de importación** del producto procesado (M/(consumo aparente)) donde el dato lo permita.

**Salida.** `processed/cv_cierre_aguas_abajo.csv` (mineral, eslabón_donde_se_rompe, evidencia espejo, industria usuaria, tamaño, dependencia_M).
**Validación.** Declarar los casos sin dato de consumo aparente (se aproxima con el espejo).

## Fase 6 — Georreferenciación y co-localización

**Objetivo.** Ubicar espacialmente cada eslabón y ver si están **co-localizados** (mina y planta en el mismo estado) o **deslocalizados**.
1. Reusar `georref_extraccion_mineral_estado_cuantitativo.csv` (L1) + `georref_transformacion_nodos.csv` (L2-L4) + `georref_regionalizacion.csv` (Herfindahl geográfico + bandera de co-localización).
2. Producir un **mapa de flujos** por mineral (estado de extracción → hub de transformación → puerto/frontera de exportación).

**Salida.** Ficha regional por mineral (ya sintetizada en `georref_regionalizacion.csv`; se ilustra en la ficha).

## Fase 7 — Ensamblaje de la ficha y tipología A/B/C/D

**Objetivo.** Integrar todo en una **ficha de cadena de valor por mineral** y clasificar.
1. **Ficha** (una por mineral): diagrama L0→L4 con, en cada eslabón: ¿existe en México? (sí/parcial/no), actores, volumen/valor/VA/empleo, X/M, y el **punto de ruptura** marcado.
2. **Tipología descriptiva** (criterio explícito):
   - **A — cadena local desarrollada**: L1-L3(-L4) presentes y conectados (p. ej. manganeso→ferroaleaciones Autlán; fluorita→HF).
   - **B — truncada en el metal refinado**: L1-L2 presentes, L3-L4 ausentes/exportados (cobre, oro, plata, plomo, zinc).
   - **C — usuario doméstico con eslabón importado**: hay industria usuaria pero el insumo procesado se importa (sílice/vidrio, grafito/batería).
   - **D — exportación en bruto**: se detiene en L1 (barita).
3. Regla de asignación: combinar (i) presencia de actores por eslabón (Fase 2), (ii) X_share_crudo y espejo (Fase 5), (iii) Ghosh/demanda intermedia (Fase 4).

**Salida.** 10 fichas de cadena (una por mineral) + `processed/cv_tipologia.csv` (mineral, eslabón_de_ruptura, tipo, justificación). Alimenta el Cap. VI y VIII.
**Validación.** Que el tipo asignado sea consistente con los tres criterios; declarar los casos límite (fluorita entre A y B).

## Fase 8 — Síntesis y bases de política

**Objetivo.** De las 10 fichas, derivar el patrón agregado (enclave estructural) y las **bases descriptivas de política** por tipo (dónde intervendría una política que quisiera prolongar la cadena), con el contrafactual internacional (China + modelo nórdico) del Paso 6.6.

**Salida.** Sección de síntesis (Cap. VIII) + tabla de recomendaciones por tipo A/B/C/D.

---

## Insumos ya disponibles (no reconstruir)

| Fase | Insumo existente | Archivo |
|---|---|---|
| 1 | Concordancia mineral×etapa×HS | `concordancia_hs_etapa.csv`, `concordancia_scian_2007_2013_minerales.csv` |
| 2 | Mapa de empresas de transformación (19 firmas) | `empresas_transformacion.csv`, `georref_transformacion_nodos.csv` |
| 3 | Precios, comercio por etapa, CCV, DVA, peso por eslabón (MIP) | `precios_usgs_anual_empalmado.csv`, `comercio_por_etapa_1992_2024.csv`, `ccv_serie.csv`, `icio_dva_mineria.csv`, `peso_bloque_mineria.csv` |
| 4 | Encadenamientos + demanda intermedia por mineral | `mip_encadenamientos_minerales.csv`, `mip_demanda_intermedia_minerales.csv` |
| 5 | Posición comercial y espejo | `comercio_posicion_resumen.csv` |
| 6 | Georreferenciación y co-localización | `georref_*_cuantitativo.csv`, `georref_regionalizacion.csv` |
| 7 | Tipología preliminar A/B/C/D | Cap. VI (docx) |

## Entregables nuevos que produce la ruta

1. `processed/cv_arbol_mineral.csv` (Fase 1)
2. `empresas_transformacion.csv` ampliado a L1-L4 (Fase 2)
3. `processed/cv_eslabones_cuantificado.csv` (Fase 3)
4. `processed/cv_cierre_aguas_abajo.csv` (Fase 5)
5. `processed/cv_tipologia.csv` + **10 fichas de cadena** (Fase 7)
6. Diagramas de cadena por mineral (SVG/Canvas) para los entregables.

## Caveats y decisiones metodológicas

- **Foto vs. serie**: el mapa de actores (Fase 2) es una **foto estructural 2024**, no una serie; los indicadores cuantitativos (Fase 3) sí tienen serie donde la fuente la da.
- **Plomo-zinc**: se tratan juntos en la MIP (coextracción); se separan solo en comercio (HS).
- **Capacidad instalada**: dato frágil (declarado por empresa); triangular y marcar confianza.
- **L4 (manufactura final)**: rara vez atribuible a un solo mineral (un cable de cobre, un vidrio con sílice); se documenta como industria usuaria, no como producción atribuible.
- **No es un modelo causal**: la ficha es **descriptiva** (dónde está y dónde falta la cadena), coherente con el diseño de la tesis.

← [[Ruta - Completar indicadores y series (seguimiento)]] · [[Memoria - Peso del bloque de 10 minerales (PIB, exportaciones, empleo)]] · [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]] · [[Catalogo de Bases de Datos]]
