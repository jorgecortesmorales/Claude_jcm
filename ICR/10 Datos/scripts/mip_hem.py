# -*- coding: utf-8 -*-
"""
Metodo de Extraccion Hipotetica (HEM) por mineral sobre la MIP INEGI 2013/2018.
Complementa a los indices de Hirschman-Rasmussen (mip_calc.py) con la medida de
Miller-Lahr (2001) casos 3 (hacia atras) y 4 (hacia adelante), tal como la aplica
Morales-Lopez (2023) al caso interregional mexicano.

Definicion (para el sector k):
  - Hacia ATRAS (Leontief, extraer COMPRAS = columna k de A):
      X_hat = (I - A^(-k))^-1 Y ,  d = X - X_hat ,  BL_k = 100 * sum(d)/sum(X)
  - Hacia ADELANTE (Ghosh, extraer VENTAS = fila k de B):
      X_hat = V'(I - B^(-k))^-1 ,  Fd = X - X_hat , FL_k = 100 * sum(Fd)/sum(X)
  BL_k / FL_k = % del VBP nacional que se perderia si el sector k dejara de comprar / vender.

Se calcula para los n sectores por Sherman-Morrison (extraer una columna/fila es una
actualizacion rango-1 de la inversa ya calculada) -> exacto e instantaneo -> permite el
rango del mineral entre los n sectores. Se valida contra una extraccion por fuerza bruta.

Insumos: identicos a mip_calc.py (Z domestica, x=VBP; Y=x-Zfila, V=x-Zcolumna).
Salida: processed/mip_hem_minerales.csv
"""
import csv, os
import numpy as np
import mip_calc as mc

OUT = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

def load_year(year, cfg):
    d = mc.readcsv(os.path.join(cfg["dir"], cfg["d"]))
    t = mc.readcsv(os.path.join(cfg["dir"], cfg["t"]))
    pcols = mc.product_columns(d[0])
    codes = [c for (_, c, _) in pcols]
    name_by_code = {c: nm for (_, c, nm) in pcols}
    Z, _ = mc.load_matrix(d, pcols, codes, name_by_code)
    x_by = {}
    for r in t[1:]:
        c = mc.code_of(r[0])
        if c in name_by_code and c not in x_by:
            x_by[c] = mc.num(r[1])
    x = np.array([x_by[c] for c in codes])
    return codes, x, Z

def hem_all(x, Z):
    """Devuelve BL, FL (% del VBP nacional) para los n sectores, via Sherman-Morrison."""
    n = len(x); xs = np.where(x == 0, 1.0, x)
    A = Z / xs[np.newaxis, :]      # a_ij = z_ij/x_j
    B = Z / xs[:, np.newaxis]      # b_ij = z_ij/x_i
    I = np.eye(n)
    L = np.linalg.inv(I - A)       # Leontief
    G = np.linalg.inv(I - B)       # Ghosh
    Y = x - Z.sum(axis=1)          # demanda final (x = L Y)
    V = x - Z.sum(axis=0)          # valor agregado (x = V (I-B)^-1)
    X = x
    sX = X.sum()
    # ---- backward (columna k de A) ----
    LA = L @ A
    colsum_LA = LA.sum(axis=0)     # sum_i (L A)_{i,k}
    diag_LA = np.diag(LA)          # (L A)_{k,k} = u_k
    BL = 100.0 * X * colsum_LA / ((1.0 + diag_LA) * sX)
    # ---- forward (fila k de B) ----
    BG = B @ G
    rowsum_BG = BG.sum(axis=1)     # sum_j (B G)_{k,j}
    diag_BG = np.diag(BG)          # (B G)_{k,k}
    FL = 100.0 * X * rowsum_BG / ((1.0 + diag_BG) * sX)
    return A, B, L, G, Y, V, X, BL, FL

def hem_bruteforce(k, A, B, Y, V, X):
    """Extraccion directa del sector k (para validar Sherman-Morrison)."""
    n = len(X); I = np.eye(n)
    Ae = A.copy(); Ae[:, k] = 0.0
    Xhat_b = np.linalg.inv(I - Ae) @ Y
    BLk = 100.0 * (X - Xhat_b).sum() / X.sum()
    Be = B.copy(); Be[k, :] = 0.0
    Xhat_f = V @ np.linalg.inv(I - Be)
    FLk = 100.0 * (X - Xhat_f).sum() / X.sum()
    return BLk, FLk

def rank_desc(v):
    return (-v).argsort().argsort() + 1

def run():
    rows = []
    for year, cfg in mc.YEARS.items():
        codes, x, Z = load_year(year, cfg)
        n = len(codes)
        A, B, L, G, Y, V, X, BL, FL = hem_all(x, Z)
        # validacion: X = L Y
        chk = np.abs(L @ Y - X).max()
        idx = {c: k for k, c in enumerate(codes)}
        rBL, rFL = rank_desc(BL), rank_desc(FL)
        TOT = BL + FL; rTOT = rank_desc(TOT)
        # validacion Sherman-Morrison vs fuerza bruta en los minerales
        maxdiff = 0.0
        for code, _ in mc.MINERALES:
            k = idx[code]
            bBL, bFL = hem_bruteforce(k, A, B, Y, V, X)
            maxdiff = max(maxdiff, abs(bBL - BL[k]), abs(bFL - FL[k]))
        print(f"===== {year} =====  n={n}  |LY-X|max={chk:.2e}  |SM-bruteforce|max={maxdiff:.2e}")
        print(f"  {'mineral':11s}{'VBP':>12s}{'HEM_back%':>10s}{'HEM_fwd%':>10s}{'HEM_tot%':>10s}{'rB':>5s}{'rF':>5s}{'rT':>5s}")
        for code, mineral in mc.MINERALES:
            k = idx[code]
            rows.append(dict(
                anio=year, codigo=code, mineral=mineral,
                vbp_mmpesos=round(float(x[k]), 3),
                hem_backward_pct=round(float(BL[k]), 4),
                hem_forward_pct=round(float(FL[k]), 4),
                hem_total_pct=round(float(TOT[k]), 4),
                rank_backward=int(rBL[k]),
                rank_forward=int(rFL[k]),
                rank_total=int(rTOT[k]),
                n_sectores=n,
            ))
            print(f"  {mineral:11s}{x[k]:12.1f}{BL[k]:10.4f}{FL[k]:10.4f}{TOT[k]:10.4f}"
                  f"{rBL[k]:5d}{rFL[k]:5d}{rTOT[k]:5d}")
    return rows

if __name__ == "__main__":
    rows = run()
    f = os.path.join(OUT, "mip_hem_minerales.csv")
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print("\nEscrito:", f)
