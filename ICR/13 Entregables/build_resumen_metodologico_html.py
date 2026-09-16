# -*- coding: utf-8 -*-
"""Convierte el 'Resumen metodológico y de resultados' (.md del vault) a un HTML
autónomo, con el sistema de diseño del proyecto, MathJax (matemática), callouts y
tablas estilizados, y los gráficos PNG embebidos (base64) en cada indicador."""
import re, os, base64
import markdown

FECHA="2026-09-07"
BASE=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR"
SRC=os.path.join(BASE,"13 Entregables","Resumenes descriptivos",f"Resumen metodologico y de resultados {FECHA}.md")
OUT=os.path.join(BASE,"13 Entregables","Resumenes descriptivos",f"Resumen metodologico y de resultados {FECHA}.html")
PNG=os.path.join(BASE,"13 Entregables","png_charts")

def b64(name):
    p=os.path.join(PNG,name)
    with open(p,"rb") as fh: return "data:image/png;base64,"+base64.b64encode(fh.read()).decode()

# graficos por sección (número de encabezado H2 -> [(archivo, pie)])
CHARTS={
 "2":[("hhi.png","HHI por mineral, 2023."),("hhi_traj.png","Trayectoria del HHI 1994-2024 (minerales ilustrativos).")],
 "3":[("ghosh.png","Encadenamiento hacia adelante por mineral, 2018."),("ghosh_cortes.png","Ghosh en los 3 cortes MIP (2008/2013/2018).")],
 "4":[("ccv.png","CCV anual de los metales base, 1992-2025.")],
 "5":[("comercio.png","Composición de exportaciones por etapa, prom. 2020-2024."),("comercio_evo.png","% exportado en bruto, evolución.")],
 "8":[("intl_ghosh.png","Comparación internacional: Ghosh de la minería en 3 cortes (2008/2013/2018).")],
 "9":[("dva.png","% del valor agregado minero exportado en crudo, prom. 1995-2020.")],
}

raw=open(SRC,encoding="utf-8").read()
# --- quitar frontmatter ---
raw=re.sub(r"^---\n.*?\n---\n","",raw,count=1,flags=re.S)
# --- título desde frontmatter (fijo) ---
TITULO="Resumen metodológico y de resultados"
SUBT="Los mercados de los minerales críticos en México · ICR · UAM · "+FECHA
# --- wikilinks [[a|b]] / [[a]] -> texto ---
raw=re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]",r"\2",raw)
raw=re.sub(r"\[\[([^\]]+)\]\]",r"\1",raw)
# --- callouts Obsidian -> <div class="callout" markdown="1"> (pre-proceso, evita fusión de blockquotes) ---
CALL={"abstract":"resumen","info":"info","note":"nota","tip":"tip","important":"clave","warning":"aviso","check":"validación","caution":"cuidado","question":"pregunta","example":"ejemplo","done":"listo"}
def pre_callout(md):
    pat=re.compile(r"^>[ ]*\[!(\w+)\][+-]?[ ]*(.*)((?:\n>.*)*)",re.M)
    def repl(m):
        tipo=m.group(1).lower(); titulo=(m.group(2) or "").strip()
        body="\n".join(re.sub(r"^>[ ]?","",ln) for ln in m.group(3).split("\n")).strip()
        lab=CALL.get(tipo,tipo); head=titulo if titulo else lab.capitalize()
        return (f'<div class="callout c-{tipo}" markdown="1">\n'
                f'<div class="callout-h">{head}</div>\n\n{body}\n\n</div>')
    return pat.sub(repl,md)
raw=pre_callout(raw)
# --- proteger matemática antes de markdown ---
math=[]
def stash(m):
    math.append(m.group(0)); return f"\x00M{len(math)-1}\x00"
raw=re.sub(r"\$\$.*?\$\$",stash,raw,flags=re.S)   # bloque
raw=re.sub(r"(?<!\$)\$[^\$\n]+?\$",stash,raw)      # inline

html=markdown.markdown(raw,extensions=["tables","fenced_code","sane_lists","attr_list","md_in_html"])

# --- restaurar matemática ---
def unstash(m): return math[int(m.group(1))]
html=re.sub(r"\x00M(\d+)\x00",unstash,html)

# --- insertar gráficos al final de cada sección (antes del siguiente <h2> o fin) ---
def chart_html(files):
    out='<div class="charts">'
    for fn,cap in files:
        out+=f'<figure><img src="{b64(fn)}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
    return out+"</div>"
# partir por h2
parts=re.split(r"(<h2>.*?</h2>)",html)
res=[]
for i,p in enumerate(parts):
    res.append(p)
    m=re.match(r"<h2>\s*(\d+)\.",p)
    if m and m.group(1) in CHARTS:
        # buscar dónde termina esta sección (siguiente h2) para insertar al final
        # insertamos justo antes del próximo <h2> concatenando al cuerpo de la sección
        body=parts[i+1] if i+1<len(parts) else ""
        parts[i+1]=body+chart_html(CHARTS[m.group(1)])
html="".join(res)

