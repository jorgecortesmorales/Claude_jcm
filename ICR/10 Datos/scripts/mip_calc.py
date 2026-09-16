# -*- coding: utf-8 -*-
"""
MIP INEGI -> encadenamientos por mineral (diseno descriptivo, cadenas de valor).
Nivel Clase SCIAN (6 dig), matriz producto x producto, base DOMESTICA.
Calcula Leontief (hacia atras), Ghosh (hacia adelante), indices Hirschman-Rasmussen
normalizados, y demanda intermedia domestica por mineral.
Valida A vs ctec de INEGI y (I-A)^-1 vs cdi de INEGI.
"""
import csv, os, sys
import numpy as np

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\Bases Originales\10 MIP INEGI"

YEARS = {
    "2013": {
        "dir": os.path.join(BASE, "2013", "conjunto_de_datos"),
        "d":   "mip_d_pb_pxp_4.csv",   # flujos domesticos
        "t":   "mip_t_pb_pxp_4.csv",   # flujos totales (para x = VBP col UTPB)
        "ctec":"mip_ctec_pxp_4.csv",   # A domestica (validacion)
        "cdi": "mip_cdi_pxp_4.csv",    # (I-A)^-1 (validacion)
    },
    "2018": {
        "dir": os.path.join(BASE, "2018", "conjunto de datos"),
        "d":   "conjunto_de_datos_mip_d_pb_pxp_42018.csv",
        "t":   "conjunto_de_datos_mip_t_pb_pxp_42018.csv",
        "ctec":"conjunto_de_datos_mip_ctec_pxp_42018.csv",
        "cdi": "conjunto_de_datos_mip_cdi_pxp_42018.csv",
    },
}

# Corpus: 9 clases (plomo-zinc combinado). Orden de reporte.
MINERALES = [
    ("212393", "barita"),
    ("212231", "cobre"),
    ("212395", "fluorita"),
    ("212396", "grafito"),
    ("212291", "manganeso"),
    ("212221", "oro"),
    ("212222", "plata"),
    ("212232", "plomo-zinc"),
    ("212324", "silice"),
]

def readcsv(path):
    with open(path, encoding="cp1252", newline="") as fh:
        return list(csv.reader(fh))

def code_of(label):
    return label.split("---")[0].strip().lstrip("﻿")

def name_of(label):
    p = label.split("---", 1)
    return p[1].strip() if len(p) > 1 else ""

def num(x):
    x = (x or "").strip()
    if x == "":
        return 0.0
    return float(x)

def product_columns(header):
    """Devuelve [(col_index, code, name)] de columnas de producto (DI por sector, no Total)."""
    out = []
    for j, h in enumerate(header):
        if h.startswith("DI---Demanda intermedia|"):
            rest = h.split("|", 1)[1]
            if rest.strip() == "Total":
                continue
            out.append((j, code_of(rest), name_of(rest)))
    return out

def load_matrix(rows, prod_cols, codes, name_by_code):
    """Z[i,j] domestica cuadrada, en orden 'codes'. Filas casadas por codigo."""
    row_by_code = {}
    for r in rows[1:]:
        c = code_of(r[0])
        if c in name_by_code and c not in row_by_code:
            row_by_code[c] = r
    n = len(codes)
    Z = np.zeros((n, n))
    col_idx_by_code = {c: j for (j, c, _) in prod_cols}
    for i, ci in enumerate(codes):
        r = row_by_code[ci]
        for jj, cj in enumerate(codes):
            j = col_idx_by_code[cj]
            Z[i, jj] = num(r[j])
    return Z, row_by_code

def load_named_matrix(path, codes, name_by_code):
    """Lee ctec o cdi. Layout: col0 = etiqueta de fila; cols 1.. = 'code---name' directo."""
    rows = readcsv(path)
    col_idx_by_code = {code_of(h): j for j, h in enumerate(rows[0]) if j >= 1}
    row_by_code = {}
    for r in rows[1:]:
        c = code_of(r[0])
        if c in name_by_code and c not in row_by_code:
            row_by_code[c] = r
    n = len(codes)
    M = np.zeros((n, n))
    for i, ci in enumerate(codes):
        r = row_by_code[ci]
        for jj, cj in enumerate(codes):
            M[i, jj] = num(r[col_idx_by_code[cj]])
    return M

