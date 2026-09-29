---
title: "Capítulo III. Marco metodológico y analítico"
chapter: "III"
lang: es-ES
---

# Índice de cuadros

{{LISTA_CUADROS}}

# Índice de ilustraciones

{{LISTA_FIGURAS}}

# Capítulo III. Marco metodológico y analítico

## III.1 Diseño descriptivo y estrategia analítica

Esta investigación adopta un **diseño descriptivo**. Su propósito no es estimar el efecto causal de una variable sobre otra, sino caracterizar la posición de los diez minerales críticos en sus cadenas de valor y documentar dónde el país agrega valor y dónde deja de hacerlo. En consecuencia, los indicadores que se construyen —índices de concentración, coeficientes de encadenamiento, medidas de captura de valor, participaciones comerciales y descomposiciones de valor agregado— se emplean como **descriptores** de la estructura de cada mercado, no como parámetros de un modelo de comportamiento. El aporte central reside en la construcción de estas bases de datos e indicadores desagregados por mineral, que no estaban disponibles, y en su lectura conjunta.

El concepto que ordena esa lectura es el de **enclave estructural**: una minería que, aun sin ser un enclave clásico de propiedad extranjera, permanece desconectada de los eslabones de transformación aguas abajo con capital y capacidad domésticos. Ese concepto no se mide con un único indicador. Se manifiesta en la **convergencia** de varios descriptores independientes: una estructura extractiva concentrada, un encadenamiento hacia adelante que se corta en el metal refinado, una fracción alta de exportación en bruto, una captura de valor persistentemente baja y una dependencia de importación justo en los eslabones de mayor valor y criticidad. Cada indicador aporta una faceta; el enclave aparece en su intersección, no en ninguno por separado. El {{cua:sintesis}} resume qué mide cada uno, de qué base procede y en qué capítulo de resultados se presenta.

Un criterio transversal gobierna todo el tratamiento de datos: **declarar, no imputar**. Cuando una serie tiene huecos, se explicitan; cuando se completan con una fuente alternativa —por ejemplo, el comercio espejo—, se marca como tal; ninguna cifra se rellena con supuestos. Este criterio se detalla en III.11 y se materializa en una declaración de vacíos por indicador (Anexo D).

## III.2 Contabilidad insumo-producto: identidad, demanda y oferta

El núcleo cuantitativo del trabajo descansa en el análisis de insumo-producto, marco desarrollado por @leontief1941 para describir las relaciones intersectoriales de una economía. Para una economía de $n$ sectores, la matriz de insumo-producto (MIP) registra el valor de las transacciones intermedias entre ellos en un año dado. De forma matricial, la identidad contable de la producción se expresa como

$$\mathbf{x} = \mathbf{Z}\,\mathbf{i} + \mathbf{f} = \mathbf{Z}'\mathbf{i} + \mathbf{v} \qquad\qquad (1)$$

donde $\mathbf{x}$ es el vector del valor bruto de producción (VBP) de orden $n\times 1$; $\mathbf{Z}$ es la matriz de transacciones intersectoriales de orden $n\times n$, cuyo elemento $z_{ij}$ es el flujo del sector $i$ —que vende— al sector $j$ —que compra— como insumo intermedio; $\mathbf{f}$ es el vector de demanda final de orden $n\times 1$; $\mathbf{v}$ es el vector de valor agregado de orden $n\times 1$, e $\mathbf{i}$ es un vector de unos de orden $n\times 1$ que, según se premultiplique o posmultiplique, suma por columnas o por filas. La primera igualdad lee la producción por filas —usos intermedios más demanda final—; la segunda, por columnas —insumos intermedios más valor agregado—. Sobre esa doble lectura se levantan los dos modelos duales que se emplean.

**Encadenamientos hacia atrás: el modelo de demanda de Leontief.** El modelo de @leontief1941 supone que cada sector emplea sus insumos en proporciones técnicas fijas. Se define el coeficiente técnico de entrada como la razón entre el flujo intermedio y la producción del sector que compra,

$$a_{ij} = \frac{z_{ij}}{x_j} \qquad\qquad (2)$$

donde $a_{ij}$ es el insumo del sector $i$ requerido por unidad de producción del sector $j$ y $x_j$ es el VBP del sector $j$. Reuniendo los coeficientes $a_{ij}$ en la matriz $\mathbf{A}$ de orden $n\times n$, la identidad (1) por el lado de la demanda se reescribe como $\mathbf{x}=\mathbf{A}\mathbf{x}+\mathbf{f}$ y se resuelve el vector de producción como función de la demanda final:

