---
title: "Auditoría de indicadores — justificación, matemática y límites"
type: metodologia
tags: [icr, metodologia, indicadores, auditoria, reproducibilidad]
created: 2026-09-15
updated: 2026-09-15
status: activo
---

# Auditoría de indicadores

> [!info] Qué es esto
> Revisión completa de **todos** los indicadores y cálculos del proyecto (no solo los coeficientes de encadenamiento). Para cada uno: **qué mide · matemática · fuente y operacionalización · supuestos · límites · por qué se incorpora · base y script**. Es el insumo del **Capítulo III (Marco metodológico y analítico)** definido en [[Arquitectura del documento (estructura expositiva)]], y el criterio de admisión de todo cuadro/figura al texto (ninguno entra sin su justificación). Fuentes: [[Catalogo de Bases de Datos]], las memorias y los scripts de `10 Datos/scripts`.

Criterio transversal (aplica a todos): **declarar, no imputar**. Los huecos de serie se explicitan y, cuando se completan, se marca con qué (p. ej. comercio espejo); nunca se rellenan con supuestos.

Notación de eslabones: **L0** recurso · **L1** extracción/beneficio · **L2** fundición-refinación o química primaria · **L3** semimanufactura · **L4** manufactura final. Equivalen a las etapas comerciales **E1–E4** (L1–L4).

---

## Grupo 0 — Insumos base (alimentan a otros indicadores)

### 0.1 Precios USGS empalmados
- **Qué mide.** Precio anual de referencia del producto refinado de cada mineral, 1992-2025, en USD/t (nominal y constante 1998).
- **Matemática.** Empalme de series del USGS (*Minerals Yearbook*, *unit value*) por factor de enlace en años de traslape; deflactor propio a 1998.
- **Fuente / operacionalización.** `precios_usgs_anual.csv` → `precios_usgs_anual_empalmado.csv` (col. `metodo`, `serie_fuente`, `factor`); mensual en `precios_consolidados_mensual.csv`.
- **Supuestos.** Continuidad del producto de referencia entre ediciones del USGS.
- **Límites.** El "producto de referencia" es un grado específico; no representa toda la heterogeneidad de grados.
- **Por qué se incorpora.** Es el **denominador del CCV** (0.1 → 3.1) y la base para valorar producción (0.2). No es un resultado en sí; es infraestructura.

### 0.2 Producción nacional y peso del bloque
- **Qué mide.** Relevancia económica del bloque de 10 minerales: participación en **PIB**, **exportaciones** y **empleo**, y descomposición del valor de producción entre **precio** y **volumen**, a lo largo de 1992-2024.
- **Matemática.**
  - Valor de producción: $V_{m,t}=Q_{m,t}\cdot p_{m,t}$ (volumen × precio empalmado).
  - Descomposición precio/volumen entre $t_0$ y $t_1$: índice de volumen $\prod (Q_{t_1}/Q_{t_0})$ y de precio $\prod(p_{t_1}/p_{t_0})$.
  - Participaciones: bloque / total nacional (PIB de la MIP; exportaciones sobre total Banco Mundial).
- **Fuente / operacionalización.** `peso_bloque_mineria.csv` (PIB/VBP/empleo, MIP 2013/2018), `peso_bloque_hist_produccion.csv`, `peso_bloque_hist_exportaciones.csv`, `peso_bloque_exportaciones.csv`. Scripts `peso_bloque.py`, `peso_bloque_historico.py`.
- **Supuestos.** Comparabilidad de volúmenes USGS (pre-2004) con CAMIMEX (2004-2018).
- **Límites.** PIB solo en dos cortes de MIP (2013/2018); empleo idem.
- **Por qué se incorpora.** Es la **justificación del objeto** (Cap. I): el bloque pesa ~0.7 % del PIB pero ~60-65 % del PIB minero no petrolero y ~77 % de las exportaciones mineras; el crecimiento traccionado por precios sin empleo anticipa el enclave. Justifica describir *estos diez*.

---

## Grupo 1 — Concentración de mercado (HHI)

