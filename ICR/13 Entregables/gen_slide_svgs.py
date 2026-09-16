# -*- coding: utf-8 -*-
"""Genera SVGs estaticos y limpios para las diapositivas del canvas (Claude Design).
Paleta 'ensayo mineral' consistente con la infografia. Fuente IBM Plex Mono/Sans via CSS del slide."""
import csv, os
BASE=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos\processed"
OUT=r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\13 Entregables\slide_svgs"
os.makedirs(OUT,exist_ok=True)
def rd(p): return list(csv.DictReader(open(os.path.join(BASE,p),encoding='utf-8-sig')))
INK="#211d18";MUT="#8a8175";HAIR="#cfc9bd";SUR="#e6e3db";COP="#b0571e"
COBRE="#c85a1a";ZINC="#0f6fa8";PLOMO="#9a5ba0";CRUDO="#c85a1a";PROC="#0f6fa8"
FS='font-family="IBM Plex Mono, monospace"'
NAMES={'cobre':'Cobre','zinc':'Zinc','plomo':'Plomo','oro':'Oro','plata':'Plata','barita':'Barita','fluorita':'Fluorita','grafito':'Grafito','silice':'Sílice','manganeso':'Manganeso','plomo-zinc':'Plomo-zinc'}

# ---------- Ghosh 2018 horizontal bars ----------
def ghosh():
    mip=rd('mip_encadenamientos_minerales.csv')
    d=[(r['mineral'],float(r['forward_rasmussen'])) for r in mip if r['anio']=='2018']
    d.sort(key=lambda x:-x[1])
    W,H=1120,470;L,R,T,B=150,60,20,40;iw=W-L-R;rowH=(H-T-B)/len(d)
    x1=3.2
    def X(v):return L+v/x1*iw
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for t in [0,1,2,3]:
        s.append(f'<line x1="{X(t):.0f}" y1="{T}" x2="{X(t):.0f}" y2="{T+len(d)*rowH:.0f}" stroke="{HAIR}"/>')
        s.append(f'<text x="{X(t):.0f}" y="{H-14}" text-anchor="middle" fill="{MUT}" font-size="15" {FS}>{t}</text>')
    xr=X(1)
    s.append(f'<line x1="{xr:.0f}" y1="{T}" x2="{xr:.0f}" y2="{T+len(d)*rowH:.0f}" stroke="{COP}" stroke-width="2" stroke-dasharray="6 5"/>')
    for i,(m,v) in enumerate(d):
        y=T+i*rowH+rowH/2;bh=22;col=COP if v>=1 else MUT
        s.append(f'<text x="{L-12}" y="{y+5:.0f}" text-anchor="end" fill="{INK}" font-size="16" {FS}>{NAMES.get(m,m)}</text>')
        s.append(f'<rect x="{L}" y="{y-bh/2:.0f}" width="{iw}" height="{bh}" rx="4" fill="{SUR}"/>')
        w=max(3,X(v)-L)
        s.append(f'<rect x="{L}" y="{y-bh/2:.0f}" width="{w:.0f}" height="{bh}" rx="4" fill="{col}"/>')
        s.append(f'<text x="{L+w+10:.0f}" y="{y+5:.0f}" fill="{INK}" font-size="16" font-weight="500" {FS}>{v:.2f}</text>')
    s.append('</svg>')
    return '\n'.join(s)

# ---------- CCV line cobre/zinc/plomo ----------
def ccv():
    rows=rd('ccv_serie.csv')
    ser={'cobre':COBRE,'zinc':ZINC,'plomo':PLOMO}
    data={k:[] for k in ser}
    for r in rows:
        if r['mineral'] in ser and r['ccv']!='':
            data[r['mineral']].append((int(r['anio']),float(r['ccv'])))
    W,H=1120,470;L,R,T,B=56,20,24,42;iw=W-L-R;ih=H-T-B
    x0,x1=1992,2025;y0,y1=0,2.8
    def X(v):return L+(v-x0)/(x1-x0)*iw
    def Y(v):return T+ih-(min(v,y1)-y0)/(y1-y0)*ih
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for t in [0,0.5,1,1.5,2,2.5]:
        s.append(f'<line x1="{L}" y1="{Y(t):.0f}" x2="{L+iw}" y2="{Y(t):.0f}" stroke="{HAIR}"/>')
        s.append(f'<text x="{L-10}" y="{Y(t)+4:.0f}" text-anchor="end" fill="{MUT}" font-size="14" {FS}>{t:.1f}</text>')
    for xt in range(1994,2026,4):
        s.append(f'<text x="{X(xt):.0f}" y="{H-14}" text-anchor="middle" fill="{MUT}" font-size="14" {FS}>{xt}</text>')
    yr=Y(1)
    s.append(f'<line x1="{L}" y1="{yr:.0f}" x2="{L+iw}" y2="{yr:.0f}" stroke="{COP}" stroke-width="2" stroke-dasharray="6 5"/>')
    s.append(f'<text x="{L+iw}" y="{yr-8:.0f}" text-anchor="end" fill="{COP}" font-size="13" {FS}>paridad 1.0</text>')
    for m,col in ser.items():
        pts=data[m]
        dd=' '.join(('M' if i==0 else 'L')+f'{X(a):.1f} {Y(b):.1f}' for i,(a,b) in enumerate(pts))
        s.append(f'<path d="{dd}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round"/>')
        for a,b in pts:
            s.append(f'<circle cx="{X(a):.1f}" cy="{Y(b):.1f}" r="3.4" fill="{col}"/>')
    s.append('</svg>')
    return '\n'.join(s)

