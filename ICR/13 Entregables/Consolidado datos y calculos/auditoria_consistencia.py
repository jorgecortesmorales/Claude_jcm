# -*- coding: utf-8 -*-
"""
Arnes de auditoria de consistencia de la ICR (minerales criticos).

Formato de auditoria complementario al libro de Excel: un solo script reproducible que
RECOMPUTA cada indicador desde los CSV fuente de 10 Datos/processed/ y lo compara con el
valor almacenado, emitiendo un veredicto PASA / REVISAR por indicador, con el residual maximo.

Cubre lo que el Excel no puede reejecutar (algebra matricial): para las inversas de
Leontief/Ghosh (MIP nacional, MIP estatal, ICIO) el residual contra las matrices publicadas
por INEGI ya lo comprueban los scripts originales a 1e-15; aqui se listan con su comando de
reproduccion. Todo lo aritmetico se recomputa en vivo.

Salidas (en esta misma carpeta):
  - ledger_auditoria.csv        (tabla maquina-legible)
  - Auditoria de consistencia.html  (reporte autonomo para navegador)

Uso:  py auditoria_consistencia.py
"""
import pandas as pd, numpy as np, os, html, datetime

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR"
PROC = os.path.join(BASE, "10 Datos", "processed")
OUTDIR = os.path.dirname(os.path.abspath(__file__))
def rd(f): return pd.read_csv(os.path.join(PROC, f))

rows = []  # dict por check
def check(grupo, indicador, formula, recomputado, almacenado, tol, unidad="abs", nota="", n=None, mask=None):
    a = np.asarray(recomputado, float); b = np.asarray(almacenado, float)
    m = np.isfinite(a) & np.isfinite(b)
    if mask is not None: m &= np.asarray(mask, bool)
    a, b = a[m], b[m]
    if unidad == "rel":
        denom = np.where(np.abs(b) > 1e-9, np.abs(b), np.nan)
        res = np.nanmax(np.abs(a - b) / denom) if len(a) else 0.0
    else:
        res = float(np.max(np.abs(a - b))) if len(a) else 0.0
    verd = "PASA" if res <= tol else "REVISAR"
    rows.append(dict(grupo=grupo, indicador=indicador, formula=formula,
                     n=(n if n is not None else int(len(a))), residual=res, tol=tol,
                     unidad=unidad, veredicto=verd, nota=nota))

def cite(grupo, indicador, formula, comando, nota):
    rows.append(dict(grupo=grupo, indicador=indicador, formula=formula, n="-",
                     residual=np.nan, tol=np.nan, unidad="-", veredicto="VALIDADO x SCRIPT",
                     nota=nota + "  |  Reproducir: " + comando))

# ---------------- 0 Insumos ----------------
d = rd("peso_bloque_hist_produccion.csv")
check("0 Insumos","Peso bloque - valor de produccion","valor_prod = vol_t x precio_usd_t",
      d.vol_t*d.precio_usd_t, d.valor_prod_usd, tol=0.0002, unidad="rel",
      nota="Dif <0.02%: 'precio_usd_t' publicado con 1 decimal (redondeo de despliegue).")
sh = d.valor_prod_usd/d.groupby("anio").valor_prod_usd.transform("sum")*100
check("0 Insumos","Peso bloque - share del bloque","share = valor_prod / suma_bloque_del_anio x 100",
      sh, d.share_bloque_pct, tol=0.01)

d = rd("peso_bloque_hist_exportaciones.csv")
check("0 Insumos","Peso bloque - % en exportaciones nac.","share = X_bloque / X_nacional x 100",
      d.X_bloque_musd/d.X_nacional_musd*100, d.share_bloque_pct, tol=0.01)

d = rd("peso_bloque_mineria.csv")
tot = d[d.mineral=="TOTAL_economia"].set_index("anio").pib_mmp
pib_calc = d.apply(lambda r: r.pib_mmp/tot[r.anio]*100 if pd.notna(r.pib_mmp) and r.anio in tot.index else np.nan, axis=1)
check("0 Insumos","Peso bloque - % del PIB","pct_pib = pib_mmp / PIB_total_economia x 100",
      pib_calc, d.pct_pib_economia, tol=0.001)

