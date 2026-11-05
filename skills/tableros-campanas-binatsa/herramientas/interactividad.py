"""Aplica a un libro existente (.twbx) la interactividad estándar de BINATSA:

1. Resaltar al pasar el mouse: una sola acción por vista, por su campo de categoría principal.
   Quedan fuera las tarjetas KPI y las hojas que no muestran ese campo (si no, se apagarían).
2. Periodo arranca en "Personalizado".
3. Control "💬 Descripciones" (Mostrar / Ocultar) en la fila de filtros del encabezado
   (ver herramientas/descripciones.py y referencias/tooltips.md).

Uso:
    python interactividad.py libro_v1.twbx libro_v2.twbx --plan '{"Dirección": "Canal", "Operación": "Asesor"}'
    python interactividad.py ... --tarjetas '^(KPI |Tarjeta )'
    python interactividad.py ... --solo-resaltar     (solo el punto 1)

--plan: vista → campo de categoría preferido (nombre visible). Las hojas se agrupan por el campo
        que comparten; cada grupo lleva su propia acción (orígenes sin encimarse) y una hoja que
        no comparte categoría con otra se resalta dentro de sí misma.
--tarjetas: expresión regular con el nombre de las hojas de tarjetas KPI de ese libro.
Trabaja sobre una copia: nunca sobrescribe el libro de entrada.
"""
import argparse, html, importlib.util, json, pathlib, re, sys, uuid, zipfile


def personalizado(x):
    """Deja el parámetro Periodo en 'Personalizado' (en la definición y en las copias de cada hoja)."""
    def r(m):
        c = re.sub(r"value='&quot;[^']*&quot;'", "value='&quot;Personalizado&quot;'", m.group(1), count=1)
        return c + re.sub(r"formula='&quot;[^']*&quot;'", "formula='&quot;Personalizado&quot;'", m.group(2), count=1)
    return re.subn(r"(<column caption='Periodo' datatype='string' name='\[[^\]]+\]' param-domain-type='list'[^>]*>)"
                   r"(\s*<calculation class='tableau' formula='[^']*' />)", r, x)


def mapa_captions(x):
    cap = {}
    for m in re.finditer(r"<column (?:caption='([^']*)' )?datatype='\w+'[^>]*name='\[([^\]]+)\]'", x):
        if m.group(1):
            cap.setdefault(m.group(2), html.unescape(m.group(1)))
    return cap


def hojas_sin_campo(x, hojas, campo, cap):
    """Hojas de la vista que no muestran el campo (por su nombre visible)."""
    fuera = []
    for h in hojas:
        i = x.find(f"<worksheet name='{h}'")
        if i < 0:
            continue
        w = x[i:x.index('</worksheet>', i)]
        vista = (w[w.find('<panes>'):] if '<panes>' in w else '') + ''.join(re.findall(r"<(?:rows|cols)>(.*?)</(?:rows|cols)>", w, re.S))
        campos = set(re.findall(r"\[(?:none|tdy|hr|wd|usr|attr):([^:\]]+):[no]k\]", vista))
        if not any(cap.get(c, c) == campo for c in campos):
            fuera.append(h)
    return fuera


NO_CATEGORIA = re.compile(r"(?i)métrica|metrica|medida|measure|kpi|selector|texto")


def campos_de(x, h, cap):
    """Campos de categoría (nombre visible) que muestra una hoja."""
    i = x.find(f"<worksheet name='{h}'")
    if i < 0:
        return []
    w = x[i:x.index('</worksheet>', i)]
    vista = (w[w.find('<panes>'):] if '<panes>' in w else '') + ''.join(re.findall(r"<(?:rows|cols)>(.*?)</(?:rows|cols)>", w, re.S))
    out = []
    for c in re.findall(r"\[(?:none|attr|usr|wd|hr|dy|mn|tdy):([^:\]]+):[no]k\]", vista):
        n = cap.get(c, c)
        if n not in out and not NO_CATEGORIA.search(n):
            out.append(n)
    return out


def grupos(x, hs, preferido, cap, tarj):
    """Agrupa las hojas de una vista por el campo de categoría que comparten.
    Cada hoja va al grupo de su campo más compartido (el preferido gana los empates);
    una hoja que no comparte con nadie queda sola y se resalta dentro de sí misma.
    Devuelve {campo: [hojas]} sin tarjetas ni hojas sin categoría."""
    cs = {h: campos_de(x, h, cap) for h in hs if h not in tarj}
    cuenta = {}
    for f in (f for v in cs.values() for f in v):
        cuenta[f] = cuenta.get(f, 0) + 1
    g = {}
    for h, fs in cs.items():
        if not fs:
            continue
        f = max(fs, key=lambda f: (cuenta[f], f == preferido, -fs.index(f)))
        g.setdefault(f, []).append(h)
    return g


