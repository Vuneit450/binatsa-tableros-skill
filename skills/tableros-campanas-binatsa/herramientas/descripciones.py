"""Control "Descripciones: Mostrar / Ocultar" para los tooltips de un libro de Tableau.

Las secciones largas del tooltip (desde la línea divisoria o la primera sección "▸") pasan a cálculos que solo
devuelven su texto cuando el parámetro está en "Mostrar". Se conservan el formato (color, negrita, tamaño) y los
datos dinámicos de arriba. Se agrega un control del parámetro en cada vista que tiene tooltips.

Uso desde otro script:  x = descripciones.agregar(x, colocar="plantilla" | "flotante")
"""
import html, re
from xml.sax.saxutils import escape as _esc

PARAM = "[Parametro Descripciones]"
def esc(s): return _esc(s, {"'": "&apos;", '"': "&quot;"})

def _param(x):
    if PARAM in x: return x
    col = (f"<column caption='Descripciones' datatype='string' name='{PARAM}' param-domain-type='list' role='measure' type='nominal' value='&quot;Mostrar&quot;'>\n"
           "        <calculation class='tableau' formula='&quot;Mostrar&quot;' />\n        <members>\n"
           "          <member value='&quot;Mostrar&quot;' />\n          <member value='&quot;Ocultar&quot;' />\n        </members>\n      </column>")
    m = re.search(r"<datasource hasconnection='false' inline='true' name='Parameters' version='[^']*'>", x)
    if m:
        return x[:m.end()] + "\n      " + col + x[m.end():]
    k = x.index("<datasources>") + len("<datasources>")
    return x[:k] + f"\n    <datasource hasconnection='false' inline='true' name='Parameters' version='18.1'>\n      <aliases enabled='yes' />\n      {col}\n    </datasource>" + x[k:]

def _literal(texto, salto):
    partes = [("'" + p.replace("'", "''") + "'") for p in texto.split("\n")]
    s = " + CHAR(10) + ".join(partes)
    return s + (" + CHAR(10)" if salto else "")

def agregar(x, colocar="flotante"):
    x = _param(x)
    nuevas = {}      # ds -> {texto_formula: nombre}
    defs = {}        # nombre -> (ds, xml de la columna)
    n = [max([0] + [int(v) for v in re.findall(r"name='\[Desc_(\d+)\]'", x)])]

    def calc(ds, formula):
        d = nuevas.setdefault(ds, {})
        if formula in d: return d[formula]
        n[0] += 1; nombre = f"Desc_{n[0]}"; d[formula] = nombre
        defs[nombre] = (ds, f"<column caption='Descripción (tooltip)' datatype='string' name='[{nombre}]' role='measure' type='nominal'>\n"
                            f"        <calculation class='tableau' formula='{esc(formula)}' />\n      </column>")
        return nombre

    def hoja(m):
        w = m.group(0)
        tt = re.search(r"<customized-tooltip[^>]*>.*?</customized-tooltip>", w, re.S)
        dsm = re.search(r"<datasources>\s*(?:<datasource [^>]*name='(?!Parameters')([^']+)'[^>]*/>)", w)
        if not tt or not dsm: return w
        ds = dsm.group(1)
        runs = list(re.finditer(r"<run(?: [^>]*)?>(.*?)</run>", tt.group(0), re.S))
        ini = next((i for i, r in enumerate(runs) if "────" in r.group(1) or html.unescape(r.group(1)).lstrip().startswith("▸")), None)
        if ini is None: return w
        usados, nuevo, salida, pend = [], tt.group(0)[:runs[ini].start()], [], None
        for r in runs[ini:]:
            texto = html.unescape(r.group(1))
            if texto in ("Æ\n", "Æ\r\n"):
                if pend is not None: pend[2] = True
                else: salida.append(r.group(0))
                continue
            if "<![CDATA[" in r.group(1) or texto.startswith("<["):
                if pend is not None: salida.append(pend); pend = None
                salida.append(r.group(0)); continue
            if pend is not None: salida.append(pend)
            attrs = re.match(r"<run((?: [^>]*)?)>", r.group(0)).group(1)
            pend = [attrs, texto.replace("Æ\n", "\n").replace("Æ\r\n", "\n"), False]
        if pend is not None: salida.append(pend)
        partes = []
        for s in salida:
            if isinstance(s, str): partes.append(s); continue
            attrs, texto, salto = s
            if not texto.strip() and not salto: continue
            f = f"IF MIN(1)=1 AND [Parameters].{PARAM}='Mostrar' THEN {_literal(texto, salto)} END"
            nom = calc(ds, f); usados.append(nom)
            partes.append(f"<run{attrs}><![CDATA[<[{ds}].[usr:{nom}:nk]>]]></run>")
        nuevo += "".join(partes) + tt.group(0)[runs[-1].end():]
        w = w[:tt.start()] + nuevo + w[tt.end():]
        usados = list(dict.fromkeys(usados))
        # dependencias de la hoja
        dep = f"<datasource-dependencies datasource='{ds}'>"
        if dep in w:
            add = "".join(f"\n            {defs[u][1]}\n            <column-instance column='[{u}]' derivation='User' name='[usr:{u}:nk]' pivot='key' type='nominal' />" for u in usados)
            w = w.replace(dep, dep + add, 1)
        pdep = "<datasource-dependencies datasource='Parameters'>"
        pcol = re.search(rf"<column caption='Descripciones'[^>]*name='{re.escape(PARAM)}'.*?</column>", x, re.S).group(0)
        if pdep in w:
            if PARAM not in w[w.index(pdep):w.index("</datasource-dependencies>", w.index(pdep))]:
                w = w.replace(pdep, pdep + "\n            " + pcol, 1)
        else:
            w = w.replace(dep, f"{pdep}\n            {pcol}\n          </datasource-dependencies>\n          {dep}", 1)
            if "<datasource name='Parameters' />" not in w:
                w = re.sub(r"(<datasources>)", r"\1\n            <datasource name='Parameters' />", w, count=1)
        # encodings del tooltip
        enc = "".join(f"\n              <tooltip column='[{ds}].[usr:{u}:nk]' />" for u in usados)
        p = w.find("<panes>")
        if p >= 0:
            sub = w[p:]
            ct = re.search(r"<customized-tooltip[^>]*>", sub)
            if "<encodings>" in sub[:ct.start() if ct else len(sub)]:
                sub = sub.replace("<encodings>", "<encodings>" + enc, 1)
            elif ct:
                sub = sub[:ct.start()] + f"<encodings>{enc}\n            </encodings>\n            " + sub[ct.start():]
            w = w[:p] + sub
        return w

    x = re.sub(r"<worksheet name='[^']*'>.*?</worksheet>", hoja, x, flags=re.S)
    # columnas nuevas en cada fuente
    por_ds = {}
    for nom, (ds, xml) in defs.items(): por_ds.setdefault(ds, []).append(xml)
    for ds, cols in por_ds.items():
        i = x.index(f"name='{ds}' version=")
        j = x.index("</connection>", i) + len("</connection>")
        a = x.find("<aliases enabled='yes' />", j, j + 200)
        k = a + len("<aliases enabled='yes' />") if a >= 0 else j
        x = x[:k] + "".join("\n      " + c for c in cols) + x[k:]
    return _controles(x, colocar)

