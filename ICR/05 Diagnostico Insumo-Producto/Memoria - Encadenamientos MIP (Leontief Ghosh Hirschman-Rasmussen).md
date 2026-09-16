---
title: Memoria — Encadenamientos productivos por mineral (MIP INEGI)
type: resultados
tags: [icr, insumo-producto, encadenamientos, ghosh, leontief, datos]
created: 2026-07-30
updated: 2026-09-05
status: activo
---

# Memoria — Encadenamientos productivos por mineral (MIP INEGI)

> [!note] Diseño descriptivo (cadenas de valor)
> Los índices de esta memoria son **descriptores** del lugar de cada mineral en la estructura productiva, no variables de un modelo causal. El aporte es **construir el indicador desagregado por mineral** —que no existía— y usarlo para describir. Ver [[Columna Vertebral Metodologica]].

Insumo del **Objetivo 1** (estructura extractiva + encadenamientos) y del **Objetivo 2** (¿hay industria compradora doméstica?).

## 1. Fuente y cobertura
- **MIP INEGI, matriz simétrica producto×producto, nivel Clase SCIAN (6 dígitos)**, cortes **2013** (base 2013) y **2018** (base 2018). Datos abiertos CSV en `10 Datos/Bases Originales/10 MIP INEGI/`.
- Serie comparable = **solo 2013 y 2018** (mismos datos abiertos CSV, bases contiguas). El corte **2008** se incorpora **aparte, como referencia histórica no encadenada** (ver §8); **2003** (solo Sector/Subsector) y **2012** (actualización que solo llega a Rama, minería agregada) quedan **fuera por mineral**.
- Base **doméstica** (`d_pb`): mide encadenamientos con la producción de origen nacional, coherente con la pregunta descriptiva sobre la cadena local. Denominador de coeficientes = producción total (VBP, `UTPB` de la tabla total).

## 2. Correspondencia mineral ↔ clase SCIAN
8 de los 10 minerales tienen clase propia; **plomo y zinc comparten una sola clase (coextracción)** y se reportan combinados como `plomo-zinc`.

| Mineral | Clase | | Mineral | Clase |
|---|---|---|---|---|
| oro | 212221 | | barita | 212393 |
| plata | 212222 | | fluorita | 212395 |
| cobre | 212231 | | grafito | 212396 |
| plomo-zinc | 212232 | | sílice | 212324 |
| manganeso | 212291 | | | |

## 3. Método
Con la matriz de flujos domésticos `Z` y la producción total `x`:
- **Coeficientes técnicos** (Leontief, hacia atrás): `A = Z · diag(x)⁻¹`; matriz inversa `L = (I − A)⁻¹`.
- **Coeficientes de distribución** (Ghosh, hacia adelante): `B = diag(x)⁻¹ · Z`; matriz inversa `G = (I − B)⁻¹`.
- **Encadenamiento hacia atrás** (poder de dispersión) = suma de columna de `L`; **hacia adelante** (sensibilidad de dispersión) = suma de fila de `G`.
- **Índices Hirschman-Rasmussen normalizados**: cada suma dividida entre la media nacional del año → **>1 = por encima del promedio de la economía**, <1 = por debajo. Comparables dentro de cada año y, como medida relativa, entre años.

> [!check] Validación
> `A` reproduce el archivo `ctec` de INEGI y `L` reproduce el `cdi` (inversa de Leontief) **a precisión de máquina**: max |A − ctec| = 1.7e-18 (2013) / 8.9e-16 (2018); max |L − cdi| = 4.2e-15 / 5.3e-15. Ghosh se construye con la misma `Z` y `x` validadas. Script: `10 Datos/scripts/mip_calc.py`.

## 4. Resultados — encadenamientos por mineral
Base: `10 Datos/processed/mip_encadenamientos_minerales.csv`. `back`/`fwd` = índices Hirschman-Rasmussen normalizados (media nacional = 1). DI/VBP = fracción de la producción que va a demanda intermedia doméstica.

**2018** (834 clases)

