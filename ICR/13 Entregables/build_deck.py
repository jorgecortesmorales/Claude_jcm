# -*- coding: utf-8 -*-
"""Ensambla las 8 diapositivas .dc.html en un deck HTML autonomo (navegable + imprimible a PDF).
Extrae el markup de cada slide (entre </helmet> y </x-dc>) y las reglas <style> del helmet."""
import re, os
D=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables"
# Historial de presentaciones de la infografia (deck autonomo): subir FECHA para una version nueva.
FECHA="2026-09-07"
OUTDIR=os.path.join(D,"Presentaciones de infografia")
os.makedirs(OUTDIR, exist_ok=True)
OUT=os.path.join(OUTDIR, f"presentacion_enclave {FECHA}.html")
ORDER=["Main","Marco","Indicadores","HHI","Ghosh","CCV","Comercio","Evolucion","Internacional","Tipologia"]
styles=[]; slides=[]
for name in ORDER:
    src=open(os.path.join(D,name+".dc.html"),encoding="utf-8").read()
    mstyle=re.search(r"<style>(.*?)</style>",src,re.S)
    if mstyle:
        css=mstyle.group(1)
        # keep only class rules (.card,.n,.fx,.cov,.q ...), drop generic resets to avoid clobbering deck
        for rule in re.findall(r"(\.[^{]+\{[^}]*\})",css):
            if rule.strip() not in styles: styles.append(rule.strip())
    body=re.search(r"</helmet>(.*?)</x-dc>",src,re.S).group(1).strip()
    slides.append(body)

SLIDES="\n".join(f'<section class="slide" data-i="{i}">{s}</section>' for i,s in enumerate(slides))
CLASSCSS="\n".join(styles)
html=f'''<title>Enclave estructural — presentación</title>
<meta name="description" content="Presentación de los cuatro indicadores descriptivos de diez minerales críticos de México, 1992-2025.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
*{{box-sizing:border-box}}
html,body{{margin:0;height:100%;background:#0e0b07;font-family:'IBM Plex Sans',system-ui,sans-serif}}
{CLASSCSS}
#deck{{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.stage{{position:relative;width:1280px;height:720px;flex:none;transform-origin:center center;box-shadow:0 20px 60px rgba(0,0,0,.5);border-radius:6px;overflow:hidden}}
.slide{{position:absolute;inset:0;display:none}}
.slide.on{{display:block}}
.slide>div{{width:1280px !important;height:720px !important}}
/* controls */
#bar{{position:fixed;left:0;right:0;bottom:0;height:52px;display:flex;align-items:center;gap:14px;padding:0 20px;
  background:linear-gradient(0deg,rgba(14,11,7,.92),rgba(14,11,7,0));color:#c8bfae;font-family:'IBM Plex Mono',monospace;font-size:13px;z-index:10}}
#bar button{{background:#1e1810;color:#efe8dc;border:1px solid #3a3126;border-radius:7px;width:36px;height:34px;font-size:16px;cursor:pointer}}
#bar button:hover{{border-color:#e07a3e}}
#bar .count{{min-width:66px;text-align:center}}
#bar .ttl{{color:#9a9182}}
#bar .sp{{margin-left:auto}}
#bar .hint{{color:#6f665a}}
.dots{{display:flex;gap:7px}}
.dots i{{width:9px;height:9px;border-radius:50%;background:#3a3126;cursor:pointer;display:block}}
.dots i.on{{background:#e07a3e}}
@media print{{
  @page{{size:1280px 720px;margin:0}}
  html,body{{background:#fff}}
  #deck{{position:static;display:block}}
  #bar{{display:none}}
  .stage{{box-shadow:none;border-radius:0;page-break-after:always;transform:none !important}}
  .slide{{display:block !important;position:relative;inset:auto}}
  .stage{{height:auto}}
}}
</style>
<div id="deck"><div class="stage" id="stage">
{SLIDES}
</div></div>
<div id="bar">
  <button id="prev" aria-label="Anterior">‹</button>
  <span class="count" id="count">1 / 8</span>
  <button id="next" aria-label="Siguiente">›</button>
  <span class="ttl" id="ttl"></span>
  <span class="sp"></span>
  <span class="dots" id="dots"></span>
  <button id="full" aria-label="Pantalla completa" style="width:auto;padding:0 12px">⛶ Pantalla completa</button>
  <span class="hint">← →  ·  imprime para PDF</span>
</div>
<script>
(function(){{
var slides=[].slice.call(document.querySelectorAll('.slide'));
var titles=["Portada","Marco","Indicadores","HHI · Concentración","Ghosh · Encadenamiento","CCV · Captura de valor","Comercio por etapa","Evolución temporal","Tipología / síntesis"];
var i=0, stage=document.getElementById('stage');
var dots=document.getElementById('dots');
slides.forEach(function(s,k){{var d=document.createElement('i');d.addEventListener('click',function(){{go(k);}});dots.appendChild(d);}});
function fit(){{var pad=70;var s=Math.min((innerWidth-pad)/1280,(innerHeight-pad)/720);stage.style.transform='scale('+s+')';}}
function go(k){{i=Math.max(0,Math.min(slides.length-1,k));
  slides.forEach(function(s,n){{s.classList.toggle('on',n===i);}});
  dots.querySelectorAll('i').forEach(function(d,n){{d.classList.toggle('on',n===i);}});
  document.getElementById('count').textContent=(i+1)+' / '+slides.length;
  document.getElementById('ttl').textContent=titles[i];
}}
addEventListener('keydown',function(e){{if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){{go(i+1);e.preventDefault();}}else if(e.key==='ArrowLeft'||e.key==='PageUp'){{go(i-1);e.preventDefault();}}else if(e.key==='Home'){{go(0);}}else if(e.key==='End'){{go(slides.length-1);}}}});
document.getElementById('next').addEventListener('click',function(){{go(i+1);}});
document.getElementById('prev').addEventListener('click',function(){{go(i-1);}});
document.getElementById('full').addEventListener('click',function(){{if(!document.fullscreenElement){{(document.documentElement.requestFullscreen||function(){{}}).call(document.documentElement);}}else{{document.exitFullscreen();}}}});
stage.addEventListener('click',function(e){{if(e.clientX> innerWidth/2)go(i+1);else go(i-1);}});
addEventListener('resize',fit);fit();go(0);
}})();
</script>
'''
open(OUT,"w",encoding="utf-8").write(html)
print("escrito",OUT,"(",len(html),"bytes,",len(slides),"slides )")
print("styles capturados:",len(styles))
