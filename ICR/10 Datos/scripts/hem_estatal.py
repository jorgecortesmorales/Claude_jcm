# -*- coding: utf-8 -*-
"""
HEM (metodo de extraccion hipotetica) de la mineria por ENTIDAD, MIP birregional INEGI 2018.
Paralelo estatal del HEM nacional (mip_hem.py) y del disenio interregional de Morales-Lopez (2023).

Para cada entidad se toma su MIP birregional (entidad + 'Resto del Pais', 70 industrias) y se
extrae el sector-region MINERIA (21-2) de la entidad:
  - hacia ATRAS: se anula la columna de la mineria en A -> % del VBP birregional que se perderia
    si esa mineria dejara de comprar insumos;
  - hacia ADELANTE: se anula la fila de la mineria en B (Ghosh) -> % que se perderia si dejara de vender.
Mide la importancia de la mineria de cada estado para el conjunto (entidad + resto del pais).
Reutiliza el cargador de ghosh_interestatal.py. Salida: processed/hem_estatal_mineria.csv
"""
import os, glob, csv
import numpy as np
import ghosh_interestatal as gi

OUT = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

def hem_sector(x, Z, k):
    """BL,FL (% del VBP total) de extraer el sector k, por Sherman-Morrison + validacion bruta."""
    n = len(x); xs = np.where(x == 0, 1.0, x)
    A = Z / xs[np.newaxis, :]; B = Z / xs[:, np.newaxis]; I = np.eye(n)
    L = np.linalg.inv(I - A); G = np.linalg.inv(I - B)
    Y = x - Z.sum(axis=1); V = x - Z.sum(axis=0); X = x; sX = X.sum()
    # Sherman-Morrison
    u = L @ A[:, k]; BL = 100.0 * X[k] * u.sum() / ((1.0 + u[k]) * sX)
    w = B[k, :] @ G;  FL = 100.0 * X[k] * w.sum() / ((1.0 + w[k]) * sX)
    # fuerza bruta (validacion)
    Ae = A.copy(); Ae[:, k] = 0.0; BLb = 100.0 * (X - np.linalg.inv(I - Ae) @ Y).sum() / sX
    Be = B.copy(); Be[k, :] = 0.0; FLb = 100.0 * (X - V @ np.linalg.inv(I - Be)).sum() / sX
    return BL, FL, max(abs(BL - BLb), abs(FL - FLb))

def run():
    rows = []; maxd = 0.0
    for path in sorted(glob.glob(os.path.join(gi.BASE, "mip_ixi_br_*_d_2018.xlsx"))):
        edo = os.path.basename(path).split("_")[3]
        d = gi.load(path)
        BL, FL, dd = hem_sector(d["x"], d["Z"], d["mi"]); maxd = max(maxd, dd)
        rows.append(dict(
            estado=gi.NOMBRE.get(edo, edo), abrev=edo,
            vbp_mineria_mdp=round(float(d["x_min"]), 1),
            hem_backward_pct=round(float(BL), 4),
            hem_forward_pct=round(float(FL), 4),
            hem_total_pct=round(float(BL + FL), 4),
        ))
    rows.sort(key=lambda r: -(r["hem_total_pct"] or 0))
    print(f"Validacion Sherman-Morrison vs fuerza bruta: max|dif| = {maxd:.2e}")
    print(f"\n{'estado':18s}{'VBPmin':>10s}{'HEM_back%':>11s}{'HEM_fwd%':>11s}{'HEM_tot%':>11s}")
    for r in rows[:14]:
        print(f"{r['estado']:18s}{r['vbp_mineria_mdp']:>10.0f}{r['hem_backward_pct']:>11.4f}"
              f"{r['hem_forward_pct']:>11.4f}{r['hem_total_pct']:>11.4f}")
    f = os.path.join(OUT, "hem_estatal_mineria.csv")
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print("\nEscrito:", f)

if __name__ == "__main__":
    run()
