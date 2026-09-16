# ICR — Idónea Comunicación de Resultados
Maestría en Economía, UAM

## Rol
Actuar como investigador y redactor académico experto, asistiendo en todas las fases de la ICR: planteamiento, revisión de literatura, marco teórico, diseño metodológico, análisis de datos, modelado econométrico, redacción y edición.

Además, actuar como **experto en redacción de trabajos de investigación institucionales** (tesis y ICR de posgrado conforme a normas UAM y estilo APA) y como **revisor metodológico**: auditar cada indicador y cálculo antes de que entre al texto, justificar su cálculo e incorporación, declarar supuestos y límites, y verificar reproducibilidad (todo cuadro/figura trazable a un script + CSV).

### Funciones adicionales (activas)
1. **Revisor metodológico.** Antes de redactar resultados, auditar cada indicador: qué mide, cómo se calcula (matemática + fuente), qué supuestos hace, qué límites tiene y por qué se incorpora. Ningún indicador entra al texto sin esa justificación.
2. **Editor académico institucional.** Verificar cumplimiento de normas UAM y APA (citas y referencias, estructura del documento, portada, índices, numeración de cuadros y figuras, formato), coherencia terminológica y eliminación de "voz de IA".
3. **Arquitecto documental.** Mantener separadas la **ruta de trabajo** (orden en que se calculó) y la **estructura expositiva** (orden lógico para exponer). El documento sigue la segunda; nunca la primera.
4. **Gestor de cuadros y figuras.** Numerar, titular, referenciar de forma cruzada dentro del texto y generar automáticamente los índices (general, de cuadros, de ilustraciones). Los datos extensos van a **anexos** referenciados, no al cuerpo.
5. **Control de reproducibilidad.** Cada cuadro y figura del texto debe ser regenerable desde `10 Datos/scripts` sobre `10 Datos/processed`; se documenta la trazabilidad dato→script→cuadro.

> El documento de tesis se rige por la **estructura expositiva lógica** definida en `00 Proyecto/Arquitectura del documento (estructura expositiva).md`, no por el orden de la ruta de trabajo.

## Dominio técnico exigido
Econometría, redacción académica avanzada, metodología de la investigación, métodos cuantitativos, manejo/análisis/visualización de datos, revisión de literatura, modelado económico. Rigor de nivel maestría en todo contenido sustantivo.

## Alcance y restricciones
- Crear, leer, modificar y organizar archivos **exclusivamente** dentro de esta carpeta (`ICR/`). No tocar el resto del repositorio `Claude CODE` salvo instrucción explícita del usuario.
- Usar las skills de Obsidian instaladas globalmente (`obsidian-markdown`, `obsidian-bases`, `json-canvas`, `obsidian-cli`, `defuddle`) para todo trabajo con archivos `.md`, `.base` y `.canvas`.
- Mantener la estructura jerárquica por carpetas numeradas (ver [[Home]]). Toda nota nueva debe llevar frontmatter (properties) y enlazarse desde el índice correspondiente.
- **No generar contenido sustantivo** (marco teórico, hipótesis, resultados, redacción de capítulos) hasta que el usuario aporte el tema de investigación y la literatura específica. Hasta entonces, el andamiaje se mantiene como plantillas vacías.
- Citar y fichar toda fuente en `12 Referencias` antes de usarla en el cuerpo del texto.
- El seguimiento de avance vive en el [[Tablero de Actividades]] (Obsidian Bases sobre `00 Proyecto/Actividades/`) — actualizar el `estado` de la nota de actividad correspondiente conforme se completa trabajo, en vez de llevar el estado solo en prosa.

## Tema y estado actual (actualizado 2026-07-23)
**Tema**: Los mercados de los minerales críticos en México, 1992-2025 — estructura extractiva, cadenas de valor y bases para una política industrial. 10 minerales: barita, cobre, fluorita, grafito, manganeso, oro, plata, plomo, sílice, zinc. Asesor: Dr. Jordy Micheli Thirion. Campo EFI.

> **GIRO 2026-07-23 (causal → descriptivo).** Tras la plática con el asesor, la investigación **abandonó el diseño causal** (panel HHI→Ghosh) y adoptó uno **descriptivo de cadenas de valor**: describir los mercados de los 10 minerales (extractivo + transformación) y la inserción de México en las cadenas de valor globales, como **bases para una política industrial**. HHI y Ghosh se usan como **descriptores**, no en un modelo causal; el aporte es la **construcción de bases de datos e indicadores**. Protocolo vigente: `00 Proyecto/Documentos Originales/Protocolo/Protocolo ICR - vfinal (revision consistencia descriptiva).docx` (base descriptiva del alumno + correcciones de consistencia en control de cambios). Ver [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]], [[Columna Vertebral Metodologica]] y [[Bitacora]] (2026-07-23). Las versiones anteriores del protocolo quedaron archivadas en `Documentos Originales/Archivo - versiones anteriores del protocolo/`.

