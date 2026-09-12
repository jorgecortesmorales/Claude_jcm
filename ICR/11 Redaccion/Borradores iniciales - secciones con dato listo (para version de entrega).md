---
title: "Borradores iniciales — secciones con dato listo (para versión de entrega)"
type: redaccion-borrador
tags: [icr, redaccion, borrador, version-inicial]
created: 2026-09-11
updated: 2026-09-11
status: version-inicial
---

# Borradores iniciales — secciones con "dato listo · texto pendiente"

> [!info] Qué es esto y cómo usarlo
> Versión **inicial** de las ocho secciones cuyo **dato/cálculo ya estaba validado** pero cuyo **texto faltaba**. Están redactadas y ancladas en las cifras reales, para que tú hagas la **versión de entrega**: revisar, adaptar a tu estilo y complementar con tus ideas. Cada sección indica el archivo de respaldo. No sustituyen tu redacción; son el punto de partida.
>
> Todas las cifras provienen de `10 Datos/processed/`. Cortes de la MIP: 2013 y 2018 (base 2018). Índices de Rasmussen normalizados: **>1 = por encima del promedio de la economía**.

---

## Cap. V

### V.6 — Fuente de datos y operacionalización
*Respaldo: `mip_calc.py`; [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]]; validación vs. INEGI.*

Los coeficientes se calculan sobre las **matrices simétricas producto por producto** de la Matriz de Insumo-Producto del INEGI para **2013** (año base 2013) y **2018** (año base 2018), tomadas de la matriz de **origen doméstico** —la que excluye los insumos importados— para no atribuir a la economía nacional eslabonamientos que en realidad se satisfacen con importaciones. De la tabla se leen, por clase de actividad (SCIAN Clase), las filas de producción bruta (P.1), producto interno bruto a precios básicos (B.1bP), remuneraciones (D.1) y puestos de trabajo (PT). Los diez minerales se mapean a **nueve clases SCIAN** —plomo y zinc quedan combinados en una sola clase por su coextracción, tal como los registra el INEGI—. El cálculo se programó de forma reproducible y se **validó contra los tabulados publicados por el propio INEGI**, reproduciéndolos a precisión de máquina, de modo que las diferencias frente a la fuente son nulas y los resultados no dependen de supuestos añadidos. Este anclaje en una fuente única y autoconsistente es lo que permite comparar minerales entre sí y con el resto de la economía sin introducir ruido de conciliación entre bases.

### V.7 — Resultados: encadenamientos por mineral
*Respaldo: `processed/mip_encadenamientos_minerales.csv` (corte 2018).*

El rasgo común de los diez minerales es un **encadenamiento hacia atrás bajo**: con la única excepción del manganeso (1.05) y, marginalmente, el oro (1.03), todos quedan **por debajo de 1** (cobre 0.94; fluorita 0.97; grafito 0.87; plata 0.99; plomo-zinc 0.99; sílice 0.94; barita 0.96). Es la firma de una actividad **intensiva en el recurso natural**, que tracciona pocos proveedores industriales aguas arriba.

La heterogeneidad está aguas abajo, en el **encadenamiento hacia adelante** (sensibilidad de dispersión). Tres minerales lo tienen muy alto: **sílice 1.92** (el mayor del corpus, posición 18 de 834 clases), **grafito 1.71** (rango 43) y **manganeso 1.54** (rango 77). En un rango intermedio-alto se ubican **cobre 1.34** (185), **fluorita 1.31** (200), **oro 1.22** (271) y **plata 1.17** (288). En el extremo bajo, **plomo-zinc 0.71** (527) y **barita 0.64** (614), que apenas alimentan industria doméstica. La lectura debe ser cuidadosa (ver V.10): un índice alto describe la **amplitud de las industrias que compran el mineral**, no el valor que México retiene; de hecho, varios de los minerales con índice más alto exportan el grueso de su producción en bruto.

