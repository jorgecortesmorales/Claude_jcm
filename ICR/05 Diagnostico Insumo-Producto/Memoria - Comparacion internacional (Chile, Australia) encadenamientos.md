---
title: "Memoria — Comparación internacional (minería): ¿casos de éxito?"
type: resultados
tags: [icr, comparacion-internacional, chile, australia, finlandia, suecia, china, brasil, peru, encadenamientos, ghosh, enclave, icio]
created: 2026-09-06
updated: 2026-09-08
status: activo
---

# Memoria — Comparación internacional (minería): ¿casos de éxito?

> [!info] Propósito
> El protocolo cita a Chile y Australia como referencias de "casos de éxito" en generar cadenas de valor a partir de la minería. Esta memoria (1) computa el **encadenamiento hacia adelante del sector-minería** de México (agregado, *like-for-like*) frente a **siete comparables** —Chile y Australia (los del protocolo), Finlandia y Suecia (modelo nórdico) y, desde el Paso 6.6, **China, Brasil y Perú** (economías emergentes minero-relevantes, ver justificación abajo)— con una fuente comparable (**OECD ICIO**); (2) documenta la **extracción** y **transformación** de cada país; y (3) contrasta la evidencia para **poner a prueba** la etiqueta de éxito. Hallazgo central, en dos planos: (a) **Chile, Australia, Brasil y Perú NO son casos de éxito en encadenamiento hacia adelante** —su minería está *por debajo* (o apenas en) el promedio de su propia economía—; los que sí muestran integración aguas adelante son **China, Finlandia y Suecia** (fundición/refinación doméstica: China por su gigantesco complejo metalúrgico, los nórdicos por integración mina-fundición). (b) A nivel **agregado**, la minería de México registra un Ghosh hacia adelante *alto* (por la fundición/refinación de metales, C24), lo que **no refuta** el enclave sino que **ilustra el límite del coeficiente agregado**: enmascara la heterogeneidad por mineral (cobre 94.7% concentrado a China) que sí revelan el análisis por mineral, el comercio por etapa y el HHI.

> [!note] Justificación de los tres países añadidos (Paso 6.6)
> - **China** — el **procesador global** de minerales críticos: aunque no es el mayor extractor de la mayoría, concentra ~50-80% de la fundición/refinación mundial de cobre, zinc, plomo, tierras raras y grafito. Es el **contrafactual del extremo opuesto** de México (destino del 94.7% del concentrado de cobre mexicano) y sirve para mostrar dónde se captura el valor que México exporta. Comparabilidad estructural: economía grande, industrializada, con política industrial minero-metalúrgica explícita.
> - **Brasil** — la **economía latinoamericana más parecida a México** en tamaño (2ª y 1ª de la región), estructura industrial diversificada, federalismo y peso del sector primario-exportador; gran minero (hierro/Vale, oro, bauxita). Controla por "efecto región" y "efecto tamaño".
> - **Perú** — vecino andino, **estructura minero-exportadora muy similar a la mexicana** (polimetálico: cobre, plata, zinc, plomo, oro; capital mixto), sin la escala de Chile. Es el comparable regional más cercano en composición de la canasta minera y sirve para ver si el enclave es un rasgo mexicano o regional.

## 1. Coeficientes computados (OECD ICIO 2020, sector-minería agregado, C1)

Método (idéntico a `mip_calc.py`, sobre el **bloque intra-país** de cada economía): `B=Z/x(fila)`, `G=(I−B)⁻¹`; encadenamiento **hacia adelante** = suma de fila de G; **Rasmussen = índice / media de las 45 industrias del país** (media país = 1). Sector comparable a los 10 minerales = **B07_08 minería no energética** (menas metálicas + otra minería/canteras). Script `10 Datos/scripts/icio_comparacion.py`; salida `processed/icio_comparacion_mineria.csv`; procedencia en `Bases Originales/12 OECD ICIO/`.

