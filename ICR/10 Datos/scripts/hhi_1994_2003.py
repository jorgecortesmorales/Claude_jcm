# -*- coding: utf-8 -*-
"""Paso 7 - Extender el HHI a 1994-2003 (aproximado, metodo regimen).

Fuente: USGS Minerals Yearbook Mexico, capitulos 1994-2003 (Tabla 2 'Structure of the
Mineral Industry' + narrativa 'Structure of the Mineral Industry'), descargados del
archivo S3 del USGS y leidos con pdftotext -layout.

Se anaden SOLO los minerales cuyo regimen de mercado esta documentado de forma
inequivoca y consistente con la serie 2004+ (evita falsa precision y el salto
grupo-vs-empresa):
  - manganeso: monopolio Autlan (unico operador en Tabla 2 todos los anios) -> 10000
  - grafito:   duopolio documentado -> 5848 (mismo regimen que 2004-2013)
  - fluorita:  lider Las Cuevas ~75-80% + fringe (narrativa 1999/2001/2002/2003) -> ~6001
  - cobre:     grupo Grupo Mexico (La Caridad + Cananea), share nacional documentado
               79% (1997), 82% (1998), 80% (2000), 85% (2001), 83% (2002), 80% (2003)
               -> HHI = share_grupo^2 (residual atomistico; cota inferior). Anios sin
               share explicito (1994-1996, 1999) se DECLARAN (no se imputan).
oro/plata/plomo/zinc: participaciones de lider documentadas pero de nivel grupo/empresa
mixto -> se registran en la memoria como evidencia cualitativa y se DECLARAN en la serie.
barita/silice: sin share firme -> declarados. 1992-1993: sin solucion (privatizacion).

NO recalcula 2004-2024 (se conservan). Salida: hhi_consolidado.csv.
"""
import csv, os

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
f_out = os.path.join(BASE, "hhi_consolidado.csv")
FUENTE = "USGS MYB Mexico 1994-2003, Tabla 2 + narrativa"

nuevos = []
def add(m, a, hhi, cob, lider, metodo, nota):
    nuevos.append(dict(mineral=m, anio=a, hhi=hhi, cobertura_pct=cob,
                       lider=lider, metodo=metodo, nota=nota))

for a in range(1994, 2004):
    add("manganeso", a, 10000, 100, "Cia. Minera Autlan 100%",
        "monopolio documentado (USGS Tabla 2)", f"{FUENTE}: Autlan productor unico")
    add("grafito", a, 5848, 100, "Grafitos Mexicanos (duopolio)",
        "duopolio documentado", f"{FUENTE}: 2 productores; mismo regimen que 2004-2013")
    add("fluorita", a, 6001, 95, "Cia. Minera Las Cuevas ~75-80%",
        "lider dominante + fringe (narrativa USGS)", f"{FUENTE}: Las Cuevas ~75% (1999/2001), 76% (2002), >80% (2003); cota inferior")

# cobre: grupo Grupo Mexico, share nacional documentado (share^2)
cobre = {1997: (79, 6241), 1998: (82, 6724), 2000: (80, 6400),
         2001: (85, 7225), 2002: (83, 6889), 2003: (80, 6400)}
for a, (sh, hhi) in cobre.items():
    add("cobre", a, hhi, sh, f"Grupo Mexico ~{sh}%",
        "lider-grupo Grupo Mexico (narrativa USGS)",
        f"{FUENTE}: La Caridad+Cananea {sh}% del cobre mina nacional; cota inferior; nivel grupo (no comparable con 2004+)")

# --- merge con lo existente (upsert por mineral+anio, conservando 2004-2024) ---
existing = list(csv.DictReader(open(f_out, encoding="utf-8-sig")))
key = lambda r: (r["mineral"], int(r["anio"]))
newkeys = {key(r) for r in nuevos}
kept = [r for r in existing if key(r) not in newkeys]
allrows = kept + nuevos

MIN = ["cobre","zinc","plomo","oro","plata","barita","silice","fluorita","grafito","manganeso"]
order = {m: i for i, m in enumerate(MIN)}
allrows.sort(key=lambda r: (order.get(r["mineral"], 99), int(r["anio"])))

fields = ["mineral","anio","hhi","cobertura_pct","lider","metodo","nota"]
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields); w.writeheader()
    for r in allrows:
        w.writerow({k: r.get(k, "") for k in fields})

print(f"Escrito: {f_out}  ({len(allrows)} filas; +{len(nuevos)} nuevas 1994-2003)")
print("\nCobertura 1994-2003 por mineral:")
for m in MIN:
    ys = sorted(int(r["anio"]) for r in allrows if r["mineral"] == m and 1994 <= int(r["anio"]) <= 2003)
    print(f"  {m:10s} {ys if ys else 'declarado (sin serie 1994-2003)'}")