# ---------- comercio 100% stacked ----------
def comercio():
    rows=rd('comercio_posicion_resumen.csv')
    from collections import defaultdict
    acc=defaultdict(list)
    for r in rows:
        if r['X_share_crudo']!='' and int(r['anio'])>=2020:
            acc[r['mineral']].append(float(r['X_share_crudo']))
    order=['barita','plomo','cobre','zinc','fluorita','silice','oro','plata','grafito','manganeso']
    d=[(m,sum(acc[m])/len(acc[m])) for m in order if acc[m]]
    W,H=1120,470;L,R,T,B=150,16,20,40;iw=W-L-R;rowH=(H-T-B)/len(d)
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for t in [0,.25,.5,.75,1]:
        xx=L+t*iw
        s.append(f'<line x1="{xx:.0f}" y1="{T}" x2="{xx:.0f}" y2="{T+len(d)*rowH:.0f}" stroke="{HAIR}"/>')
        s.append(f'<text x="{xx:.0f}" y="{H-14}" text-anchor="middle" fill="{MUT}" font-size="14" {FS}>{int(t*100)}%</text>')
    for i,(m,cr) in enumerate(d):
        y=T+i*rowH+rowH/2;bh=23;wc=cr*iw
        s.append(f'<text x="{L-12}" y="{y+5:.0f}" text-anchor="end" fill="{INK}" font-size="16" {FS}>{NAMES.get(m,m)}</text>')
        s.append(f'<rect x="{L}" y="{y-bh/2:.0f}" width="{max(0,wc-1):.0f}" height="{bh}" rx="3" fill="{CRUDO}"/>')
        s.append(f'<rect x="{L+wc+1:.0f}" y="{y-bh/2:.0f}" width="{max(0,iw-wc-1):.0f}" height="{bh}" rx="3" fill="{PROC}"/>')
        if cr>.13: s.append(f'<text x="{L+8:.0f}" y="{y+5:.0f}" fill="#fff" font-size="15" font-weight="500" {FS}>{round(cr*100)}%</text>')
        if cr<.87: s.append(f'<text x="{L+iw-8:.0f}" y="{y+5:.0f}" text-anchor="end" fill="#fff" font-size="15" font-weight="500" {FS}>{round((1-cr)*100)}%</text>')
    s.append('</svg>')
    return '\n'.join(s)

# ---------- HHI 2023 horizontal bars (regime) ----------
def hhi():
    rows=rd('hhi_consolidado.csv')
    d=[(r['mineral'],int(r['hhi'])) for r in rows if r['anio']=='2023']
    d.sort(key=lambda x:-x[1])
    W,H=1120,470;L,R,T,B=150,70,20,40;iw=W-L-R;rowH=(H-T-B)/len(d)
    x1=10000
    def X(v):return L+v/x1*iw
    def col(v):return "#8a3221" if v>=6000 else (COP if v>=2500 else ("#b98a1e" if v>=1500 else MUT))
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for t in [0,2500,5000,7500,10000]:
        xx=X(t)
        s.append(f'<line x1="{xx:.0f}" y1="{T}" x2="{xx:.0f}" y2="{T+len(d)*rowH:.0f}" stroke="{HAIR}"/>')
        s.append(f'<text x="{xx:.0f}" y="{H-14}" text-anchor="middle" fill="{MUT}" font-size="13" {FS}>{t:,}</text>')
    for i,(m,v) in enumerate(d):
        y=T+i*rowH+rowH/2;bh=22
        s.append(f'<text x="{L-12}" y="{y+5:.0f}" text-anchor="end" fill="{INK}" font-size="16" {FS}>{NAMES.get(m,m)}</text>')
        s.append(f'<rect x="{L}" y="{y-bh/2:.0f}" width="{iw}" height="{bh}" rx="4" fill="{SUR}"/>')
        w=max(3,X(v)-L)
        s.append(f'<rect x="{L}" y="{y-bh/2:.0f}" width="{w:.0f}" height="{bh}" rx="4" fill="{col(v)}"/>')
        s.append(f'<text x="{L+w+10:.0f}" y="{y+5:.0f}" fill="{INK}" font-size="15" font-weight="500" {FS}>{v:,}</text>')
    s.append('</svg>')
    return '\n'.join(s)

for name,fn in [('ghosh',ghosh),('ccv',ccv),('comercio',comercio),('hhi',hhi)]:
    open(os.path.join(OUT,name+'.svg'),'w',encoding='utf-8').write(fn())
    print('escrito',name+'.svg')
print('OK')
