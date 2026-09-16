---
title: Handoff — Fase de datos (cadenas de valor)
type: proyecto
tags: [icr, proyecto, handoff, cadenas-de-valor, datos]
created: 2026-07-23
updated: 2026-07-23
status: pendiente-ejecutar
---

# Handoff — Fase de datos (cadenas de valor) · para el chat nuevo

> [!important] Fuente única de verdad para arrancar la fase de datos del diseño **descriptivo**. Léela completa antes de tocar nada. Todo el trabajo es **dentro de `ICR/`**. Usar el lanzador **`py`** (no `python`).

## 1. Dónde estamos (contexto imprescindible)
La ICR pivotó de un diseño **causal** (panel HHI→Ghosh) a uno **descriptivo de cadenas de valor** (giro 2026-07-23; ver [[Bitacora]]). Se **describe**, no se busca causa. **Aporte = construir las bases de datos e indicadores y usarlos para describir.** Regla de oro: **descripciones objetivas y honestas, sin forzar relaciones ni casos.**

- **Protocolo vigente**: `Documentos Originales/Protocolo/Protocolo ICR - vfinal (revision consistencia descriptiva).docx` (+ PDF). Razonamiento en [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]]. Versiones viejas en `Documentos Originales/Archivo - versiones anteriores del protocolo/`.
- **Caps I-IV**: `Documentos Originales/Caps I-IV Cortes Morales.docx` **ya adaptado al diseño descriptivo y aceptado** (limpio). La línea causal quedó en `Archivo…/Caps I-IV (linea causal).docx`.
- **Método**: [[Columna Vertebral Metodologica]] + [[Diagrama - Columna Vertebral Metodologica]]. **Inventario de activos**: [[Auditoria - Que sigue sirviendo]]. **Navegación**: [[Mapa del Proyecto]].
- Vault alineado: planteamiento (pregunta/objetivos/hipótesis), Cronograma, Marco Teórico (Tres Tradiciones + cadenas de valor globales), Corpus, actividades (Tablero), Home, `CLAUDE.md`.

## 2. Diseño en una frase
Caracterizar los mercados de los 10 minerales críticos —**estructura extractiva + industria de transformación**— y la **inserción de México en las cadenas de valor (locales y globales)**, como bases para una política industrial. 3 objetivos: (1) estructura extractiva (HHI) + encadenamientos (Ghosh/CCV); (2) cadenas de valor locales; (3) inserción en CVG. Reforma = contexto. Litio fuera. Sin caso de contraste único (C-17 resuelto: describir el espectro; barita = hallazgo).

## 3. Tareas de la fase de datos (qué hacer)
1. **MIP INEGI** — obtener y depurar las Matrices Insumo-Producto (cortes 2003, 2008, 2012, 2018; RAS 2020/2023). Calcular por mineral: **Leontief** (hacia atrás), **Ghosh** (hacia adelante), **CCV** e índices **Hirschman-Rasmussen**. Además, extraer la **demanda intermedia doméstica** de cada mineral (insumo del Objetivo 2: ¿hay sectores compradores?). *(Correspondencia rama SCIAN ↔ mineral; tratar coextracción.)*
2. **Comercio por etapa (Objetivo 3)** — con BACI/Comtrade (HS 6 dígitos, ya en `10 Datos/Bases Originales/04 Comercio Exterior`), clasificar por **etapa de procesamiento** (mena → concentrado → refinado → intermedio → bien final) y describir la posición de México: participación por etapa, **dependencia de importaciones** procesadas, análisis espejo (exportar bruto / importar procesado). Alternativa analítica abierta (según datos): upstreamness/downstreamness (Antràs-Chor) y participación TiVA/ICIO (OECD).
3. **Empresas de transformación (Objetivo 2)** — identificar, a nivel de empresa, procesadores/usuarios domésticos de los minerales extraídos en México (directorios, reportes). ¿Existe cadena local?
4. **Cap. VI reconvertido** — de "modelo de panel" a **caracterización/tipología descriptiva** de los 10 mercados (HHI + Ghosh + posición GVC). Reescribir el Word `11 Redaccion/Avance Cap VI…` (o renombrarlo).
5. **Reencuadre de los Word Caps. V, VII, VIII** — hoy tienen el enfoque causal del bloque previo ("puente causal"): Cap. V → descripción de encadenamientos + cadena local; Cap. VII → reforma como contexto (event study opcional); Cap. VIII → síntesis + bases de política. *(Marcados con aviso; ver [[Auditoria - Que sigue sirviendo]].)*
6. **Notas de método del vault** aún causales: [[Modelo Econometrico]], [[Variables y Datos]] e índices de Caps. V/VII/VIII — reescribir al marco descriptivo al tocar cada capítulo.

