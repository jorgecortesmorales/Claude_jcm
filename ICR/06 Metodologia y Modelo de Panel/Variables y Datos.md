---
title: Variables y Datos
type: metodologia
tags: [icr, metodologia, datos]
created: 2026-07-16
updated: 2026-07-16
status: en-construccion
---

> [!warning] Reencuadre pendiente (2026-07-23) — diseño descriptivo
> El proyecto pasó de un diseño causal (panel HHI→Ghosh) a uno **descriptivo de cadenas de valor**. Esta nota aún refleja el enfoque causal y se reescribirá en la fase de capítulos. Ver [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]] y [[Columna Vertebral Metodologica]].


# Variables y Datos

## Variable dependiente
- **Coeficiente de Ghosh (FL)** — principal. Fuente: cálculo propio a partir de MIP INEGI.
- **Coeficiente de captura de valor (CCV)** — alternativa, mayor cobertura temporal. Fuente: Comtrade (precio exportación) / USGS (precio producto refinado). Complemento nacional 2015-2024: `10 Datos/Bases Originales/04 Comercio Exterior/`.

## Variable independiente clave
- **HHI por mineral-año** — construcción propia a partir de series de participación de mercado (Cámara Minera de México, SGM, Perfiles de Mercado SE). Ver estimaciones iniciales en [[Corpus de Diez Minerales]] y [[Sintesis Comparativa]].

## Variables de control
- **Precio internacional del mineral (PrecioIntl)**: ✅ **LISTA** — `10 Datos/processed/precios_usgs_anual_empalmado.csv`: los 10 minerales, 1993-2025 (330 obs.), USD/t, nominal y constantes 1998. Serie primaria armonizada USGS DS-140 + empalme documentado (ver [[Definicion de Series USGS|Definición de Series USGS]]). Robustez: Cochilco mensual para los 5 metales (`precios_consolidados_mensual.csv`).

> [!warning] Decisión metodológica (2026-07-17): no usar el precio implícito nacional como PrecioIntl
> Se evaluó sustituir el precio USGS de los 5 no metálicos por el precio implícito nacional (valor/volumen INEGI). **Se descartó como fuente primaria por endogeneidad**: PrecioIntl debe ser exógeno (productores tomadores de precios), pero el precio implícito incorpora el poder de mercado doméstico — el mismo mecanismo que captura el HHI (caso extremo: el precio implícito del manganeso es en gran medida el precio fijado por Autlán como monopolista). Usarlo como control filtraría parte del efecto del HHI hacia β₂ y sesgaría β₁ hacia cero. Problemas adicionales: inconsistencia de unidades en el panel (USD/bolsa vs. MXN/doméstico) y efectos de composición del valor unitario.
> **Uso aprobado**: prueba de robustez secundaria, convertido a USD y declarada explícitamente como operacionalización alternativa. Matiz a declarar en el Cap. VI: los precios USGS de no metálicos también son valores unitarios (no cotizaciones de bolsa), pero son externos a la estructura de mercado mexicana, lo que preserva la exogeneidad.
- **CAPEX de empresas dominantes** (informes anuales/estados financieros) — pendiente de recopilar.
- **Proporción de capital extranjero por mineral** — pendiente de recopilar.
- **Precio y valor de producción nacional** (complementario, en pesos) → `10 Datos/Bases Originales/02 Produccion y Precios Nacionales/2. produccion y precios.xlsx` (mensual, 2000-2025, los 10 minerales del corpus).

## Bases de datos disponibles
Ver clasificación completa por tema y utilidad en [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]] (10 Datos/). Resumen:
- `01 Criticidad y Produccion Historica/` — listas USGS/UE + producción histórica nacional (todos los minerales).
- `02 Produccion y Precios Nacionales/` — producción, volumen y precios mensuales, exactamente los 10 minerales del corpus (2000-2025). **Más directamente aprovechable.**
- `03 Precios Internacionales Cochilco/` — PrecioIntl para 5/10 minerales.
- `04 Comercio Exterior/` — exportaciones/importaciones/balanza 2015-2024.
- `05 Reservas y Produccion Mundial/` — posición mundial de México, un corte (no serie), útil para redacción y comparación Chile/Australia (H2).
- `00 Proyecto/Documentos Originales/Base de Datos - Mercados Mineros Mexico.xlsx` — hojas: `Léeme`, `Datos_Mercado`, `Comercio_Exterior`, `Anexo_1990_2020`, `Catalogo_Minerales`, `Catalogo_Empresas`, `Fuentes`. Pendiente de auditoría de cobertura/completitud por mineral-año.

← [[Home]] · [[Modelo Econometrico|Modelo Econométrico]] · [[Diccionario de Variables]] · [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]] (10 Datos/)