**Tabla A — Encadenamiento hacia adelante del sector-minería no energética (B07_08; Ghosh–Rasmussen, media país = 1) en tres cortes** (los mismos del Ghosh de la MIP: 2008/2013/2018; +2020 como referencia reciente)

| País | 2008 | 2013 | 2018 | (2020) | Lectura |
|---|---:|---:|---:|---:|---|
| **China** | 1.56 | 1.56 | **1.53** | — | el más alto: complejo metalúrgico global (procesa el mundo) |
| **México** | 1.65 | 1.58 | **1.51** | 1.42 | alto los tres cortes (agregado; ver §4bis) |
| **Finlandia** | 1.41 | 1.41 | **1.31** | 1.23 | alto: integración nórdica |
| **Suecia** | 1.26 | 1.26 | **1.27** | 1.35 | alto: fundición doméstica (Boliden) |
| **Brasil** | 0.97 | 0.90 | **0.99** | — | ≈1: en el promedio de su economía |
| **Australia** | 0.96 | 0.82 | **0.83** | 0.91 | por debajo del promedio propio |
| **Chile** | 0.89 | 0.85 | **0.73** | 0.79 | **<1 y bajando** = enclave |
| **Perú** | 0.67 | 0.63 | **0.62** | — | **el más bajo**: enclave polimetálico |

Patrón **estable en los tres cortes**: China, México, Finlandia y Suecia por encima de 1; Brasil en ≈1; Australia, Chile y Perú por debajo del promedio de su propia economía (Chile además cae 0.89→0.73; Perú es el mínimo, ~0.62). Rangos y backward por año en `icio_comparacion_mineria.csv` (China/Brasil/Perú en los cortes 2008/2013/2018; la ventana 2020 conserva los cinco originales). Referencia (energéticos B05_06 y servicios B09) en la misma base. **Nota clave**: un Ghosh alto en China significa algo distinto que en México — en China refleja fundición/refinación *doméstica* masiva; en México, el promedio de metales que sí se funden con el cobre que se exporta en bruto (ver §5, DVA, donde China y México se separan nítidamente).

**Compradores domésticos de la minería no energética** (a quién le vende, top): México → **C24 metales básicos** (US$7,206 M), C23, construcción; Chile → **a sí misma** (concentrado intra-sector, US$7,168 M) y poco a C24 (US$982 M); Australia → C24 (US$33,396 M, alúmina/aluminio) pese a exportar hierro/litio en bruto; Finlandia y Suecia → **C24** (fundición/refinación) como destino principal.

> [!important] Cómo leer estos números (caveat central)
> El coeficiente **hacia adelante de Ghosh mide la asignación del producto a uso intermedio doméstico, NO la profundidad ni la captura de valor de la cadena**. Por eso:
> - **Chile** —el "referente" del protocolo— sale **por debajo del promedio de su propia economía** (0.786, rango 34/45): su minería, gigantesca (11.4% del VBP), asigna casi todo su producto a **sí misma / exportación**, no a downstream doméstico. Es la firma estadística del **enclave** que documenta la literatura (Aroca; Atienza et al.).
> - **México** sale **alto (1.423, rango 4/45)** porque el agregado B07_08 **sí** captura el paso minería→**C24 metales básicos** (fundición/refinación de metales que en México sí ocurre). Esto **no contradice** el enclave estructural: el agregado **promedia** el cobre exportado 94.7% como concentrado a China (que se registra como exportación, no como forward doméstico) con los metales que sí se funden. La **heterogeneidad por mineral** (cobre 1.34, sílice 1.92, plomo-zinc 0.71, barita 0.64 en `mip_encadenamientos_minerales.csv`) y el **comercio por etapa** revelan el enclave que el promedio esconde → **caveat de agregación**.
> - **Finlandia y Suecia** son los que muestran forward genuinamente alto con base en **fundición/refinación doméstica** (Boliden, Harjavalta): el verdadero "caso de éxito" en integración aguas adelante es el **modelo nórdico**, no Chile ni Australia.

