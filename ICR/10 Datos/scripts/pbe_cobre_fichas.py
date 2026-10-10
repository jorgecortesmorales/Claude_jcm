# -*- coding: utf-8 -*-
"""Preguntas B/E (piloto cobre) — fichas de proceso por operacion, matriz de tecnologias de frontera y razones
de eleccion de proceso. Transcripcion manual de documentos de empresas (Bases Originales/16 y 19), con la cita
que sustenta cada dato. Las menciones automaticas (pbe_frontera_menciones.py) se revisaron a mano para asignar
el estado de cada tecnologia.
Salidas (processed/): cobre_procesos_catalogo.csv, cobre_procesos_operaciones.csv,
                      cobre_frontera_matriz.csv, cobre_procesos_razones.csv
"""
import os, csv

OUT = os.path.join(r"C:\Users\Jorge\OneDrive\Escritorio\Claude CODE\ICR\10 Datos", "processed")
GM = "Grupo México, Informe Anual BMV 2025"
TRS_BV = "SCC, TRS S-K 1300 Buenavista del Cobre (Golder, 2023; datos a 31/12/2022)"
TRS_LC = "SCC, TRS S-K 1300 La Caridad (Golder, 2023; datos a 31/12/2022)"
TRS_TQ = "SCC, TRS S-K 1300 Toquepala (Wood, 2023; datos a 31/12/2022)"
TRS_CJ = "SCC, TRS S-K 1300 Cuajone (Wood, 2023; datos a 31/12/2022)"
TRS_ES = "BHP, TRS S-K 1300 Minera Escondida (FY2022)"
TRS_SA = "Vale, TRS S-K 1300 Salobo (datos a 31/12/2021)"
BO_AI = "Boliden, Mineral Resources and Mineral Reserves Aitik 2025 (PERC)"
BO_KE = "Boliden, Mineral Resources and Mineral Reserves Kevitsa 2025 (PERC)"
BO_AR = "Boliden Mineral AB, Annual Report 2024"
JX = "Jiangxi Copper, informe anual 2025 (HKEX, 27/03/2026)"

def escribir(nombre, cab, filas):
    with open(os.path.join(OUT, nombre), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh); w.writerow(cab); w.writerows(filas)

# --- B1. Catalogo de trabajo de procesos del cobre (a validar con manuales; por fichar) ---
CAT = [
 ("L1 Minado", "Tajo abierto con camión y pala", "Yacimientos cercanos a la superficie (pórfidos)"),
 ("L1 Minado", "Subterráneo por hundimiento de bloques o paneles", "Yacimientos masivos profundos"),
 ("L1 Minado", "Subterráneo por subniveles o corte y relleno", "Cuerpos de menor tamaño o polimetálicos"),
 ("L1 Conminución", "Trituración giratoria y cónica; molienda SAG y de bolas", "Circuito convencional"),
 ("L1 Conminución", "Molienda con rodillos de alta presión (HPGR)", "Alternativa a SAG en mineral duro"),
 ("L1 Conminución", "Molienda vertical o agitada (Vertimill, IsaMill)", "Remolienda fina"),
 ("L1 Concentración", "Flotación en celdas mecánicas; columnas; celdas Jameson", "Sulfuros de cobre y molibdeno"),
 ("L1 Concentración", "Flotación de partícula gruesa", "Recuperación de partículas gruesas; menor energía y agua"),
 ("L2 Hidrometalurgia", "Lixiviación en pilas o botaderos de óxidos y sulfuros secundarios", "Mineral de baja ley"),
 ("L2 Hidrometalurgia", "Biolixiviación o lixiviación de sulfuros primarios", "Calcopirita de baja ley"),
 ("L2 Hidrometalurgia", "Extracción por solventes y electroobtención (ESDE / SX-EW)", "Cátodo a partir de soluciones de lixiviación"),
 ("L2 Pirometalurgia", "Fusión flash", "Fusión de concentrado con aire enriquecido"),
 ("L2 Pirometalurgia", "Fusión en baño (ISASMELT, Teniente, Noranda, Mitsubishi)", "Fusión de concentrado"),
 ("L2 Pirometalurgia", "Conversión Peirce-Smith, Teniente o flash", "Mata a cobre blíster"),
 ("L2 Pirometalurgia", "Plantas de ácido sulfúrico", "Captura del dióxido de azufre"),
 ("L2 Refinación", "Refinación a fuego y electrorrefinación (láminas iniciales o cátodo permanente)", "Ánodo a cátodo"),
 ("L3 Semimanufactura", "Colada continua de alambrón; planchón; laminados", "Cátodo a semimanufactura"),
]
escribir("cobre_procesos_catalogo.csv", ["eslabon", "proceso", "uso", "fuente"],
         [c + ("lista de trabajo; validar con Schlesinger et al., Extractive Metallurgy of Copper, y Wills, Mineral Processing Technology (por fichar)",) for c in CAT])

