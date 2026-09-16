---
title: Mensaje de arranque — Extracción HHI hacia atrás
type: proyecto
tags: [icr, proyecto, arranque]
created: 2026-07-18
status: para-copiar-en-sesion-nueva
---

# Mensaje de arranque para sesión nueva

Copiar todo lo que está debajo de la línea y pegarlo como primer mensaje en una sesión nueva de Claude Code (modelo ligero).

---

## Contexto del proyecto

Estoy construyendo la base de datos B5 (HHI por mineral-año) para mi tesis de maestría en Economía (UAM Azcapotzalco). El proyecto vive en `C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR`. La base acumula participación de mercado del productor líder por mineral, extraída de los Informes Anuales de CAMIMEX (PDFs en `ICR/10 Datos/Bases Originales/08 CAMIMEX Informes Anuales/`).

## Estado actual

El archivo maestro es `ICR/10 Datos/processed/hhi_numeradores.csv` (331 filas, 14 columnas). Ya cubre **2019-2024** para los 10 minerales del corpus (oro, plata, cobre, zinc, plomo, manganeso, barita, fluorita, sílice, grafito).

## Tarea

Continuar la extracción **hacia atrás**: años-dato **2018, 2017, 2016, 2015** (de los Informes CAMIMEX 2019, 2018, 2017, 2016 respectivamente) y luego **2014-2004** (informes 2015-2005). Cada informe reporta el año previo (ej: info_2019.pdf → datos de 2018).

## Convenciones a seguir estrictamente

1. **Para los 5 metales** (oro, plata, cobre, zinc, plomo): extraer de la narrativa del capítulo correspondiente la **participación por empresa del líder** (% publicado por CAMIMEX) y el **orden de los siguientes** productores. NO es necesario renderizar imágenes de las tablas de minas — basta con el texto. Registrar el total nacional cuando CAMIMEX lo publique (o calcularlo desde INEGI B3 en `ICR/10 Datos/raw/csv/2_produccion_y_precios/Volumen.csv`).

2. **Manganeso**: siempre = Compañía Minera Autlán, 100% (monopolio constante 1993-2025).

3. **Barita**: buscar "Baramin" o "mayor productor" en el capítulo de barita. Registrar producción de Baramin y total nacional (INEGI B3, columna 10 del Volumen.csv). Calcular participación.

4. **Fluorita**: Koura (antes Mexichem) = monopolio de facto (~100%). Confirmar que sigue siendo "la principal/única empresa productora" en cada informe. Total nacional = INEGI B3 columna 11.

5. **Sílice**: buscar "Grupo Materias Primas" o "mayor productor" en el capítulo de arena sílica. Registrar producción de GMP y total nacional (INEGI B3, columna 12). Calcular participación. NOTA: la sílice está **concentrada** (GMP/Covia domina 74-99%), NO es fragmentada.

6. **Grafito**: CAMIMEX no lo desglosa. Registrar como "atomizado, CAMIMEX no desglosa, caso de contraste".

## Formato de cada fila del CSV (14 columnas)

```
mineral,anio_dato,nivel,unidad_minera,empresa,estado,volumen,unidad_volumen,participacion_pct,total_nacional,unidad_total,fuente,pagina,nota
```

Para nivel empresa (que es lo que registramos de 2020 hacia atrás):
```
Cobre,2018,empresa,,Grupo Mexico,,577580,toneladas,78.8,732863,toneladas,Informe CAMIMEX 2019,,Narrativa: mayor productor 78.8%
```

## Verificaciones automáticas tras cada año

Después de registrar un año-dato, correr:
```bash
awk -F, 'NR>1 {c[$2]++} END {for(y in c) print y": "c[y]}' ICR/10\ Datos/processed/hhi_numeradores.csv | sort
```
Para confirmar que el año se agregó con las filas esperadas (~10 por año: 5 metales + manganeso + barita + fluorita + sílice + grafito).

## Informes ya convertidos a texto

Los archivos `info_YYYY.txt` ya existen en la carpeta de CAMIMEX (convertidos con pdftotext). Si alguno no existe, convertirlo con:
```bash
export PATH="$PATH:/c/Users/Jorge/AppData/Local/Microsoft/WinGet/Packages/oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe/poppler-25.07.0/Library/bin"
pdftotext -layout "ICR/10 Datos/Bases Originales/08 CAMIMEX Informes Anuales/info_YYYY.pdf" "ICR/10 Datos/Bases Originales/08 CAMIMEX Informes Anuales/info_YYYY.txt"
```

## Cómo localizar los capítulos en cada informe

```bash
grep -nE "por (compa|empresa)|mayor productor|participaci.n de [0-9]" info_YYYY.txt | grep -iE "oro|plata|cobre|zinc|plomo"
grep -iE "baramin|koura|grupo materias primas|arena s.lica" info_YYYY.txt
```

## Puntos de atención

- Los informes anteriores a ~2015 son más delgados en datos por empresa. Si un mineral no tiene % del líder publicado, registrar el orden (1°, 2°…) y poner "sin % publicado" en la nota.
- Oro y plata: CAMIMEX los reporta en onzas, INEGI en toneladas — usar el % publicado por CAMIMEX directamente, no intentar dividir volúmenes.
- Zinc 2019: Peñoles fue líder pero sin % publicado (ya registrado así).
- El informe 2020 (datos 2019) y el 2021 (datos 2020) ya están procesados — no repetirlos.
- Barita 2019: CAMIMEX 2020 dice "Baramin produjo 235 mil toneladas en 2019" — eso es dato 2019, verificar si ya está registrado o registrarlo.
- Al terminar cada bloque de 2-3 años, actualizar la bitácora (`ICR/00 Proyecto/Bitacora.md`).

## Arrancar con

Año-dato **2018** (Informe CAMIMEX 2019, archivo `info_2019.txt` o `info_2019.pdf`).
