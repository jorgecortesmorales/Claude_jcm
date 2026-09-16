---
title: Handoff — Reestructuración metodológica (columna vertebral industrial)
type: proyecto
tags: [icr, proyecto, handoff, metodologia]
created: 2026-07-22
updated: 2026-07-22
status: pendiente-ejecutar
---

# Handoff — bloque de modificaciones metodológicas (para ejecutar en un chat nuevo)

> [!important] Cómo usar esta nota
> Esta nota es la **fuente única de verdad** para ejecutar un bloque de cambios que quedó pendiente al terminarse el contexto de la conversación anterior. Contiene **(1) el porqué** (el arco intelectual y las decisiones tomadas), **(2) las 5 tareas** con rutas y cuidados exactos, y **(3) notas técnicas del entorno**. Léela completa antes de tocar nada. Todo el trabajo es **exclusivamente dentro de `ICR/`**.

---

## 1. POR QUÉ — el arco intelectual (leer para entender, no solo ejecutar)

### 1.1 De dónde venimos
El asesor (Dr. Micheli) hizo **cuatro observaciones** al protocolo (ver [[Guion Reunion Asesor - Observaciones]] para el detalle completo):
1. Anclar la relevancia en el **desarrollo industrial de México** (no en la criticidad vista desde EE.UU./UE).
2. La **aportación está en los datos y en la causalidad, no en el modelo** (el panel HHI→Ghosh, por sí solo, es asociación, no causa).
3. **La reforma de 2023 no da escala de tiempo** para analizar efectos estructurales.
4. Los **actores tradicionales (mineros) no son actores industriales**: te dirán por qué no invierten en extracción, no por qué no se industrializa aguas abajo.

Ya se generó (conversación previa): protocolo con control de cambios que responde a las 4 observaciones, un guion, la extracción de la Tabla 2 del USGS a `10 Datos/processed/myb_estructura_industria.csv`, y la corrección de la fusión de fluorita a **enero 2012** en `hhi_numeradores.csv` y en las notas del vault.

### 1.2 La decisión nueva de esta conversación (lo que hay que incorporar)
Discutiendo el rol del **event study / la reforma**, se llegó a una reestructuración que **complementa y resuelve** las observaciones 2 y 4. La idea central es una **columna vertebral con enfoque de desarrollo industrial**, articulada por una **pregunta única**:

> **¿Por qué México no industrializa aguas abajo de sus minerales críticos, y qué política lo corregiría?**

**El eslabón clave que antes faltaba — el puente oferta/demanda:**
El panel (Cap. VI) entrega un **número**: a mayor concentración (HHI), menor encadenamiento hacia adelante (Ghosh), β₁ < 0. Pero ese número admite **dos lecturas opuestas** que la econometría **sola no puede distinguir**:
- **Lectura A — falla de OFERTA (poder de mercado):** las empresas concentradas *pueden* integrarse pero *no quieren* (exportan en bruto y refinan afuera; p. ej. Grupo México refina cobre en EE.UU. vía ASARCO). ⇒ la concentración **causa** la baja industrialización. **Política:** regular competencia + condicionar concesiones a integrar.
- **Lectura B — falla de DEMANDA:** los minerales concentrados son también los que **no tienen industria compradora** en México, por razones ajenas a la concentración. ⇒ la concentración es **solo correlación**. **Política:** fomentar la industria transformadora doméstica.

El **análisis documental/de escritorio** es exactamente lo que **decide entre A y B**: no es un estudio paralelo, es el **intérprete** del panel, y **la recomendación de política industrial depende de cuál sea**. Esto ya está latente en el protocolo como diseño **secuencial explicativo** (Creswell y Clark): la fase cuantitativa arroja el resultado y la cualitativa **explica el mecanismo**. Ahora se hace **explícito**.

