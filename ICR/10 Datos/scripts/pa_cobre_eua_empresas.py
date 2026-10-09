# -*- coding: utf-8 -*-
"""Pregunta A (piloto cobre), paso por empresa.
1) Espejo EUA -> Mexico: exportaciones de EUA a Mexico (Comtrade, EUA reportante) frente a importaciones de
   Mexico desde EUA (Comtrade, Mexico reportante), partidas 2603 (concentrado) y 7403 (refinado), 1992-2024.
2) Transacciones de Southern Copper Corp. (operaciones en Mexico) con Asarco LLC, 2013-2025, transcritas de
   la nota de partes relacionadas de los 10-K (SEC EDGAR), millones de USD.
Entradas: Bases Originales/11 Comercio Comtrade/comercio_cobre_eua_1992_2024_crudo.csv (pa_cobre_eua_comtrade.py)
          Bases Originales/11 Comercio Comtrade/comercio_cobre_mx_importaciones_1992_2024_crudo.csv (pa_cobre_mx_importaciones.py)
Salidas:  processed/cobre_eua_mx_espejo_bilateral.csv, processed/scc_asarco_transacciones.csv
"""
import os
import pandas as pd

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
RAW = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade")
OUT = os.path.join(BASE, "processed")

u = pd.read_csv(os.path.join(RAW, "comercio_cobre_eua_1992_2024_crudo.csv"))
m = pd.read_csv(os.path.join(RAW, "comercio_cobre_mx_importaciones_1992_2024_crudo.csv"))
filas = []
for hs, forma in [(2603, "concentrado"), (7403, "refinado")]:
    x = u[(u.hs4 == hs) & (u.flujo == "X") & (u.socio_m49 == 484)].groupby("anio")[["valor_usd", "peso_kg"]].sum()
    xt = u[(u.hs4 == hs) & (u.flujo == "X") & (u.socio_m49 == 0)].groupby("anio")["valor_usd"].sum()
    mi = m[(m.hs4 == hs) & (m.socio_m49 == 842)].groupby("anio")[["valor_usd", "peso_kg"]].sum()
    mt = m[(m.hs4 == hs) & (m.socio_m49 == 0)].groupby("anio")["valor_usd"].sum()
    d = pd.DataFrame({"eua_x_a_mx_musd": x.valor_usd / 1e6, "eua_x_a_mx_kt": x.peso_kg / 1e6,
                      "eua_x_total_musd": xt / 1e6,
                      "mx_m_desde_eua_musd": mi.valor_usd / 1e6, "mx_m_desde_eua_kt": mi.peso_kg / 1e6,
                      "mx_m_total_musd": mt / 1e6})
    d["cociente_mx_m_sobre_eua_x"] = d.mx_m_desde_eua_musd / d.eua_x_a_mx_musd
    d.insert(0, "forma", forma)
    filas.append(d.reset_index())
esp = pd.concat(filas).round(3)
esp.to_csv(os.path.join(OUT, "cobre_eua_mx_espejo_bilateral.csv"), index=False, encoding="utf-8")

# --- Southern Copper: compras y ventas a Asarco LLC (nota de partes relacionadas, 10-K) ---
FUENTE = {2015: "10-K FY2015 (0001104659-16-100568)", 2017: "10-K FY2017 (0001047469-18-001211)",
          2019: "10-K FY2019 (0001558370-20-001781)", 2021: "10-K FY2021 (0001558370-22-002968)",
          2024: "10-K FY2024 (0001558370-25-002017)", 2025: "10-K FY2025 (0001104659-26-021492)"}
TX = [  # anio, compras a Asarco, ventas a Asarco, 10-K del que se toma (el mas reciente que lo reporta)
    (2013, 98.0, 88.7, 2015), (2014, 47.9, 24.7, 2015), (2015, 32.0, 72.3, 2017), (2016, 30.3, 37.1, 2017),
    (2017, 37.2, 96.2, 2019), (2018, 37.2, 81.8, 2019), (2019, 37.6, 11.3, 2021), (2020, 233.9, 77.9, 2021),
    (2021, 31.3, 33.4, 2021), (2022, 66.3, 48.0, 2024), (2023, 30.4, 39.6, 2025), (2024, 4.7, 38.0, 2025),
    (2025, 71.5, 51.8, 2025)]
CONT = {  # descripcion textual de lo comprado / vendido, segun el 10-K del anio
    2015: ("chatarra y otro mineral residual de cobre", "catodos, alambron y anodos; acido sulfurico, plata, oro y cal"),
    2019: ("chatarra y otro mineral residual de cobre", "catodos y alambron; acido sulfurico, plata y oro"),
    2020: ("concentrado de cobre y lodos anodicos; servicios de maquila", "concentrado de cobre; acido sulfurico, plata y oro"),
    2021: ("concentrados de cobre y alambron; servicios de maquila", ""),
    2024: ("concentrados de cobre, laminas iniciales, catodos, barras y un activo fijo; servicios de maquila", ""),
    2025: ("concentrados de cobre, laminas iniciales, catodos, barras y un activo fijo; servicios de maquila", ""),
}
tx = pd.DataFrame([dict(anio=a, compras_a_asarco_musd=c, ventas_a_asarco_musd=v, fuente=FUENTE[f],
                        compras_descripcion=CONT.get(a, ("", ""))[0], ventas_descripcion=CONT.get(a, ("", ""))[1])
                   for a, c, v, f in TX])
tx.to_csv(os.path.join(OUT, "scc_asarco_transacciones.csv"), index=False, encoding="utf-8")
e = esp[esp.forma == "concentrado"].merge(tx[["anio", "compras_a_asarco_musd"]], on="anio", how="left")
print(e[e.anio >= 2005][["anio", "eua_x_a_mx_musd", "mx_m_desde_eua_musd", "cociente_mx_m_sobre_eua_x", "compras_a_asarco_musd"]].round(2).to_string(index=False))
