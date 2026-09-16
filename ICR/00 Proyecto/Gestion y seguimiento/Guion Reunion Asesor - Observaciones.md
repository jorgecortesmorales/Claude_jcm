---
title: Guion para la reunión con el asesor — respuesta a las cuatro observaciones
type: proyecto
tags: [icr, proyecto, asesor, protocolo]
created: 2026-07-21
updated: 2026-07-21
status: preparacion-reunion
---

# Guion — respuesta a las observaciones del Dr. Micheli

Cuatro observaciones del asesor sobre el protocolo. Para cada una: **(A) la observación a fondo** (qué te está diciendo en términos teóricos), **(B) tu respuesta a fondo**, **(C) qué cambié en el protocolo** (los cambios están marcados con control de cambios en `Protocolo ICR - correcciones asesor (control de cambios).docx`) y **(D) en palabras simples** (la observación y tu respuesta explicadas de forma llana, para que las tengas en la punta de la lengua). La observación 3 lleva además una sección extra que explica **por qué el Event Study sí funciona**.

Encuadre general que conviene que lleves de entrada: **ninguna de las cuatro es un golpe al proyecto.** Dos son críticas de validez que ya corregí (la 3 y la 4), una es una indicación de encuadre (la 1) y la otra es una redirección sobre dónde está tu aporte (la 2) — y el trabajo de datos de estas semanas la responde casi sola. Además, **las observaciones 2 y 4 apuntan al mismo punto ciego** (la amenaza de que la relación concentración→encadenamiento sea espuria), y las dos se cierran con lo mismo.

---

## Observación 1 — "Relevancia del tema en el marco del desarrollo industrial de México"

**(A) Qué observa, a fondo.** No es un reparo, es una instrucción de encuadre. Te pide anclar la **relevancia** del problema en el **debate de desarrollo industrial** de México, y no en la "criticidad" de los minerales vista desde EE.UU./UE (que es el gancho con el que abre tu protocolo). En lenguaje de economía del desarrollo: el interés del tema no es la *seguridad de suministro* de tus socios comerciales, sino la **falla de transformación estructural** — que México reproduzca el patrón de **enclave primario-exportador** en lugar de industrializar aguas abajo de su base mineral. Es un tema clásico de Prebisch/CEPAL y de política industrial.

**(B) Tu respuesta, a fondo.** De acuerdo, y de hecho tu tesis *ya es* sobre eso: los **encadenamientos hacia adelante** (Ghosh) y el **coeficiente de captura de valor** son, literalmente, la medida de cuánta industrialización se genera después de la extracción. Solo hacía falta **subir ese argumento al frente** de la justificación, en vez de dejarlo implícito bajo la criticidad geoeconómica. La criticidad EE.UU./UE se queda como **criterio de selección** del corpus de diez minerales, no como la relevancia del problema.

**(C) Qué cambié.** Inserté un párrafo nuevo en la justificación (§1.b) que encuadra el problema como una **oportunidad de desarrollo industrial no capturada** y define los encadenamientos hacia adelante como el indicador de esa industrialización. No borré nada: es una adición.

**(D) En simple.** *Él dice*: "no lo vendas como que a los gringos les preocupa; véndelo como un problema de industrialización de México". *Yo respondo*: "tienes razón, y mi tesis ya mide exactamente eso — cuánto se industrializa después de sacar el mineral —; lo pongo al frente y dejo lo de EE.UU./UE solo para justificar por qué elegí estos diez minerales".

---

## Observación 2 — "La aportación está en los datos y en las relaciones de causalidad, no en el modelo"

**(A) Qué observa, a fondo.** Dos cosas. Primero, **te valida el trabajo empírico**: tu contribución original es la **base de datos** que armaste (el HHI por mineral-año 1993-2025, la base de estructura de la industria extraída del USGS, las fusiones fechadas) y las **relaciones causales** que puedas establecer. Segundo, y en corto, te **advierte que no sobrevendas el modelo de panel**: un panel HHI→Ghosh con efectos fijos de doble vía es una herramienta estándar, su sofisticación no es lo novedoso, y —esto es lo delicado— **por sí solo no identifica causalidad, solo asociación condicional**. Los efectos fijos controlan lo que no cambia (por mineral y por año), pero no descartan endogeneidad: HHI y Ghosh podrían estar codeterminados por la misma estructura de enclave, o haber causalidad inversa, o variables omitidas.

