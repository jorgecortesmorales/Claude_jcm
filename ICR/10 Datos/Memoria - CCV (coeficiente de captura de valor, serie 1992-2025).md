---
title: "Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)"
type: memoria
tags: [icr, datos, ccv, cadenas-de-valor, encadenamiento-adelante, comtrade, usgs, obj3]
created: 2026-09-05
updated: 2026-09-05
status: hecho
---

# Memoria — CCV (coeficiente de captura de valor), serie anual mineral-año 1992-2025

> [!abstract] Qué es
> El **CCV** es la segunda operacionalización del **encadenamiento hacia adelante** del diseño descriptivo. Mientras el índice de **Ghosh** es discreto (atado a los cortes de la MIP 2013 y 2018), el CCV es una **serie continua** que mide, año con año, qué fracción del valor del producto de referencia capta México cuando exporta el mineral en su **forma bruta** (mena/concentrado o mineral crudo). Un CCV bajo y persistente es el descriptor de serie del **enclave estructural**: se exporta el recurso sin captar el valor del eslabón procesado. Ver [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] y [[Memoria - Comercio por etapa de procesamiento (Obj 3)]].

## 1. Definición y fórmula

Para cada mineral *m* y año *t*:

$$\text{CCV}_{m,t}=\frac{VU^{X,E1}_{m,t}}{P^{USGS}_{m,t}}$$

- **Numerador — valor unitario de exportación en frontera (forma bruta, E1):**
  $$VU^{X,E1}_{m,t}=\frac{\sum_{h\in E1_m}\text{valor}^{X}_{h,t}}{\sum_{h\in E1_m}\text{peso}_{h,t}}\quad[\text{USD/t}]$$
  con valor y peso neto de las fracciones **E1** de exportación de México (reporter 484, socio Mundo, flujo X) de **UN Comtrade**. El peso es `netWgt` (kg); respaldo `qty` cuando la unidad reportada es kg (código 8). Solo se agregan las fracciones E1 que tienen peso ese año (evita sesgar al alza el valor unitario).
- **Denominador — precio del producto de referencia USGS:** `precio_usd_t_nominal` de `precios_usgs_anual_empalmado.csv` (USGS DS-140 valor unitario de consumo aparente 1990-2020, empalmado con MCS / Cochilco 2021-2025), por mineral-año.

Correspondencia mineral ↔ HS(E1) ↔ producto de referencia: `concordancia_hs_etapa.csv`.

Ambos términos están en USD/t nominales, de modo que el CCV es un **cociente adimensional**. Lectura: CCV → 1 significa que la forma exportada en bruto ya vale casi como el producto de referencia; CCV → 0 significa que la exportación bruta capta poco de ese valor (mayor distancia al eslabón procesado).

## 2. Insumos y cobertura

- **Numerador:** `10 Datos/Bases Originales/11 Comercio Comtrade/comercio_e1_valor_peso_comtrade_mx_1992_2025.csv` (413 filas E1, valor + peso, 1992-2025). Descargado con `10 Datos/scripts/ccv_download.py` (API pública `preview`, sin clave; `motCode=0` como total; throttling ~1/req y reintento en 429). Se re-descargó **toda** la serie —no solo 1992-2014— porque el archivo previo `comercio_hs_comtrade_mx_2015_2024.csv` solo guardaba valor, sin peso.
- **Denominador:** `10 Datos/processed/precios_usgs_anual_empalmado.csv`.
- **Respaldo del numerador por ESPEJO (paso 1 de la ruta, 2026-09-06):** todos los huecos del CCV (excl. oro/plata) eran por **numerador** (México no reportó `netWgt`, o no reportó la exportación E1), no por precio. Se recuperó el valor unitario con **datos espejo** —lo que los socios reportan **importar desde México** (flujo M, socio 484), que sí traen peso— vía `scripts/ccv_fill_gaps.py` → `Bases Originales/11 Comercio Comtrade/comercio_e1_espejo_huecos.csv`. `ccv_calc.py` lo usa como respaldo y marca la celda con `fuente_numerador='espejo'`. **Caveat:** el espejo es **CIF** (incluye flete/seguro) y puede **sobreestimar** el valor unitario frente al FOB propio; los años rellenados se leen con esa reserva.
- **Salida:** `10 Datos/processed/ccv_serie.csv` (340 filas = 10 minerales × 34 años). Columnas: `mineral, grupo_ccv, anio, hs_e1, valor_export_e1_usd, peso_export_e1_t, valor_unitario_export_usd_t, precio_refinado_usgs_usd_t, ccv, fuente_numerador, nota`.
- **Script de cálculo:** `10 Datos/scripts/ccv_calc.py`. **Validación:** 340 filas, 0 malformadas (`py`+`csv`).

Cobertura de CCV **tras el relleno por espejo (2026-09-06)**: **cobre, zinc, manganeso, fluorita, grafito, barita, silice = 34 años completos (1992-2025)**; **plomo 33** (único hueco: **1994**, sin comercio espejo → **cero estructural, declarado, no imputado**). Celdas rellenadas por espejo: manganeso 11, barita 6, silice 3, grafito 2, cobre 1, plomo 1. Oro/plata siguen sin CCV informativo (artefacto de ley; ver §4). **Hallazgo del espejo:** el manganeso **sí** tiene una pequeña exportación de mineral en bruto (que México no reportaba); su serie CCV queda completa 1992-2025, aunque el grueso del manganeso se transforma en el país (ferroaleaciones).

