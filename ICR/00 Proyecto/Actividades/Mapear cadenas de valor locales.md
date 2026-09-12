---
title: Mapear las cadenas de valor locales (demanda intermedia)
tipo: subactividad
fase: "Fase 2 - Cadenas de valor locales"
estado: hecho
prioridad: alta
mes_objetivo: "M4-M7"
tags: [icr, subactividad, cadenas-de-valor]
created: 2026-07-23
updated: 2026-09-09
---
Describir, por mineral, la demanda intermedia doméstica en la MIP: ¿qué sectores compran el mineral como insumo? Objetivo 2 del [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)|protocolo descriptivo]].

## Avance (2026-09-09) — Actividad B COMPLETA (10 fichas de cadena)
Ejecutada la [[Ruta metodologica - Construccion de cadenas de valor locales por mineral|Ruta metodológica]] (Fases 1, 3, 7 y 8). **10 fichas de cadena de valor** (una por mineral, L0→L4 con diagrama, cuantificación por eslabón, actores, encadenamientos, cierre aguas abajo, georref y tipología A/B/C/D) en [[Indice - Fichas de Cadena de Valor]]. Datos nuevos: `processed/cv_arbol_mineral.csv`, `cv_eslabones_cuantificado.csv`, `cv_tipologia.csv`; script `scripts/cv_build.py`. **Patrón:** B=5 (Cu,Au,Ag,Pb,Zn), A=2 (Mn; fluorita límite), C=2 (grafito,sílice), D=1 (barita) → predominio del enclave estructural (truncado en el metal). Síntesis y bases de política en [[Sintesis - Patron agregado y bases de politica (cadenas de valor)]]. Piloto (cobre/fluorita) validado con el alumno antes de escalar; formato con glosas para lectura no especializada.

## Avance (2026-09-05) — HECHO (demanda intermedia, insumo previo)
Demanda intermedia doméstica por mineral (top compradores) extraída de la MIP para **2013/2018** (`mip_demanda_intermedia_minerales.csv`) y **2008** (`…_2008_referencia.csv`). Cruzada con las **19 empresas de transformación** verificadas ([[Identificar empresas de transformacion]], `empresas_transformacion.csv`) → mapa estructural del eslabón local por mineral (metales preciosos/cobre → solo fundición-refinación; fluorita → HF de Koura; sílice → vidrio; grafito → siderurgia; barita → perforación petrolera). Recogido en el Cap. VI y en [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] §5.