**(B) Tu respuesta, a fondo.** Coincides: el aporte es (i) la base de datos, que no existía, y (ii) el mecanismo causal. Reposicionas el **panel como un ejercicio descriptivo y de contraste** de la relación, y trasladas la **carga de la causalidad** a los **quiebres estructurales fechados** que tu base ahora documenta con precisión:
- **Fluorita**: la fusión de **enero de 2012** hace saltar el HHI de ≈6,525 a 10,000 — un corte casi experimental *dentro del mismo mineral* (misma geología, mismo destino, mismo todo salvo la concentración).
- **Cobre**: la **huelga de Cananea (2007-2010)** derrumba y luego recupera la participación de Grupo México (86.6% → 51.2% → 66%) — variación exógena de concentración.
- **Grafito**: paso a **productor único formal en 2014**.

Con esos cortes puedes hacer un ejercicio **tipo antes-después / diferencias-en-diferencias dentro del mineral** (¿cambió el Ghosh/CCV del mineral tras el salto de concentración, frente a los minerales sin salto?), mucho más defendible como causal que la nube de puntos HHI-Ghosh entre minerales. Así, **tu base de datos se convierte en tu motor de identificación**: entregas lo que él pide.

**(C) Qué cambié.** (1) Reformulé el Objetivo específico 2: el panel "documenta la asociación" y la identificación causal se apoya en los quiebres fechados. (2) Inserté un párrafo en las técnicas del modelo que explica la **variación cuasi-experimental** de esos tres episodios. No toqué la especificación econométrica ni las hipótesis H1/H3, que ya están redactadas en términos de "relación estadística" (honestas).

**(D) En simple.** *Él dice*: "lo valioso es que juntaste datos que nadie tenía y que puedes contar la causa; el modelito de panel no es la joya, y ojo: correlación no es causa". *Yo respondo*: "de acuerdo; el panel lo dejo como foto descriptiva, y la causa la demuestro con tres momentos donde la concentración cambió de golpe dentro de un mismo mineral —la fusión de fluorita en 2012, la huelga de Cananea, el grafito quedándose con un solo productor en 2014— y veo si el encadenamiento se movió justo ahí. Eso sí es causal, y solo pude hacerlo porque construí la base".

---

## Observación 3 — "La reforma no da la escala de tiempo para analizar efectos"

**(A) Qué observa, a fondo — y tiene razón.** La reforma es de **abril de 2023**; hoy (mediados de 2026) hay apenas ~2-3 años de post-periodo, **con litigio aún abierto en la SCJN**. Con eso **no puedes medir efectos estructurales de largo plazo** (¿cambió la integración vertical?, ¿cambiaron los encadenamientos?): no hay horizonte suficiente y los pocos años disponibles están contaminados por precios globales, incertidumbre judicial y cambio de sexenio. Tal como estaba redactada H4 ("ha afectado de forma diferencial…"), prometías un **efecto realizado** que la ventana temporal no permite estimar.

**(B) Tu respuesta, a fondo — separa los dos relojes.**
1. El **motor estructural** de la tesis (concentración → bajos encadenamientos, H1-H3) corre sobre el panel **1993-2025 y no depende en absoluto de la reforma**. Ese resultado se sostiene solo, con 30 años de datos.
2. La reforma se analiza como **choque reciente a horizonte corto**, y para eso el **Event Study de retornos anormales (CAR) es exactamente la herramienta correcta**, porque mide la **reacción del mercado al anuncio** en una ventana de días — no un efecto de largo plazo. Tu H4 (impacto asimétrico establecidos vs. entrantes) se contrasta como **diferencia de CAR entre los dos grupos**, cosa que sí es factible.

Es una **refutación parcial legítima**: "la reforma no da tiempo" es cierto para **efectos estructurales**, pero **no para efectos de anuncio**, que es lo que el Event Study mide.

**(C) Qué cambié.** Reformulé (1) la pregunta subsidiaria 3, (2) el Objetivo específico 3, (3) **H4** y (4) las técnicas del Objetivo 3, todos en clave de **corto plazo / anuncio**, dejando explícito que la consolidación estructural de largo plazo es **conjetura a documentar, no a estimar**. El Event Study pasa de "opción metodológica adicional" a **vía principal** del capítulo.

### Por qué el Event Study SÍ funciona pese a la escala de tiempo corta (esto estúdialo)

La confusión natural es: "si la reforma es muy reciente, ¿cómo voy a medir su efecto?". La respuesta está en **qué mide** un Event Study, que **no** es el efecto realizado, sino la **expectativa del mercado sobre ese efecto**, revelada en el instante del anuncio. Paso a paso:

