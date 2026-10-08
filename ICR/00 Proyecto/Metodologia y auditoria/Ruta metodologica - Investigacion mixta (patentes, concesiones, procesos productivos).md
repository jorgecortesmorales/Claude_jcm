---
title: "Ruta metodológica — Investigación mixta: patentes, concesiones y procesos productivos (módulos C, D, E)"
type: metodologia
tags: [icr, metodologia, ruta, metodos-mixtos, patentes, concesiones, procesos, innovacion, capacidades-tecnologicas]
created: 2026-10-08
updated: 2026-10-08
status: propuesta
inclusion_icr: por definir
---

# Ruta metodológica — Investigación mixta: patentes, concesiones y procesos productivos

> [!info] Para qué sirve esta nota
> Diseña una investigación de métodos mixtos (cuantitativo + cualitativo) sobre tres variables nuevas: **C. patentes**, **D. concesiones** y **E. procesos productivos** (extracción, concentración, refinación y transformación, en México y en el mundo). Está escrita para funcionar de dos formas: como **módulo de la ICR** (complemento de capítulos o capítulo nuevo) o como **investigación independiente**. No hay nada calculado todavía.

## 1. Pregunta, objeto y unidad de análisis

**Pregunta general.** ¿Qué capacidades tecnológicas e institucionales acompañan a la extracción de los diez minerales críticos en México y cómo se comparan con las de otros países productores?

**Preguntas específicas.**

| Módulo | Pregunta | Tipo |
|---|---|---|
| C1 | ¿Cuántas patentes se crean por mineral, eslabón, país y año? | Cuantitativa |
| C2 | ¿Cómo se clasifican según las taxonomías existentes? | Cuantitativa (codificación) |
| C3 | ¿Cuántas se usan efectivamente? | Cuantitativa con indicadores indirectos + cualitativa |
| C4 | ¿Por qué no se usan las que no se usan? | Documental + datos (entrevista solo complementaria) |
| D1 | ¿Cómo se ha comportado el número de concesiones (títulos, superficie, titulares) entre 1992 y 2025? | Cuantitativa |
| D2 | ¿Cuántas concesiones se han convertido en proyectos y en cuánto tiempo? | Cuantitativa |
| D3 | ¿Por qué la mayoría no llega a proyecto? | Documental + datos (sin entrevistas) |
| E1 | ¿Qué procesos existen en el mundo por mineral y eslabón? | Documental |
| E2 | ¿Cuáles se usan en México, dónde y por quién? | Documental + cuantitativa |
| E3 | ¿Por qué esos y no otros, y qué tan cerca de la frontera están? | Documental + cualitativa |

**Unidad de análisis:** mineral × eslabón (L0-L4, la misma notación del Cap. III y del Anexo C) × país × año. Mantener esa unidad es lo que permite cruzar los tres módulos entre sí y con los indicadores ya construidos (HHI, Ghosh, HEM, CCV, comercio por etapa).

## 2. Diseño de métodos mixtos

**Diseño secuencial explicativo** (Creswell y Plano Clark, por fichar): primero la fase cuantitativa (conteos, series, tasas de conversión), después la cualitativa, que se diseña con los resultados de la primera (qué patentes, concesiones u operaciones revisar a fondo). **La fase cualitativa es documental**: las razones se obtienen de registros administrativos, documentos de empresas y de gobierno, y literatura publicada. Las entrevistas no son fuente principal; en patentes y procesos se reservan para validar casos donde los documentos se contradicen o callan, y en concesiones no se usan. La integración se hace en una **matriz conjunta** mineral × eslabón que pone lado a lado patentes (C), proyectos (D) y procesos (E).

> [!note] Pauta descriptiva
> Las fases cuantitativas describen. Las respuestas a los «por qué» (C4, D3, E3) son las razones que **declaran los actores y los documentos**, codificadas y contadas, no relaciones estimadas entre variables. Si la investigación entra a la ICR, se redactan con la misma pauta que el resto del manuscrito.

