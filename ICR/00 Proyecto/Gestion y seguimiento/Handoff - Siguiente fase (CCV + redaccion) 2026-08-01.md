---
title: Handoff — Siguiente fase (serie CCV + redacción)
type: proyecto
tags: [icr, proyecto, handoff, cadenas-de-valor, ccv, redaccion]
created: 2026-08-01
updated: 2026-08-01
status: pendiente-ejecutar
---

# Handoff — para el chat nuevo (2026-08-01)

> [!important] Fuente única de verdad para continuar. Léela completa antes de tocar nada. Todo el trabajo es **dentro de `ICR/`**. Usar el lanzador **`py`** (no `python`). El diseño es **descriptivo (cadenas de valor)**, concepto ordenador = **enclave estructural**.

## 1. Dónde estamos
- **Fase de datos COMPLETA** (los 3 objetivos) + **HHI consolidado cerrado**.
- **Redacción**: Caps. I-IV, V, VI, VII y VIII en forma **descriptiva**, con **cambios aceptados** por el alumno. **Único pendiente de control de cambios: el PROTOCOLO** (lo deja con marcas a propósito, para revisión del **asesor** — **NO aceptar** hasta su visto bueno).
- Concepto teórico: **enclave estructural** (desconexión aguas abajo con capital nacional; neo-extractivismo, Svampa), al que se llega **por contraste** con el enclave clásico de propiedad (Cardoso-Faletto). Ver [[Marco Teorico - Tres Tradiciones]] y [[Propuesta - Reestructuracion Cap II (marco articulado enclave)]].

## 2. Lo que sigue (tareas)
1. **PRINCIPAL — construir el CCV (coeficiente de captura de valor) como SERIE ANUAL mineral-año 1992-2025.** Es el **único indicador de serie que el protocolo diseña y que falta** (Diseño Metodológico: *"datos anuales continuos desde 1992 → hasta 320 observaciones"*; *"CCV = precio exportación frontera (Comtrade) / precio producto refinado destino (USGS)"*). Es la segunda operacionalización del encadenamiento hacia adelante (el Ghosh es discreto, atado a los cortes MIP).
   - **Insumos ya disponibles**: (a) **valor unitario de exportación** = valor/peso de las fracciones de exportación en bruto (E1) por mineral, de **UN Comtrade** (la descarga 2015-2024 está en `10 Datos/Bases Originales/11 Comercio Comtrade/`; para 1992-2014 **re-descargar** Comtrade México, reporter 484, flujo X, netWgt, por las HS E1 — API pública `preview`, sin clave, con rate limit ~1/s); (b) **precio del producto refinado** = `10 Datos/processed/precios_usgs_anual_empalmado.csv` (USGS, anual, 1992-2025). Correspondencia mineral↔HS(E1)↔producto USGS: usar `10 Datos/processed/concordancia_hs_etapa.csv`.
   - CCV = valor unitario exportación (frontera, bruto) ÷ precio producto refinado (destino), por mineral-año. Guardar en `10 Datos/processed/ccv_serie.csv` + memoria.
2. **Completar el HHI consolidado 2004-2020** (hoy solo 2021-2023; los numeradores/participación del líder existen 2004-2024 en `hhi_numeradores.csv`). Método documentado en la [[Bitacora]] (2026-08-01): participación de grupo vs. producción nacional, residual atomístico, monopolios=10,000.
3. **Opcionales**: comercio bilateral por socio (destinos/orígenes); extender comercio por etapa pre-2015; revisar la **caída de exportación de HF 2018→2023** (161→6.5 MM USD, posible cambio de fracción HS); cuantificar tamaño de las industrias usuarias.
4. **Protocolo**: cuando el asesor dé el visto bueno, aceptar los cambios (`Documentos Originales/Protocolo/Protocolo ICR - vfinal (consistencia PIJCM - control de cambios).docx`).

## 3. Indicadores ya construidos (no recalcular; rutas)
En `10 Datos/processed/`:
- `hhi_numeradores.csv` (participación/numeradores 2004-2024) · `hhi_consolidado.csv` (HHI por grupo 2021-2023).
- `mip_encadenamientos_minerales.csv` (Leontief, Ghosh, Hirschman-Rasmussen, DI/VBP; 2013 y 2018) · `mip_demanda_intermedia_minerales.csv`.
- `comercio_por_etapa.csv` · `comercio_posicion_resumen.csv` · `concordancia_hs_etapa.csv` (2015-2024).
- `empresas_transformacion.csv` (19 firmas, cadena local, con `fuente`).
- `precios_usgs_anual_empalmado.csv`, `myb_estructura_industria.csv`, `precios_consolidados_mensual.csv`.
Scripts en `10 Datos/scripts/`: `mip_calc.py`, `comercio_etapa.py`, `comercio_summary.py`, `build_capV.py`, `build_capVI.py`.
Memorias: [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] (05), [[Memoria - Comercio por etapa de procesamiento (Obj 3)]] (10 Datos), [[Memoria - Empresas de transformacion (Obj 2 - cadena local)]] (10 Datos), fichas en [[Fichas - Empresas de transformacion (Obj 2)]] (09).

