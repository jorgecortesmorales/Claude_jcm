---
title: Validación de Fuentes de Precios
type: datos
tags: [icr, datos, validacion, qa]
created: 2026-07-16
status: validado
---

# Validación de Fuentes de Precios y Producción

Auditoría realizada el 2026-07-16 sobre las bases de precios/producción importadas. **Veredicto general: SÍ sirven para la tesis**, con las salvedades documentadas abajo.

## 1. Series Cochilco (5 archivos `Precios-*-Mensual.xlsx`) — ✅ VÁLIDAS

**Fuente**: Comisión Chilena del Cobre (Cochilco), Dirección de Estudios y Políticas Públicas — agencia oficial del gobierno de Chile que republica los precios de la Bolsa de Metales de Londres (BML/LME), COMEX y London Fix. Es fuente estándar en la literatura de economía minera; citable directamente.

| Mineral | Serie | Unidad | Cobertura | Cubre horizonte 1992-2025 |
|---|---|---|---|---|
| Cobre | BML + COMEX (nominal) | ¢USD/lb | ene-1960 a dic-2024 | ✅ (falta 2025) |
| Oro | London Fix AM | USD/ozt | ene-1978 a dic-2024 | ✅ (falta 2025) |
| Plata | London Fix | USD/ozt | ene-1978 a dic-2024 | ✅ (falta 2025) |
| Plomo | BML settle | ¢USD/lb | ene-1989 a dic-2024 | ✅ (falta 2025) |
| Zinc | BML settle | ¢USD/lb | ene-1989 a dic-2024 | ✅ (falta 2025) |

**Uso en la tesis**: variable de control `PrecioIntl` del [[Modelo Econometrico|modelo de panel]] para estos 5 metales, y denominador del CCV (precio del producto refinado en destino).

**Salvedades**:
- Series **nominales** — decidir si el panel usa nominal (con efectos fijos de año absorben inflación común) o deflactar; declararlo en el Cap. VI.
- Falta **2025** — actualizar desde cochilco.cl al cierre del año de datos.
- El COMEX de cobre tiene huecos ("N.D.") en los sesenta-setenta — usar BML como serie principal.

## 2. INEGI Banco de Indicadores (`2. produccion y precios.xlsx`) — ✅ VÁLIDA CON UNA CORRECCIÓN

**Fuente**: consulta generada del Banco de Indicadores de INEGI (metadatos del archivo lo confirman: autor INEGI, generado 21/12/2025). Fuente oficial, citable.

- **Producción** (valor, millones MXN corrientes) y **Volumen** (toneladas): mensual ene-2000 a oct-2025, exactamente los 10 minerales del corpus. ✅
- **Precios v1** (implícito = valor/volumen): ⚠️ **ERROR DETECTADO Y VERIFICADO** — las columnas de **oro y plata están infladas exactamente 1000×** respecto a la fórmula declarada en la propia hoja (verificado: oro ene-2000 muestra 8.70E10 cuando valor×10⁶/volumen = 8.70E7). Plomo, cobre, zinc y los no metálicos son correctos (ratio = 1). **No usar la hoja v1 para oro/plata**; usar el consolidado (abajo), donde el precio implícito se recalculó desde las hojas primarias.
- **Precios v2**: consolidación mixta ya construida (Cochilco para los 5 metales + implícito nacional para los 5 no metálicos). Estructura coherente y valores verificados contra Cochilco (oro ene-2000 = 284.6 ✓). Útil como referencia; el consolidado nuevo la reemplaza con trazabilidad completa por serie/fuente.

**Validación cruzada realizada**: el precio implícito nacional de oro (87.0M MXN/ton, ene-2000) es consistente con el internacional (284.6 USD/ozt × 32,150.7 ozt/ton × ~9.5 MXN/USD ≈ 87M MXN/ton) — la coherencia entre ambas fuentes independientes respalda la calidad de los datos INEGI.

**Salvedad de cobertura**: el horizonte del panel inicia en 1993, pero INEGI aquí inicia en **2000** — los años 1993-1999 de producción/precios nacionales requerirán otra fuente (Anuarios SGM o INEGI histórico).

**Salvedad conceptual**: el precio implícito nacional para los 5 no metálicos **no es un precio internacional** — para `PrecioIntl` de manganeso/grafito/barita/fluorita/sílice sigue pendiente USGS Mineral Commodity Summaries (como ya prevé el protocolo).

## 3. Balanza comercial (`4. balanza comercial.xlsx`) — ✅ VÁLIDA CON FLAGS

Cobertura 2015-2024, USD. Consolidada en `processed/comercio_exterior_2015_2024.csv` (verificado: las 3 categorías suman exactamente el TOTAL GENERAL).

**Flags**:
- La hoja Importaciones original tiene layout partido (2015-2019 y 2020-2024 en bloques con productos en distinto orden) — el consolidado ya lo resuelve emparejando por nombre de producto.
- ⚠️ Exportaciones, fila "Otros (No Metálicos)": los valores 2021-2024 son idénticos al 2020 (210,841,038 repetido) — probable arrastre en el archivo original. Verificar contra la fuente primaria antes de usar esa fila específica.
- Columnas auxiliares con `#¡REF!` en las hojas originales — excluidas del consolidado.
- **Fuente primaria confirmada (2026-07-16)**: Informes Anuales de la **Cámara Minera de México (CAMIMEX)** — datos extraídos manualmente por el usuario desde los PDF. Citable como: Cámara Minera de México, *Informe Anual* (ediciones correspondientes a cada año). Implicación de la extracción manual: conviene un spot-check de ~5-10 valores contra los PDF originales antes de usar la base en el Cap. V/VI (el valor repetido de "Otros (No Metálicos)" 2021-2024 probablemente sea un artefacto de esa transcripción).

## 4. Archivos consolidados producidos (en `processed/`)

| Archivo | Contenido | Filas |
|---|---|---|
| `precios_consolidados_mensual.csv` | Formato largo: `fecha,anio,mes,mineral,serie,unidad,fuente,precio`. Cochilco (3,396 obs.: oro 564, plata 564, cobre BML+COMEX 1,404, plomo 432, zinc 432) + precio implícito nacional recalculado para los 10 minerales (3,092 obs., ene-2000 a oct-2025) | 6,488 |
| `comercio_exterior_2015_2024.csv` | Formato largo: `anio,flujo,categoria,producto,es_agregado,valor_usd`. Exportaciones (250) + Importaciones (260), con marcador de filas agregadas | 510 |

Formato de ambos: UTF-8 con BOM, separador coma, **decimales con punto, sin separadores de miles**, fechas ISO — abren directo en Excel sin conversión.

Además, **las 40 hojas de los 10 libros** están exportadas como CSV crudo en `raw/csv/<archivo>/<hoja>.csv` con el mismo formato.

← [[Home]] · [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]] · [[Variables y Datos]]
