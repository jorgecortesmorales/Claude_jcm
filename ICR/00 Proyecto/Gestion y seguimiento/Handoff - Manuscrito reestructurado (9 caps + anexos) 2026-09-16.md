---
title: "Handoff — Manuscrito reestructurado (9 capítulos + anexos) 2026-09-16"
type: handoff
tags: [icr, handoff, estado, reestructura, manuscrito, pipeline]
created: 2026-09-16
updated: 2026-09-16
status: activo
---

# Handoff — arrancar un chat nuevo (ICR minerales críticos)

> [!info] Qué es esto
> Fuente única de verdad para continuar la tesis en un chat con contexto limpio. **Reemplaza** al handoff del 2026-09-15. **No confundir** con el otro proyecto (ICR de Diana, vivienda Colombia, en `ICR DIANA/`).

## 0. Reglas de trabajo (vigentes)
- Trabajar **solo dentro de `ICR/`**; usar `py` (no `python`); skills de Obsidian para `.md`/`.canvas`/`.base`.
- **Diseño descriptivo**, no causal. Concepto ordenador = **enclave estructural**. HHI/Ghosh/CCV son descriptores.
- **Sin voz de IA** en la redacción; versionar (git); handoff antes de agotar contexto.
- **No aceptar el control de cambios del PROTOCOLO** — espera al asesor (Dr. Jordy Micheli Thirion).
- Git: rama `main`, remoto `git@github.com:jorgecortesmorales/Claude_jcm.git`. **Todo pusheado; `main` = `0d88dca`.**

## 1. Estado actual — reestructura completa hecha (los 12 puntos del encargo, cerrados)

El encargo del 2026-09-15 (12 puntos: estructura expositiva, datos/gráficos completos, índices, descripciones completas, APA, vacíos, vault, sin comentarios, rol ampliado, auditoría de indicadores, recomendaciones de lectura, secuencia) **está aplicado**.

**Documento** — `11 Redaccion/manuscrito/ICR - Manuscrito (nueva estructura).docx`:
- **9 capítulos** con estructura expositiva (método consolidado en Cap. III), separada de la ruta de trabajo. Orden: I Introducción (justificación + peso y composición del bloque) · II Marco teórico (incl. criticidad por producto) · III Marco metodológico · IV Contexto histórico e institucional (reforma 2023 + internacional) · V Estructura empresarial (HHI) · VI Encadenamientos · VII Inserción global · VIII Tipología (+ Ghosh estatal/interestatal + mapas) · IX Síntesis y política.
- **Anexos B** (series completas: CCV, HHI, comercio, encadenamientos, **por eslabón por mineral y por país**), **C** (10 fichas de cadena + mapa por mineral), **D** (declaración de vacíos).
- **37 cuadros, 29 ilustraciones**, índice general + de cuadros + de ilustraciones como **campos de Word** (abrir y F9), citas y bibliografía **APA**, 0 referencias cruzadas rotas.

**Pipeline reproducible** (`11 Redaccion/pandoc/`):
- `build.py` compila un capítulo; `build_book.py` ensambla el manuscrito completo; `mk_accepted.py` (Caps I/II/IV desde el aceptado), `mk_cap5.py` (Cap V), `mk_anexos.py` (Anexos). Figuras: `11 Redaccion/figuras/fig_*.py` (matplotlib desde CSV) + mapas en `figuras/mapas/`.
- `reference.docx` (TNR 12, 1.5, justificado), `apa.csl`, `references.bib`. Regenerar todo: `py pandoc/build_book.py`.
- **Nota técnica:** la comparación internacional (ICIO) usa el sector **B07_08** (minería no energética) → México Ghosh 1.51 / crudo 0.38; China 1.53 / 0.07.

**Indicadores**: auditados uno por uno en [[Auditoria de indicadores (justificacion, matematica, limites)]] → Cap. III. Incluidos: HHI (mercado y geográfico), Leontief/Ghosh/Rasmussen, **por eslabón (mineral, estatal, interestatal, internacional)**, demanda intermedia, CCV, comercio por etapa y destinos, DVA/crudo_share, peso y composición del bloque, criticidad por producto.

## 2. Qué sigue (todo opcional; el núcleo está completo)
1. **Revisión de literatura del alumno** por capítulo (guía: [[Recomendaciones de lectura por capitulo]]) y **adaptar la redacción a tu voz** (los Caps V-IX y III son borradores técnicos sólidos, sin voz de IA, listos para tu pluma).
2. **Cosmético**: excluir del índice general los tres encabezados de índice (ajuste menor de estilo en `build_book.py`).
3. **Bibliografía**: migrar [[Bibliografia]] a Zotero → exportar `.bib` para citas 100 % gestionadas (hoy las 7 metodológicas van con `references.bib` y el resto como texto APA).
4. **Protocolo**: control de cambios en espera del asesor (no aceptar antes).
5. **Opcionales de análisis**: event study + entrevistas (Cap. VII/IV), Ghosh interestatal por eslabón si se quisiera aún más detalle.

## 3. Para orientarte al arrancar
- **Mapa visual** del proyecto: [[Mapa Visual del Proyecto]] (canvas). **MOC**: [[Mapa del Proyecto]]. **Tablero de avance**: [[Estructura y Cronograma de la ICR]].
- **Arquitectura del documento**: [[Arquitectura del documento (estructura expositiva)]] (rige el manuscrito).
- **Organización del vault** (nueva, sep-2026): `00 Proyecto/` en subcarpetas **Gestion y seguimiento/** (handoffs, bitácora, rutas) y **Metodologia y auditoria/** (arquitectura, auditorías, protocolo, recomendaciones). Carpetas `01`–`09` = notas de trabajo históricas; manuscrito final en `11 Redaccion/manuscrito/`.
- **Memoria de estado**: [[icr_reestructura_documento]] (auto-memoria).

← [[Home]] · [[Mapa del Proyecto]] · [[Bitacora]] · [[Estructura y Cronograma de la ICR]]
