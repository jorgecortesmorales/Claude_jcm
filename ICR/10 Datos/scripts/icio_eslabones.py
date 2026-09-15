# -*- coding: utf-8 -*-
"""Ghosh hacia adelante internacional por ESLABON (no solo el extractivo), 8 paises.
Reutiliza icio_comparacion.py (mismo bloque domestico, mismo metodo) pero extrae tres
industrias ICIO a lo largo de la cadena metalica:
  extraccion      = B07_08 (mineria no energetica: menas metalicas + otra)
  refinacion      = C24    (industrias metalicas basicas: fundicion/refinacion)
  semimanufactura = C25    (fabricacion de productos metalicos)
CAVEAT: C24/C25 son toda la industria metalica del pais (incluye acero/aluminio), no solo los
10 minerales; comparacion a nivel sector (aggregation caveat, igual que en la mineria).
Cortes: 2018 (principal) y 2020. Salida: processed/icio_eslabones_metal.csv
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import icio_comparacion as ic

SML = r"C:\Users\Jorge\AppData\Local\Temp\claude\C--Users-Jorge-OneDrive-Escritorio-Claude-CODE\9bf14e12-846d-41f3-9d66-cec1c99b4f6a\scratchpad"
OUT = os.path.join(ic.OUTDIR, "icio_eslabones_metal.csv")

ic.MINEROS = {
    "B07_08": "L1 extraccion (menas metalicas)",
    "C24":    "L2 refinacion (metales basicos)",
    "C25":    "L3 semimanufactura (productos metalicos)",
}
ESL = {"B07_08": "L1", "C24": "L2", "C25": "L3"}

def main():
    allrows = []
    for anio in (2008, 2013, 2018, 2020):
        path = os.path.join(SML, f"{anio}_SML.csv")
        if not os.path.exists(path):
            print("  FALTA SML:", path, file=sys.stderr); continue
        results, _ = ic.main(path, anio)
        for r in results:
            r["eslabon"] = ESL.get(r["sector"], "")
            allrows.append(r)
        print(f"  {anio}: {len(results)} filas")
    # ordenar: anio, eslabon, forward desc
    order_e = {"L1": 0, "L2": 1, "L3": 2}
    allrows.sort(key=lambda r: (r["anio"], order_e.get(r["eslabon"], 9), -r["forward_rasmussen"]))
    fields = ["anio", "pais", "pais_nombre", "eslabon", "sector", "sector_nombre",
              "vbp_musd", "share_vbp_pct", "forward_G_rowsum", "forward_rasmussen",
              "backward_rasmussen", "rank_forward", "rank_backward", "n_industrias"]
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(allrows)
    print("Escrito:", OUT, f"({len(allrows)} filas)")
    # resumen 2018: forward por pais x eslabon
    print("\n=== Ghosh hacia adelante (Rasmussen, 2018) — cadena metalica por pais ===")
    print(f"{'pais':11s}{'L1 extrac':>10s}{'L2 refin':>10s}{'L3 semis':>10s}")
    for c in ic.PAISES:
        d = {r["eslabon"]: r for r in allrows if r["anio"] == 2018 and r["pais"] == c}
        def g(e): return f"{d[e]['forward_rasmussen']:10.3f}" if e in d else f"{'n/d':>10s}"
        print(f"{ic.NOMBRE_PAIS[c]:11s}{g('L1')}{g('L2')}{g('L3')}")

if __name__ == "__main__":
    main()
