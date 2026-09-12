# -*- coding: utf-8 -*-
"""Mapas de cadena de valor por mineral (y agregado).
Panel izquierdo: México — estados sombreados por participación en la extracción 2024
  + marcadores de plantas de transformación (nombre de empresa y ciudad).
Panel derecho: mundo — flechas de DESTINO de exportación (rojo, sale de México) y
  ORIGEN de importación (azul, entra a México), top-3 por mineral (Comtrade 2019-2024).
Fuentes: georref_extraccion_mineral_estado_cuantitativo.csv, georref_transformacion_nodos.csv,
  cv_comercio_socios.csv; geometrías en Bases Originales/14 Geo/.
Salida: 13 Entregables/mapas/mapa_<mineral>.png + mapa_conjunto.png
"""
import json, csv, os, unicodedata
from collections import defaultdict
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPoly, FancyArrowPatch
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR"
GEO  = os.path.join(BASE, "10 Datos", "Bases Originales", "14 Geo")
PROC = os.path.join(BASE, "10 Datos", "processed")
OUT  = os.path.join(BASE, "13 Entregables", "mapas")
os.makedirs(OUT, exist_ok=True)

def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii","ignore").decode().lower().strip()
    return s

# ---------- geometrías ----------
def load_polys(path, namekey):
    """devuelve {nombre_norm: (rings, nombre_original)}; rings = lista de anillos exteriores [(lon,lat)...]"""
    d = json.load(open(path, encoding="utf-8"))
    out = {}
    for f in d["features"]:
        nm = f["properties"][namekey]; g = f["geometry"]; polys = []
        if g["type"] == "Polygon": geoms = [g["coordinates"]]
        elif g["type"] == "MultiPolygon": geoms = g["coordinates"]
        else: continue
        for poly in geoms:
            polys.append([(pt[0], pt[1]) for pt in poly[0]])  # anillo exterior
        out[norm(nm)] = (polys, nm)
    return out

MX = load_polys(os.path.join(GEO, "mexico_estados.json"), "name")
WORLD = load_polys(os.path.join(GEO, "world_countries.json"), "name")

def centroid(rings):
    xs = [x for r in rings for x,_ in r]; ys = [y for r in rings for _,y in r]
    return (sum(xs)/len(xs), sum(ys)/len(ys))
MX_CENT = {k: centroid(v[0]) for k,v in MX.items()}

# ---------- coordenadas de ciudades (plantas) lon,lat ----------
CITY = {
 "nacozari":(-109.68,30.37),"cananea":(-110.30,30.98),"ciudad de mexico":(-99.13,19.43),
 "monterrey":(-100.31,25.67),"monterrey / slp":(-100.31,25.67),"vallejo (cdmx)":(-99.15,19.48),
 "torreon":(-103.41,25.54),"san luis potosi":(-100.98,22.15),"tamos":(-97.96,22.20),
 "teziutlan":(-97.36,19.82),"gomez palacio":(-103.50,25.56),"matamoros":(-97.50,25.87),
 "lazaro cardenas / monterrey / varias":(-101.5,19.5),"cuenca de campeche / golfo":(-92.0,19.2),
}
# ---------- centroides de países (trade) lon,lat ----------
COUNTRY = {
 "china":(104,35),"estados unidos":(-98,39),"japon":(138,37),"corea del sur":(128,36),
 "canada":(-106,56),"belgica":(4.5,50.6),"alemania":(10,51),"peru":(-75,-10),"india":(79,22),
 "brasil":(-51,-10),"paises bajos":(5.5,52),"espana":(-3.7,40),"reino unido":(-1.5,52.5),
 "suiza":(8,47),"chile":(-71,-35),"colombia":(-74,4),"taiwan":(121,23.7),"hong kong":(114,22.3),
 "malasia":(102,4),"vietnam":(106,16),"guatemala":(-90.4,15.7),"singapur":(103.8,1.35),
 "italia":(12.5,42),"francia":(2.5,46.7),"turquia":(35,39),"sudafrica":(25,-29),
}
MX_LONLAT = (-102, 23.6)

# ---------- datos ----------
EXTR = defaultdict(dict)     # mineral -> {estado_norm: share%}
for r in csv.DictReader(open(os.path.join(PROC,"georref_extraccion_mineral_estado_cuantitativo.csv"),encoding="utf-8")):
    try: EXTR[r["mineral"]][norm(r["estado"])] = float(r["share_2024_pct"])
    except: pass