$$\mathbf{x} = (\mathbf{I}-\mathbf{A})^{-1}\,\mathbf{f} = \mathbf{L}\,\mathbf{f} \qquad\qquad (3)$$

donde $\mathbf{I}$ es la matriz identidad de orden $n\times n$ y $\mathbf{L}=(\mathbf{I}-\mathbf{A})^{-1}$ es la matriz inversa de Leontief, cuyo elemento $l_{ij}$ mide la producción total —directa e indirecta— del sector $i$ necesaria para satisfacer una unidad de demanda final del sector $j$. El **encadenamiento hacia atrás** del sector $j$ es la suma de su columna en la inversa de Leontief,

$$BL_j = \sum_{i=1}^{n} l_{ij} \qquad\qquad (4)$$

y mide cuánto tracciona el sector $j$ a sus proveedores. En la minería suele ser bajo, porque la extracción es intensiva en el recurso y demanda pocos insumos industriales.

**Encadenamientos hacia adelante: el modelo de oferta de Ghosh.** El modelo de @ghosh1958 es el dual: en lugar de preguntar de dónde provienen los insumos, describe hacia dónde se distribuye la producción. Se define el coeficiente de distribución como la razón entre el flujo intermedio y la producción del sector que vende,

$$b_{ij} = \frac{z_{ij}}{x_i} \qquad\qquad (5)$$

donde $b_{ij}$ es la fracción de la producción del sector $i$ que se vende al sector $j$ y $x_i$ es el VBP del sector $i$. Reuniendo los coeficientes $b_{ij}$ en la matriz $\mathbf{B}$ de orden $n\times n$, la identidad (1) por el lado de la oferta, $\mathbf{x}'=\mathbf{v}'+\mathbf{x}'\mathbf{B}$, se resuelve como función del valor agregado:

$$\mathbf{x}' = \mathbf{v}'(\mathbf{I}-\mathbf{B})^{-1} = \mathbf{v}'\,\mathbf{G} \qquad\qquad (6)$$

donde $\mathbf{G}=(\mathbf{I}-\mathbf{B})^{-1}$ es la matriz inversa de Ghosh, con elemento $g_{ij}$, y el superíndice $'$ denota trasposición. El **encadenamiento hacia adelante** del sector $i$ es la suma de su fila en la inversa de Ghosh,

$$FL_i = \sum_{j=1}^{n} g_{ij} \qquad\qquad (7)$$

Para un mineral, un valor elevado de $FL_i$ significa que su producción alimenta a una industria transformadora doméstica amplia; uno bajo, que se destina a la demanda final —típicamente la exportación en bruto— sin apenas procesamiento interno. Es el descriptor central del trabajo, porque describe si existe cadena de valor local aguas abajo del recurso. Ahora bien, el modelo de oferta supone coeficientes de distribución fijos y su interpretación más defendible es la de un **modelo de precios** [@dietzenbacher1997; @oosterhaven1988]; aquí se emplea como descriptor de posición estructural, nunca como mecanismo causal, y por eso se lee siempre junto a los demás indicadores (III.5, III.6) y con las cinco cautelas que se desarrollan en el Capítulo VI.

**Normalización: los índices de Hirschman-Rasmussen.** Las sumas (4) y (7) dependen de las unidades y de la estructura de cada matriz, por lo que no son comparables sin normalizar. Sobre la idea de eslabonamientos de @hirschman1958, @rasmussen1956 divide cada suma sectorial entre el promedio de todas las sumas de la economía. El poder de dispersión (hacia atrás) y la sensibilidad de dispersión (hacia adelante) resultan, respectivamente,

$$U_j = \frac{\tfrac{1}{n}\sum_{i} l_{ij}}{\tfrac{1}{n^{2}}\sum_{i}\sum_{j} l_{ij}}, \qquad
  U_i = \frac{\tfrac{1}{n}\sum_{j} g_{ij}}{\tfrac{1}{n^{2}}\sum_{i}\sum_{j} g_{ij}} \qquad\qquad (8)$$

