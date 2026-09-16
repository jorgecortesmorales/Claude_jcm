# -*- coding: utf-8 -*-
"""Genera los Anexos B (series), C (fichas de cadena) y D (vacíos) en Markdown."""
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__)); RED = os.path.dirname(HERE)
PROC = os.path.normpath(os.path.join(RED, "..", "10 Datos", "processed"))
MAN = os.path.join(RED, "manuscrito")

def load(fn):
    with open(os.path.join(PROC, fn), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

NOM = {"cobre":"Cobre","zinc":"Zinc","plomo":"Plomo","plomo-zinc":"Plomo-zinc","oro":"Oro",
       "plata":"Plata","manganeso":"Manganeso","fluorita":"Fluorita","grafito":"Grafito",
       "silice":"Sílice","barita":"Barita"}
ORD = ["cobre","zinc","plomo","oro","plata","manganeso","fluorita","grafito","silice","barita"]

def wide_table(fn, valcol, fmt, y0, y1, minerals=ORD):
    d = defaultdict(dict)
    for r in load(fn):
        try: d[r["mineral"]][int(r["anio"])] = float(r[valcol])
        except Exception: pass
    cols = [m for m in minerals if m in d]
    head = "| Año | " + " | ".join(NOM[m] for m in cols) + " |\n"
    head += "|---|" + "|".join("---:" for _ in cols) + "|\n"
    rows = []
    for y in range(y0, y1+1):
        cells = []
        any_ = False
        for m in cols:
            v = d[m].get(y)
            if v is None: cells.append("")
            else: cells.append(fmt(v)); any_ = True
        if any_:
            rows.append(f"| {y} | " + " | ".join(cells) + " |")
    return head + "\n".join(rows)

# ================= ANEXO B =================
b = ['---\ntitle: "Anexo B. Series completas de indicadores"\nchapter: "B"\nlang: es-ES\n---\n',
     "# Anexo B. Series completas de indicadores\n",
     "Este anexo reúne, año por año, las series que los capítulos de resultados presentan de forma resumida. Todas proceden de las bases en `10 Datos/processed` y son reproducibles con los scripts de `10 Datos/scripts`.\n",
     "## B.1 Coeficiente de captura de valor (CCV) por mineral, 1992-2025\n",
     "Cuadro {#cua:bccv}: Coeficiente de captura de valor por mineral y año (celdas vacías = sin dato; oro y plata no informativos por artefacto de ley). Fuente: cálculo propio con UN Comtrade y precios USGS empalmados (`ccv_serie.csv`).\n",
     wide_table("ccv_serie.csv", "ccv", lambda v: f"{v:.2f}", 1992, 2025) + "\n",
     "## B.2 Índice HHI de concentración por mineral, 2004-2024\n",
     "Cuadro {#cua:bhhi}: Índice HHI de la producción por mineral y año (2004-2020 aproximado por régimen, cota inferior; 2021-2024 por mina). Fuente: cálculo propio, base B5 (`hhi_consolidado.csv`).\n",
     wide_table("hhi_consolidado.csv", "hhi", lambda v: f"{v:.0f}", 2004, 2024) + "\n"]

# B.3 posición comercial
pos = defaultdict(dict)
for r in load("comercio_posicion_resumen.csv"):
    try: pos[r["mineral"]][int(r["anio"])] = float(r["X_share_crudo"])
    except Exception: pass
yrs = sorted({y for m in pos.values() for y in m})
b.append("## B.3 Posición comercial: fracción exportada en bruto (etapa 1) por mineral\n")
b.append("Cuadro {#cua:bpos}: Fracción de la exportación que sale en bruto (X_share_crudo) por mineral y año. Fuente: cálculo propio con UN Comtrade (`comercio_posicion_resumen.csv`).\n")
h = "| Mineral | " + " | ".join(str(y) for y in yrs) + " |\n|---|" + "|".join("---:" for _ in yrs) + "|\n"
rows = []
for m in ORD:
    if m in pos:
        rows.append(f"| {NOM[m]} | " + " | ".join(f"{pos[m][y]:.2f}" if y in pos[m] else "" for y in yrs) + " |")
b.append(h + "\n".join(rows) + "\n")

# B.4 encadenamientos completos
enc = defaultdict(dict)
for r in load("mip_encadenamientos_minerales.csv"):
    enc[r["mineral"]][int(r["anio"])] = (r["forward_rasmussen"], r["backward_rasmussen"])
for r in load("mip_encadenamientos_2008_referencia.csv"):
    enc[r["mineral"]][2008] = (r["forward_rasmussen"], r["backward_rasmussen"])
b.append("## B.4 Encadenamientos de insumo-producto por mineral (2008, 2013, 2018)\n")
b.append("Cuadro {#cua:benc}: Índices de Ghosh-Rasmussen (hacia adelante) y de Leontief-Rasmussen (hacia atrás) por mineral y corte. 2008 = referencia no encadenada. Fuente: cálculo propio con MIP INEGI (`mip_encadenamientos_minerales.csv`).\n")
b.append("| Mineral | Adelante 2008 | Adelante 2013 | Adelante 2018 | Atrás 2008 | Atrás 2013 | Atrás 2018 |\n|---|---:|---:|---:|---:|---:|---:|")
def g(m, y, i):
    v = enc[m].get(y);
    return f"{float(v[i]):.2f}" if v else ""
brows = []
for m in ORD:
    key = "plomo-zinc" if m in ("plomo","zinc") else m
    if key in enc:
        brows.append(f"| {NOM[m]} | {g(key,2008,0)} | {g(key,2013,0)} | {g(key,2018,0)} | {g(key,2008,1)} | {g(key,2013,1)} | {g(key,2018,1)} |")
b.append("\n".join(brows) + "\n\n*Nota: plomo y zinc comparten la clase SCIAN 212232 en la MIP; sus encadenamientos se reportan de forma conjunta.*\n")

open(os.path.join(MAN, "10-anexo-B.md"), "w", encoding="utf-8").write("\n".join(b))
print("Anexo B ok")

# ================= ANEXO C =================
arbol = defaultdict(dict); cuant = defaultdict(dict)
for r in load("cv_arbol_mineral.csv"): arbol[r["mineral"]][r["eslabon"]] = r
for r in load("cv_eslabones_cuantificado.csv"): cuant[r["mineral"]][r["eslabon"]] = r
tip = {r["mineral"]: r for r in load("cv_tipologia.csv")}

c = ['---\ntitle: "Anexo C. Fichas de cadena de valor por mineral"\nchapter: "C"\nlang: es-ES\n---\n',
     "# Anexo C. Fichas de cadena de valor por mineral\n",
     "Cada ficha descompone la cadena del mineral en los eslabones L1-L4 (más L0, el recurso en el suelo), con su clase SCIAN y fracción HS, la cuantificación desde la matriz insumo-producto (valor bruto de producción, PIB y empleo, 2018) y el comercio por etapa (exportaciones e importaciones, promedio 2018-2023, en millones de dólares). Se indica el tipo y el punto de ruptura. El valor de los eslabones no atribuibles no se imputa al mineral (clase compartida).\n"]
def num(x):
    try: return f"{float(x):,.0f}".replace(",", " ")
    except Exception: return "—"
i = 0
for m in ORD:
    if m not in arbol: continue
    i += 1
    t = tip.get(m) or tip.get("plomo-zinc", {})
    c.append(f"## C.{i} {NOM[m]}\n")
    c.append(f"**Tipo {t.get('tipo','—')}** · punto de ruptura: **{t.get('eslabon_ruptura','—')}**. {t.get('justificacion','')}\n")
    c.append(f"Cuadro {{#cua:cf{i}}}: Ficha de cadena de valor — {NOM[m]}. VBP/PIB en millones de pesos (2018); empleo en puestos; X/M en millones de USD (prom. 2018-2023). Fuente: cálculo propio (MIP INEGI 2018; UN Comtrade).\n")
    c.append("| Eslabón | Descripción | SCIAN / HS | VBP | PIB | Empleo | X | M | ¿Atribuible? |")
    c.append("|---|---|---|---:|---:|---:|---:|---:|---|")
    c.append(f"| L0 | Recurso en el suelo (reservas) | — | — | — | — | — | — | — |")
    for esl in ("L1","L2","L3","L4"):
        a = arbol[m].get(esl); q = cuant[m].get(esl)
        if not a and not q: continue
        desc = (a["descripcion"] if a else "")[:44]
        sh = (f"{a['scian']} / {a['hs']}" if a else "")
        atr = {"si":"sí","no":"no","comp":"compartida"}.get((q or a or {}).get("atribuible_mip") or (a or {}).get("atribuible_mip",""), "—")
        vbp = num(q["vbp_mmp_2018"]) if q and q.get("vbp_mmp_2018") else "—"
        pib = num(q["pib_mmp_2018"]) if q and q.get("pib_mmp_2018") else "—"
        emp = num(q["empleo_2018"]) if q and q.get("empleo_2018") else "—"
        X = num(q["X_musd_1823"]) if q and q.get("X_musd_1823") else "—"
        M = num(q["M_musd_1823"]) if q and q.get("M_musd_1823") else "—"
        c.append(f"| {esl} | {desc} | {sh} | {vbp} | {pib} | {emp} | {X} | {M} | {atr} |")
    c.append("")
    if os.path.exists(os.path.join(RED, "figuras", "mapas", f"mapa_{m}.png")):
        c.append(f"![Ilustración {{#fig:map{i}}}: Geografía de la extracción y ejes comerciales — {NOM[m]}. "
                 f"Fuente: elaboración propia (SGM 2024; UN Comtrade 2019-2024).](figuras/mapas/mapa_{m}.png){{width=95%}}")
    c.append("")
open(os.path.join(MAN, "11-anexo-C.md"), "w", encoding="utf-8").write("\n".join(c))
print("Anexo C ok (%d fichas)" % i)

# ================= ANEXO D =================
d = '''---
title: "Anexo D. Declaración de vacíos por indicador"
chapter: "D"
lang: es-ES
---

# Anexo D. Declaración de vacíos por indicador

Fiel al criterio metodológico de **declarar, no imputar** (Capítulo III, III.11), este anexo detalla, para cada indicador, los vacíos de sus series, su causa y el tratamiento aplicado. Ningún vacío se rellenó con supuestos; cuando se completó, se hizo con una fuente identificada y marcada.

Cuadro {#cua:dvac}: Declaración de vacíos por indicador, causa y tratamiento. Fuente: elaboración propia.

| Indicador | Vacío | Causa | Tratamiento |
|---|---|---|---|
| HHI concentración | 1994-2003 sin desglose por empresa | Ausencia de datos de participación por empresa en fuentes abiertas | Declarado; recuperación futura con USGS *Minerals Yearbook* histórico |
| HHI concentración | 2004-2020 aproximado (cota inferior) | Reconstrucción por régimen de mercado (líder + grupos, residual atomístico) | No comparable en nivel con 2021-2024 (por mina); se lee por trayectoria |
| HHI | Sílice sin dato 2024 | Falta distribución por empresa ese año | Declarado; se usa el dato más reciente disponible |
| CCV | Plomo 1994 | Sin comercio espejo para completar el hueco | Declarado, no imputado |
| CCV | Oro y plata no informativos | Artefacto de ley (el valor unitario refleja la ley, no la forma) | Se sustituye por el comercio por etapa (Cap. VII) |
| CCV | Años completados por espejo (valores CIF) | El numerador propio (FOB) tenía huecos de peso | Marcados como espejo; se leen con reserva por posible sobrestimación |
| Encadenamientos MIP | Plomo y zinc en clase combinada (212232) | Coextracción; el INEGI no los separa | Reportados de forma conjunta |
| Encadenamientos por eslabón | Clases de transformación no atribuibles por mineral | Las clases 331/325 agregan varios minerales | El valor no se atribuye al mineral; se ancla con comercio y capacidad instalada |
| Encadenamientos | Corte 2008 no encadenado | Cambio de año base y de clasificación SCIAN | Referencia histórica; se lee por patrón y orden, no por nivel |
| Comercio por etapa | Destino = socio declarado (Comtrade) | Reexportación y *entrepôt* no depurados | Declarado; no altera la dirección del desplazamiento |
| Comparación internacional | Nivel sector-minería agregado, no por mineral | La clasificación ISIC de OECD ICIO no desagrega por mineral | Se cruza con el comercio por etapa por mineral |
| Peso del bloque | PIB y empleo solo en cortes de MIP (2013, 2018) | La MIP no es anual | Declarado; las series de valor y exportaciones sí son anuales |

La convergencia de indicadores independientes —estructura, encadenamientos, captura de valor, comercio por etapa y comparación internacional— sostiene el retrato descriptivo sin que ninguno de estos vacíos comprometa las conclusiones.
'''
open(os.path.join(MAN, "12-anexo-D.md"), "w", encoding="utf-8").write(d)
print("Anexo D ok")