## 2. Chile

**Extracción.** Primer productor mundial de cobre (~24% global); también molibdeno, litio (Salar de Atacama), plata, oro. Estructura mixta: la **estatal Codelco** (~30% de la producción nacional de cobre) + grandes privadas (BHP/Escondida, Anglo American, etc.).

**Transformación.** Chile **sí funde y refina** una parte del cobre (fundiciones de Codelco: Chuquicamata, Potrerillos, Ventanas —esta última en cierre—, más Altonorte de Glencore), a diferencia de México, que exporta el concentrado. **Pero**: en 2024 el **concentrado sin refinar fue 50.9%** del valor de las exportaciones mineras y el cobre procesado en fundiciones chilenas solo **33%**; se estima que **~94% del concentrado se exporta** para su procesamiento en el exterior (paralelo casi exacto al 94.7% del concentrado de cobre mexicano que va a China). La capacidad de fundición es **insuficiente y en discusión** (MOU Codelco–Glencore 2025 para ampliarla). La manufactura aguas abajo (semis, productos de cobre) es **delgada**.

**Encadenamientos (literatura).** Estudios con las MIP del Banco Central de Chile (1995-2011) encuentran que la minería del cobre **mantiene características de enclave**, con encadenamientos hacia adelante **y** hacia atrás **limitados** y en **tendencia decreciente** a nivel nacional y regional; el sector es central por **volumen de producción**, no por sus encadenamientos (Aroca; Atienza, Lufin y Soto).

**¿Éxito?** En **escala** y **captura fiscal/estatal** (Codelco, regalías), sí. En **cadena de valor aguas adelante**, **no**: exporta concentrado en proporciones comparables a México y su downstream es motivo de política, no un logro consolidado.

## 3. Australia

**Extracción.** Potencia en mineral de hierro (1º mundial), litio (espodumeno, 1º mundial), bauxita, oro, carbón; grandes privadas (BHP, Rio Tinto, Fortescue).

**Transformación.** Cuadro **mixto**: **sí** procesa bauxita→alúmina→algo de aluminio (cadena real en alúmina); **pero** el **mineral de hierro se exporta casi íntegro en bruto** (a China) y el **litio se exporta sobre todo como espodumeno concentrado** (a China), aunque construye plantas de hidróxido (Kwinana, Kemerton) con resultados mixtos. Su ventaja distintiva es el **sector de servicios, equipo y tecnología minera (METS)** —innovación y exportación de servicios—, no la manufactura del mineral.

**Encadenamientos (literatura).** Con las IO tables australianas y el método de extracción hipotética, la minería muestra **encadenamientos hacia atrás fuertes** (demanda de servicios/equipo: el METS) pero encadenamientos **hacia adelante débiles**, concentrados en materiales no metálicos (Weldegiorgis et al., 2024).

**¿Éxito?** En **escala**, **servicios mineros (METS)** y **marco regulatorio/fiscal**, sí. En **encadenamiento hacia adelante** del mineral, **no** (hierro y litio son en gran medida enclaves de exportación en bruto).

## 3bis. Finlandia (modelo nórdico) — país de éxito #1 confirmado con literatura

**Por qué se elige.** La literatura sitúa al **clúster minero-metalúrgico nórdico (Finlandia + Suecia)** como el referente de integración aguas adelante: fundición/refinación doméstica, servicios y tecnología minera. Finlandia lidera el índice de atractivo minero (Fraser 2025) y, junto con Suecia, concentra ~80% de la tecnología mundial de minería subterránea (Nordic Innovation; OECD Mining Regions). Es un "caso de éxito" **distinto** de Chile/Australia: el éxito **sí** está en el encadenamiento, no solo en escala o fisco.

**Extracción.** Níquel, cobalto, cromo (Kemi, única mina de cromo de la UE), oro, zinc, cobre; minería relativamente **pequeña** (0.4% del VBP), pero estratégica para minerales críticos de la transición.