## 3. Módulo C — Patentes

### 3.1 Fuentes

| Fuente | Uso | Acceso |
|---|---|---|
| **Lens.org** | Familias, citas, situación jurídica; búsqueda por CPC y texto; API | Gratuito (registro) |
| **USPTO PatentsView** | Datos masivos de EUA: cesionarios, citas, cesiones | Gratuito |
| **Espacenet / PATSTAT (EPO)** | Familias DOCDB/INPADOC, situación jurídica mundial | Espacenet gratuito; PATSTAT de pago (consultar acceso por la UAM) |
| **WIPO PATENTSCOPE** | Solicitudes PCT | Gratuito |
| **IMPI (SIGA, ViDoc)** | Patentes solicitadas y concedidas en México; licencias inscritas | Gratuito; las licencias por solicitud de información |
| Google Patents en BigQuery | Alternativa masiva | Gratuito con límite |

### 3.2 Identificación del universo

1. **Clases CPC/IPC por eslabón** (lista inicial, a validar contra el esquema CPC vigente):
   - Minado: E21C, E21D, E21F.
   - Trituración y molienda: B02C.
   - Separación y concentración: B03B, B03C, B03D (flotación).
   - Metalurgia extractiva: C22B, con subgrupos por metal (cobre, metales nobles, plomo, zinc, manganeso; hidrometalurgia).
   - Electrometalurgia: C25C.
   - No metálicos: C01B (carbono y grafito, silicio, flúor y HF), C01F (compuestos de calcio, estroncio y bario), C01G (manganeso).
   - Tecnologías de mitigación en metalurgia: Y02P.
2. **Palabras clave por mineral** combinadas con las clases, para separar cobre de zinc, etc.
3. **Validación**: comparar el universo con el conjunto de patentes mineras de la OMPI (Daly et al., 2019, *Mining patent data*, por fichar) y revisar a mano una muestra aleatoria (precisión y exhaustividad de la búsqueda).

### 3.3 Indicadores cuantitativos (C1)

- **Unidad de conteo: familia de patentes**, por año de prioridad, con conteo fraccional por país del solicitante y del inventor. Evita contar dos veces la misma invención presentada en varias oficinas.
- Número de familias por mineral × eslabón × país × año; participación de México; patentes concedidas frente a solicitadas.
- **Ventaja tecnológica revelada** (Soete, 1987, por fichar):

$$RTA_{ij} = \frac{P_{ij} / \sum_j P_{ij}}{\sum_i P_{ij} / \sum_i \sum_j P_{ij}} \qquad\qquad (1)$$

donde $P_{ij}$ es el número de familias del país $i$ en el eslabón o tecnología $j$.

- **Calidad**: citas recibidas, tamaño de la familia, familias triádicas (indicadores de la OCDE; Squicciarini, Dernis y Criscuolo, 2013, por fichar).
- **Quién patenta**: empresas mineras, proveedores de equipo y servicios (METS), universidades y centros públicos.

### 3.4 Clasificación teórica (C2)

Cada familia se clasifica en cinco dimensiones:

| Dimensión | Categorías | Base teórica (por fichar) | Cómo se asigna |
|---|---|---|---|
| Objeto | Producto / proceso | Manual de Oslo (OCDE-Eurostat, 2018) | Reivindicaciones + CPC |
| Grado de novedad | Incremental / radical (y modular / arquitectónica) | Henderson y Clark (1990); índices de originalidad y radicalidad de la OCDE | Indicadores de citas + codificación manual |
| Eslabón | L0-L4 | Notación de la ICR | Mapeo CPC → eslabón |
| Fuente sectorial | Dominada por proveedores / intensiva en escala / proveedores especializados / basada en ciencia | Pavitt (1984) | Tipo de solicitante |
| Ambiental | Verde / no verde | Etiqueta Y02 | CPC |

La codificación manual se hace sobre una **muestra estratificada**, con dos codificadores y acuerdo medido con kappa de Cohen.

