# -*- coding: utf-8 -*-
"""Paso 5 (ruta) — georreferenciacion CUANTITATIVA: produccion por mineral x entidad (2024).
Datos transcritos de las tablas 'Produccion minera por entidad federativa' del SGM, Anuario
Estadistico de la Mineria Mexicana, edicion 2025 (leidas como imagen; paginas por mineral).
Unidades: toneladas, salvo oro/plata en kilogramos. Calcula la participacion (%) por estado y
el indice de concentracion geografica (share del estado lider) por mineral.
Salida: processed/georref_extraccion_mineral_estado_cuantitativo.csv
"""
import csv, os

# mineral -> (unidad, pagina_SGM, {estado: produccion_2024})
DATA = {
 "cobre": ("toneladas", 100, {
    "Sonora":544345.80,"Zacatecas":121335.80,"San Luis Potosi":33479.99,"Chihuahua":19844.46,
    "Coahuila":15000.00,"Baja California Sur":13978.00,"Guerrero":10881.03,"Durango":6934.01,
    "Hidalgo":3245.92,"Michoacan":2081.43,"Jalisco":1578.62,"Queretaro":1544.00,"Mexico":1133.00,
    "Oaxaca":911.09,"Sinaloa":427.00,"Aguascalientes":386.00}),
 "manganeso": ("toneladas", 104, {"Hidalgo":134110.00}),
 "oro": ("kilogramos", 106, {
    "Sonora":38360.30,"Zacatecas":37872.85,"Guerrero":19710.00,"Chihuahua":9607.54,"Durango":8108.57,
    "San Luis Potosi":2660.00,"Mexico":813.59,"Oaxaca":390.00,"Queretaro":216.54,"Sinaloa":166.00,
    "Coahuila":105.12,"Nayarit":70.00,"Aguascalientes":60.00,"Michoacan":44.88,"Hidalgo":35.66,"Jalisco":6.73}),
 "plata": ("kilogramos", 108, {
    "Zacatecas":3632404.44,"Chihuahua":1045873.90,"Sonora":835288.10,"Durango":812980.00,
    "San Luis Potosi":217660.00,"Mexico":136930.00,"Guerrero":114470.00,"Hidalgo":101680.00,
    "Jalisco":76020.00,"Guanajuato":55130.00,"Sinaloa":40980.00,"Oaxaca":31750.00,"Aguascalientes":16790.00,
    "Coahuila":96770.00,"Queretaro":1270.00,"Nayarit":5030.00}),
 "plomo": ("toneladas", 110, {
    "Zacatecas":258738.82,"Chihuahua":60609.55,"Durango":14618.63,"Hidalgo":7703.80,"Mexico":5527.34,
    "Guerrero":4326.58,"Jalisco":4052.92,"Oaxaca":3844.38,"Aguascalientes":3116.00,"San Luis Potosi":2517.08,
    "Queretaro":299.00,"Sonora":1.90}),
 "zinc": ("toneladas", 114, {
    "Zacatecas":563495.74,"Chihuahua":115878.35,"Durango":97404.99,"Sonora":78029.61,"Guerrero":32406.50,
    "Mexico":27583.70,"San Luis Potosi":27039.19,"Hidalgo":25639.97,"Coahuila":15000.00,"Oaxaca":9506.33,
    "Aguascalientes":8381.00,"Jalisco":5479.19,"Queretaro":3649.00}),
 "barita": ("toneladas", 126, {
    "Nuevo Leon":405788.00,"Sonora":265380.00,"Coahuila":13982.99,"Chihuahua":2919.00,"Oaxaca":2319.14,
    "Jalisco":1507.00,"Veracruz":494.07,"Puebla":30.00,"Chiapas":26.00}),
 "fluorita": ("toneladas", 145, {
    "San Luis Potosi":2247995.71,"Durango":71074.00,"Coahuila":31352.00}),
 "grafito": ("toneladas", 147, {"Sonora":2150.20}),
 "silice": ("toneladas", 162, {
    "Coahuila":1635148.00,"Puebla":1234257.00,"Baja California":244774.14,"Sonora":48098.39,
    "Jalisco":555.00,"Chihuahua":80.82}),
}

OUT = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed\georref_extraccion_mineral_estado_cuantitativo.csv"
rows = []
concentr = {}
for m, (unit, pag, estados) in DATA.items():
    tot = sum(estados.values())
    lider = max(estados.items(), key=lambda x: x[1])
    concentr[m] = (lider[0], lider[1]/tot*100, len(estados))
    for e, v in sorted(estados.items(), key=lambda x: -x[1]):
        rows.append(dict(mineral=m, estado=e, produccion_2024=round(v, 2), unidad=unit,
                         share_2024_pct=round(v/tot*100, 2), fuente=f"SGM Anuario 2025 p.{pag}"))

with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["mineral","estado","produccion_2024","unidad","share_2024_pct","fuente"])
    w.writeheader(); w.writerows(rows)
print(f"Escrito {OUT} ({len(rows)} filas)")
print("\nConcentracion geografica de la extraccion (2024) — estado lider:")
for m,(e,s,n) in concentr.items():
    print(f"  {m:10s} lider={e} ({s:.0f}%)  n_estados={n}")
