---
title: "Resumen descriptivo de la investigación (datos e indicadores)"
type: sintesis
tags: [icr, resumen, indicadores, ccv, hhi, ghosh, comercio, cadenas-de-valor, enclave]
created: 2026-09-05
updated: 2026-09-05
status: hecho
---

# Resumen descriptivo de la investigación — qué calculamos, con qué fórmulas y qué muestran los datos

> [!info] Propósito
> Síntesis **descriptiva** (no analítica) de la fase de datos de la tesis: los indicadores construidos, sus fórmulas y los datos resultantes. Es la base textual de la **infografía interactiva** y de las **presentaciones**. Concepto ordenador: **enclave estructural** (desconexión aguas abajo con capital nacional). 10 minerales, 1992-2025.

> [!note] Versión completa y entregables (actualizado 2026-09-05)
> El documento **completo** —con la matemática de cada cálculo desarrollada y el **guion diapositiva por diapositiva** de la presentación del protocolo— es `13 Entregables/Resumenes descriptivos/Resumen descriptivo - datos e indicadores 2026-09-05.docx`. Las versiones fechadas se archivan en `13 Entregables/Resumenes descriptivos/` (historial); para generar una nueva, subir la constante `FECHA` en `build_resumen_docx.py`. Entregables (archivados por fecha en subcarpetas de `13 Entregables/`; índice en `Historial de entregables.md`): **presentación de avances / protocolo** (`Presentaciones de avances/presentacion_protocolo 2026-09-05.html`, Artifact), **infografía de datos** con evolución temporal (`Infografias/infografia_indicadores 2026-09-05.html`), la **presentación que da formato de presentación a la infografía** (`Presentaciones de infografia/`), y esta síntesis. Gráficos temporales en `13 Entregables/png_charts/` (`hhi_traj`, `ghosh_cortes`, `comercio_evo`).

## 1. Marco: las cuatro fases de la cadena de valor

Cada mineral se describe a lo largo de cuatro eslabones: **E1** mena/concentrado o mineral crudo → **E2** metal refinado / mineral procesado o químico → **E3** semimanufactura → **E4** bien final. El aporte de la tesis es la **construcción de datos e indicadores** que ubican a México en esa cadena, no un modelo causal. Los indicadores son **descriptores**.

## 2. Los cuatro indicadores y sus fórmulas

### 2.1 HHI — concentración de la extracción (Objetivo 1)
Índice de Herfindahl-Hirschman de la producción minera nacional por mineral:
$$\text{HHI}_{m,t}=\sum_i s_{i,t}^2\qquad s_i=\text{participación \% del grupo } i$$
Rango 0-10,000. Umbrales: **>2,500 alta concentración**, 1,500-2,500 moderada, <1,500 baja. Serie **2004-2023**. Método: 2021-2023 con detalle por mina consolidado a grupo vs. producción nacional; **2004-2020 aproximado** (participaciones de grupo conocidas + residual atomístico; monopolios documentados = 10,000). El nivel 2004-2020 no es directamente comparable con 2021-2023: léase como **indicador de régimen**. Ver [[Catalogo de Bases de Datos]] y `hhi_consolidado.csv`.

### 2.2 Encadenamiento hacia adelante — MIP (Objetivo 1)
Sobre la Matriz Insumo-Producto del INEGI, **tres cortes: 2008 (referencia, base distinta) → 2013 → 2018**, nivel Clase SCIAN:
$$B=\text{coef. de distribución},\quad G=(I-B)^{-1}\ (\text{inversa de Ghosh})$$
$$\text{Índice hacia adelante (Rasmussen)}=\frac{\tfrac1n\sum_j g_{ij}}{\tfrac{1}{n^2}\sum_{i,j} g_{ij}}$$
Un índice >1 = el sector empuja la producción aguas abajo por encima del promedio de la economía. Se reporta además la **demanda intermedia doméstica / VBP** (qué parte del valor bruto se usa como insumo dentro del país). Backward (Leontief) $L=(I-A)^{-1}$ como complemento. Ver [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]].

### 2.3 CCV — coeficiente de captura de valor, serie continua (Objetivo 3)
Segunda operacionalización del encadenamiento hacia adelante, **anual 1992-2025** (el Ghosh es discreto):
$$\text{CCV}_{m,t}=\frac{VU^{X,E1}_{m,t}}{P^{USGS}_{m,t}}=\frac{\text{valor unitario de exportación en bruto (USD/t)}}{\text{precio del producto de referencia (USD/t)}}$$
CCV → 1: la forma exportada ya vale casi como el producto de referencia. CCV → 0: se exporta el recurso captando poco valor (rasgo de enclave). Numerador de UN Comtrade (fracciones E1, valor/peso); denominador de USGS. Ver [[Memoria - CCV (coeficiente de captura de valor, serie 1992-2025)]].

### 2.4 Comercio por etapa de procesamiento — inserción global (Objetivo 3)
$$\text{X\_share\_crudo}_{m,t}=\frac{X^{E1}_{m,t}}{X^{\text{total}}_{m,t}}\qquad\text{(participación del crudo en las exportaciones)}$$
Con su espejo del lado importador (dependencia de procesado importado). Serie **2015-2024**, UN Comtrade. Ver [[Memoria - Comercio por etapa de procesamiento (Obj 3)]].

## 3. Los datos (resultados principales)

### 3.1 HHI — concentración por mineral (último dato, 2023)
| Régimen | Minerales (HHI 2023) |
|---|---|
| **Monopolio (10,000)** | manganeso, fluorita, grafito |
| **Muy alta** | sílice 6,670 |
| **Alta** | cobre 3,764 |
| **Moderada / baja** | plomo 1,823 · zinc 1,551 · barita 1,380 · plata 914 · oro 312 |