# --- B2. Ficha por operacion ---
OPS = [
 ("México", "Buenavista del Cobre", "SCC (Grupo México)", "Tajo abierto, camión y pala",
  "Dos concentradoras: 82 000 y 115 000 t de mineral/día", "Plantas ESDE I, II y III (30, 120 y 328 t de cátodo/día); el informe señala dos operativas",
  "Sin fundición propia; el concentrado va a La Caridad (hasta 40.5 % de la producción de las concentradoras) o se exporta por Guaymas", "—", GM + "; " + TRS_BV),
 ("México", "La Caridad", "SCC (Grupo México)", "Tajo abierto, camión y pala",
  "Concentradora de 94 500 t de mineral/día (cobre y molibdeno)", "Planta ESDE de 21 900 t de cátodo/año",
  "Fundición: horno flash, convertidor El Teniente y convertidores convencionales; 1 000 000 t de concentrado/año; dos plantas de ácido",
  "Refinería electrolítica de 300 000 t/año; refinería de metales preciosos; planta de alambrón", GM + "; " + TRS_LC),
 ("Perú", "Toquepala", "SCC (Grupo México)", "Tajo abierto",
  "Dos concentradoras de 60 000 t/día cada una; HPGR en el circuito", "Planta ESDE de 56 336 t de cátodo/año; lixiviación de sulfuros primarios de baja ley (recuperación media de 36 % en 15 años)",
  "Concentrado a la fundición de Ilo", "—", GM + "; " + TRS_TQ),
 ("Perú", "Cuajone", "SCC (Grupo México)", "Tajo abierto, banda transportadora a molienda",
  "Concentradora de 90 000 t/día; HPGR instalados en 2013", "—", "Concentrado a la fundición de Ilo", "—", GM + "; " + TRS_CJ),
 ("Perú", "Ilo (fundición y refinería)", "SCC (Grupo México)", "—", "—", "—",
  "Horno ISASMELT, dos hornos rotatorios de separación, cuatro convertidores Peirce-Smith, dos hornos de ánodos; captura de más de 92 % del azufre; toma de agua de mar y dos desaladoras",
  "Refinería electrolítica con láminas iniciales", GM + "; " + TRS_TQ),
 ("Chile", "Escondida", "BHP (57.5 %)", "Dos tajos abiertos",
  "Tres concentradoras de sulfuros", "Lixiviación ácida de óxidos y mixtos; biolixiviación de sulfuros; planta de cátodos",
  "Sin fundición en el sitio (se exporta concentrado)", "—; dos plantas desaladoras de agua de mar", TRS_ES),
 ("Brasil", "Salobo", "Vale", "Tajo abierto",
  "Tres líneas de 12 Mt/año (36 Mt/año); HPGR en trituración terciaria; Vertimills; columnas de flotación", "—", "Sin fundición en el sitio", "—", TRS_SA),
 ("Suecia", "Aitik", "Boliden", "Tajo abierto; trituradora dentro del tajo con bandas; acarreo autónomo en implementación",
  "Concentradora (no detallada en el informe de recursos)", "—", "Concentrado a la fundición de Rönnskär (Boliden), que también procesa chatarra electrónica", "—", BO_AI + "; " + BO_AR),
 ("Finlandia", "Kevitsa", "Boliden", "Tajo abierto, camión y pala; línea de trolley en la rampa oeste con 13 de 17 camiones con pantógrafo (2023)",
  "Concentradora (no detallada en el informe de recursos)", "—", "—", "—", BO_KE),
 ("China", "Dexing y fundición de Guixi", "Jiangxi Copper", "Tajo abierto (según fuente secundaria)",
  "No detallada en el informe anual", "—", "Guixi: primera línea completa de fusión flash en China, según la empresa", "—", JX),
 ("Australia", "Pendiente", "—", "—", "—", "—", "—", "—", "No se obtuvo un documento técnico comparable (Olympic Dam, BHP)"),
]
escribir("cobre_procesos_operaciones.csv",
         ["pais", "operacion", "empresa", "minado", "concentracion", "hidrometalurgia", "fundicion", "refinacion_y_otros", "fuente"], OPS)