**Cómo se contesta A vs B SIN depender de entrevistas** (resuelve la restricción de tiempo del alumno y la obs. 4):
- **Matriz insumo-producto (Cap. V):** dice si **existe** demanda doméstica aguas abajo de cada mineral (si la casilla es ~0, es falla de demanda).
- **Datos de comercio (BACI/Comtrade, ya importados en `10 Datos/Bases Originales/04 Comercio Exterior`):** la huella de reprimarización (exportar bruto / importar procesado) por mineral.
- **Reportes públicos de empresas** (informes anuales/MD&A, transcripciones de *earnings calls*): dónde refinan/procesan; qué dicen de integrar.
- Metodológicamente legítimo: el *process tracing* (Beach y Pedersen) y el análisis temático (Braun y Clarke) **operan sobre evidencia documental**, no solo sobre entrevistas. **Las entrevistas quedan como complemento opcional**, no como pieza de carga.

**El rol de la reforma (Cap. VII) baja a SECUNDARIO:**
- El event study mide "reforma → valuación/inversión", que **no habla directamente de industrialización** y cuyo signo es **obvio** (la inversión cayó; ya está descrito con IED −56.3% y exploración −11.5%). Su único aporte no-obvio es la **asimetría** (¿golpea más a entrantes que a incumbentes? → ¿la reforma **fija** la estructura oligopólica?), pero es **empíricamente frágil** porque los entrantes casi no cotizan.
- Nexo legítimo con el hilo central: la reforma prueba la **rama institucional** y muestra si la palanca de política **refuerza la estructura concentrada** que el Cap. VI liga con la baja industrialización. **No prueba la industrialización.**
- **Decisión abierta (consultar con el usuario/asesor): A) quitar la reforma del todo** (implica reescribir Objetivo 3 y H4 — cambio estructural), **o B) dejarla ligera y de escritorio** (análisis documental de reportes/earnings calls + análisis jurídico diferencial de la reforma; event study como pierna menor de triangulación, reencuadrado en magnitud/asimetría, no en el signo). **El usuario se inclina por B.** Ejecutar como B salvo indicación contraria, dejando la opción A señalada.

### 1.3 La columna vertebral (el hilo que todo debe respetar)
**Cap. V** (mide el hueco: Ghosh bajo + tamaño de demanda doméstica; H2 vs Chile/Australia) → **Cap. VI** (panel HHI→Ghosh: la concentración está *asociada* con el hueco; + **quiebres estructurales fechados** para causalidad: fluorita ene-2012, huelga de Cananea 2007-2010, grafito monopolio 2014) → **puente documental oferta/demanda** (interpreta el panel; bifurca la política) → **Cap. VIII** (qué falla domina → recomendación de política industrial diferenciada). La **reforma (Cap. VII)** es una nota al margen que muestra que la palanca institucional actual empuja en contra.

---

## 2. LAS 5 TAREAS (qué hacer)

### Tarea 1 — Actualizar los Word más recientes de capítulos + el protocolo con este enfoque
- Archivos: `11 Redaccion/Cap V - Diagnostico Insumo-Producto.docx`, `Avance Cap VI - Base B5 HHI (2026-07-20).docx`, `Cap VII - Impacto Reforma 2023.docx`, `Cap VIII - Sintesis y Conclusiones.docx` (y las notas `.md` de andamiaje correspondientes en `11 Redaccion/`).
- Insertar/ajustar **la columna vertebral y el puente oferta/demanda** de §1.2–1.3, con la **metodología muy clara**. En el Cap. VI, dejar explícito que el panel es **asociación** y que la causalidad se apoya en los quiebres fechados + el puente documental. En el Cap. VII, reencuadrar a **secundario/desk-based** (opción B) con la asimetría/entrenchment como único aporte no-obvio.
- **Mantener lo que ya funciona; cambiar/añadir solo lo necesario.** Evitar redacción "de IA" verbosa.
- Formato consistente con los Word existentes: Times New Roman 12, carta, márgenes ≈3 cm.