| Mineral | VBP (MM$) | DI/VBP | Atrás | Adelante | Lectura |
|---|--:|--:|--:|--:|---|
| sílice | 6,959 | 0.99 | 0.94 | **1.92** | fuerte hacia adelante |
| grafito | 720 | 0.88 | 0.87 | **1.71** | fuerte hacia adelante |
| manganeso | 635 | 0.78 | **1.05** | **1.54** | ambos sobre la media |
| cobre | 92,893 | 0.53 | 0.94 | **1.34** | hacia adelante alto |
| fluorita | 5,862 | 0.50 | **0.97** | **1.31** | hacia adelante alto |
| oro | 69,491 | 0.96 | **1.03** | **1.22** | ambos ≈media |
| plata | 49,784 | 0.89 | 0.99 | **1.18** | hacia adelante moderado |
| plomo-zinc | 34,725 | 0.14 | 0.99 | 0.71 | **bajo hacia adelante** |
| barita | 686 | 0.03 | 0.96 | 0.64 | **casi sin transformación local** |

**2013** (822 clases) — misma tendencia; diferencias notables: barita DI/VBP 0.18 (vs 0.03 en 2018) y fluorita hacia adelante 0.87 (vs 1.31). Serie completa en el CSV.

**Patrón general.** Los minerales críticos mexicanos tienen encadenamiento **hacia atrás bajo** (extracción intensiva en recursos, pocos insumos industriales) y encadenamiento **hacia adelante** heterogéneo: alto en los que alimentan una industria transformadora doméstica (sílice→vidrio, grafito→acero, manganeso→química), bajo en los que se exportan en bruto (barita, plomo-zinc).

## 4bis. Cómo leer el índice de Ghosh: por qué un valor >1 debe tomarse con cautela

Es tentador leer un índice de Ghosh mayor que 1 como evidencia de que el mineral tiene una cadena de valor local desarrollada. **No lo es**, y esta distinción es central para el diseño descriptivo de la investigación. El índice normalizado de encadenamiento hacia adelante (media de la fila del mineral en la inversa de Ghosh $G=(I-B)^{-1}$, dividida entre la media general de la matriz) mide **cuánto se conecta la producción del sector con los sectores que están aguas abajo en la estructura insumo-producto doméstica, en relación con el promedio de la economía**. Un valor >1 indica un "arrastre" estructural superior al del sector típico. Eso es una propiedad de la estructura de transacciones observada en el año de la matriz —un *potencial* de conexión aguas abajo—, no una medida de desarrollo de cadena ni de captura de valor. Cinco razones lo justifican:

1. **Refleja la amplitud de las industrias usuarias, no el valor que México retiene.** La sílice tiene el índice hacia adelante más alto (1.92 en 2018) porque vidrio, cemento, cerámica y construcción usan arena sílica ampliamente. Eso dice que la economía doméstica *consume* sílice en muchos sectores, no que el país capture valor: de hecho la sílice pertenece al tipo "usuario con eslabón importado" —el insumo procesado de mayor valor (silicio metálico, ferrosilicio) se **importa**—.

2. **Un índice alto puede ser un solo eslabón, no una cadena.** Oro (1.22) y plata (1.17) tienen índices por encima de 1 porque casi toda su producción va a un único destino —*fundición y refinación de metales preciosos* (≈99 %)— y de ahí se exporta. El encadenamiento estructural alto convive con una cadena **truncada** en el metal refinado. La "fundición y refinación" es un eslabón, no una cadena manufacturera aguas abajo.

3. **No distingue el insumo de origen nacional del importado.** Un mineral puede tener un Ghosh doméstico alto y, a la vez, alimentar una industria usuaria que corre con insumo **procesado importado**. Es el caso de grafito (1.71) y sílice: existe industria usuaria nacional (siderurgia, vidrio), pero los electrodos de grafito y el silicio se importan. El índice de la matriz doméstica no captura esa fuga.

4. **Es sensible a la clasificación y al año base.** El manganeso pasa de 1.00 en el corte de referencia 2008 a 1.79 en 2013, en parte porque en 2008 su clase agrupa actividades vecinas más amplias (ver §8). El nivel del índice depende de cómo esté definida la clase y de la añada de la matriz, no solo del "desarrollo" real.

5. **Descansa en supuestos del modelo.** El modelo de Ghosh supone coeficientes de distribución fijos; su interpretación más defendible es como modelo de precios (Dietzenbacher, 1997), no como predicción de cantidades. Aquí se emplea como **descriptor** de posición estructural, no como mecanismo causal.