### 3.5 Uso efectivo (C3)

No hay un registro directo del uso. Se combinan indicadores, de más indirecto a más directo:

1. **Mantenimiento**: pago de anualidades y vigencia (situación jurídica INPADOC/IMPI). Una patente que se deja caducar pronto rara vez está en uso.
2. **Licencias y cesiones**: registro de cesiones de la USPTO; licencias inscritas en el IMPI.
3. **Uso observado**: correspondencia entre la tecnología de la patente y los procesos que describen los reportes técnicos de las operaciones (enlace con el módulo E).
4. **Tipología de uso** de Torrisi et al. (2016, por fichar): uso interno, licenciada, de bloqueo, durmiente. Cada familia se asigna a una categoría con las evidencias 1-3 y las de 3.6; la entrevista solo se usa para validar una submuestra.

### 3.6 Razones de no uso (C4): de dónde salen sin depender de entrevistas

Seis fuentes, de la más estructurada a la más interpretativa. Cada razón se registra con su fuente y el fragmento que la sustenta, y se cuentan por mineral, eslabón, tipo de titular y país.

1. **El evento jurídico de terminación** (INPADOC *legal events*, gaceta del IMPI): dice *cómo* terminó la patente —caducidad por falta de pago de anualidades, retiro, abandono, rechazo, nulidad tras oposición—. Separa la patente que el titular dejó caer (decisión económica) de la que nunca se concedió (problema técnico o de novedad). Es un dato, no una interpretación.
2. **Encuestas ya publicadas a inventores y titulares**, como evidencia secundaria: PatVal-EU (Giuri et al., 2007), Torrisi et al. (2016), la encuesta RIETI-Georgia Tech (Walsh y Nagaoka, 2009) y la encuesta anual de la Oficina Japonesa de Patentes sobre utilización de patentes (todas por fichar y verificar). Publican la proporción de patentes no usadas y sus razones declaradas por campo tecnológico y tipo de titular. Se aplican a nuestro universo como **distribución de referencia** por campo (metalurgia, minería, química inorgánica), marcada como proyección y no como dato propio.
3. **Señales de bloqueo en los propios datos**: familias citadas por los examinadores como anterioridad que limita solicitudes de competidores (citas de categoría X/Y), y familias con cobertura en países donde el titular no tiene operaciones ni ventas. Son indicadores de uso estratégico, no de uso productivo.
4. **Estudios de alternativas de proceso en los reportes técnicos** (módulo E): los estudios de factibilidad NI 43-101 y JORC comparan tecnologías candidatas y dicen por qué se descartó cada una (recuperación, costo de reactivos, agua, energía, escala, riesgo de escalamiento). Es la fuente documental más directa del porqué de la no adopción de una tecnología en una operación concreta.
5. **Literatura técnica de revisión** sobre cada tecnología (revistas como *Minerals Engineering*, *Hydrometallurgy*, *Journal of Cleaner Production*), con una revisión sistemática con protocolo PRISMA: cadenas de búsqueda por tecnología, criterios de inclusión explícitos y registro de las barreras al escalamiento industrial que reporta cada artículo.
6. **Documentos de los titulares**: informes anuales y de sostenibilidad de las empresas (tecnologías abandonadas, pruebas piloto), informes de las oficinas de transferencia de universidades y centros públicos, estadísticas del IMPI sobre licencias, y expedientes de litigio o de licencia obligatoria por falta de explotación (Ley Federal de Protección a la Propiedad Industrial, artículos a verificar).

**Codificación** (ver [[Codificacion tematica]]) con categorías iniciales de la literatura (por fichar): falta de activos complementarios (Teece, 1986), uso estratégico o de bloqueo, costo o mercado insuficiente, inmadurez tecnológica (TRL) o fracaso del escalamiento, regulación, y capacidad de absorción (Cohen y Levinthal, 1990); se admiten categorías emergentes. Dos codificadores sobre una muestra común; acuerdo con kappa de Cohen.

