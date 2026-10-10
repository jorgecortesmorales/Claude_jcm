---
title: "Memoria — Preguntas B y E: métodos de extracción, concentración y refinación del cobre (piloto)"
type: memoria
tags: [icr, cobre, procesos, tecnologia, frontera, pregunta-b, modulo-e, exploratorio]
created: 2026-10-12
updated: 2026-10-12
status: resultados preliminares (piloto)
inclusion_icr: por definir
---

# Memoria — Preguntas B y E: procesos del cobre (piloto)

> [!info] Alcance
> Primer levantamiento de B y E con el cobre como piloto ([[Ruta metodologica - Preguntas A y B (cobre-EUA; metodos y frontera tecnologica)]], [[Ruta metodologica - Investigacion mixta (patentes, concesiones, procesos productivos)]]). Es una **actividad paralela a la ICR**; no se ha decidido incorporarla. Los resultados son descriptivos y se apoyan en documentos de las empresas, con la cita que sustenta cada dato en los CSV.

## 1. Documentos usados

| País | Operación | Documento | Tipo |
|---|---|---|---|
| México | Buenavista del Cobre, La Caridad | Grupo México, Informe Anual BMV 2025; SCC, TRS S-K 1300 (datos a 2022) | Informe anual y reporte técnico |
| Perú | Toquepala, Cuajone, Ilo | Grupo México 2025; SCC, TRS S-K 1300 (datos a 2022) | Informe anual y reporte técnico |
| Chile | Escondida | BHP, TRS S-K 1300 (FY2022) | Reporte técnico |
| Brasil | Salobo | Vale, TRS S-K 1300 (datos a 2021) | Reporte técnico |
| Suecia | Aitik, Rönnskär | Boliden, informe de recursos y reservas Aitik 2025 (PERC); Boliden Mineral AB, informe anual 2024 | Informe técnico y anual |
| Finlandia | Kevitsa | Boliden, informe de recursos y reservas Kevitsa 2025 (PERC) | Informe técnico |
| China | Dexing, Guixi | Jiangxi Copper, informe anual 2025 (HKEX) | Informe anual |
| Australia | — | Pendiente: no se obtuvo un documento técnico comparable | — |

Los reportes técnicos S-K 1300 (SEC) se descargaron de copias en minedocs.com y finboard.net, porque la SEC bloquea la descarga directa. Los documentos están en `10 Datos/Bases Originales/19 Procesos cobre/` y `16 Empresas cobre EUA-MX/`.

## 2. Procesos por operación (B2)

| Operación | Concentración | Hidrometalurgia | Fundición y refinación |
|---|---|---|---|
| Buenavista (México) | Dos concentradoras: 82 000 y 115 000 t/día | ESDE: tres plantas descritas (30, 120 y 328 t de cátodo/día) | Sin fundición propia; concentrado a La Caridad o exportado |
| La Caridad (México) | 94 500 t/día | ESDE: 21 900 t/año | Horno flash, convertidor El Teniente y convertidores convencionales (1 000 000 t de concentrado/año); refinería de 300 000 t/año; alambrón |
| Toquepala (Perú) | Dos de 60 000 t/día; HPGR | ESDE: 56 336 t/año; lixiviación de sulfuros primarios de baja ley | Concentrado a Ilo |
| Cuajone (Perú) | 90 000 t/día; HPGR desde 2013 | — | Concentrado a Ilo |
| Ilo (Perú) | — | — | ISASMELT y convertidores Peirce-Smith; captura de azufre de más de 92 %; agua de mar desalinizada |
| Escondida (Chile) | Tres concentradoras de sulfuros | Lixiviación de óxidos y biolixiviación de sulfuros | Sin fundición; dos desaladoras |
| Salobo (Brasil) | 36 Mt/año; HPGR; Vertimills; columnas | — | Sin fundición |
| Aitik (Suecia) | No detallada | — | Concentrado a Rönnskär (Boliden), que también recicla chatarra electrónica |
| Kevitsa (Finlandia) | No detallada | — | — |
| Guixi (China) | — | — | Fusión flash (primera línea completa en China, según la empresa) |

