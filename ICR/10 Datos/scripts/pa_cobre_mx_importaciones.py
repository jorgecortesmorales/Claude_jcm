# -*- coding: utf-8 -*-
"""Pregunta A (piloto cobre, paso por empresa) — importaciones de MEXICO de cobre (2603, 7402, 7403, 7404)
por socio, 1992-2024 (UN Comtrade, API publica preview). Sirve de espejo de las exportaciones de EUA a Mexico.
Salida: Bases Originales/11 Comercio Comtrade/comercio_cobre_mx_importaciones_1992_2024_crudo.csv
"""
import urllib.request, urllib.error, json, time, csv, os, sys
BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
OUT = os.path.join(BASE, "Bases Originales", "11 Comercio Comtrade", "comercio_cobre_mx_importaciones_1992_2024_crudo.csv")
API = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
def fetch(y):
    url = f"{API}?reporterCode=484&period={y}&cmdCode=2603,7402,7403,7404&flowCode=M"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for _ in range(10):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r).get("data") or []
        except urllib.error.HTTPError as e:
            if e.code == 404: return []
            time.sleep(10)
        except Exception as ex:
            print("reintento", y, ex, file=sys.stderr); time.sleep(6)
    print("FALLA", y, file=sys.stderr); return []
with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(["anio", "hs4", "socio_m49", "valor_usd", "peso_kg"])
    for y in range(1992, 2025):
        for r in fetch(y):
            if r.get("customsCode") == "C00" and r.get("motCode") == 0 and r.get("partner2Code") == 0:
                w.writerow([y, r["cmdCode"], r["partnerCode"], r.get("primaryValue"), r.get("netWgt")])
        time.sleep(2); print(y, flush=True)
print("Escrito:", OUT)