### Tarea 2 — Rehacer el protocolo con control de cambios (CUIDADO FINO)
- **Base**: partir del **limpio** `00 Proyecto/Documentos Originales/Protocolo/Protocolo ICR - Cortes Morales - UAM Azcapotzalco vfinal.docx` (el documento *anterior* al que ya tenía marcas).
- **Antes de escribir**, **revisar** `00 Proyecto/Documentos Originales/Protocolo ICR - correcciones asesor (control de cambios).docx` (el que el usuario editó) para ver **qué recortó el usuario** de mis inserciones previas: usar **su redacción recortada** como base, **no repetir redundancias ni repeticiones** que él eliminó. (Word ya está cerrado; se puede copiar y leer. Para ver el texto "aceptado" de ese archivo: recorrer el XML y tomar los `w:t` que **no** estén dentro de un `w:del`.)
- Aplicar como **control de cambios fresco sobre el vfinal**: los cambios por las 4 observaciones (versión recortada del usuario) **+** los cambios nuevos de §1.2–1.3 (puente oferta/demanda como intérprete del panel; cualitativo desk-based con entrevistas opcionales; reforma secundaria; enfoque de desarrollo industrial). **No cambiar lo que ya funciona.**
- **Versionado claro y diferenciado**: nombrar el archivo nuevo distinto, p. ej. `Protocolo ICR - v2 correcciones asesor + metodologia (control de cambios).docx`. **No sobrescribir** el archivo que el usuario editó. Dejar constancia (en esta nota o en [[Bitacora]]) de qué versión es cuál:
  - `...vfinal.docx` = original aprobado (limpio).
  - `...correcciones asesor (control de cambios).docx` = 1ª ronda (4 observaciones), editada por el usuario.
  - `...v2 correcciones asesor + metodologia (control de cambios).docx` = 2ª ronda (observaciones recortadas + puente oferta/demanda), **nueva**.
- Técnica de control de cambios: `w:ins`/`w:del` vía `python-docx`+`OxmlElement`/`qn` (helper probado: para reemplazar un párrafo, envolver los `w:r` viejos en un `w:del` convirtiendo `w:t`→`w:delText` y anexar un `w:ins` con el texto nuevo; para insertar párrafo nuevo, crear `w:p` con `w:ins` y marcar la marca de párrafo como insertada en `pPr/rPr/ins`). Autor sugerido: "Revision metodologica 2026-07-22". Verificar reconstruyendo las versiones "aceptada" y "rechazada".

### Tarea 3 — Diagrama de flujo (algoritmo) de la columna vertebral
- **Doble entregable**: (a) **Mermaid** dentro de una nota `.md` (se ve en Obsidian) y (b) **PDF** limpio para consultar fuera. **Herramientas del entorno: `matplotlib` SÍ (PDF vectorial), `graphviz`/`reportlab`/`cairosvg` NO.** Generar el PDF con matplotlib (cajas + flechas) o exportando un SVG propio; NO depender de graphviz.
- **Contenido del diagrama** (respetar §1.3): Pregunta central (desarrollo industrial) → dos fallas candidatas (mercado / institucional) → **Cap. V** (mide hueco + demanda doméstica; H2) → **Cap. VI** (panel HHI→Ghosh β₁<0 + quiebres fluorita 2012 / Cananea / grafito 2014) → **puente oferta/demanda** con **bifurcación**: [Oferta→política de competencia+integración] / [Demanda→política de fomento industrial] → **Cap. VIII** (recomendación). **Reforma (Cap. VII)** como caja lateral secundaria ("¿afloja o fija la estructura?"). Incluir las fuentes por paso. Diseño **limpio, legible, sin saturar**.
- Ubicación sugerida: `06 Metodologia y Modelo de Panel/` (nota .md con Mermaid) y el PDF en la misma carpeta. Enlazar desde [[Home]] y desde el índice de metodología.

### Tarea 4 — Descripción muy clara y completa de los pasos metodológicos
- Nota `.md` en `06 Metodologia y Modelo de Panel/` (p. ej. `Columna Vertebral Metodologica.md`), enlazada al diagrama de la Tarea 3. **Muy clara y completa**: cada paso (Cap. V, Cap. VI, puente oferta/demanda, Cap. VII, Cap. VIII), **su importancia y su conexión** con el siguiente, el enfoque de desarrollo industrial, y cómo el puente oferta/demanda traduce el número del panel en una conclusión de política. Incluir el **ejemplo de la fluorita de punta a punta** (Cap. V: encadenamiento bajo + casi sin industria de HF; Cap. VI: concentrada + quiebre 2012; puente: ¿Orbia decide no integrar o no hay industria fluoroquímica?; conclusión de política según A/B).

