# -*- coding: utf-8 -*-
"""Paso 2 (ruta) — extender el HHI consolidado a 2024.
Metales (cobre, oro, plata, plomo, zinc): detalle POR MINA 2024 (hhi_numeradores.csv, nivel=mina),
grupo -> share = vol_grupo / total_nacional, HHI = Σ share^2 (residual atomistico), como 2021-2023.
Fluorita: monopolio Koura = 10000. Barita: solo dato de lider 2024 (hhi_nometalicos) -> aprox
lider^2 + residual (cota inferior; se marca). Silice y grafito 2024: sin distribucion usable -> se
DECLARAN como hueco (no se imputan). Conserva 2004-2023; agrega 2024. Salida: hhi_consolidado.csv.

NOTA cobre: el total nacional 2024 no viene impreso (grafico SGM ~750-760k t). Se usa 755,000 t
(extremo bajo del rango, consistente con la cobertura ~74% del detalle por mina); marcado 'estimado'.
"""
import csv, os, re
from collections import defaultdict

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
f_num = os.path.join(BASE, "hhi_numeradores.csv")
f_nomet = os.path.join(BASE, "hhi_nometalicos_2020_2024.csv")
f_out = os.path.join(BASE, "hhi_consolidado.csv")

def num(s):
    s = (s or "").replace(",", "").strip()
    m = re.match(r"[-+]?\d*\.?\d+", s)
    return float(m.group()) if m else None

TOT_COBRE_2024 = 755000.0  # estimado (grafico SGM 'produccion minera nacional de cobre' 2024)

# ---- metales: detalle por mina 2024 ----
mina = [r for r in csv.DictReader(open(f_num, encoding="utf-8-sig"))
        if r["anio_dato"] == "2024" and r["nivel"] == "mina"]
grp = defaultdict(lambda: defaultdict(float)); tot = {}
for r in mina:
    m = r["mineral"].strip().lower(); g = (r["empresa"].strip() or "n.d.")
    v = num(r["volumen"])
    if v is not None: grp[m][g] += v
    t = num(r["total_nacional"])
    if t is not None: tot[m] = t
tot["cobre"] = TOT_COBRE_2024

rows2024 = []
for m in ["cobre", "oro", "plata", "plomo", "zinc"]:
    groups = grp.get(m); T = tot.get(m)
    if not groups or not T: continue
    shares = {g: v / T for g, v in groups.items()}          # fraccion
    hhi = sum((s * 100) ** 2 for s in shares.values())      # HHI 0-10000 (residual atomistico)
    cob = sum(shares.values()) * 100
    top = max(shares.items(), key=lambda x: x[1])
    metodo = "mina->grupo vs total nacional" + (" (total cobre estimado)" if m == "cobre" else "")
    rows2024.append(dict(mineral=m, anio=2024, hhi=round(hhi), cobertura_pct=round(cob),
                         lider=f"{top[0]} {top[1]*100:.0f}%", metodo=metodo,
                         nota="detalle por mina 2024 (CAMIMEX/SGM)" +
                              ("; total nacional 2024 estimado ~755,000 t (grafico SGM)" if m == "cobre" else "")))

# ---- no metalicos 2024 ----
nomet = {r["mineral"].strip().lower(): r for r in csv.DictReader(open(f_nomet, encoding="utf-8-sig"))
         if r["anio_dato"] == "2024"}
# fluorita y manganeso: monopolios documentados que continuan
rows2024.append(dict(mineral="fluorita", anio=2024, hhi=10000, cobertura_pct=100,
                     lider="Koura/Orbia 100%", metodo="monopolio documentado",
                     nota="monopolio de grupo (Koura) continua"))
rows2024.append(dict(mineral="manganeso", anio=2024, hhi=10000, cobertura_pct=100,
                     lider="Cia. Minera Autlan 100%", metodo="monopolio documentado",
                     nota="Autlan, productor unico (Molango) continua"))
# barita: solo lider 2024
b = nomet.get("barita")
if b and num(b.get("participacion_lider_pct")):
    p = num(b["participacion_lider_pct"])
    rows2024.append(dict(mineral="barita", anio=2024, hhi=round(p * p), cobertura_pct=round(p),
                         lider=f"{b['empresa_lider']} {p:.0f}%",
                         metodo="lider + residual atomistico (aprox., solo lider 2024)",
                         nota="cota inferior: solo participacion del lider disponible en 2024"))
# silice y grafito 2024: sin distribucion usable -> NO se agregan (hueco declarado)

# ---- conservar 2004-2023 ----
keep = [r for r in csv.DictReader(open(f_out, encoding="utf-8-sig")) if int(r["anio"]) <= 2023]
MIN = ["cobre", "zinc", "plomo", "oro", "plata", "barita", "silice", "fluorita", "grafito", "manganeso"]
allrows = keep + rows2024
order = {mm: i for i, mm in enumerate(MIN)}
allrows.sort(key=lambda r: (order.get(r["mineral"], 99), int(r["anio"])))
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["mineral", "anio", "hhi", "cobertura_pct", "lider", "metodo", "nota"])
    w.writeheader()
    for r in allrows:
        w.writerow({k: r.get(k, "") for k in w.fieldnames})

print(f"Escrito {f_out}: +{len(rows2024)} filas 2024")
for r in rows2024:
    print(f"  {r['mineral']:10s} 2024 hhi={r['hhi']:>6} cob={r['cobertura_pct']}%  {r['lider']}")
print("Sin 2024 (declarado, sin distribucion usable): silice, grafito")