### 1.1 HHI de concentración extractiva
- **Qué mide.** Concentración de la producción por mineral (estructura de mercado extractiva).
- **Matemática.** $\text{HHI}=\sum_i s_i^2$, con $s_i$ la participación de la empresa/mina $i$ (en puntos, escala 0–10 000).
- **Fuente / operacionalización.** Numeradores empresa/mina en `hhi_numeradores.csv` (CAMIMEX + USGS, con página y fuente); serie en `hhi_consolidado.csv` (col. `metodo`, `cobertura_pct`, `nota`); no metálicos en `hhi_nometalicos_2020_2024.csv`. Scripts `hhi_2024.py`, `hhi_consolidado_2004_2020.py`, `hhi_1994_2003.py` (agenda).
- **Supuestos.** 2004-2020 **reconstruido por régimen** (líder + grupos conocidos, residual atomístico) = **cota inferior**; 2021-2024 por mina.
- **Límites.** Los niveles 2004-2020 **no son estrictamente comparables** con 2021-2024; se lee por trayectoria, no por nivel exacto. Sílice sin 2024.
- **Por qué se incorpora.** Es uno de los tres descriptores de la tipología (Cap. VIII). **Hallazgo clave**: la concentración **no covaría** con el grado de transformación (minerales con HHI máximo tienen Ghosh alto y otros muy concentrados se exportan en bruto) → la estructura de mercado, por sí sola, no explica el enclave; es descriptor, no causa.

### 1.2 HHI geográfico (complementario)
- **Qué mide.** Concentración **territorial** de la extracción entre entidades (cuán localizada está la producción de cada mineral).
- **Matemática.** Mismo índice sobre participaciones estatales $s_{estado}$.
- **Fuente.** `georref_regionalizacion.csv` (col. `hhi_geografico`, `n_estados`, `share_lider_pct`).
- **Por qué se incorpora.** Da la **dimensión espacial del enclave** (Cap. VIII): extracción hiperconcentrada por estado frente a escasos nodos de transformación. Complementa al HHI de mercado (1.1) sin sustituirlo.

---

## Grupo 2 — Encadenamientos insumo-producto (MIP nacional)

### 2.1 Modelo de demanda de Leontief (hacia atrás)
- **Qué mide.** Cuánto **tracciona a proveedores** cada mineral.
- **Matemática.** Coeficientes técnicos $a_{ij}=z_{ij}/x_j$; $\mathbf{A}$; inversa de Leontief $\mathbf{L}=(\mathbf{I}-\mathbf{A})^{-1}$; encadenamiento hacia atrás $=\sum_i l_{ij}$ (suma de columna).
- **Supuestos.** Proporciones técnicas fijas (Leontief, 1941).
- **Por qué se incorpora.** Muestra el patrón común: **arrastre hacia atrás bajo** (extracción intensiva en recurso). Contexto necesario del hacia-adelante.

### 2.2 Modelo de oferta de Ghosh (hacia adelante) — indicador central
- **Qué mide.** Hacia dónde se **distribuye** la producción; si alimenta industria transformadora doméstica.
- **Matemática.** Coeficientes de distribución $b_{ij}=z_{ij}/x_i$; $\mathbf{G}=(\mathbf{I}-\mathbf{B})^{-1}$; hacia adelante $=\sum_j g_{ij}$ (suma de fila).
- **Supuestos.** Coeficientes de distribución fijos; interpretación más defendible como **modelo de precios** (Dietzenbacher, 1997). Aquí, **descriptor de posición estructural**, no mecanismo causal.
- **Por qué se incorpora.** Es el **indicador central** del diseño: describe si existe cadena aguas abajo. **Se lee con cinco cautelas** (Cap. VI): (i) mide amplitud de industrias usuarias, no valor retenido; (ii) un valor alto puede ser un solo eslabón; (iii) no distingue insumo nacional del importado; (iv) sensible a clasificación/año base; (v) descansa en supuestos del modelo. **Nunca se lee solo**: se cruza con CCV, comercio por etapa y empresas.

### 2.3 Índices de Hirschman-Rasmussen (normalización)
- **Qué mide.** Encadenamientos comparables entre ramas (poder y sensibilidad de dispersión).
- **Matemática.** Cada suma sectorial dividida entre el promedio de todas las sumas ⇒ media = 1. Valor > 1 = por encima del promedio de la economía.
- **Por qué se incorpora.** Hace **comparables** los minerales entre sí y entre cortes; es la métrica en que se reportan 2.2 y 2.1.

