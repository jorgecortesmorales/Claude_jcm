---
title: "Memoria — Georreferenciación y destinos (extracción, transformación, exportación)"
type: resultados
tags: [icr, georreferenciacion, comercio, destinos, cadenas-de-valor, enclave]
created: 2026-09-06
updated: 2026-09-06
status: activo
---

# Memoria — Georreferenciación y destinos

> [!info] Qué añade
> Sitúa **en el espacio** el enclave estructural: (1) dónde se **extrae** cada mineral, (2) dónde —y si— se **transforma** dentro del país, y (3) a qué **países** se exporta lo que no se sigue transformando. Diseño descriptivo; los datos son el aporte. Complementa el Ghosh/CCV/comercio con la dimensión territorial y de destino.

## 1. Extracción por mineral y estado (¿dónde se saca?)

**Cuantitativo (paso 5, 2026-09-06):** `10 Datos/processed/georref_extraccion_mineral_estado_cuantitativo.csv` — producción por mineral×entidad **2024**, con participación (%). Fuente: SGM, *Anuario Estadístico de la Minería Mexicana* 2025, tablas "Producción minera por entidad federativa" (leídas página por página como imagen; el texto del PDF venía desalineado). Se conserva el cualitativo previo en `georref_extraccion_mineral_estado.csv`.

| Mineral | Estado líder (2024) | Participación líder | Otros estados relevantes (2024) |
|---|---|--:|---|
| Cobre | **Sonora** | 70% | Zacatecas 16%, SLP 4% |
| Oro | **Sonora** | 32% | Zacatecas 32%, Guerrero 16%, Chihuahua 8% |
| Plata | **Zacatecas** | 50% | Chihuahua 15%, Sonora 12%, Durango 11% |
| Plomo | **Zacatecas** | 71% | Chihuahua 17%, Durango 4% |
| Zinc | **Zacatecas** | 56% | Chihuahua 11%, Durango 10%, Sonora 8% |
| Fluorita | **San Luis Potosí** | 96% | Durango 3%, Coahuila 1% |
| Barita | **Nuevo León** | 59% | Sonora 38% (juntos 97%) |
| Grafito | **Sonora** | 100% | (único) |
| Manganeso | **Hidalgo** | 100% | (único; Molango) |
| Sílice | **Coahuila** | 52% | Puebla 39%, Baja California 8% |

> [!important] Concentración geográfica de la extracción (hallazgo)
> La extracción está **muy concentrada en el espacio**: **Zacatecas** domina los metales preciosos y de coextracción (plata 50%, plomo 71%, zinc 56%); **Sonora** domina cobre (70%), oro (junto a Zacatecas) y grafito (100%); **San Luis Potosí** concentra la fluorita (96%, Las Cuevas); **Hidalgo** el manganeso (100%, Molango); **Nuevo León + Sonora** la barita (97%); **Coahuila + Puebla** la sílice (91%). Es un mapa de **enclaves regionales por mineral**.
>
> Correcciones vs. el cualitativo previo (con el dato 2024): la **barita** la lidera **Nuevo León** (no Coahuila); la **sílice 2024** la lideran **Coahuila y Puebla** (Veracruz —histórico— cayó a ~0 en 2024).

> [!note] Cuidados
> (a) Unidades: oro/plata en **kg**; el resto en **toneladas**. (b) 2024 son cifras **preliminares** (p/) del SGM. (c) La producción por mineral del SGM difiere en nivel de la de CAMIMEX usada en el HHI (fuentes/criterios distintos); no se mezclan. (d) Como cross-check, el total nacional de cobre 2024 del SGM (777,106 t) **corrobora** el estimado usado en el HHI (~755,000 t, dif. ~3%). `sgm_6_...csv` da además el **valor minero total por estado** (2019-2023).

## 2. Transformación por nodo y estado (¿dónde —y si— se transforma?)

Base: `10 Datos/processed/georref_transformacion_nodos.csv` (derivado del directorio de 19 empresas verificadas).

- **Cobre**: fundición/refinación **junto a la mina** en Sonora (La Caridad–Nacozari, Cananea) + refinería en CDMX; semis (alambre/cable) en el corredor industrial (Monterrey/SLP, CDMX).
- **Oro, plata, plomo, zinc**: un solo gran nodo de refinación — **Torreón, Coahuila** (Met-Mex Peñoles) — más zinc en **SLP** (IMMSA) y baterías en **Nuevo León** (Clarios).
- **Manganeso**: ferroaleaciones de Autlán en **Veracruz (Tamós), Puebla (Teziutlán), Durango (Gómez Palacio)**.
- **Fluorita**: ácido fluorhídrico en **Matamoros, Tamaulipas** (Koura) — el único eslabón químico avanzado.
- **Sílice**: vidrio en **Monterrey** (Vitro) — pero el silicio metálico se importa.
- **Grafito**: no hay transformación del mineral; la industria usuaria (acero EAF) usa electrodos **importados**.
- **Barita**: no hay transformación; uso directo como densificante en **perforación petrolera** (Golfo/Campeche).