# --- B4. Matriz de tecnologias de frontera (estado verificado a mano) ---
A, P, G, NA, SE = "adoptada", "en implementación, proyecto o estudio", "mención genérica", "no aplica", "sin evidencia en los documentos revisados"
MAT = [
 ("México", "La Caridad", "T12 Fusión o conversión flash", A, "«horno flash, el convertidor El Teniente y los convertidores convencionales»", GM),
 ("México", "La Caridad", "T14 Captura de azufre en fundición", A, "gases de SO2 del horno flash y convertidores «se procesan en ácido sulfúrico en dos plantas»", GM),
 ("México", "La Caridad", "T09 Relaves filtrados o espesados", P, "Golder recomienda un estudio comparativo; «filtered tailings appear to be an attractive option due to the site conditions»", TRS_LC),
 ("México", "La Caridad", "T08 Celdas Jameson (en ESDE)", G, "celdas Jameson usadas para limpiar el electrolito de la planta ESDE, no en la flotación de mineral", TRS_LC),
 ("México", "Buenavista del Cobre", "Todas", SE, "el TRS disponible (63 pp.) no menciona ninguna de las 15 tecnologías", TRS_BV),
 ("Perú", "Toquepala", "T05 HPGR", A, "producto de las trituradoras «transported to a HPGR surge bin»", TRS_TQ),
 ("Perú", "Toquepala", "T11 Lixiviación de sulfuros primarios", A, "«low-grade primary sulfide leaching has averaged a copper recovery of about 36% over the last 15 years»", TRS_TQ),
 ("Perú", "Toquepala", "T09 Relaves filtrados o espesados", P, "planta de relaves filtrados y depósito en seco considerados en el plan y en el costo de cierre", TRS_TQ),
 ("Perú", "Cuajone", "T05 HPGR", A, "«2013 Installation of high-pressure grind rolls (HPGR) in the concentrator»", TRS_CJ),
 ("Perú", "Cuajone", "T09 Relaves filtrados o espesados", P, "planta de relaves filtrados y planta piloto incluidas en el capital de sostenimiento", TRS_CJ),
 ("Perú", "Ilo", "T10 Agua de mar o desalinizada", A, "«a seawater intake system, two desalination plants to provide water for the process»", TRS_TQ),
 ("Perú", "Ilo", "T14 Captura de azufre en fundición", A, "recaptura de dióxido de azufre «a más de 92%» desde 2007", GM),
 ("Chile", "Escondida", "T10 Agua de mar o desalinizada", A, "«two seawater desalination plants»", TRS_ES),
 ("Chile", "Escondida", "T11 Biolixiviación de sulfuros", A, "«Acid Bioleaching of Sulphide Mineralisation»; ley de corte para el proceso de biolixiviación", TRS_ES),
 ("Chile", "Escondida", "T13 IA", G, "intención de formar capacidades en IA y autonomía con universidades", TRS_ES),
 ("Brasil", "Salobo", "T05 HPGR", A, "«HPGR were retained instead of SAG mills»", TRS_SA),
 ("Brasil", "Salobo", "T08 Molienda vertical", A, "«3 Vertimills: 1,500 hp»", TRS_SA),
 ("Suecia", "Aitik", "T04 Trituración en el tajo y bandas", A, "«Ore handled by the in-pit crusher is transported on conveyor belts»", BO_AI),
 ("Suecia", "Aitik", "T01 Acarreo autónomo", P, "«in Aitik the implementation of autonomous hauling systems is underway»", BO_AR),
 ("Suecia", "Rönnskär (fundición)", "T15 Reciclaje de material secundario", A, "«Rönnskär is a world leader in the recycling of electronics»", BO_AR),
 ("Finlandia", "Kevitsa", "T02 Acarreo electrificado (trolley)", A, "«Trolley line built on the west ramp in 2023 is in use with 13 trucks out of 17»", BO_KE),
 ("China", "Guixi", "T12 Fusión flash", A, "«the first entity to introduce the entire flash smelting technology production line in the PRC»", JX),
 ("China", "Jiangxi Copper", "T13 IA", P, "iniciativa «Artificial Intelligence +» en minas, fundición y gestión", JX),
]
escribir("cobre_frontera_matriz.csv", ["pais", "operacion", "tecnologia", "estado", "evidencia", "fuente"], MAT)

