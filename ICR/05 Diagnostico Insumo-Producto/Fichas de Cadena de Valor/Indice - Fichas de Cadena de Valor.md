---
title: "Índice — Fichas de Cadena de Valor (Actividad B)"
type: indice
tags: [icr, cadena-de-valor, ficha, indice]
created: 2026-09-09
updated: 2026-09-09
status: en-construccion
---

# Índice — Fichas de Cadena de Valor por mineral (Actividad B)

Producto de la [[Ruta metodologica - Construccion de cadenas de valor locales por mineral|Ruta metodológica]] (Fases 1–7). Cada ficha mapea los eslabones **L0→L4**, cuantifica cada uno (VBP/empleo MIP + X/M comercio + CCV), ubica el **punto de ruptura** de la cadena dentro del país y clasifica en la tipología **A/B/C/D**. Alimenta el Cap. VI (tipología) y el Cap. VIII (bases de política).

## Tipología descriptiva
- **A** — cadena local desarrollada (L1–L3(-L4) presentes y conectados).
- **B** — truncada en el metal refinado (L1–L2 presentes, L3–L4 ausentes/exportados).
- **C** — usuario doméstico con eslabón importado (hay industria usuaria; el insumo procesado se importa).
- **D** — exportación en bruto (se detiene en L1).

## Fichas (10 completas)

| Mineral | Tipo | Ruptura | Rasgo distintivo |
|---|---|---|---|
| [[Ficha CV - Cobre]] | **B** truncada en el metal | L2→L3 | co-localizado (mina+fundición), pero exporta concentrado 61→81 % |
| [[Ficha CV - Oro]] | **B** truncada en el metal | L2→L4 | exporta refinado (doré); joyería importada |
| [[Ficha CV - Plata]] | **B** truncada en el metal | L2→L4 | 1.º mundial; se cierra en el lingote |
| [[Ficha CV - Plomo]] | **B** truncada en el metal | L1→L2 | baterías (Clarios) pero de reciclado, no del primario |
| [[Ficha CV - Zinc]] | **B** truncada en el metal | L1→L2 | refina (IMMSA) pero exporta concentrado 64→80 % |
| [[Ficha CV - Fluorita]] | **A** (límite A/B) | L2→L3 | HF de clase mundial (Koura); enclave de exportación |
| [[Ficha CV - Manganeso]] | **A** desarrollada | L2→L3 | Autlán exporta ferroaleación, no mena |
| [[Ficha CV - Grafito]] | **C** usuario c/ insumo importado | L1→L2 | siderurgia EAF usa electrodos importados; mina decrece |
| [[Ficha CV - Silice]] | **C** usuario c/ insumo importado | L1→L2 | vidrio/cemento local; silicio importado (M≈264 MUSD) |
| [[Ficha CV - Barita]] | **D** exportación en bruto | L1→L2 | insumo petrolero (PEMEX); sin química del bario |

## Patrón agregado
**B = 5** (cobre, oro, plata, plomo, zinc) · **A = 2** (manganeso; fluorita en el límite) · **C = 2** (grafito, sílice) · **D = 1** (barita). Domina la **cadena truncada en el metal (B)**: la huella del **enclave estructural**. Los dos casos A (manganeso→ferroaleación, fluorita→HF) muestran que la transformación con capital nacional es posible, pero se detiene en el intermedio y —en la fluorita— opera como enclave de exportación. Síntesis y bases de política en [[Sintesis - Patron agregado y bases de politica (cadenas de valor)]] (Fase 8).

## Mapas (ubicación y comercio)
Cada ficha incluye su **mapa de cadena** (§6b): panel de México con la extracción por estado y las plantas de transformación (empresa y ciudad), y panel mundial con los **países de destino de exportación** (rojo) y **origen de importación** (azul). El **mapa de conjunto** está en la [[Sintesis - Patron agregado y bases de politica (cadenas de valor)|síntesis]]. PNG en `13 Entregables/mapas/` (`mapa_<mineral>.png`, `mapa_conjunto.png`); scripts `cv_socios.py` (socios) y `cv_mapas.py` (mapas).

## Datos de respaldo
`processed/cv_arbol_mineral.csv` (Fase 1) · `processed/cv_eslabones_cuantificado.csv` (Fase 3) · `processed/cv_tipologia.csv` (Fase 7) · `processed/cv_comercio_socios.csv` y `cv_socios_resumen.csv` (destinos/orígenes) · geometrías en `10 Datos/Bases Originales/14 Geo/` · scripts `cv_build.py`, `cv_socios.py`, `cv_mapas.py`.

## Criticidad de los productos
La clasificación de **cada producto por nivel de criticidad** (listas oficiales USGS 2025 / UE CRMA 2023 / IEA), su sector y su estatus de uso/exportación/importación en México está en [[Clasificacion de productos por criticidad]].

← [[Indice Diagnostico Insumo-Producto]] · [[Ruta metodologica - Construccion de cadenas de valor locales por mineral]] · [[Home]]