**El enclave en el espacio.** La transformación existente es **puntual** (uno o dos nodos por mineral) y, para los metales del noroeste, pegada a la mina hasta el metal refinado; la manufactura de mayor valor (semis, químicos) es delgada, se concentra en el corredor Monterrey–CDMX o **está ausente**. Hay una desconexión territorial entre las muchas zonas de extracción y los pocos nodos de transformación.

## 3. Destinos de exportación (¿a dónde va lo que no se transforma?)

Base: `10 Datos/processed/comercio_destinos_mineral_etapa.csv` (UN Comtrade, México reportante, flujo X, acumulado 2019-2024, por país socio). Foco en E1 (crudo) y E2 (procesado/refinado).

| Mineral · etapa | Destino principal | Lectura |
|---|---|---|
| **Cobre · concentrado (E1)** | **China 94.7 %** (Japón, EUA marginales) | El concentrado se **funde/refina en China**, no en México |
| Cobre · refinado (E2) | EUA 69 %, China 26 % | El cátodo/refinado sí va a Norteamérica |
| **Plomo · concentrado (E1)** | **China 65 %, Corea 26.5 %** | Fundición en Asia |
| **Zinc · concentrado (E1)** | **Corea 58 %, Japón 11 %, Bélgica 11 %** | Refinación en Asia/Europa |
| **Oro/plata · concentrado (E1)** | China, Corea, Alemania | Refinación fuera |
| Oro/plata · doré/bullion (E2) | **EUA 79-98 %** (Suiza) | Forma estándar hacia EUA/Suiza |
| **Fluorita · espato (E1)** | **EUA 88 %**, China | Grado ácido a EUA |
| Fluorita · fluoroquímica/HF (E2) | **EUA 100 %** | El HF va íntegro a EUA |
| Grafito, sílice, manganeso, barita | **EUA ~90-100 %** | Proximidad (T-MEC) |

> [!important] Hallazgo
> Se distinguen **dos geografías de la fuga de valor**: (a) los **concentrados de metales base y preciosos** viajan a **China y el este de Asia** (y algo a Europa) —donde está la capacidad de fundición/refinación—; (b) las **formas ya procesadas o refinadas** y los **no metálicos** van sobre todo a **Estados Unidos** por proximidad. Es decir, la transformación que México no hace **ocurre en China/Asia** para los concentrados: el valor agregado se genera allá. Esto espacializa el enclave y matiza la idea de una simple dependencia de EUA.

> [!note] Cuidado
> Comtrade reporta el país **socio declarado por México**, que puede diferir del **destino final de consumo** por reexportaciones/entrepôt (p. ej. metales preciosos vía Suiza; concentrados vía puertos asiáticos). Léase como destino comercial inmediato, no necesariamente final.

### 3.1 Cómo cambió el destino en el tiempo (serie 1992-2024)

Base: `10 Datos/processed/comercio_destinos_serie_resumen.csv` (crudo por año en `comercio_destinos_serie_crudo.csv`). Muestra un **desplazamiento geográfico** nítido en los concentrados: de **Norteamérica/Europa (1990s)** a **Asia —sobre todo China— (2010s-2020s)**.

| Mineral · etapa | Destino principal — trayectoria | China (fin de serie) |
|---|---|---|
| **Cobre · concentrado (E1)** | EUA 100% (1995) → China 34% (2004) → **China 94% (2022)** | **94%** |
| **Plomo · concentrado (E1)** | EUA 100% (1992) → Canadá/Suiza → China/Corea; **China 63% (2024)** | 63% |
| **Zinc · concentrado (E1)** | Bélgica/Francia (1990s-2000s) → Corea/China; **Corea 61% (2024)** | 30% |
| **Oro · concentrado (E1)** | EUA 100% (1990s) → Perú/Corea → **China 98% (2024)** | 98% |
| **Fluorita · fluoroquímica/HF (E2)** | **EUA ~72-100% en toda la serie** (proximidad) | 0% |

> [!important] Doble profundización del enclave (une el paso 1 y el paso 3)
> Dos tendencias se refuerzan: (a) México exporta **cada vez más en bruto** (share E1 del cobre ~2%→81%, ver comercio por etapa 1992-2024); y (b) ese bruto va **cada vez más a Asia/China** para transformarse. Es decir, el valor agregado que México no capta se genera crecientemente en **China**. Los procesados y no metálicos (HF, sílice) siguen anclados a **EUA** por proximidad (T-MEC).

