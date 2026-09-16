---
title: "Notas — Llenado de vacíos en las series (2026-09-06)"
type: proyecto
tags: [icr, datos, series, vacios, notas]
created: 2026-09-06
updated: 2026-09-06
---

# Notas — Llenado de vacíos en las series de los indicadores

Distinción operativa: **vacío extensible** (la fuente existe, faltaba procesarla) vs **vacío por límite de fuente** (no hay dato observable; solo proxy o queda declarado).

## Resuelto en esta sesión

- **Comercio por etapa pre-2015 → serie 1992-2024** *(extensible, hecho)*. Se descargó de UN Comtrade todas las fracciones HS de la concordancia (X y M, socio Mundo) 1992-2014 y se empalmó con 2015-2024. Salidas: `processed/comercio_por_etapa_1992_2024.csv` y `comercio_posicion_1992_2024.csv` (X_share_crudo por mineral-año). **Caveat**: a lo largo del periodo cambian las versiones del Sistema Armonizado (HS1992…2017); las fracciones a 4-6 dígitos son mayormente estables, pero puede haber saltos en años de revisión → leer como **tendencia**, validar por fracción si se cita un año puntual.

## Pendiente con método definido (no hecho aún)

- **HHI 1992-2003** *(límite parcial de fuente)*. La participación por empresa/mina no está en datos estructurados antes de 2004. Vía: leer la **Tabla 2 del USGS Minerals Yearbook** de ediciones ~1994-2003 (en imagen, como ya se hizo para 2004-2020) + SGM Anuarios históricos + CAMIMEX, con el mismo método aproximado de "líder/régimen". **1992-1993 probablemente no reconstruible** (privatización en curso). Nivel pre-2004 se leería como **régimen**, no cifra exacta. Esfuerzo: medio-alto (lectura de imágenes).
- **HHI 2024** *(extensible)*. Vía: **CAMIMEX Compendio 2025 / SGM Anuario 2024** (ya en `Bases Originales/08` y `09`) con detalle por mina donde exista; `hhi_nometalicos_2020_2024.csv` ya trae 2024 para no metálicos. **2025**: aún no publicado (datos salen 2026-27) → dejar pendiente.
- **CCV — años sueltos dentro de 1992-2025** *(extensible, menor)*. Rellenar con: (a) **precio alterno** para el denominador el año sin USGS (Cochilco / World Bank Pink Sheet / LME); (b) **datos espejo** (lo que el socio reporta importar de México) para el numerador; (c) interpolación lineal solo como último recurso, marcada. No interpolar tramos largos.
- **MIP — años intermedios (RAS 2020/2023)** *(extensible, opcional)*. Actualizar 2013→2020 y 2018→2023 con **RAS** usando marginales de las tablas oferta-utilización del INEGI. El Ghosh RAS es **estimado**, no observado; declararlo. Prioridad baja.

## Regla general
No se inventan datos. Todo relleno lleva su **bandera de método** y su caveat. Los vacíos por límite de fuente se **declaran** en la memoria correspondiente en lugar de imputarse.

← [[Bitacora]] · [[Catalogo de Bases de Datos]]
