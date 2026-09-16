# -*- coding: utf-8 -*-
"""Genera Evolucion.dc.html: diapositiva de evolucion temporal para el deck de datos.
Rejilla 2x2 con tres graficos temporales (PNG embebidos como data-URI, para que
funcionen tambien en el Artifact) + una celda de lecturas. Estilo 'ensayo mineral'."""
import base64, os, sys
D=os.path.dirname(os.path.abspath(__file__))
PNG=os.path.join(D,"png_charts")

# Modo:
#   (por defecto)            -> data-URI embebido, escribe Evolucion.dc.html en 13 Entregables (deck autonomo)
#   --filenames <outdir>     -> referencias por nombre de archivo, escribe en <outdir> (canvas Claude Design)
FILENAMES = "--filenames" in sys.argv
OUTDIR = D
if FILENAMES:
    OUTDIR = sys.argv[sys.argv.index("--filenames")+1]

def datauri(name):
    with open(os.path.join(PNG,name),"rb") as fh:
        return "data:image/png;base64,"+base64.b64encode(fh.read()).decode()

def src(name):
    return name if FILENAMES else datauri(name)

hhi=src("hhi_traj.png"); com=src("comercio_evo.png"); gho=src("ghosh_cortes.png")

INK="#211d18"; COP="#b0571e"; MUT="#8a8175"; CARD="#f6f5f1"; HAIR="#d7d2c7"; SOFT="#575048"
def cell(title, img=None, cap=None, body=None):
    inner=f'<div style="font-family:\'Spectral\',serif;font-weight:600;font-size:18px;color:{INK};margin:0 0 6px">{title}</div>'
    if img is not None:
        inner+=f'<img src="{img}" alt="{title}" style="width:100%;height:176px;object-fit:contain;display:block">'
        if cap: inner+=f'<div style="font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:{MUT};margin-top:3px">{cap}</div>'
    if body is not None:
        inner+=body
    return (f'<div style="background:{CARD};border:1px solid {HAIR};border-radius:12px;'
            f'padding:13px 16px;display:flex;flex-direction:column;justify-content:flex-start;overflow:hidden">{inner}</div>')

lecturas=(f'<ul style="margin:5px 0 0;padding-left:18px;color:{SOFT};font-size:13.5px;line-height:1.42">'
  f'<li><b style="color:{INK}">CCV del cobre ≈ 0.22 durante 33 años</b> (diapositiva anterior): la posición en la cadena no se mueve con los ciclos de precio — la firma del enclave.</li>'
  f'<li><b style="color:{INK}">Ghosh 2008→2013→2018</b>: patrón estable (sílice, grafito, cobre arriba; barita abajo).</li>'
  f'<li><b style="color:{INK}">Concentración</b>: fluorita salta a monopolio en 2012; barita se desconcentra tras 2021.</li>'
  f'<li><b style="color:{INK}">Comercio</b>: el cobre se exporta cada vez más en bruto (~42%→~80%).</li>'
  f'</ul>')

grid=(f'<div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;flex:1;margin-top:12px;min-height:0">'
  + cell("Concentración (HHI), 2004–2023", img=hhi, cap="fluorita→monopolio 2012 · barita baja tras 2021")
  + cell("Exportación en bruto, 2015–2024", img=com, cap="% E1 sobre exportación total")
  + cell("Encadenamiento (Ghosh), 3 cortes", img=gho, cap="2008 (ref) → 2013 → 2018")
  + cell("Lecturas", body=lecturas)
  + '</div>')

slide=(f'<div style="width:1280px;height:720px;background:#efeeea;color:{INK};'
  f'font-family:\'IBM Plex Sans\',system-ui,sans-serif;padding:40px 60px;display:flex;flex-direction:column;overflow:hidden">'
  f'<div style="display:flex;align-items:baseline;gap:16px">'
  f'<span style="font-family:\'IBM Plex Mono\',monospace;font-size:14px;color:{COP};border:1px solid {COP};border-radius:6px;padding:3px 9px">05 · EVOLUCIÓN</span>'
  f'<h2 style="font-family:\'Spectral\',serif;font-weight:800;font-size:32px;letter-spacing:-.01em;margin:0">Cómo cambian los indicadores en el tiempo</h2>'
  f'</div>'
  f'<div style="font-family:\'IBM Plex Mono\',monospace;font-size:14px;color:{MUT};margin:8px 0 0">Los descriptores no son estáticos: la dimensión temporal es parte del hallazgo · 1992–2025 según la fuente</div>'
  f'{grid}'
  f'</div>')

html=('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">\n'
  '<style>\n*{box-sizing:border-box}\nbody{margin:0}\n</style>\n</helmet>\n'
  + slide + '\n</x-dc>\n</body>\n</html>\n')

open(os.path.join(OUTDIR,"Evolucion.dc.html"),"w",encoding="utf-8").write(html)
print("escrito Evolucion.dc.html (",len(html),"bytes ) en",OUTDIR,"| modo:",("filenames" if FILENAMES else "data-uri"))
