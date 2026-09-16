---
title: Mapa del Proyecto
type: moc
tags: [icr, moc, mapa]
created: 2026-07-16
updated: 2026-09-16
status: activo
---

# 🗺️ Mapa del Proyecto — dónde vive cada cosa

> [!info] Los mercados de los minerales críticos en México, 1992-2025
> **Diseño descriptivo**; concepto ordenador = **enclave estructural**. Para el mapa **visual** abre [[Mapa Visual del Proyecto]] (canvas). Para el **avance** por capítulo/actividad, [[Estructura y Cronograma de la ICR]].

> [!tip] Cómo está organizado el vault (nueva estructura, sep-2026)
> El **documento** se rige por [[Arquitectura del documento (estructura expositiva)]] (9 capítulos). Las carpetas numeradas `01`–`09` conservan las **notas de trabajo** históricas; el **manuscrito final** vive en `11 Redaccion/manuscrito/`.

## ① Fundamentos y navegación
- [[Home]] — portada del vault
- [[CLAUDE]] — rol, alcance y reglas del proyecto
- [[Estructura y Cronograma de la ICR]] — **tablero maestro** de avance (plan vs. real)
- [[Mapa Visual del Proyecto]] — mapa mental (canvas)
- **Gestión** → `00 Proyecto/Gestion y seguimiento/`: handoffs, [[Bitacora]], cronograma, rutas y planes
- **Metodología y auditoría** → `00 Proyecto/Metodologia y auditoria/`

## ② Planteamiento — `01 Planteamiento/`
- [[Pregunta de Investigacion]] · [[Objetivos]] · [[Hipotesis]] · [[Justificacion]] · [[Estructura de la Tesis]]

## ③ Marco teórico — `02 Marco Teorico/`
- [[Definiciones - Mineral Critico]] · [[Corpus de Diez Minerales]] · [[Clasificacion de productos por criticidad]] · [[Marco Teorico - Tres Tradiciones]]

## ④ Metodología e indicadores — `00 Proyecto/Metodologia y auditoria/`
- [[Arquitectura del documento (estructura expositiva)]] — estructura expositiva del documento
- [[Auditoria de indicadores (justificacion, matematica, limites)]] — los ~50 indicadores, uno por uno
- [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]] · [[Recomendaciones de lectura por capitulo]]

## ⑤ Datos y memorias
- [[Catalogo de Bases de Datos]] (`10 Datos/`) — inventario de bases; `processed/` = indicadores; `scripts/` = cálculo
- **Memorias de indicadores** (`05 Diagnostico Insumo-Producto/` y `10 Datos/`):
  - [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]]
  - [[Memoria - Encadenamientos por eslabon (extraccion, refinacion, semimanufactura)]]
  - [[Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)]]
  - [[Memoria - Comercio por etapa de procesamiento (Obj 3)]]
  - [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]]
  - [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]]
  - [[Memoria - Peso del bloque de 10 minerales (PIB, exportaciones, empleo)]]

## ⑥ Manuscrito y entregables
- **Manuscrito (nueva estructura)** → `11 Redaccion/manuscrito/` (fuentes Markdown) → `ICR - Manuscrito (nueva estructura).docx`
  - I Introducción · II Marco · III Metodología · IV Contexto · V Estructura · VI Encadenamientos · VII Inserción global · VIII Tipología · IX Síntesis · Anexos B/C/D
  - Pipeline: `11 Redaccion/pandoc/build_book.py` (reproducible)
- [[Resumen descriptivo de la investigacion (datos e indicadores)]]
- **Bibliografía** → [[Bibliografia]] (`12 Referencias/`)
- **Entregables visuales** → `13 Entregables/` (mapas, infografías, presentaciones)

← [[Home]] · [[CLAUDE]] · [[Estructura y Cronograma de la ICR]]