Todas las operaciones revisadas se explotan a **tajo abierto**. En México, Grupo México integra en Sonora todos los eslabones hasta el alambrón (La Caridad). Escondida y Salobo exportan concentrado sin fundición en el sitio.

## 3. Tecnologías de frontera (B4)

Lista de trabajo de 15 tecnologías (T01-T15, `pbe_frontera_menciones.py`), por validar con la literatura. Cada mención automática se revisó a mano; una mención no equivale a adopción.

| País | Adoptadas (documentadas) | En implementación, proyecto o estudio | Mención genérica |
|---|---|---|---|
| México | 2: fusión flash y captura de azufre (La Caridad) | 1: relaves filtrados (recomendación de Golder) | 1: celdas Jameson usadas en la limpieza del electrolito, no en flotación |
| Perú | 5: HPGR (Toquepala y Cuajone), lixiviación de sulfuros primarios (Toquepala), agua desalinizada y captura de azufre (Ilo) | 2: relaves filtrados (Toquepala y Cuajone) | — |
| Chile | 2: agua desalinizada y biolixiviación de sulfuros (Escondida) | — | 1: IA |
| Brasil | 2: HPGR y molienda vertical (Salobo) | — | — |
| Suecia | 2: trituración en el tajo con bandas (Aitik) y reciclaje de chatarra electrónica (Rönnskär) | 1: acarreo autónomo (Aitik) | — |
| Finlandia | 1: acarreo con trolley (Kevitsa) | — | — |
| China | 1: fusión flash (Guixi) | 1: iniciativa de IA | — |

El TRS de Buenavista disponible (63 páginas) no menciona ninguna de las 15 tecnologías.

## 4. Razones de elección declaradas (B3)

| Categoría | Casos documentados |
|---|---|
| Características del yacimiento | Tajo abierto en La Caridad y Buenavista: «due to the proximity of the ore to the surface and the physical characteristics of the deposit» |
| Ley del mineral | La Caridad: más de 0.30 % de cobre a la concentradora; de 0.15 a 0.30 % a lixiviación; ESDE «best available process … low-grade ore». Toquepala: ley de corte por proceso |
| Mineralogía | La Caridad: flotación para la calcocita, «the best available technology at the time». Salobo: HPGR en lugar de molienda SAG por el contenido de magnetita |
| Economía del plan minero | Escondida: concentradora para sulfuros para «maximise net present value»; mineral mixto a lixiviación por menor disponibilidad de óxidos |
| Antigüedad del equipo | Buenavista: la segunda concentradora se construyó 30 años después, con equipo moderno |
| Condiciones del sitio | La Caridad: relaves filtrados recomendados «due to the site conditions» |

## 5. Límites

- **Documentos heterogéneos.** Los TRS S-K 1300 (México, Perú, Chile, Brasil) describen los procesos con más detalle que los informes PERC de Boliden y el informe anual de Jiangxi Copper. El número de tecnologías documentadas depende del documento y no permite ordenar a los países.
- **Fechas distintas**: los datos van de 2021 a 2025, según el documento.
- **Una operación por país** en Chile, Brasil, Suecia, Finlandia y China; Australia, pendiente.
- **La lista de tecnologías** es de trabajo; falta validarla con la literatura sobre innovación minera.
- **El TRS de Buenavista** disponible parece incompleto (63 páginas, frente a más de 250 en los demás TRS de SCC).

## Trazabilidad

| Producto | Script | Salida |
|---|---|---|
| Menciones automáticas de 15 tecnologías | `10 Datos/scripts/pbe_frontera_menciones.py` | `processed/cobre_frontera_menciones.csv` |
| Catálogo, fichas, matriz verificada, razones | `10 Datos/scripts/pbe_cobre_fichas.py` | `processed/cobre_procesos_catalogo.csv`, `cobre_procesos_operaciones.csv`, `cobre_frontera_matriz.csv`, `cobre_procesos_razones.csv` |

← [[Control - Investigacion complementaria (A-E)]] · [[Bitacora]]