### V.8 — La demanda intermedia doméstica de cada mineral
*Respaldo: `processed/mip_demanda_intermedia_minerales.csv` (corte 2018).*

Al desagregar a **qué industrias vende** cada mineral dentro del país, el encadenamiento hacia adelante adquiere sentido y revela dónde se interrumpe la cadena:

- **Metales preciosos y cobre.** El oro (99.5 %) y la plata (99 %) destinan casi la totalidad de su demanda intermedia a **fundición y refinación de metales preciosos**; el cobre, el 93.5 % a **fundición y refinación de cobre**. La cadena doméstica llega hasta el **metal refinado** y se detiene: un valor alto de demanda intermedia sobre producción indica aquí procesamiento metalúrgico interno, no una cadena larga.
- **Plomo-zinc.** El 79.5 % va a **fundición y refinación de otros metales no ferrosos** y un 5.2 % a la **fabricación de acumuladores** (baterías): único vínculo manufacturero relevante, y desacoplado del mineral primario, que se exporta como concentrado.
- **Sílice.** Se reparte entre **envases de vidrio (43.4 %)** y **cemento (38.6 %)**: la cadena doméstica más amplia del corpus, aunque de bajo grado —el eslabón de mayor valor, el silicio metálico, se importa—.
- **Grafito.** Se dirige a la **siderurgia** (ferroaleaciones 43 %, complejos siderúrgicos 32 %, moldeo 14 %): eslabonamiento industrial genuino, pero cuyo insumo procesado (electrodos) se importa.
- **Fluorita.** El 82.3 % va a la **fabricación de cemento** (grado metalúrgico, como mineralizador del clínker). Esta cifra subestima la cadena fluoroquímica —el ácido fluorhídrico de Koura—, que ocurre **dentro de la empresa** (integración con su propia mina) y se destina a la exportación, por lo que no aparece en el flujo sectorial doméstico.
- **Manganeso.** Presenta el destino **más disperso** (farmacéutica 23 %, alimentos para animales 22 %, ladrillos 21 %, químicos inorgánicos 9 %), reflejo de que la mena doméstica es pequeña y de usos variados, mientras la ferroaleación de Autlán se alimenta en parte de mineral importado. En 2013 el 89 % iba a ferroaleaciones.
- **Barita.** El 58 % se destina a la **perforación de pozos petroleros** y un 14 % a la extracción de petróleo: es, en esencia, un insumo petrolero, sin cadena manufacturera.

### V.11 — El coeficiente de captura de valor (CCV), serie 1992–2025
*Respaldo: [[Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)]]; `processed/ccv_serie.csv`.*

El CCV mide qué fracción del precio internacional del producto **refinado** capta México cuando exporta el mineral en su etapa más cruda (E1): un valor cercano a 0 indica que casi todo el valor se genera afuera; cercano a 1, que se retiene. Como serie continua 1992–2025, ofrece la profundidad temporal que los dos cortes de la MIP no dan.

En el **cobre** el CCV se sitúa en **0.23–0.26** (2024–2025): al exportar concentrado, México cobra cerca de una cuarta parte del precio del cátodo refinado. En el **zinc**, **0.36–0.40**. En la **fluorita**, el CCV ronda **1.0** (1.07–1.13), pero no porque la cadena esté cerrada, sino porque el espato se exporta a un valor cercano a su propio precio de referencia: capta casi todo el valor **del crudo**, que vale poco frente al fluoropolímero. La **barita** (0.82–0.93) reproduce ese patrón sobre un producto de muy bajo valor unitario. En el extremo opuesto, **manganeso (0.11–0.13)** y **sílice (0.16–0.21)** capturan poco. Dos casos requieren advertencia: el **plomo** arroja un CCV mayor que 1 (1.7–2.7) que es un **artefacto** —su concentrado carga créditos de plata y oro que elevan el valor por tonelada por encima del plomo puro—; y el **oro y la plata** dan CCV ≈ 0 no por baja captura, sino porque **no exportan mena**, sino metal ya refinado (doré), de modo que el indicador, construido sobre la etapa cruda, no aplica a su caso.

