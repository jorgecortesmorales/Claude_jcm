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

El concepto que ordena esa lectura es el de **enclave estructural**: una minería que, aun sin ser un enclave clásico de propiedad extranjera, permanece desconectada de los eslabones de transformación aguas abajo con capital y capacidad domésticos. Ese concepto no se mide con un único indicador. Se manifiesta en la **convergencia** de varios descriptores independientes: una estructura extractiva concentrada, un encadenamiento hacia adelante que se corta en el metal refinado, una fracción alta de exportación en bruto, una captura de valor persistentemente baja y una dependencia de importación justo en los eslabones de mayor valor y criticidad. Cada indicador aporta una faceta; el enclave aparece en su intersección, no en ninguno por separado. El Cuadro {{cua:sintesis}} resume qué mide cada uno, de qué base procede y en qué capítulo de resultados se presenta.

Un criterio transversal gobierna todo el tratamiento de datos: **declarar, no imputar**. Cuando una serie tiene huecos, se explicitan; cuando se completan con una fuente alternativa —por ejemplo, el comercio espejo—, se marca como tal; ninguna cifra se rellena con supuestos. Este criterio se detalla en III.11 y se materializa en una declaración de vacíos por indicador (Anexo D).

## III.2 Contabilidad insumo-producto: identidad, demanda y oferta

El núcleo cuantitativo del trabajo descansa en la matriz de insumo-producto (MIP). La MIP registra, para una economía de $n$ sectores, el valor de las transacciones intermedias entre ellos en un año. Sea $z_{ij}$ el flujo del sector $i$ (que vende) al sector $j$ (que compra) como insumo intermedio, $x_i$ el valor bruto de la producción del sector $i$ y $f_i$ su demanda final. La identidad contable por filas establece que toda la producción se destina a usos intermedios o finales:

$$x_i = \sum_{j=1}^{n} z_{ij} + f_i .$$

Leída por columnas, la producción de cada sector se descompone en el valor de sus insumos intermedios y su valor agregado. Sobre esta doble lectura se levantan los dos modelos duales que se emplean.

**Encadenamientos hacia atrás: el modelo de demanda de Leontief.** El modelo de @leontief1941 supone que cada sector emplea insumos en proporciones técnicas fijas. Se define el coeficiente técnico $a_{ij} = z_{ij}/x_j$; reuniendo los coeficientes en la matriz $\mathbf{A}$, la identidad se reescribe como $\mathbf{x} = \mathbf{A}\mathbf{x} + \mathbf{f}$, cuya solución es

$$\mathbf{x} = (\mathbf{I}-\mathbf{A})^{-1}\,\mathbf{f} = \mathbf{L}\,\mathbf{f}.$$

La inversa de Leontief $\mathbf{L}=(\mathbf{I}-\mathbf{A})^{-1}$ tiene elementos $l_{ij}$ que miden la producción total —directa e indirecta— del sector $i$ necesaria para satisfacer una unidad de demanda final del sector $j$. El **encadenamiento hacia atrás** del sector $j$ es la suma de su columna, $\sum_i l_{ij}$: mide cuánto tracciona a sus proveedores. En la minería suele ser bajo, porque la extracción es intensiva en el recurso y demanda pocos insumos industriales.

**Encadenamientos hacia adelante: el modelo de oferta de Ghosh.** El modelo de @ghosh1958 es el dual: en lugar de preguntar de dónde provienen los insumos, describe hacia dónde se distribuye la producción. Se define el coeficiente de distribución $b_{ij} = z_{ij}/x_i$; con la matriz $\mathbf{B}$, la lectura por columnas conduce a $\mathbf{x}' = \mathbf{v}' + \mathbf{x}'\mathbf{B}$, con solución

$$\mathbf{x}' = \mathbf{v}'(\mathbf{I}-\mathbf{B})^{-1} = \mathbf{v}'\,\mathbf{G}.$$

La inversa de Ghosh $\mathbf{G}=(\mathbf{I}-\mathbf{B})^{-1}$ tiene elementos $g_{ij}$; el **encadenamiento hacia adelante** del sector $i$ es la suma de su fila, $\sum_j g_{ij}$. Para un mineral, un valor elevado significa que su producción alimenta a una industria transformadora doméstica amplia; uno bajo, que se destina a la demanda final —típicamente la exportación en bruto— sin apenas procesamiento interno. Es el descriptor central del trabajo, porque describe si existe cadena de valor local aguas abajo del recurso. Ahora bien, el modelo de oferta supone coeficientes de distribución fijos y su interpretación más defendible es la de un **modelo de precios** [@dietzenbacher1997; @oosterhaven1988]; aquí se emplea como descriptor de posición estructural, nunca como mecanismo causal, y por eso se lee siempre junto a los demás indicadores (III.5, III.6) y con las cinco cautelas que se desarrollan en el Capítulo VI.