**Entrevista (complementaria):** solo para los casos de la muestra donde las seis fuentes no dan razón o se contradicen.

## 4. Módulo D — Concesiones

### 4.1 Fuentes

| Fuente | Uso | ¿La tenemos? |
|---|---|---|
| **Cartografía Minera** (SE-DGRM): polígonos de concesiones vigentes | Títulos, superficie, titular, ubicación | No |
| **Registro Público de Minería** y solicitudes a la **Plataforma Nacional de Transparencia** | Serie histórica de títulos otorgados, vigentes, cancelados y caducos | No (las solicitudes tienen plazo legal de respuesta) |
| **Informes Anuales de CAMIMEX** 2005-2023 | Números agregados de concesiones y superficie, y proyectos | **Sí** (`10 Datos/Bases Originales/08 CAMIMEX Informes Anuales/`; hay menciones de concesiones en 21 informes) |
| **Anuarios del SGM** | Estadística de concesiones y producción | **Sí** (`09 SGM Anuarios`) |
| SE: «Proyectos mineros operados por compañías de capital extranjero» (anual) | Proyectos por etapa (exploración, desarrollo, producción) | No |
| Reportes NI 43-101 / 10-K / informes anuales | Proyecto ↔ título de concesión | No |
| DOF; Ley Minera y reforma de 2023 | Cambios de régimen | **Sí** (`15 Marco Institucional/Mexico/`) |
| Bases de organizaciones civiles (CartoCrítica, Fundar) | Series históricas ya depuradas, para cotejo | No |

### 4.2 Método

1. **Panel de títulos**: número de título, fecha de expedición, vigencia, superficie, titular, entidad, municipio, polígono, estado (vigente, cancelado, caduco).
2. **Serie D1**: títulos otorgados, vigentes y cancelados por año; superficie concesionada (ha y % del territorio) por entidad; concentración de la superficie por titular (**HHI de hectáreas**, misma fórmula del Cap. III).
3. **Conversión en proyecto (D2)**:
   - Enlace título ↔ proyecto con un **cruce espacial** (SIG) de los polígonos con las ubicaciones de minas y proyectos (SGM, SE, reportes técnicos), y por titular.
   - **Embudo por cohorte** de otorgamiento: título → exploración → desarrollo → producción.
   - **Tasa de conversión**: $c_{g,e} = N_{g,e} / N_g$, con $N_g$ = títulos de la cohorte $g$ y $N_{g,e}$ = los que alcanzaron la etapa $e$.
   - **Tiempo hasta producción**: curvas de supervivencia de Kaplan-Meier, descriptivas, por cohorte, tipo de titular y entidad.
4. **Asignación de mineral**: los títulos mexicanos no se otorgan por mineral, así que el mineral se asigna por el proyecto enlazado o, a falta de proyecto, por las ocurrencias minerales del SGM dentro del polígono (con marca de imputación).
### 4.3 Razones de no conversión (D3): solo documentos, registros y literatura

**a) La retención especulativa del título como posibilidad explicativa parcial.** La concesión puede funcionar como un activo financiero: empresas *junior* que cotizan en bolsas de riesgo (TSX-V, ASX) adquieren títulos, levantan capital con ellos, los ceden en opción o en *joint venture* y los venden, sin pasar a desarrollo. La ruta no supone que esto ocurra; lo describe con indicadores observables:

| Indicador | Fuente | Qué describe |
|---|---|---|
| **Cesiones y transmisiones de derechos** por título antes de cualquier obra | Registro Público de Minería (solicitud de transparencia) | Rotación del título como activo |
| **Tipo de titular**: productora, *junior* listada, persona física, otra | Registro + listados de TSX-V/ASX/BMV | Quién retiene la superficie |
| **Superficie en manos de titulares sin producción** (ha y %) | Panel de títulos + enlace con proyectos | Magnitud de la superficie sin actividad |
| **Comprobación de obras y trabajos** (títulos con y sin informes) | Registro / DGRM (obligación de la Ley Minera, artículos a verificar) | Actividad declarada por título |
| **Derecho adicional por concesiones inactivas**: recaudación y número de títulos que lo pagan | SAT / SHCP; Ley Federal de Derechos (artículo a verificar) | Inactividad reconocida fiscalmente |
| **Cancelaciones por falta de pago** y declaratorias de libertad de terreno | DOF | Títulos que se abandonan |
| **Anuncios de opción, venta o *farm-out*** de propiedades mexicanas | Comunicados de SEDAR+ y ASX | Transacciones del título como activo |

Los momentos de solicitud y de cesión se presentan en una **cronología junto con el ciclo de precios** del Cap. IV, sin estimar la relación (pauta descriptiva).

**b) Otras razones documentadas**, con la misma regla de registrar fuente y fragmento:

- Diagnóstico del propio gobierno: exposición de motivos de la reforma de 2023 y de la de 2014, informes de labores de la SE.
- Auditorías de la **Auditoría Superior de la Federación** a la administración de concesiones (verificación de obras, cobro de derechos).
- Permisos ambientales: resoluciones de MIA de la SEMARNAT (Gaceta Ecológica).
- Conflicto social y consulta: bases de conflictos mineros (OCMAL, EJAtlas) y resoluciones de la SCJN sobre consulta indígena.
- Razones de empresa: secciones de riesgos y de discusión de resultados (MD&A) de informes trimestrales y anuales, y listas de proyectos suspendidos (SE, CAMIMEX).
- Literatura académica y de organizaciones civiles sobre concesiones en México (por fichar: trabajos de Fundar, CartoCrítica y estudios académicos sobre minería y acaparamiento de tierra en México; literatura sobre exploración especulativa de empresas *junior*).

**Categorías de codificación iniciales:** retención especulativa o financiera del título, financiamiento, precios, permisos ambientales, conflicto social y consulta, ley o tamaño del yacimiento insuficiente, cambio regulatorio (2014, 2023), litigio. Se cuentan por cohorte, tipo de titular, entidad y mineral. **No se usan entrevistas.**

## 5. Módulo E — Procesos productivos (responde también a la pregunta B)

El detalle del instrumento está en [[Ruta metodologica - Preguntas A y B (cobre-EUA; metodos y frontera tecnologica)]] (B.2-B.3). En resumen:

1. **Catálogo mundial** de procesos por mineral × eslabón (manuales técnicos, USGS, Cochilco, ICSG, ILZSG).
2. **Ficha técnica por operación** en México y en los países de comparación del Cap. VII (Chile, Perú, Australia, Brasil, China, Finlandia, Suecia), con libro de códigos común.
3. **Índice de adopción de tecnologías de frontera** por operación, empresa y país.
4. **Razones de elección** codificadas a partir de la justificación y de los estudios de alternativas de los reportes técnicos; entrevistas a ingenieros de planta o proveedores (METS) solo como complemento.
5. **Comparación con los siete países de la ICR** (Chile, Perú, Australia, Brasil, China, Finlandia, Suecia), mineral por mineral donde el país tenga la operación.

## 6. Integración de los tres módulos

| Mineral | Eslabón | C: familias de patentes (México / mundo; RTA) | D: concesiones → proyectos (tasa de conversión) | E: proceso usado en México / frontera (índice de adopción) |
|---|---|---|---|---|
| … | L1 … L4 | | | |

La matriz se cruza con los indicadores que ya existen en la ICR (HHI, Ghosh y HEM por eslabón, CCV, comercio por etapa, tipología A/B/C/D) en una sola lectura por mineral, como las fichas del Anexo C.

## 7. Cómo encaja en la ICR, o fuera de ella

