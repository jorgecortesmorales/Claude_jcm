# -*- coding: utf-8 -*-
"""Preguntas B/E (piloto cobre) — menciones de tecnologias de frontera en documentos de empresas.
Busca, en el texto de cada documento, terminos de una lista de trabajo de 15 tecnologias (T01-T15) y guarda
cada fragmento encontrado para su verificacion manual. Una mencion NO equivale a adopcion: el fragmento se
clasifica despues a mano (adoptada / proyecto o prueba / otra empresa o generico / no aplica).

Uso: py pbe_frontera_menciones.py <archivo.txt|pdf> <etiqueta_documento> [<etiqueta>...]
     o importar buscar(texto, etiqueta) desde otro script.
Salida: processed/cobre_frontera_menciones.csv (se agrega; columnas: documento, tecnologia, termino, fragmento)
"""
import os, re, sys, csv

BASE = r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos"
OUT = os.path.join(BASE, "processed", "cobre_frontera_menciones.csv")

TEC = {  # lista de trabajo; validar contra la literatura de innovacion minera (por fichar)
 "T01 Acarreo autonomo": r"autonomous haul|autonomous truck|driverless|camiones? autónomos?|acarreo autónomo",
 "T02 Acarreo electrificado (trolley o bateria)": r"trolley|battery[- ]electric (haul|truck)|electric haul|camiones? eléctricos?",
 "T03 Operacion remota o centro integrado": r"remote operations? cent|integrated remote|remotely operated|teleoperat|centro integrado de operaci|operación remota",
 "T04 Trituracion y transporte en el tajo (IPCC)": r"in[- ]pit crush|IPCC|trituración en (el )?tajo",
 "T05 Molienda con rodillos de alta presion (HPGR)": r"HPGR|high[- ]pressure grinding|rodillos de alta presión",
 "T06 Seleccion de mineral por sensores": r"ore sorting|sensor[- ]based sort|bulk sort|clasificación (de mineral )?por sensores",
 "T07 Flotacion de particula gruesa": r"coarse particle flotation|HydroFloat|flotación de partículas? gruesas?",
 "T08 Molienda fina agitada o celdas Jameson": r"Jameson|IsaMill|Vertimill|stirred mill|molino(s)? agitado",
 "T09 Relaves filtrados o espesados": r"filtered tailings|dry[- ]stack|thickened tailings|paste tailings|relaves filtrados|jales filtrados|relaves espesados",
 "T10 Agua de mar o desalinizada": r"desalinat|seawater|sea water|agua de mar|desaliniz",
 "T11 Lixiviacion de sulfuros primarios o biolixiviacion": r"bioleach|bio-leach|chloride leach|primary sulphide leach|primary sulfide leach|Cuprochlor|Jetti|biolixivia|lixiviación de sulfuros",
 "T12 Fusion o conversion flash": r"flash smelt|flash convert|flash furnace|horno flash|fusión flash",
 "T13 Gemelo digital, aprendizaje automatico o IA": r"digital twin|machine learning|artificial intelligence|inteligencia artificial|gemelo digital",
 "T14 Captura de azufre en fundicion": r"sulph?ur (dioxide )?(capture|fixation|recovery)|captura de (dióxido de )?azufre|recaptura de dióxido",
 "T15 Reciclaje de material secundario en fundicion": r"e-scrap|electronic scrap|recycled material|secondary (raw )?material|chatarra electrónica",
}
PAT = {k: re.compile(v, re.I) for k, v in TEC.items()}

def texto_de(path):
    if path.lower().endswith(".pdf"):
        from pypdf import PdfReader
        return " ".join((p.extract_text() or "") for p in PdfReader(path).pages)
    return open(path, encoding="utf-8", errors="ignore").read()

def buscar(texto, etiqueta, ancho=220):
    t = re.sub(r"\s+", " ", texto)
    filas = []
    for k, p in PAT.items():
        for m in p.finditer(t):
            filas.append([etiqueta, k, m.group(0), t[max(0, m.start() - ancho):m.end() + ancho]])
    return filas

def guardar(filas):
    nuevo = not os.path.exists(OUT)
    with open(OUT, "a", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        if nuevo: w.writerow(["documento", "tecnologia", "termino", "fragmento"])
        w.writerows(filas)

if __name__ == "__main__":
    path, etiqueta = sys.argv[1], sys.argv[2]
    f = buscar(texto_de(path), etiqueta)
    guardar(f)
    from collections import Counter
    c = Counter(x[1] for x in f)
    print(etiqueta, "| menciones:", len(f)); [print("  ", k, n) for k, n in sorted(c.items())]
