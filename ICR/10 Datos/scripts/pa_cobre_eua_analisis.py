# -*- coding: utf-8 -*-
"""Pregunta A (piloto cobre) — indicadores descriptivos del comercio de cobre de EUA y el papel de Mexico.
Entrada: Bases Originales/11 Comercio Comtrade/comercio_cobre_eua_1992_2024_crudo.csv (pa_cobre_eua_comtrade.py)
         processed/comercio_destinos_serie_resumen.csv (exportaciones de Mexico por etapa y socio)
Salidas (processed/):
  cobre_eua_comercio_forma.csv  anio x flujo x forma: totales de EUA y participacion de Mexico y de los
                                principales socios (valor y peso)
  cobre_eua_shiftshare.csv      descomposicion del cambio de las importaciones de EUA desde Mexico
                                (en peso y en valor) entre 1995-1999 y 2020-2024, por forma
  cobre_eua_espejo.csv          comercio espejo: X de Mexico a EUA (Comtrade, Mexico) vs M de EUA desde Mexico
Uso: py "10 Datos/scripts/pa_cobre_eua_analisis.py"
"""
import os
import pandas as pd

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
RAW = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade", "comercio_cobre_eua_1992_2024_crudo.csv")
OUT = os.path.join(BASE, "processed")
FORMA = {2603: "concentrado", 7401: "matas y cemento", 7402: "sin refinar (blister/anodo)",
         7403: "refinado", 7404: "chatarra", 7405: "aleaciones madre"}
for h in range(7407, 7414):
    FORMA[h] = "semimanufacturas"
SOCIOS = {484: "mexico", 152: "chile", 124: "canada", 604: "peru", 156: "china", 410: "corea", 392: "japon"}

d = pd.read_csv(RAW)
d["forma"] = d["hs4"].astype(int).map(FORMA)
d = d.dropna(subset=["forma"])
g = d.groupby(["anio", "flujo", "forma", "socio_m49"], as_index=False)[["valor_usd", "peso_kg"]].sum()

tot = g[g.socio_m49 == 0].drop(columns="socio_m49").rename(columns={"valor_usd": "valor_total_usd", "peso_kg": "peso_total_kg"})
socio_sum = g[g.socio_m49 != 0].groupby(["anio", "flujo", "forma"], as_index=False)[["valor_usd", "peso_kg"]].sum()
socio_sum.columns = ["anio", "flujo", "forma", "valor_socios_usd", "peso_socios_kg"]
res = tot.merge(socio_sum, on=["anio", "flujo", "forma"], how="outer")
# si falta el renglon Mundo (o su peso), se usa la suma de socios. Comtrade no reporta peso en
# algunos anios/partidas (p. ej. chatarra 2000-2003 y 2008): ahi la participacion en peso queda vacia.
res["valor_total_usd"] = res["valor_total_usd"].fillna(res["valor_socios_usd"])
res["peso_total_kg"] = res["peso_total_kg"].where(res["peso_total_kg"] > 0, res["peso_socios_kg"])
res.loc[~(res["peso_total_kg"] > 0), "peso_total_kg"] = float("nan")
for code, nom in SOCIOS.items():
    s = g[g.socio_m49 == code][["anio", "flujo", "forma", "valor_usd", "peso_kg"]]
    s.columns = ["anio", "flujo", "forma", f"valor_{nom}", f"peso_{nom}"]
    res = res.merge(s, on=["anio", "flujo", "forma"], how="left")
    res[f"share_valor_{nom}"] = (res[f"valor_{nom}"].fillna(0) / res["valor_total_usd"]).round(4)
    sin_peso = res[f"valor_{nom}"].notna() & res[f"peso_{nom}"].isna()   # socio con valor pero sin peso
    res[f"share_peso_{nom}"] = (res[f"peso_{nom}"].fillna(0) / res["peso_total_kg"]).round(4)
    res.loc[sin_peso, f"share_peso_{nom}"] = float("nan")
res = res.sort_values(["flujo", "forma", "anio"])
res.to_csv(os.path.join(OUT, "cobre_eua_comercio_forma.csv"), index=False, encoding="utf-8")

# --- shift-share en peso (importaciones de EUA desde Mexico), 1995-1999 vs 2020-2024 ---
m = res[res.flujo == "M"].copy()
rows = []
for forma, x in m.groupby("forma"):
    for med, tcol, mcol, esc in [("peso_t", "peso_total_kg", "peso_mexico", 1e3), ("valor_musd", "valor_total_usd", "valor_mexico", 1e6)]:
        y = x.copy(); y[mcol] = y[mcol].fillna(0)
        if med == "peso_t":   # solo anios con peso total y con peso de Mexico informado
            y = y[y[tcol].notna() & ~(x["valor_mexico"].notna() & x["peso_mexico"].isna())]
        a = y[y.anio.between(1995, 1999)]; b = y[y.anio.between(2020, 2024)]
        if a.empty or b.empty:
            continue
        T0, T1 = a[tcol].mean(), b[tcol].mean(); M0, M1 = a[mcol].mean(), b[mcol].mean()
        s0 = M0 / T0 if T0 else 0; s1 = M1 / T1 if T1 else 0
        rows.append(dict(forma=forma, medida=med, n_anios_ini=len(a), n_anios_fin=len(b),
                         imp_eua_ini=T0 / esc, imp_eua_fin=T1 / esc, desde_mx_ini=M0 / esc, desde_mx_fin=M1 / esc,
                         share_mx_ini=round(s0, 4), share_mx_fin=round(s1, 4), cambio_mx=(M1 - M0) / esc,
                         efecto_total_eua=(T1 - T0) * (s0 + s1) / 2 / esc,     # cambio del total importado por EUA
                         efecto_participacion=(s1 - s0) * (T0 + T1) / 2 / esc))  # cambio de la participacion de MX
pd.DataFrame(rows).round(1).to_csv(os.path.join(OUT, "cobre_eua_shiftshare.csv"), index=False, encoding="utf-8")

# --- comercio espejo (valor): X de Mexico a EUA vs M de EUA desde Mexico ---
mx = pd.read_csv(os.path.join(OUT, "comercio_destinos_serie_resumen.csv"))
mx = mx[mx.mineral == "cobre"].copy()
mx["x_mx_a_eua_usd"] = mx.valor_total_usd * mx.share_eua
ETAPA = {"E1 Mena/concentrado": ["concentrado"],
         "E2 Metal en bruto/refinado": ["matas y cemento", "sin refinar (blister/anodo)", "refinado", "aleaciones madre"],
         "E3 Semimanufacturas": ["semimanufacturas"]}
esp = []
for et, formas in ETAPA.items():
    us = m[m.forma.isin(formas)].groupby("anio", as_index=False)["valor_mexico"].sum()
    us.columns = ["anio", "m_eua_desde_mx_usd"]
    xx = mx[mx.etapa == et][["anio", "x_mx_a_eua_usd"]]
    e = xx.merge(us, on="anio", how="outer"); e.insert(1, "etapa", et)
    e["cociente_m_x"] = (e.m_eua_desde_mx_usd / e.x_mx_a_eua_usd).round(3)
    esp.append(e)
pd.concat(esp).sort_values(["etapa", "anio"]).to_csv(os.path.join(OUT, "cobre_eua_espejo.csv"), index=False, encoding="utf-8")
print("ok:", len(res), "filas; shift-share", len(rows), "formas")
