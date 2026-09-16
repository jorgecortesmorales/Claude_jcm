# -*- coding: utf-8 -*-
"""
Paso 6.5 — Descomposicion de valor agregado (DVA / reprocesamiento) de la MINERIA.
Complemento del Ghosh: mide el valor RETENIDO vs. el exportado en CRUDO para reprocesarse
en el extranjero (firma del enclave en dinero), sobre la matriz GLOBAL OECD ICIO.

Indicadores por pais s y sector minero i0 (foco B07_08 no energetica):
  - EXGR      : exportaciones brutas del sector (US$ M).
  - DVASH     : valor agregado domestico contenido en esas exportaciones / EXGR
                (DVA = suma_{k in s} v_k (L e)_k ; e = vector de export. del sector).  Alto ~ mineria intensiva en recurso.
  - VAX_min   : VA de la mineria (i0) incorporado en TODAS las exportaciones de s
                = v_i0 * sum_{k in s} L[i0,k] E_k.
  - REPROC    : de VAX_min, share que sale EMBEBIDO en exportaciones de sectores NO mineros
                de s (= transformado en casa antes de exportar). Alto = integra (nordico).
  - CRUDO     : 1 - REPROC = share que sale como producto minero directo (concentrado) para
                reprocesarse afuera. Alto = enclave.
  - FABS      : VA de la mineria absorbido en demanda final EXTRANJERA / VA total de la mineria.
Metodo Leontief global: A=Z/X(col), L=(I-A)^-1, v=VA/X. Fuente OECD ICIO 2023.
CAVEAT: agregado (mineria), no por mineral; base-anio del archivo.
Uso:  py icio_dva.py <ruta AAAA_SML.csv> <anio> [modo]
      modo 'mineria' (default) reporta B05_06/B07_08/B09 de los 5 paises; imprime + devuelve filas.
Escribe/upsertea processed/icio_dva_mineria.csv (una fila por pais-sector-anio).
"""
import csv, os, sys
import numpy as np

OUTDIR = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
OUTCSV = os.path.join(OUTDIR, "icio_dva_mineria.csv")

PAISES = ["MEX", "CHL", "AUS", "FIN", "SWE", "CHN", "BRA", "PER"]
NOMBRE = {"MEX":"Mexico","CHL":"Chile","AUS":"Australia","FIN":"Finlandia","SWE":"Suecia",
          "CHN":"China","BRA":"Brasil","PER":"Peru"}
INDUS = ["A01_02","A03","B05_06","B07_08","B09","C10T12","C13T15","C16","C17_18","C19",
         "C20","C21","C22","C23","C24","C25","C26","C27","C28","C29","C30","C31T33",
         "D","E","F","G","H49","H50","H51","H52","H53","I","J58T60","J61","J62_63",
         "K","L","M","N","O","P","Q","R","S","T"]
INDUS_SET = set(INDUS)
FD_CATS = {"HFCE","NPISH","GGFC","GFCF","INVNT","DPABR"}
MINEROS = ["B05_06","B07_08","B09"]
MIN_SET = set(MINEROS)

def parse_ci(tok):
    # 'MEX_B07_08' -> ('MEX','B07_08'); 'MEX_HFCE' -> ('MEX','HFCE')
    p = tok.split("_", 1)
    return (p[0], p[1]) if len(p) == 2 else (tok, "")

def load_global(path):
    with open(path, encoding="utf-8", newline="") as fh:
        rd = csv.reader(fh)
        header = next(rd)
        ci_cols = []          # (col_index, country, indus)
        fd_cols = []          # (col_index, country)
        out_col = None
        for j, h in enumerate(header):
            if j == 0: continue
            if h == "OUT": out_col = j; continue
            c, code = parse_ci(h)
            if code in INDUS_SET: ci_cols.append((j, c, code))
            elif code in FD_CATS: fd_cols.append((j, c))
        N = len(ci_cols)
        ci_index = {(c, code): k for k, (_, c, code) in enumerate(ci_cols)}
        countries = []
        for (_, c, code) in ci_cols:
            if c not in countries: countries.append(c)
        cidx = {c: k for k, c in enumerate(countries)}
        Z = np.zeros((N, N)); X = np.zeros(N); VA = np.zeros(N)
        FD = np.zeros((N, len(countries)))   # FD[i, country] agregando 6 categorias
        colj_to_k = {j: k for k, (j, _, _) in enumerate(ci_cols)}
        fd_colj_to_c = {j: cidx[c] for (j, c) in fd_cols}
        row_i_of = {}   # supplier CI row -> i
        va_row = None
        for row in rd:
            lab = row[0]
            if lab == "VA": va_row = row; continue
            if lab in ("TLS", "OUT"): continue
            c, code = parse_ci(lab)
            if code not in INDUS_SET: continue
            i = ci_index[(c, code)]
            # Z intermediate
            for (j, cc, cd) in ci_cols:
                v = row[j]
                if v: Z[i, colj_to_k[j]] = float(v)
            # FD aggregated by destination country
            for (j, cc) in fd_cols:
                v = row[j]
                if v: FD[i, fd_colj_to_c[j]] += float(v)
            X[i] = float(row[out_col] or 0)
        # VA row: value added per CI column
        if va_row is not None:
            for (j, c, code) in ci_cols:
                v = va_row[j]
                if v: VA[ci_index[(c, code)]] = float(v)
    return dict(N=N, ci_cols=ci_cols, ci_index=ci_index, countries=countries, cidx=cidx,
                Z=Z, X=X, VA=VA, FD=FD)