CSS="""
:root{--bg:#efeeea;--paper:#faf9f6;--ink:#211d18;--ink2:#3a352d;--mut:#8a8175;--cop:#b0571e;--cop2:#c85a1a;--hair:#d7d2c7;--hair2:#e6e2d8}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:16px;line-height:1.6}
.wrap{max-width:920px;margin:0 auto;padding:0 26px 90px}
header.hero{background:var(--ink);color:#efeeea;padding:46px 0 40px;margin-bottom:8px}
header.hero .wrap{padding-top:0;padding-bottom:0}
.kick{font-family:'IBM Plex Mono',monospace;font-size:13px;color:#e0954e;letter-spacing:.04em;margin-bottom:10px}
header h1{font-family:'Spectral',serif;font-weight:800;font-size:40px;line-height:1.05;margin:0 0 8px;letter-spacing:-.01em}
header .sub{color:#b8b1a4;font-size:15px}
h2{font-family:'Spectral',serif;font-weight:800;font-size:27px;margin:44px 0 12px;padding-top:14px;border-top:2px solid var(--hair);letter-spacing:-.01em}
h3{font-family:'IBM Plex Sans',sans-serif;font-weight:600;font-size:18px;color:var(--cop);margin:22px 0 6px}
h4{font-weight:600;font-size:16px;margin:16px 0 4px}
p{margin:9px 0}
a{color:var(--cop)}
strong,b{color:var(--ink)}
code{font-family:'IBM Plex Mono',monospace;font-size:.88em;background:#00000010;padding:1px 5px;border-radius:4px}
hr{border:0;border-top:1px solid var(--hair);margin:26px 0}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:14px;background:var(--paper);border:1px solid var(--hair);border-radius:8px;overflow:hidden}
th,td{padding:7px 11px;text-align:left;border-bottom:1px solid var(--hair2)}
th{background:var(--ink);color:#efeeea;font-weight:600;font-size:13px}
tr:last-child td{border-bottom:0}
tbody tr:nth-child(even){background:#00000005}
td:not(:first-child),th:not(:first-child){text-align:right}
.tablewrap{overflow-x:auto}
.callout{border-left:4px solid var(--mut);background:var(--paper);border-radius:0 8px 8px 0;padding:12px 16px;margin:16px 0}
.callout-h{font-weight:600;font-size:14px;margin-bottom:4px;color:var(--ink)}
.callout-b p{margin:6px 0}
.c-warning,.c-caution{border-left-color:#c0872a;background:#faf4e8}
.c-important,.c-clave{border-left-color:var(--cop);background:#fbeee4}
.c-check,.c-done{border-left-color:#2e7d52;background:#eaf5ee}
.c-abstract,.c-info,.c-note,.c-tip{border-left-color:#3a7ca5;background:#eaf1f6}
.callout-h::before{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--mut);margin-right:7px}
.c-warning .callout-h::before,.c-caution .callout-h::before{content:"▲"}
.c-important .callout-h::before,.c-clave .callout-h::before{content:"◆"}
.c-check .callout-h::before,.c-done .callout-h::before{content:"✓"}
.c-abstract .callout-h::before,.c-info .callout-h::before,.c-note .callout-h::before,.c-tip .callout-h::before{content:"❯"}
.charts{display:grid;grid-template-columns:1fr;gap:16px;margin:18px 0 6px}
@media(min-width:680px){.charts{grid-template-columns:1fr 1fr}}
figure{margin:0;background:var(--paper);border:1px solid var(--hair);border-radius:10px;padding:10px}
figure img{width:100%;height:auto;display:block;border-radius:4px}
figcaption{font-size:12px;color:var(--mut);margin-top:6px;font-style:italic}
mjx-container{overflow-x:auto;overflow-y:hidden;max-width:100%}
.toc{background:var(--paper);border:1px solid var(--hair);border-radius:10px;padding:14px 18px;margin:22px 0}
.toc b{display:block;font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--mut);margin-bottom:6px;letter-spacing:.05em}
.toc a{display:inline-block;margin:2px 14px 2px 0;font-size:14px}
footer{margin-top:40px;padding-top:16px;border-top:2px solid var(--hair);color:var(--mut);font-size:13px}
@media print{header.hero{background:#fff;color:#000;border-bottom:2px solid #000}header h1{color:#000}.charts{grid-template-columns:1fr 1fr}}
"""

MJX="""
<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""

doc=f"""<!doctype html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITULO} · ICR</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{CSS}</style>{MJX}
</head><body>
<header class="hero"><div class="wrap">
<div class="kick">ICR · MAESTRÍA EN ECONOMÍA · UAM · 10 MINERALES · 1992-2025</div>
<h1>{TITULO}</h1><div class="sub">{SUBT}</div></div></header>
<div class="wrap tablewrap-note">
{html}
<footer>Elaboración propia · versión HTML del documento del vault (mismo contenido, matemática renderizada con MathJax). Bases e indicadores en <code>10 Datos/processed</code>; scripts en <code>10 Datos/scripts</code>.</footer>
</div>
<script>
// envolver tablas para scroll horizontal en movil
document.querySelectorAll('table').forEach(function(t){{var w=document.createElement('div');w.className='tablewrap';t.parentNode.insertBefore(w,t);w.appendChild(t);}});
</script>
</body></html>"""

open(OUT,"w",encoding="utf-8").write(doc)
print("escrito:",OUT,"(",len(doc),"bytes )")
