---
title: "Memoria — Encadenamientos por eslabón (extracción, refinación, semimanufactura)"
type: memoria
tags: [icr, encadenamientos, ghosh, eslabones, insumo-producto]
created: 2026-09-15
updated: 2026-09-15
status: vigente
---

# Encadenamientos hacia adelante por eslabón de la cadena

> [!abstract] Qué añade
> El Ghosh hacia adelante se calculaba solo para el **eslabón extractivo** (la clase minera). Aquí se calcula además para la **refinación (L2)** y la **semimanufactura (L3)**, en los tres frentes donde hay encadenamientos: nacional por mineral (MIP 2013/2018), estatal (MIP estatal 2018) e internacional (OECD ICIO 2018/2020). Permite ver **hasta qué eslabón se sostiene el arrastre hacia adelante** y desmonta que el índice extractivo, alto, implique cadena desarrollada.

## Método (idéntico en los tres frentes)
Sensibilidad de dispersión de Ghosh normalizada: fila del sector en $G=(I-B)^{-1}$, sumada y dividida entre el promedio (media = 1). Se extrae para tres eslabones:

| Eslabón | Nacional (SCIAN Clase, MIP) | Estatal (35 industrias) | Internacional (ICIO) |
|---|---|---|---|
| **L1 extracción** | clase minera 212xxx | 21-2 minería no petrolera | B07_08 menas metálicas |
| **L2 refinación** | 331411 (Cu), 331412 (Au+Ag), 331419 (Pb-Zn+no ferrosos), 331112 (ferroaleaciones)… | **331-332 (combinado)** | C24 metales básicos |
| **L3 semimanufactura** | 331420 (Cu), 331490 (no ferrosos)… | **331-332 (combinado)** | C25 productos metálicos |

Datos: `processed/mip_encadenamientos_eslabones.csv` (2008/2013/2018), `ghosh_estatal_eslabones.csv` (intra 2018), `ghosh_interestatal_eslabones.csv` (birregional 2018), `icio_eslabones_metal.csv` (2008/2013/2018/2020). Scripts: `mip_eslabones.py`, `ghosh_estatal_eslabones.py`, `ghosh_interestatal_eslabones.py`, `icio_eslabones.py`. **Cobertura de años igualada a la de los cálculos mineros** (nacional +2008 ref.; internacional 2008-2020).

## 1. Nacional por mineral (MIP 2018) — Ghosh hacia adelante (Rasmussen)

| Mineral | L1 extracción | L2 refinación | L3 semimanufactura | Clase L2 / L3 · atribuibilidad |
|---|---:|---:|---:|---|
| Cobre | 1.34 | **1.37** | 0.95 | 331411 / 331420 · **atribuible** |
| Oro | 1.22 | **0.62** | 1.02 | 331412 / 331490 · compartida (Au+Ag) |
| Plata | 1.18 | **0.62** | 1.02 | 331412 / 331490 · compartida |
| Plomo-zinc | 0.71 | 0.63 | 1.02 | 331419 / 331490 · compartida |
| Manganeso | 1.54 | 1.34 | — | 331112 · compartida (ferroaleaciones+acero) |
| Fluorita | 1.31 | 1.44 | 1.31 | 325180 / 325211 · no atribuible (agregado) |
| Grafito | 1.71 | 1.44 | 1.24 | 325180 / 327999 · no atribuible |
| Sílice | 1.92 | 1.44 | 1.34 | 325180 / 327211 · no atribuible |
| Barita | 0.64 | 1.44 | — | 325180 · no atribuible |

**Lectura.** El caso decisivo es el de los metales con clase dedicada:
- **Cobre:** la refinación (331411) tiene Ghosh **1.37**, incluso mayor que la extracción (1.34): la fundición sí alimenta industria doméstica; pero la semimanufactura (laminación, 331420) cae a **0.95** — la cadena se debilita justo en el eslabón que agregaría más valor.
- **Oro y plata:** la refinación de metales preciosos (331412) tiene Ghosh **0.62** (muy bajo): el metal refinado **no alimenta industria doméstica, se exporta como lingote**. Es la firma del enclave en el propio índice: extracción con arrastre medio → refinación sin arrastre.
- **Manganeso:** ferroaleaciones (331112) 1.34 — el eslabón transformador sí conecta con la siderurgia (caso tipo A).
- En los **no metálicos** (barita, fluorita, grafito, sílice) el eslabón L2 cae en la clase agregada de químicos (325180), no separable por mineral: su Ghosh (1.44) es de esa clase, no del mineral.