donde $U_j$ es el índice normalizado de encadenamiento hacia atrás del sector $j$ y $U_i$, el de encadenamiento hacia adelante del sector $i$, y $n$ es el número de sectores. Por construcción, la media de cada índice sobre todos los sectores es igual a la unidad: un valor mayor que 1 indica un encadenamiento por encima del promedio de la economía, y uno menor que 1, por debajo. Esta normalización hace comparables las posiciones relativas entre minerales y entre cortes temporales.

**Una medida complementaria: la extracción hipotética.** Los índices de Rasmussen miden la *intensidad* del encadenamiento —qué tan articulado está un sector por unidad de producción—, pero no su *peso* en la economía: un sector puede estar intensamente encadenado y a la vez ser marginal por su tamaño. Para captar esa segunda dimensión se añade el método de extracción hipotética [@millerlahr2001; @dietzenbacherlinden1997], en sus variantes hacia atrás (extracción de las compras, caso 3 de la taxonomía) y hacia adelante (extracción de las ventas, caso 4). El método consiste en "extraer" hipotéticamente el sector $k$ —anular su columna en la matriz $\mathbf{A}$ (o su fila en $\mathbf{B}$)— y resolver de nuevo el modelo con la matriz alterada $\mathbf{A}^{(-k)}$ (o $\mathbf{B}^{(-k)}$): la reducción del VBP total mide cuánto depende la economía de ese sector. El encadenamiento hacia atrás del sector $k$ es esa reducción, expresada como porcentaje del VBP nacional,

$$\text{EH}^{-}_{k} = 100\cdot\frac{\mathbf{i}'\big(\mathbf{x}-\hat{\mathbf{x}}^{(-k)}\big)}{\mathbf{i}'\mathbf{x}},\qquad
  \hat{\mathbf{x}}^{(-k)} = \big(\mathbf{I}-\mathbf{A}^{(-k)}\big)^{-1}\mathbf{f} \qquad\qquad (9)$$

donde $\text{EH}^{-}_{k}$ es el encadenamiento hacia atrás por extracción del sector $k$ y $\hat{\mathbf{x}}^{(-k)}$ es el vector de producción hipotética tras anular sus compras. De forma simétrica, el encadenamiento hacia adelante extrae las ventas del sector $k$ y resuelve el modelo de oferta de Ghosh,

$$\text{EH}^{+}_{k} = 100\cdot\frac{\mathbf{i}'\big(\mathbf{x}-\hat{\mathbf{x}}_{G}^{(-k)}\big)}{\mathbf{i}'\mathbf{x}},\qquad
  \big(\hat{\mathbf{x}}_{G}^{(-k)}\big)' = \mathbf{v}'\big(\mathbf{I}-\mathbf{B}^{(-k)}\big)^{-1} \qquad\qquad (10)$$

donde $\hat{\mathbf{x}}_{G}^{(-k)}$ es la producción hipotética tras anular las ventas del sector $k$. Es el método que @morales2023 aplica al caso interregional mexicano por sector-región, y que aquí se incorpora para comparar directamente con ese antecedente y para contrastar la lectura de intensidad —los índices de Rasmussen (8)— con la de peso económico —la extracción (9)-(10)—: los resultados por mineral se presentan en el Capítulo VI y su versión estatal en el Capítulo VIII.

**Fuente y operacionalización.** Se emplean las matrices simétricas producto por producto de la MIP del INEGI para 2013 (año base 2013) y 2018 (año base 2018), en su máximo nivel de desagregación —la clase de actividad SCIAN a seis dígitos (822 clases en 2013, 834 en 2018)—, sobre la matriz de origen doméstico, de modo que los encadenamientos reflejan la articulación con la producción nacional. A ese nivel, ocho de los diez minerales tienen clase propia; plomo y zinc comparten una sola clase, coherente con su coextracción geológica, por lo que sus encadenamientos se reportan de forma conjunta ({{cua:scian}}).

