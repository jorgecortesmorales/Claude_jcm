---
title: Diagrama — Columna vertebral metodológica (descriptivo)
type: metodologia
tags: [icr, metodologia, diagrama, columna-vertebral, cadenas-de-valor]
created: 2026-07-22
updated: 2026-07-23
status: activo
---

# Diagrama — columna vertebral metodológica (diseño descriptivo)

Algoritmo **descriptivo** de la investigación: caracterizar los mercados de los diez minerales críticos y sus cadenas de valor (local y global) para sentar las bases de una política industrial. Descripción paso a paso en [[Columna Vertebral Metodologica]]. Versión imprimible: ![[Columna Vertebral Metodologica - Diagrama.pdf]]

```mermaid
flowchart TD
    Q["<b>Pregunta central — descriptiva</b><br/>¿Cómo son los mercados de los diez minerales críticos en México<br/>—extractivo e industrial— y cómo se inserta el país en sus cadenas de valor?"]
    AP["<b>Aporte:</b> construir las bases de datos e indicadores<br/>(que hoy no existen desagregados por mineral) y usarlos para describir"]
    O1["<b>Objetivo 1 — Estructura extractiva y encadenamientos</b><br/>concentración (HHI) + Ghosh / CCV, como descriptores<br/><i>Fuentes: base B5 HHI (CAMIMEX / USGS MYB) · MIP INEGI</i>"]
    O2["<b>Objetivo 2 — Cadenas de valor locales</b><br/>¿existe industria de transformación doméstica?<br/>demanda intermedia (MIP) + identificación de empresas<br/><i>Fuentes: MIP · directorios · reportes corporativos</i>"]
    O3["<b>Objetivo 3 — Inserción en cadenas de valor globales</b><br/>posición por etapa (mena→concentrado→refinado→bien final)<br/><i>Fuentes: comercio BACI/Comtrade · opcional: TiVA / upstreamness (Antràs-Chor)</i>"]
    S["<b>Síntesis — descripción integrada de los 10 mercados</b>"]
    POL["<b>Bases para una política industrial</b><br/>(recomendaciones, como posibilidad)"]
    INST["<b>Contexto institucional</b> (transversal)<br/>reforma 2023: frenar especulación / soberanía, no industrialización<br/>entrevistas y event study opcionales"]

    Q --> AP --> O1
    O1 --> O2 --> O3 --> S --> POL
    INST -. contexto .-> S

    classDef q fill:#d3e0f0,stroke:#375a7f,color:#1a1a1a;
    classDef ap fill:#f6e9d0,stroke:#b8860b,color:#1a1a1a;
    classDef obj fill:#dce6f2,stroke:#375a7f,color:#1a1a1a;
    classDef end2 fill:#dfe9df,stroke:#2f6b3f,color:#1a1a1a;
    classDef side fill:#f0f0f0,stroke:#8a8a8a,color:#1a1a1a;
    class Q q;
    class AP ap;
    class O1,O2,O3 obj;
    class S,POL end2;
    class INST side;
```

## Cómo leerlo

- **No hay causalidad ni "puente que decide la causa".** El hilo es **descriptivo**: tres objetivos que caracterizan cada mercado (estructura extractiva → cadena local → posición global) y convergen en una síntesis.
- **Objetivo 1** retrata el lado extractivo (concentración y encadenamiento); **Objetivo 2**, si hay industria compradora doméstica; **Objetivo 3**, en qué eslabón de la cadena global participa México.
- La **síntesis** integra los tres retratos y sienta las **bases de política industrial**.
- El **marco institucional** (reforma 2023) es contexto transversal, no una palanca de industrialización.

## Fuentes por paso

| Paso | Insumo / fuente |
|---|---|
| Obj. 1 — estructura + encadenamientos | Base B5 HHI (CAMIMEX + USGS MYB Tabla 2); MIP INEGI (Leontief/Ghosh/CCV) |
| Obj. 2 — cadenas de valor locales | MIP (demanda intermedia doméstica) + directorios y reportes de empresas |
| Obj. 3 — inserción en CVG | Comercio BACI/Comtrade por etapa; opcional: OECD TiVA / upstreamness |
| Síntesis + política | Integración descriptiva de los 10 mercados |
| Contexto institucional | Reforma 2023 (documental); entrevistas / event study opcionales |

← [[Home]] · [[Columna Vertebral Metodologica]] · [[Diseno Metodologico|Diseño Metodológico]]