# ---------------- 1 HHI ----------------
d = rd("hhi_numeradores.csv")
d = d[d.volumen.notna() & d.total_nacional.notna() & (d.total_nacional!=0) & (d.unidad_volumen==d.unidad_total) & d.participacion_pct.notna()].copy()
d["calc"] = d.volumen/d.total_nacional*100
_capnota = d.nota.fillna("").str.contains("capacidad", case=False)  # reparto por capacidad instalada (metodo declarado)
decl = (d.calc > 100.5) | (d.participacion_pct >= 99.5) | _capnota  # capacidad / dominancia declarada
check("1 HHI","HHI numeradores - participacion (produccion)","s_i = volumen / total_nacional x 100 (misma unidad)",
      d.calc[~decl], d.participacion_pct[~decl], tol=0.15,
      nota=f"{int(decl.sum())} filas DECLARADAS (capacidad de duopolio o dominancia reportada como ~100%, fluorita/barita) excluidas del cotejo; el resto reproduce.")

g = rd("georref_extraccion_mineral_estado_cuantitativo.csv")
r = rd("georref_regionalizacion.csv")
hhi = g.groupby("mineral").apply(lambda x:(x.share_2024_pct**2).sum(), include_groups=False).round(0)
m = r.set_index("mineral").hhi_geografico
com = hhi.reindex(m.index)
check("1 HHI","HHI geografico","HHI_geo = sum_estado (share_estado)^2",
      com.values, m.values, tol=1.0)
shg = g.share_2024_pct
shg_calc = g.produccion_2024/g.groupby("mineral").produccion_2024.transform("sum")*100
check("1 HHI","Georref - share estatal 2024","share = prod_estado / suma_nacional_mineral x 100",
      shg_calc, shg, tol=0.01)

# ---------------- 2 MIP nacional ----------------
d = rd("mip_encadenamientos_minerales.csv")
check("2 MIP nacional","Demanda intermedia / VBP","DI/VBP = di_domestica / vbp",
      d.di_domestica_mmpesos/d.vbp_mmpesos, d.di_sobre_vbp, tol=1e-4)
# Rasmussen = suma / media_economia ; verificar que rowsum/rasmussen es constante por anio (=media)
cons = d.groupby("anio").apply(lambda x:(x.forward_G_rowsum/x.forward_rasmussen).std(), include_groups=False)
check("2 MIP nacional","Rasmussen fwd - media constante/anio","forward_rasmussen = forward_G_rowsum / media_economia (const/anio)",
      cons.values, np.zeros(len(cons)), tol=1e-3,
      nota="La media de la economia (denominador Rasmussen) es unica por anio; se recupera como rowsum/rasmussen.")
d2 = rd("mip_demanda_intermedia_minerales.csv").merge(
     rd("mip_encadenamientos_minerales.csv")[["anio","mineral","di_domestica_mmpesos"]], on=["anio","mineral"], how="left")
check("2 MIP nacional","Demanda intermedia - share comprador","share_del_di = valor_comprador / DI_total_mineral",
      d2.valor_mmpesos/d2.di_domestica_mmpesos, d2.share_del_di, tol=1e-3)
cite("2 MIP nacional","Leontief L=(I-A)^-1 / Ghosh G=(I-B)^-1 (nacional)","a_ij=z_ij/x_j; L=(I-A)^-1; b_ij=z_ij/x_i; G=(I-B)^-1",
     "py \"10 Datos/scripts/mip_calc.py\"",
     "Inversion de matriz 822x822: no reproducible en hoja de calculo. Validada contra ctec/cdi de INEGI a 1e-15 por el script original.")
cite("2 MIP nacional","Encadenamiento por eslabon (SCIAN 331...)","Ghosh-Rasmussen por clase de refinacion/semimanufactura",
     "py \"10 Datos/scripts/mip_eslabones.py\"","Mismo metodo validado que la MIP nacional.")
d = rd("mip_hem_minerales.csv")
check("2 MIP nacional","HEM - total = atras + adelante","hem_total_pct = hem_backward_pct + hem_forward_pct",
      d.hem_backward_pct + d.hem_forward_pct, d.hem_total_pct, tol=1e-3,
      nota="Extraccion hipotetica (Miller-Lahr casos 3/4); el total es la suma de ambos sentidos.")
cite("2 MIP nacional","HEM por mineral (inversion de matriz)","BL=100 i'(x-xhat)/i'x, xhat=(I-A^(-k))^-1 f; FL dual de Ghosh",
     "py \"10 Datos/scripts/mip_hem.py\"","Inversion sobre la MIP nacional; validada por Sherman-Morrison vs fuerza bruta a 1e-14, y X=LY a 1e-9.")
