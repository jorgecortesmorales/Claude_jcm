# -*- coding: utf-8 -*-
"""Ghosh INTER-ESTATAL (MIP birregional 2018) por eslabon: extraccion (21-2) y transformacion
metalica (331-332) de la REGION-entidad, con el arrastre inter-estatal endogeno (70 industrias).
Reutiliza load()/ghosh_fwd() de ghosh_interestatal.py. Salida: processed/ghosh_interestatal_eslabones.csv
CAVEAT: el MIP estatal combina refinacion (331) y semis (332) en una industria; no separables.
"""
import os, sys, glob, csv
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ghosh_interestatal as gi

def region1_index(path, pref):
    """indice (entre las 70 filas industria) de la 1a industria de la REGION 1 cuyo nombre empieza con pref."""
    df = pd.read_excel(path, sheet_name=0, header=None); n = len(df)
    hr = next(i for i in range(n) if str(df.iloc[i, 1]).strip() == "Actividad")
    ind_cols = []
    for j in range(2, df.shape[1]):
        h = str(df.iloc[hr, j]).strip()
        if h.startswith(("CP", "CG", "P.51", "P.52", "d P.6", "Exportaciones")):
            if not ind_cols: continue
            break
        if h in ("nan", ""): continue
        ind_cols.append(j)
    K = len(ind_cols); ind_rows = list(range(hr + 1, hr + 1 + K))
    for k in range(K // 2):  # solo region 1 (primer bloque de 35)
        if str(df.iloc[ind_rows[k], 1]).strip().startswith(pref):
            return k
    return None

def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(gi.BASE, "mip_ixi_br_*_d_2018.xlsx"))):
        edo = os.path.basename(path).split("_")[3]
        d = gi.load(path)
        FL, Ui = gi.ghosh_fwd(d["Z"], d["x"])
        rk = (-Ui).argsort().argsort()
        for eslabon, pref, tipo in [("L1", "21-2", "extraccion"),
                                    ("L2+L3", "331-332", "transformacion metalica (refinacion+semis)")]:
            k = region1_index(path, pref)
            if k is None: continue
            rows.append(dict(
                estado=gi.NOMBRE.get(edo, edo), abrev=edo, eslabon=eslabon, tipo=tipo,
                vbp_mdp=round(float(d["x"][k]), 1),
                forward_rasmussen_br=round(float(Ui[k]), 4),
                rank_forward_de_70=int(rk[k] + 1),
            ))
    rows.sort(key=lambda r: (r["estado"], r["eslabon"]))
    f = os.path.join(gi.OUT, "ghosh_interestatal_eslabones.csv")
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("Escrito:", f, "| filas:", len(rows))
    trans = sorted([r for r in rows if r["eslabon"] == "L2+L3"], key=lambda r: -r["vbp_mdp"])[:10]
    ext = {r["estado"]: r for r in rows if r["eslabon"] == "L1"}
    print(f"{'estado':18s}{'VBP_transf':>11s}{'fwd_transf_br':>14s}{'fwd_extrac_br':>14s}")
    for r in trans:
        fe = ext.get(r["estado"], {}).get("forward_rasmussen_br", float("nan"))
        print(f"{r['estado']:18s}{r['vbp_mdp']:>11.0f}{r['forward_rasmussen_br']:>14.2f}{fe:>14.2f}")

if __name__ == "__main__":
    main()