NODOS = defaultdict(list)    # mineral -> [(nodo,estado,empresa)]
for r in csv.DictReader(open(os.path.join(PROC,"georref_transformacion_nodos.csv"),encoding="utf-8")):
    NODOS[r["mineral"]].append((r["nodo"], r["estado"], r["empresa"]))

SOC = defaultdict(lambda: defaultdict(float))  # (mineral,flujo) -> {pais: valor}
for r in csv.DictReader(open(os.path.join(PROC,"cv_comercio_socios.csv"),encoding="utf-8")):
    SOC[(r["mineral"],r["flujo"])][r["pais"]] += float(r["valor_usd_2019_2024"])

def top_socios(mineral, flujo, n=3):
    d = SOC[(mineral,flujo)]; tot = sum(d.values()) or 1
    named = [(p,v) for p,v in d.items() if norm(p) in COUNTRY]
    named.sort(key=lambda kv:-kv[1])
    return [(p, v/tot) for p,v in named[:n]]

# plomo-zinc comparten nodos y minería L1 combinada; usar clave de nodos
NODO_KEY = {"plomo":"plomo-zinc","zinc":"plomo-zinc","oro":"oro-plata","plata":"oro-plata"}

# ---------- dibujo ----------
def plot_polys(ax, polys_dict, facecolor="#f2efe9", edgecolor="#b9b2a6", lw=0.4, only=None):
    for k,(rings,nm) in polys_dict.items():
        if only is not None and k not in only: continue
        for ring in rings:
            ax.add_patch(MplPoly(ring, closed=True, facecolor=facecolor, edgecolor=edgecolor, linewidth=lw, zorder=1))

def place_labels(ax, markers, ylim, color="#12507a", tcolor="#0d3a59"):
    """Dibuja estrellas y etiquetas con lineas guia; evita el traslape apilando
    verticalmente las etiquetas cercanas. markers = [(x,y,linea1,linea2)] (linea2 puede ir vacia)."""
    gap = (ylim[1]-ylim[0]) * 0.082
    placed = []
    for (x, y, l1, l2) in sorted(markers, key=lambda m: -m[1]):
        ax.plot(x, y, marker="*", ms=13, color=color, mec="white", mew=0.6, zorder=6)
        side = 1 if x <= -100 else -1               # oeste->etiqueta a la derecha; este->a la izquierda
        tx = x + side*1.4; ty = y
        for _ in range(240):
            if not any(abs(ty-py) < gap and abs(tx-px) < 8 for (px, py) in placed): break
            ty -= gap*0.55
        ty = max(ty, ylim[0]+1.0)
        lbl = f"{l1}\n{l2}" if l2 else l1
        ax.annotate(lbl, xy=(x, y), xytext=(tx, ty),
                    fontsize=6.5, color=tcolor, zorder=7,
                    ha=("left" if side>0 else "right"), va="center",
                    arrowprops=dict(arrowstyle="-", color=color, lw=0.5, shrinkA=1, shrinkB=4),
                    bbox=dict(boxstyle="round,pad=0.16", fc="white", ec=color, lw=0.4, alpha=0.92))
        placed.append((tx, ty))

def draw_mexico(ax, mineral):
    shares = EXTR.get(mineral, {})
    norm_c = Normalize(0, max(shares.values()) if shares else 1)
    cmap = plt.cm.YlOrRd
    for k,(rings,nm) in MX.items():
        sh = shares.get(k)
        fc = cmap(0.15+0.8*norm_c(sh)) if sh else "#eeeae2"
        for ring in rings:
            ax.add_patch(MplPoly(ring, closed=True, facecolor=fc, edgecolor="#9a9488", linewidth=0.5, zorder=1))
    # marcadores de plantas, con lineas guia y descolision vertical de etiquetas
    markers=[]
    for (nodo,estado,empresa) in NODOS.get(NODO_KEY.get(mineral,mineral), []):
        c = CITY.get(norm(nodo)) or MX_CENT.get(norm(estado))
        if not c: continue
        emp = empresa.split("(")[0].strip()
        emp = {"Grupo México":"Grupo México","Compañía Minera Autlán":"Autlán",
               "Met-Mex Peñoles":"Met-Mex Peñoles"}.get(emp, emp[:20])
        markers.append((c[0], c[1], emp, nodo.split("/")[0].strip()))
    place_labels(ax, markers, ylim=(14,33))
    ax.set_xlim(-118,-86); ax.set_ylim(14,33); ax.set_aspect(1.18); ax.axis("off")
    ax.set_title("Extracción (estados) y transformación (plantas)", fontsize=9, color="#333")
    sm = ScalarMappable(norm=norm_c, cmap=cmap); sm.set_array([])
    cb = plt.colorbar(sm, ax=ax, fraction=0.03, pad=0.01); cb.ax.tick_params(labelsize=6)
    cb.set_label("% de la extracción nacional 2024", fontsize=6)