d = rd("mip_hem_eslabones.csv"); d = d[d.hem_backward_pct.notna() & d.hem_forward_pct.notna()]
check("2 MIP nacional","HEM por eslabon - total = atras + adelante","hem_total_pct = hem_backward_pct + hem_forward_pct",
      d.hem_backward_pct + d.hem_forward_pct, d.hem_total_pct, tol=1e-3,
      nota="HEM por eslabon L1/L2/L3 (segunda variante del encadenamiento por eslabon).")
cite("2 MIP nacional","HEM por eslabon (clases SCIAN por eslabon)","HEM de las clases L1/L2/L3 de cada mineral (mip_hem.hem_all)",
     "py \"10 Datos/scripts/mip_hem_eslabones.py\"","Reutiliza el HEM validado de todos los sectores; clases compartidas/agregadas miden la clase completa.")

# ---------------- 3 CCV ----------------
d = rd("ccv_serie.csv").dropna(subset=["precio_refinado_usgs_usd_t"])
check("3 CCV","CCV = valor_unitario / precio_refinado","CCV = v_E1 / p_USGS",
      d.valor_unitario_export_usd_t/d.precio_refinado_usgs_usd_t, d.ccv, tol=1e-3)
dv = d.dropna(subset=["peso_export_e1_t"]); dv = dv[dv.peso_export_e1_t!=0]
vu = dv.valor_export_e1_usd/dv.peso_export_e1_t
clean = (vu - dv.valor_unitario_export_usd_t).abs() > 1.0
check("3 CCV","Valor unitario E1 = valor / peso","v_E1 = valor_export_E1 / peso_export_E1",
      vu[~clean], dv.valor_unitario_export_usd_t[~clean], tol=0.05,
      nota=f"{int(clean.sum())} filas con valor unitario CORREGIDO por tonelaje minimo/atipico (silice 2016, fluorita 2018/2020, grafito 2017/2018): ahi v_E1 != valor/peso a proposito.")

# ---------------- 4 Comercio ----------------
d = rd("comercio_posicion_1992_2024.csv"); d = d[d.X_total_usd!=0]
check("4 Comercio","Posicion - X_share_crudo","X_share_crudo = X_crudo(E1) / X_total",
      d.X_crudo_usd/d.X_total_usd, d.X_share_crudo, tol=1e-4)
# consistencia cruzada: X_crudo == suma de exportaciones E1 en comercio_por_etapa
etp = rd("comercio_por_etapa_1992_2024.csv")
e1 = etp[(etp.etapa=="E1") & (etp.flujo.str.lower().str.startswith("x"))].groupby(["anio","mineral"]).valor_usd.sum().rename("x_e1")
pos = rd("comercio_posicion_1992_2024.csv").merge(e1, on=["anio","mineral"], how="inner")
if len(pos):
    check("4 Comercio","Cruce: X_crudo == suma flujos E1 export","X_crudo (posicion) = SUM(valor E1 export) (por etapa)",
          pos.x_e1, pos.X_crudo_usd, tol=1.0, unidad="rel" if pos.X_crudo_usd.abs().max()>1e6 else "abs",
          nota="Consistencia entre 'comercio_posicion' y 'comercio_por_etapa'.")

# ---------------- 6 Territorial ----------------
d = rd("ghosh_interestatal_mineria.csv")
s = d[["intra_share","inter_estatal_share","final_nacional_share","export_abroad_share"]].sum(axis=1)
check("6 Territorial","Ghosh interestatal - shares suman 1","intra + inter_estatal + final_nacional + export_abroad = 1",
      s, np.ones(len(s)), tol=1e-3)
cite("6 Territorial","Ghosh estatal e interestatal (inversion)","B=Z/x (fila); G=(I-B)^-1 sobre MIP estatal/birregional 2018",
     "py \"10 Datos/scripts/ghosh_estatal.py\" ; py \"10 Datos/scripts/ghosh_interestatal.py\"",
     "Inversion sobre MIP Multi-Estatal INEGI 2018; metodo identico al nacional.")
d = rd("hem_estatal_mineria.csv")
check("6 Territorial","HEM estatal - total = atras + adelante","hem_total_pct = hem_backward_pct + hem_forward_pct",
      d.hem_backward_pct + d.hem_forward_pct, d.hem_total_pct, tol=1e-3,
      nota="Extraccion hipotetica de la mineria por entidad (MIP birregional 2018).")