### 2.4 Demanda intermedia doméstica (DI/VBP y compradores)
- **Qué mide.** Qué fracción de la producción va a uso intermedio interno y **qué sectores** compran cada mineral.
- **Matemática.** $DI/VBP$ y participaciones de la fila del mineral en la matriz de flujos.
- **Fuente.** `mip_demanda_intermedia_minerales.csv`.
- **Por qué se incorpora.** **Da sentido** al Ghosh: distingue procesamiento metalúrgico (un eslabón: oro, plata, cobre → fundición/refinación) de cadena larga; localiza dónde se interrumpe la cadena (p. ej. fluorita→cemento subestima la cadena fluoroquímica intra-firma).

### 2.5 Encadenamiento por eslabón (extracción / refinación / semimanufactura)
- **Qué mide.** Si el arrastre hacia adelante **se sostiene al descender** por la cadena (L1→L2→L3).
- **Matemática.** Ghosh-Rasmussen calculado por separado para las clases SCIAN 331… (refinación) y semimanufactura de cada mineral.
- **Fuente.** `mip_encadenamientos_eslabones.csv`. Script `mip_eslabones.py`.
- **Por qué se incorpora.** **Vuelve visible el enclave dentro del propio índice**: el cobre refina 1.37 pero cae a 0.95 en semis; la refinación de preciosos (331412) tiene Ghosh 0.62. Si el arrastre probara cadena desarrollada, debería crecer; se observa lo contrario.

### 2.6 Corte de referencia 2008 (profundidad histórica)
- **Qué mide.** Un tercer punto (MIP 2008) como **referencia histórica no encadenada**.
- **Fuente.** `mip_encadenamientos_2008_referencia.csv`, `mip_demanda_intermedia_2008_referencia.csv`.
- **Límites.** No forma serie comparable (mezcla cambio real con cambio de año base/clasificación); el manganeso 2008 no es comparable (clase 212291 agrupa vecinos). Se lee por **patrón y orden**, no por nivel.
- **Por qué se incorpora.** Muestra que el mapa de eslabonamientos es **estructural y persistente**, no de un solo año.

> **Validación (todos los MIP).** La matriz $\mathbf{A}$ reproduce el archivo publicado por INEGI y $\mathbf{L}$ los coeficientes directos e indirectos, con diferencias de $10^{-15}$ (precisión de máquina). Script `mip_calc.py`; base `mip_encadenamientos_minerales.csv`. Límite estructural: la MIP **no separa plomo de zinc** (clase 212232) → encadenamientos conjuntos.

---

## Grupo 3 — Captura de valor en el tiempo

### 3.1 Coeficiente de captura de valor (CCV), serie 1992-2025
- **Qué mide.** Versión **continua** del encadenamiento hacia adelante: cuánto del valor del producto refinado capta la forma **bruta** que México exporta.
- **Matemática.** $CCV_{m,t}=\dfrac{v^{E1}_{m,t}}{p^{USGS}_{m,t}}$, con $v^{E1}$ = valor unitario de exportación de la forma bruta (etapa 1) y $p^{USGS}$ = precio refinado empalmado. CCV→1: la forma bruta ya vale casi como el refinado; CCV→0: capta poco (mayor distancia al eslabón procesado).
- **Fuente.** `ccv_serie.csv` (col. `valor_unitario_export_usd_t`, `precio_refinado_usgs_usd_t`, `ccv`, `fuente_numerador`, `nota`). Scripts `ccv_download.py`, `ccv_calc.py`, `ccv_fill_gaps.py`. Numerador UN Comtrade E1; denominador USGS.
- **Supuestos / límites.** Solo es informativo en **metales base** (cobre, zinc): brecha estable ≈0.22-0.30 = captura no realizada (**hallazgo fuerte** del enclave). En plomo el concentrado argentífero contamina (créditos de plata); en oro/plata es artefacto de ley (no informativo → se usa comercio por etapa); en no metálicos oscila ≈1 (mide primas de grado). Años completados por **espejo** son CIF (posible sobrestimación). Hueco no completable: plomo 1994 (se declara, no se imputa).
- **Por qué se incorpora.** Aporta la **dimensión temporal continua** que los dos cortes de la MIP no dan; complementa al Ghosh sin sustituirlo.

---

## Grupo 4 — Comercio por etapa de procesamiento

### 4.1 Concordancia HS × etapa
- **Qué mide / operacionaliza.** Asigna cada fracción HS a una etapa E1–E4 de cada mineral.
- **Fuente.** `concordancia_hs_etapa.csv` (30 filas). Base de 4.2-4.4.
- **Por qué se incorpora.** Es la **operacionalización** que permite leer el comercio por grado de transformación (no por producto suelto).