def hojas_de(x, dash):
    m = re.search(rf"<dashboard [^>]*?name='{re.escape(dash)}'.*?</dashboard>", x, re.S)
    if not m:
        sys.exit(f"No encontré la vista '{dash}' en el libro.")
    d = m.group(0)
    d = d[:d.find('<devicelayouts>')] if '<devicelayouts>' in d else d
    return [h for h in dict.fromkeys(re.findall(r"<zone [^>]*name='([^']*)'", d)) if f"<worksheet name='{h}'" in x]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("libro"); ap.add_argument("salida")
    ap.add_argument("--plan", required=True, help="JSON: vista → campo de categoría")
    ap.add_argument("--tarjetas", default=r"^(KPI |Tarjeta )", help="regex de las hojas de tarjetas KPI")
    ap.add_argument("--solo-resaltar", action="store_true", help="no tocar Periodo ni agregar el control Descripciones")
    a = ap.parse_args()
    if pathlib.Path(a.libro).resolve() == pathlib.Path(a.salida).resolve():
        sys.exit("La salida debe ser otro archivo (versión nueva).")
    plan, tarj_re = json.loads(a.plan), re.compile(a.tarjetas)

    z = zipfile.ZipFile(a.libro); twb = [n for n in z.namelist() if n.endswith('.twb')][0]
    raw = z.read(twb).decode('utf-8'); nl = '\r\n' if '\r\n' in raw else '\n'
    x = raw.replace('\r\n', '\n') if nl == '\r\n' else raw
    nl = '\n'

    x, n_per = (x, 0) if a.solo_resaltar else personalizado(x)
    # Se quitan las acciones de resaltar al pasar el mouse que ya existan: varias por vista se anulan entre sí.
    x = re.sub(r"\s*<action [^>]*>\s*<activation auto-clear='true' type='on-hover' />.*?</action>", "", x, flags=re.S)
    cap, acc = mapa_captions(x), []
    for dash, campo in plan.items():
        hs = hojas_de(x, dash)
        tarj = [h for h in hs if tarj_re.search(html.unescape(h))]
        # Una acción por grupo de hojas que comparten categoría. Los orígenes no se enciman
        # (cada hoja dispara una sola acción), así no se anulan entre sí.
        gs = grupos(x, hs, campo, cap, tarj)
        for f, miembros in sorted(gs.items(), key=lambda kv: -len(kv[1])):
            fuera = [h for h in hs if h not in miembros]
            g = uuid.uuid4().hex.upper()
            b = [f"    <action caption='Resaltar al pasar el mouse ({dash} · {f})' name='[Action{90000 + len(acc)}_{g}]'>",
                 "      <activation auto-clear='true' type='on-hover' />"]
            if fuera:
                b.append(f"      <source dashboard='{dash}' type='sheet'>")
                b += [f"        <exclude-sheet name='{h}' />" for h in fuera]
                b.append("      </source>")
            else:
                b.append(f"      <source dashboard='{dash}' type='sheet' />")
            b.append("      <command command='tsc:brush'>")
            if fuera:
                b.append(f"        <param name='exclude' value='{','.join(fuera)}' />")
            b += [f"        <param name='field-captions' value='{f}' />", f"        <param name='target' value='{dash}' />",
                  "      </command>", "    </action>"]
            acc.append(nl.join(b))
            print(f"  {html.unescape(dash)} · {f}: {', '.join(html.unescape(h) for h in miembros)}")
        sin = [h for h in hs if h not in tarj and not any(h in m for m in gs.values())]
        if sin:
            print(f"  {html.unescape(dash)} · sin categoría (no resaltan): {', '.join(html.unescape(h) for h in sin)}")

    sp = importlib.util.spec_from_file_location("descripciones", pathlib.Path(__file__).with_name("descripciones.py"))
    de = importlib.util.module_from_spec(sp); sp.loader.exec_module(de)
    if not a.solo_resaltar:
        x = de.agregar(x, colocar="flotante")

    if '</actions>' in x:
        k = x.rindex('</actions>'); x = x[:k] + nl.join(acc) + nl + '  ' + x[k:]
    else:
        k = x.index('<worksheets>'); x = x[:k] + '<actions>' + nl + nl.join(acc) + nl + '  </actions>' + nl + '  ' + x[k:]
    with zipfile.ZipFile(a.salida, 'w', zipfile.ZIP_DEFLATED) as zo:
        for it in z.infolist():
            zo.writestr(it, x.encode('utf-8') if it.filename == twb else z.read(it.filename))
    print(f"{pathlib.Path(a.salida).name}: {len(acc)} acciones de resaltar | Periodo → Personalizado en {n_per} lugares | control Descripciones: {'no' if a.solo_resaltar else 'agregado'}")


if __name__ == "__main__":
    main()
