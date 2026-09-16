---
title: Índice de Redacción en Word (Caps. V-VIII)
type: redaccion
tags: [icr, redaccion, indice]
created: 2026-07-21
updated: 2026-07-22
status: activo
---

# Ruta de los documentos Word — redacción por capítulo

Desde el **Capítulo V** cada capítulo tiene **su propio archivo `.docx`**, todos en esta carpeta `11 Redaccion/`. Los Caps. I-IV siguen en un solo archivo (`00 Proyecto/Documentos Originales/Caps I-IV Cortes Morales.docx`), porque ya están redactados como bloque; los ajustes pendientes sobre ese bloque viven en [[Ediciones Pendientes Documentos Word]].

| Cap. | Archivo Word (en `11 Redaccion/`) | Estado | Nota de andamiaje (Obsidian) |
|------|-----------------------------------|--------|------------------------------|
| V — Diagnóstico Insumo-Producto | `Cap V - Calculo de encadenamientos MIP (metodo y resultados).docx` ✅ **con resultados** (documento principal) · `Cap V - Diagnostico Insumo-Producto.docx` (andamio reencuadrado, descriptivo) | Método (Leontief/Ghosh/Hirschman-Rasmussen, con fórmulas) + resultados por mineral + demanda intermedia doméstica. Base MIP INEGI 2013/2018, validado vs INEGI. | [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] · [[Indice Diagnostico Insumo-Producto]] |
| VI — Caracterización de los mercados (tipología descriptiva) | `Cap VI - Caracterizacion de los mercados (tipologia descriptiva).docx` ✅ **reconvertido** (ya no es "modelo de panel") | Tipología descriptiva de los 10 mercados: productos por las 4 fases de la CV + HHI + Ghosh + posición comercial + cadena local, integrando Obj. 1-3. | [[Memoria - Empresas de transformacion (Obj 2 - cadena local)]] · [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] |
| VII — Reforma 2023 (contexto) + referencia internacional | `Cap VII - Impacto Reforma 2023.docx` ✅ **con C2 integrado** (generado por `build_capVII.py`) | Reforma como **contexto institucional** (no impacto causal); event study **opcional**; **VII.5 nueva**: referencia internacional (OECD ICIO 2020, reencuadre del "éxito"). | [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]] |
| VIII — Síntesis y Conclusiones | `Cap VIII - Sintesis y Conclusiones.docx` ✅ **con C2 integrado** (generado por `build_capVIII.py`) | VIII.2 tipología A/B/C/D; **VIII.3 recomendaciones** (diferenciadas + contrafactual nórdico) y **VIII.4 declaración de vacíos** ahora completas. | [[Ruta - Completar indicadores y series (seguimiento)]] |

> [!note] Reorganización (2026-08-01)
> Los cambios de Caps. V, VII y VIII se **aceptaron** y los archivos vigentes quedaron con **nombre canónico** (sin sufijo). Los andamios previos (causales) se movieron a `11 Redaccion/Archivo - andamios previos/` (Cap. V/VII/VIII andamio + `Avance Cap VI - Base B5 HHI`). La versión pre-marco de Caps I-IV quedó en `Documentos Originales/Archivo - versiones anteriores del protocolo/Caps I-IV (pre-marco enclave).docx`.

## Convenciones
- **Nombre de archivo**: `Cap <N> - <Título corto>.docx`. El del Cap. VI conserva su nombre histórico (`Avance Cap VI - Base B5 HHI…`) porque ya estaba en uso; al madurar puede renombrarse a `Cap VI - Modelo de Panel.docx` sin perder el vínculo desde aquí.
- **Formato**: Times New Roman 12, tamaño carta, márgenes ≈3 cm — igual que el `Avance Cap VI`, para que el ensamblado final sea homogéneo.
- Cada Word abre con una línea **ESTADO** que marca si es andamio o tiene resultados; borrarla al cerrar el capítulo.
- El contenido sustantivo se redacta en el Word; las notas `.md` de `11 Redaccion/` y los índices por carpeta numerada quedan como andamio/seguimiento, no como el texto final.

## Estado de propagación a estos Word
- ✅ **C2 — Integración a la redacción (2026-09-06)**: propagados a los Word todos los hallazgos de los pasos 1-6, con las declaraciones de huecos. **Cap. V**: +V.10 cautela del Ghosh (>1 ≠ cadena), +V.11 CCV (serie 1992-2025, cobre/zinc ≈0.22/0.30 = enclave, espejo/CIF y plomo 1994 declarados), +V.12 corte de referencia 2008 (3 cortes). **Cap. VI**: +VI.4 HHI 2004-2024, +VI.5 georreferenciación (extracción vs transformación), +VI.6 destinos (desplazamiento a China), grafito amorfo vs criticidad; tipología renumerada VI.7-VI.8. **Cap. VII**: +VII.5 referencia internacional (ICIO 2020; Chile/Australia forward débil, Finlandia/Suecia integran, México agregado engañoso). **Cap. VIII**: VIII.3 recomendaciones por eslabón + contrafactual nórdico; VIII.4 declaración de vacíos (CCV, HHI, MIP, RAS, Comtrade, agregación, 2025). Todos regenerados por script (`build_capV/VI/VII/VIII.py` en `10 Datos/scripts`).
- ✅ **Cap. VI (2026-07-22)**: incorporada la corrección de la fecha de la fusión de fluorita (**enero 2012**, no 2013) y la serie HHI ≈6,525 (2004-2011) → 10,000 (2012+), en la nueva sección 7 del `Avance Cap VI`.
- ✅ **Caps. V-VIII (2026-07-22)**: insertada la columna vertebral y el **puente oferta/demanda**; Cap. VII reencuadrado a **secundario / de escritorio** (opción B, puede omitirse). Guía completa en [[Columna Vertebral Metodologica]] y [[Diagrama - Columna Vertebral Metodologica|el diagrama]].
- **Todos**: la base `10 Datos/processed/myb_estructura_industria.csv` (estructura de la industria por mineral-año, USGS MYB) es fuente para los Caps. IV, V y VI.

← [[Home]] · [[Ediciones Pendientes Documentos Word]] · [[Bitacora]]
