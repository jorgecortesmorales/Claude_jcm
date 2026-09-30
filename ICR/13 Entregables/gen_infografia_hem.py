# -*- coding: utf-8 -*-
"""Genera la infografia 2026-09-29 a partir de la 2026-09-07: agrega los paneles de la extraccion
hipotetica (HEM) por mineral (seccion 02) y por pais (seccion 05), construidos desde processed/."""
import csv
R = "C:/Users/Jorge/OneDrive/Escritorio/Claude CODE/ICR/"
P = R + "10 Datos/processed/"
SRC = R + "13 Entregables/Infografias/infografia_indicadores 2026-09-07.html"
OUT = R + "13 Entregables/Infografias/infografia_indicadores 2026-09-29.html"
def rd(f): return list(csv.DictReader(open(P + f, encoding='utf-8')))
s = open(SRC, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a)); s = s.replace(a, b)

NM = {'barita':'Barita','cobre':'Cobre','fluorita':'Fluorita','grafito':'Grafito','manganeso':'Manganeso','oro':'Oro','plata':'Plata','plomo-zinc':'Plomo-zinc','silice':'Sílice'}
MONO = "font-family:'IBM Plex Mono',monospace;font-size:13px"

def bar(label, pct, val_txt, color, lw=82, vw=150):
    return (f'      <div style="display:flex;align-items:center;gap:10px"><span style="width:{lw}px;font-size:14px">{label}</span>'
            f'<div style="flex:1;background:var(--hair,#e6e2d8);border-radius:4px;height:22px"><div style="width:{pct:.0f}%;height:100%;background:{color};border-radius:4px"></div></div>'
            f'<span style="width:{vw}px;{MONO}">{val_txt}</span></div>')

# ---------- HEM por mineral ----------
hm = sorted([r for r in rd('mip_hem_minerales.csv') if r['anio'] == '2018'], key=lambda r: -float(r['hem_total_pct']))
ras = {r['mineral']: float(r['forward_rasmussen']) for r in rd('mip_encadenamientos_minerales.csv') if r['anio'] == '2018'}
mx = max(float(r['hem_total_pct']) for r in hm)
bars = []
for r in hm:
    v = float(r['hem_total_pct']); m = r['mineral']
    bars.append(bar(NM[m], max(v / mx * 100, 0.6), f"{v:.3f} % · R {ras[m]:.2f}", 'var(--copper)' if v >= 0.1 else 'var(--muted)', 90, 150))
PANEL_MIN = f"""  <div class="formula">Extracción hipotética · HEM<sub>k</sub> = 100 · (Σx − Σx̄<sub>(k)</sub>) / Σx &nbsp;·&nbsp; % del VBP nacional</div>
  <div class="panel">
    <div class="cap">Segunda variante · el peso: extracción hipotética total por mineral, MIP 2018 (% del VBP nacional) · R = índice de Rasmussen hacia adelante</div>
    <div style="display:flex;flex-direction:column;gap:9px;margin:14px 2px 4px">
{chr(10).join(bars)}
    </div>
    <div class="legend"><span class="it"><span class="sw" style="background:var(--copper)"></span>HEM ≥ 0.1 % del VBP</span><span class="it"><span class="sw" style="background:var(--muted)"></span>HEM &lt; 0.1 %</span></div>
    <div class="note">Rasmussen mide la <b>intensidad</b> (media de la economía = 1); el HEM, el <b>peso</b>: cuánto del valor bruto de producción nacional se perdería si el mineral dejara de comprar o de vender. Por eslabón, el cobre es el único con clase propia en extracción, refinación y semimanufactura: ambas variantes son altas en los dos primeros y descienden en el tercero. Por entidad (MIP birregional 2018), Sonora encabeza el HEM de la minería (0.53 %), seguida de Coahuila (0.19 %) y Durango (0.13 %).</div>
  </div>
  <div class="take"><span class="mk">→</span><p><b>Las dos variantes, en conjunto.</b> Ordenan distinto: sílice, grafito y manganeso tienen la intensidad más alta (1.92, 1.71, 1.54) y un peso inferior a 0.041 % del VBP; cobre, oro y plata, una intensidad intermedia (1.34, 1.22, 1.17) y el peso más alto (0.33, 0.24 y 0.16 %). Plomo-zinc y barita quedan por debajo de 1 en intensidad, con un peso inferior a 0.05 %.</p></div>
"""
rep("""Plomo y zinc comparten clase SCIAN por coextracción.</p></div>
</div></section>""", """Plomo y zinc comparten clase SCIAN por coextracción.</p></div>
""" + PANEL_MIN + """</div></section>""")
rep('<h2>Encadenamiento hacia adelante · Ghosh</h2>', '<h2>Encadenamiento hacia adelante · Ghosh (intensidad y peso)</h2>')
rep('<a class="jump" href="#ghosh">02 · Ghosh</a>', '<a class="jump" href="#ghosh">02 · Ghosh + HEM</a>')

