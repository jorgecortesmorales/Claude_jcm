---
title: Definición de Series USGS (PrecioIntl armonizado)
type: datos
tags: [icr, datos, usgs, precios]
created: 2026-07-17
status: construida-completa
updated: 2026-07-17
---

> [!success] SERIE COMPLETA — `processed/precios_usgs_anual_empalmado.csv`
> **Panel completo: 10 minerales × 33 años (1993-2025) = 330 observaciones, sin huecos ni duplicados**, nominal y constantes 1998, con método/fuente/factor documentados por fila. Construida el 2026-07-17: base DS-140 + empalme por encadenamiento de razón (ratio splicing) para los años recientes. QA: continuidad verificada en todas las junturas; transiciones consistentes con movimientos de mercado documentados (cobre +51% 2021, plata -14% 2022, zinc -24% 2023). Ver sección "Empalme" abajo y el protocolo de spot-check.

# Definición de series USGS para PrecioIntl armonizado (10 minerales)

**Fuente**: USGS *Historical Statistics for Mineral and Material Commodities in the United States* (Data Series 140), National Minerals Information Center. Un archivo XLSX por commodity.

**Definición única para los 10 minerales** (esta es la ventaja de armonización): *valor unitario del consumo aparente en EE.UU., en USD por tonelada métrica*, disponible en versión **nominal** y en **dólares constantes de 1998** (deflactor: CPI-U). Cobertura desde ~1900. Los años recientes no cubiertos por DS-140 se empalman desde los *Mineral Commodity Summaries* (ediciones 2021-2025), validando coincidencia en los años de traslape.

## Series construidas — cobertura real verificada

| Mineral | Archivo descargado | Último año con dato | Años a empalmar desde MCS |
|---|---|---|---|
| Barita | ds140-barite-2021.xlsx | 2019 (2020-21 = W) | 2020-2024 |
| Cobre | ds140-copper-2020.xlsx | 2020 | 2021-2024 |
| Fluorita | ds140-fluorspar-2020.xlsx | ⚠️ **2006** (2007+ = W) | **2007-2024 (17 años)** |
| Grafito (natural) | ds140-graphite-2022.xlsx | 2022 | 2023-2024 |
| Manganeso | ds140-manganese-2022.xlsx | 2022 | 2023-2024 |
| Oro | ds140-gold-2022.xlsx | 2022 | 2023-2024 |
| Plata | ds140-silver-2021.xlsx | 2021 | 2022-2024 |
| Plomo | ds140-lead-2021.xlsx | 2021 | 2022-2024 |
| Sílice | ds140-sand-industrial-2022.xlsx | 2022 | 2023-2024 |
| Zinc | ds140-zinc-2022.xlsx | 2022 | 2023-2024 |

Notas: (1) la correspondencia sílice → "Industrial sand and gravel" es la categoría USGS que cubre arena sílica; documentar en el Cap. VI. (2) **Caso fluorita**: EE.UU. dejó de reportar el valor unitario de consumo aparente desde 2007 (confidencialidad, "W") — para 2007-2024 la serie de empalme natural es el *valor unitario de las importaciones estadounidenses de fluorita grado ácido* que publican los MCS/Minerals Yearbook; es un cambio de definición que debe declararse en el Cap. VI (sigue siendo externo al mercado mexicano, y EE.UU. absorbe ~70% de la exportación mexicana de fluorita, lo que lo hace incluso más pertinente como precio de destino).

## Decisiones propuestas (pendientes de validación del usuario)

1. **Serie primaria de PrecioIntl para el panel: DS-140 valor unitario para los 10 minerales** — una sola fuente, definición y unidad (USD/t) para todo el panel; evita mezclar cotizaciones de bolsa (5 metales) con valores unitarios (5 no metálicos), que introduciría heterogeneidad de definición entre unidades del panel.
2. **Robustez: Cochilco** (cotizaciones LME/COMEX/London Fix, mensuales) para los 5 metales — la serie estándar de la literatura; si β₁ sobrevive con ambas, el hallazgo se refuerza.
3. **Nominal como principal** — los efectos fijos de año (γₜ) absorben la inflación común; consistente con Cochilco nominal. La columna en dólares de 1998 queda disponible para robustez.

## Caveat de exogeneidad a declarar en el Cap. VI
El valor unitario DS-140 refleja el mercado de EE.UU. (consumo aparente), no una "cotización mundial" — pero es **externo a la estructura de mercado mexicana**, que es lo que exige la identificación (a diferencia del precio implícito nacional, descartado en [[Variables y Datos]]). EE.UU. es además el principal destino de exportación de la mayoría del corpus, lo que hace este valor unitario especialmente pertinente como referencia de precio de destino.

## Empalme (construido 2026-07-17)

**Método**: encadenamiento de razón (ratio splicing) — estándar para series con cambio de fuente. `valor(t) = serie_fuente(t) × factor`, donde `factor = DS-140(año_ancla) / serie_fuente(año_ancla)`. Conserva el nivel DS-140 y adopta las tasas de crecimiento de la serie fuente. El factor y la fuente van registrados en cada fila del CSV.

