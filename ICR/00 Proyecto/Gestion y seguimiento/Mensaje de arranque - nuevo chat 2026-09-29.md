---
title: "Mensaje de arranque — nuevo chat 2026-09-29"
type: handoff
tags: [icr, handoff, arranque]
created: 2026-09-29
updated: 2026-09-29
status: reemplazado
---

# Mensaje de arranque — nuevo chat

Copia y pega el bloque en un chat nuevo de Claude Code (directorio de trabajo: `C:\Users\Jorge\OneDrive\Escritorio\Claude CODE`).

```text
Continúo mi tesis ICR sobre los mercados de los minerales críticos en México (proyecto en ICR/; no confundir con ICR DIANA/).

1. Lee primero el handoff vigente:
   "ICR/00 Proyecto/Gestion y seguimiento/Handoff - Estado actual (HEM, consolidado y certificacion) 2026-09-29.md"
   y después ICR/CLAUDE.md.

2. Respeta estas reglas (están en el handoff):
   - Trabaja solo dentro de ICR/, usa `py` y las skills de Obsidian para los .md.
   - Diseño descriptivo. Mi pauta de redacción: la interpretación de resultados es SOLO descriptiva
     (describir y analizar resultados, sin implicaciones ni búsqueda de relaciones). Excepción: los dos
     coeficientes de Ghosh (Rasmussen = intensidad, HEM = peso) se interpretan por separado y en conjunto.
   - Estilo matemático del Cap. III: el de Morales-López (2023) — ecuaciones numeradas con
     `\qquad\qquad (n)` y glosario "donde X es … de orden n×1".
   - Referencias cruzadas: `{{cua:X}}` y `{{fig:X}}` solos, nunca "Cuadro {{cua:X}}".
   - No aceptes el control de cambios del PROTOCOLO (espera al asesor).
   - Sin voz de IA; todo cambio versionado en git; haz handoff antes de agotar contexto.
   - Tras cualquier cambio al manuscrito o a los datos: recompila (py pandoc/build_book.py y
     py pandoc/update_pdf.py desde "ICR/11 Redaccion") y vuelve a correr el cotejo de certificación
     (13 Entregables/Consolidado datos y calculos/cotejo_certificacion.py), que debe dar 0 difieren.

3. Confírmame en pocas líneas el estado actual y los pendientes del handoff (§3), y dime por dónde
   sugieres seguir. No modifiques nada todavía.
```

← [[Handoff - Estado actual (HEM, consolidado y certificacion) 2026-09-29]] · [[Bitacora]]