# --- B3. Razones de eleccion de proceso declaradas en los documentos ---
RAZ = [
 ("México", "La Caridad", "Minado a tajo abierto", "Características del yacimiento", "«due to the proximity of the ore to the surface and the physical characteristics of the deposit»", TRS_LC),
 ("México", "Buenavista del Cobre", "Minado a tajo abierto", "Características del yacimiento", "«due to the proximity of the ore to the surface and the physical characteristics of the deposit»", TRS_BV),
 ("México", "La Caridad", "Molienda y flotación convencional", "Mineralogía; tecnología disponible", "seleccionada para la calcocita, «the best available technology at the time»", TRS_LC),
 ("México", "La Caridad", "ESDE", "Ley del mineral", "«best available process to recover copper from low concentration solutions resulting from leaching low-grade ore»", TRS_LC),
 ("México", "La Caridad", "Concentradora o pila de lixiviación", "Ley del mineral", "mineral con ley mayor a 0.30 % a la concentradora; entre 0.15 % y 0.30 % a lixiviación", GM),
 ("México", "Buenavista del Cobre", "Dos concentradoras distintas", "Antigüedad del equipo", "la segunda concentradora «was designed and built with modern equipment 30 years after Concentrator 1»", TRS_BV),
 ("México", "La Caridad", "Relaves filtrados (recomendación)", "Condiciones del sitio", "«Filtered tailings appear to be an attractive option due to the site conditions»", TRS_LC),
 ("Perú", "Toquepala", "Concentradora o lixiviación", "Ley del mineral", "el material bajo la ley de corte se envía a lixiviación si supera la ley de corte de ese proceso", TRS_TQ),
 ("Chile", "Escondida", "Concentradora para sulfuros", "Economía del plan minero", "«optimised mine plan with consideration of technical and economic parameters in order to maximise net present value»", TRS_ES),
 ("Chile", "Escondida", "Mineral mixto a lixiviación ácida", "Disponibilidad de mineral", "«because of lower availability of oxides at the mine plans»", TRS_ES),
 ("Brasil", "Salobo", "HPGR en lugar de molienda SAG", "Mineralogía", "por el alto contenido de magnetita y cobre de los guijarros de tamaño crítico", TRS_SA),
]
escribir("cobre_procesos_razones.csv", ["pais", "operacion", "decision", "categoria_de_razon", "cita", "fuente"], RAZ)
print("ok:", len(CAT), len(OPS), len(MAT), len(RAZ))