## 3. Resultados (CCV medio y rango, todos los años con dato)

| Mineral | Grupo | CCV medio | Mín | Máx | Lectura |
|---|---|---:|---:|---:|---|
| **Cobre** | metal base | **0.224** | 0.125 | 0.364 | Estable ~0.20-0.30 en 33 años: el concentrado capta ~22% del cobre refinado en frontera. |
| **Zinc** | metal base | **0.296** | 0.180 | 0.444 | Estable ~0.30: concentrado de zinc vs. zinc refinado. |
| Plomo | metal base | 1.051 | 0.069 | 2.690 | Volátil, a veces >1 → **créditos de plata/oro** en el concentrado argentífero inflan el valor/t (rompe la lectura de captura). |
| Oro | metal precioso | 0.000 | 0.000 | 0.000 | **Artefacto de ley**: mena en bruto (t brutas) ÷ oro puro/t ≈ 0; no informativo. |
| Plata | metal precioso | 0.301 | 0.000 | 1.355 | Igual artefacto (mena/concentrado vs. plata pura); ruidoso, no interpretable como captura. |
| Barita | no metálico | 1.589 | 0.662 | 4.404 | ~1 o >1: la barita exportada (grado perforación) supera el valor unitario de consumo aparente USGS → prima de frontera. |
| Fluorita | no metálico | 0.851 | 0.471 | 1.704 | ~1: espato flúor exportado vs. fluorita grado ácido importada (referencia). |
| Grafito | no metálico | 0.465 | 0.216 | 2.876 | Ruidoso: grafito natural vs. referencia flake importada. |
| Sílice | no metálico | 1.976 | 0.157 | 14.380 | Muy ruidoso: arena/cuarzo exportado vs. valor de producción USGS (mezcla de grados). |
| Manganeso | no metálico | 0.222 | 0.111 | 0.524 | Solo 1992-2014; mena de Mn vs. referencia. |

## 4. Interpretación por grupo — dónde el CCV es informativo (caveat central)

El CCV es fiel al diseño del protocolo, pero su **poder descriptivo depende del grupo mineral**, porque numerador (forma bruta exportada) y denominador (referencia USGS) no siempre son "el mismo producto una etapa más arriba":

1. **Metales base — cobre y zinc: el CCV funciona como descriptor de captura de valor.** El concentrado y el metal refinado son productos distintos y la brecha (CCV ≈ 0.2-0.3) refleja ley del concentrado + cargos de tratamiento/refinación no captados. Es el **hallazgo fuerte**: cobre exporta con un CCV estable en ~0.22 durante tres décadas, coherente con el enclave estructural (se exporta concentrado, no cátodo).
2. **Plomo: contaminado por co-productos.** El concentrado de plomo mexicano es **argentífero**; su valor/t incorpora créditos de plata/oro, por lo que el CCV sube por encima de 1 en varios años. Se reporta la serie pero **no** se lee como "captura" pura.
3. **Metales preciosos — oro y plata: CCV no informativo (artefacto de ley).** La fracción E1 es mena/concentrado en toneladas brutas; el denominador es metal puro por tonelada. El cociente ≈ 0 sólo mide dilución de ley, no captura de valor. Para oro/plata el encadenamiento hacia adelante se describe mejor con la **participación E1 vs. E2/E4** del comercio por etapa (doré y joyería), no con el CCV.
4. **No metálicos — barita, fluorita, grafito, sílice, manganeso: el CCV mide prima/descuento de frontera.** Aquí la referencia USGS es un producto **cercano** a la forma exportada, así que el CCV oscila alrededor de 1 y capta diferencias de grado/mercado más que un salto de eslabón. Útil como descriptor relativo, con ruido (sílice es el caso extremo).

**Recomendación de uso en la tesis:** presentar el CCV como serie continua principalmente para **cobre y zinc** (y plomo con la nota de créditos), donde mide lo que el concepto pide; para oro/plata remitir al comercio por etapa; para no metálicos usarlo como descriptor de prima de frontera. Así el CCV **complementa** al Ghosh (discreto, 2013/2018) sin sobre-interpretarlo.

## 5. Límites y cuidados

- **Unidad de peso y relleno por espejo:** cuando México no reporta `netWgt`, el hueco se rellena con el valor unitario **espejo** (importaciones de socios desde México), marcado `fuente_numerador='espejo'`. Es **CIF** → posible sesgo al alza; leer esos años con reserva y, para lecturas de nivel fino, preferir los años `propio`. **Hueco no rellenable:** plomo **1994** (sin comercio espejo) → se declara, no se imputa.
- **Doble vintage 2019:** filas idénticas deduplicadas por (año, HS) prefiriendo la que trae peso.
- **Denominador empalmado:** 1990-2020 USGS DS-140; 2021-2025 empalme (Cochilco/MCS) documentado en la propia serie de precios — implica un pequeño quiebre de fuente al final, ya declarado en [[Memoria Metodologica de Bases de Datos]].
- **Convención CAMIMEX/USGS** ya incorporada en los precios (Informe año N = dato N−1; sin Tabla 2 USGS 2017/2020) — ver [[Memoria Metodologica de Bases de Datos]].

← [[Home]] · [[Mapa del Proyecto]] · [[Columna Vertebral Metodologica]] · [[Catalogo de Bases de Datos]]
