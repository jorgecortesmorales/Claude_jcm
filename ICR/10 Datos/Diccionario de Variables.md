---
title: Diccionario de Variables
type: datos
tags: [icr, datos]
created: 2026-07-16
updated: 2026-09-29
status: vigente
---

# Diccionario de Variables

> [!info] Diseño descriptivo (desde 2026-07-23)
> Los indicadores son **descriptores** de la estructura de cada mercado, no variables dependientes/independientes de un modelo causal. La matemática, supuestos y límites de cada uno están en [[Auditoria de indicadores (justificacion, matematica, limites)]]; las bases, en [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]].

| Variable | Descripción | Tipo (descriptor de…) | Unidad | Fuente / base |
|---|---|---|---|---|
| HHI | Índice de Herfindahl-Hirschman por mineral-año | Concentración extractiva | Índice (0-10 000) | CAMIMEX, SGM, USGS — `hhi_consolidado` |
| HHI geográfico | HHI sobre participaciones estatales en la extracción | Concentración territorial | Índice (0-10 000) | SGM — `georref_regionalizacion` |
| Leontief / BL, $U_j$ | Encadenamiento hacia atrás (suma de columna de $\mathbf{L}$) y su índice de Rasmussen | Arrastre sobre proveedores | Índice (media = 1) | MIP INEGI — `mip_encadenamientos_minerales` |
| Ghosh / FL, $U_i$ | Encadenamiento hacia adelante (suma de fila de $\mathbf{G}$) y su índice de Rasmussen | Intensidad del arrastre aguas abajo | Índice (media = 1) | MIP INEGI — `mip_encadenamientos_minerales`, `mip_encadenamientos_eslabones` |
| HEM atrás ($\text{EH}^{-}$) | % del VBP que se perdería al extraer las compras del sector | Peso económico (hacia atrás) | % del VBP | `mip_hem_minerales`, `mip_hem_eslabones`, `hem_estatal_mineria`, `icio_hem_mineria` |
| HEM adelante ($\text{EH}^{+}$) | % del VBP que se perdería al extraer las ventas del sector | Peso económico del arrastre aguas abajo | % del VBP | idem |
| HEM total | HEM atrás + HEM adelante | Peso económico total | % del VBP | idem |
| DI/VBP | Fracción del VBP destinada a demanda intermedia doméstica | Uso intermedio interno | Proporción | MIP INEGI — `mip_encadenamientos_minerales` |
| CCV | Coeficiente de captura de valor (valor unitario E1 / precio refinado USGS) | Captura de valor en el tiempo | Razón de precios | Comtrade / USGS — `ccv_serie` |
| X_share_crudo | Fracción de la exportación que sale en etapa E1 | Posición comercial | Proporción | Comtrade — `comercio_posicion_1992_2024` |
| crudo_share | Fracción del VA minero exportado que sale en crudo | Captura de valor internacional | Proporción | OECD ICIO — `icio_dva_mineria` |
| PrecioIntl | Precio de referencia del refinado (USGS empalmado) | Insumo del CCV y de la valuación | USD/t | USGS — `precios_usgs_anual_empalmado` |

## Fuentes de datos crudos
- `00 Proyecto/Documentos Originales/Base de Datos - Mercados Mineros Mexico.xlsx` — hojas: `Léeme`, `Datos_Mercado`, `Comercio_Exterior`, `Anexo_1990_2020`, `Catalogo_Minerales`, `Catalogo_Empresas`, `Fuentes`.
- `10 Datos/Bases Originales/` — ver clasificación completa en [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]].
- **CSV limpio de todas las hojas**: `raw/csv/`. **Indicadores**: `processed/`. Consolidado con fórmulas vivas: `13 Entregables/Consolidado datos y calculos/`.

← [[Home]] · [[Catalogo de Bases de Datos]]
