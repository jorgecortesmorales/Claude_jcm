# -*- coding: utf-8 -*-
"""Pregunta A (piloto cobre) — concentrado de cobre exportado por el puerto de Guaymas.
Transcripcion de los anuarios estadisticos por puerto de la Direccion General de Puertos y Marina Mercante
(gob.mx; Bases Originales/17 Puerto Guaymas/PASOGU00.pdf = 2020, PASOGU00-1.pdf = 2022), tablas
"Productos principales por pais de destino - Exportacion" y "por entidad de origen - Exportacion".
Se compara con la exportacion nacional de concentrado de cobre de Mexico (Comtrade, HS 2603, peso neto) para
obtener una cota inferior del concentrado embarcado en Guaymas que no es exportacion mexicana:
    cota_inferior = exportacion_guaymas - exportacion_nacional_mexico
(si todo el concentrado mexicano saliera por Guaymas, lo que excede el total nacional no puede ser mexicano).
Salidas: processed/guaymas_concentrado_cobre.csv, processed/guaymas_concentrado_cobre_destinos.csv
"""
import os
import pandas as pd

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
OUT = os.path.join(BASE, "processed")

# toneladas; granel mineral + contenerizada, trafico de altura (exportacion)
GUAYMAS = {2020: dict(granel=1932232, contenedor=4027, fuente="DGPMM, anuario por puerto 2020 (PASOGU00.pdf), pp. 30-37"),
           2022: dict(granel=1791125, contenedor=0, fuente="DGPMM, anuario por puerto 2022 (PASOGU00-1.pdf), pp. 20-23")}
DEST = [  # anio, pais, toneladas (concentrado de cobre, granel + contenedor)
    (2020, "China", 1516881 + 3353), (2020, "Japón", 132314), (2020, "Filipinas", 117742), (2020, "España", 112199),
    (2020, "Corea del Sur", 21803), (2020, "Países Bajos", 20792), (2020, "Chile", 10502), (2020, "Sudáfrica", 674),
    (2022, "China", 1127502), (2022, "Japón", 465729), (2022, "Perú", 95997), (2022, "España", 75164), (2022, "Alemania", 10777), (2022, "Filipinas", 10764), (2022, "Canadá", 5192),
]
mx = pd.read_csv(os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade", "comercio_e1_valor_peso_comtrade_mx_1992_2025.csv"))
mx = mx[mx.hs.astype(str).str.startswith("2603")].drop_duplicates(["anio"]).set_index("anio")
filas = []
for a, g in GUAYMAS.items():
    tot = g["granel"] + g["contenedor"]
    nac = mx.loc[a, "peso_neto_kg"] / 1000.0
    filas.append(dict(anio=a, guaymas_export_concentrado_t=tot, mexico_export_nacional_concentrado_t=round(nac),
                      cota_inferior_no_mexicano_t=round(tot - nac), cota_inferior_pct=round((tot - nac) / tot * 100, 1),
                      fuente=g["fuente"]))
res = pd.DataFrame(filas)
res.to_csv(os.path.join(OUT, "guaymas_concentrado_cobre.csv"), index=False, encoding="utf-8")
d = pd.DataFrame(DEST, columns=["anio", "pais_destino", "toneladas"])
d["pct_del_anio"] = (d.toneladas / d.anio.map({a: g["granel"] + g["contenedor"] for a, g in GUAYMAS.items()}) * 100).round(1)
d.to_csv(os.path.join(OUT, "guaymas_concentrado_cobre_destinos.csv"), index=False, encoding="utf-8")
print(res.to_string(index=False)); print(d.to_string(index=False))