1. **El precio de una acción es el valor presente de TODOS los flujos futuros esperados** de la empresa. Es decir, el precio de hoy ya es una apuesta sobre el futuro completo de la empresa, descontado al presente.

2. **Hipótesis de mercados eficientes (forma semifuerte)**: los precios incorporan la información pública de forma casi inmediata. Cuando llega una **noticia inesperada** (la aprobación de la reforma), el precio **salta** para reflejar la nueva expectativa de flujos futuros. Ese salto ocurre en **horas o días**, no en años.

3. **Mecánica del cálculo**:
   - **Ventana de estimación** (por ejemplo, los 120 días *antes* del evento): estimas el "retorno normal" de cada acción con un **modelo de mercado** (cómo se mueve esa acción en función del índice general, su beta). Es el comportamiento esperado *si no pasara nada*.
   - **Ventana de evento** (por ejemplo, [−1, +1] o [−5, +5] días alrededor de la fecha de la reforma): calculas el **retorno anormal** = retorno observado − retorno normal. Ese "anormal" es la parte **no explicada por el mercado general**, es decir, la reacción **específica de la empresa** al evento.
   - **CAR** (retorno anormal acumulado): sumas los retornos anormales dentro de la ventana. Es la reacción total atribuible al evento.

4. **La clave conceptual**: como el precio ya descuenta el futuro, un movimiento **hoy** ya contiene la valoración que hace el mercado de las **consecuencias de largo plazo** de la reforma — pero **comprimidas en una reacción inmediata**. No necesitas *esperar* diez años para ver si la reforma frenó la inversión: el mercado, que es prospectivo, **te dice hoy** cuánto cree que la va a frenar. La ventana corta es justamente lo que **aísla** la reacción a la ley de todo lo demás (precios de commodities, ciclo económico), porque en tres días alrededor del anuncio no pasó nada más relevante.

5. **Cómo contrasta tu H4**: calculas el CAR **por separado** para (a) los grandes consorcios establecidos (Grupo México, Peñoles, Fresnillo plc — con concesiones largas previas a 2023) y (b) las empresas más expuestas a nuevas concesiones/entrantes cotizadas. Si la reforma golpea más a los entrantes, su CAR será **más negativo**. La **diferencia de CAR entre grupos** es la prueba directa de la asimetría — una comparación transversal que **no requiere una serie temporal larga**.

6. **Límites que debes declarar tú mismo** (para que no te los saque él):
   - Solo cubre **empresas cotizadas** (las junior pequeñas y las privadas no entran) → por eso las **entrevistas** complementan, cubriendo a los actores no cotizados.
   - Requiere una **fecha de evento limpia** y sin otras noticias grandes en la ventana. En tu caso hay **varias fechas candidatas** (anuncio de la iniciativa, aprobación en abril 2023, fallos de la SCJN), y puedes correr el estudio para cada una.
   - Mide **expectativas, no resultados realizados**: si el mercado se equivoca, el CAR predice mal. Pero para tu tesis, "impacto **anticipado por el mercado**" es una afirmación legítima y **acotada**, que es justo lo que la escala temporal permite sostener.

**(D) En simple.** *Él dice*: "la reforma es de hace nada; no te alcanza el tiempo para ver qué efecto tuvo". *Yo respondo*: "cierto para efectos de fondo de largo plazo — y por eso el corazón de mi tesis (concentración → poco encadenamiento) usa 30 años de datos y no depende de la reforma. Para la reforma uso un **Event Study**, que no necesita tiempo largo: el **precio de una acción es una apuesta sobre el futuro de la empresa**, así que cuando pasa la ley de sorpresa, los inversionistas **rehacen su apuesta al instante** y el precio brinca. Midiendo cuánto brinca en los días alrededor de la ley — y **cuánto más brinca para los nuevos que para los grandes ya establecidos** — leo lo que el mercado cree que la ley va a provocar, sin esperar diez años. La ventana corta es una ventaja, no un defecto, porque aísla la reacción a la ley".

---

## Observación 4 — "Los actores tradicionales te van a decir por qué no invierten en extracción; no son actores industriales"

