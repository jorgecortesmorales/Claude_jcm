---
title: "Handoff — Estado actual (manuscrito e investigación complementaria A-E) 2026-10-12"
type: handoff
tags: [icr, handoff, estado, manuscrito, investigacion-complementaria, cobre, transparencia]
created: 2026-10-12
updated: 2026-10-12
status: activo
---

# Handoff — arrancar un chat nuevo (ICR minerales críticos)

> [!info] Qué es esto
> Fuente única de verdad para continuar en un chat con contexto limpio. **Reemplaza** a [[Handoff - Estado actual (HEM, consolidado y certificacion) 2026-09-29]], que sigue valiendo como referencia técnica del manuscrito (HEM, consolidado, cotejo, cómo regenerar). **No confundir** con los otros proyectos del repositorio (`ICR DIANA/`, `AMPLIACIONES/`, `RETO ACTINVER/`, `Econometría/`).

## 0. Reglas de trabajo (vigentes)
- Trabajar **solo dentro de `ICR/`**; usar `py` (no `python`); skills de Obsidian para `.md`/`.canvas`/`.base`.
- **Diseño descriptivo**, no causal. Concepto ordenador: **enclave estructural**. HHI, Ghosh, HEM y CCV son descriptores.
- **Pauta de redacción del alumno:** la interpretación de resultados es **solo descriptiva** (describir y analizar, **sin implicaciones ni búsqueda de relaciones**). Excepción: los dos coeficientes de Ghosh (**Rasmussen** = intensidad; **HEM** = peso) se interpretan por separado y en conjunto. Aplica también a los escritos de la investigación complementaria.
- **Estilo matemático:** el de **Morales-López (2023)**: ecuaciones numeradas con `$$ … \qquad\qquad (n)$$` y glosario «donde X es …».
- **Referencias cruzadas del manuscrito:** `{{cua:X}}` / `{{fig:X}}` solos, nunca «Cuadro {{cua:X}}».
- **Revisar a mano las afirmaciones de dirección u orden** («supera», «desde», «en todos»): el cotejo solo certifica números. En esta etapa se corrigieron varias de ese tipo (ver [[Bitacora]] 2026-10-08 c).
- **Copia de control del alumno:** `11 Redaccion/manuscrito/ICR - Manuscrito (nueva estructura) - versión (08-10-2026).docx/.pdf` **no se toca ni se versiona**; solo se edita el manuscrito del pipeline.
- **No aceptar el control de cambios del PROTOCOLO**: espera al asesor (Dr. Jordy Micheli Thirion).
- **Sin voz de IA**; todo cambio versionado en git (rama `main`, remoto `git@github.com:jorgecortesmorales/Claude_jcm.git`, todo pusheado al cierre); handoff antes de agotar contexto.
- Tras cualquier cambio al manuscrito o a sus datos: recompilar (`py pandoc/build_book.py` y `py pandoc/update_pdf.py` desde `11 Redaccion`) y correr el cotejo (`13 Entregables/Consolidado datos y calculos/cotejo_certificacion.py`, debe dar 0 difieren). `update_pdf.py` ya reintenta las llamadas que Word rechaza; si aun así queda un `WINWORD.EXE` oculto, pedir al alumno que lo cierre (Administrador de tareas → Detalles).
- **Acceso web:** la SEC bloquea `curl` sin correo en el encabezado y, desde el 12/10/2026, también la navegación del navegador integrado. Para documentos de la SEC: búsqueda de texto completo (efts.sec.gov) o copias públicas (minedocs.com, finboard.net). No saltar verificaciones anti-bots.

## 1. Manuscrito (sin cambios desde el 2026-09-30)
- `11 Redaccion/manuscrito/ICR - Manuscrito (nueva estructura).docx` (+ PDF, 178 pp.): 9 capítulos + Anexos B/C/D; **52 cuadros, 33 ilustraciones**; cotejo 1 453/1 453, 0 difieren.
- Detalle técnico (HEM, consolidado, regeneración, ICIO): ver el handoff del 2026-09-29.
- **Pendiente principal:** versión de entrega del alumno (voz propia) de los Caps. III y V-IX (+ §II.2.5). La versión base ya sigue la pauta descriptiva.

## 2. Investigación complementaria A-E (paralela; inclusión en la ICR por definir)

Cuadro de control por subpuntos: **[[Control - Investigacion complementaria (A-E)]]** (actualizarlo en cada avance).

| Punto | Estado | Documentos |
|---|---|---|
| **A.** Cobre que dejó de ir a EUA | Casi completo; falta medir el tránsito por Guaymas | [[Memoria - Pregunta A (cobre, destino y abasto de EUA) piloto]] · escrito independiente [[Mexico y el abasto de cobre de Estados Unidos, 1992-2024]] (`11 Redaccion/Escritos independientes/`, .md y .docx) |
| **B y E.** Métodos y frontera tecnológica; procesos | Piloto de cobre hecho (10 operaciones, 6 países + México; Australia pendiente) | [[Memoria - Preguntas B y E (procesos del cobre) piloto]] |
| **C.** Patentes | Solo ruta | [[Ruta metodologica - Investigacion mixta (patentes, concesiones, procesos productivos)]] |
| **D.** Concesiones | Ruta; datos en espera de solicitudes de transparencia | Misma ruta |

