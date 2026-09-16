---
title: Memoria — Comercio por etapa de procesamiento (Obj. 3, inserción en CVG)
type: resultados
tags: [icr, comercio, cadenas-de-valor, comtrade, datos, obj3]
created: 2026-07-30
updated: 2026-07-30
status: activo
---

# Memoria — Comercio por etapa de procesamiento (Objetivo 3)

> [!note] Diseño descriptivo (cadenas de valor)
> Describe la **posición de México por etapa** en la cadena global de cada mineral (mena → concentrado → refinado → intermedio → bien final) y el patrón **espejo** (exportar en bruto / importar procesado). Es construcción de base de datos e indicador, no modelo causal. Ver [[Columna Vertebral Metodologica]] y, para el lado interno, [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]].

## 1. Fuente y obtención
- **UN Comtrade**, API pública *preview* (sin clave). Reportante **México (484)**, socio **Mundo (0)**, frecuencia anual, clasificación **HS**, flujos exportación (X) e importación (M), **2015–2024**. Se toma la fila `motCode = 0` (todos los modos de transporte) como total.
- No había datos HS locales: solo agregados CAMIMEX por mineral (sin etapa) y un extracto manual de DataMéxico. La descarga HS se guardó en `10 Datos/Bases Originales/11 Comercio Comtrade/comercio_hs_comtrade_mx_2015_2024.csv`.
- Rutinas: `10 Datos/scripts/comercio_etapa.py` (descarga + clasificación) y `comercio_summary.py` (posición/espejo).

## 2. Concordancia mineral × etapa × fracción HS
Es el núcleo del indicador y es **revisable**. Etapas: **E1** mena/concentrado o mineral crudo; **E2** metal en bruto/refinado o mineral procesado/químico; **E3** semimanufactura/intermedio; **E4** manufactura/bien final atribuible al mineral. Tabla completa en `10 Datos/processed/concordancia_hs_etapa.csv`. Resumen:

| Mineral | E1 (crudo) | E2 | E3 | E4 |
|---|---|---|---|---|
| Cobre | 2603 | 7401/7402/7403/7405 | 7407–7413 (semis) | 7415/7418/7419 |
| Plomo | 2607 | 7801 | 7804 | 7806 |
| Zinc | 2608 | 7901 | 7903/7904/7905 | 7907 |
| Manganeso | 2602 | ferroaleac. 720211/19/30 | MnO₂ 282010; metal 8111 | — |
| Oro | 261610 | 7108 (bruto/semilabrado) | — | — |
| Plata | 261690 | 7106 (bruto/semilabrado) | — | — |
| Oro-plata (manuf.) | — | — | — | joyería 7113/7114/7115 |
| Barita | 251110 | químicos Ba 281640/283660 | — | — |
| Fluorita | 252921/252922 | fluoroquímica 281111/282612/282619/390461 | — | — |
| Grafito | 250410/250490 | grafito artificial 3801 | electrodos 8545 | — |
| Sílice | 250510/250610 | silicio/ferrosilicio 280461/69, 720221/29; SiO₂ 281122 | — | — |

**Decisiones declaradas** (debatibles, ajustables): joyería (7113–7115) es multimetal → se reporta como fila propia "oro-plata (manufacturas)", no atribuida a un mineral. Cables eléctricos (8544) y vidrio (7005–7020) se excluyen por multimaterial. Chatarra (74xx/78xx/79xx "waste and scrap") se excluye por no ser producto de la cadena.

## 3. Resultados — posición de México (participación por etapa)
Base: `processed/comercio_por_etapa.csv` (mineral × etapa × flujo × año) y `processed/comercio_posicion_resumen.csv` (totales, participación cruda vs procesada, espejo). Promedio 2018–2023:

