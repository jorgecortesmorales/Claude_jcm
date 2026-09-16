# -*- coding: utf-8 -*-
"""Paso 3 (ruta) — resumen de la serie temporal de destinos.
De comercio_destinos_serie_crudo.csv arma, por (anio, mineral, etapa): total exportado,
destino principal y su share, y el share a China y a EUA (los dos polos del hallazgo).
Muestra el DESPLAZAMIENTO de destinos en el tiempo (p. ej. concentrado de cobre -> China).
Salida: processed/comercio_destinos_serie_resumen.csv.
"""
import csv, os
from collections import defaultdict

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
f_in = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade", "comercio_destinos_serie_crudo.csv")
f_out = os.path.join(BASE, "processed", "comercio_destinos_serie_resumen.csv")

by = defaultdict(lambda: defaultdict(float))  # (anio,mineral,etapa) -> {pais: valor}
for r in csv.DictReader(open(f_in, encoding="utf-8")):
    by[(int(r["anio"]), r["mineral"], r["etapa"])][r["pais_destino"]] += float(r["valor_usd"])

rows = []
for (a, m, e), dests in sorted(by.items()):
    tot = sum(dests.values())
    if tot <= 0: continue
    top = max(dests.items(), key=lambda x: x[1])
    rows.append(dict(
        anio=a, mineral=m, etapa=e,
        valor_total_usd=round(tot, 2),
        destino_principal=top[0], share_principal=round(top[1] / tot, 4),
        share_china=round(dests.get("China", 0.0) / tot, 4),
        share_eua=round(dests.get("Estados Unidos", 0.0) / tot, 4),
        n_destinos=sum(1 for v in dests.values() if v > 0),
    ))
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["anio", "mineral", "etapa", "valor_total_usd",
        "destino_principal", "share_principal", "share_china", "share_eua", "n_destinos"])
    w.writeheader(); w.writerows(rows)
print(f"Escrito {f_out} ({len(rows)} filas)")

# reporte: desplazamiento de destino del concentrado de cobre (E1) por año
print("\nConcentrado de cobre (E1) — % a China vs EUA por año:")
for r in rows:
    if r["mineral"] == "cobre" and r["etapa"].startswith("E1") and r["anio"] % 3 == 0:
        print(f"  {r['anio']}: China {r['share_china']*100:4.0f}%  EUA {r['share_eua']*100:4.0f}%  "
              f"top={r['destino_principal']} ({r['share_principal']*100:.0f}%)")
