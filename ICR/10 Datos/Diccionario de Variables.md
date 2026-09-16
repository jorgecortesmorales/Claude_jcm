---
title: Diccionario de Variables
type: datos
tags: [icr, datos]
created: 2026-07-16
updated: 2026-07-16
status: en-construccion
---

# Diccionario de Variables

| Variable | Descripción | Tipo | Unidad | Fuente |
|---|---|---|---|---|
| HHI | Índice de Herfindahl-Hirschman por mineral-año | Independiente clave | Índice (0-10,000) | Cámara Minera de México, SGM, Perfiles de Mercado SE |
| Ghosh (FL) | Coeficiente de encadenamiento hacia adelante | Dependiente (principal) | Coeficiente | MIP INEGI (cálculo propio) |
| CCV | Coeficiente de captura de valor | Dependiente (alternativa) | Razón de precios | Comtrade / USGS (cálculo propio) |
| Leontief | Coeficiente de encadenamiento hacia atrás | Descriptivo (Cap. V) | Coeficiente | MIP INEGI (cálculo propio) |
| PrecioIntl | Precio internacional del mineral | Control | USD/unidad | Cochilco (cobre/plata/oro/plomo/zinc, ya en `processed/precios_consolidados_mensual.csv`) + USGS pendiente (resto) — ver [[Validacion de Fuentes de Precios\|Validación]] |
| CAPEX | Inversión de capital de empresas dominantes | Control | MDD/año | Informes anuales/estados financieros |
| CapExtran | Proporción de capital extranjero de empresas dominantes | Control | % | Informes anuales |

Ver contexto completo en [[Variables y Datos]] (06 Metodologia y Modelo de Panel/).

## Fuentes de datos crudos
- `00 Proyecto/Documentos Originales/Base de Datos - Mercados Mineros Mexico.xlsx` — hojas: `Léeme`, `Datos_Mercado`, `Comercio_Exterior`, `Anexo_1990_2020`, `Catalogo_Minerales`, `Catalogo_Empresas`, `Fuentes`.
- `10 Datos/Bases Originales/` (5 subcarpetas temáticas, 9 archivos) — ver clasificación completa en [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]].
- **CSV limpio de todas las hojas**: `raw/csv/` (40 archivos). **Consolidados listos para análisis**: `processed/precios_consolidados_mensual.csv` y `processed/comercio_exterior_2015_2024.csv` — ver [[Validacion de Fuentes de Precios|Validación de Fuentes de Precios]].

Datos procesados adicionales en `processed/`.

← [[Home]]