## 4. Cobertura temporal de los indicadores (contexto de la Tarea 1)
- **Serie multi-año**: HHI (numeradores 2004-2024; consolidado 2021-2023), comercio por etapa (2015-2024).
- **Dos cortes (por diseño)**: encadenamientos MIP (2013, 2018).
- **Foto única**: empresas de transformación / cadena local.
- **Falta como serie continua**: el **CCV** (1992-2025) → Tarea 1 de arriba.

## 5. Capítulos (rutas y estado) — `11 Redaccion/`
- **Cap. V**: `Cap V - Calculo de encadenamientos MIP (metodo y resultados).docx` (principal, con fórmulas y resultados) + `Cap V - Diagnostico Insumo-Producto.docx` (andamio reencuadrado).
- **Cap. VI**: `Cap VI - Caracterizacion de los mercados (tipologia descriptiva).docx` — productos por las 4 fases + los 3 indicadores (HHI/Ghosh/comercio) + tipología A/B/C/D.
- **Cap. VII / VIII**: reencuadrados (contexto / tipología descriptiva).
- **Caps. I-IV**: `Documentos Originales/Caps I-IV Cortes Morales.docx` (con marco del enclave estructural, aceptado).
- Andamios viejos en `11 Redaccion/Archivo - andamios previos/` y `Documentos Originales/Archivo - versiones anteriores del protocolo/`.
- Índice: [[Indice de Redaccion Word]]. **Nota**: si algún capítulo necesita pasar de "documento con resultados/andamio" a **prosa de tesis completa**, es trabajo pendiente de redacción.

## 6. Decisiones firmes (no reabrir sin el usuario)
- Diseño **descriptivo**; HHI/Ghosh/CCV = **descriptores**. **Enclave estructural** (no de propiedad).
- **Litio fuera**. Sin caso de contraste único (barita = concentración decreciente, confirmada por el HHI). Reforma 2023 = **contexto**. Comparación Chile/Australia **opcional**.
- **Plomo-zinc** comparten clase en la MIP (coextracción) → Ghosh/DI conjuntos.
- MIP: solo **2013 y 2018** (datos abiertos; 2003/2008/2012 no comparables).
- **Corrección fluorita**: la cadena fluoroquímica **SÍ existe** (Koura, mayor planta de HF del mundo, Matamoros); llega al HF, se trunca antes de los fluoropolímeros (importados). Ya corregido en memorias, columna vertebral y Cap. V.

## 7. Cuidados técnicos (para no tropezar)
- **`py`** (no `python`). Disponibles: `python-docx`, `lxml`, `numpy`, `matplotlib`, `PIL`, `csv`, `faster-whisper`. **NO**: `node`/`pptxgenjs`, `pandoc`, LibreOffice, comando `zip`. Para empaquetar `.docx` usar **`zipfile` de Python** (incluir `[Content_Types].xml` primero).
- **Word con control de cambios** vía `python-docx`/`lxml` (`w:ins`/`w:del`, marca del fin de párrafo en `pPr/rPr`); **verificar reconstruyendo aceptada y rechazada** (rechazar todo = original exacto). No sobrescribir; versionar/archivar.
- **Renderizar `.docx` a PDF** con **Word COM** (PowerShell): `ExportAsFixedFormat($pdf,17,...,7)` con `ShowRevisions=$true` para ver las marcas; luego `pdftoppm` + leer imágenes.
- **Caps. V/VII/VIII** en **ASCII sin acentos** (convención de esos Word) — respetarla al editar.
- **Comtrade**: API pública `https://comtradeapi.un.org/public/v1/preview/C/A/HS` (sin clave), tomar la fila `motCode=0` (total); rate limit ~1/s (throttling + reintento en 429).
- **Validar CSVs** con `py`+`csv`. **CAMIMEX**: Informe del año N = año-dato N−1. **USGS MYB Tabla 2**: leer en imagen; sin Tabla 2 para 2017/2020.
- Actualizar la [[Bitacora]] al cerrar cada tarea.

## 8. Al arrancar el chat nuevo
NO ejecutar de inmediato: leer esta nota + [[Bitacora]] (entradas 2026-08-01), confirmar en el chat un plan corto (1-2 frases por: CCV serie, HHI 2004-2020, opcionales) y por dónde empezar (sugerido: **CCV**), y esperar aprobación.

← [[Home]] · [[Mapa del Proyecto]] · [[Columna Vertebral Metodologica]] · [[Catalogo de Bases de Datos]]