def main(path, anio):
    G = load_global(path)
    N = G["N"]; Z = G["Z"]; X = G["X"]; VA = G["VA"]; FD = G["FD"]
    ci_cols = G["ci_cols"]; ci_index = G["ci_index"]; cidx = G["cidx"]
    xsafe = np.where(X == 0, 1.0, X)
    A = Z / xsafe[np.newaxis, :]          # A[i,j] = Z[i,j]/X[j]
    v = VA / xsafe                         # coef VA
    I = np.eye(N)
    print(f"  [{anio}] invirtiendo (I-A) {N}x{N} ...", flush=True)
    L = np.linalg.inv(I - A)
    # pais de cada CI (indice de columna k)
    country_of_k = np.array([cidx[c] for (_, c, _) in ci_cols])
    indus_of_k   = [code for (_, _, code) in ci_cols]
    is_min_k = np.array([1 if code in MIN_SET else 0 for code in indus_of_k])
    # export vector: EXGR[i] = intermed a paises != su pais + demanda final de paises != su pais
    # intermed foraneo:
    same = (country_of_k[:, None] == country_of_k[None, :])   # NxN True si mismo pais (row i, col k)
    EXGR_int = np.where(same, 0.0, Z).sum(axis=1)
    # final foraneo: FD[i, c] con c != pais(i)
    own_c = country_of_k                                       # pais de cada fila i (mismos indices)
    FD_foreign = FD.copy()
    for i in range(N):
        FD_foreign[i, own_c[i]] = 0.0
    EXGR_fin = FD_foreign.sum(axis=1)
    EXGR = EXGR_int + EXGR_fin
    totalFD = FD.sum(axis=1)               # demanda final total por sector proveedor

    rows = []
    for s in PAISES:
        cs = cidx[s]
        # sectores de s
        ks_all = [k for k in range(N) if country_of_k[k] == cs]
        for sec in MINEROS:
            i0 = ci_index[(s, sec)]
            gross = EXGR[i0]
            # DVA en exportaciones del sector i0: e con solo i0
            e = np.zeros(N); e[i0] = gross
            xstar = L @ e
            va_by_k = v * xstar
            dva = va_by_k[country_of_k == cs].sum()
            dvash = dva / gross if gross else None
            # VA de i0 incorporado en las exportaciones de s, por sector exportador k in s
            # contrib_k = v[i0]*L[i0,k]*EXGR[k]
            contrib = v[i0] * L[i0, ks_all] * EXGR[np.array(ks_all)]
            vax_min = contrib.sum()
            mask_min = np.array([1 if indus_of_k[k] in MIN_SET else 0 for k in ks_all])
            via_min = contrib[mask_min == 1].sum()
            via_nonmin = contrib[mask_min == 0].sum()
            reproc = via_nonmin / vax_min if vax_min else None
            crudo = via_min / vax_min if vax_min else None
            # VA de i0 absorbido en demanda final extranjera / VA total de i0
            # VA_i0 en FD de pais c = v[i0]*sum_k L[i0,k]*FD[k,c]
            va_i0_in_fd_c = v[i0] * (L[i0, :] @ FD)      # vector por pais c
            tot_abs = v[i0] * (L[i0, :] @ totalFD)
            foreign_abs = (tot_abs - va_i0_in_fd_c[cs]) / tot_abs if tot_abs else None
            rows.append(dict(
                anio=anio, pais=s, pais_nombre=NOMBRE[s], sector=sec,
                exgr_musd=round(gross,1),
                dva_share=round(dvash,4) if dvash is not None else "",
                vax_mineria_musd=round(vax_min,1),
                reproc_domestico_share=round(reproc,4) if reproc is not None else "",
                crudo_share=round(crudo,4) if crudo is not None else "",
                foreign_abs_share=round(foreign_abs,4) if foreign_abs is not None else "",
            ))
    return rows

def upsert(rows):
    existing = []
    if os.path.exists(OUTCSV):
        existing = list(csv.DictReader(open(OUTCSV, encoding="utf-8")))
    key = lambda r: (str(r["anio"]), r["pais"], r["sector"])
    newkeys = {key(r) for r in rows}
    kept = [r for r in existing if key(r) not in newkeys]
    allrows = kept + rows
    allrows.sort(key=lambda r: (int(r["anio"]), PAISES.index(r["pais"]) if r["pais"] in PAISES else 9, r["sector"]))
    fields = ["anio","pais","pais_nombre","sector","exgr_musd","dva_share","vax_mineria_musd",
              "reproc_domestico_share","crudo_share","foreign_abs_share"]
    with open(OUTCSV, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields); w.writeheader(); w.writerows(allrows)

if __name__ == "__main__":
    path = sys.argv[1]; anio = int(sys.argv[2])
    rows = main(path, anio)
    upsert(rows)
    print(f"\n===== ICIO {anio} — DVA / reprocesamiento, sector-mineria =====")
    print(f"{'pais':10s} {'sec':7s} {'EXGR':>10s} {'DVASH':>6s} {'REPROC':>7s} {'CRUDO':>6s} {'FABS':>6s}")
    for r in rows:
        print(f"{r['pais_nombre']:10s} {r['sector']:7s} {r['exgr_musd']:10.0f} "
              f"{(r['dva_share'] or 0):6} {(r['reproc_domestico_share'] or 0):7} "
              f"{(r['crudo_share'] or 0):6} {(r['foreign_abs_share'] or 0):6}")
    print(f"\nActualizado: {OUTCSV}")