> [!important] Cómo se usa entonces
> El índice de Ghosh es una condición **necesaria pero no suficiente** para hablar de cadena local: señala dónde *existen* conexiones aguas abajo en la estructura doméstica, pero no si México captura valor ni si la cadena se detiene pronto. Por eso en esta investigación **nunca se lee solo**: se cruza con el **CCV** (¿se exporta en bruto o se capta valor?), el **comercio por etapa** (¿se exporta crudo e importa procesado? patrón espejo) y el **mapa de empresas de transformación** (¿la industria existe y se alimenta de producción nacional?). El enclave estructural aparece en la **combinación** de los cuatro indicadores, no en el Ghosh aislado —y de hecho la co-ocurrencia entre alta concentración (HHI) y bajo encadenamiento hacia adelante que anticipaba H1 **no se observa**: varios minerales muy concentrados (manganeso, fluorita, grafito, sílice) tienen índices de Ghosh altos, lo que confirma que el índice mide arrastre estructural, no truncamiento de la cadena—. Esta lectura conjunta es la que sustenta la tipología A/B/C/D del Cap. VI.

## 5. ¿Quién compra cada mineral? (demanda intermedia doméstica, Obj. 2)
Base: `10 Datos/processed/mip_demanda_intermedia_minerales.csv` (top compradores por mineral/año). Estructura 2018:

- **Metales preciosos y cobre** → **un solo eslabón: fundición y refinación**. Oro 99.5 % y plata 99.0 % a *Fundición y refinación de metales preciosos*; cobre 93.5 % a *Fundición y refinación de cobre*; plomo-zinc 79.5 % a *Fundición y refinación de otros metales no ferrosos* (+5 % a acumuladores/pilas). La cadena doméstica **llega hasta el metal refinado** y, salvo plomo-zinc, no continúa aguas abajo.
- **Fluorita** → 82 % a *cemento* y 13 % a *otros productos minerales no metálicos* en la MIP (grado metalúrgico / metspar). ⚠️ **Corrección (Tarea 3, 2026-08-01):** la cadena fluoroquímica **sí existe** en México —Koura/Orbia opera en Matamoros la planta de **ácido fluorhídrico (HF) más grande del mundo**, integrada con la mina Las Cuevas—; el 82 % a cemento refleja el metspar y que la transferencia mina→HF es **intra-firma** (no captada a nivel de sector en la MIP). La cadena local llega al **HF** (escala mundial; México exportó ~161 MM USD de HF en 2018) pero **se detiene antes de los fluoropolímeros** de mayor valor (PTFE), que se importan (~30–40 MM USD/año). Ver [[Memoria - Comercio por etapa de procesamiento (Obj 3)]].
- **Grafito** → siderurgia y fundición (ferroaleaciones 43 %, complejos siderúrgicos 32 %, moldeo de hierro/acero 14 %): eslabón industrial real (refractarios/electrodos/recarburación).
- **Sílice** → **vidrio** (envases 43 %) y **construcción** (cemento 39 %, azulejos): cadena doméstica amplia.
- **Manganeso** → uso **disperso** (farmacéutica, alimentos para animales, ladrillos, química inorgánica, fertilizantes, pilas): sensibilidad de dispersión alta.
- **Barita** → **perforación de pozos petroleros** (58 %) y partes de frenos (15 %): insumo de servicios petroleros, no de una cadena manufacturera; y solo ~3 % de la producción se transforma en el país (el resto se exporta).

## 6. Cuidados y límites (declarados)
- **Plomo-zinc combinado**: la MIP no los separa (coextracción); el HHI sí los distingue. Los indicadores de encadenamiento son conjuntos para ambos.
- **Años base distintos** (2013 y 2018): los **niveles** de VBP no son deflactados; los **índices normalizados** (relativos a la media nacional de cada año) sí son comparables como posición relativa.
- **"Fundición y refinación" es un eslabón, no una cadena**: un DI/VBP alto en metales indica smelting doméstico, no necesariamente manufactura aguas abajo. Distinción central para el Obj. 2.
- **Ghosh y supuestos**: el modelo de Ghosh supone coeficientes de distribución fijos; se usa como **descriptor** de posición, no como predicción.

## 7. Pendiente (no bloquea el Cap. V descriptivo)
- CCV (coeficiente de captura de valor) — vía comercio por etapa (Tarea 2), no MIP.
- Actualización RAS a 2020/2023 y comparación internacional Chile/Australia — **opcionales** en el diseño descriptivo.

## 8. Corte de referencia 2008 (no encadenado)