**Transformación.** **Fundición/refinación doméstica real**: refinerías de níquel/cobalto (Harjavalta, Kokkola/Umicore, Terrafame — cadena níquel→sulfato para baterías), química del cobalto de clase mundial. La minería **alimenta** la metalurgia doméstica (C24) y la química (C20).

**Encadenamientos (ICIO 2020 + literatura).** Forward Rasmussen **1.234** (rango 9/45): la minería está **por encima** del promedio de su economía, alimentando metales básicos, química y papel. Consistente con la literatura del clúster nórdico integrado (Nordic Innovation; OECD; "Digging in the dark", Springer 2021).

**¿Éxito?** **Sí en encadenamiento hacia adelante**: extracción pequeña pero con downstream metalúrgico-químico doméstico. El contraste con Chile es nítido (minería 28× más grande en Chile por %VBP, pero forward más débil).

## 3ter. Suecia (modelo nórdico) — país de éxito #2 confirmado con literatura

**Por qué se elige.** Otra mitad del clúster nórdico; caso clásico de minería con **fundición integrada** (Boliden). Complementa a Finlandia y da robustez al "modelo nórdico" como referente de integración.

**Extracción.** Primer productor de mineral de hierro de la UE (LKAB, Kiruna/Malmberget), cobre, zinc, plomo, oro, plata; minería ~0.6% del VBP.

**Transformación.** **Boliden** opera minas **y** fundiciones (Rönnskär cobre/metales preciosos/electrónica reciclada; Harjavalta en Finlandia): modelo mina→fundición→metal refinado **integrado verticalmente y doméstico**. LKAB avanza hacia hierro de reducción directa (HYBRIT, acero verde) — profundización downstream en marcha.

**Encadenamientos (ICIO 2020 + literatura).** Forward Rasmussen **1.349** (rango 5/45), con **C24 metales básicos** como comprador doméstico principal (US$2,434 M): firma de la fundición integrada. Es, de los cinco países, el de **encadenamiento hacia adelante más alto junto con México** — pero con un mecanismo distinto (fundición doméstica genuina vs. agregado que promedia el concentrado exportado).

**¿Éxito?** **Sí en encadenamiento hacia adelante**: la integración mina-fundición (Boliden) es precisamente lo que a México le falta en el cobre. Es el contrafactual más útil para el Cap. VIII.

## 3quater. China (Paso 6.6) — el procesador global, extremo opuesto de México

**Por qué se elige.** China es el **destino del 94.7% del concentrado de cobre mexicano** y el **procesador dominante** del mundo (≈50-80% de la fundición/refinación global de cobre, zinc, plomo, aluminio, grafito y tierras raras). Es el **contrafactual del extremo opuesto**: donde México exporta valor en bruto, China lo captura. Comparabilidad estructural: economía grande, industrializada, con política industrial minero-metalúrgica explícita de largo plazo.

**Extracción y transformación.** Gran extractor de carbón, tierras raras, grafito, tungsteno, molibdeno; pero su rasgo definitorio es la **metalurgia**: importa concentrados de medio mundo (Chile, Perú, México, Australia) y los **funde/refina domésticamente** para alimentar su manufactura (electrónica, baterías, acero, semis). La minería *alimenta* un aparato industrial doméstico completo aguas abajo.

**Encadenamientos (ICIO, B07_08).** Forward Rasmussen **1.53 en 2018** (1.56 en 2008 y 2013) — el **más alto de los ocho países**. A diferencia de México, su Ghosh alto **sí** corresponde a transformación doméstica genuina, como confirma el DVA (§5): `crudo_share` ≈ **0.07** (funde casi todo lo que toca). Es la imagen especular de un enclave.

**¿Éxito?** **Sí, en captura de valor aguas adelante** — pero por una vía (escala + política industrial + control de la refinación global) difícilmente replicable por México. Su utilidad en la tesis es **mostrar a dónde va el valor** que México no retiene, no como modelo a imitar directamente.