**Normalización: los índices de Hirschman-Rasmussen.** Las sumas anteriores dependen de las unidades y de la estructura de cada matriz, por lo que no son comparables sin normalizar. Sobre la idea de eslabonamientos de @hirschman1958, @rasmussen1956 divide cada suma sectorial entre el promedio de todas las sumas de la economía. El poder de dispersión (hacia atrás normalizado) y la sensibilidad de dispersión (hacia adelante normalizado) resultan, respectivamente,

$$U_j = \frac{\tfrac{1}{n}\sum_i l_{ij}}{\tfrac{1}{n^2}\sum_i\sum_j l_{ij}}, \qquad
  U_i = \frac{\tfrac{1}{n}\sum_j g_{ij}}{\tfrac{1}{n^2}\sum_i\sum_j g_{ij}} .$$

Por construcción, la media de cada índice sobre todos los sectores es igual a la unidad: un valor mayor que 1 indica un encadenamiento por encima del promedio de la economía, y uno menor que 1, por debajo. Esta normalización hace comparables las posiciones relativas entre minerales y entre cortes temporales.

**Fuente y operacionalización.** Se emplean las matrices simétricas producto por producto de la MIP del INEGI para 2013 (año base 2013) y 2018 (año base 2018), en su máximo nivel de desagregación —la clase de actividad SCIAN a seis dígitos (822 clases en 2013, 834 en 2018)—, sobre la matriz de origen doméstico, de modo que los encadenamientos reflejan la articulación con la producción nacional. A ese nivel, ocho de los diez minerales tienen clase propia; plomo y zinc comparten una sola clase, coherente con su coextracción geológica, por lo que sus encadenamientos se reportan de forma conjunta (Cuadro {{cua:scian}}).

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

El cálculo se programó de forma reproducible y se validó contra los tabulados del propio INEGI: la matriz de coeficientes técnicos $\mathbf{A}$ reproduce el archivo publicado y la inversa $\mathbf{L}$ reproduce el archivo de coeficientes directos e indirectos, con diferencias del orden de $10^{-15}$ (precisión de máquina). La inversa de Ghosh se construye sobre la misma matriz de flujos ya validada [@millerblair2009]. A los dos cortes comparables se añade la MIP de 2008 como **referencia histórica no encadenada**: no forma serie —los movimientos 2008→2013 mezclan cambio real con cambio de año base y de clasificación—, por lo que se lee por el patrón y el orden, no por el nivel exacto.

## III.3 El encadenamiento por eslabón

El encadenamiento hacia adelante del eslabón extractivo no dice hasta dónde se sostiene el arrastre al descender por la cadena. Para verlo, el índice de Ghosh-Rasmussen se calcula por separado para la extracción (L1), la refinación (L2) y la semimanufactura (L3) de cada mineral, identificando las clases SCIAN de transformación correspondientes (fundición, refinación y laminación, clases 331). Si el arrastre hacia adelante fuera prueba de una cadena desarrollada, debería sostenerse o crecer al avanzar hacia L2 y L3; documentar si se sostiene o se corta es el objeto de este cálculo, cuyos resultados se presentan en el Capítulo VI y, en su versión internacional, en el Capítulo VII.

## III.4 Concentración de mercado: el índice de Herfindahl-Hirschman

La estructura de mercado de cada mineral se describe con el índice de Herfindahl-Hirschman (HHI), definido como la suma de los cuadrados de las participaciones de mercado:

$$\text{HHI} = \sum_{k} s_k^{2}, \qquad s_k \in [0,1] ,$$

expresado en la escala habitual de 0 a 10 000. Se calcula sobre la producción por mineral a partir de los numeradores de empresa o de unidad minera documentados en fuentes primarias (CAMIMEX y USGS). La serie 2004-2020 se reconstruye por **régimen de mercado** —a partir del líder y los grupos conocidos, con el residual tratado de forma atomística—, lo que la convierte en una **cota inferior** no estrictamente comparable en nivel con el tramo 2021-2024, calculado por mina; por ello la serie se lee por su trayectoria, no por su nivel puntual.