def _en_encabezado(d, nid):
    """Mete el control en la fila de filtros del encabezado, al lado del último filtro. Devuelve d o None."""
    import copy, xml.etree.ElementTree as ET
    zs = d.find("<zones>"); ze = d.find("</zones>", zs)
    if zs < 0 or ze < 0: return None
    frag = d[zs:ze + len("</zones>")]
    try:
        root = ET.fromstring(frag)
    except ET.ParseError:
        return None
    padre = {c: p for p in root.iter() for c in p}
    num = lambda z, k: int(z.get(k, "0"))
    params = [z for z in root.iter("zone") if z.get("type-v2") == "paramctrl" and num(z, "y") < 12000 and "Parametro Descripciones" not in z.get("param", "")]
    if not params: return None
    R = max(params, key=lambda z: num(z, "x") + num(z, "w"))
    textos = [z for z in root.iter("zone") if z.get("type-v2") == "text" and num(z, "y") < 12000 and num(z, "x") + num(z, "w") <= num(R, "x")]
    if not textos: return None
    T = max(textos, key=lambda z: num(z, "w")); A = num(R, "w")
    if num(T, "w") < A + 6000: return None
    def ancestros(z):
        out = []
        while z in padre: z = padre[z]; out.append(z)
        return out
    aR, aT = ancestros(R), ancestros(T)
    Hc = next((a for a in aR if a in aT), None)
    if Hc is None: return None
    C = R if padre.get(R) is Hc else next(a for a in aR if padre.get(a) is Hc)
    t_fin = num(T, "x") + num(T, "w"); c_fin = num(C, "x") + num(C, "w")
    for z in Hc.iter("zone"):
        if z is Hc: continue
        if t_fin <= num(z, "x") < c_fin: z.set("x", str(num(z, "x") - A))
    for z in [T] + [a for a in aT if a is not Hc and a in ancestros(T)][:aT.index(Hc)]:
        z.set("w", str(num(z, "w") - A))
    nuevo = ET.Element("zone", {"h": R.get("h"), "id": str(nid), "mode": "compact", "param": "[Parameters].[Parametro Descripciones]",
                                "type-v2": "paramctrl", "w": str(A), "x": str(c_fin - A), "y": R.get("y")})
    estilo = R.find("zone-style")
    if estilo is not None: nuevo.append(copy.deepcopy(estilo))
    hijos = list(Hc); Hc.insert(hijos.index(C) + 1, nuevo)
    return d[:zs] + ET.tostring(root, encoding="unicode") + d[ze + len("</zones>"):]