| Opción | Dónde va | Ventaja | Costo |
|---|---|---|---|
| **a) Complementos** | D → Cap. IV (marco institucional) y V (estructura); E → Cap. III (método) y fichas del Anexo C; C → recuadro en VIII | No altera la arquitectura de 9 capítulos | La innovación queda dispersa |
| **b) Capítulo nuevo** | «Capacidades tecnológicas: patentes, concesiones y procesos», entre VIII y IX | Lectura integrada; la tipología del Cap. VIII gana una dimensión | Más extensión; requiere ajustar preguntas, objetivos y el Cap. IX |
| **c) Independiente** | Artículo o documento de trabajo con pregunta y marco propios | No compromete el calendario de la ICR | Pierde el cruce con los indicadores del manuscrito, salvo que se cite |

Para que funcione en las tres opciones: el módulo lleva **marco propio** (innovación en minería y encadenamientos laterales; por fichar: Morris, Kaplinsky y Kaplan, 2012; Bartos, 2007; Pietrobelli, Marin y Olivari, 2018), **datos y scripts en carpetas propias** (`10 Datos/Bases Originales/16 Patentes`, `17 Concesiones`, `18 Procesos`; scripts `pat_*.py`, `con_*.py`, `proc_*.py`) y **la misma unidad mineral × eslabón**, que es lo que permite volver a integrarlo.

## 8. Fases y esfuerzo estimado

| Fase | Contenido | Semanas (aprox.) |
|---|---|---|
| 0 | Protocolo del módulo, libro de códigos, solicitudes de transparencia (D) y de acceso a PATSTAT (C) | 2 |
| 1 | D cuantitativo: panel de títulos, series, enlace espacial con proyectos | 3-4 |
| 2 | C cuantitativo: búsqueda, validación, conteos, RTA, clasificación | 4-5 |
| 3 | E documental: catálogo, fichas por operación, índice de adopción | 3-4 |
| 4 | Fase cualitativa documental: codificación de razones (C4, D3, E3), revisión sistemática; entrevistas complementarias solo en C y E | 4-5 |
| 5 | Integración, matriz conjunta, redacción | 2-3 |

**Piloto recomendado: cobre**, en los tres módulos. Es el mineral con más documentación pública (10-K de Southern Copper, títulos de Grupo México, patentes de metalurgia del cobre) y el que motiva la pregunta A. Con el piloto se calibran el libro de códigos y los tiempos antes de pasar a los otros nueve.

## 9. Riesgos y límites

- **Series históricas de concesiones** incompletas en datos abiertos; dependen de las solicitudes de transparencia.
- **Uso de patentes**: los indicadores indirectos (mantenimiento, licencias) subestiman el uso interno no registrado; la entrevista lo corrige solo en la muestra.
- **Atribución por mineral**: varias clases CPC (C22B de hidrometalurgia, B03D) son comunes a varios metales; se marca la atribuibilidad como en el HEM por eslabón.
- **Fuentes documentales**: los registros de cesiones y de comprobación de obras dependen de solicitudes de transparencia; si no se obtienen, D3 se apoya en el DOF, la ASF, los comunicados de SEDAR+/ASX y la literatura.
- **Entrevistas complementarias** (C y E): si se hacen, requieren consentimiento informado y, si se publica, aval ético de la UAM.

## Decisiones pendientes del alumno

- [ ] Opción de inclusión: a) complementos, b) capítulo nuevo, c) independiente.
- [ ] Alcance: los diez minerales o piloto de cobre primero.
- [x] Las razones de no uso (C4) y de no conversión (D3) salen de datos y documentos; entrevistas solo complementarias en C y E (decisión del alumno, 2026-10-08).
- [ ] ¿Se gestiona acceso a PATSTAT por la UAM o se trabaja con Lens.org y PatentsView?

← [[Ruta metodologica - Preguntas A y B (cobre-EUA; metodos y frontera tecnologica)]] · [[Ruta metodologica - Construccion de cadenas de valor locales por mineral]] · [[Handoff - Estado actual (HEM, consolidado y certificacion) 2026-09-29]] · [[Bitacora]]