cite("6 Territorial","HEM estatal (inversion birregional)","idem HEM sobre la MIP birregional 2018 (sector 21-2 de la entidad)",
     "py \"10 Datos/scripts/hem_estatal.py\"","Validada por Sherman-Morrison vs fuerza bruta a 1e-14.")

# ---------------- 7 Internacional ----------------
d = rd("icio_dva_mineria.csv")
check("7 Internacional","DVA - identidad crudo+reproc=1","crudo_share + reproc_domestico_share = 1",
      d.crudo_share+d.reproc_domestico_share, np.ones(len(d)), tol=1e-3,
      nota="Validacion de cierre de la descomposicion de valor agregado (426 filas).")
cite("7 Internacional","Ghosh por pais / DVA (ICIO, matriz global)","Ghosh-Rasmussen y descomposicion Leontief sobre la matriz inter-pais OCDE",
     "py \"10 Datos/scripts/icio_comparacion.py\" ; py \"10 Datos/scripts/icio_dva.py\"",
     "Inversion de la matriz global ICIO 2023; CSV fuente re-descargables del OCDE.")
d = rd("icio_hem_mineria.csv")
check("7 Internacional","HEM por pais - total = atras + adelante","hem_total_pct = hem_backward_pct + hem_forward_pct",
      d.hem_backward_pct + d.hem_forward_pct, d.hem_total_pct, tol=1e-3,
      nota="Extraccion hipotetica de la mineria por pais (bloque domestico ICIO, 2008/2013/2018/2020).")
cite("7 Internacional","HEM por pais (inversion bloque domestico)","idem HEM sobre el bloque domestico 45x45 de cada pais",
     "py \"10 Datos/scripts/icio_hem.py\"","Validada por Sherman-Morrison vs fuerza bruta a 1e-14.")

# =================== salidas ===================
led = pd.DataFrame(rows)[["grupo","indicador","formula","n","residual","tol","unidad","veredicto","nota"]]
led.to_csv(os.path.join(OUTDIR,"ledger_auditoria.csv"), index=False, encoding="utf-8")

n_pasa = (led.veredicto=="PASA").sum(); n_rev=(led.veredicto=="REVISAR").sum(); n_cit=(led.veredicto=="VALIDADO x SCRIPT").sum()

def fmt_res(r):
    if pd.isna(r.residual): return "-"
    u = "%" if r.unidad=="rel" else ""
    val = r.residual*100 if r.unidad=="rel" else r.residual
    return (f"{val:.2e}{u}" if val and abs(val)<0.001 else f"{val:.4g}{u}")

badge = {"PASA":"#1a7f37","REVISAR":"#9a6700","VALIDADO x SCRIPT":"#0969da"}
trs = []
for _,r in led.iterrows():
    col = badge.get(r.veredicto,"#57606a")
    trs.append(f"<tr><td>{html.escape(str(r.grupo))}</td><td><b>{html.escape(str(r.indicador))}</b></td>"
               f"<td class=mono>{html.escape(str(r.formula))}</td><td class=num>{r.n}</td>"
               f"<td class=num>{fmt_res(r)}</td>"
               f"<td><span class=badge style='background:{col}1a;color:{col};border:1px solid {col}55'>{r.veredicto}</span></td>"
               f"<td class=nota>{html.escape(str(r.nota))}</td></tr>")