**(A) Qué observa, a fondo — es la más filosa, y es válida.** Tu marco de entrevistas estaba cargado del **lado extractivo** (CAMIMEX, SGM, grandes mineras, despachos de derecho minero). Si a Grupo México o a Peñoles les preguntas por qué no hay integración industrial, te contestan desde la **lógica de la extracción** ("por qué no invertimos más en explorar/extraer bajo la nueva ley") — que es inversión *extractiva*, no el **eslabón industrial** que a ti te falta. **No son actores de transformación**, así que estructuralmente no pueden explicarte por qué no se forma el encadenamiento aguas abajo.

**Y aquí está la conexión con la observación 2.** El encadenamiento hacia adelante puede fallar por **dos lados**: por la **oferta** (los mineros no integran porque las rentas del oligopolio les bastan — *tu hipótesis*) **o** por la **demanda** (no hay industria transformadora doméstica que compre el insumo: sin industria de HF/fluoroquímicos que absorba la fluorita, sin vidrio/electrónica de alta pureza que absorba la sílice…). **Si la falla es de demanda, tu correlación HHI→Ghosh podría ser espuria**: ambas cosas (alta concentración y bajos encadenamientos) serían efecto común de la estructura de enclave, sin que una cause la otra. Esa es **la misma amenaza de identificación** que asoma en la observación 2, y solo la despejas **hablando con el lado industrial/aguas abajo**.

**(B) Tu respuesta, a fondo.** Tienes razón: la muestra estaba sesgada al lado extractivo. **Amplías el marco muestral al lado industrial/aguas abajo** por cadena (química del flúor para fluorita, vidrio/fundición para sílice, siderurgia para manganeso y barita, electrónica/baterías para grafito) y a las **cámaras de la industria de transformación**. Reformulas la pregunta cualitativa de "por qué los mineros no integran" a "**por qué falla el eslabón extracción-industria, visto desde los dos lados**". Y esto te sirve doble: **descarta la explicación alternativa de demanda** y con ello **refuerza la identificación causal** que te pidió en la observación 2.

**(C) Qué cambié.** (1) En Fuentes de información reorganicé las entrevistas en **dos bloques** (extracción + aguas abajo). (2) En el Objetivo específico 3 y en las técnicas del Objetivo 3 quedó explícito que el diseño cualitativo cubre **ambos lados del eslabón**, con la distinción oferta/demanda como pieza del diagnóstico causal.

**(D) En simple.** *Él dice*: "los mineros te van a hablar de por qué sacan o no sacan mineral, no de por qué no se industrializa; para eso no son los indicados". *Yo respondo*: "cierto; agrego entrevistas del **otro lado de la cadena** — los que *comprarían* el mineral para transformarlo (química, vidrio, acero, electrónica) — porque la falta de industrialización puede ser culpa de los mineros (que no integran) **o** de que no hay industria que compre. Preguntando a ambos lados sé cuál de las dos es, y de paso blindo mi afirmación de que la concentración es la causa".

---

## Cierre — el mensaje de fondo para la reunión

Las cuatro observaciones, bien leídas, **empujan la tesis hacia donde los datos ya la pueden llevar**: menos peso en el modelo econométrico como vitrina, más peso en (a) **la base de datos** que construiste, (b) **la identificación causal** vía los cortes estructurales fechados (fluorita 2012, Cananea, grafito 2014) y (c) un **diseño cualitativo de dos lados** que cierra la amenaza de la explicación por demanda. No vas en modo defensa; vas en modo **"sí, y esto ya lo tengo encaminado"**.

Un punto que conviene que menciones tú mismo como muestra de rigor: al construir la base **descubriste que el grafito no es el mercado atomizado que creías** (el USGS solo identifica uno o dos productores; desde 2014 es monopolio de Grafitos Mexicanos), lo que obliga a **repensar cuál es el "caso de contraste" de baja concentración** del corpus — probablemente la barita (líder decreciente) o la variación dentro de los metales. Es una decisión abierta (ver C-17 en [[Ediciones Pendientes Documentos Word]]); llevarla tú a la mesa demuestra que la base de datos está haciendo su trabajo.

### Referencias del paquete
- Protocolo con **control de cambios**: `00 Proyecto/Documentos Originales/Protocolo ICR - correcciones asesor (control de cambios).docx` (8 cambios, todos marcados).
- Cambios pendientes en los Caps. I-IV y su detalle: [[Ediciones Pendientes Documentos Word]] (lote 2026-07-21, C-16 a C-19).
- Evidencia de datos: [[Bitacora]] 2026-07-21; bases `10 Datos/processed/hhi_numeradores.csv` y `myb_estructura_industria.csv`.

← [[Home]] · [[Protocolo Aprobado]] · [[Ediciones Pendientes Documentos Word]]
