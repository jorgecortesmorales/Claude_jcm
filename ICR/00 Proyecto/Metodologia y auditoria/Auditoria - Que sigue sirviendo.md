---
title: Auditoría — qué sigue sirviendo bajo el diseño descriptivo
type: proyecto
tags: [icr, proyecto, auditoria, rediseno]
created: 2026-07-23
updated: 2026-07-23
status: activo
---

# Auditoría — qué sigue sirviendo bajo el diseño descriptivo

Inventario de los activos del proyecto tras el giro **causal → descriptivo (cadenas de valor)** del 2026-07-23 (ver [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]] y [[Bitacora]]). Es el insumo para la siguiente fase: operar sobre los **capítulos** y las **bases de datos**. Regla general: **casi todo el trabajo de datos se conserva; cambia su función** (de variables de un modelo causal a descriptores de cada mercado).

## 1. Bases de datos e indicadores — **el corazón del aporte, se conserva**

| Activo | Estado | Uso descriptivo |
|---|---|---|
| `10 Datos/processed/hhi_numeradores.csv` (493 filas) | ✅ Sirve | HHI por mineral-año = estructura extractiva (Obj. 1) |
| `10 Datos/processed/myb_estructura_industria.csv` (816 filas) | ✅ Sirve | actores y estructura de la industria (USGS Tabla 2) |
| `10 Datos/processed/precios_usgs_anual_empalmado.csv` | ✅ Sirve | precios/valores unitarios por etapa |
| `comercio_exterior_2015_2024.csv` + Bases Originales `04 Comercio Exterior` | ✅ **Gana peso** | posición por etapa e inserción en CVG (Obj. 3) |
| MIP INEGI (por obtener) | ⏳ Pendiente | encadenamientos (Ghosh/CCV, Obj. 1) **y** demanda intermedia doméstica (Obj. 2) |
| Precios Cochilco, reservas, criticidad USGS/UE | ✅ Sirve | contexto y selección del corpus |

**Nuevo dato a construir**: comercio por **etapa de procesamiento** (mena → concentrado → refinado → intermedio → bien final) e identificación de **empresas de transformación** domésticas (Obj. 2 y 3). Ver actividades [[Insercion en cadenas de valor globales]], [[Mapear cadenas de valor locales]], [[Identificar empresas de transformacion]].

## 2. Capítulos I-IV (borrador `Caps I-IV Cortes Morales.docx`) — **se conservan con reencuadre**

- **Cap. I (Introducción)** y **Cap. III (Contexto histórico)**: descriptivos, se conservan casi tal cual.
- **Cap. II (Marco teórico)**: **ajustar** — incorporar **cadenas de valor globales** (Gereffi, Kaplinsky) como eje; conservar estructuralismo (Prebisch) y eslabonamientos (Hirschman/Ghosh); **demotar el SCP causal** (Bain/Mason) a herramienta descriptiva de organización industrial. Revisar el caso de contraste (grafito ya no atomizado — C-17 abierta).
- **Cap. IV (Estructura empresarial)**: ya es **descripción pura** por mineral; se conserva. Aplicar los ajustes de datos pendientes ([[Ediciones Pendientes Documentos Word]]: fluorita ene-2012, grafito concentrado, sílice concentrada, barita decreciente).

## 3. Capítulos V-VIII (andamios `.docx` en `11 Redaccion/`) — **reencuadre**

| Cap. | Acción |
|---|---|
| **V — Insumo-producto** | Conservar, reencuadrado a **descripción** de encadenamientos (Ghosh/CCV) + demanda intermedia doméstica (Obj. 2). |
| **VI — "Modelo de panel"** | **Reconvertir**: de modelo causal a **caracterización/tipología descriptiva** de los 10 mercados (HHI + Ghosh + posición GVC). Renombrar el capítulo. |
| **VII — Reforma 2023** | Reencuadrar a **contexto institucional** (propósito: especulación/soberanía, no industrialización); event study **opcional**. |
| **VIII — Síntesis** | Conservar; integra la descripción y las **bases de política industrial**. |

> Los `.docx` de V-VIII aún tienen el enfoque del bloque previo (columna vertebral con "puente causal"); se reescribirán en la fase de capítulos.

## 4. Notas del vault

- ✅ **Actualizadas al diseño descriptivo**: [[Columna Vertebral Metodologica]], [[Diagrama - Columna Vertebral Metodologica]], [[Diseno Metodologico]] (callout), actividades (Tablero), [[Home]], `CLAUDE.md`.
- ⚠️ **Marcadas para reescritura** (aún causales): [[Modelo Econometrico]], [[Variables y Datos]], índices de los Caps. V/VII/VIII, y las notas de planteamiento [[Pregunta de Investigacion]], [[Objetivos]], [[Hipotesis]], [[Justificacion]] (reflejan el protocolo causal; se alinean al v3 en la fase de capítulos).
- 📦 **Archivado**: versiones anteriores del protocolo en `Documentos Originales/Archivo - versiones anteriores del protocolo/` (original, con-comentarios, correcciones v1, v2, el borrador v3 escueto y el PDF causal previo). **Protocolo vigente**: `Protocolo ICR - vfinal (revision consistencia descriptiva).docx` (+ PDF); la base descriptiva del alumno es `...vfinal.docx`.

## 5. Otros

- **Event study preliminar** (GM AR −4.07%/−4.73%, CAR≈−8.3%): se conserva como pieza **menor y opcional** del contexto institucional (Cap. VII).
- **Comparación Chile/Australia**: **opcional** (referencia ilustrativa); el rol de México se describe con la posición en CVG.
- **Litio/LitioMx**: **fuera** (no hay producción en México).

## Próximas acciones (fase de capítulos y bases)
1. Obtener y depurar la **MIP INEGI** → Ghosh/CCV + demanda intermedia doméstica.
2. Construir el **comercio por etapa** y la identificación de **empresas de transformación**.
3. Reconvertir el **Cap. VI** (tipología descriptiva) y reencuadrar Caps. V, VII, VIII.
4. Ajustar el **Cap. II** (marco teórico → cadenas de valor).
5. Alinear las notas de planteamiento al protocolo v3.

← [[Home]] · [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]] · [[Bitacora]]
