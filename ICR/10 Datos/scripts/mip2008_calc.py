# -*- coding: utf-8 -*-
"""
MIP INEGI 2008 -> encadenamientos por mineral (CORTE DE REFERENCIA, no encadenado).
Base 2008 / SCIAN 2007, nivel Clase, producto x producto, DOMESTICA.

Usa las matrices A (coef. tecnicos) y L (directos+indirectos) PUBLICADAS por INEGI
como autoritativas, y computa Ghosh G=(I-B)^-1 desde los flujos domesticos.
Indices Hirschman-Rasmussen (atras/adelante) y demanda intermedia domestica por mineral.

VALIDACION:
  (1) max|L_inegi - (I - A_inegi)^-1|  -> precision de maquina (confirma extraccion+algebra).
  (2) max|A_inegi - Z_dom/x|           -> confirma extraccion de flujos y VBP
                                          (limitada por el redondeo de los flujos publicados).

Salida SEPARADA: processed/mip_encadenamientos_2008_referencia.csv
(mismas columnas que mip_encadenamientos_minerales.csv + base_scian + comparabilidad).
"""
import csv, os
import numpy as np

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
INTER = os.path.join(BASE, "processed", "mip2008_intermedios")
OUTDIR = os.path.join(BASE, "processed")

# Corpus: 9 clases con concordancia (plomo-zinc combinado). Manganeso con caveat.
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
MANGANESO_NOTA = ("clase 212291 mas amplia en 2008 (agrega 212292 mercurio/antimonio "
                  "y 212299 otros metalicos); en 2018 son clases aparte -> nivel no comparable")

def read_matrix(path):
    with open(path, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    codes = rows[0][1:]
    n = len(codes)
    M = np.zeros((n, n))
    for i, r in enumerate(rows[1:]):
        M[i, :] = [float(v) for v in r[1:]]
    return codes, M

def read_vec(path):
    x, di, name = {}, {}, {}
    with open(path, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            x[r["codigo"]] = float(r["vbp"])
            di[r["codigo"]] = float(r["di_domestica"])
            name[r["codigo"]] = r["nombre"]
    return x, di, name

def main():
    codes, A = read_matrix(os.path.join(INTER, "A_inegi.csv"))
    cZ, Z = read_matrix(os.path.join(INTER, "Z_dom.csv"))
    cL, L = read_matrix(os.path.join(INTER, "L_inegi.csv"))
    assert codes == cZ == cL, "orden de clases inconsistente entre matrices"
    xmap, dimap, name = read_vec(os.path.join(INTER, "vec.csv"))
    n = len(codes)
    x = np.array([xmap[c] for c in codes])
    DI = np.array([dimap[c] for c in codes])

    I = np.eye(n)
    # --- Validacion (1): L de INEGI vs (I - A)^-1 ---
    L_from_A = np.linalg.inv(I - A)
    dL = np.abs(L - L_from_A).max()
    # --- Validacion (2): A de INEGI vs Z_dom / x (redondeo de flujos publicados) ---
    xsafe = np.where(x == 0, 1.0, x)
    A_from_Z = Z / xsafe[np.newaxis, :]
    dA = np.abs(A - A_from_Z).max()

    print(f"n clases = {n}")
    print(f"VALIDACION (1) max|L_inegi - (I-A_inegi)^-1| = {dL:.3e}  (precision de maquina)")
    print(f"VALIDACION (2) max|A_inegi - Z_dom/x|        = {dA:.3e}  (limitada por redondeo de flujos)")

    # --- Ghosh desde flujos domesticos: B = z_ij / x_i (fila), G = (I-B)^-1 ---
    B = Z / xsafe[:, np.newaxis]
    G = np.linalg.inv(I - B)

    # --- Hirschman-Rasmussen normalizados (media = 1) ---
    BL = L.sum(axis=0)          # hacia atras (col sums de Leontief)
    FL = G.sum(axis=1)          # hacia adelante (row sums de Ghosh)
    U = BL / BL.mean()
    Ui = FL / FL.mean()
    rank_bl = (-BL).argsort().argsort() + 1
    rank_fl = (-FL).argsort().argsort() + 1

    idx = {c: k for k, c in enumerate(codes)}
    results, di_detail = [], []
    for code, mineral in MINERALES:
        k = idx[code]
        nota = MANGANESO_NOTA if mineral == "manganeso" else ""
        results.append(dict(
            anio=2008, codigo=code, mineral=mineral,
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
            base_scian="SCIAN2007_base2008",
            comparabilidad="referencia",
            nota=nota,
        ))
        # demanda intermedia: top compradores domesticos (fila del mineral en Z)
        row = Z[k, :]
        tot = row.sum()
        for j in np.argsort(-row)[:8]:
            if row[j] <= 0:
                continue
            di_detail.append(dict(
                anio=2008, mineral_codigo=code, mineral=mineral,
                comprador_codigo=codes[j], comprador=name[codes[j]][:70],
                valor_mmpesos=round(float(row[j]), 3),
                share_del_di=round(float(row[j] / tot), 4) if tot else None,
                base_scian="SCIAN2007_base2008", comparabilidad="referencia",
            ))

    print(f"\n{'mineral':11s} {'VBP':>12s} {'DI_dom':>12s} {'DI/VBP':>7s} "
          f"{'Gcrudo':>7s} {'back':>6s} {'fwd':>6s} {'rB':>4s} {'rF':>4s}")
    for r in results:
        print(f"{r['mineral']:11s} {r['vbp_mmpesos']:12.1f} {r['di_domestica_mmpesos']:12.1f} "
              f"{(r['di_sobre_vbp'] or 0):7.3f} {r['forward_G_rowsum']:7.3f} "
              f"{r['backward_rasmussen']:6.3f} {r['forward_rasmussen']:6.3f} "
              f"{r['rank_backward']:4d} {r['rank_forward']:4d}")

    f1 = os.path.join(OUTDIR, "mip_encadenamientos_2008_referencia.csv")
    with open(f1, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(results[0].keys()))
        w.writeheader(); w.writerows(results)
    f2 = os.path.join(OUTDIR, "mip_demanda_intermedia_2008_referencia.csv")
    with open(f2, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(di_detail[0].keys()))
        w.writeheader(); w.writerows(di_detail)
    print(f"\nEscritos:\n  {f1}\n  {f2}")
    return dL, dA

if __name__ == "__main__":
    main()