*(Cortes 2013 y 2018 en el CSV.)*

## 2. Estatal (MIP estatal 2018) — Ghosh hacia adelante por entidad y eslabón

El MIP estatal (35 industrias) **combina refinación y semis** en "331-332 industrias metálicas básicas + productos metálicos"; a esa resolución L2 y L3 no se separan. Top entidades por VBP de transformación metálica:

| Estado | Forward extracción (21-2) | Forward transformación (331-332) | VBP transformación (mdp) |
|---|---:|---:|---:|
| Coahuila | 1.61 | 1.18 | 342 365 |
| Nuevo León | 0.88 | **1.22** | 271 120 |
| San Luis Potosí | 1.40 | 1.19 | 59 931 |
| Sonora | 1.41 | 1.09 | 103 420 |
| Puebla | 0.97 | 1.10 | 40 960 |
| Querétaro | 1.03 | 1.11 | 36 272 |

**Lectura.** La **transformación metálica** con mayor arrastre está en **Coahuila y Nuevo León** (el eje siderúrgico), no donde más se extrae. Donde coexisten extracción y transformación forward-altas (Coahuila, SLP, Sonora) hay integración regional; donde la extracción es alta pero la transformación menor, el valor sale del estado (enclave regional, ver [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]] §3bis).

## 3. Internacional (OECD ICIO 2018) — Ghosh hacia adelante por país y eslabón

| País | L1 extracción (B07_08) | L2 refinación (C24) | L3 semimanufactura (C25) |
|---|---:|---:|---:|
| **China** | 1.53 | **1.30** | 1.02 |
| **México** | 1.51 | 1.17 | 1.12 |
| Finlandia | 1.31 | 1.06 | 1.14 |
| Suecia | 1.27 | 1.08 | 1.06 |
| Brasil | 0.99 | 1.19 | 1.24 |
| Australia | 0.83 | 0.83 | 1.24 |
| Chile | 0.73 | **1.23** | 1.12 |
| Perú | 0.62 | 0.98 | 1.06 |

**Lectura.** La comparación por eslabón matiza el hallazgo central. **China sostiene el arrastre de la extracción a la refinación (1.53 → 1.30)**: es el procesador integrado. **México cae más (1.51 → 1.17)**: su alto forward extractivo no se prolonga con la misma fuerza a la refinación. Chile, con extracción bajísima (0.73), tiene la refinación **más forward-integrada** (1.23) — su poca fundición sí alimenta industria—, lo que confirma que el índice extractivo aislado engaña en ambos sentidos. *Caveat: C24/C25 son toda la industria metálica del país (acero/aluminio incluidos), no solo los 10 minerales.*

## Interpretación de conjunto (enclave estructural)
Medir el Ghosh eslabón por eslabón responde a "por qué el forward extractivo es artificialmente alto" ([[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)|§4bis]]): el arrastre **no se propaga** aguas abajo de forma automática.
- Donde la refinación **alimenta industria doméstica**, el forward se sostiene (cobre 1.37; manganeso 1.34; China 1.30).
- Donde la refinación **exporta el producto** (oro/plata 0.62; extracción de Chile/Perú), el arrastre se corta.
- La **semimanufactura** casi siempre es el eslabón más débil (cobre 0.95), justo donde se agregaría más valor.

El perfil por eslabón de México —extracción alta, refinación media, semis débil— es la traducción cuantitativa del **enclave estructural**: la cadena existe pero pierde fuerza en cada paso aguas abajo, y en los metales preciosos se rompe en la propia refinación.

## Caveats
- **Atribuibilidad**: solo el cobre tiene clases SCIAN dedicadas de refinación y semis; oro-plata y plomo-zinc comparten clase; los no metálicos caen en agregados (325180) → su L2/L3 no es mineral-específico (se marca en el CSV).
- **Estatal**: 35 industrias combinan refinación y semis (no separables); intra-estatal.
- **Internacional**: sector agregado (toda la industria metálica), no por mineral; ISIC Rev.4.
- Niveles **no comparables entre años base** ni entre frentes (distinta agregación); se comparan posiciones relativas.

← [[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]] · [[Memoria - Comparacion internacional (Chile, Australia) encadenamientos]] · [[Indice Diagnostico Insumo-Producto]]
