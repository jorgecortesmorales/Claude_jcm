# -*- coding: utf-8 -*-
"""Genera el slide 'Internacional.dc.html' (comparacion internacional + DVA) para el deck,
embebiendo intl_ghosh.png y dva.png como base64, con el sistema de diseno de los demas slides."""
import base64, os
D=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables"
PNG=os.path.join(D,"png_charts")
def b64(name):
    with open(os.path.join(PNG,name),"rb") as fh: return base64.b64encode(fh.read()).decode()
intl=b64("intl_ghosh.png"); dva=b64("dva.png")

card='background:#f6f5f1;border:1px solid #d7d2c7;border-radius:12px;padding:13px 16px;display:flex;flex-direction:column;overflow:hidden'
ct='font-family:\'Spectral\',serif;font-weight:600;font-size:18px;color:#211d18;margin:0 0 6px'
body=f'''<div style="width:1280px;height:720px;background:#efeeea;color:#211d18;font-family:'IBM Plex Sans',system-ui,sans-serif;padding:40px 60px;display:flex;flex-direction:column;overflow:hidden">
<div style="display:flex;align-items:baseline;gap:16px"><span style="font-family:'IBM Plex Mono',monospace;font-size:14px;color:#b0571e;border:1px solid #b0571e;border-radius:6px;padding:3px 9px">09 · INTERNACIONAL</span><h2 style="font-family:'Spectral',serif;font-weight:800;font-size:32px;letter-spacing:-.01em;margin:0">¿Casos de éxito? México frente a los referentes</h2></div>
<div style="font-family:'IBM Plex Mono',monospace;font-size:14px;color:#8a8175;margin:8px 0 0">Sector-minería agregado · OECD ICIO, corte 2018 · 8 países (Chile, Australia, nórdicos + China, Brasil, Perú) · México y China casi idénticos en Ghosh pero opuestos en captura de valor</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;flex:1;margin-top:12px;min-height:0">
<div style="{card}"><div style="{ct}">Encadenamiento hacia adelante de la minería (Ghosh, media país = 1) · corte 2018</div><img src="data:image/png;base64,{intl}" style="width:100%;height:auto;margin:auto 0;object-fit:contain"><div style="font-family:'IBM Plex Mono',monospace;font-size:12px;color:#8a8175;margin-top:6px">China 1.53 ≈ México 1.51; Chile 0.73, Australia 0.83, Perú 0.62 bajo 1.0</div></div>
<div style="{card}"><div style="{ct}">El enclave “en dinero”: % del valor minero exportado en crudo</div><img src="data:image/png;base64,{dva}" style="width:100%;height:auto;margin:auto 0;object-fit:contain"><div style="font-family:'IBM Plex Mono',monospace;font-size:12px;color:#8a8175;margin-top:6px">Perú/Chile ~98% (enclaves más profundos); China 7% (procesa); México 38% engañoso</div></div>
</div>
<div style="background:#211d18;color:#efeeea;border-radius:12px;padding:12px 18px;margin-top:14px;font-family:'IBM Plex Sans',sans-serif;font-size:15px;line-height:1.45"><b style="color:#e0954e">Reencuadre.</b> México y China tienen un Ghosh casi idéntico (1.51 vs 1.53) pero una realidad opuesta: China funde casi todo (7% en crudo), México exporta el cobre 94.7% en concentrado y su agregado se ve “alto” sólo porque promedia los metales preciosos que sí funde. El éxito aguas adelante es China y el <b>modelo nórdico</b> (fundición doméstica), no Chile, Australia, Brasil ni Perú —éste, con la misma canasta que México, es el enclave más profundo—. <span style="color:#8a8175">Regionalmente, sólo el cobre tiene su fundición en el mismo estado que la mina (Sonora).</span></div>
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
open(os.path.join(D,"Internacional.dc.html"),"w",encoding="utf-8").write(tpl)
print("escrito Internacional.dc.html", len(tpl), "bytes")