Un segundo índice, el **HHI geográfico**, aplica la misma fórmula a las participaciones de las entidades federativas en la extracción de cada mineral, y describe la concentración territorial de la producción. Ambos son descriptores complementarios: el primero caracteriza la estructura empresarial (Capítulo V); el segundo, la dimensión espacial del enclave (Capítulo VIII).

## III.5 El coeficiente de captura de valor

El índice de Ghosh está atado a los dos cortes de la MIP. Para dar profundidad temporal al encadenamiento hacia adelante se construye un segundo descriptor, el **coeficiente de captura de valor** (CCV), como serie anual mineral-año 1992-2025. Para cada mineral $m$ y año $t$,

$$\text{CCV}_{m,t} = \frac{v^{E1}_{m,t}}{p^{\text{USGS}}_{m,t}} ,$$

donde $v^{E1}_{m,t}$ es el valor unitario de exportación del mineral en su forma bruta (mena o concentrado, etapa comercial 1) y $p^{\text{USGS}}_{m,t}$ es el precio del producto de referencia refinado del USGS. Un CCV cercano a 1 indica que la forma exportada en bruto ya vale casi como el producto refinado; uno cercano a 0, que la exportación bruta capta poco de ese valor —mayor distancia al eslabón procesado—. Un CCV bajo y persistente es el descriptor de serie del enclave estructural. El numerador procede de UN Comtrade (fracciones de exportación de México, con valor y peso); el denominador, de los precios del USGS empalmados. Los huecos se completaron con datos espejo —lo que los socios reportan importar desde México—, marcados como tales; el único hueco no completable (plomo, 1994) se declara y no se imputa. El poder descriptivo del CCV depende del grupo mineral —es nítido en los metales base y un artefacto de ley en oro y plata—, matiz que se discute con los resultados en el Capítulo VI.

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

Para situar el caso mexicano se emplean las tablas de insumo-producto inter-país de la OCDE (edición 2023, corte 2018, el mismo año del Ghosh nacional). Sobre el bloque doméstico de nueve países se calcula el encadenamiento hacia adelante del sector-minería no energética con el método de III.2 (índice de Ghosh-Rasmussen, media de cada economía = 1), y su versión por eslabón (extracción, refinación C24, semimanufactura C25). La comparación es a nivel de sector-minería agregado, no por mineral.

Como el índice de Ghosh es un coeficiente de asignación y no mide cuánto valor retiene el país, se añade una **descomposición de valor agregado**. Sobre la matriz global se separa, del valor agregado minero que cada país exporta, la parte que sale ya transformada en casa —embebida en las exportaciones de otros sectores— de la que sale como producto minero en crudo para reprocesarse en el extranjero. Esa segunda fracción, el *crudo_share*, es la firma del enclave en dinero: un valor alto revela que el valor de la minería se realiza fuera del país. Esta descomposición es la que separa nítidamente a economías con un índice de Ghosh casi idéntico pero capturas de valor opuestas, y evidencia por qué el índice agregado engaña cuando promedia minerales que sí se funden en el país con otros que se exportan en concentrado.

## III.10 Peso del bloque y precios de referencia

Dos construcciones dan soporte a los indicadores anteriores. La primera es el **peso del bloque** de diez minerales en la economía —su participación en el PIB, las exportaciones y el empleo, y la descomposición del valor de producción entre precio y volumen—, que sustenta la justificación del objeto en el Capítulo I. El valor de producción de cada mineral es $V_{m,t}=Q_{m,t}\,p_{m,t}$ (volumen por precio), y la variación entre dos años se descompone en un índice de volumen y uno de precio. La segunda es la serie de **precios anuales del USGS empalmados** (1992-2025, en términos nominales y constantes de 1998), que sirve de denominador al CCV y de valuador de la producción. Ambas se apoyan en fuentes primarias (MIP del INEGI para PIB y empleo; UN Comtrade y USGS para exportaciones, producción y precios) y se documentan en el Anexo B.

## III.11 Criterio de tratamiento de datos: declarar, no imputar

Todo el trabajo se rige por un criterio explícito: los vacíos de las series se declaran y, cuando se intenta llenarlos, se hace con una fuente identificada y marcada (comercio espejo para los huecos del CCV; reconstrucción por régimen para el HHI histórico), nunca con supuestos ni interpolaciones silenciosas. Este criterio, además de honestidad metodológica, protege la lectura descriptiva: el retrato del enclave no descansa en ningún dato imputado, sino en la convergencia de indicadores independientes calculados sobre datos observados. El Cuadro {{cua:sintesis}} sintetiza el conjunto y su articulación; la declaración de vacíos por indicador se recoge en el Anexo D.

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