## 3quinquies. Brasil (Paso 6.6) — el par latinoamericano por tamaño y estructura

**Por qué se elige.** Es la **economía latinoamericana más comparable a México** (tamaño, industrialización, federalismo, diversificación, peso primario-exportador). Controla por "efecto región" y "efecto tamaño": si el enclave fuera solo un rasgo de país grande y latinoamericano, Brasil debería parecerse a México.

**Extracción y transformación.** Gran minero de **hierro** (Vale, 2º mundial), oro, bauxita, niobio (casi monopolio mundial), manganeso. Procesa parte del hierro en acero (CSN, Gerdau, Usiminas) y la bauxita en alúmina/aluminio, pero **exporta hierro en gran medida en bruto/pellet** a China.

**Encadenamientos (ICIO, B07_08).** Forward Rasmussen **0.99 en 2018** (0.97/0.90/0.99): justo en el promedio de su economía — ni enclave marcado ni integración clara. Pero el DVA lo delata: `crudo_share` ≈ **0.82** (2018) — buena parte del VA minero sale en crudo pese al Ghosh ≈1. Ilustra por qué el Ghosh, solo, engaña.

**¿Éxito?** **Parcial**: más integrado que Chile/Perú por su siderurgia, pero lejos del modelo nórdico. Confirma que el patrón mexicano no es idiosincrásico sino **regional/estructural**.

## 3sexies. Perú (Paso 6.6) — el vecino andino, misma canasta polimetálica

**Por qué se elige.** Es el comparable regional **más cercano a México en composición de la canasta minera**: polimetálico (cobre, plata, zinc, plomo, oro), capital mixto, sin la escala chilena. Prueba si el enclave es un rasgo mexicano o **compartido en la minería polimetálica andina**.

**Extracción y transformación.** 2º productor mundial de cobre y plata, gran productor de zinc/plomo/oro. Transformación doméstica **mínima**: la fundición de La Oroya (Doe Run) lleva años en crisis/cierre; exporta esencialmente **concentrados**.

**Encadenamientos (ICIO, B07_08).** Forward Rasmussen **0.62 en 2018** — el **más bajo de los ocho**, y `crudo_share` ≈ **0.98** (2018), empatado con Chile como el **enclave más profundo en dinero**. Perú es el espejo más nítido de lo que sería México sin su fundición de metales preciosos.

**¿Éxito?** **No**: enclave polimetálico casi puro. Su valor para la tesis es mostrar que la **misma canasta mineral** que México, sin transformación doméstica, produce el enclave en su forma extrema — reforzando que la diferencia la hace la **integración aguas abajo**, no la dotación.

## 4. Contraste con México y lectura para la tesis

| | México | Chile | Australia | Finlandia | Suecia |
|---|---|---|---|---|---|
| Rol global | 1º plata; relevante Cu, Zn, fluorita | 1º cobre | 1º hierro y litio | Ni/Co/Cr críticos | 1º hierro UE |
| Propiedad | mayoritariamente **nacional privada** | mixta (**estatal** Codelco + privada) | privada (multinacionales) | privada + estatal (Terrafame) | privada (**Boliden**, LKAB estatal) |
| ¿Funde/refina? | metales sí (hasta refinado); resto no | cobre parcialmente (insuficiente) | alúmina sí; hierro/litio casi no | **sí** (Ni/Co: Harjavalta, Kokkola) | **sí, integrado** (Boliden Rönnskär) |
| Concentrado exportado | cobre **94.7%** (a China) | cobre **~94%** | hierro y litio en bruto (a China) | menor (procesa domésticamente) | menor (procesa domésticamente) |
| Fwd Rasmussen minería (ICIO 2020, B07_08) | **1.42** (rk 4) — agregado, ver §1 | **0.79** (rk 34) | **0.91** (rk 26) | **1.23** (rk 9) | **1.35** (rk 5) |
| Encadenamiento adelante | agregado alto **pero heterogéneo por mineral**; enclave en cobre | **débil** (enclave) | hacia atrás fuerte; adelante débil | **fuerte** (metalurgia-química) | **fuerte** (mina→fundición) |
| "Éxito" en | — | escala, fisco, **Codelco** | escala, **METS**, regulación | **integración downstream** (Ni/Co críticos) | **integración mina-fundición** (Boliden) |