**Resultados clave de A** (descriptivos): consumo aparente de EUA de ~3 000 kt (fines de los noventa) a 1 660-1 970 kt (2009-2024); de 7 fundiciones primarias quedan 2; EUA exportador neto de concentrado desde 2005; refinado importado sobre todo de Chile (70 % en 2024), México 2 % en refinado y 41 % en chatarra. México registra como importación solo 5 % (2011-2017) y 43 % (2018-2024) del concentrado que EUA declara exportarle; Grupo México (Informe BMV 2022-2025), Capstone (TRS Pinto Valley 2021) y Mercator (2011) documentan el envío del concentrado de Arizona a Guaymas; ASIPONA registra «concentrado de cobre en tránsito internacional proveniente del sur de los Estados Unidos con destino hacia Asia»; cota inferior de lo no mexicano embarcado en Guaymas: 119 598 t (2020) y 224 129 t (2022).

**Reglas propias de C y D** (decisión del alumno): las razones de no uso de patentes y de no conversión de concesiones se obtienen de datos y documentos (en D se describe la retención especulativa del título con indicadores observables); entrevistas solo complementarias en C y E, ninguna en D. Comparación con los siete países de la ICR (Chile, Perú, Australia, Brasil, China, Finlandia, Suecia).

**Datos y scripts nuevos:** `10 Datos/scripts/pa_cobre_*.py`, `pa_guaymas_concentrado.py`, `pbe_frontera_menciones.py`, `pbe_cobre_fichas.py`; CSV en `10 Datos/processed/` (`cobre_eua_*`, `scc_asarco_transacciones`, `cobre_eua_rutas_concentrado_documentos`, `guaymas_concentrado_cobre*`, `cobre_procesos_*`, `cobre_frontera_*`); originales en `10 Datos/Bases Originales/` carpetas 07 (MCS y MYB de cobre), 11 (Comtrade), 16 (empresas), 17 (puerto de Guaymas), 18 (transparencia; acuses), 19 (procesos del cobre). Las carpetas de `Bases Originales` no se suben a git.

## 3. Solicitudes de transparencia en curso
Detalle y tabla de seguimiento: [[Solicitudes de transparencia (Guaymas y concesiones) 2026-10-08]]. Textos completos: `Solicitudes completas para pegar (S1, S2, S4, S5, S6).txt`.

| Clave | Institución | Folio vigente | Respuesta a más tardar (con prórroga) |
|---|---|---|---|
| S1 | ANAM (tránsito y comercio de la fracción 2603 por aduana) | 342746500069626 | 09/11/2026 (24/11/2026) |
| S2 | ASIPONA Guaymas (concentrado por tipo de tráfico) | 340000800008126 | 10/11/2026 (25/11/2026) |
| S3 | SEMAR (anuarios de Guaymas por producto) | 340026600164526 (prevención respondida) | por confirmar tras el desahogo |
| S4 | SE (padrón histórico de títulos) | 340025900094226 | 10/11/2026 (25/11/2026) |
| S5 | SE (transmisiones, comprobación de obras, cancelaciones) | 340025900094326 | 10/11/2026 (25/11/2026) |
| S6 | SAT (derecho adicional y derechos sobre minería) | 340027700331526 | 10/11/2026 (25/11/2026) |

Las solicitudes del 09/10/2026 con solo el resumen (folios 342746500069326, 340000800007826, 340025900093826, 340025900093926, 340027700330826) siguen vivas. Prevenciones posibles hasta el **19/10/2026**: si llega una, redactar la respuesta a partir del oficio. Las respuestas se guardan en `10 Datos/Bases Originales/18 Transparencia/` con el folio en el nombre.

## 4. Qué sigue (opciones)
1. **Manuscrito:** versión de entrega del alumno (Caps. III y V-IX).
2. **Mientras llegan las respuestas:** D4 (series de concesiones y superficie de los informes CAMIMEX y anuarios SGM ya descargados); validar con literatura las listas de procesos (B1) y de tecnologías de frontera (B4); C1 (primera búsqueda de patentes de cobre en Lens.org); Australia en B/E.
3. **Al llegar las respuestas:** S1-S3 → tránsito por Guaymas (cerrar A5 y actualizar el escrito independiente); S4-S6 → D1-D3.
4. Decidir la inclusión de A-E en la ICR (A en VII.3; capítulo nuevo o complementos; o investigación independiente).
5. Pendientes heredados: protocolo (espera al asesor); entregables con redacción interpretativa previa; bibliografía a Zotero; agenda de datos del Cap. IX.

## 5. Para orientarte al arrancar
- [[Control - Investigacion complementaria (A-E)]] · [[Bitacora]] (entradas 2026-10-08 a 2026-10-12) · [[Handoff - Estado actual (HEM, consolidado y certificacion) 2026-09-29]] (técnico del manuscrito).
- Mapa: [[Mapa del Proyecto]] · [[Home]] · [[Arquitectura del documento (estructura expositiva)]].
- Arranque: [[Mensaje de arranque - nuevo chat 2026-10-12]].

← [[Home]] · [[Bitacora]]
