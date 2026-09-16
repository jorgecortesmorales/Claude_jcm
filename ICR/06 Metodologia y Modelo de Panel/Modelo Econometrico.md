---
title: Modelo Econométrico
type: metodologia
tags: [icr, metodologia, econometria]
created: 2026-07-16
status: aprobada-en-protocolo
---

> [!warning] Reencuadre pendiente (2026-07-23) — diseño descriptivo
> El proyecto pasó de un diseño causal (panel HHI→Ghosh) a uno **descriptivo de cadenas de valor**. Esta nota aún refleja el enfoque causal y se reescribirá en la fase de capítulos. Ver [[Protocolo v3 - Rediseño descriptivo (cadenas de valor)]] y [[Columna Vertebral Metodologica]].


# Modelo Econométrico (Cap. VI — especificación base, Protocolo sección 5)

## Especificación
$$FL_{jt} = \beta_0 + \beta_1 HHI_{jt} + \beta_2 PrecioIntl_{jt} + \beta_3 CAPEX_{jt} + \beta_4 CapExtran_j + \alpha_j + \gamma_t + \varepsilon_{jt}$$

Donde:
- **FLⱼₜ**: coeficiente de Ghosh del mineral *j* en el periodo *t* (variable dependiente principal).
- **HHIⱼₜ**: Índice de Herfindahl-Hirschman (variable independiente clave, [[Sintesis Comparativa|ver valores por mineral]]).
- **PrecioIntlⱼₜ**: controla el ciclo de precios internacionales de materias primas.
- **CAPEXⱼₜ**: inversión de capital de las empresas dominantes.
- **CapExtranⱼ**: proporción de capital extranjero de las empresas dominantes.
- **αⱼ**: efectos fijos de mineral. **γₜ**: efectos fijos de año. **εⱼₜ**: error.

**Hipótesis central**: β₁ < 0 y estadísticamente significativo (ver [[Hipotesis|H1]]).

## Estrategia de identificación (declarada ex ante)
1. **MCO con efectos fijos de doble vía** + errores estándar agrupados por mineral — especificación principal.
2. **Efectos aleatorios** — robustez A, condicional a que la prueba de Hausman no rechace exogeneidad de los efectos.
3. **Estimador de Mundlak** — robustez B.
4. **Misma secuencia con CCV como variable dependiente alternativa** — robustez C, panel ampliado a hasta 320 observaciones (10 minerales × 32 años).

## Resultado si β₁ no es significativo
Se reporta como hallazgo válido que desplaza el peso explicativo hacia el marco institucional (Cap. VII) — el diseño no depende de confirmar H1.

## Estado
⏳ Pendiente de estimación — depende de que [[Capitulo 5 - Diagnostico Insumo Producto|Cap. V]] produzca los coeficientes de Ghosh (dependencia técnica declarada en el cronograma del protocolo).

← [[Home]] · [[Variables y Datos]] · Fuente: Protocolo, sección 5