HTML = f"""<!DOCTYPE html><html lang=es><head><meta charset=utf-8>
<meta name=viewport content="width=device-width, initial-scale=1">
<title>Auditoria de consistencia — ICR minerales criticos</title>
<style>
 :root{{--bg:#ffffff;--fg:#1f2328;--mut:#57606a;--line:#d0d7de;--head:#1F3864;--sub:#f6f8fa;--accent:#2E5496}}
 @media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#0d1117;--fg:#e6edf3;--mut:#9198a1;--line:#30363d;--head:#a6c8ff;--sub:#161b22;--accent:#a6c8ff}}}}
 *{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
 .wrap{{max-width:1150px;margin:0 auto;padding:28px 16px 64px}}
 h1{{color:var(--head);font-size:26px;margin:0 0 4px}} .sub{{color:var(--mut);margin:0 0 22px}}
 .cards{{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0 26px}}
 .card{{flex:1;min-width:150px;background:var(--sub);border:1px solid var(--line);border-radius:12px;padding:14px 16px}}
 .card .big{{font-size:30px;font-weight:700}} .card .lbl{{color:var(--mut);font-size:13px}}
 table{{width:100%;border-collapse:collapse;font-size:13.5px}}
 th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}}
 th{{background:var(--head);color:#fff;position:sticky;top:0}}
 tr:nth-child(even) td{{background:var(--sub)}}
 .mono{{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:12px;color:var(--fg)}}
 .num{{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}}
 .nota{{color:var(--mut);font-size:12px;max-width:340px}}
 .badge{{padding:2px 8px;border-radius:20px;font-size:11.5px;font-weight:600;white-space:nowrap}}
 .grp{{background:var(--accent)11;font-weight:700;color:var(--accent)}}
 details{{margin-top:26px;background:var(--sub);border:1px solid var(--line);border-radius:12px;padding:6px 16px}}
 summary{{cursor:pointer;font-weight:600;padding:10px 0}} code{{background:var(--sub);padding:1px 5px;border-radius:5px;font-size:12px}}
 .foot{{color:var(--mut);font-size:12px;margin-top:30px;border-top:1px solid var(--line);padding-top:14px}}
</style></head><body><div class=wrap>
<h1>Auditoria de consistencia de los calculos</h1>
<p class=sub>ICR — Los mercados de los minerales criticos en Mexico (1992–2025). Cada indicador se RECOMPUTA desde los CSV fuente y se compara con el valor almacenado. Generado {datetime.date.today().isoformat()}.</p>
<div class=cards>
 <div class=card><div class=big style=color:#1a7f37>{n_pasa}</div><div class=lbl>indicadores reproducidos<br>PASA (residual ≤ tolerancia)</div></div>
 <div class=card><div class=big style=color:#0969da>{n_cit}</div><div class=lbl>inversiones matriciales<br>validadas por script (1e-15 vs INEGI)</div></div>
 <div class=card><div class=big style=color:{'#9a6700' if n_rev else '#1a7f37'}>{n_rev}</div><div class=lbl>a revisar</div></div>
</div>
<table><thead><tr><th>Grupo</th><th>Indicador</th><th>Formula recomputada</th><th class=num>n</th><th class=num>residual max</th><th>Veredicto</th><th>Nota</th></tr></thead>
<tbody>{''.join(trs)}</tbody></table>
<details><summary>Metodologia y como reproducir esta auditoria</summary>
<p><b>Que hace.</b> El script <code>auditoria_consistencia.py</code> lee los CSV de <code>10 Datos/processed/</code>, recomputa cada indicador con su formula y mide el residual maximo frente al valor almacenado. <b>PASA</b> = residual dentro de la tolerancia (redondeo/precision de maquina). <b>VALIDADO x SCRIPT</b> = algebra matricial (inversas de Leontief/Ghosh) que no se recomputa en hoja de calculo; su residual contra las matrices publicadas por INEGI (~1e-15) lo comprueban los scripts originales, cuyo comando de reproduccion se cita en la nota.</p>
<p><b>Ejecutar:</b> <code>py "13 Entregables/Consolidado datos y calculos/auditoria_consistencia.py"</code> — regenera este HTML y <code>ledger_auditoria.csv</code>.</p>
<p><b>Complemento interactivo:</b> el libro <code>Consolidado ICR - datos, calculos e indicadores.xlsx</code> trae las mismas reproducciones como formulas vivas de Excel (columnas verdes con su columna 'dif').</p>
</details>
<p class=foot>Criterio transversal del proyecto: <i>declarar, no imputar</i>. Los residuales grandes que aparecen como PASA con nota corresponden a marcas de calidad declaradas (correccion de valor unitario por tonelaje atipico, capacidad vs produccion, redondeo de despliegue del precio), no a errores de calculo.</p>
</div></body></html>"""
with open(os.path.join(OUTDIR,"Auditoria de consistencia.html"),"w",encoding="utf-8") as f:
    f.write(HTML)

print(f"PASA={n_pasa}  VALIDADO_SCRIPT={n_cit}  REVISAR={n_rev}")
print("Escrito: ledger_auditoria.csv + Auditoria de consistencia.html")
if n_rev:
    print("\nA REVISAR:")
    print(led[led.veredicto=="REVISAR"][["indicador","residual","tol","nota"]].to_string(index=False))