## 4. Datos ya disponibles (no recolectar desde cero)
- `10 Datos/processed/hhi_numeradores.csv` (493 filas) — **HHI** por mineral-año. ✔
- `10 Datos/processed/myb_estructura_industria.csv` (816 filas) — estructura de la industria (USGS Tabla 2). ✔
- `10 Datos/processed/precios_usgs_anual_empalmado.csv` — precios/valores unitarios. ✔
- `comercio_exterior_2015_2024.csv` + `Bases Originales/04 Comercio Exterior` — insumo del comercio por etapa. ✔
- Inventario completo y estado: [[Catalogo de Bases de Datos]] y [[Memoria Metodologica de Bases de Datos]].

## 5. Cuidados técnicos (para no tropezar)
- **`py`** (no `python`). Disponibles: `python-docx`, `matplotlib`, `PIL`, `faster-whisper`, `av`, `csv`. NO: `graphviz`/`reportlab`/`cairosvg`.
- **Validar CSVs** con `py`+`csv` (contar columnas). En `myb_estructura_industria.csv` **no** usar `awk -F,` (comas dentro de comillas → falsos positivos).
- **Word con control de cambios** (`w:ins`/`w:del` vía python-docx + OxmlElement/qn); autor y fecha; **verificar reconstruyendo aceptada y rechazada** (rechazar todo debe dar el original exacto). No sobrescribir; versionar y archivar lo viejo.
- **Diagramas**: Mermaid en `.md` + PDF con **matplotlib** (cajas + flechas), revisar el PDF para evitar solapes.
- **Notas de voz**: no oigo audio; transcribir local con `faster-whisper large-v3` y **mostrar la transcripción para verificar** antes de actuar (ver [[transcribir-notas-voz]] en memoria).
- **CAMIMEX**: el Informe Anual del año N reporta el año-dato **N−1**.
- **USGS MYB Tabla 2**: leer **en imagen**; no hay Tabla 2 para 2017 ni 2020; sílice ausente.

## 6. Decisiones firmes (no reabrir sin el usuario)
- Diseño **descriptivo** (no causal). HHI/Ghosh = **descriptores**.
- **Sin caso de contraste único** (C-17 resuelto); describir el espectro; **barita** = hallazgo de concentración decreciente.
- Reforma 2023 = **contexto** (propósito: soberanía/anti-especulación, no industrialización). Event study **opcional**.
- **Litio/LitioMx fuera**. Comparación Chile/Australia **opcional**.
- Fluorita: duopolio hasta 2011 / monopolio de grupo desde **ene-2012**. Grafito: **concentrado** (duopolio→monopolio 2014), no atomizado. Sílice: concentrada.
- **Título del protocolo**: se deja como está (decisión del usuario).

## 7. Estilo de trabajo
Redacción académica sin "voz de IA", solo lo necesario. Validar cada entregable. Actualizar la [[Bitacora]] al cerrar cada tarea. Handoff antes de agotar contexto.

← [[Home]] · [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]] · [[Auditoria - Que sigue sirviendo]] · [[Mapa del Proyecto]]