def curved_arrow(ax, p0, p1, color, lw):
    a = FancyArrowPatch(p0, p1, connectionstyle="arc3,rad=0.18", arrowstyle="-|>",
                        mutation_scale=12, lw=lw, color=color, alpha=0.85, zorder=4)
    ax.add_patch(a)

def place_world_labels(ax, items):
    """Etiquetas de país en el mapa mundial con descolisión vertical y línea guía.
    items = [(cx, cy, texto, color_borde, color_texto)]."""
    gap = 11.0; placed = []
    for (cx, cy, text, ec, tc) in sorted(items, key=lambda t: -t[1]):
        tx = cx + 5; ty = cy
        for _ in range(200):
            if not any(abs(ty-py) < gap and abs(tx-px) < 42 for (px, py) in placed): break
            ty -= gap*0.6
        ax.annotate(text, xy=(cx, cy), xytext=(tx, ty), fontsize=6.3, color=tc, zorder=7,
                    ha="left", va="center",
                    arrowprops=dict(arrowstyle="-", color=ec, lw=0.4, shrinkA=1, shrinkB=3),
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=ec, lw=0.3, alpha=0.9))
        placed.append((tx, ty))

def draw_world(ax, mineral):
    plot_polys(ax, WORLD, facecolor="#f2efe9", edgecolor="#c9c2b6", lw=0.3)
    # México resaltado
    plot_polys(ax, MX, facecolor="#dfeaf3", edgecolor="#12507a", lw=0.5, only=set(MX.keys()))
    ax.plot(*MX_LONLAT, "o", ms=5, color="#12507a", zorder=6)
    items=[]
    for p,sh in top_socios(mineral,"X"):
        c = COUNTRY[norm(p)]
        curved_arrow(ax, MX_LONLAT, c, "#c0392b", 0.8+3.5*sh)
        items.append((c[0], c[1], f"{p} {sh*100:.0f}%", "#c0392b", "#8e2a20"))
    for p,sh in top_socios(mineral,"M"):
        c = COUNTRY[norm(p)]
        curved_arrow(ax, c, MX_LONLAT, "#2471a3", 0.6+3.0*sh)
        items.append((c[0], c[1], f"{p} {sh*100:.0f}%", "#2471a3", "#1a4d73"))
    place_world_labels(ax, items)
    ax.set_xlim(-170,180); ax.set_ylim(-58,84); ax.set_aspect(1.3); ax.axis("off")
    ax.set_title("Destino de exportación (rojo) y origen de importación (azul)", fontsize=9, color="#333")

TIPO = {"cobre":"B","oro":"B","plata":"B","plomo":"B","zinc":"B","fluorita":"A (límite)",
        "manganeso":"A","grafito":"C","silice":"C","barita":"D"}
NOMBRE = {"cobre":"Cobre","oro":"Oro","plata":"Plata","plomo":"Plomo","zinc":"Zinc",
          "fluorita":"Fluorita","manganeso":"Manganeso","grafito":"Grafito","silice":"Sílice","barita":"Barita"}

def mineral_map(mineral):
    fig, (a1,a2) = plt.subplots(1,2, figsize=(13,5.2), gridspec_kw={"width_ratios":[1,1.35]})
    draw_mexico(a1, mineral); draw_world(a2, mineral)
    fig.suptitle(f"Cadena de valor — {NOMBRE[mineral]}  ·  tipo {TIPO[mineral]}",
                 fontsize=13, fontweight="bold", color="#1a1a1a", y=0.99)
    fig.text(0.5,0.02,"Extracción: SGM Anuario 2025 (2024). Transformación: reportes corporativos. "
             "Comercio: UN Comtrade 2019-2024. Elaboración propia.", ha="center", fontsize=6.5, color="#666")
    fig.tight_layout(rect=[0,0.03,1,0.96])
    p = os.path.join(OUT, f"mapa_{mineral}.png"); fig.savefig(p, dpi=140); plt.close(fig)
    print("  ", p)