**Tabla síntesis — los ocho países en dos ejes (corte 2018)**, ordenados por menor enclave en dinero:

| País | Ghosh fwd (media=1) | `crudo_share` DVA | Lectura conjunta |
|---|---:|---:|---|
| **China** | 1.53 | **0.07** | procesa casi todo: captura de valor real |
| **Finlandia** | 1.31 | 0.45 | integración nórdica (Ni/Co) |
| **Suecia** | 1.27 | 0.48 | fundición integrada (Boliden) |
| **México** | 1.51 | 0.38 | Ghosh y DVA agregados *engañan*: enclave por mineral (cobre) |
| **Australia** | 0.83 | 0.77 | METS fuerte, mineral en bruto |
| **Brasil** | 0.99 | 0.82 | siderurgia parcial, hierro en bruto |
| **Chile** | 0.73 | 0.98 | enclave del cobre |
| **Perú** | 0.62 | 0.98 | enclave polimetálico extremo |

> [!important] Reencuadre del "caso de éxito" (con coeficientes, ocho países)
> Los coeficientes ICIO **matizan el supuesto del protocolo en varias direcciones**:
> 1. **Chile, Australia, Brasil y Perú NO son casos de éxito en encadenamiento hacia adelante**: su minería está en o por debajo del promedio de su propia economía (fwd 0.73 / 0.83 / 0.99 / 0.62) y, en dinero, exportan la mayor parte del VA minero en crudo (`crudo_share` 0.98 / 0.77 / 0.82 / 0.98). Comparten con México el patrón de exportar concentrado/mineral en bruto. Lo que distingue a algunos no es una cadena manufacturera lograda, sino la **respuesta institucional**: propiedad estatal y fisco (Codelco) en Chile; servicios y tecnología minera (METS) en Australia; siderurgia en Brasil. **Perú es el espejo extremo** de México sin su fundición de preciosos.
> 2. **El "éxito" en integración aguas adelante es China y el modelo nórdico (Finlandia, Suecia)**: China por su **complejo metalúrgico global** (`crudo_share` 0.07 — funde el mundo), los nórdicos por **fundición/refinación doméstica** a pequeña escala (Boliden, Harjavalta) → fwd 1.31 y 1.27, `crudo` ~0.45-0.48. Ese es el contrafactual útil para el Cap. VIII: no "ser Chile", sino **integrar mina→fundición→metal** con capital y política domésticos. China marca **a dónde va el valor** que México no retiene.
> 3. **El coeficiente agregado de México (Ghosh 1.51; `crudo` 0.38) engaña si se lee solo**: es "bueno" porque promedia los metales que sí se funden (C24) con el cobre exportado 94.7% en bruto. El **enclave estructural** aparece al desagregar por mineral y ver el comercio por etapa, no en el agregado — es el **caveat de agregación** hecho evidencia, y una confirmación de la §4bis de [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]]: un Ghosh alto **no** equivale a cadena desarrollada. La comparación México↔China es la ilustración más nítida: **Ghosh casi idéntico (1.51 vs 1.53), realidad opuesta** (`crudo` 0.38 promedio-engañoso vs 0.07 procesador genuino).

## 5. Descomposición de valor agregado (DVA / reprocesamiento): el enclave en dinero (Paso 6.5)

