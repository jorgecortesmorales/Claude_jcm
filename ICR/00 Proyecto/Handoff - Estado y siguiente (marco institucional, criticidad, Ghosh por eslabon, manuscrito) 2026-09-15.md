---
title: "Handoff — Estado al 2026-09-15 e inicio de chat nuevo"
type: handoff
tags: [icr, handoff, estado, marco-institucional, ghosh-eslabon]
created: 2026-09-15
updated: 2026-09-15
status: activo
---

# Handoff — arrancar un chat nuevo (ICR minerales críticos)

> [!info] Qué es esto
> Fuente única de verdad para continuar la tesis en un chat con contexto limpio. Resume qué está hecho, qué sigue y dónde vive cada cosa. **No confundir con el otro proyecto** [[icr_diana_vivienda|ICR de Diana (vivienda Colombia, ARDL)]], que vive en `ICR DIANA/`.

## 0. Reglas de trabajo (vigentes)
- Trabajar **solo dentro de `ICR/`**; usar `py` (no `python`); skills de Obsidian para `.md`/`.canvas`/`.base`.
- **Diseño descriptivo**, no causal. Concepto ordenador = **enclave estructural**. HHI/Ghosh/CCV son descriptores.
- **Sin voz de IA** en la redacción; versionar (git); handoff antes de agotar contexto.
- **No aceptar el control de cambios del PROTOCOLO** — espera al asesor (Dr. Jordy Micheli Thirion).
- Git: rama `main`, remoto `git@github.com:jorgecortesmorales/Claude_jcm.git` (SSH autenticado, identidad `jorgecortesmorales8@gmail.com`). **Todo pusheado; `main` = `639527b`.**

## 1. Estado actual — TODO lo sustantivo está hecho

**Datos e indicadores (aporte central): completos y validados.**
- Los 8 indicadores + Actividad A (peso del bloque 1992-2024) + Actividad B (cadenas de valor locales).
- **Nuevo (2026-09-15): Ghosh hacia adelante por eslabón** (extracción / refinación / semimanufactura) en los tres frentes: nacional por mineral (MIP 2008/2013/2018), estatal e inter-estatal (2018), internacional (ICIO 2008-2020). Memoria: [[Memoria - Encadenamientos por eslabon (extraccion, refinacion, semimanufactura)]]. Hallazgo: el arrastre no se propaga aguas abajo (cobre refina 1.37 pero semis 0.95; refinación de preciosos 0.62; China sostiene 1.53→1.30, México cae 1.51→1.17).

**Actividad B (cadenas de valor locales): cerrada.**
- 10 fichas L0→L4 + tipología A/B/C/D + mapas por mineral y de conjunto + socios comerciales. Índice: [[Indice - Fichas de Cadena de Valor]].

**Criticidad de productos: hecha e integrada.**
- Clasificación producto-por-producto (USGS 2022/2025, UE CRMA 2023, IEA): [[Clasificacion de productos por criticidad]] + `criticidad_productos.csv`. Integrada en Cap. II (§II.2.5, borrador), VI (§VI.8.1) y VII (§VII.5.2).

**Marco institucional (Cap. VII): investigado y redactado (descriptivo).**
- Notas: [[Marco institucional de Mexico y su impacto en las cadenas de valor (descriptivo)]], [[Comparativa institucional internacional (China y modelo nordico) descriptivo]].
- Fuentes descargadas (`10 Datos/Bases Originales/15 Marco Institucional/`, fuera de git): decreto DOF 2023, Ley Minera, IGF/IISD (evaluación MX), Observatorio del Desarrollo 35, CEPAL, OCDE (restricciones), UE CRMA, Nordic Battery, ORF China, Fraser. Catálogo + qué leer: [[Fuentes del marco institucional (analisis y evaluaciones) - bibliografia anotada]] y [[Guia de lectura - marco institucional (que leer de cada documento)]].
- Académicos revisados por pares (descarga manual): Poelzer et al. 2015 (nórdico), PMC 2026 (China).

**Redacción.**
- **Caps. I-IV**: ✅ aceptados (documento del alumno, `00 Proyecto/Documentos Originales/Caps I-IV Cortes Morales.docx`).
- **Caps. V-VIII**: borradores generados por script (`build_capV/VI/VII/VIII.py` → `.docx` en `11 Redaccion/`), con todos los resultados. Estado = **📝 falta versión de entrega del alumno** (adaptar a su voz).
- **Manuscrito consolidado (Caps I-VIII)**: `11 Redaccion/ICR - Manuscrito consolidado (Caps I-VIII).docx` + `.pdf` (114 pp), ensamblado con Word (`build_manuscrito_word.py`; NO usar docxcompose, Word lo rechaza). Regenerable sin tocar los capítulos individuales.

## 2. Qué sigue (ruta crítica)
1. **📝 Versión de entrega del alumno**: adaptar a su redacción los Caps. V-VIII y el §II.2.5 del Cap. II. *Es trabajo del alumno (voz/estilo), no técnico.* Prioridad V → VI → VIII → VII. Los borradores iniciales están en [[Borradores iniciales - secciones con dato listo (para version de entrega)]].
2. **⏸️ Protocolo**: control de cambios en espera del asesor (no aceptar antes).
3. **⭕ Opcionales** (no bloquean): event study + entrevistas (Cap. VII); leer los PDF del marco institucional (guía provista); refrescar entregables (infografía/deck) con lo nuevo; `gh auth login` si se quiere el CLI (el push por SSH ya funciona).
4. **⏳ Cierre**: revisión final + examen (plan may-jun 2027; el análisis va ~9 meses adelantado).

## 3. Para orientarte al arrancar
- **Tablero maestro de avance** (capítulos→subtemas→actividades, plan vs. real, estados): [[Estructura y Cronograma de la ICR]] + artefacto interactivo (https://claude.ai/code/artifact/d020c84f-0043-4943-a46a-a57c6a10dca9).
- **Bitácora**: [[Bitacora]] (entradas 2026-09-09 → 2026-09-15).
- **Catálogo de datos**: [[Catalogo de Bases de Datos]]. **Resumen metodológico**: `13 Entregables/Resumenes descriptivos/`.
- **Memoria de estado**: [[icr_estado_2026_08]] (auto-memoria).

← [[Home]] · [[Estructura y Cronograma de la ICR]] · [[Bitacora]] · [[Indice - Fichas de Cadena de Valor]]