### 4.2 Comercio por etapa (serie 1992-2024) y posición
- **Qué mide.** Exportaciones/importaciones por etapa; **posición comercial** (share exportado en crudo vs. procesado).
- **Matemática.** $X\_share\_crudo = X_{E1}/X_{total}$; simétrico para procesado e importaciones.
- **Fuente.** `comercio_por_etapa_1992_2024.csv`, `comercio_posicion_1992_2024.csv`, `comercio_posicion_resumen.csv`. Scripts `comercio_etapa*.py`.
- **Por qué se incorpora.** Es el **tercer descriptor** de la tipología (exportación en bruto) y evidencia directa del truncamiento: se exporta E1, se importa E3-E4.

### 4.3 Destinos de exportación (geografía del comercio)
- **Qué mide.** A **quién** se exporta cada etapa, y su desplazamiento en el tiempo.
- **Fuente.** `comercio_destinos_mineral_etapa.csv`, `comercio_destinos_serie_resumen.csv` (col. `share_china`, `share_eua`). Scripts `comercio_destinos*.py`.
- **Límites.** Socio **declarado** de Comtrade (reexportación/entrepôt no depurados) — no altera la dirección del desplazamiento.
- **Por qué se incorpora.** Muestra la **doble profundización del enclave**: fases cada vez más crudas y destino cada vez más concentrado en China (cobre concentrado: 100 % EE.UU. 1995 → 94 % China 2022).

---

## Grupo 5 — Cadena de valor local (empresas y fichas)

### 5.1 Empresas de transformación
- **Qué mide.** ¿Existe eslabón de transformación local?, ¿quién y dónde?
- **Fuente.** `empresas_transformacion.csv` (col. `rol`, `ubicacion`, `propiedad`, `confianza`, `fuente`); estructura industrial en `myb_estructura_industria.csv`.
- **Por qué se incorpora.** **Corrige el dato sectorial**: buena parte de la cadena ocurre **intra-firma** (integración vertical) invisible en la MIP (caso fluorita→HF). Aporta el nivel de empresa (Objetivo 2).

### 5.2 Fichas de cadena L0–L4 y cuantificación por eslabón
- **Qué mide.** Cada mercado descompuesto en eslabones, cuantificados (VBP, PIB, empleo desde MIP; X/M por etapa) con el **punto de ruptura**.
- **Fuente.** `cv_arbol_mineral.csv`, `cv_eslabones_cuantificado.csv` (VBP/PIB/empleo 2013 y 2018), `cv_tipologia.csv`. Scripts `cv_build.py`.
- **Límites.** Solo el **cobre** tiene clases SCIAN dedicadas a su transformación; el resto comparte clase (metales preciosos 331412; no ferrosos 331419; manganeso con siderurgia 331112; HF en 325180) → el valor de esos eslabones **no se atribuye** al mineral y se ancla con comercio y capacidad instalada.
- **Por qué se incorpora.** Es el **integrador** (Cap. VIII): localiza el punto de ruptura y la **invisibilidad estadística** de los eslabones como síntoma del enclave.

### 5.3 Tipología A/B/C/D
- **Qué mide.** Clasifica los diez mercados por grado de transformación doméstica (A desarrollada · B truncada en refinado · C usuario con eslabón importado · D exportación en bruto).
- **Fuente.** `cv_tipologia.csv` (col. `criterio_actores`, `criterio_espejo`, `criterio_ghosh_di`, `justificacion`).
- **Por qué se incorpora.** Es la **síntesis descriptiva** que ordena los resultados en un mapa comparable.

---

## Grupo 6 — Dimensión territorial (Ghosh subnacional)

### 6.1 Georreferenciación de extracción y transformación
- **Qué mide.** Distribución estatal de la extracción (cuantitativa) y ubicación de los nodos de transformación.
- **Fuente.** `georref_extraccion_mineral_estado_cuantitativo.csv` (share por estado 2024, SGM), `georref_transformacion_nodos.csv`.
- **Por qué se incorpora.** Base de los **mapas** (figuras Cap. VIII) y del HHI geográfico (1.2).

