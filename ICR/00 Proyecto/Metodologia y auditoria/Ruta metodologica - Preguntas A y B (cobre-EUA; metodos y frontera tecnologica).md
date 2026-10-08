---
title: "Ruta metodológica — Preguntas A y B (destino del cobre y abasto de EUA; métodos de extracción, concentración y refinación)"
type: metodologia
tags: [icr, metodologia, ruta, cobre, comercio, tecnologia, procesos, exploratorio]
created: 2026-10-08
updated: 2026-10-08
status: propuesta
inclusion_icr: por definir
---

# Ruta metodológica — Preguntas A y B

> [!info] Estado
> Propuesta de ruta, **sin decisión de inclusión en la ICR**. Nada de lo que sigue se ha calculado salvo la observación preliminar de A, que sale de un CSV que ya existe. La pregunta B se resuelve con el módulo E de la investigación mixta ([[Ruta metodologica - Investigacion mixta (patentes, concesiones, procesos productivos)]]); aquí se plantea su versión corta.

## A. El cambio de destino del cobre: ¿EUA necesita menos cobre o lo obtiene de otro lado?

### A.0 Lo que ya dicen nuestros datos (observación preliminar)

Con `10 Datos/processed/comercio_destinos_serie_resumen.csv` (UN Comtrade, exportaciones de México por etapa y socio, 1992-2024):

| Etapa | 2000 | 2008 | 2016 | 2024 |
|---|---|---|---|---|
| E1 concentrado: valor (MUSD) | 116 | 327 | 1 324 | 3 719 |
| E1 concentrado: % a EUA | 52 % | 0 % | 0 % | 0 % |
| E1 concentrado: % a China | 0 % | 81 % | 79 % | 100 % |
| E2 refinado: % a EUA | 99 % | 42 % | 59 % | 58 % |
| E3 semimanufacturas: % a EUA | 88 % | 82 % | 75 % | 93 % |

El giro de destino ocurre en el **concentrado**, y ocurre cuando ese flujo era todavía pequeño (116 MUSD en 2000): el concentrado no dejó de ir a EUA para ir a China, sino que creció unas treinta veces y el crecimiento se dirigió a China. Las semimanufacturas siguen yendo mayoritariamente a EUA, y el refinado también en la mayoría de los años de la tabla (58 % en 2024; 42 % en 2008). Por eso la pregunta A se descompone en cuatro.

### A.1 Preguntas operativas

1. **A1.** ¿Cayeron las importaciones de EUA de cobre mexicano, y en qué forma (concentrado, ánodo/blíster, cátodo, chatarra, semimanufacturas)?
2. **A2.** ¿Cambió el requerimiento de cobre de EUA (producción minera, producción refinada, consumo aparente)?
3. **A3.** ¿De qué países importa EUA cada forma de cobre, y cómo cambió la participación de México?
4. **A4.** ¿Por qué el concentrado mexicano dejó de ir a EUA? (capacidad de fundición en EUA; destino de los concentrados de Grupo México hacia sus propias fundiciones de ASARCO; contratos con fundidores asiáticos). Esta parte es **contexto documentado**, no una relación estimada.

### A.2 Fuentes

| Fuente | Qué aporta | ¿La tenemos? |
|---|---|---|
| Comtrade, México exportador (HS 2603, 7401-7404, 7405-7411) | Flujo por etapa y socio | **Sí** (`comercio_destinos_serie_resumen.csv`, `comercio_por_etapa_1992_2024.csv`) |
| Comtrade, **EUA importador**, mismas partidas por socio, 1992-2024 | Lado del comprador; comercio espejo contra México | No; mismo script de descarga de Comtrade, cambiando el reportante |
| USGS *Mineral Commodity Summaries* — Copper (ediciones 1996-2026) | Producción minera y refinada de EUA, consumo aparente, dependencia neta de importaciones, principales proveedores de refinado | Parcial (la carpeta `07 USGS MCS` no tiene aún las fichas de cobre) |
| USGS *Minerals Yearbook* — Copper (capítulo de EUA) | Fundiciones y refinerías de EUA por año y su capacidad (cierres y reaperturas) | No |
| ICSG, *World Copper Factbook* (gratuito) | Capacidad de fundición y refinación por país; comercio de concentrado | No |
| Informes 10-K de Southern Copper y anuales de Grupo México / ASARCO | Destino de los concentrados propios; flujos intra-grupo México→EUA | No |

### A.3 Método

1. **Series en peso y en valor.** Usar el peso neto de Comtrade para separar el efecto precio. En concentrado, convertir a cobre contenido con la ley media declarada (dato a verificar por año; USGS o los 10-K).
2. **Consumo aparente de EUA**: $C_t = P_t + M_t - X_t \pm \Delta S_t$, con $P$ = producción refinada; **dependencia neta**: $D_t = (M_t - X_t)/C_t$.
3. **Participación de México en las importaciones de EUA** por etapa $k$: $s^k_{MX,t} = M^k_{EUA\leftarrow MX,t} / M^k_{EUA,t}$.
4. **Descomposición del cambio** de las importaciones de EUA desde México (*shift-share*): $\Delta M^k_{MX} = \Delta M^k_{EUA}\, \bar s^k_{MX} + \bar M^k_{EUA}\, \Delta s^k_{MX}$. El primer término indica si EUA demandó menos de esa forma; el segundo, si sustituyó proveedor.
5. **Comercio espejo** México-X frente a EUA-M por año (como en el CCV), para validar.
6. **Contexto A4**: cronología de las fundiciones de EUA (USGS MYB) y del destino de los concentrados de Grupo México (10-K), con fecha y fuente de cada evento.

