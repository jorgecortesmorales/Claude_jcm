---
title: Memoria — Empresas de transformación y cadena local (Obj. 2)
type: resultados
tags: [icr, cadenas-de-valor, empresas, obj2, datos]
created: 2026-08-01
updated: 2026-08-01
status: v1-con-verificacion-parcial
---

# Memoria — Empresas de transformación y cadena local (Objetivo 2)

> [!note] Diseño descriptivo
> Identifica, **a nivel de empresa**, los procesadores/usuarios domésticos de cada mineral y responde: **¿existe cadena local?** Complementa el lado interno de la MIP ([[Memoria - Encadenamientos MIP (Leontief Ghosh Hirschman-Rasmussen)]]) y el global del comercio ([[Memoria - Comercio por etapa de procesamiento (Obj 3)]]).

## 1. Fuentes y método
- **Eslabón metalúrgico (metales)**: USGS MYB Tabla 2 (`processed/myb_estructura_industria.csv`) — ya trae fundiciones y refinerías con dueño y ubicación. **Sourced**.
- **Verificación de usuarios downstream**: reportes/directorios corporativos (web) — **Autlán** (ferroaleaciones) y **Koura/Orbia** (fluoroquímica) verificados.
- **Sectores compradores**: MIP (Cuadro V.4) y comercio por etapa (Tarea 2).
- Mapa completo: `processed/empresas_transformacion.csv` (19 firmas, con columna `confianza`: sourced-USGS / verificado-web / verificado-comercio / preliminar-por-verificar).

## 2. Hallazgo central
Para los **metales**, la transformación doméstica **existe pero es la fundición/refinación de los propios grupos extractivos** —integración vertical **hasta metal refinado**, luego exportación—:
- **Grupo México**: fundición y refinería **La Caridad** (Nacozari), fundición **Cananea**, refinería de zinc **IMMSA** (S.L.P.); + **Cobre de México** (refinería, CDMX).
- **Peñoles**: **Met-Mex Torreón** (refinación de plomo, zinc, plata y oro).

La cadena local, en los metales, **se detiene en el metal refinado**: no continúa hacia la manufactura (la joyería es importadora neta; los semis de cobre se importan en neto). Es la expresión, a nivel de empresa, del **enclave estructural**: hay transformación, pero concentrada, de propiedad de los mismos grupos y truncada en el eslabón primario/metalúrgico.

**La integración vertical explica por qué la MIP (nivel de sector) subestima la cadena local**: buena parte ocurre *dentro* de las firmas (transferencias intra-grupo) y no se ve como flujo intersectorial. El análisis de empresa **corrige** la lectura agregada —caso fluorita, abajo—.

## 3. Veredicto por mineral — ¿existe cadena local y hasta qué eslabón?

| Mineral | ¿Cadena local? | Hasta qué eslabón | Empresas clave |
|---|---|---|---|
| **Manganeso** | ✅ Sí, la más integrada | mina → **ferroaleaciones** → siderurgia | **Autlán** (Tamós, Teziutlán, Gómez Palacio) |
| **Fluorita** | ✅ Sí, hasta HF | espato → **ácido fluorhídrico (HF)**; se trunca antes de fluoropolímeros (importados) | **Koura/Orbia** (Matamoros, mayor planta de HF del mundo) |
| **Cobre** | ⚠️ Parcial | mina → **refinado** (+ algo de semis/cable); semis netos importados | Grupo México, Cobre de México; Viakable, Condumex |
| **Oro / Plata** | ⚠️ Hasta refinado | mina → **metal refinado**; joyería importadora neta | Met-Mex Peñoles |
| **Plomo-zinc** | ⚠️ Hasta refinado | mina → **refinado**; vínculo menor con baterías | Peñoles, IMMSA; Clarios/LTH |
| **Sílice** | ⚠️ Baja gama | usuarios de **vidrio y cemento**; silicio/ferrosilicio importados | Vitro, O-I; CEMEX, Holcim, GCC |
| **Grafito** | ⚠️ Débil | usuario **siderúrgico**; electrodos importados (importador neto) | AHMSA, Ternium, DeAcero (CANACERO) |
| **Barita** | ❌ Mínima | **servicios petroleros** (lodos); sin cadena manufacturera; se exporta en bruto | Halliburton, Baker Hughes, PEMEX |

## 4. Corrección relevante (2026-08-01)
La **fluorita** se había reportado como "cadena fluoroquímica ausente" (memorias Cap V y Tarea 2, columna vertebral). **Es incorrecto**: Koura opera la mayor planta de **HF** del mundo en Matamoros; México **exportó ~161 MM USD de HF en 2018**. La cadena llega al HF y se trunca antes de los **fluoropolímeros** (PTFE), que se importan. Corregido en las notas afectadas y en el docx del Cap. V. (A revisar: caída de la exportación de HF 2018→2023, de ~161 a ~6.5 MM USD.)

## 5. Confianza (las 19 firmas quedan verificadas)
- **Sourced (USGS MYB Tabla 2)**: eslabón metalúrgico de los metales (Grupo México, Peñoles, Cobre de México).
- **Verificado-web + fichado** (ago-2026): Autlán (Mn), Koura (fluorita), Viakable y Condumex (semis de cobre), Clarios/LTH (baterías), Vitro y Owens-Illinois (vidrio), CEMEX/Holcim/Cruz Azul/GCC (cemento — fluorita como mineralizador del clínker confirmado), Ternium/ArcelorMittal/DeAcero/Gerdau vía CANACERO (siderurgia EAF, grafito), PEMEX (barita, abastecida de Coahuila/Sonora). Fichas y fuentes: [[Fichas - Empresas de transformacion (Obj 2)]].
- **Verificado-comercio**: los eslabones ausentes/importados (fluoropolímeros de fluorita; silicio/ferrosilicio de sílice; electrodos de grafito).
- **Pendiente opcional**: cuantificar el tamaño de cada usuario (empleo, valor de producción) donde haya datos; revisar la caída de exportación de HF 2018→2023.

← [[Catalogo de Bases de Datos]] · [[Columna Vertebral Metodologica]] · [[Identificar empresas de transformacion]] · [[Mapear cadenas de valor locales]]