El índice de Ghosh (§1) es un coeficiente de **asignación**; no mide cuánto valor **retiene** el país ni si el mineral se procesa dentro o fuera. Para eso se computa una **descomposición de valor agregado** sobre la matriz **global** OECD ICIO 2023 (método Leontief global; script `10 Datos/scripts/icio_dva.py` → `processed/icio_dva_mineria.csv`). Para la minería no energética (B07_08) de cada país se calcula, del valor agregado minero que se exporta, qué fracción sale **ya transformada en casa** (embebida en exportaciones de sectores no mineros, p. ej. metales básicos) frente a la que sale como **producto minero directo** (concentrado) para **reprocesarse en el extranjero** = `crudo_share`. Un `crudo_share` alto es la firma del enclave **en dinero**.

**Tabla B — `crudo_share` de la minería no energética (share del VA minero exportado que sale en crudo)**. Los cinco originales tienen serie anual completa 1995-2020; China, Brasil y Perú se computaron en los cortes 2008/2013/2018 (+2020).

| País | Prom. serie | 1995 → 2020 | Cortes MIP 2008/2013/2018 | Lectura |
|---|---:|---:|---:|---|
| **Perú** | **~0.96** | — | 0.92 / 0.97 / **0.98** | Empata a Chile como **enclave más profundo en dinero**: misma canasta polimetálica que México, sin transformación. |
| **Chile** | **0.97** | 1.00 → 0.96 | 0.95 / 0.98 / 0.97 | Enclave **extremo y constante 26 años**: casi todo el cobre sale como concentrado a reprocesar afuera. El Ghosh (0.79) solo lo insinuaba. |
| **Brasil** | **~0.86** | — | 0.87 / 0.90 / 0.82 | Alto pese a Ghosh ≈1: siderurgia parcial, pero exporta hierro sobre todo en bruto. |
| **Australia** | **0.67** | 0.52 → 0.74 | 0.66 / 0.76 / 0.77 | **Se deteriora**: cada vez más crudo (auge del hierro/litio a China). |
| **Suecia** | **0.41** | 0.42 → 0.46 | 0.34 / 0.48 / 0.48 | Integra cerca de la mitad (Boliden). |
| **México** | **0.38** | 0.24 → 0.48 | 0.34 / 0.34 / 0.38 | Agregado bajo (parece integrado); cíclico ~0.33-0.40 con **repunte reciente** (0.48 en 2020) y **absorción extranjera al alza 0.21 → 0.65**. |
| **Finlandia** | **0.29** | 0.31 → 0.51 | 0.20 / 0.27 / 0.45 | El más integrado en promedio de los originales (Ni/Co); sube hacia el final. |
| **China** | **~0.07** | — | 0.08 / 0.06 / **0.07** | **El procesador**: funde casi todo lo que toca. Extremo opuesto — captura el valor que los demás exportan en crudo. |

> [!important] Qué añade el DVA sobre el Ghosh
> 1. **Rankea a Chile y Perú como los enclaves más profundos** (≈0.97-0.98 de su VA minero exportado en crudo, estable una década): en términos de valor, Chile —el "referente" del protocolo— y Perú son los casos *menos* integrados de los ocho. En el extremo opuesto, **China (0.07)** funde casi todo: es el destino del valor que los demás exportan en crudo. México↔China con Ghosh casi idéntico (1.51 vs 1.53) pero `crudo` opuesto (0.38 vs 0.07) es la mejor ilustración de por qué el Ghosh, solo, engaña.
> 2. **Confirma el caveat de agregación en México.** El `crudo_share` agregado de México (0.38) es *bajo* —incluso menor que el de Suecia— porque el agregado promedia los metales preciosos que **sí** se funden en el país con el cobre que sale 94.7 % en concentrado. Igual que el Ghosh (1.42), el DVA agregado **engaña si se lee solo**: el enclave del cobre solo aparece al desagregar por mineral (Cap. V) y en el comercio por etapa.
> 3. **Aporta una señal temporal** (serie completa 1995-2020): el `crudo_share` de México es cíclico (oscila ~0.24-0.51 con el ciclo de precios) pero de punta a punta **casi se duplica (0.24 en 1995 → 0.48 en 2020)**, y —más nítido— su VA minero **absorbido en el extranjero se triplica (0.21 → 0.65)**: evidencia en valor de la *profundización* del enclave (más crudo, mucho más afuera) que también muestran los destinos hacia China (§Cap. VI). Australia se deteriora aún más marcadamente (0.52 → 0.74). Chile, en cambio, es **plano en ~0.97 los 26 años**: enclave estructural, no coyuntural.
> 4. La `dva_share` (VA doméstico en las exportaciones mineras) es alta en todos (~0.80-0.92) por ser minería intensiva en recurso: **no** es el indicador que discrimina —lo es el `crudo_share`—.