def conjunto_map():
    fig, (a1,a2) = plt.subplots(1,2, figsize=(13,5.6), gridspec_kw={"width_ratios":[1,1.35]})
    # México: intensidad = nº de minerales con extracción en el estado; hubs de transformación
    count = defaultdict(int)
    for m,dd in EXTR.items():
        for st,sh in dd.items():
            if sh>=5: count[st]+=1
    norm_c = Normalize(0, max(count.values()) if count else 1); cmap=plt.cm.YlGnBu
    for k,(rings,nm) in MX.items():
        c=count.get(k); fc=cmap(0.12+0.8*norm_c(c)) if c else "#eeeae2"
        for ring in rings: a1.add_patch(MplPoly(ring,closed=True,facecolor=fc,edgecolor="#9a9488",lw=0.5,zorder=1))
    HUBS={"Torreón":(-103.41,25.54),"Nacozari/Cananea":(-110.0,30.6),"San Luis Potosí":(-100.98,22.15),
          "Matamoros":(-97.50,25.87),"Monterrey":(-100.31,25.67),"Molango/Tamós":(-98.7,20.8),"CDMX":(-99.13,19.43)}
    place_labels(a1, [(c[0],c[1],nm,"") for nm,c in HUBS.items()], ylim=(14,33),
                 color="#b83232", tcolor="#7a1f1f")
    a1.set_xlim(-118,-86); a1.set_ylim(14,33); a1.set_aspect(1.18); a1.axis("off")
    a1.set_title("Estados extractores (nº de minerales, ≥5%) y hubs de transformación", fontsize=9,color="#333")
    sm=ScalarMappable(norm=norm_c,cmap=cmap); sm.set_array([])
    cb=plt.colorbar(sm,ax=a1,fraction=0.03,pad=0.01); cb.ax.tick_params(labelsize=6); cb.set_label("nº de minerales",fontsize=6)
    # Mundo: ejes dominantes agregando todos los minerales
    plot_polys(a2, WORLD, "#f2efe9","#c9c2b6",0.3)
    plot_polys(a2, MX, "#dfeaf3","#12507a",0.5, only=set(MX.keys()))
    a2.plot(*MX_LONLAT,"o",ms=5,color="#12507a",zorder=6)
    aggX=defaultdict(float); aggM=defaultdict(float)
    for (m,fl),dd in SOC.items():
        for p,v in dd.items():
            if norm(p) in COUNTRY:
                (aggX if fl=="X" else aggM)[p]+=v
    tX=sum(aggX.values()) or 1; tM=sum(aggM.values()) or 1
    items=[]
    for p,v in sorted(aggX.items(),key=lambda kv:-kv[1])[:4]:
        c=COUNTRY[norm(p)]; curved_arrow(a2,MX_LONLAT,c,"#c0392b",1+4*v/tX)
        items.append((c[0],c[1],f"{p} {v/tX*100:.0f}%","#c0392b","#8e2a20"))
    for p,v in sorted(aggM.items(),key=lambda kv:-kv[1])[:4]:
        c=COUNTRY[norm(p)]; curved_arrow(a2,c,MX_LONLAT,"#2471a3",0.8+3.5*v/tM)
        items.append((c[0],c[1],f"{p} {v/tM*100:.0f}%","#2471a3","#1a4d73"))
    place_world_labels(a2, items)
    a2.set_xlim(-170,180); a2.set_ylim(-58,84); a2.set_aspect(1.3); a2.axis("off")
    a2.set_title("Ejes comerciales del bloque: exportación (rojo) e importación (azul)", fontsize=9,color="#333")
    fig.suptitle("Cadenas de valor de los minerales críticos — visión de conjunto",
                 fontsize=13,fontweight="bold",color="#1a1a1a",y=0.99)
    fig.text(0.5,0.02,"Extracción: SGM 2024. Comercio: UN Comtrade 2019-2024 (suma de los 10 minerales, socios nombrados). Elaboración propia.",
             ha="center",fontsize=6.5,color="#666")
    fig.tight_layout(rect=[0,0.03,1,0.96])
    p=os.path.join(OUT,"mapa_conjunto.png"); fig.savefig(p,dpi=140); plt.close(fig); print("  ",p)

if __name__=="__main__":
    print("Generando mapas por mineral:")
    for m in NOMBRE: mineral_map(m)
    print("Mapa de conjunto:"); conjunto_map()
    print("Listo.")
