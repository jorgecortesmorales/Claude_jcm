---
title: "Síntesis — Patrón agregado y bases de política (cadenas de valor)"
type: sintesis
tags: [icr, cadena-de-valor, sintesis, politica-industrial, enclave, fase-8]
created: 2026-09-09
updated: 2026-09-09
status: escalado
---

# Síntesis — Patrón agregado de las 10 cadenas y bases de política (Fase 8)

> [!abstract] Idea central
> Al mapear las 10 cadenas de valor locales (Fases 1–7), **domina el tipo B —truncada en el metal—** (5 de 10): la cadena existe hasta el metal/refinado pero no profundiza hacia semimanufactura y manufactura, y el mineral tiende a salir en bruto. Es la huella empírica del **enclave estructural**: capital que puede ser nacional, pero **desconectado aguas abajo**. Los dos casos tipo A (manganeso→ferroaleación; fluorita→HF) prueban que la transformación con capital nacional es viable, aunque se detenga en el intermedio o —en la fluorita— opere como **enclave de exportación**.

## 1. El patrón

| Tipo | Definición | Minerales | n |
|---|---|---|---:|
| **A** | Cadena local desarrollada (L1–L3 conectados) | manganeso; **fluorita** (límite A/B) | 2 |
| **B** | Truncada en el metal (L1–L2 sí, L3–L4 no/exportados) | cobre, oro, plata, plomo, zinc | 5 |
| **C** | Usuario doméstico con eslabón importado | grafito, sílice | 2 |
| **D** | Exportación / uso en bruto (se detiene en L1) | barita | 1 |

**Tres lecturas transversales:**
1. **El sistema estadístico casi no distingue la transformación por mineral.** Sólo el cobre tiene una clase SCIAN dedicada aguas abajo (331411 fundición, 331420 laminación). Oro-plata comparten 331412; plomo-zinc y otros no ferrosos comparten 331419; el manganeso comparte 331112 con la siderurgia; el HF de la fluorita se diluye en "químicos básicos inorgánicos" (325180). *La invisibilidad estadística de los eslabones es, en sí, un síntoma del enclave.*
2. **Co-localización rara.** Sólo el cobre tiene la fundición junto a la mina (La Caridad, Sonora). En el resto, extracción y transformación están deslocalizadas — y en la fluorita la planta de HF está en la **frontera** (Matamoros), mirando a la exportación. Existe, sin embargo, una **cadena metalúrgica nacional** real (extractivos del centro-norte → fundición de Coahuila/SLP/NL: Peñoles, IMMSA), que matiza la idea de "fuga total". ([[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)|georref §3bis-3ter]])
3. **Arrastre aguas adelante alto pero mal realizado.** Varios minerales tienen Ghosh/forward elevado (sílice 1.92, grafito 1.71, manganeso 1.54) porque son insumos de industrias grandes; pero ese empuje se **realiza como exportación de metal o como importación del eslabón procesado**, no como cadena local. ([[mip_encadenamientos_minerales]])

## 1bis. Geografía de la cadena y del comercio

El mapa de conjunto resume las dos dimensiones espaciales del enclave: **dónde se extrae y se transforma** (México) y **hacia/desde dónde comercia** el bloque.

![[mapa_conjunto.png]]

- **Extracción**: concentrada en el centro-norte —Zacatecas, Durango, Sonora y Chihuahua son los estados multi-mineral—; **transformación** en unos pocos hubs metalúrgicos (Nacozari/Cananea, Torreón, San Luis Potosí, Matamoros, Molango-Tamós, Monterrey, CDMX), casi siempre bajo la firma que extrae.
- **Dos geografías de comercio**: los **concentrados (E1) se van a Asia** —el cobre a China (71 %), el plomo y el zinc a China/Corea—, mientras los **productos con algo de proceso y los metales preciosos van a Estados Unidos** (plata 95 %, oro 76 %, ferromanganeso 96 %, HF 94 %). En el agregado del bloque, EE.UU. concentra ~58 % de las exportaciones (lo procesado) y China ~32 % (lo crudo); del lado de las **importaciones**, EE.UU. (68 %) y China surten los eslabones que México no fabrica (semis de cobre, silicio, electrodos de grafito, fluoropolímeros).
- La lectura es nítida: **el valor sale con el concentrado hacia el procesador asiático y regresa —procesado— desde el norte**. Los mapas por mineral (uno por ficha) detallan cada caso; todos en `13 Entregables/mapas/`.

## 2. Bases descriptivas de política por tipo

*No es un modelo causal ni un recetario: es dónde una política que quisiera prolongar la cadena tendría que intervenir, según lo que cada tipo revela.*

| Tipo | Dónde se rompe | Palanca descriptiva (dónde intervendría) |
|---|---|---|
| **A** (Mn, fluorita) | en el intermedio (química fina de Mn; fluoropolímeros) | consolidar el eslabón siguiente al que ya existe; en fluorita, reconectar el HF (hoy enclave de exportación) con una química nacional de flúor |
| **B** (Cu, Au, Ag, Pb, Zn) | metal→semis (se exporta concentrado/metal, se importan semis) | capturar la semimanufactura (alambrón/laminados) aprovechando la refinación que ya existe; el cobre —co-localizado— es el candidato más claro |
| **C** (grafito, sílice) | insumo procesado importado pese a demanda local | sustituir importación del eslabón intermedio (electrodos de grafito; silicio) donde la industria usuaria (acero EAF, vidrio) ya jala |
| **D** (barita) | no arranca aguas abajo | caso de baja prioridad de encadenamiento (mercado chico, ligado al ciclo petrolero) |

## 3. Contrafactual internacional (Paso 6.6)

La comparación a 8 países ([[Memoria - Comparacion internacional (Chile, Australia) encadenamientos|comparación internacional]]) da la vara: **México y China tienen un Ghosh casi idéntico (1.51 vs 1.53) pero un perfil de exportación opuesto** (crudo 0.38 vs 0.07) — China transforma dentro, México exporta más en bruto. El **modelo nórdico** (Finlandia/Suecia) muestra encadenamiento profundo con reprocesamiento doméstico; **Perú** es el enclave más puro. México queda en una posición intermedia: **tiene refinación (no es Perú) pero no cierra la cadena (no es China ni los nórdicos)** — exactamente lo que predice la tipología B dominante.

## Fuentes / archivos
`processed/cv_tipologia.csv` · `processed/cv_eslabones_cuantificado.csv` · [[mip_encadenamientos_minerales]] · [[comercio_posicion_resumen]] · [[icio_comparacion_mineria]] · [[Memoria - Georreferenciacion y destinos (extraccion, transformacion, exportacion)]]

← [[Indice - Fichas de Cadena de Valor]] · [[Ruta metodologica - Construccion de cadenas de valor locales por mineral]] · [[Home]]
