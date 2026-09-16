---
title: "Handoff — Paso 6 (comparación internacional) + C2 (integración a redacción)"
type: proyecto
tags: [icr, proyecto, handoff, comparacion-internacional, ghosh, redaccion]
created: 2026-09-06
updated: 2026-09-06
status: paso-6-hecho / C2-hecho
---

# Handoff — para el chat nuevo (2026-09-06)

> [!important] Fuente única de verdad para continuar. Léela completa antes de tocar nada. Todo el trabajo es **dentro de `ICR/`**. Usar **`py`** (no `python`). Diseño **descriptivo**, concepto ordenador = **enclave estructural**. El seguimiento vivo del esfuerzo está en [[Ruta - Completar indicadores y series (seguimiento)]] — actualízalo en cada avance.

> [!done] Estado al 2026-09-08 (punto de entrada para sesión nueva). **Ruta completa: pasos 1-8, 6.5, C2, +A.** Añadido: comparación internacional en 3 cortes (2008/2013/2018), DVA 1995-2020, HHI extendido 1994-2024, regionalización descriptiva (paso 8). **Auditoría matemática hecha**: los 8 indicadores son correctos y consistentes con la literatura (ver `00 Proyecto/Auditoria - verificacion matematica de indicadores 2026-09-08.md`). **Entregables refrescados** y **presentación del protocolo ya expuesta** (2 versiones, HTML+PDF, en `13 Entregables`); skill `explicar-icr` y mapa conceptual Canvas creados. **Único pendiente del proyecto**: aceptar el control de cambios del PROTOCOLO (espera del asesor) — **NO aceptar**. **Opcional**: paso 6.6 (mejorar comparativa: China + Perú/Canadá + upstreamness). Seguir el log de [[Ruta - Completar indicadores y series (seguimiento)]].
>
> Avance 2026-09-06: **PASO 6 y C2 COMPLETADOS.** Paso 6 (OECD ICIO 2020; +2 países = Finlandia y Suecia) → `processed/icio_comparacion_mineria.csv` + memoria comparativa. C2 → Caps V-VIII regenerados por script con todos los hallazgos y las declaraciones de huecos (VII.5 referencia internacional; VIII.3/VIII.4 completas). **NO se tocó el control de cambios del PROTOCOLO.** Pendiente: pasos 7-8 (opcionales/aproximados). Ver log en [[Ruta - Completar indicadores y series (seguimiento)]].

## 1. Qué se está haciendo (contexto)
Se ejecuta, **punto por punto**, la ruta para completar los indicadores/series de la tesis (10 minerales críticos, 1992-2025). Ya se hicieron los pasos 1-5. **Faltan el paso 6 y la consideración C2.** Reglas firmes: **no imputar** (los huecos se declaran); los resultados "estimados" se calculan pero su uso lo decide el alumno; el **PROTOCOLO conserva control de cambios a la espera del asesor — NO aceptar**.

## 2. Estado (pasos 1-5, cerrados 2026-09-06)
- **P1 ✅ CCV** completado por **datos espejo**: 7 minerales 1992-2025 completos + plomo 33/34 (falta 1994, declarado); oro/plata sin CCV (artefacto de ley). Columna `fuente_numerador` (propio/espejo, caveat CIF). `processed/ccv_serie.csv`; scripts `ccv_fill_gaps.py`, `ccv_calc.py`. Memoria: `10 Datos/Memoria - CCV (...).md`.
- **P2 ✅ HHI 2024**: serie 2004-2024 (`processed/hhi_consolidado.csv`, `scripts/hhi_2024.py`). 8 minerales con 2024; **sílice/grafito 2024 declarados sin dato**; cobre total 2024 estimado (SGM da 777,106 t, corrobora).
- **P3 ✅ Destinos serie temporal 1992-2024** (`processed/comercio_destinos_serie_resumen.csv`; scripts `comercio_destinos_serie*.py`). Hallazgo: concentrados se desplazan a **China/Asia** (cobre E1: EUA 100% 1995 → China 94% 2022); HF a EUA. Huecos por reporte propio declarados (memoria georref §3.1/§3.2).
- **P4 ⛔ RAS — superado (opción A del alumno)**: RAS por mineral **inviable** (INEGI: MIP solo años base 2013/2018; COU anual ~263 ramas, minería agregada → sin marginales a nivel Clase). Cubierto por CCV (por mineral) + 3 cortes MIP + ICIO agregado (este paso 6). **No se hace RAS.**
- **P5 ✅ Georreferenciación cuantitativa**: `processed/georref_extraccion_mineral_estado_cuantitativo.csv` (producción 2024 por mineral×estado, del SGM Anuario 2025 leído como imagen) + `georref_transformacion_nodos.csv`. Extracción muy concentrada (Zacatecas metales; Sonora cobre/oro/grafito; SLP fluorita 96%; Hidalgo manganeso 100%; NL+Sonora barita; Coahuila+Puebla sílice).
- **+A ✅ Tarea grafito**: producción ↓ (2024 ≈2,150 t, −20%/año) y criticidad ↑, **sin paradoja** (México produce amorfo, no flake/batería; China monopoliza esférico/sintético). `05 Diagnostico Insumo-Producto/Nota - Grafito (...).md`.