**Cobertura y validación.** Serie **anual completa 1995-2020** para los cinco países originales (incluye los 3 cortes de la MIP: 2008, 2013 y 2018), toda la ventana de la edición 2023 del ICIO; **China, Brasil y Perú** se computaron en los cortes 2008/2013/2018 (+2020), suficientes para ubicarlos en el patrón. *Nota de reproducibilidad*: los bloques ICIO previos a 2011 no eran descargables por `curl` (WAF de la OCDE) ni por SDMX-TiVA (error de servidor); se obtuvieron con descarga manual desde el navegador. **Validación**: identidad `reproc+crudo=1` sin violaciones (390 filas) y validez de cara (petróleo de México y carbón de Australia salen en crudo con 0.81-0.98, como corresponde). El pre-1995 (1992-94) y 2021-2025 quedan fuera de la ventana ICIO → se cubren con el proxy comercial `X_share_crudo` por etapa (1992-2024). **Caveat**: agregado a nivel minería, no por mineral.

## 6. Fuentes
- **OECD (2023).** *OECD Inter-Country Input-Output Database* (edición 2023, año 2020). http://oe.cd/icio — fuente de los coeficientes computados (§1) y de la descomposición DVA (§5); procedencia en `Bases Originales/12 OECD ICIO/`.
- Aroca, P. (2018). *Mining linkages in the Chilean copper supply network and regional economic development.* Resources Policy. https://www.sciencedirect.com/science/article/abs/pii/S0301420717303173
- Atienza, Lufin y Soto (2018). *Copper mining in Chile and its regional employment linkages.* Resources Policy. https://www.sciencedirect.com/science/article/abs/pii/S0301420717303185
- Weldegiorgis et al. (2024). *Inter-sectoral economic linkages in the Australian mining industry (partial hypothetical extraction).* Aust. J. Agric. Resource Econ. https://onlinelibrary.wiley.com/doi/10.1111/1467-8489.12544
- **Nordic Innovation (2026).** *Nordic Minerals and Mining Value Chain — Pathways to Growth.* https://pub.norden.org/nordicinnovation2026-01/nordic-minerals-and-mining-value-chain.html — clúster nórdico integrado (Finlandia+Suecia), ~80% de la tecnología de minería subterránea.
- **OECD (s.f.).** *Mining Regions and Cities: Västerbotten and Norrbotten, Sweden* — ecosistema minero e integración regional. https://www.oecd-ilibrary.org/sites/b403ec5a-en/index.html?itemId=/content/component/b403ec5a-en
- **"Digging in the dark"** (2021), *Mineral Economics* (Springer) — revisión de política minera sueca y finlandesa. https://link.springer.com/article/10.1007/s13563-021-00255-6
- Datos de concentrado de cobre chileno (2024, ~94% exportado; 50.9% concentrado / 33% procesado): Springer y análisis sectoriales 2025. https://link.springer.com/article/10.1007/s40171-025-00464-w · https://en.wikipedia.org/wiki/List_of_copper_smelters_in_Chile
- Método de encadenamientos (Rasmussen 1956; Hirschman 1958); comparación UE: https://www.sciencedirect.com/science/article/abs/pii/S0301420706000055

← [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] · [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]]
