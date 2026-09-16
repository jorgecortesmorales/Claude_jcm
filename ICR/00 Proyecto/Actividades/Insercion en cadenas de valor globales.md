---
title: Inserción de México en las cadenas de valor globales
tipo: subactividad
fase: "Fase 3 - Inserción en CVG"
estado: hecho
prioridad: alta
mes_objetivo: "M5-M8"
tags: [icr, subactividad, cadenas-de-valor, comercio]
created: 2026-07-23
updated: 2026-09-05
---
Describir la posición de México por etapa de procesamiento (mena → concentrado → refinado → intermedio → bien final) con comercio BACI/Comtrade: participación por etapa, dependencia de importaciones procesadas, análisis espejo. Objetivo 3.

## Avance (2026-07-30)
- **Datos construidos**: comercio de México por fracción HS descargado de **UN Comtrade** (API pública, sin clave), 2015-2024, X y M vs Mundo. Concordancia **mineral × etapa × HS** construida (revisable) y aplicada. Salidas: `10 Datos/processed/comercio_por_etapa.csv`, `comercio_posicion_resumen.csv`, `concordancia_hs_etapa.csv`; crudo en `Bases Originales/11 Comercio Comtrade/`. Método, resultados y cuidados en [[Memoria - Comercio por etapa de procesamiento (Obj 3)]].
- **Hallazgo**: patrón **espejo** (exportar bruto / importar procesado) claro en cobre, fluorita, grafito, sílice y manganeso. Fluorita confirma la MIP (exporta espato, importa 100% fluoroquímica).
- **Pendiente/opcional**: extracción bilateral por socio (destinos/orígenes), CCV, upstreamness/TiVA.

## Cierre (2026-09-05) — HECHO (núcleo descriptivo)
El análisis descriptivo del Obj. 3 está completo: posición por etapa 2015-2024 + análisis espejo + **CCV como serie 1992-2025** ([[Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)]]) que da la dimensión temporal del encadenamiento hacia adelante. **Solo quedan opcionales**: bilateral por socio, comercio por etapa pre-2015, upstreamness/TiVA.