### V.12 — Profundidad temporal: el corte de referencia 2008
*Respaldo: `processed/mip_encadenamientos_2008_referencia.csv`.*

Para asomarse a la evolución de los encadenamientos antes de 2013 se incorpora la MIP de **2008** (base 2008, SCIAN 2007) como **corte de referencia no encadenado**: sus niveles **no son estrictamente comparables** con los de 2013 y 2018 —cambian el año base, los precios y, en el manganeso, la amplitud de la clase—, por lo que se usa para leer **dirección y estructura**, no magnitudes exactas. Con esa cautela, el encadenamiento hacia adelante no describe una tendencia única: en el cobre desciende y se recupera (1.63 → 1.18 → 1.34), en la fluorita cae y repunta (1.11 → 0.87 → 1.31), mientras que en la sílice crece de forma sostenida (1.60 → 1.80 → 1.92) y en el manganeso salta y cede (1.00 → 1.79 → 1.54). La lección descriptiva es que la posición de un mineral en la cadena **no es estática** y responde a reconfiguraciones industriales y de clasificación, lo que refuerza el uso de los índices como fotografías comparables solo dentro de cada año base.

---

## Cap. VI

### VI.3 — Perfil de cada mercado (síntesis por mineral)
*Respaldo: [[Indice - Fichas de Cadena de Valor]] (detalle por mineral); `cv_tipologia.csv`, `hhi_consolidado.csv`, `comercio_posicion_resumen.csv`.*

Cada mercado se resume por su estructura (HHI), su encadenamiento hacia adelante (Ghosh normalizado, 2018), su posición comercial (participación exportada en bruto) y hasta qué eslabón llega su cadena local:

- **Cobre.** Concentración alta (Grupo México dominante). Refina y lamina en el país, pero exporta cada vez más **concentrado** (de 61 % a 81 % del valor exportado entre 2018 y 2024) e importa semimanufacturas: cadena presente hasta el metal, truncada antes de las semis.
- **Plomo.** Refinación nacional (Peñoles) y baterías (Clarios), pero el primario sale como concentrado (86 % en bruto) y el circuito de baterías opera sobre plomo reciclado: cadena desacoplada del mineral de mina.
- **Zinc.** Refinación nacional (IMMSA, Peñoles); aun así exporta concentrado (64 %→80 %) e importa semis y galvanizado.
- **Manganeso.** Caso integrado: Autlán convierte la mena en **ferroaleación** y exporta producto procesado, no mineral; la ruptura está más arriba, en la química fina del manganeso.
- **Oro.** Estructura fragmentada; se exporta ya **refinado** (doré, ~95 %); la joyería es importadora neta. Cadena cerrada en el lingote.
- **Plata.** Primer productor mundial; se exporta refinada; la manufactura de valor (platería, joyería) es limitada e importadora neta.
- **Barita.** Se extrae y muele; se usa (o exporta) **en bruto** como densificante de lodos de perforación; sin química del bario doméstica.
- **Fluorita.** La cadena no metálica más profunda: Koura opera la mayor planta de **ácido fluorhídrico** del mundo, integrada con su mina; pero se detiene antes de los fluoropolímeros, que se importan, y el HF opera como enclave de exportación.
- **Grafito.** Existe industria usuaria (acería por horno de arco eléctrico), pero el eslabón intermedio (electrodos de grafito) se importa; la extracción, además, decrece.
- **Sílice.** Cadena de vidrio y cemento amplia pero de baja gama; el silicio metálico, de mayor valor, se importa.

### VI.7 — Tipología comparativa de los diez mercados
*Respaldo: `processed/cv_tipologia.csv`.*

