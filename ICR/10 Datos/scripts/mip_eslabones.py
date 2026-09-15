# -*- coding: utf-8 -*-
"""Ghosh (y Leontief/Rasmussen) por ESLABON de la cadena, no solo el extractivo.
Para cada mineral extrae el encadenamiento de tres clases SCIAN:
  L1 extraccion (clase minera 212xxx), L2 refinacion/fundicion, L3 semimanufactura.
Reutiliza la maquinaria de mip_calc.py (misma matriz domestica, Ghosh sobre TODOS los
sectores). Corte MIP 2013 y 2018. Salida: processed/mip_encadenamientos_eslabones.csv
Atribuibilidad de la clase aguas abajo:
  si   = clase dedicada al mineral (p.ej. 331411 fundicion de cobre)
  comp = clase compartida (p.ej. 331412 oro+plata; 331419 no ferrosos; 331112 ferroaleaciones+acero)
  no   = clase agregada / no atribuible (p.ej. 325180 quimicos basicos; usuario como vidrio 327211)
"""
import csv, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mip_calc as mc
import mip2008_calc as m8

OUT = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"

# L2 (refinacion/quimica primaria) y L3 (semimanufactura) por mineral, con atribuibilidad
ESLAB = {
 "barita":     {"L2": ("325180", "no"),   "L3": (None, None)},
 "cobre":      {"L2": ("331411", "si"),   "L3": ("331420", "si")},
 "fluorita":   {"L2": ("325180", "no"),   "L3": ("325211", "no")},
 "grafito":    {"L2": ("325180", "no"),   "L3": ("327999", "no")},
 "manganeso":  {"L2": ("331112", "comp"), "L3": (None, None)},
 "oro":        {"L2": ("331412", "comp"), "L3": ("331490", "comp")},
 "plata":      {"L2": ("331412", "comp"), "L3": ("331490", "comp")},
 "plomo-zinc": {"L2": ("331419", "comp"), "L3": ("331490", "comp")},
 "silice":     {"L2": ("325180", "no"),   "L3": ("327211", "no")},
}
TIPO = {"L1": "extraccion", "L2": "refinacion", "L3": "semimanufactura"}

def arrays_for_year(year, cfg):
    """Reconstruye G, FL, Ui, ranks para TODOS los sectores (como mip_calc.run_year)."""
    d = mc.readcsv(os.path.join(cfg["dir"], cfg["d"]))
    t = mc.readcsv(os.path.join(cfg["dir"], cfg["t"]))
    hdr = d[0]; pcols = mc.product_columns(hdr)
    codes = [c for (_, c, _) in pcols]
    name_by_code = {c: nm for (_, c, nm) in pcols}
    n = len(codes)
    Z, _ = mc.load_matrix(d, pcols, codes, name_by_code)
    x_by_code = {}
    for r in t[1:]:
        c = mc.code_of(r[0])
        if c in name_by_code and c not in x_by_code:
            x_by_code[c] = mc.num(r[1])
    x = np.array([x_by_code[c] for c in codes])
    xsafe = np.where(x == 0, 1.0, x)
    A = Z / xsafe[np.newaxis, :]; B = Z / xsafe[:, np.newaxis]
    I = np.eye(n)
    L = np.linalg.inv(I - A); G = np.linalg.inv(I - B)
    BL = L.sum(axis=0); FL = G.sum(axis=1)
    U = BL / BL.mean(); Ui = FL / FL.mean()
    rank_bl = (-BL).argsort().argsort() + 1
    rank_fl = (-FL).argsort().argsort() + 1
    idx = {c: k for k, c in enumerate(codes)}
    return dict(codes=codes, name=name_by_code, n=n, x=x,
                FL=FL, BL=BL, U=U, Ui=Ui, rbl=rank_bl, rfl=rank_fl, idx=idx)