### A.4 Productos y lugar posible en la ICR

- 2 cuadros (consumo aparente y dependencia de EUA; participación de México por etapa) y 2 ilustraciones (participación por socio en las importaciones de EUA de concentrado y de cátodo).
- Si se incluye: una subsección de **VII.3** (destinos) o un recuadro en VII.3. Esfuerzo bajo: una descarga de Comtrade y la lectura de las fichas MCS/MYB de cobre.

## B. Métodos de extracción, concentración y refinación: cuáles se usan en México, por qué, y qué tan cerca de la frontera están las empresas

### B.1 Preguntas operativas

1. **B1.** Catálogo mundial de métodos por mineral y eslabón: minado (cielo abierto; subterráneo por hundimiento de bloques, subniveles, corte y relleno, cámaras y pilares), concentración (trituración y molienda, flotación, gravimetría, separación magnética, lixiviación en pilas), refinación (pirometalurgia: fusión-conversión-electrorrefinación; hidrometalurgia: lixiviación-extracción por solventes-electroobtención; cianuración con Merrill-Crowe o carbón en pulpa para oro y plata; tostación-lixiviación-electroobtención para zinc; proceso Parkes para plomo-plata; HF a partir de fluorita grado ácido; ferroaleaciones de manganeso en horno eléctrico; silicio metálico por reducción carbotérmica). La lista es un punto de partida a validar con los manuales técnicos.
2. **B2.** Qué métodos usa cada operación mexicana, con capacidad y año de instalación.
3. **B3.** Por qué esos y no otros: tipo de mineral (sulfuro u óxido), ley, geometría y profundidad del yacimiento, escala, agua y energía, subproductos y costos, según **la justificación que dan los propios documentos técnicos**.
4. **B4.** Qué tan cerca de la frontera tecnológica están las empresas mexicanas.

### B.2 Fuentes

- **Reportes técnicos NI 43-101** (SEDAR+) de las empresas que cotizan en Canadá (Torex, Alamos, Equinox, First Majestic, Capstone, entre otras). Las secciones de pruebas metalúrgicas y de métodos de recuperación (ítems 13 y 17 del formato, a verificar) describen el diagrama de flujo y su justificación.
- **10-K de Southern Copper** (concentradoras, plantas de extracción por solventes y electroobtención, fundición y refinería de Grupo México); informes anuales de **Peñoles, Fresnillo, Autlán y Orbia**.
- **SGM**: monografías geológico-mineras por estado; **USGS MYB** de México (capítulo por país).
- Manuales de referencia para el catálogo (por fichar): Wills, *Mineral Processing Technology*; Schlesinger et al., *Extractive Metallurgy of Copper*; equivalentes para zinc-plomo y metales preciosos.
- Frontera tecnológica: reportes de innovación minera (Cochilco, ICMM, IEA) y literatura sobre innovación en cadenas mineras de América Latina (por fichar).

### B.3 Método

1. **Ficha técnica por operación** (libro de códigos común con el módulo E): mineral, eslabón, método, capacidad, recuperación, año de la tecnología, proveedor tecnológico, fuente y página.
2. **Matriz mineral × eslabón × método**, con dos columnas: en el mundo y en México.
3. **B3 por análisis documental**: se codifica la razón que da cada reporte técnico para su elección de proceso (categorías: mineralogía, ley, escala, agua, energía, costos, subproductos, regulación).
4. **B4 con un índice de adopción**: se define una lista de $K$ tecnologías de frontera por eslabón (por ejemplo, selección de mineral por sensores, molienda con rodillos de alta presión, flotación de partícula gruesa, acarreo autónomo, biolixiviación; la lista se fija con la literatura) y se calcula $A_o = \frac{1}{K}\sum_{k} a_{o,k}$, donde $a_{o,k}=1$ si la operación $o$ adoptó la tecnología $k$. Se compara con operaciones de Chile, Perú y Australia, documentadas con los mismos tipos de reporte. Se complementa con patentes (módulo C) y gasto en I+D (ESIDET-INEGI e informes de empresa).

### B.4 Productos y lugar posible en la ICR

- Matriz de métodos (anexo), cuadro de adopción por empresa y eslabón, síntesis por mineral.
- Si se incluye: complemento del **Cap. V** (estructura) y de las **fichas L0-L4 del Anexo C**; o, junto con C-D-E, un capítulo nuevo de capacidades tecnológicas.

## Decisiones pendientes del alumno

- [ ] ¿A entra a la ICR (subsección de VII.3) o queda como nota aparte?
- [ ] ¿B se trabaja dentro del módulo E (recomendado, para no duplicar fichas) o por separado?
- [ ] Piloto: empezar por el **cobre**, que es el mineral mejor documentado (10-K de Southern Copper) y el que motiva la pregunta A.

← [[Ruta metodologica - Investigacion mixta (patentes, concesiones, procesos productivos)]] · [[Handoff - Estado actual (HEM, consolidado y certificacion) 2026-09-29]] · [[Bitacora]]