def _controles(x, colocar):
    ids = [int(v) for v in re.findall(r"<zone [^>]*id='(\d+)'", x)]
    nid = [max(ids + [0]) + 1000]
    con_tooltip = set(re.findall(r"<worksheet name='([^']*)'>(?:(?!</worksheet>).)*<customized-tooltip", x, re.S))
    def zona(xx, yy, ww, hh, flotante):
        nid[0] += 1
        return (f"<zone h='{hh}' id='{nid[0]}' mode='compact' param='[Parameters].{PARAM}' type-v2='paramctrl' w='{ww}' x='{xx}' y='{yy}'>"
                "<zone-style><format attr='border-style' value='none' /><format attr='margin' value='2' /></zone-style></zone>")
    for dm in list(re.finditer(r"<dashboard [^>]*?name='([^']*)'", x)):
        ini = x.index(dm.group(0)); fin = x.index("</dashboard>", ini); d = x[ini:fin]
        if f"param='[Parameters].{PARAM}'" in d: continue
        principal = d[:d.find("<devicelayouts>")] if "<devicelayouts>" in d else d
        hojas = set(re.findall(r"<zone [^>]*name='([^']*)'", principal))
        if not hojas & con_tooltip: continue
        enc = _en_encabezado(d, nid[0] + 1)
        if enc is not None:
            nid[0] += 1; x = x[:ini] + enc + x[fin:]; continue
        if colocar == "plantilla":
            m = re.search(r"<zone h='(\d+)' id='99\d+' type-v2='text' w='(\d+)' x='(\d+)' y='(\d+)'><formatted-text><run fontcolor='#44546a' fontsize='8'>ℹ️", d)
            if not m: continue
            h, w, xx, yy = (int(v) for v in m.groups()); ancho = 9000
            nuevo = m.group(0).replace(f"w='{w}'", f"w='{w - ancho}'", 1)
            d = d[:m.start()] + nuevo + d[m.end():]
            k = d.index("</zone>", m.start()) + len("</zone>")
            d = d[:k] + "\n" + zona(xx + w - ancho, yy, ancho, h, False) + d[k:]
        else:
            hojas_z = [dict(re.findall(r"(\w[\w-]*)='([^']*)'", z)) for z in re.findall(r"<zone [^>]*type-v2='(?:text|bitmap|paramctrl|filter|dashboard-object|empty)'[^>]*>|<zone [^>]*name='[^']*'[^>]*>", principal)]
            hojas_z = [z for z in hojas_z if all(k in z for k in ("x", "y", "w", "h"))]
            botones = [z for z in hojas_z if z.get("type-v2") == "dashboard-object"]
            if not botones: continue
            fila_y = max(set(int(b["y"]) for b in botones), key=lambda v: sum(1 for b in botones if int(b["y"]) == v))
            fila = [z for z in hojas_z if int(z["y"]) == fila_y and (z.get("type-v2") == "dashboard-object" or (z.get("type-v2") == "text"))]
            a = max(fila, key=lambda z: int(z["x"]) + int(z["w"]))
            xx = max(int(z["x"]) + int(z["w"]) for z in fila if z.get("type-v2") == "dashboard-object")
            ancho = 9000; yy = fila_y; hh = int(botones[0]["h"])
            def choca(x0):
                return any(int(z["y"]) < yy + hh and yy < int(z["y"]) + int(z["h"]) and int(z["x"]) < x0 + ancho and x0 < int(z["x"]) + int(z["w"])
                           and int(z["w"]) < 90000 for z in hojas_z)
            for cand in [xx] + sorted({int(z["x"]) + int(z["w"]) for z in fila}) + [100000 - ancho - 200]:
                if cand + ancho <= 100000 and not choca(cand):
                    xx = cand; break
            else:
                # sin espacio libre en la fila: usar el lado vacío de una caja de texto corta del encabezado
                cortas = []
                for z in re.finditer(r"(<zone [^>]*type-v2='text'[^>]*>)(.*?)</zone>", principal, re.S):
                    at = dict(re.findall(r"(\w[\w-]*)='([^']*)'", z.group(1)))
                    texto = "".join(re.findall(r">([^<]*)</run>", z.group(2))).replace("Æ&#10;", "").strip()
                    if all(k in at for k in ("x", "y", "w", "h")) and int(at["y"]) < 15000:
                        if int(at["w"]) >= ancho + 4000 and len(texto) <= 25: cortas.insert(0, at)        # caja corta: primero
                        elif int(at["w"]) >= 4 * ancho: cortas.append(at)                                  # título ancho: su lado derecho
                if cortas:
                    c = cortas[0]; xx = int(c["x"]) + int(c["w"]) - ancho; yy = int(c["y"]); hh = min(int(c["h"]), 3200)
                else:
                    xx = 100000 - ancho - 200
            a = {"x": xx, "y": yy, "h": hh, "w": ancho}
            k = d.index("</zones>")
            d = d[:k] + zona(a["x"], a["y"], a["w"], a["h"], True) + "\n      " + d[k:]
        x = x[:ini] + d + x[fin:]
    return x
