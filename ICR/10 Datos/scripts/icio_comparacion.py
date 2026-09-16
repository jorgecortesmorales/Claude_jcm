# -*- coding: utf-8 -*-
"""
Paso 6 — Comparacion internacional de encadenamientos de la MINERIA.
Fuente: OECD ICIO 2023 ed. (año 2020, archivo 2020_SML.csv del bloque 2016-2020).
Metodo: identico a mip_calc.py pero sobre el BLOQUE DOMESTICO (pais c -> pais c)
de cada pais, a nivel sector-mineria AGREGADO (ISIC Rev4, 45 industrias ICIO).
  A = Z / x (col)      L = (I-A)^-1   backward = colsum(L)
  B = Z / x (fila)     G = (I-B)^-1   forward  = rowsum(G)
  Rasmussen = indice / media  (media de las 45 industrias del pais = 1)
Sectores mineros ICIO:
  B05_06 = mineria de energeticos (carbon, petroleo, gas)
  B07_08 = mineria NO energetica (menas metalicas + otra mineria/canteras)  <- comparable a la tesis
  B09    = servicios de apoyo a la mineria
Paises: MEX (Mexico agregado, like-for-like C1), CHL, AUS, FIN, SWE.
CAVEAT: comparacion a nivel sector-mineria agregado, NO por mineral; base-anio 2020.
Escribe:
  processed/icio_comparacion_mineria.csv         (indicadores por pais x sector minero)
  Bases Originales/12 OECD ICIO/bloques_domesticos_mineria_2020.csv  (Z_cc de mineria, reproducibilidad)
"""
import csv, os
import numpy as np

CSV_ICIO = r"C:\Users\Jorge\AppData\Local\Temp\claude\C--Users-Jorge-OneDrive-Escritorio-Claude-CODE\9bf14e12-846d-41f3-9d66-cec1c99b4f6a\scratchpad\2020_SML.csv"
OUTDIR   = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
BASEDIR  = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\Bases Originales\12 OECD ICIO"

ANIO = 2020
PAISES = ["MEX", "CHL", "AUS", "FIN", "SWE", "CHN", "BRA", "PER"]
NOMBRE_PAIS = {"MEX":"Mexico","CHL":"Chile","AUS":"Australia","FIN":"Finlandia","SWE":"Suecia",
               "CHN":"China","BRA":"Brasil","PER":"Peru"}
# 45 industrias ICIO en orden canonico (sin demanda final)
INDUS = ["A01_02","A03","B05_06","B07_08","B09","C10T12","C13T15","C16","C17_18","C19",
         "C20","C21","C22","C23","C24","C25","C26","C27","C28","C29","C30","C31T33",
         "D","E","F","G","H49","H50","H51","H52","H53","I","J58T60","J61","J62_63",
         "K","L","M","N","O","P","Q","R","S","T"]
MINEROS = {"B05_06":"mineria energeticos","B07_08":"mineria no energetica (metales+otra)","B09":"servicios apoyo mineria"}

def build_col_index(header):
    idx = {h: j for j, h in enumerate(header)}
    out_col = idx["OUT"]
    cols = {}
    for c in PAISES:
        cols[c] = [idx[f"{c}_{ind}"] for ind in INDUS]
    return cols, out_col