def row_for(year, A, mineral, l1code, eslabon, code, atrib):
    if code is None or code not in A["idx"]:
        return dict(anio=year, mineral=mineral, eslabon=eslabon, tipo=TIPO[eslabon],
                    scian=(code or ""), clase="(sin clase separable)", atribuible=(atrib or "-"),
                    vbp_mmpesos="", forward_G_rowsum="", forward_rasmussen="",
                    backward_rasmussen="", rank_forward="", rank_backward="", n_sectores=A["n"])
    k = A["idx"][code]
    return dict(anio=year, mineral=mineral, eslabon=eslabon, tipo=TIPO[eslabon],
                scian=code, clase=A["name"][code][:48], atribuible=atrib,
                vbp_mmpesos=round(A["x"][k], 1),
                forward_G_rowsum=round(A["FL"][k], 4),
                forward_rasmussen=round(A["Ui"][k], 4),
                backward_rasmussen=round(A["U"][k], 4),
                rank_forward=int(A["rfl"][k]), rank_backward=int(A["rbl"][k]),
                n_sectores=A["n"])

def arrays_2008():
    """Arrays G/FL/Ui para TODAS las clases, corte 2008 (referencia), desde mip2008_intermedios."""
    INTER = m8.INTER
    codes, A = m8.read_matrix(os.path.join(INTER, "A_inegi.csv"))
    _,     Z = m8.read_matrix(os.path.join(INTER, "Z_dom.csv"))
    _,     L = m8.read_matrix(os.path.join(INTER, "L_inegi.csv"))
    xmap, _, name = m8.read_vec(os.path.join(INTER, "vec.csv"))
    n = len(codes); x = np.array([xmap[c] for c in codes])
    xsafe = np.where(x == 0, 1.0, x)
    B = Z / xsafe[:, None]; G = np.linalg.inv(np.eye(n) - B)
    BL = L.sum(axis=0); FL = G.sum(axis=1); U = BL / BL.mean(); Ui = FL / FL.mean()
    rbl = (-BL).argsort().argsort() + 1; rfl = (-FL).argsort().argsort() + 1
    idx = {c: k for k, c in enumerate(codes)}
    return dict(codes=codes, name={c: name.get(c, "") for c in codes}, n=n, x=x,
                FL=FL, BL=BL, U=U, Ui=Ui, rbl=rbl, rfl=rfl, idx=idx)

def main():
    out = []
    years = [("2008", arrays_2008())] + [(y, arrays_for_year(y, cfg)) for y, cfg in mc.YEARS.items()]
    for year, A in years:
        for code, mineral in mc.MINERALES:
            # L1 extraccion (clase minera)
            out.append(row_for(year, A, mineral, code, "L1", code, "si"))
            l2c, l2a = ESLAB[mineral]["L2"]; l3c, l3a = ESLAB[mineral]["L3"]
            out.append(row_for(year, A, mineral, code, "L2", l2c, l2a))
            out.append(row_for(year, A, mineral, code, "L3", l3c, l3a))
    f = os.path.join(OUT, "mip_encadenamientos_eslabones.csv")
    with open(f, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    print("Escrito:", f, f"({len(out)} filas)")
    # resumen 2018: forward_rasmussen por eslabon
    print("\n=== Ghosh hacia adelante (Rasmussen, 2018) por eslabon ===")
    print(f"{'mineral':11s} {'L1 extrac':>10s} {'L2 refin':>10s} {'L3 semis':>10s}  (clase L2 / L3, atrib)")
    for code, mineral in mc.MINERALES:
        r = {x["eslabon"]: x for x in out if x["anio"]=="2018" and x["mineral"]==mineral}
        def g(e):
            v=r[e]["forward_rasmussen"]; return f"{v:10.3f}" if v!="" else f"{'n/d':>10s}"
        print(f"{mineral:11s} {g('L1')} {g('L2')} {g('L3')}  ({r['L2']['scian']}/{r['L2']['atribuible']}, {r['L3']['scian']}/{r['L3']['atribuible']})")

if __name__ == "__main__":
    main()