Cuadro {#cua:scian}: Correspondencia entre los minerales del corpus y las clases SCIAN de la MIP. Fuente: elaboración propia con la MIP del INEGI (bases 2013 y 2018) y el Sistema de Clasificación Industrial de América del Norte.

| Mineral | Clase SCIAN | Denominación |
|---|---|---|
| Oro | 212221 | Minería de oro |
| Plata | 212222 | Minería de plata |
| Cobre | 212231 | Minería de cobre |
| Plomo-zinc | 212232 | Minería de plomo y zinc (clase combinada) |
| Manganeso | 212291 | Minería de manganeso |
| Sílice | 212324 | Minería de arena sílica |
| Barita | 212393 | Minería de barita |
| Fluorita | 212395 | Minería de fluorita |
| Grafito | 212396 | Minería de grafito |

El cálculo se programó de forma reproducible y se validó contra los tabulados del propio INEGI: la matriz de coeficientes técnicos $\mathbf{A}$ de la ecuación (2) reproduce el archivo publicado y la inversa de Leontief $\mathbf{L}$ de la ecuación (3) reproduce el archivo de coeficientes directos e indirectos, con diferencias del orden de $10^{-15}$ (precisión de máquina). La inversa de Ghosh se construye sobre la misma matriz de flujos ya validada [@millerblair2009]. A los dos cortes comparables se añade la MIP de 2008 como **referencia histórica no encadenada**: no forma serie —los movimientos 2008→2013 mezclan cambio real con cambio de año base y de clasificación—, por lo que se lee por el patrón y el orden, no por el nivel exacto.

## III.3 El encadenamiento por eslabón

El encadenamiento hacia adelante del eslabón extractivo no dice hasta dónde se sostiene el arrastre al descender por la cadena. Para verlo, el índice de Ghosh-Rasmussen se calcula por separado para la extracción (L1), la refinación (L2) y la semimanufactura (L3) de cada mineral, identificando las clases SCIAN de transformación correspondientes (fundición, refinación y laminación, clases 331). Si el arrastre hacia adelante fuera prueba de una cadena desarrollada, debería sostenerse o crecer al avanzar hacia L2 y L3; documentar si se sostiene o se corta es el objeto de este cálculo, cuyos resultados se presentan en el Capítulo VI y, en su versión internacional, en el Capítulo VII.

## III.4 Concentración de mercado: el índice de Herfindahl-Hirschman

La estructura de mercado de cada mineral se describe con el índice de Herfindahl-Hirschman (HHI), definido como la suma de los cuadrados de las participaciones de mercado de los productores:

$$\text{HHI} = \sum_{k=1}^{m} s_k^{2} \qquad\qquad (11)$$

donde $s_k$ es la participación del productor $k$ en la producción del mineral, con $s_k\in[0,1]$, y $m$ es el número de productores; el índice se expresa en la escala habitual de 0 a 10 000 multiplicando por ese factor. Se calcula sobre la producción por mineral a partir de los numeradores de empresa o de unidad minera documentados en fuentes primarias (CAMIMEX y USGS). La serie 2004-2020 se reconstruye por **régimen de mercado** —a partir del líder y los grupos conocidos, con el residual tratado de forma atomística—, lo que la convierte en una **cota inferior** no estrictamente comparable en nivel con el tramo 2021-2024, calculado por mina; por ello la serie se lee por su trayectoria, no por su nivel puntual.

Un segundo índice, el **HHI geográfico**, aplica la misma fórmula a las participaciones de las entidades federativas en la extracción de cada mineral, y describe la concentración territorial de la producción. Ambos son descriptores complementarios: el primero caracteriza la estructura empresarial (Capítulo V); el segundo, la dimensión espacial del enclave (Capítulo VIII).

## III.5 El coeficiente de captura de valor

El índice de Ghosh está atado a los dos cortes de la MIP. Para dar profundidad temporal al encadenamiento hacia adelante se construye un segundo descriptor, el **coeficiente de captura de valor** (CCV), como serie anual mineral-año 1992-2025. Para cada mineral $m$ y año $t$,

$$\text{CCV}_{m,t} = \frac{v^{E1}_{m,t}}{p^{\text{USGS}}_{m,t}} \qquad\qquad (12)$$

donde $\text{CCV}_{m,t}$ es el coeficiente de captura de valor del mineral $m$ en el año $t$; $v^{E1}_{m,t}$ es el valor unitario de exportación del mineral en su forma bruta (mena o concentrado, etapa comercial 1), y $p^{\text{USGS}}_{m,t}$ es el precio del producto de referencia refinado del USGS. Un CCV cercano a 1 indica que la forma exportada en bruto ya vale casi como el producto refinado; uno cercano a 0, que la exportación bruta capta poco de ese valor —mayor distancia al eslabón procesado—. Un CCV bajo y persistente es el descriptor de serie del enclave estructural. El numerador procede de UN Comtrade (fracciones de exportación de México, con valor y peso); el denominador, de los precios del USGS empalmados. Los huecos se completaron con datos espejo —lo que los socios reportan importar desde México—, marcados como tales; el único hueco no completable (plomo, 1994) se declara y no se imputa. El poder descriptivo del CCV depende del grupo mineral —es nítido en los metales base y un artefacto de ley en oro y plata—, matiz que se discute con los resultados en el Capítulo VI.

## III.6 Comercio por etapa de procesamiento

Para observar en qué grado de transformación comercia México cada mineral se construye una serie de comercio exterior clasificada por **etapa de procesamiento** (E1 a E4), a partir de una concordancia que asigna cada fracción del Sistema Armonizado (HS) a la etapa correspondiente de cada mineral. Con esa concordancia se derivan las exportaciones e importaciones por etapa (1992-2024) y la **posición comercial**, medida como la fracción de la exportación que sale en bruto, $X^{\text{crudo}}/X^{\text{total}}$, y su simétrica para la importación de productos procesados. Un país que exporta en E1 e importa en E3-E4 exhibe el patrón del enclave. La serie se complementa con la **geografía del comercio** —a qué socio se dirige cada etapa y cómo se desplaza en el tiempo—, con la cautela de que Comtrade reporta el socio declarado (sin depurar reexportación ni *entrepôt*), lo que no altera la dirección del desplazamiento.

## III.7 Empresas de transformación y fichas de cadena de valor

El dato sectorial de la MIP no observa la transformación que ocurre **dentro** de las firmas extractivas verticalmente integradas. Para corregir esa subestimación, se levantó un mapa de empresas de transformación por mineral —quién procesa, en qué eslabón, dónde y bajo qué propiedad— a partir de reportes corporativos y perfiles de mercado. Ese mapa se organiza en diez **fichas de cadena de valor**, una por mineral, que descomponen cada mercado en cinco eslabones y localizan el **punto de ruptura**: el eslabón a partir del cual el país deja de agregar valor.

La notación de eslabones, común a los capítulos de resultados, se ilustra en la Ilustración {{fig:cadena}}. Los eslabones L1 a L4 coinciden con las cuatro fases de transformación y con las etapas comerciales E1-E4; se añade L0 para ubicar la dotación previa a toda actividad.

![Ilustración {#fig:cadena}: Los cinco eslabones de la cadena de valor de un mineral (notación L0-L4) y su equivalencia con las etapas comerciales E1-E4. Elaboración propia.](figuras/cadena_L0_L4.png){width=100%}

La cuantificación de cada eslabón (valor de producción, PIB y empleo desde la MIP; exportaciones e importaciones por etapa) encuentra un límite estructural que es, en sí mismo, un hallazgo: solo el cobre cuenta con clases SCIAN dedicadas a su transformación; el oro y la plata comparten una única clase de metales preciosos, el plomo y el zinc otra, el manganeso comparte la suya con la siderurgia y el ácido fluorhídrico de la fluorita se diluye en «químicos básicos inorgánicos». Donde no hay cadena diferenciada, tampoco hay categoría estadística que la mida; por eso el valor de esos eslabones no se atribuye al mineral y se ancla con el comercio y la capacidad instalada.

## III.8 Georreferenciación y encadenamiento subnacional

La cadena de valor tiene una dimensión territorial. Se georreferencia la extracción por entidad (participación estatal en la producción de cada mineral) y se localizan los nodos de transformación. Sobre esa base se calcula el índice de Ghosh-Rasmussen a escala **estatal** e **interestatal**, que describe hasta qué eslabón sostiene el arrastre cada entidad y qué fracción se fuga como exportación. El resultado ubica la transformación con mayor arrastre en el eje siderúrgico del noreste, no donde más se extrae, de modo que la desconexión aguas abajo también es espacial.

## III.9 Comparación internacional: encadenamientos y descomposición de valor agregado

Para situar el caso mexicano se emplean las tablas de insumo-producto inter-país de la OCDE (edición 2023, corte 2018, el mismo año del Ghosh nacional). Sobre el bloque doméstico de nueve países se calcula el encadenamiento hacia adelante del sector-minería no energética con el método de III.2 —el índice de Ghosh-Rasmussen de las ecuaciones (5) a (8), con la media de cada economía igual a 1—, y su versión por eslabón (extracción, refinación C24, semimanufactura C25). La comparación es a nivel de sector-minería agregado, no por mineral.

Como el índice de Ghosh es un coeficiente de asignación y no mide cuánto valor retiene el país, se añade una **descomposición de valor agregado**. Sobre la matriz global se separa, del valor agregado minero que cada país exporta, la parte que sale ya transformada en casa —embebida en las exportaciones de otros sectores— de la que sale como producto minero en crudo para reprocesarse en el extranjero. Esa segunda fracción, el *crudo_share*, es la firma del enclave en dinero: un valor alto revela que el valor de la minería se realiza fuera del país. Esta descomposición es la que separa nítidamente a economías con un índice de Ghosh casi idéntico pero capturas de valor opuestas, y evidencia por qué el índice agregado engaña cuando promedia minerales que sí se funden en el país con otros que se exportan en concentrado.

## III.10 Peso del bloque y precios de referencia

Dos construcciones dan soporte a los indicadores anteriores. La primera es el **peso del bloque** de diez minerales en la economía —su participación en el PIB, las exportaciones y el empleo, y la descomposición del valor de producción entre precio y volumen—, que sustenta la justificación del objeto en el Capítulo I. El valor de producción de cada mineral se obtiene como el producto de su volumen físico por su precio,

$$V_{m,t} = Q_{m,t}\,p_{m,t} \qquad\qquad (13)$$

donde $V_{m,t}$ es el valor de producción del mineral $m$ en el año $t$, $Q_{m,t}$ su volumen físico y $p_{m,t}$ su precio unitario; la variación del valor entre dos años se descompone en un índice de volumen y uno de precio. La segunda es la serie de **precios anuales del USGS empalmados** (1992-2025, en términos nominales y constantes de 1998), que sirve de denominador al CCV y de valuador de la producción. Ambas se apoyan en fuentes primarias (MIP del INEGI para PIB y empleo; UN Comtrade y USGS para exportaciones, producción y precios) y se documentan en el Anexo B.

## III.11 Criterio de tratamiento de datos: declarar, no imputar

Todo el trabajo se rige por un criterio explícito: los vacíos de las series se declaran y, cuando se intenta llenarlos, se hace con una fuente identificada y marcada (comercio espejo para los huecos del CCV; reconstrucción por régimen para el HHI histórico), nunca con supuestos ni interpolaciones silenciosas. Este criterio, además de honestidad metodológica, protege la lectura descriptiva: el retrato del enclave no descansa en ningún dato imputado, sino en la convergencia de indicadores independientes calculados sobre datos observados. El {{cua:sintesis}} sintetiza el conjunto y su articulación; la declaración de vacíos por indicador se recoge en el Anexo D.

Cuadro {#cua:sintesis}: Síntesis de los indicadores construidos: qué describe cada uno, base de datos de origen y capítulo de resultados donde se presenta. Fuente: elaboración propia; detalle en la auditoría de indicadores y en el Catálogo de Bases de Datos.

| Indicador | Qué describe | Base de datos | Resultados |
|---|---|---|---|
| HHI (mercado y geográfico) | Concentración extractiva y territorial | `hhi_consolidado`, `georref_regionalizacion` | Cap. V, VIII |
| Leontief / Ghosh / Rasmussen | Encadenamientos hacia atrás y adelante | `mip_encadenamientos_minerales` | Cap. VI |
| Encadenamiento por eslabón | Dónde se corta el arrastre (L1-L3) | `mip_encadenamientos_eslabones` | Cap. VI, VII |
| Demanda intermedia doméstica | Qué sectores compran cada mineral | `mip_demanda_intermedia_minerales` | Cap. VI |
| CCV (serie 1992-2025) | Captura de valor en el tiempo | `ccv_serie` | Cap. VI |
| Comercio por etapa y posición | Grado de transformación comerciado | `comercio_por_etapa_1992_2024` | Cap. VII |
| Ghosh internacional / DVA | Inserción y captura frente a 9 países | `icio_comparacion_mineria`, `icio_dva_mineria` | Cap. VII |
| Fichas L0-L4 y tipología | Punto de ruptura; tipo de mercado | `cv_tipologia`, `cv_eslabones_cuantificado` | Cap. VIII |
| Criticidad por producto | Dónde se concentra la criticidad | `criticidad_productos` | Cap. II, VII |
| Peso del bloque | Relevancia económica del objeto | `peso_bloque_mineria` | Cap. I |

## Fuentes y referencias
