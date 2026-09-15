# -*- coding: utf-8 -*-
"""Ghosh hacia adelante por ENTIDAD para dos eslabones (no solo el extractivo):
  extraccion   = industria '21-2 Mineria no petrolera'
  transformacion metalica = industria '331-332 Industrias metalicas basicas; productos metalicos'
CAVEAT: el MIP estatal (35 industrias) COMBINA refinacion (331) y semimanufactura (332) en una
sola industria; a esta resolucion no se pueden separar L2 y L3 (a diferencia del nacional).
Reutiliza load()/ghosh() de ghosh_estatal.py. Salida: processed/ghosh_estatal_eslabones.csv
"""
import os, sys, glob, csv
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ghosh_estatal as ge

def idx_starts(names, pref):
    for k, nm in enumerate(names):
        if nm.startswith(pref): return k
    return None

def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(ge.BASE, "mip_ixi_e_*_intra_2018.xlsx"))):
        edo = os.path.basename(path).split("_")[3]
        d = ge.load(path)
        FL, Ui, BL, U = ge.ghosh(d["Z"], d["x"])
        names = d["ind_names"]
        rk = (-Ui).argsort().argsort()
        for eslabon, pref, tipo in [("L1", "21-2", "extraccion"),
                                    ("L2+L3", "331-332", "transformacion metalica (refinacion+semis)")]:
            k = idx_starts(names, pref)
            if k is None:
                continue
            rows.append(dict(
                estado=ge.NOMBRE.get(edo, edo), abrev=edo, eslabon=eslabon, tipo=tipo,
                industria=names[k][:52],
                vbp_mdp=round(float(d["x"][k]), 1),
                forward_rowsum=round(float(FL[k]), 4),
                forward_rasmussen=round(float(Ui[k]), 4),
                backward_rasmussen=round(float(U[k]), 4),
                rank_forward_de_35=int(rk[k] + 1),
            ))
    # ordenar por estado y eslabon
    rows.sort(key=lambda r: (r["estado"], r["eslabon"]))
    f = os.path.join(ge.OUT, "ghosh_estatal_eslabones.csv")
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("Escrito:", f, "| filas:", len(rows))
    # resumen: estados con mayor transformacion metalica
    print(f"\n=== Ghosh hacia adelante por eslabon (top estados por VBP de transformacion) ===")
    trans = sorted([r for r in rows if r["eslabon"] == "L2+L3"], key=lambda r: -r["vbp_mdp"])[:12]
    print(f"{'estado':18s}{'VBP_transf':>11s}{'fwd_transf':>11s}{'fwd_extrac':>11s}")
    ext = {r["estado"]: r for r in rows if r["eslabon"] == "L1"}
    for r in trans:
        fe = ext.get(r["estado"], {}).get("forward_rasmussen", float("nan"))
        print(f"{r['estado']:18s}{r['vbp_mdp']:>11.0f}{r['forward_rasmussen']:>11.2f}{fe:>11.2f}")

if __name__ == "__main__":
    main()
