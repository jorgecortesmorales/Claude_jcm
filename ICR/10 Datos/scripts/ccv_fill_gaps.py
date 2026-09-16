# -*- coding: utf-8 -*-
"""Paso 1 (ruta) — rellenar huecos del CCV con DATOS ESPEJO.
Todos los huecos del CCV (excl. oro/plata) son por NUMERADOR faltante (México no reportó peso,
o no reportó la exportación E1 ese año), no por precio. Se recupera el valor unitario vía
ESPEJO: lo que los socios reportan IMPORTAR desde México (flujo M, socio=484), que sí trae
netWgt. Salida: comercio_e1_espejo_huecos.csv (valor+peso por mineral-año), que ccv_calc.py
usa como respaldo del numerador con bandera fuente_numerador='espejo'.

CAVEAT: el espejo es CIF (incluye flete/seguro) y puede sobreestimar el valor unitario frente
al FOB propio; se marca cada relleno. Si el espejo también es ~0, el hueco es 'sin exportación
en bruto' (cero estructural, p. ej. manganeso) y se declara, no se imputa.
"""
import urllib.request, json, time, csv, os, sys

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
E1 = {
 "cobre": ["2603"], "plomo": ["2607"], "manganeso": ["2602"],
 "barita": ["251110"], "grafito": ["250410", "250490"], "silice": ["250510", "250610"],
}
GAPS = {
 "cobre": [2015], "plomo": [1994, 2015],
 "grafito": [2019, 2020], "manganeso": list(range(2015, 2026)),
 "barita": [2014, 2016, 2017, 2018, 2019, 2020], "silice": [2015, 2017, 2019],
}
API = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"

def mirror(year, hslist):
    """Suma valor y peso que los socios reportan importar de Mexico (socio 484), flujo M."""
    url = (f"{API}?period={year}&cmdCode={','.join(hslist)}&flowCode=M&partnerCode=484")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(10):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.load(r).get("data") or []
            v = w = 0.0
            for x in data:
                if x.get("partnerCode") == 484 and x.get("motCode") == 0:
                    v += x.get("primaryValue") or 0.0
                    w += x.get("netWgt") or 0.0
            return v, w
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(10); continue
            if e.code == 404: return 0.0, 0.0
            time.sleep(6)
        except Exception as ex:
            print(f"    retry {year}: {ex}", file=sys.stderr); time.sleep(6)
    raise RuntimeError(f"fallo espejo {year}")

rows = []
print("Descargando ESPEJO para huecos del CCV...", file=sys.stderr)
for m, years in GAPS.items():
    for y in years:
        v, w = mirror(y, E1[m])
        rows.append(dict(anio=y, mineral=m, valor_usd_espejo=round(v, 2),
                         peso_neto_kg_espejo=round(w, 1),
                         nota=("recuperable" if w > 0 else "sin comercio espejo (cero estructural)")))
        print(f"  {m:10s} {y}: valor=${v:,.0f} peso={w:,.0f}kg -> "
              f"{'uv='+format(v/(w/1000),'.1f') if w>0 else 'sin peso'}", file=sys.stderr)
        time.sleep(4)

raw_dir = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade")
f_out = os.path.join(raw_dir, "comercio_e1_espejo_huecos.csv")
with open(f_out, "w", encoding="utf-8", newline="") as fh:
    w_ = csv.DictWriter(fh, fieldnames=["anio", "mineral", "valor_usd_espejo",
                                        "peso_neto_kg_espejo", "nota"])
    w_.writeheader(); w_.writerows(sorted(rows, key=lambda x: (x["mineral"], x["anio"])))
rec = sum(1 for r in rows if r["peso_neto_kg_espejo"] > 0)
print(f"\nEscrito: {f_out}  ({len(rows)} huecos; {rec} recuperables por espejo)", file=sys.stderr)
