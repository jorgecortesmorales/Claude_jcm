# -*- coding: utf-8 -*-
"""Pregunta A (piloto cobre) — balance de cobre de ESTADOS UNIDOS, 1995-2025 (miles de t de cobre contenido).
Transcripcion de las Salient Statistics de los USGS Mineral Commodity Summaries — Copper, ediciones
2000, 2005, 2010, 2015, 2020, 2025 y 2026 (PDF y TXT en Bases Originales/07 USGS MCS/). Para cada anio
se toma la edicion MAS RECIENTE que lo reporta (cifras revisadas); el ultimo anio de una edicion sin
edicion posterior queda marcado como estimado (e).
Se agrega, para contraste, la serie DS-140 (USGS Historical Statistics, cobre refinado, 1992-2020).

Notas de definicion:
- '(2)'/'(3)' del USGS = menos de media unidad -> 0.
- Consumo aparente: hasta la edicion 2015 = 'apparent, unmanufactured'; desde 2020 = 'primary refined
  copper and copper from old scrap'. No es estrictamente la misma definicion (se marca).
Salidas: processed/cobre_eua_balance_usgs.csv y processed/cobre_eua_fuentes_importacion_usgs.csv
"""
import os, csv
import pandas as pd

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
OUT = os.path.join(BASE, "processed")
VARS = ["mina", "ref_primaria", "ref_secundaria", "imp_concentrado", "imp_refinado",
        "exp_concentrado", "exp_refinado", "consumo_aparente", "dependencia_neta_pct"]
ED = {  # edicion: (anios, {var: valores})
 2000: (range(1995, 2000), dict(mina=[1850,1920,1940,1860,1660], ref_primaria=[1930,2010,2070,2140,1870],
        ref_secundaria=[352,345,383,336,240], imp_concentrado=[127,72,44,217,150], imp_refinado=[429,543,632,683,860],
        exp_concentrado=[239,195,127,37,40], exp_refinado=[217,169,93,86,25], consumo_aparente=[2540,2830,2950,3010,3090],
        dependencia_neta_pct=[7,14,13,14,27])),
 2005: (range(2000, 2005), dict(mina=[1450,1340,1140,1120,1160], ref_primaria=[1590,1630,1440,1250,1280],
        ref_secundaria=[209,172,70,53,55], imp_concentrado=[0,46,72,27,35], imp_refinado=[1060,991,927,882,800],
        exp_concentrado=[116,45,23,9,30], exp_refinado=[94,23,26,93,120], consumo_aparente=[3100,2500,2610,2430,2640],
        dependencia_neta_pct=[37,22,37,40,43])),
 2010: (range(2005, 2010), dict(mina=[1140,1200,1170,1310,1190], ref_primaria=[1210,1210,1280,1230,1100],
        ref_secundaria=[47,45,46,53,55], imp_concentrado=[0,0,1,1,1], imp_refinado=[1000,1070,829,724,650],
        exp_concentrado=[137,108,134,301,170], exp_refinado=[40,106,51,37,90], consumo_aparente=[2400,2190,2270,2020,1660],
        dependencia_neta_pct=[42,38,37,31,24])),
 2015: (range(2010, 2015), dict(mina=[1110,1110,1170,1250,1370], ref_primaria=[1060,992,962,993,1070],
        ref_secundaria=[38,37,39,47,50], imp_concentrado=[1,15,6,3,0], imp_refinado=[605,670,630,734,600],
        exp_concentrado=[137,252,301,348,390], exp_refinado=[78,40,159,113,100], consumo_aparente=[1760,1730,1770,1770,1810],
        dependencia_neta_pct=[32,34,36,34,31])),
 2020: (range(2015, 2020), dict(mina=[1380,1430,1260,1220,1300], ref_primaria=[1090,1180,1040,1070,1000],
        ref_secundaria=[49,46,40,41,45], imp_concentrado=[0,0,14,32,35], imp_refinado=[687,708,813,778,650],
        exp_concentrado=[392,331,237,253,330], exp_refinado=[86,134,94,190,140], consumo_aparente=[1840,1880,1860,1830,1800],
        dependencia_neta_pct=[32,30,36,33,35])),
 2025: (range(2020, 2025), dict(mina=[1200,1230,1230,1130,1100], ref_primaria=[872,922,930,843,850],
        ref_secundaria=[43,49,40,39,40], imp_concentrado=[2,11,12,3,0], imp_refinado=[676,919,732,771,810],
        exp_concentrado=[383,344,351,339,320], exp_refinado=[41,48,27,33,60], consumo_aparente=[1660,1960,1820,1690,1800],
        dependencia_neta_pct=[38,44,41,41,45])),
 2026: (range(2021, 2026), dict(mina=[1230,1230,1130,1050,1000], ref_primaria=[931,917,843,882,790],
        ref_secundaria=[49,40,39,39,60], imp_concentrado=[11,12,3,0,0], imp_refinado=[919,732,771,903,1700],
        exp_concentrado=[344,351,339,326,340], exp_refinado=[48,27,29,72,110], consumo_aparente=[1970,1810,1680,1860,2200],
        dependencia_neta_pct=[44,41,42,45,57])),
}
fila = {}
for ed in sorted(ED):                      # las ediciones posteriores sobrescriben
    anios, vals = ED[ed]
    for i, y in enumerate(anios):
        fila[y] = {"anio": y, "edicion_mcs": ed, **{v: vals[v][i] for v in VARS}}