### 6.2 Ghosh estatal e interestatal (+ por eslabón, fuga de exportación)
- **Qué mide.** Encadenamiento hacia adelante por **entidad** y su descomposición (intra-estatal, inter-estatal, exportación); **fuga por exportación**.
- **Matemática.** Ghosh-Rasmussen sobre matriz estatal (rank de 35) e interestatal (rank de 70); `fuga_export_share` = parte del arrastre que se va como exportación.
- **Fuente.** `ghosh_estatal_mineria.csv`, `ghosh_estatal_eslabones.csv`, `ghosh_interestatal_mineria.csv`, `ghosh_interestatal_eslabones.csv`. Scripts `ghosh_estatal*.py`, `ghosh_interestatal*.py`.
- **Por qué se incorpora.** Muestra que la transformación con más arrastre se concentra en el **eje siderúrgico (Coahuila, Nuevo León)**, no donde más se extrae — la desconexión aguas abajo también es espacial.

---

## Grupo 7 — Comparación internacional (OECD ICIO)

### 7.1 Ghosh por país y por eslabón (ICIO)
- **Qué mide.** Encadenamiento hacia adelante del sector minería (y de refinación C24 / semimanufactura C25) de 9 países comparables (corte 2018).
- **Matemática.** Mismo Ghosh-Rasmussen (media país = 1) sobre el bloque doméstico de cada país en la matriz inter-país OCDE.
- **Fuente.** `icio_comparacion_mineria.csv`, `icio_eslabones_metal.csv`. Scripts `icio_comparacion.py`, `icio_eslabones.py`.
- **Límites.** Nivel **sector-minería agregado**, no por mineral (ISIC).
- **Por qué se incorpora.** Reencuadra el supuesto del protocolo sobre "casos de éxito": Chile, Australia, Brasil y Perú **no** superan el patrón; el referente real es **China** y el **modelo nórdico**. México (1.51) y China (1.53) tienen Ghosh casi idéntico → prueba de que el índice no basta.

### 7.2 Descomposición de valor agregado (DVA / crudo_share) — complementario clave
- **Qué mide.** El enclave **en dinero**: fracción del valor agregado minero exportado que sale **en crudo** (para reprocesarse fuera) vs. transformado en casa.
- **Matemática.** Sobre la matriz global: `dva_share`, `vax_mineria`, `reproc_domestico_share`, **`crudo_share`**, `foreign_abs_share`. Un `crudo_share` alto = firma del enclave.
- **Fuente.** `icio_dva_mineria.csv`. Script `icio_dva.py`.
- **Por qué se incorpora.** **Separa** a México (Ghosh 1.51, crudo 0.38) de China (1.53, crudo 0.07) — asignación casi idéntica, captura opuesta. Chile y Perú ≈0.98 (los enclaves más profundos). Es la evidencia más nítida de por qué el Ghosh no se lee solo, y de que el agregado de México engaña (promedia preciosos fundidos con cobre exportado en concentrado).

---

## Grupo 8 — Criticidad por producto

### 8.1 Clasificación de criticidad producto por producto
- **Qué mide.** El **eslabón** de mayor criticidad de cada mineral (estratégico > crítico > medio > bajo) y si México lo produce/exporta/importa.
- **Fuente.** `criticidad_productos.csv` (col. `nivel_criticidad`, `mx_usa`, `mx_exporta`, `mx_importa`); base oficial USGS (2022/2025), UE (CRMA 2023), IEA. Nota en [[Clasificacion de productos por criticidad]].
- **Por qué se incorpora.** Muestra que **la criticidad se concentra en productos y grados, no en el mineral**, y que en grafito, sílice y manganeso el eslabón estratégico es justo el ausente: **la criticidad se fuga con el valor**. Alimenta II.3, VII y VIII.

---

## Cierre: por qué la lectura es conjunta

Ningún indicador prueba el enclave por sí solo. El diseño descriptivo **hace converger indicadores independientes**: estructura (HHI) · encadenamientos (Leontief/Ghosh/Rasmussen, por eslabón) · captura de valor (CCV, DVA/crudo_share) · comercio por etapa y destinos · comparación internacional · criticidad por producto. El **enclave estructural** aparece en la **combinación**, no en ningún índice aislado — y el hecho de que la concentración no covaríe con el encadenamiento confirma que se está describiendo, no imponiendo, el patrón.

← [[Arquitectura del documento (estructura expositiva)]] · [[Catalogo de Bases de Datos]] · [[CLAUDE]]