Del cruce entre estructura extractiva y grado de transformación doméstica emergen **cuatro tipos** de mercado, que ordenan a los diez minerales según dónde se detiene su cadena de valor:

- **Tipo A — cadena local desarrollada** (manganeso; fluorita, en el límite con B): la transformación de escala ocurre en el país, verticalmente integrada por el propio extractor (ferroaleación en Autlán; ácido fluorhídrico en Koura). Es el tipo más cercano a una industrialización del recurso, aunque se detenga en el intermedio.
- **Tipo B — truncada en el metal** (cobre, oro, plata, plomo, zinc): los grupos integran hasta la fundición y refinación y exportan el metal o el concentrado; la semimanufactura y la manufactura son escasas o importadas. Es el patrón **dominante** (cinco de diez) y la expresión más clara del enclave estructural.
- **Tipo C — usuario doméstico con eslabón importado** (grafito, sílice): existe una industria usuaria robusta (acero, vidrio), pero el eslabón intermedio de mayor valor —electrodos, silicio metálico— se importa pese a la demanda local.
- **Tipo D — exportación en bruto** (barita): sin eslabón manufacturero doméstico; el mineral se usa o se exporta esencialmente crudo.

La tipología muestra que el enclave no es uniforme: convive un núcleo de metales truncados en el refinado (B) con dos casos de integración química/metalúrgica con capital nacional (A) y dos de demanda doméstica insatisfecha con oferta local (C). Un hallazgo transversal, revelado por el análisis a nivel de empresa, es que buena parte de la cadena local ocurre **dentro de las firmas extractivas**, lo que el dato sectorial subestima —el eslabón de HF de la fluorita es el ejemplo—.

---

## Cap. VII

### VII.5 — La referencia internacional: ¿casos de éxito?
*Respaldo: `processed/icio_comparacion_mineria.csv` y `icio_dva_mineria.csv` (OECD ICIO, sector minería metálica B07_08, 2018).*

Situar a México frente a ocho países —Chile, Australia, Finlandia, Suecia, China, Brasil, Perú y el propio México— desmonta la idea de que sus vecinos mineros integran más. En el **encadenamiento hacia adelante** de la minería metálica (Rasmussen normalizado, 2018), el orden es: **China 1.53**, **México 1.51**, Finlandia 1.31, Suecia 1.27, Brasil 0.99, Australia 0.83, Chile 0.73 y **Perú 0.62**. Ni Chile ni Australia —los referentes habituales— superan su propio promedio nacional: su minería, medida así, **no arrastra** aguas adelante. Los únicos con integración clara son China, el procesador global, y el modelo nórdico (Finlandia y Suecia), que funden dentro.

Ahora bien, el índice de Ghosh **engaña por agregación**, y la descomposición de valor agregado (DVA) lo revela en dinero. La **participación exportada en crudo** —el valor minero que sale sin reprocesar— coloca a **China en 0.07** (funde casi todo), a **México en 0.38**, a Finlandia y Suecia en ~0.46–0.48, y a **Chile (0.98) y Perú (0.98)** como los enclaves más profundos. Dos lecturas se siguen. Primera: **México y China exhiben un Ghosh casi idéntico (1.51 y 1.53) pero una captura de valor opuesta** (0.38 frente a 0.07); el índice, por sí solo, no distingue integración real de amplitud de usuarios. Segunda: el 0.38 agregado de México **es más favorable de lo que corresponde**, porque promedia los metales preciosos que sí se funden (oro, plata) con el cobre, que sale 94.7 % como concentrado; el agregado **oculta** el enclave del cobre. Perú, con la misma canasta polimetálica que México pero con crudo de 0.98, confirma que el enclave no es idiosincrásico: lo produce la (falta de) integración aguas abajo, no la dotación.

---

← [[Estructura y Cronograma de la ICR]] · [[Indice de Redaccion Word]] · [[Bitacora]]
