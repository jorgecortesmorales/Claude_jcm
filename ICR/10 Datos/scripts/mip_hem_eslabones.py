# -*- coding: utf-8 -*-
"""
Extraccion hipotetica (HEM) por ESLABON de la cadena (L1 extraccion / L2 refinacion / L3 semis),
para cada mineral. Complemento del HEM por mineral (mip_hem.py) y paralelo del
Ghosh-Rasmussen por eslabon (mip_eslabones.py). Corte MIP 2013 y 2018.

Reutiliza mip_hem.hem_all (que devuelve el HEM % validado de TODOS los sectores por
Sherman-Morrison) y el mapa de clases SCIAN por eslabon de mip_eslabones.ESLAB.
Salida: processed/mip_hem_eslabones.csv
"""
import os, csv, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mip_calc as mc
import mip_hem as mh
from mip_eslabones import ESLAB, TIPO

OUT = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

def load_full(year, cfg):
    d = mc.readcsv(os.path.join(cfg["dir"], cfg["d"]))
    t = mc.readcsv(os.path.join(cfg["dir"], cfg["t"]))
    pcols = mc.product_columns(d[0])
    codes = [c for (_, c, _) in pcols]
    name_by = {c: nm for (_, c, nm) in pcols}
    Z, _ = mc.load_matrix(d, pcols, codes, name_by)
    x_by = {}
    for r in t[1:]:
        c = mc.code_of(r[0])
        if c in name_by and c not in x_by:
            x_by[c] = mc.num(r[1])
    x = np.array([x_by[c] for c in codes])
    return codes, name_by, x, Z

def run():
    rows = []
    for year, cfg in mc.YEARS.items():
        codes, name_by, x, Z = load_full(year, cfg)
        idx = {c: k for k, c in enumerate(codes)}
        A, B, L, G, Y, V, X, BL, FL = mh.hem_all(x, Z)   # HEM % de todos los sectores
        TOT = BL + FL
        rfwd = (-FL).argsort().argsort() + 1
        for code, mineral in mc.MINERALES:
            eslabs = [("L1", code, "si"),
                      ("L2",) + ESLAB[mineral]["L2"],
                      ("L3",) + ESLAB[mineral]["L3"]]
            for esl, ccode, atrib in eslabs:
                if ccode is None or ccode not in idx:
                    rows.append(dict(anio=year, mineral=mineral, eslabon=esl, tipo=TIPO[esl],
                        scian=(ccode or ""), clase="(sin clase separable)", atribuible=(atrib or "-"),
                        hem_backward_pct="", hem_forward_pct="", hem_total_pct="", rank_forward=""))
                    continue
                k = idx[ccode]
                rows.append(dict(anio=year, mineral=mineral, eslabon=esl, tipo=TIPO[esl],
                    scian=ccode, clase=name_by[ccode][:48], atribuible=atrib,
                    hem_backward_pct=round(float(BL[k]), 4),
                    hem_forward_pct=round(float(FL[k]), 4),
                    hem_total_pct=round(float(TOT[k]), 4),
                    rank_forward=int(rfwd[k])))
    f = os.path.join(OUT, "mip_hem_eslabones.csv")
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("Escrito:", f, f"({len(rows)} filas)")
    print("\n=== HEM hacia adelante (% del VBP, 2018) por eslabon ===")
    print(f"{'mineral':11s}{'L1 extrac':>11s}{'L2 refin':>11s}{'L3 semis':>11s}   (clase L2/L3)")
    for code, mineral in mc.MINERALES:
        r = {x['eslabon']: x for x in rows if x['anio']=='2018' and x['mineral']==mineral}
        def g(e):
            v=r[e]['hem_forward_pct']; return f"{v:11.4f}" if v!="" else f"{'n/d':>11s}"
        print(f"{mineral:11s}{g('L1')}{g('L2')}{g('L3')}   ({r['L2']['scian']}/{r['L3']['scian']})")

if __name__ == "__main__":
    run()
