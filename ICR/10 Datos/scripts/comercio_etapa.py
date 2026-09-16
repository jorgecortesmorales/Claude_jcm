# -*- coding: utf-8 -*-
"""Tarea 2 - Comercio por etapa de procesamiento (Obj. 3).
Descarga comercio de Mexico (reporter 484) por fraccion HS desde UN Comtrade (API publica
preview, sin clave), clasifica por etapa segun una concordancia mineral x etapa x HS, y
calcula participacion por etapa, dependencia de importaciones procesadas y analisis espejo.
"""
import urllib.request, json, time, csv, os, sys

# ---------------- CONCORDANCIA mineral x etapa x HS ----------------
# Etapas: E1 mena/concentrado o mineral crudo; E2 metal en bruto/refinado o mineral procesado/quimico;
#         E3 semimanufactura/intermedio; E4 manufactura/bien final (atribuible al mineral).
# Codigos HS 2017/2022 (4 dig = encabezado completo del mineral; 6 dig donde el mineral comparte encabezado).
CONC = {
 "cobre": {
   "E1 Mena/concentrado": ["2603"],
   "E2 Metal en bruto/refinado": ["7401","7402","7403","7405"],
   "E3 Semimanufacturas": ["7407","7408","7409","7410","7411","7412","7413"],
   "E4 Manufacturas": ["7415","7418","7419"],
 },
 "plomo": {
   "E1 Mena/concentrado": ["2607"],
   "E2 Metal en bruto/refinado": ["7801"],
   "E3 Semimanufacturas": ["7804"],
   "E4 Manufacturas": ["7806"],
 },
 "zinc": {
   "E1 Mena/concentrado": ["2608"],
   "E2 Metal en bruto/refinado": ["7901"],
   "E3 Semimanufacturas": ["7903","7904","7905"],
   "E4 Manufacturas": ["7907"],
 },
 "manganeso": {
   "E1 Mena/concentrado": ["2602"],
   "E2 Ferroaleaciones": ["720211","720219","720230"],
   "E3 Quimicos/metal": ["282010","8111"],
 },
 "oro": {
   "E1 Mena/concentrado": ["261610"],
   "E2 Bruto/semilabrado": ["7108"],
 },
 "plata": {
   "E1 Mena/concentrado": ["261690"],
   "E2 Bruto/semilabrado": ["7106"],
 },
 "oro-plata (manufacturas)": {   # joyeria/orfebreria - metales preciosos combinados (multi-metal)
   "E4 Joyeria/orfebreria": ["7113","7114","7115"],
 },
 "barita": {
   "E1 Crudo/molido": ["251110"],
   "E2 Quimicos de bario": ["281640","283660"],
 },
 "fluorita": {
   "E1 Espato fluor (crudo)": ["252921","252922"],
   "E2 Fluoroquimica": ["281111","282612","282619","390461"],
 },
 "grafito": {
   "E1 Grafito natural": ["250410","250490"],
   "E2 Grafito artificial/prep.": ["3801"],
   "E3 Electrodos/articulos de carbono": ["8545"],
 },
 "silice": {
   "E1 Arena silica/cuarzo": ["250510","250610"],
   "E2 Silicio/ferrosilicio/SiO2": ["280461","280469","720221","720229","281122"],
 },
}

# codigos unicos
codes = sorted({c for m in CONC.values() for lst in m.values() for c in lst})
YEARS = list(range(2015, 2025))
BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

def fetch(year, flow):
    url = (f"{BASE}?reporterCode=484&period={year}&cmdCode={','.join(codes)}"
           f"&flowCode={flow}&partnerCode=0")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)["data"]
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(6); continue
            if e.code == 404:
                return []
            time.sleep(4)
        except Exception:
            time.sleep(4)
    raise RuntimeError(f"fallo {year} {flow}")

# ---------------- descarga ----------------
raw = {}  # (year, flow, cmd) -> value
print("Descargando Comtrade (Mexico 484, Mundo)...", file=sys.stderr)
for y in YEARS:
    for fl in ("X", "M"):
        data = fetch(y, fl)
        n = 0
        for r in data:
            if r.get("motCode") == 0 and r.get("partnerCode") == 0:
                raw[(y, fl, str(r["cmdCode"]))] = r.get("primaryValue") or 0.0
                n += 1
        print(f"  {y} {fl}: {n} codigos con dato", file=sys.stderr)
        time.sleep(3)

# ---------------- salidas ----------------
outdir = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
raw_dir = os.path.join(outdir, "Bases Originales", "11 Comercio Comtrade")
os.makedirs(raw_dir, exist_ok=True)
proc = os.path.join(outdir, "processed")

# 1) crudo largo: anio, flujo, hs, valor_usd
f_raw = os.path.join(raw_dir, "comercio_hs_comtrade_mx_2015_2024.csv")
with open(f_raw, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["anio","flujo","hs","valor_usd"])
    for (y,fl,cmd),v in sorted(raw.items()):
        w.writerow([y, "Exportacion" if fl=="X" else "Importacion", cmd, round(v,2)])

# 2) por mineral x etapa x flujo x anio
rows_etapa = []
for mineral, etapas in CONC.items():
    for etapa, hslist in etapas.items():
        for y in YEARS:
            for fl,fln in (("X","Exportacion"),("M","Importacion")):
                val = sum(raw.get((y,fl,c),0.0) for c in hslist)
                rows_etapa.append(dict(anio=y, mineral=mineral, etapa=etapa, flujo=fln,
                                       hs=";".join(hslist), valor_usd=round(val,2)))
f_etapa = os.path.join(proc, "comercio_por_etapa.csv")
with open(f_etapa, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows_etapa[0].keys())); w.writeheader(); w.writerows(rows_etapa)

# 3) resumen por mineral (2018 y 2023): participacion por etapa y espejo
def summ(mineral, year):
    etapas = CONC[mineral]
    ex = {e: sum(raw.get((year,"X",c),0.0) for c in hs) for e,hs in etapas.items()}
    im = {e: sum(raw.get((year,"M",c),0.0) for c in hs) for e,hs in etapas.items()}
    return ex, im

print("\n================ RESUMEN (millones USD) ================")
for year in (2018, 2023):
    print(f"\n===== {year} =====")
    for mineral in CONC:
        ex, im = summ(mineral, year)
        tex, tim = sum(ex.values()), sum(im.values())
        if tex+tim == 0: continue
        print(f"\n[{mineral}]  X_total={tex/1e6:,.1f}  M_total={tim/1e6:,.1f}")
        for e in ex:
            print(f"   {e:34s} X={ex[e]/1e6:9,.1f}  M={im[e]/1e6:9,.1f}"
                  + (f"  Xshare={ex[e]/tex*100:4.0f}%" if tex else ""))

print("\nEscritos:")
print(" ", f_raw)
print(" ", f_etapa)