> [!warning] Referencia histórica, no serie comparable
> La **MIP 2008** (base 2008 / **SCIAN 2007**, tabulados en Excel) se incorpora como **tercer punto de referencia** para dar profundidad temporal descriptiva (**2008 → 2013 → 2018**), **no** como serie comparable. Los movimientos 2008→2013 mezclan cambio real con cambio de año base y de añada de clasificación. Se lee como **punto ilustrativo con caveats**, apoyándose en el **patrón/orden**, no en el nivel exacto. Base **doméstica**, nivel **Clase** (814 clases). Archivo **separado**: `10 Datos/processed/mip_encadenamientos_2008_referencia.csv`.

> [!check] Validación 2008 (a precisión de máquina)
> Extracción de los `.XLSX` `_4` domésticos con ubicación dinámica de encabezados (`mip2008_extract.py`). (1) `(I − A_inegi)⁻¹` reproduce el `cdi` de INEGI: **max |L − (I−A)⁻¹| = 4.9e-15**; (2) `Z_dom / x` reproduce el `ctec` (A) de INEGI: **max |A − Z/x| = 1.6e-15**. La extracción es correcta. Ghosh se construye con la misma `Z`/`x` validadas. Script de cálculo: `mip2008_calc.py`.

**Encadenamientos 2008** (814 clases; `back`/`fwd` = Hirschman-Rasmussen normalizado, media nacional = 1)

| Mineral | VBP (MM$ 2008) | DI/VBP | Atrás | Adelante | G crudo (Σfila) |
|---|--:|--:|--:|--:|--:|
| grafito | 404 | 0.91 | 0.97 | **1.69** | 2.60 |
| cobre | 12,361 | 0.74 | 0.84 | **1.63** | 2.51 |
| sílice | 1,217 | 0.81 | 0.90 | **1.60** | 2.47 |
| oro | 12,804 | 0.98 | 0.95 | **1.48** | 2.29 |
| plomo-zinc | 7,930 | 0.79 | 0.98 | **1.35** | 2.09 |
| barita | 270 | 0.90 | 0.96 | **1.29** | 1.99 |
| fluorita | 1,286 | 0.36 | **0.98** | **1.11** | 1.72 |
| manganeso ⚠️ | 8,105 | 0.27 | 0.86 | 1.00 | 1.55 |
| plata | 19,037 | 0.18 | 0.94 | 0.80 | 1.23 |

**Lectura (patrón, no nivel).** El orden hacia adelante 2008 es coherente con el de 2013/2018 en la parte alta (grafito, sílice, cobre, oro por encima de la media) y en la baja (plata, y en 2008 también fluorita más moderada). Los **compradores domésticos** replican la misma estructura de eslabón único que en 2018 (`mip_demanda_intermedia_2008_referencia.csv`): metales preciosos y plomo-zinc → *fundición y refinación* + *laminación secundaria*; cobre → *fundición y refinación de cobre* (74%); grafito → *siderurgia/ferroaleaciones y refractarios*; sílice → *vidrio* (envases 64%); barita → *perforación de pozos petroleros* (89%); fluorita → *química básica* (80%); manganeso → *química básica* (55%) + *ferroaleaciones* (43%).

> [!caution] Caveats obligatorios del corte 2008
> - **Año base 2008 / precios de 2008**: los **niveles de VBP no son comparables** con 2013/2018 (sin deflactar, base distinta); los **coeficientes** (ratios) son más robustos, pero aun así de una añada SCIAN previa.
> - **Índices Rasmussen normalizados**: su nivel **no es estrictamente comparable entre añadas** (la normalización usa el promedio de una economía cuya clasificación y tamaño cambian). Por eso se reporta también el **Ghosh crudo (suma de fila)** y **DI/VBP**, y la lectura se apoya en el **patrón/orden**.
> - **Manganeso (212291) ⚠️**: en 2008 la clase es **más amplia** (agrega 212292 mercurio/antimonio y 212299 otros metálicos), lo que **infla su VBP** (8,105 MM$, muy por encima de 2013/2018) y **contamina** su encadenamiento hacia adelante (1.00 vs 1.79 en 2013). **No comparable** ni en nivel ni en posición. En 2018 esas clases van aparte.
> - **Plomo-zinc** sigue combinado (coextracción), como en la serie comparable.

← [[Indice Diagnostico Insumo-Producto]] · [[Columna Vertebral Metodologica]] · [[Catalogo de Bases de Datos]]
