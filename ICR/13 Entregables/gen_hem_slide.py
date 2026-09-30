# -*- coding: utf-8 -*-
"""Genera el slide 'HEM.dc.html' (extraccion hipotetica: segunda variante del Ghosh) para el deck,
embebiendo hem.png y hem_intl.png como base64, con el sistema de diseno de los demas slides.
Correr despues de gen_png_charts.py y antes de build_deck.py."""
import base64, os
D=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables"
PNG=os.path.join(D,"png_charts")
def b64(name):
    with open(os.path.join(PNG,name),"rb") as fh: return base64.b64encode(fh.read()).decode()
hem=b64("hem.png"); intl=b64("hem_intl.png")

card='background:#f6f5f1;border:1px solid #d7d2c7;border-radius:12px;padding:13px 16px;display:flex;flex-direction:column;overflow:hidden'
ct='font-family:\'Spectral\',serif;font-weight:600;font-size:18px;color:#211d18;margin:0 0 6px'
mono='font-family:\'IBM Plex Mono\',monospace;font-size:12px;color:#8a8175;margin-top:6px'
body=f'''<div style="width:1280px;height:720px;background:#efeeea;color:#211d18;font-family:'IBM Plex Sans',system-ui,sans-serif;padding:40px 60px;display:flex;flex-direction:column;overflow:hidden">
<div style="display:flex;align-items:baseline;gap:16px"><span style="font-family:'IBM Plex Mono',monospace;font-size:14px;color:#b0571e;border:1px solid #b0571e;border-radius:6px;padding:3px 9px">02b · HEM</span><h2 style="font-family:'Spectral',serif;font-weight:800;font-size:32px;letter-spacing:-.01em;margin:0">Segunda variante del Ghosh: el peso del encadenamiento</h2></div>
<div style="font-family:'IBM Plex Mono',monospace;font-size:14px;color:#8a8175;margin:8px 0 0">Extracción hipotética (Miller y Lahr, 2001; Morales-López, 2023) · % del VBP que se perdería si el sector dejara de comprar o de vender · MIP INEGI 2018 y OECD ICIO 2018</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;flex:1;margin-top:12px;min-height:0">
<div style="{card}"><div style="{ct}">Por mineral · HEM total y Rasmussen frente a HEM hacia adelante</div><img src="data:image/png;base64,{hem}" style="width:100%;height:auto;margin:auto 0;object-fit:contain"><div style="{mono}">Cobre 0.33 %, oro 0.24 %, plata 0.16 % del VBP; sílice, grafito y manganeso &lt; 0.041 %</div></div>
<div style="{card}"><div style="{ct}">Por país · minería no energética, % del VBP doméstico</div><img src="data:image/png;base64,{intl}" style="width:100%;height:auto;margin:auto 0;object-fit:contain"><div style="{mono}">Chile 6.74 %, Australia 5.23 %, Perú 4.49 %, China 3.53 %, Brasil 2.14 %, México 1.44 %</div></div>
</div>
<div style="background:#211d18;color:#efeeea;border-radius:12px;padding:12px 18px;margin-top:14px;font-family:'IBM Plex Sans',sans-serif;font-size:15px;line-height:1.45"><b style="color:#e0954e">Las dos variantes, en conjunto.</b> El índice de Rasmussen mide la intensidad (media = 1); el HEM, el peso. Ordenan distinto: sílice, grafito y manganeso tienen la intensidad más alta y un peso bajo; cobre, oro y plata, una intensidad intermedia y el peso más alto. Entre países el orden es casi inverso: México y los nórdicos, intensidad alta y peso bajo; Chile, Perú y Australia, intensidad por debajo de 1 y el peso más alto; China, alto en ambos. <span style="color:#8a8175">Por entidad (2018), Sonora encabeza el peso (0.53 %).</span></div>
</div>'''

tpl=f'''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
*{{box-sizing:border-box}}
body{{margin:0}}
</style>
</helmet>
{body}
</x-dc>
</body>
</html>'''
open(os.path.join(D,"HEM.dc.html"),"w",encoding="utf-8").write(tpl)
print("escrito HEM.dc.html", len(tpl), "bytes")