def run_year(year, cfg):
    d = readcsv(os.path.join(cfg["dir"], cfg["d"]))
    t = readcsv(os.path.join(cfg["dir"], cfg["t"]))
    hdr = d[0]
    pcols = product_columns(hdr)
    codes = [c for (_, c, _) in pcols]
    name_by_code = {c: nm for (_, c, nm) in pcols}
    n = len(codes)

    # Z domestica
    Z, _ = load_matrix(d, pcols, codes, name_by_code)

    # x = VBP (total output) desde tabla TOTAL, col UTPB (col1), casado por codigo
    tcol1 = 1
    x_by_code = {}
    for r in t[1:]:
        c = code_of(r[0])
        if c in name_by_code and c not in x_by_code:
            x_by_code[c] = num(r[tcol1])
    x = np.array([x_by_code[c] for c in codes])

    # DI total domestica por producto (col2) para validacion de fila
    di_by_code = {}
    for r in d[1:]:
        c = code_of(r[0])
        if c in name_by_code and c not in di_by_code:
            di_by_code[c] = num(r[2])
    DI = np.array([di_by_code[c] for c in codes])

    # --- Coeficientes ---
    xsafe = np.where(x == 0, 1.0, x)
    A = Z / xsafe[np.newaxis, :]          # a_ij = z_ij / x_j   (tecnicos, Leontief)
    B = Z / xsafe[:, np.newaxis]          # b_ij = z_ij / x_i   (allocation, Ghosh)
    I = np.eye(n)
    L = np.linalg.inv(I - A)              # Leontief (I-A)^-1
    G = np.linalg.inv(I - B)              # Ghosh    (I-B)^-1

    # --- Validacion contra INEGI ---
    A_inegi = load_named_matrix(os.path.join(cfg["dir"], cfg["ctec"]), codes, name_by_code)
    L_inegi = load_named_matrix(os.path.join(cfg["dir"], cfg["cdi"]),  codes, name_by_code)
    dA = np.abs(A - A_inegi).max()
    dL = np.abs(L - L_inegi).max()

    # Validacion identidad de fila: x_i ?= DI_i + demanda final domestica_i
    # (chequeo suave sobre minerales)
    # --- Indices Hirschman-Rasmussen (normalizados, media=1) ---
    BL = L.sum(axis=0)                    # hacia atras (col sums de Leontief)
    FL = G.sum(axis=1)                    # hacia adelante (row sums de Ghosh)
    U = BL / BL.mean()                    # poder de dispersion (backward) normalizado
    Ui = FL / FL.mean()                   # sensibilidad de dispersion (forward) normalizado

    # rank (1 = mayor)
    rank_bl = (-BL).argsort().argsort() + 1
    rank_fl = (-FL).argsort().argsort() + 1

    idx = {c: k for k, c in enumerate(codes)}
    results = []
    for code, mineral in MINERALES:
        k = idx[code]
        results.append(dict(
            anio=year, codigo=code, mineral=mineral,
            vbp_mmpesos=round(x[k], 3),
            di_domestica_mmpesos=round(DI[k], 3),
            di_sobre_vbp=round(DI[k] / x[k], 4) if x[k] else None,
            backward_L_colsum=round(BL[k], 4),
            forward_G_rowsum=round(FL[k], 4),
            backward_rasmussen=round(U[k], 4),
            forward_rasmussen=round(Ui[k], 4),
            rank_backward=int(rank_bl[k]),
            rank_forward=int(rank_fl[k]),
            n_sectores=n,
        ))

    # demanda intermedia: top compradores domesticos de cada mineral (fila del mineral en Z)
    di_detail = []
    for code, mineral in MINERALES:
        k = idx[code]
        row = Z[k, :]
        order = np.argsort(-row)
        tot = row.sum()
        for j in order[:8]:
            if row[j] <= 0:
                continue
            di_detail.append(dict(
                anio=year, mineral_codigo=code, mineral=mineral,
                comprador_codigo=codes[j], comprador=name_by_code[codes[j]][:70],
                valor_mmpesos=round(row[j], 3),
                share_del_di=round(row[j] / tot, 4) if tot else None,
            ))

    return dict(year=year, n=n, dA=dA, dL=dL,
                results=results, di_detail=di_detail,
                # muestras para diagnostico
                sample=[(codes[idx[c]], m, round(x[idx[c]],1), round(DI[idx[c]],1))
                        for c, m in MINERALES])

def main():
    allres, alldetail = [], []
    for year, cfg in YEARS.items():
        R = run_year(year, cfg)
        print(f"\n===== {year} =====  n_sectores={R['n']}")
        print(f"  VALIDACION  max|A - ctec_INEGI| = {R['dA']:.3e}   max|L - cdi_INEGI| = {R['dL']:.3e}")
        print(f"  {'mineral':11s} {'VBP':>12s} {'DI_dom':>12s} {'DI/VBP':>7s} {'back':>6s} {'fwd':>6s} {'rB':>4s} {'rF':>4s}")
        for r in R["results"]:
            print(f"  {r['mineral']:11s} {r['vbp_mmpesos']:12.1f} {r['di_domestica_mmpesos']:12.1f} "
                  f"{(r['di_sobre_vbp'] or 0):7.3f} {r['backward_rasmussen']:6.3f} {r['forward_rasmussen']:6.3f} "
                  f"{r['rank_backward']:4d} {r['rank_forward']:4d}")
        allres.extend(R["results"])
        alldetail.extend(R["di_detail"])
    return allres, alldetail

if __name__ == "__main__":
    allres, alldetail = main()
    # escribir salidas
    outdir = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
    f1 = os.path.join(outdir, "mip_encadenamientos_minerales.csv")
    with open(f1, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(allres[0].keys()))
        w.writeheader(); w.writerows(allres)
    f2 = os.path.join(outdir, "mip_demanda_intermedia_minerales.csv")
    with open(f2, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(alldetail[0].keys()))
        w.writeheader(); w.writerows(alldetail)
    print(f"\nEscritos:\n  {f1}\n  {f2}")
