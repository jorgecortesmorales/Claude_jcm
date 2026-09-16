#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Preprocesador + compilador del manuscrito ICR.
- Numera cuadros y figuras por capitulo (Cuadro III.2, Ilustracion III.1).
- Resuelve referencias cruzadas {{cua:label}} / {{fig:label}}.
- Genera indice de cuadros {{LISTA_CUADROS}} y de ilustraciones {{LISTA_FIGURAS}}.
- Llama a pandoc con reference.docx institucional, APA (citeproc+CSL) y TOC.

Convenciones de autoria en el Markdown fuente:
  Tabla:   (linea de pie, tras la tabla, separada por linea en blanco)
           Cuadro {#cua:LABEL}: Titulo. Fuente: ...
  Figura:  ![Ilustracion {#fig:LABEL}: Titulo. Fuente: ...](figuras/x.png){width=...}
  Ref.:    {{cua:LABEL}}  ->  "Cuadro III.2"
           {{fig:LABEL}}  ->  "Ilustracion III.1"
  Indices: {{LISTA_CUADROS}} / {{LISTA_FIGURAS}}

Uso:  py build.py  manuscrito/03-metodologia.md  ../<salida>.docx
"""
import sys, os, re, subprocess, tempfile

PANDOC = os.environ.get("PANDOC_BIN",
    r"C:\Users\Jorge\AppData\Local\Pandoc\pandoc.exe")
HERE = os.path.dirname(os.path.abspath(__file__))
REDACCION = os.path.dirname(HERE)          # 11 Redaccion

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return "", text
    return m.group(1), m.group(2)

def meta_get(front, key, default=None):
    m = re.search(rf"^{key}:\s*[\"']?(.+?)[\"']?\s*$", front, re.M)
    return m.group(1) if m else default

def preprocess(body, chap):
    """Devuelve (body_procesado, cuadros, figuras) con numeracion resuelta."""
    cua_map, fig_map = {}, {}   # label -> "III.2"
    cua_list, fig_list = [], [] # (num, titulo_plano)
    counters = {"cua": 0, "fig": 0}

    def plain(s):
        s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
        s = re.sub(r"\*(.+?)\*", r"\1", s)
        return s.strip()

    # --- PASS 1a: figuras (dentro de ![...]) ---
    def fig_sub(m):
        label, titulo = m.group(1), m.group(2)
        counters["fig"] += 1
        num = f"{chap}.{counters['fig']}"
        fig_map[label] = num
        fig_list.append((num, plain(titulo)))
        return f"![**Ilustración {num}.** {titulo}"
    body = re.sub(r"!\[Ilustración \{#fig:([\w-]+)\}:\s*(.*?)(?=\]\()",
                  fig_sub, body)

    # --- PASS 1b: cuadros (linea de pie) ---
    def cua_sub(m):
        label, titulo = m.group(1), m.group(2)
        counters["cua"] += 1
        num = f"{chap}.{counters['cua']}"
        cua_map[label] = num
        cua_list.append((num, plain(titulo)))
        return f": **Cuadro {num}.** {titulo}"
    body = re.sub(r"^Cuadro \{#cua:([\w-]+)\}:\s*(.*)$",
                  cua_sub, body, flags=re.M)

    # --- PASS 2: referencias cruzadas ---
    def ref_sub(m):
        kind, label = m.group(1), m.group(2)
        if kind == "cua":
            n = cua_map.get(label)
            return f"Cuadro {n}" if n else f"Cuadro ??{label}"
        n = fig_map.get(label)
        return f"Ilustración {n}" if n else f"Ilustración ??{label}"
    body = re.sub(r"\{\{(cua|fig):([\w-]+)\}\}", ref_sub, body)

    # --- indices generados ---
    def render_list(items, kind):
        if not items:
            return f"*(sin {kind})*"
        out = []
        for num, tit in items:
            pre = "Cuadro" if kind == "cuadros" else "Ilustración"
            out.append(f"{pre} {num}. {tit}")
        return "\n\n".join(out)
    body = body.replace("{{LISTA_CUADROS}}", render_list(cua_list, "cuadros"))
    body = body.replace("{{LISTA_FIGURAS}}", render_list(fig_list, "ilustraciones"))

    return body, cua_list, fig_list

def main():
    if len(sys.argv) < 3:
        print("uso: py build.py <entrada.md> <salida.docx>"); sys.exit(1)
    src, out = sys.argv[1], sys.argv[2]
    text = read(src)
    front, body = split_front_matter(text)
    chap = meta_get(front, "chapter", "X")
    body_p, cua, fig = preprocess(body, chap)

    # reconstruir con front matter (para title/lang) + cuerpo procesado
    processed = f"---\n{front}\n---\n{body_p}"
    tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                      encoding="utf-8", dir=REDACCION)
    tmp.write(processed); tmp.close()

    cmd = [PANDOC, os.path.basename(tmp.name), "-o", out,
           "--reference-doc", os.path.join("pandoc", "reference.docx"),
           "--toc", "--toc-depth=3",
           "--citeproc",
           "--csl", os.path.join("pandoc", "apa.csl"),
           "--bibliography", os.path.join("pandoc", "references.bib"),
           "-M", "lang=es-ES",
           "--resource-path", REDACCION,
           "-f", "markdown+pipe_tables+table_captions+implicit_figures"]
    try:
        r = subprocess.run(cmd, cwd=REDACCION, capture_output=True, text=True)
        sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
        code = r.returncode
    finally:
        os.unlink(tmp.name)
    print(f"\n[build] capitulo {chap}: {len(cua)} cuadros, {len(fig)} figuras -> {out}")
    sys.exit(code)

if __name__ == "__main__":
    main()