## 3. PASO 6 — Comparación internacional (a ejecutar)
**Objetivo:** contrastar el encadenamiento hacia adelante de la **minería** de México con países de referencia, para poner a prueba la etiqueta de "casos de éxito".

**Consideración C1 (firme):**
1. Calcular también **México a nivel minería AGREGADA** (mismo nivel que los demás), para comparación **like-for-like**. (México por mineral ya está en `mip_encadenamientos_minerales.csv`; aquí se agrega a "minería".)
2. Países: **Chile y Australia** + **2 más** que la literatura tome como "caso de éxito". Candidatos (confirmar 2 con literatura al inicio del paso): **Finlandia, Suecia, Canadá, Noruega** (clúster minero-metalúrgico + servicios/tecnología). Sugerencia: Finlandia/Suecia (modelo nórdico) y/o Canadá.
3. **Orden de redacción**: PRIMERO la comparativa de encadenamientos de los **sectores minería** entre países; DESPUÉS la justificación de elegir los **10 minerales** y sus encadenamientos particulares.

**Método (recomendado):**
- Fuente comparable: **OECD ICIO** (edición reciente; ~45 industrias ISIC para ~76 países, incluye MEX, CHL, AUS, FIN, SWE, CAN, NOR; minería = B05_06 energía, B07 metal ores, B08 other mining). Para un Ghosh **doméstico comparable**, extraer el **bloque intra-país** de cada país (país c→país c), construir B (coef. de distribución) y **G=(I−B)⁻¹**, y tomar el encadenamiento hacia adelante (suma de fila normalizada) de las filas de minería. Replicar el método de `10 Datos/scripts/mip_calc.py` / `mip2008_calc.py` (A=Z/x col; B=Z/x fila; L=(I−A)⁻¹; G=(I−B)⁻¹; Rasmussen = fila/media).
- **Cuidado ICIO**: archivo grande. Bajar **una edición/año** y extraer solo los bloques domésticos necesarios (45×45 por país → invertir es trivial). Si ICIO no es accesible, usar MIP nacionales: **Banco Central de Chile** (MIP), **ABS** Australia (5209.0), **Stats Finland/SCB Suecia/StatCan/SSB Noruega** — más heterogéneo.
- **CAVEAT declarado**: la comparación es a **nivel sector-minería agregado, NO por mineral** (ICIO/MIP nacionales no separan cobre/zinc). Además base-año/clasificación distintas. Es válida como contraste, con ese caveat.

**Ya hecho (base para el paso 6):** `05 Diagnostico Insumo-Producto/Memoria - Comparacion internacional (Chile, Australia) encadenamientos.md` documenta extracción/transformación de Chile y Australia y la evidencia de literatura (Chile exporta ~94% de concentrado, enclave con encadenamientos débiles/decrecientes; Australia hacia atrás fuerte/METS, adelante débil). **Veredicto preliminar: ni Chile ni Australia son "éxito" en encadenamiento hacia adelante.** El paso 6 añade: (a) coeficientes computados (México agregado + los 4-5 países); (b) documentación de los 2 países nuevos; (c) tabla comparativa de coeficientes.