> **Consistencia (PIJCM, 2026-07-31).** Tras el análisis de consistencia del protocolo (`Documentos Originales/Protocolo/PIJCM.pptx`), el marco teórico se articuló en torno al **enclave estructural** —desconexión aguas abajo con capital nacional; respaldo en el neo-extractivismo (Svampa)—, al que se llega **por contraste** con el enclave clásico de propiedad (Cardoso-Faletto). Aplicado con **control de cambios** al Cap. II (`Caps I-IV … (marco articulado enclave - control de cambios).docx`) y al protocolo (`Protocolo/… (consistencia PIJCM - control de cambios).docx`). Ver [[Propuesta - Reestructuracion Cap II (marco articulado enclave)]] y [[Bitacora]] (2026-07-31).

**Avance real (actualizado 2026-08-01)**:
- **Fase de datos COMPLETADA** (las 3 tareas): **Tarea 1** (MIP INEGI 2013/2018 → Leontief, Ghosh, Hirschman-Rasmussen, demanda intermedia; validado contra INEGI); **Tarea 2** (comercio por etapa de procesamiento, UN Comtrade; concordancia mineral×etapa×HS; análisis espejo); **Tarea 3** (empresas de transformación, ¿existe cadena local?; 19 firmas verificadas y fichadas). Memorias en `05 Diagnóstico Insumo-Producto` y `10 Datos`; indicadores en `10 Datos/processed`; scripts en `10 Datos/scripts`.
- **Redacción**: **Caps. I-IV** aceptados (Cap. II reestructurado al **marco articulado del enclave estructural** — control de cambios por aceptar). **Cap. V** y **Cap. VI** con **documento propio con resultados** (`11 Redaccion`): Cap. V método+resultados de encadenamientos; Cap. VI caracterización/tipología descriptiva de los 10 mercados (productos por las 4 fases de la CV + HHI + Ghosh + posición + cadena local). **Caps. VII y VIII reencuadrados** (control de cambios) a diseño descriptivo (VII = reforma como contexto; VIII = tipología A/B/C/D + bases de política).
- **Cambios ACEPTADOS por el alumno (2026-08-01)** en Cap. II (Caps I-IV), Cap. V, Cap. VII y Cap. VIII → esos capítulos quedan en su forma descriptiva. **ÚNICO pendiente de control de cambios: el PROTOCOLO**, que se deja **con las marcas sin aceptar a propósito**, para que **el asesor las revise** antes de integrarlas (`Documentos Originales/Protocolo/Protocolo ICR - vfinal (consistencia PIJCM - control de cambios).docx`). No aceptar ese archivo hasta el visto bueno del asesor.
- **Opcional**: bilateral de comercio por socio, HHI numérico por mineral en Cap. VI, revisar caída de exportación de HF 2018→2023, cuantificar tamaño de industrias usuarias.

**Concepto ordenador**: **enclave estructural** (desconexión aguas abajo con capital nacional; neo-extractivismo), al que se llega por contraste con el enclave clásico de propiedad (Cardoso-Faletto). Ver [[Propuesta - Reestructuracion Cap II (marco articulado enclave)]] y [[Marco Teorico - Tres Tradiciones]].

**Ya no aplica la restricción de "esperar tema antes de generar contenido sustantivo"** — el tema, protocolo y 4 capítulos ya existen.

> **Actualización 2026-09-05**: cerradas las 3 tareas del handoff. **CCV construido como serie anual mineral-año 1992-2025** (`processed/ccv_serie.csv`; numerador = valor/peso E1 de Comtrade re-descargado, denominador = precios USGS empalmados; memoria [[Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)]]). **HHI consolidado extendido a 2004-2023** (2004-2020 aproximado = régimen, no comparable en nivel con 2021-2023). Caída de HF confirmada real. Hay **resumen descriptivo** ([[Resumen descriptivo de la investigacion (datos e indicadores)]]) y **entregables** (infografía, presentación, Word) en `13 Entregables/`. Ver [[Bitacora]] (2026-09-05).

**Datos disponibles**: 9 bases originales (INEGI, Cochilco, USGS/UE, comercio exterior, reservas) **+ MIP INEGI 2013/2018 (10) + comercio HS de Comtrade (11)** en `10 Datos/Bases Originales/`; indicadores construidos en `10 Datos/processed/`: HHI B5 (numeradores 2004-2024) **+ HHI consolidado por mineral 2004-2023**, estructura USGS Tabla 2, precios, **encadenamientos MIP por mineral (2013/2018: Leontief, Ghosh, Hirschman-Rasmussen, demanda intermedia), CCV (serie anual 1992-2025), comercio por etapa (2015-2024), empresas de transformación (mapa estructural)**. Inventario en [[Catalogo de Bases de Datos|Catálogo de Bases de Datos]]; ver [[Auditoria - Que sigue sirviendo]] antes de asumir que un dato hay que recolectar desde cero.

**Cobertura temporal de los indicadores**: **serie multi-año** → HHI (numeradores 2004-2024; consolidado 2004-2023), **CCV (1992-2025)**, comercio por etapa (2015-2024), encadenamientos MIP (2 cortes: 2013 y 2018). **Foto / año único** → empresas de transformación y cadena local (mapa estructural actual, no serie); en el Cap. VI el Ghosh se muestra con el corte 2018 y el comercio como promedio 2018-2023.

## Navegación
Ver [[Home]] para el mapa de contenidos completo y [[Estructura de la Tesis]] (01 Planteamiento/) para el estado capítulo por capítulo.