# ---------- HEM por país ----------
hi = {r['pais']: r for r in rd('icio_hem_mineria.csv') if r['anio'] == '2018' and r['sector'] == 'B07_08'}
h08 = {r['pais']: r for r in rd('icio_hem_mineria.csv') if r['anio'] == '2008' and r['sector'] == 'B07_08'}
gr = {r['pais']: float(r['forward_rasmussen']) for r in rd('icio_comparacion_mineria.csv') if r['anio'] == '2018' and r['sector'] == 'B07_08'}
PN = {'CHL':'Chile','AUS':'Australia','PER':'Perú','CHN':'China','BRA':'Brasil','MEX':'México','SWE':'Suecia','FIN':'Finlandia'}
order = sorted(hi, key=lambda p: -float(hi[p]['hem_total_pct']))
mx = max(float(hi[p]['hem_total_pct']) for p in order)
bars = []
for p in order:
    v = float(hi[p]['hem_total_pct'])
    bars.append(bar(PN[p], v / mx * 100, f"{v:.2f} % ({float(h08[p]['hem_total_pct']):.2f}→) · R {gr[p]:.2f}", 'var(--copper)' if p == 'MEX' else 'var(--muted)', 82, 190))
PANEL_INT = f"""  <div class="panel">
    <div class="cap">Segunda variante · el peso: extracción hipotética de la minería no energética, % del VBP doméstico — OECD ICIO, corte 2018 (2008→2018 entre paréntesis) · R = Ghosh-Rasmussen 2018</div>
    <div style="display:flex;flex-direction:column;gap:9px;margin:14px 2px 4px">
{chr(10).join(bars)}
    </div>
    <div class="note">Los dos coeficientes ordenan a los países de forma casi inversa: México, Finlandia y Suecia combinan un índice de Rasmussen alto con un peso bajo; Chile, Perú y Australia, un índice por debajo de 1 con el peso más alto; China registra valores altos en ambos. Chile pasa de 16.86 % (2008) a 6.74 % (2018). Serie completa 2008 · 2013 · 2018 · 2020 en icio_hem_mineria.csv.</div>
  </div>
"""
rep("""    <div class="legend"><span class="it"><span class="sw" style="background:var(--s-crudo)"></span>exportado en crudo (a reprocesar afuera)</span>""",
    """    <div class="legend"><span class="it"><span class="sw" style="background:var(--s-crudo)"></span>exportado en crudo (a reprocesar afuera)</span>""")
# insertar el panel HEM entre el panel Ghosh y el panel DVA
anchor = """  <div class="panel">
    <div class="cap">El enclave “en dinero”"""
rep(anchor, PANEL_INT + anchor)

rep('"plata":{"2008":[0.796,0.180],"2013":[1.301,0.956],"2018":[1.175,0.89]}', '"plata":{"2008":[0.796,0.180],"2013":[1.301,0.956],"2018":[1.1748,0.89]}')
rep("significan cosas opuestas, como muestra el panel siguiente.", "significan cosas opuestas, como muestran los dos paneles siguientes.")
# ---------- footer ----------
rep("Ghosh = mip_encadenamientos_minerales.csv + 2008_referencia ·",
    "Ghosh = mip_encadenamientos_minerales.csv + 2008_referencia · HEM = mip_hem_minerales.csv, mip_hem_eslabones.csv, hem_estatal_mineria.csv, icio_hem_mineria.csv ·")
open(OUT, 'w', encoding='utf-8').write(s)
print('ok', OUT)