> [!note] Cobertura por mineral y huecos declarados (serie de destinos)
> La serie usa el **reporte de exportación propio de México** (no espejo), así que hereda sus huecos donde el flujo fue mínimo o no se reportó. Cobertura 1992-2024 por mineral (etapa principal exportada):
> - **Completos y robustos:** cobre (E1-E4), fluorita (E1 espato, E2 HF), grafito (E1-E3), sílice (E1-E2), oro E2 (doré), plata E2 (bullion), joyería oro-plata E4.
> - **Con huecos menores (flujo delgado o año faltante):** plomo E1 (falta 1994), oro E1 (n=29; el oro casi no sale como mena, sale como doré E2), plata E1 (n=32), zinc/plomo en E3/E4 (semis/manufacturas: valores pequeños → shares ruidosos).
> - **Huecos por declarar:** **manganeso E1** solo 1992-2014 (México deja de reportar exportación de mineral de manganeso desde 2015; el flujo residual sí aparece por espejo —ver CCV— pero aquí no se rellenó; su historia de destino es sobre todo **E2 ferroaleaciones → EUA**, que sí está completa). **Barita E1** con huecos 2014-2020 (exportación en crudo esporádica); **barita E2 (químicos de bario)** cesa como flujo reportado tras 2017.
> - **Cosmético:** un par de años tempranos de zinc traen `socio_58` = Bélgica (código antiguo Bélgica-Luxemburgo).
> Ninguno se imputa; los huecos se declaran. El manganeso E1 2015-2024 podría rellenarse por espejo (como en el CCV) si se desea nivel de detalle de destino para ese flujo menor.

### 3.2 Los huecos de destino los explica la inserción por etapa

Los huecos de la serie de destinos **no son un defecto de dato: son la ausencia real de un flujo**, y la **composición por etapa** (`comercio_por_etapa_1992_2024.csv`) lo confirma. Un destino solo puede existir si hay exportación en esa etapa; donde la etapa cae a ~0, no hay a quién reportar.

- **Manganeso**: la exportación de **mena (E1)** pasa de ~$11 M (2013) a **$0 desde 2015**, mientras la de **ferroaleaciones (E2)** continúa. Por eso los destinos de manganeso E1 terminan en 2014: México dejó de exportar el mineral en bruto porque lo **transforma dentro del país** (ferroaleaciones de Autlán) — el "hueco" es en realidad un **hallazgo** (cadena local que sustituye la exportación cruda).
- **Barita**: la **E1 (crudo)** es intermitente ($28.9 M en 2013; ~$0 en 2018; $13-19 M en 2021-2024) y la **E2 (químicos de bario) cesa tras 2000**. Los huecos de destino coinciden con los años sin flujo.

En suma, **los pasos 1 (comercio por etapa) y 3 (destinos) son consistentes**: la etapa dice *si* hay flujo y de qué tipo; el destino dice *a dónde*. La falta parcial de destinos se lee junto a la etapa, no como error.

## 3bis. Ghosh por estado con la MIP estatal 2018 (Paso 8 numérico)

La co-localización de la sección 2 (descriptiva) se **cuantifica** con la **MIP Multi-Estatal 2018 de INEGI** (publicada abr-2024; matrices industria×industria intra-estatales, 35 industrias, 32 entidades). Para el sector **21-2 minería no petrolera** de cada estado se computa el **encadenamiento hacia adelante de Ghosh** (Rasmussen, media estado = 1) y una **«fuga»** = fracción del producto minero del estado que sale como exportación (a otros estados + al extranjero), leída directamente de las columnas de demanda final de la matriz. Script `10 Datos/scripts/ghosh_estatal.py` → `processed/ghosh_estatal_mineria.csv`; gráfica `ghosh_estatal.png`.

**Tabla — minería por estado (2018), estados con minería relevante (VBP > 5,000 mdp):**

| Estado | Minería (% de su economía) | Ghosh fwd (media=1) | **Fuga** (exporta en bruto) | Lectura |
|---|---:|---:|---:|---|
| **Coahuila** | 2.0 % | 1.61 | **32 %** | integra (siderurgia local) |
| **Sonora** | 9.6 % | 1.41 | **39 %** | integra (fundición de cobre local) |
| **San Luis Potosí** | 1.8 % | 1.40 | 53 % | integra parcialmente (metalurgia) |
| Aguascalientes | 1.5 % | 1.21 | 70 % | intermedio |
| **Durango** | 7.0 % | 1.03 | **77 %** | **enclave** (concentrado sale) |
| **Zacatecas** | **10.2 %** | 1.04 | **84 %** | **enclave** (el estado más minero, casi todo en bruto) |
| Chihuahua | 1.3 % | 0.96 | 89 % | enclave |
| Guerrero | 2.5 % | 1.05 | 87 % | enclave |
| Nuevo León | 0.3 % | 0.88 | 95 % | enclave (minería marginal) |