Hallazgo de trayectoria: **barita con concentración decreciente** (líder Baramin 82%→37% de 2021 a 2023). **Fluorita: quiebre por fusión** — duopolio (~6,525) hasta 2011 → monopolio de grupo (10,000) desde enero 2012 (Koura/Orbia).

### 3.2 CCV — captura de valor en frontera (media de la serie y último año)
| Mineral | Grupo | CCV medio | Lectura |
|---|---|---:|---|
| **Cobre** | metal base | **0.224** | Estable ~0.22 en 33 años: se exporta concentrado, no cátodo. |
| **Zinc** | metal base | **0.296** | Estable ~0.30. |
| Plomo | metal base | 1.051 | Volátil (créditos de plata/oro en el concentrado). |
| Fluorita | no metálico | 0.851 | ~1: espato flúor vs. fluorita grado ácido. |
| Grafito | no metálico | 0.465 | Grafito natural vs. flake. |
| Manganeso | no metálico | 0.222 | Mena vs. referencia (1992-2014). |
| Barita / Sílice | no metálico | 1.59 / 1.98 | Prima de frontera (referencia cercana). |
| Oro / Plata | metal precioso | ≈0 / ruidoso | **No informativo** (artefacto de ley: mena bruta vs. metal puro). |

**Cobre es el descriptor de enclave por excelencia**: durante tres décadas la exportación bruta capta ~22% del valor del cobre refinado.

### 3.3 Ghosh 2018 — empuje hacia adelante e integración doméstica
| Mineral | Índice adelante (Rasmussen) | Demanda interm. dom./VBP |
|---|---:|---:|
| Sílice | 1.92 | 0.99 |
| Grafito | 1.71 | 0.88 |
| Manganeso | 1.54 | 0.78 |
| Cobre | 1.34 | 0.53 |
| Fluorita | 1.31 | 0.50 |
| Oro | 1.22 | 0.96 |
| Plata | 1.18 | 0.89 |
| Barita | 0.64 | 0.03 |
| Plomo-zinc | 0.71 | 0.14 |

Alto empuje aguas abajo donde existe industria usuaria local (sílice→vidrio, grafito→siderurgia, manganeso→química/ferroaleaciones); bajo en lo que se exporta en bruto (barita, plomo-zinc).

### 3.4 Comercio por etapa — cuánto se exporta en bruto (promedio 2020-2024)
| Exporta casi todo en **bruto** (E1) | Exporta **procesado/refinado** (E2+) |
|---|---|
| barita 100% · plomo 85% · cobre 73% · fluorita 65% · zinc 57% | oro 2% (doré) · plata 4% · grafito 2% · manganeso 0% · sílice 19% |

Patrón **espejo** nítido (exporta bruto / importa procesado) en cobre, fluorita, grafito, sílice y manganeso. En oro/plata el "procesado" es doré/bullion (forma estándar de exportación), y la joyería es importadora neta.

### 3.5 Cadena local (Objetivo 2) — ¿existe industria de transformación?
19 firmas verificadas y fichadas. Veredicto: **manganeso** (Autlán, ferroaleaciones) y **fluorita** (Koura, hasta HF) con cadena local ✅; **metales** integrados solo hasta refinado (Grupo México, Peñoles) ⚠️; **sílice/grafito** baja gama ⚠️; **barita** mínima ❌. **Caída del HF**: la exportación de ácido fluorhídrico se desplomó de ~$160M (2018) a ~$0-6M (2022-2023) — el único eslabón avanzado perdió su rol exportador tras 2020.

### 3.6 Evolución en el tiempo (síntesis)
Los indicadores no son estáticos; la dimensión temporal es parte del hallazgo:
- **HHI (2004-2023)**: la **fluorita salta a monopolio** (10,000) en 2012 por la fusión Koura/Orbia; la **barita se desconcentra** al final (líder 82%→37%, HHI ~6,800→~1,400 entre 2021 y 2023). Quiebre de método en 2020/21 (antes = régimen aproximado).
- **CCV (1992-2025)**: **estabilidad** como firma del enclave — cobre ~0.22 durante 33 años, zinc ~0.30; la posición en la cadena no se mueve con los ciclos de precio.
- **Ghosh (2008→2013→2018)**: patrón estable en la parte alta (sílice, grafito, cobre, oro > media) y baja (barita < 1); manganeso bajo en 2008 por clase más amplia (caveat de base distinta).
- **Comercio (2015-2024)**: el cobre exporta **cada vez más en bruto** (~42%→~80%); la fluorita refleja el auge y colapso del ácido fluorhídrico (pico 2021-2023, caída 2024).

## 4. Síntesis — tipología descriptiva de los mercados
- **A — cadena local desarrollada**: manganeso, fluorita (llega a ferroaleaciones / HF).
- **B — truncada en refinado**: metales base (cobre, plomo, zinc) y preciosos (oro, plata): integrados hasta metal, exportan y no siguen aguas abajo.
- **C — usuario con eslabón importado**: sílice, grafito (hay industria usuaria, pero el insumo procesado se importa).
- **D — exportación en bruto**: barita (se exporta el mineral sin transformación).

El conjunto describe un **enclave estructural**: extracción concentrada, exportación en formas de bajo valor agregado y desconexión con los eslabones industriales aguas abajo, con capital mayoritariamente nacional.

← [[Home]] · [[Mapa del Proyecto]] · [[Columna Vertebral Metodologica]]