### Tarea 5 — Barrido de consistencia de todo el proyecto
- Revisar **todas las carpetas y archivos** y verificar que estén actualizados y consistentes con: (a) fluorita = **duopolio hasta 2011 / monopolio de grupo desde ene-2012** (no 2013); (b) **grafito NO atomizado** (decisión abierta C-17: el USGS solo lista 1-2 productores; desde 2014 monopolio de Grafitos Mexicanos); (c) el **enfoque de desarrollo industrial** y el **puente oferta/demanda**; (d) la **reforma secundaria** y las **entrevistas opcionales**. Buscar y corregir referencias viejas ("enero 2013", "duopolio hasta 2012", "grafito atomizado/fragmentado", reforma como pieza central, HHI fluorita ~9,600). Enlazar las notas nuevas desde [[Home]] y los índices.

---

## 3. NOTAS TÉCNICAS DEL ENTORNO (para no tropezar)
- **Python**: usar el lanzador **`py`** (el alias `python` abre la Microsoft Store y falla). `python-docx`, `matplotlib`, `PIL` disponibles; `graphviz`/`reportlab`/`cairosvg` NO.
- **Validar CSVs** con `py` + módulo `csv` (contar columnas), **NO con `awk -F,`** en `myb_estructura_industria.csv` (tiene comas dentro de campos entrecomillados → falsos positivos). En `hhi_numeradores.csv` sí aplica `awk -F, 'NF!=14'` (se saneó para que no tenga comillas/comas internas).
- **PDFs del USGS**: leer las tablas **en imagen** (Read sobre el PDF); `pdftotext` solo para localizar páginas.
- **Convención CAMIMEX**: el Informe Anual del año N reporta el año-dato **N−1** (esto causó el error de fecha de fluorita).
- **Word/lock**: no escribir sobre un `.docx` abierto (aparece `~$...`). Ya está cerrado, pero verificar antes de sobrescribir; ante la duda, usar nombre nuevo.

## 4. EVENT STUDY PRELIMINAR (ya corrido — insumo para Cap. VII, opción B)
- **Fuente**: cierres diarios ajustados de **Yahoo Finance** (API `query1.finance.yahoo.com/v8/finance/chart`), tickers `GMEXICOB.MX`, `PE&OLES.MX`, índice `^MXX` (IPC). Evento t0 = aprobación en Diputados **~20-21 abril 2023** (iniciativa 24-mar; Senado 29-abr; DOF 8-may). Modelo de mercado sobre el IPC; ventana de estimación 28-sep-2022 a 4-abr-2023 (130 días).
- **Resultados**: Grupo México AR **−4.07%** el día de la votación (t=−1.64, 10%) y **−4.73%** tras entrada en vigor (t=−1.90, 10%); CAR[−1,+10] ≈ **−8.3%** (no signif. al 5% con una sola acción). Peñoles más ruidosa. **Lectura**: la tubería funciona y hay señal económica del signo correcto; la significancia requiere **agrupar empresas en cartera** y el contraste entrantes vs. establecidos. **Limitación**: Grupo México pesa mucho en el IPC (sesga β). *(No se guardó el script; reproducible con lo anterior.)*

## 5. PUNTEROS
- [[Guion Reunion Asesor - Observaciones]] · [[Ediciones Pendientes Documentos Word]] (lote 2026-07-21, C-16 a C-19; C-17 = decisión grafito) · [[Bitacora]] (entradas 2026-07-21) · [[Indice de Redaccion Word]].
- Datos: `10 Datos/processed/hhi_numeradores.csv` (493 filas), `10 Datos/processed/myb_estructura_industria.csv` (816 filas), `10 Datos/Bases Originales/04 Comercio Exterior/` (comercio para el puente oferta/demanda).
- Protocolo: `00 Proyecto/Documentos Originales/` (vfinal limpio; correcciones-asesor editado por el usuario; con-comentarios-del-profesor).

← [[Home]] · [[Protocolo Aprobado]]