**Fuentes de literatura ya citadas** (en la memoria comparativa): Aroca 2018; Atienza et al. 2018; Weldegiorgis et al. 2024.

## 4. C2 — Integración a la redacción (después del paso 6)
Integrar **todos** los hallazgos en las memorias/capítulos, **incluyendo las declaraciones de lo que falta y cómo se intenta llenar cada hueco**. Insumos y destino:
- **Cap. V** (método+resultados encadenamientos): CCV completo (espejo, caveat CIF), §4bis cautela Ghosh (>1 ≠ cadena desarrollada), 3 cortes MIP.
- **Cap. VI** (tipología A/B/C/D): HHI 2004-2024, georreferenciación (extracción vs transformación), destinos (desplazamiento a China), grafito (amorfo vs criticidad).
- **Cap. VII/VIII** (contexto/política): comparación internacional (reencuadre del "éxito"), doble profundización del enclave (más crudo + más China), bases de política por eslabón ausente.
- **Declaraciones de huecos (obligatorias en el texto)**: HHI 2004-2024 (1994-2003 recuperable vía USGS Tabla 2 = paso 7 pendiente; 1992-93 no reconstruible); plomo 1994 sin CCV; oro/plata sin CCV (artefacto de ley); manganeso/plomo-zinc combinados en MIP; destino final Comtrade (socio declarado); comparación internacional agregada no por mineral; 2025 no publicado; RAS por mineral inviable.
- Refrescar entregables (infografía/decks/resumen) con los datos nuevos si el alumno lo pide (Artifacts: infografía ea144363, deck 9b3361d6, canvas 8c1c2e64; contract 0.1.31 para el canvas).

## 5. Datos y herramientas
- **Base MIP 2018 (Clase, doméstica)**: `10 Datos/Bases Originales/10 MIP INEGI/2018/conjunto de datos/` (`..._mip_d_pb_pxp_42018.csv` flujos; `..._mip_t_..._42018.csv` totales; `..._mip_ctec_...` A; `..._mip_cdi_...` L). Método en `scripts/mip_calc.py`.
- **Processed clave**: `mip_encadenamientos_minerales.csv` (Ghosh por mineral 2013/2018 + 2008 ref), `ccv_serie.csv`, `hhi_consolidado.csv` (2004-2024), `comercio_por_etapa_1992_2024.csv`, `comercio_posicion_1992_2024.csv`, `comercio_destinos_serie_resumen.csv`, `comercio_destinos_mineral_etapa.csv`, `georref_extraccion_mineral_estado_cuantitativo.csv`, `georref_transformacion_nodos.csv`.
- **Herramientas confirmadas**: `py` con `openpyxl`, `numpy`, `csv`, `matplotlib`, `python-docx`, `PIL`; **Comtrade API pública** funciona (patrón en `ccv_download.py`, con sleeps/429); **lectura de PDF como imagen** funciona (`pdftoppm -f N -l N -jpeg -r 130` + Read); **Node v24** instalado (para canvas Design). **No** hay pandas.
- **WebSearch/WebFetch** disponibles (deferred: cargar con ToolSearch `select:WebSearch,WebFetch`). ResearchGate/paywalls dan 403 en WebFetch (usar abstracts/otras fuentes).

## 6. Cómo arrancar el chat nuevo
Pega este mensaje:

> Continúo mi tesis (proyecto en `ICR/`, con su CLAUDE.md). Trabaja solo dentro de `ICR/`, usa `py`, diseño descriptivo, concepto ordenador = enclave estructural. La fuente única de verdad es `ICR/00 Proyecto/Handoff - Paso 6 (comparacion internacional) + C2 2026-09-06.md`. Léela COMPLETA (y la [[Ruta - Completar indicadores y series (seguimiento)]]) y, sin ejecutar aún, devuélveme un plan corto (2-3 frases) confirmando el paso 6 (comparación internacional: México agregado + Chile/Australia + 2 países de éxito; primero comparativa sectorial, luego justificación de los 10 minerales; caveat de agregación) y C2. Recién que apruebe, ejecutas. No aceptar el control de cambios del PROTOCOLO.

← [[Ruta - Completar indicadores y series (seguimiento)]] · [[Bitacora]] · [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]]