> [!important] El enclave, medido por estado
> Solo **tres estados retienen su mineral**: Coahuila, Sonora y San Luis Potosí —los únicos con **fundición/metalurgia co-localizada** (el mine→smelter de cobre en Sonora, la siderurgia de Coahuila, la fundición de plomo-plata en SLP)—. En el otro extremo, los **dos estados más mineros del país** (Zacatecas, con la minería en 10.2 % de su economía, y Durango) **fugan 84 % y 77 %** de su producto minero como concentrado a reprocesar fuera del estado: extracción intensa, cadena local ausente. Es el **enclave estructural en su dimensión territorial**, ahora con el dato insumo-producto y no solo con la georreferenciación. **Caveat**: 35 industrias (minería agregada, no por mineral) y versión **intra-estatal** —la fracción «fuga» que va a otros estados (p. ej. concentrado de Zacatecas → fundición de Torreón, Coahuila) es encadenamiento nacional, no pérdida de valor del país; separarla requiere la MIP birregional/multiestatal del mismo paquete (pendiente)—.

## 3ter. Ghosh inter-estatal (MIP birregional 2018): separar cadena nacional de fuga real

La versión intra-estatal (§3bis) no distingue si el mineral que «sale» del estado va a **otro estado de México** (encadenamiento nacional) o **al extranjero** (fuga real). La **MIP birregional 2018** (entidad + «resto del país», 2×35 industrias; flujos inter-estatales endógenos) permite descomponer el producto minero de cada estado en cuatro destinos. Script `ghosh_interestatal.py` → `processed/ghosh_interestatal_mineria.csv`; gráfica `ghosh_interestatal.png`.

**Tabla — destino del producto minero por estado (2018), % del VBP minero:**

| Estado | Propio estado | Otros estados (cadena nacional) | Demanda final | **Al extranjero (fuga real)** | Ghosh fwd birregional |
|---|---:|---:|---:|---:|---:|
| **Chihuahua** | 10 % | 12 % | 2 % | **76 %** | 0.92 |
| **Guerrero** | 13 % | 26 % | 3 % | **59 %** | 1.08 |
| **Zacatecas** | 12 % | 30 % | 6 % | **53 %** | 1.07 |
| Baja California Sur | 22 % | 44 % | 5 % | 30 % | 1.32 |
| **Durango** | 20 % | **46 %** | 5 % | 29 % | 1.30 |
| **Sonora** | **56 %** | 14 % | 6 % | 24 % | 1.39 |
| Coahuila | 68 % | 25 % | 3 % | 4 % | 1.59 |
| **San Luis Potosí** | 47 % | **48 %** | 4 % | 1 % | 1.65 |
| Nuevo León | 5 % | 91 % | 3 % | 0 % | 1.62 |

> [!important] Reencuadre: buena parte del «enclave regional» es cadena nacional
> La fuga intra-estatal (§3bis) **exageraba** el enclave: al abrir el destino, gran parte del mineral que sale de un estado **alimenta la industria de otro estado de México** (concentrado → fundición), no se pierde al extranjero. Casos claros: **Durango** manda 46 % a otros estados (y solo 29 % al extranjero); **San Luis Potosí**, 48 % a otros estados y **1 %** afuera; **Nuevo León**, 91 % nacional. El **enclave verdadero —el mineral que sale del país en bruto—** se concentra en **Chihuahua (76 %), Guerrero (59 %) y Zacatecas (53 %)**. Sonora retiene más que ningún otro dentro de su propio estado (56 %, su fundición de cobre) y exporta 24 % en bruto. Es decir: existe una **cadena metalúrgica nacional inter-estatal** (los estados extractivos surten a los estados con fundición: Coahuila, San Luis, Nuevo León), y el enclave se localiza en unos pocos estados y —sobre todo— en el **eslabón del metal** (la exportación en bruto que el análisis nacional ya mostraba). **Caveat**: 35 industrias, minería agregada; «resto del país» agregado (no dice a qué estado va; el detalle estado-a-estado requiere la MIP multiestatal completa 1120×1120).

## 4. Enlace con la tesis
- Refuerza **H3** (inserción en eslabones primarios): el concentrado de cobre a China (94.7 %) es la imagen más nítida del enclave.
- Complementa el **Objetivo 2** (cadena local): los nodos de transformación existentes y su localización, ahora con el **Ghosh por estado** (§3bis) que cuantifica dónde la cadena se queda y dónde se fuga.
- Insumo para **bases de política** (Cap. VIII): dónde estarían los eslabones ausentes y en qué territorio; el contraste Sonora/Coahuila (integran) vs Zacatecas/Durango (fugan) señala el tipo de intervención regional.

← [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] · [[Memoria - Comercio por etapa de procesamiento (Obj 3)]] · [[Catalogo de Bases de Datos]]