| Mineral | Años empalmados | Serie fuente del crecimiento | Año ancla | Factor |
|---|---|---|---|---|
| Oro | 2023-2025 | Cochilco London Fix AM anual; 2025: MCS 2026 (3,300 USD/ozt e) | 2022 | 32,139.2 (≈ conversión troy exacta 32,150.7 ✓) |
| Plata | 2022-2025 | Cochilco London Fix anual; 2025: MCS 2026 (38 USD/ozt e) | 2021 | 32,226.9 |
| Cobre | 2021-2025 | Cochilco BML anual; 2025: MCS 2026 LME cash (440 ¢/lb e) | 2020 | 22.587 (teórico ¢/lb→USD/t: 22.05) |
| Plomo | 2022-2025 | Cochilco BML anual; 2025: transferencia de crecimiento del precio NA del MCS 2026 (106/108.8) | 2021 | 24.898 |
| Zinc | 2023-2025 | Cochilco BML anual; 2025: MCS 2026 LME cash (130 ¢/lb e) | 2022 | 26.505 |
| Barita | 2020-2025 | MCS 2024/2026, valor unitario molida ex-works | 2019 | 0.6313 |
| Grafito | 2023-2025 | MCS 2026, valor unitario de importaciones flake | 2022 | 1.7417 ⚠️ |
| Manganeso | 2023-2025 | MCS 2026, precio CIF China USD/mtu contenido Mn | 2022 | 335.01 |
| Sílice | 2023-2025 | MCS 2026, valor promedio de producción | 2022 | 0.9978 (≈1: mismo concepto ✓) |
| Fluorita (A) | 2007-2015 | MYB T1: valor/cantidad total de importaciones CIF | 2006 | 1.0023 (≈1 — **DS-140 ES el valor unitario de imports totales** para este mineral 100% importado ✓) |
| Fluorita (B) | 2016-2025 | MCS 2011/2021/2026, valor unitario imports grado ácido CIF | 2006 | 0.9355 |

**Validaciones cruzadas del empalme**: Cochilco anual 2024 vs MCS 2026 → oro 2,387.4 vs 2,388 ✓; plata 28.24 vs 28.37 ✓; cobre LME 414.8 vs 414.7 ✓; zinc 126.00 vs 126.0 ✓ (exactos).

**Flags honestos**:
- ⚠️ **Grafito**: la razón DS-140/flake fue 1.01 en 2021 pero 1.74 en 2022 (el valor DS-140 2022 refleja mezcla con lump/chip, cuyo precio se disparó). El encadenamiento usa 2022 (último traslape, práctica estándar); los 3 años empalmados tienen incertidumbre de nivel elevada. Alternativa documentada: anclar en 2021 daría valores ~42% menores.
- **2025 en general**: valores marcados "e" (estimados) por USGS en el MCS 2026; se revisarán cuando salga el MCS 2027.
- **Constantes 1998 de años empalmados**: deflactadas con CPI-U anual de BLS (verificado que es el deflactor exacto de DS-140: razón nominal/constante de oro 2020 = 163.0/258.811 ✓); el CPI 2025 (322.5) es estimación propia.
- **MYB fluorita**: la nota al pie del MYB 2010 advierte que "value data for fluorspar imports appear to be underreported" — sesgo potencial de nivel en 2007-2015, mitigado por el anclaje.
- Los PDFs y XLS fuente del empalme quedaron en `Bases Originales/07 USGS MCS/` (con sus .txt extraídos) para verificación.

## Spot-check recomendado al usuario (~10 min)
Verificar estos valores transcritos manualmente contra los archivos en `07 USGS MCS/`:
1. `mcs2024-barite.pdf`: precio 2019 = **179** (ancla de barita)
2. `mcs2026-barite.pdf`: precio 2023 = **218**, 2024 = **210**
3. `mcs2026-graphite.pdf`: flake 2022 = **1,200** (ancla), 2023 = **1,080**
4. `mcs2026-manganese.pdf`: 2022 = **5.97** USD/mtu (ancla), 2024 = **5.53**
5. `mcs2026-sand-industrial.pdf`: 2022 = **45.40** (ancla), 2025e = **36**
6. `mcs2011-fluorspar.pdf`: grado ácido 2006 = **217** (ancla B)
7. `myb1-2010-fluor.xls` T1: imports 2006 = **553,000 t / $112,000 miles** (ancla A)
8. `mcs2026-gold/silver/copper/zinc/lead.pdf`: 2025e = **3,300 / 38 / 440 (LME) / 130 (LME) / 106 (NA)**

## Protocolo anti-error (acordado)
1. Validación de estas definiciones por el usuario **antes** de construir. 2. Trazabilidad por fila (fuente/edición/tabla). 3. Flags automáticos: saltos >±50% a-a, coincidencia en años de traslape DS-140↔MCS, correlación direccional vs. precio implícito nacional. 4. Spot-check del usuario en ~12 puntos de mayor riesgo (extremos y empalmes).

← [[Home]] · [[Variables y Datos]] · [[Catalogo de Bases de Datos|Catálogo]] · [[Validacion de Fuentes de Precios|Validación de Fuentes]]