def main(CSV_ICIO, ANIO):
    with open(CSV_ICIO, encoding="utf-8", newline="") as fh:
        rd = csv.reader(fh)
        header = next(rd)
        cols, out_col = build_col_index(header)
        # fila de interes: PAIS_INDUS para paises objetivo
        wanted = {}
        for c in PAISES:
            for k, ind in enumerate(INDUS):
                wanted[f"{c}_{ind}"] = (c, k)
        # almacen: Zrow[c][i, :] = flujos de la fila (i) hacia las 45 columnas domesticas de c; xrow[c][i]=OUT
        Zrow = {c: np.zeros((45, 45)) for c in PAISES}
        xvec = {c: np.zeros(45) for c in PAISES}
        found = 0
        for row in rd:
            lab = row[0]
            if lab in wanted:
                c, i = wanted[lab]
                jcols = cols[c]
                Zrow[c][i, :] = [float(row[j] or 0) for j in jcols]
                xvec[c][i] = float(row[out_col] or 0)
                found += 1
        assert found == len(PAISES) * 45, f"filas encontradas={found}"

    results = []
    blocks = []
    for c in PAISES:
        Z = Zrow[c]              # Z[i,j] intra-pais (i vende a j), 45x45
        x = xvec[c].copy()
        xsafe = np.where(x == 0, 1.0, x)
        A = Z / xsafe[np.newaxis, :]     # tecnicos (col)  -> Leontief
        B = Z / xsafe[:, np.newaxis]     # allocation (fila) -> Ghosh
        I = np.eye(45)
        L = np.linalg.inv(I - A)
        G = np.linalg.inv(I - B)
        BL = L.sum(axis=0)               # backward (colsum L)
        FL = G.sum(axis=1)               # forward  (rowsum G)
        U  = BL / BL.mean()
        Ui = FL / FL.mean()
        rank_b = (-BL).argsort().argsort() + 1
        rank_f = (-FL).argsort().argsort() + 1
        vbp_total = x.sum()
        for sec, nom in MINEROS.items():
            k = INDUS.index(sec)
            results.append(dict(
                anio=ANIO, pais=c, pais_nombre=NOMBRE_PAIS[c],
                sector=sec, sector_nombre=nom,
                vbp_musd=round(x[k], 1),
                share_vbp_pct=round(100 * x[k] / vbp_total, 3) if vbp_total else None,
                backward_L_colsum=round(BL[k], 4),
                forward_G_rowsum=round(FL[k], 4),
                backward_rasmussen=round(U[k], 4),
                forward_rasmussen=round(Ui[k], 4),
                rank_backward=int(rank_b[k]),
                rank_forward=int(rank_f[k]),
                n_industrias=45,
            ))
        # guardar bloque domestico de mineria (filas mineras -> todas las columnas) para reproducibilidad
        for sec in MINEROS:
            i = INDUS.index(sec)
            for j, ind_j in enumerate(INDUS):
                if Z[i, j] != 0:
                    blocks.append(dict(pais=c, anio=ANIO, vende=sec, compra=ind_j,
                                       flujo_musd=round(Z[i, j], 3)))
    return results, blocks

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else CSV_ICIO
    anio = int(sys.argv[2]) if len(sys.argv) > 2 else ANIO
    results, blocks = main(path, anio)
    os.makedirs(BASEDIR, exist_ok=True)
    f1 = os.path.join(OUTDIR, "icio_comparacion_mineria.csv")
    # upsert por (anio,pais,sector): conserva otros años ya calculados
    fields = list(results[0].keys())
    existing = []
    if os.path.exists(f1):
        existing = [r for r in csv.DictReader(open(f1, encoding="utf-8"))]
    key = lambda r: (str(r["anio"]), r["pais"], r["sector"])
    newk = {key(r) for r in results}
    allrows = [r for r in existing if key(r) not in newk] + [{k: str(v) for k, v in r.items()} for r in results]
    allrows.sort(key=lambda r: (int(r["anio"]), PAISES.index(r["pais"]) if r["pais"] in PAISES else 9, r["sector"]))
    with open(f1, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(allrows)
    f2 = os.path.join(BASEDIR, f"bloques_domesticos_mineria_{anio}.csv")
    with open(f2, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(blocks[0].keys()))
        w.writeheader(); w.writerows(blocks)
    # impresion diagnostica: foco B07_08 (mineria no energetica, comparable)
    print(f"===== ICIO {anio} — encadenamiento hacia adelante, sector-mineria (media pais=1) =====")
    print(f"{'pais':10s} {'sector':8s} {'fwd_ras':>8s} {'rk_fwd':>6s} {'back_ras':>8s} {'rk_bk':>6s} {'%VBP':>7s}")
    for r in results:
        print(f"{r['pais_nombre']:10s} {r['sector']:8s} {r['forward_rasmussen']:8.3f} "
              f"{r['rank_forward']:6d} {r['backward_rasmussen']:8.3f} {r['rank_backward']:6d} "
              f"{(r['share_vbp_pct'] or 0):7.3f}")
    print(f"\nEscritos:\n  {f1}\n  {f2}")