| Mineral | X cruda (E1) | X procesada | M procesada | Saldo neto (MM USD) | Lectura |
|---|--:|--:|--:|--:|---|
| Cobre | 68% | 32% | 83% | +199 | **espejo**: exporta mineral, importa semis |
| Plomo | 83% | 17% | 72% | +1,014 | exporta concentrado |
| Zinc | 55% | 45% | 89% | +642 | refina parte (Torreón) |
| Fluorita | 61% | 39% | 100% | +124 | exporta espato **y HF** (Koura); importa fluoropolímeros |
| Sílice | 20% | 80% | 78% | −327 | **importador neto** de silicio/ferrosilicio |
| Grafito | 1% | 99% | 98% | −59 | **importador neto** de electrodos |
| Manganeso | 0% | 100% | 65% | −26 | importador neto de químicos de Mn |
| Oro | 4% | 96% | 100% | +3,318 | exporta oro en bruto (doré) |
| Plata | 3% | 97% | 100% | +2,172 | exporta plata en bruto |
| Oro-plata (joyería) | — | 100% | 100% | −263 | importador neto de joyería |

## 4. Interpretación
- **Patrón espejo (exportar bruto / importar procesado)**, nítido en **cobre, grafito, sílice**: México exporta el eslabón primario e importa el derivado de mayor valor (semis de cobre, electrodos de grafito, silicio/ferrosilicio).
- **Fluorita** ⚠️ **(corregido 2026-08-01)**: **no es un caso de espejo simple**. México exporta espato flúor (E1: 61%) **y ácido fluorhídrico (HF)** —Koura/Orbia opera en Matamoros la mayor planta de HF del mundo, integrada con la mina Las Cuevas—: en 2018 México **exportó ~161 MM USD de HF** (fracción 281111). La cadena local **llega al HF pero se detiene antes de los fluoropolímeros** (PTFE, fracción 390461), que se **importan** (~30–40 MM USD/año). **Cambio a revisar**: la exportación de HF se desplomó de ~161 MM (2018) a ~6.5 MM (2023) —posible reorientación de Koura al consumo interno o cambio de registro—.
- **Cobre**: el eslabón primario (mena) domina y **crece** (61%→80% de las exportaciones entre 2018 y 2023), mientras las importaciones son semimanufacturas (≈83%): se profundiza la exportación en bruto.
- **Metales preciosos (oro, plata)**: la alta "participación procesada" es **oro/plata en bruto (doré/bullion)**, la forma estándar de exportación —**no** manufactura de mayor valor—; la joyería (manufactura real) es **importadora neta**. No leer su 96–97% como industrialización.
- **Sílice y grafito**: **importadores netos** del eslabón procesado (silicio/ferrosilicio; electrodos), pese a la extracción doméstica: la transformación de mayor valor ocurre fuera.

## 5. Cuidados y límites (declarados)
- **Concordancia HS revisable**: la atribución de fracciones a etapas es una decisión metodológica; los resultados se recalculan al ajustarla (`comercio_etapa.py`).
- **Hueco de reporte 2018 en barita** (y en general baja cobertura de no metálicos pequeños en Comtrade): barita 251110 sin exportación reportada 2016–2020, con dato en 2015 y 2021+. No interpretar el 0 como ausencia real de comercio.
- **2019**: Comtrade devolvió filas de dos vintages de clasificación; se deduplicó por código (último valor); el 2603 quedó consistente con la serie. Revisar si se usa 2019 puntualmente.
- **API preview**: límite de registros y *rate limit*; se descargó socio Mundo agregado (no bilateral). El análisis por socio/destino queda para una extracción posterior.
- **Precios de exportación como proxy de valor**: los valores son en USD FOB/CIF de Comtrade; el CCV (captura de valor) fino requiere cruzar precio frontera vs precio del producto refinado.

## 6. Pendiente / opcional
- Extracción bilateral (socios) para destino de exportaciones y origen de importaciones.
- CCV por mineral (precio exportación bruto vs precio producto procesado).
- Upstreamness/downstreamness (Antràs-Chor) y participación TiVA/ICIO — **alternativa analítica abierta**.

← [[Catalogo de Bases de Datos]] · [[Columna Vertebral Metodologica]] · [[Insercion en cadenas de valor globales]]