ultimo = {max(ED[ed][0]) for ed in ED}
for y, r in fila.items():
    r["estimado"] = "e" if (y in ultimo and fila[y]["edicion_mcs"] == next(ed for ed in sorted(ED) if max(ED[ed][0]) == y)
                            and not any(y in ED[ed][0] for ed in ED if ed > r["edicion_mcs"])) else ""
    r["def_consumo"] = "aparente no manufacturado" if r["edicion_mcs"] <= 2015 else "refinado primario + chatarra vieja"
df = pd.DataFrame([fila[y] for y in sorted(fila)])

# DS-140 (refinado) para contraste
ds = pd.read_excel(os.path.join(BASE, "Bases Originales", "06 USGS DS-140", "ds140-copper-2020.xlsx"), header=4)
ds = ds.rename(columns={"Year": "anio"})
ds = ds[pd.to_numeric(ds["anio"], errors="coerce").between(1992, 2020)].copy()
ds["anio"] = ds["anio"].astype(int)
ds = ds[["anio", "Primary production", "Imports", "Exports", "Apparent consumption"]]
ds.columns = ["anio", "ds140_ref_primaria", "ds140_imp_refinado", "ds140_exp_refinado", "ds140_consumo_aparente"]
for c in ds.columns[1:]:
    ds[c] = pd.to_numeric(ds[c], errors="coerce") / 1000.0
df = ds.merge(df, on="anio", how="outer").sort_values("anio")
df.to_csv(os.path.join(OUT, "cobre_eua_balance_usgs.csv"), index=False, encoding="utf-8")

# Fuentes de importacion (texto 'Import Sources' de cada edicion), % del cobre contenido
FUENTES = [
 ("1995-1998", 2000, "no manufacturado", {"Canada": 43, "Chile": 21, "Mexico": 15, "Otros": 21}),
 ("2000-2003", 2005, "no manufacturado", {"Canada": 28, "Chile": 26, "Peru": 23, "Mexico": 9, "Otros": 14}),
 ("2005-2008", 2010, "no manufacturado", {"Chile": 40, "Canada": 34, "Peru": 13, "Mexico": 6, "Otros": 7}),
 ("2010-2013", 2015, "no manufacturado", {"Chile": 51, "Canada": 26, "Mexico": 13, "Peru": 6, "Otros": 4}),
 ("2015-2018", 2020, "refinado", {"Chile": 56, "Canada": 26, "Mexico": 11, "Otros": 7}),
 ("2015-2018", 2020, "mena y concentrado", {"Mexico": 99, "Otros": 1}),
 ("2015-2018", 2020, "chatarra", {"Canada": 55, "Mexico": 33, "Otros": 12}),
 ("2020-2023", 2025, "refinado", {"Chile": 65, "Canada": 17, "Mexico": 9, "Peru": 6, "Otros": 3}),
 ("2020-2023", 2025, "mena y concentrado", {"Canada": 99, "Otros": 1}),
 ("2020-2023", 2025, "chatarra", {"Canada": 46, "Mexico": 42, "Rep. Dominicana": 3, "Otros": 9}),
 ("2021-2024", 2026, "refinado", {"Chile": 68, "Canada": 16, "Peru": 7, "Mexico": 6, "Otros": 3}),
 ("2021-2024", 2026, "mena y concentrado", {"Canada": 99, "Otros": 1}),
 ("2021-2024", 2026, "chatarra", {"Canada": 45, "Mexico": 43, "Otros": 12}),
]
with open(os.path.join(OUT, "cobre_eua_fuentes_importacion_usgs.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["periodo", "edicion_mcs", "forma", "pais", "pct"])
    for per, ed, forma, d in FUENTES:
        for p, v in d.items():
            w.writerow([per, ed, forma, p, v])
print(df[["anio", "mina", "ref_primaria", "imp_refinado", "exp_concentrado", "consumo_aparente",
          "ds140_consumo_aparente", "dependencia_neta_pct", "estimado"]].to_string(index=False))
