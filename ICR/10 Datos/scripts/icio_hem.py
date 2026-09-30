# -*- coding: utf-8 -*-
"""
Extraccion hipotetica (HEM) de la MINERIA por pais, sobre OECD ICIO 2023.
Complemento internacional del HEM nacional (mip_hem.py) y estatal (hem_estatal.py),
y paralelo del Ghosh-Rasmussen por pais (icio_comparacion.py).

Sobre el BLOQUE DOMESTICO (pais c -> pais c, 45 industrias ISIC Rev.4) de cada pais se
extrae el sector-mineria y se mide el % del VBP domestico del pais que se perderia:
  - hacia ATRAS: se anula la columna del sector minero en A, se resuelve Leontief;
  - hacia ADELANTE: se anula la fila del sector minero en B, se resuelve Ghosh.
Mide el PESO economico de la mineria en cada economia (comparable entre paises, como el
Rasmussen con media pais=1 mide la intensidad). Sector comparable: B07_08 (mineria no energetica).

Uso:  py icio_hem.py <AAAA_SML.csv> <anio>
Salida (upsert por anio,pais,sector): processed/icio_hem_mineria.csv
"""
import csv, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import icio_comparacion as ic

OUTDIR = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

def load_blocks(CSV, anio):
    """Devuelve {pais: (Z 45x45, x 45)} del bloque domestico intra-pais."""
    with open(CSV, encoding="utf-8", newline="") as fh:
        rd = csv.reader(fh); header = next(rd)
        cols, out_col = ic.build_col_index(header)
        wanted = {}
        for c in ic.PAISES:
            for k, ind in enumerate(ic.INDUS):
                wanted[f"{c}_{ind}"] = (c, k)
        Zrow = {c: np.zeros((45, 45)) for c in ic.PAISES}
        xvec = {c: np.zeros(45) for c in ic.PAISES}
        found = 0
        for row in rd:
            lab = row[0]
            if lab in wanted:
                c, i = wanted[lab]
                Zrow[c][i, :] = [float(row[j] or 0) for j in cols[c]]
                xvec[c][i] = float(row[out_col] or 0)
                found += 1
        assert found == len(ic.PAISES) * 45, f"filas encontradas={found}"
    return {c: (Zrow[c], xvec[c]) for c in ic.PAISES}

def hem_sector(x, Z, k):
    """BL,FL (% del VBP domestico) de extraer el sector k; + validacion Sherman-Morrison vs bruta."""
    n = len(x); xs = np.where(x == 0, 1.0, x)
    A = Z / xs[np.newaxis, :]; B = Z / xs[:, np.newaxis]; I = np.eye(n)
    L = np.linalg.inv(I - A); G = np.linalg.inv(I - B)
    Y = x - Z.sum(axis=1); V = x - Z.sum(axis=0); X = x; sX = X.sum()
    u = L @ A[:, k]; BL = 100.0 * X[k] * u.sum() / ((1.0 + u[k]) * sX)
    w = B[k, :] @ G;  FL = 100.0 * X[k] * w.sum() / ((1.0 + w[k]) * sX)
    Ae = A.copy(); Ae[:, k] = 0.0; BLb = 100.0 * (X - np.linalg.inv(I - Ae) @ Y).sum() / sX
    Be = B.copy(); Be[k, :] = 0.0; FLb = 100.0 * (X - V @ np.linalg.inv(I - Be)).sum() / sX
    return BL, FL, max(abs(BL - BLb), abs(FL - FLb))

def compute(CSV, anio):
    blocks = load_blocks(CSV, anio)
    rows = []; maxd = 0.0
    for c in ic.PAISES:
        Z, x = blocks[c]
        for sec, nom in ic.MINEROS.items():
            k = ic.INDUS.index(sec)
            BL, FL, dd = hem_sector(x, Z, k); maxd = max(maxd, dd)
            rows.append(dict(anio=anio, pais=c, pais_nombre=ic.NOMBRE_PAIS[c],
                sector=sec, sector_nombre=nom,
                vbp_musd=round(float(x[k]), 1),
                hem_backward_pct=round(float(BL), 4),
                hem_forward_pct=round(float(FL), 4),
                hem_total_pct=round(float(BL + FL), 4)))
    return rows, maxd

def upsert(rows):
    f = os.path.join(OUTDIR, "icio_hem_mineria.csv")
    fields = list(rows[0].keys())
    existing = list(csv.DictReader(open(f, encoding="utf-8"))) if os.path.exists(f) else []
    key = lambda r: (str(r["anio"]), r["pais"], r["sector"])
    newk = {key(r) for r in rows}
    allrows = [r for r in existing if key(r) not in newk] + [{k: str(v) for k, v in r.items()} for r in rows]
    order = {p: i for i, p in enumerate(ic.PAISES)}
    allrows.sort(key=lambda r: (int(r["anio"]), order.get(r["pais"], 9), r["sector"]))
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(allrows)
    return f

if __name__ == "__main__":
    CSV = sys.argv[1]; anio = int(sys.argv[2])
    rows, maxd = compute(CSV, anio)
    f = upsert(rows)
    print(f"ICIO HEM {anio} — validacion Sherman-Morrison vs bruta: max|dif|={maxd:.2e}")
    print(f"{'pais':10s}{'sector':8s}{'HEM_back%':>10s}{'HEM_fwd%':>10s}{'HEM_tot%':>10s}")
    for r in rows:
        if r["sector"] == "B07_08":
            print(f"{r['pais_nombre']:10s}{r['sector']:8s}{r['hem_backward_pct']:>10.4f}"
                  f"{r['hem_forward_pct']:>10.4f}{r['hem_total_pct']:>10.4f}")
    print("Escrito:", f)
