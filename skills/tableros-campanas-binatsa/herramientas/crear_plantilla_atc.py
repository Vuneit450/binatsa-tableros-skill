#!/usr/bin/env python3
"""Crea la Plantilla BINATSA de ATC a partir de la Plantilla de Cobranza (que ya tiene el estilo probado).

Conserva el diseño, las acciones y los nombres internos de los cálculos; cambia los datos (llamadas entrantes
inventadas), las fórmulas, los formatos, los títulos, los tooltips y la Guía y glosario.

Uso:
  python crear_plantilla_atc.py plantillas/plantilla_cobranza_binatsa.twbx plantillas/
"""
import csv, datetime as dt, html, io, pathlib, random, re, sys, zipfile
from xml.sax.saxutils import escape as _esc

def esc(s): return _esc(s, {"'": "&apos;", '"': "&quot;"})

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
zin = zipfile.ZipFile(src)
x = zin.read([n for n in zin.namelist() if n.endswith('.twb')][0]).decode('utf-8').replace('\r\n', '\n')
DSR = "federated.0rvlq4v1w8nh7n18mx6q00cg2562"   # resumen diario por asesor
DSL = "federated.0spjcqc1j6imwg1gq7cjt1s5sxd7"   # detalle de llamadas
random.seed(2027)
HOY = dt.date.today()

# ================= 1. Datos inventados =================
NOMBRES = ["Laura Méndez Ruiz", "Carlos Ortega Salinas", "Daniela Prieto Lara", "Jorge Valdez Moreno",
           "Mariana Cruz Ibarra", "Ricardo Fuentes Ávila", "Paola Estrada Núñez", "Luis Herrera Campos",
           "Andrea Robles Mejía", "Fernando Zamora Ríos", "Sofía Castañeda Vela", "Miguel Ángel Solís Durán",
           "Valeria Bautista Peña", "Héctor Medina Lozano", "Gabriela Rangel Torres"]
LOGINS = [f"asesor.{i:02d}" for i in range(1, 16)]
GRUPOS = ["G_C1_A"] * 5 + ["G_C2_A"] * 5 + ["G_C3_A"] * 5
NUEVAS = {"recibidas_dia": "integer", "atendidas_dia": "integer", "abandonadas_dia": "integer",
          "abandonadas_5s_dia": "integer", "demoradas_20s_dia": "integer", "en_nivel_dia": "integer",
          "espera_seg_dia": "real", "tmo_seg_dia": "real", "tipificadas_dia": "integer",
          "horas_disponible_dia": "real", "horas_aux_dia": "real", "horas_conectado_dia": "real", "dia_asesor": "integer"}

def dias(n):
    d = HOY - dt.timedelta(days=n)
    while d < HOY:
        if d.weekday() != 6:
            yield d
        d += dt.timedelta(days=1)

# columnas que ya existen en la fuente (se conservan en cero para no romper cálculos que no se usan)
viejas = re.findall(r"<column datatype='(\w+)' name='([^']+)' ordinal='\d+' />",
                    x[x.index("<relation connection='textscan.resumen'"):x.index("</relation>", x.index("<relation connection='textscan.resumen'"))])
fil = []
for d in dias(120):
    sab = d.weekday() == 5
    for lg, gr in zip(LOGINS, GRUPOS):
        if random.random() < 0.05:
            continue
        rec = int(random.randint(60, 110) * (0.5 if sab else 1))
        aban = int(rec * random.uniform(0.02, 0.12)); aban5 = int(aban * random.uniform(0.5, 0.9))
        ate = rec - aban; dem = int(ate * random.uniform(0.02, 0.16))
        fila = {c: ("0" if t != "string" else "") for t, c in viejas}
        fila.update({"agente": lg, "grupo": gr, "rol": "Asesor", "fecha_ingreso_agente": "2025-06-01",
                     "fecha": d.isoformat(), "fecha_dt": d.isoformat(),
                     "recibidas_dia": rec, "atendidas_dia": ate, "abandonadas_dia": aban, "abandonadas_5s_dia": aban5,
                     "demoradas_20s_dia": dem, "en_nivel_dia": ate - dem,
                     "espera_seg_dia": round(ate * random.uniform(8, 26), 1),
                     "tmo_seg_dia": round(ate * random.uniform(360, 640), 1),
                     "tipificadas_dia": int(ate * random.uniform(0.85, 1.0)),
                     "horas_disponible_dia": round(random.uniform(2.5, 4) * (0.5 if sab else 1), 2),
                     "horas_aux_dia": round(random.uniform(0.6, 1.6) * (0.5 if sab else 1), 2),
                     "horas_conectado_dia": round((4.5 if sab else 8) + random.uniform(-0.5, 0.5), 2), "dia_asesor": 1})
        fil.append(fila)
cols_r = [c for _, c in viejas] + list(NUEVAS)
b = io.StringIO(); w = csv.DictWriter(b, fieldnames=cols_r, lineterminator="\n"); w.writeheader(); w.writerows(fil)
csv_res = b.getvalue().encode("utf-8")

TIPIF = [("Aclaración de cargo", 18), ("Estado de cuenta", 16), ("Información general", 15), ("Alta de servicio", 9),
         ("Cambio de datos", 9), ("Queja", 7), ("Cancelación", 6), ("Atendida sin tipificar", 5), ("Abandonada", 8)]
cols_l = re.findall(r"<column datatype='\w+' name='([^']+)' ordinal='\d+' />",
                    x[x.index("<relation connection='textscan.llamadas'"):x.index("</relation>", x.index("<relation connection='textscan.llamadas'"))])
fl, n = [], 0
t_, p_ = zip(*TIPIF)
for d in dias(30):
    for _ in range(random.randint(900, 1300) // (2 if d.weekday() == 5 else 1)):
        n += 1
        h = random.choices(range(8, 21), weights=[4, 8, 10, 10, 9, 8, 7, 8, 9, 8, 6, 4, 2])[0]
        t0 = dt.datetime.combine(d, dt.time(h, random.randint(0, 29) * 2, random.randint(0, 59)))
        r = random.choices(t_, p_)[0]; i = random.randrange(15)
        fmt = lambda t: t.strftime("%Y-%m-%d %H:%M:%S")
        espera = random.randint(2, 90)
        fila = {c: "" for c in cols_l}
        fila.update({"llamada_id": f"L{n:07d}", "nombre_tarea": "Entrante", "nombre_tarea_flujo": "Flujo 1",
                     "tarea_id": GRUPOS[i], "numero_principal": 5500000000 + n, "numero_marcado": 5500000000 + n,
                     "nombre_contacto": f"Cliente {n:06d}", "tipo_llamada": "Entrante", "fecha_marcado": fmt(t0),
                     "fecha_fin": fmt(t0 + dt.timedelta(seconds=espera + 300)), "tiempo_espera": espera,
                     "tiempo_conversacion": 0 if r == "Abandonada" else random.randint(120, 720),
                     "tiempo_facturable": 0, "tiempo_retencion": 0, "rondas_marcacion": 1,
                     "resultado_llamada": r, "nombre_grupo": GRUPOS[i], "agente": "" if r == "Abandonada" else LOGINS[i]})
        fl.append(fila)
b = io.StringIO(); w = csv.DictWriter(b, fieldnames=cols_l, lineterminator="\n"); w.writeheader(); w.writerows(fl)
csv_lla = b.getvalue().encode("utf-8")

# nuevas columnas en la fuente: definición del CSV y registros de metadatos
rel_i = x.index("<relation connection='textscan.resumen'"); rel_f = x.index("</columns>", rel_i)
n0 = len(viejas)
extra = "".join(f"\n            <column datatype='{t}' name='{c}' ordinal='{n0 + k}' />" for k, (c, t) in enumerate(NUEVAS.items()))
x = x[:rel_f] + extra.lstrip("\n") + "\n          " + x[rel_f:]
mi = x.index("<metadata-records>", x.index(f"name='{DSR}' version=")); mf = x.index("</metadata-records>", mi)
oid = re.search(r"<object-id>([^<]*)</object-id>", x[mi:mf]).group(1)
md = "".join(f"""
          <metadata-record class='column'>
            <remote-name>{c}</remote-name>
            <remote-type>{'20' if t == 'integer' else '5'}</remote-type>
            <local-name>[{c}]</local-name>
            <parent-name>[resumen_diario.csv]</parent-name>
            <remote-alias>{c}</remote-alias>
            <ordinal>{n0 + k}</ordinal>
            <local-type>{t}</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
            <object-id>{oid}</object-id>
          </metadata-record>""" for k, (c, t) in enumerate(NUEVAS.items()))
x = x[:mf] + md.lstrip("\n") + "\n        " + x[mf:]

# ================= 2. Fórmulas =================
FILT = "([Parameters].[Parameter 8]='Todos' OR [Calc_Canal]=[Parameters].[Parameter 8])"
CUR = f"[fecha_dt]>=[Desde_E] AND [fecha_dt]<=[Hasta_E] AND {FILT}"
PRE = f"[fecha_dt]>=DATEADD('day',-(DATEDIFF('day',[Desde_E],[Hasta_E])+1),[Desde_E]) AND [fecha_dt]<[Desde_E] AND {FILT}"
SEV = f"[fecha_dt]>=DATEADD('day',-7,[Desde_E]) AND [fecha_dt]<=DATEADD('day',-7,[Hasta_E]) AND {FILT}"
SIETE = "DATEDIFF('day',[Desde_E],[Hasta_E])+1>7"
FMT = {"n": "n#,##0", "p": "p0.0%", "s": 'n#,##0" s"', "m": 'n#,##0.0" min"', "r": "n#,##0.0", "h": 'n#,##0.0" h"'}
TXT = {"n": "#,##0", "p": "0.0%", "s": '#,##0" s"', "m": '#,##0.0" min"', "r": "#,##0.0", "h": '#,##0.0" h"'}

def agg(f, c):
    k = f["kind"]
    if k == "sum": return f"SUM(IF {c} THEN [{f['num']}] END)"
    if k == "countd": return f"COUNTD(IF {c} THEN [agente] END)"
    num, den, esc_ = f"SUM(IF {c} THEN [{f['num']}] END)", f"SUM(IF {c} THEN [{f['den']}] END)", f.get("scale", "")
    return f"IF {den}>0 THEN {num}/{den}{esc_} END"

def deltas(fam, pct, inv):
    out = {}
    for s in "ps":
        v, r = f"[K_{fam}_v]", f"[K_{fam}_{s}]"
        d = f"({v}-{r})*100" if pct else f"({v}-{r})/ABS({r})*100"
        g = f"NOT ISNULL({v}) AND NOT ISNULL({r})" + ("" if pct else f" AND {r}<>0")
        u = " pp" if pct else "%"
        txt = f"(IF {d}>=0 THEN '▲ +' ELSE '▼ ' END)+STR(ROUND({d},1))+'{u}'"
        mej, emp = (f"{d}<=-0.05", f"{d}>=0.05") if inv else (f"{d}>=0.05", f"{d}<=-0.05")
        f_g, f_r = f"IF {g} AND {mej} THEN {txt} END", f"IF {g} AND {emp} THEN {txt} END"
        f_n = f"IF NOT ({g}) THEN '-' ELSEIF ABS({d})<0.05 THEN '0.0{u}' END"
        if s == "s":
            f_g, f_r, f_n = (f"IF {SIETE} THEN ({q}) END" for q in (f_g, f_r, f_n))
        out[s + "g"], out[s + "r"], out[s + "n"] = f_g, f_r, f_n
    return out

# familias: nombre interno -> métrica de ATC
F = {
 "Pago":  dict(t="Recibidas", e="📞", sub="Llamadas que entraron", kind="sum", num="recibidas_dia", f="n", inv=False,
               q="Llamadas únicas que entraron: atendidas + abandonadas.", c="Suma de llamadas recibidas en el rango."),
 "Tasa":  dict(t="Atendidas", e="🎧", sub="Contestadas por un asesor", kind="sum", num="atendidas_dia", f="n", inv=False,
               q="Llamadas contestadas por un asesor.", c="Suma de llamadas atendidas en el rango."),
 "PTP":   dict(t="Nivel de servicio", e="✅", sub="Atendidas en ≤ 20 s ÷ atendidas", kind="ratio", num="en_nivel_dia", den="atendidas_dia", f="p", inv=False,
               q="Qué parte de las llamadas atendidas se contestó a tiempo. Meta: 90 %.", c="1 − demoradas (espera > 20 s) ÷ atendidas. Verde ≥ 90 %, rojo < 90 %."),
 "MPTP":  dict(t="% Abandono > 5 s", e="🚪", sub="Abandonadas > 5 s ÷ recibidas", kind="ratio", num="abandonadas_5s_dia", den="recibidas_dia", f="p", inv=True,
               q="Llamadas en que el cliente colgó tras esperar más de 5 s. Meta: 5 %.", c="Abandonadas con espera > 5 s ÷ recibidas. Verde ≤ 5 %, rojo > 5 %."),
 "Cob":   dict(t="ASA", e="⏱️", sub="Espera promedio antes de atender", kind="ratio", num="espera_seg_dia", den="atendidas_dia", f="s", inv=True,
               q="Segundos que espera en promedio el cliente antes de que lo atiendan. Meta: 20 s.", c="(Cola + pendiente) ÷ atendidas. Verde ≤ 20 s, rojo > 20 s."),
 "Cont":  dict(t="TMO", e="🕒", sub="Tiempo promedio por llamada", kind="ratio", num="tmo_seg_dia", den="atendidas_dia", scale="/60", f="m", inv=True,
               q="Minutos que dura en promedio una llamada atendida. Meta: 10 min.", c="(Pendiente + conversación + espera + post-llamada) ÷ atendidas. Verde ≤ 10 min, rojo > 10 min."),
 "Llam":  dict(t="Abandonadas", e="🚪", sub="Colgaron antes de ser atendidos", kind="sum", num="abandonadas_dia", f="n", inv=True,
               q="Llamadas en que el cliente colgó antes de ser atendido.", c="Suma de llamadas abandonadas en el rango."),
 "Conex": dict(t="Nivel de atención", e="📶", sub="Atendidas ÷ recibidas", kind="ratio", num="atendidas_dia", den="recibidas_dia", f="p", inv=False,
               q="Qué parte de las llamadas que entraron se atendió.", c="Atendidas ÷ recibidas."),
 "PxL":   dict(t="Atendidas por asesor", e="👤", sub="Promedio por asesor y día", kind="ratio", num="atendidas_dia", den="dia_asesor", f="r", inv=False,
               q="Cuántas llamadas atiende en promedio un asesor en un día.", c="Atendidas ÷ días-asesor con actividad."),
 "Int":   dict(t="Personas conectadas", e="👥", sub="Asesores distintos con actividad", kind="countd", f="n", inv=False,
               q="Cuántos asesores distintos tuvieron actividad en el rango.", c="Conteo de asesores distintos con actividad."),
 "Vue":   dict(t="Demoradas > 20 s", e="⌛", sub="Atendidas con espera > 20 s", kind="sum", num="demoradas_20s_dia", f="n", inv=True,
               q="Llamadas atendidas después de esperar más de 20 s.", c="Suma de llamadas atendidas con espera mayor a 20 s."),
 "MLl":   dict(t="% Tipificación", e="🏷️", sub="Tipificadas ÷ atendidas", kind="ratio", num="tipificadas_dia", den="atendidas_dia", f="p", inv=False,
               q="Qué parte de las llamadas atendidas se cerró con un motivo.", c="Atendidas con tipificación ÷ atendidas."),
 "MCa":   dict(t="Horas disponibles", e="🟢", sub="Listo para recibir llamadas", kind="sum", num="horas_disponible_dia", f="h", inv=False,
               q="Horas en que los asesores estuvieron listos para recibir llamadas.", c="Suma de horas en estado disponible."),
 "MVu":   dict(t="Horas en auxiliares", e="☕", sub="Estados no disponibles", kind="sum", num="horas_aux_dia", f="h", inv=True,
               q="Horas en estados no disponibles (baño, comida, etc.).", c="Suma de horas en auxiliares."),
 "FLl":   dict(t="Atendidas por hora", e="⚡", sub="Atendidas ÷ horas conectado", kind="ratio", num="atendidas_dia", den="horas_conectado_dia", f="r", inv=False,
               q="Cuántas llamadas atiende un asesor por hora conectado.", c="Atendidas ÷ horas conectado."),
 "FCa":   dict(t="Horas conectado", e="🔌", sub="Tiempo total en sesión", kind="sum", num="horas_conectado_dia", f="h", inv=False,
               q="Horas totales que los asesores estuvieron conectados.", c="Suma de horas conectado."),
 "KP":    dict(t="Tipificadas", e="🏷️", sub="Atendidas con motivo", kind="sum", num="tipificadas_dia", f="n", inv=False,
               q="Llamadas atendidas que se cerraron con un motivo.", c="Suma de llamadas tipificadas."),
 "MKP":   dict(t="Espera total", e="⏳", sub="Minutos en cola de las atendidas", kind="sum", num="espera_seg_dia", f="r", inv=True,
               q="Segundos totales de espera de las llamadas atendidas.", c="Suma de cola + pendiente de las atendidas."),
 "CMa":   dict(t="Días-asesor", e="📅", sub="Asesores con actividad por día", kind="sum", num="dia_asesor", f="n", inv=False,
               q="Suma de días en que cada asesor tuvo actividad.", c="Un día-asesor = un asesor con actividad en un día."),
 "Sin":   dict(t="Abandonadas > 5 s", e="🚪", sub="Colgaron tras esperar > 5 s", kind="sum", num="abandonadas_5s_dia", f="n", inv=True,
               q="Llamadas abandonadas después de esperar más de 5 s.", c="Suma de abandonadas con espera mayor a 5 s."),
}

def pon(nombre, formula, caption=None, datatype=None, fmt=None):
    """Reescribe la fórmula (y opcionalmente título, tipo y formato) de un cálculo en la fuente y en todas las hojas."""
    global x
    patron = re.compile(rf"<column caption='([^']*)' datatype='(\w+)'(?: default-format='[^']*')? name='\[{re.escape(nombre)}\]'( role='\w+' type='\w+'[^>]*)>\s*<calculation class='tableau' formula='[^']*' />")
    def r(m):
        cap = esc(caption) if caption else m.group(1); dtp = datatype or m.group(2)
        df = f" default-format='{esc(fmt)}'" if fmt else ""
        return f"<column caption='{cap}' datatype='{dtp}'{df} name='[{nombre}]'{m.group(3)}>\n        <calculation class='tableau' formula='{esc(formula)}' />"
    x, k = patron.subn(r, x)
    return k

for fam, f in F.items():
    pct = f["f"] == "p"
    dtp = "integer" if f["kind"] in ("countd",) or (f["kind"] == "sum" and f["f"] == "n") else "real"
    fmt = FMT[f["f"]]
    pon(f"K_{fam}_v", agg(f, CUR), f["t"], dtp, fmt)
    pon(f"K_{fam}_p", agg(f, PRE), f"{f['t']} (periodo previo)", dtp, fmt)
    pon(f"K_{fam}_s", agg(f, SEV), f"{f['t']} (7 días previos)", dtp, fmt)
    for k in (1, 2, 3):
        pon(f"K_{fam}_c{k}", agg(f, f"{CUR} AND [Calc_Canal]='Canal {k}'"), f"{f['t']} · Canal {k}", dtp, fmt)
    for suf, fo in deltas(fam, pct, f["inv"]).items():
        pon(f"K_{fam}_{suf}", fo, f"{f['t']} · {suf[0]} ({ {'g': 'mejora', 'r': 'empeora', 'n': 'sin cambio'}[suf[1]] })")

# tablas, embudos y selectores
pon("A_Asig", agg(F["Vue"], CUR), "Demoradas > 20 s", "integer", FMT["n"])
pon("A_Prom", agg(F["PTP"], CUR), "Nivel de servicio", "real", FMT["p"])
for nombre, cap, col in [("F_Asig", "① Recibidas", "recibidas_dia"), ("F_Marc", "② Atendidas", "atendidas_dia"),
                         ("F_Conn", "③ En nivel de servicio", "en_nivel_dia"), ("F_Ptp", "④ Tipificadas", "tipificadas_dia"),
                         ("FL_Ll", "① Recibidas", "recibidas_dia"), ("FL_Co", "② Atendidas", "atendidas_dia"),
                         ("FL_Kp", "③ En nivel de servicio", "en_nivel_dia"), ("FL_Pt", "④ Tipificadas", "tipificadas_dia")]:
    pon(nombre, f"SUM(IF {CUR} THEN [{col}] END)", cap, "integer", FMT["n"])

OPC_DIR = ["Recibidas", "Atendidas", "Abandonadas", "Nivel de servicio", "Nivel de atención", "% Abandono > 5 s", "ASA", "TMO", "Demoradas > 20 s"]
MAP_DIR = {"Recibidas": "Pago", "Atendidas": "Tasa", "Abandonadas": "Llam", "Nivel de servicio": "PTP", "Nivel de atención": "Conex",
           "% Abandono > 5 s": "MPTP", "ASA": "Cob", "TMO": "Cont", "Demoradas > 20 s": "Vue"}
def caso_crudo(op):
    f = F[MAP_DIR[op]]
    if f["kind"] == "sum": return f"SUM([{f['num']}])"
    return f"IF SUM([{f['den']}])>0 THEN SUM([{f['num']}])/SUM([{f['den']}]){f.get('scale', '')} END"
pon("M_DirV", "CASE [Parameters].[Parameter 9] " + " ".join(f"WHEN '{o}' THEN {caso_crudo(o)}" for o in OPC_DIR) + " END", "KPI elegido (canal)", "real")
pon("K_DirT", "IF ISNULL([M_DirV]) THEN '' ELSEIF [Parameters].[Parameter 9]='Nivel de servicio' OR [Parameters].[Parameter 9]='Nivel de atención' OR [Parameters].[Parameter 9]='% Abandono > 5 s' "
              "THEN STR(ROUND([M_DirV]*100,0))+'%' ELSEIF [Parameters].[Parameter 9]='ASA' THEN STR(ROUND([M_DirV],0))+' s' "
              "ELSEIF [Parameters].[Parameter 9]='TMO' THEN STR(ROUND([M_DirV],1))+' min' ELSE STR(ROUND([M_DirV],0)) END", "KPI elegido (canal, texto)")

OPC_SEG = ["Atendidas", "Nivel de servicio", "TMO", "% Tipificación", "Atendidas por hora", "Horas disponibles", "Horas en auxiliares", "Horas conectado"]
MAP_SEG = {"Atendidas": "Tasa", "Nivel de servicio": "PTP", "TMO": "Cont", "% Tipificación": "MLl", "Atendidas por hora": "FLl",
           "Horas disponibles": "MCa", "Horas en auxiliares": "MVu", "Horas conectado": "FCa"}
pon("M_SegV", "CASE [Parameters].[Parameter 5] " + " ".join(f"WHEN '{o}' THEN [K_{MAP_SEG[o]}_v]" for o in OPC_SEG) + " END", "KPI elegido", "real")
pon("M_SegC", "CASE [Parameters].[Parameter 5] " + " ".join(f"WHEN '{o}' THEN [K_{MAP_SEG[o]}_v]" for o in OPC_SEG) + " END", "KPI elegido (color)", "real", "n#,##0.0")
def seg_txt(o):
    f = F[MAP_SEG[o]]; v = f"[K_{MAP_SEG[o]}_v]"
    if f["f"] == "p": return f"STR(ROUND({v}*100,0))+'%'"
    if f["f"] == "m": return f"STR(ROUND({v},1))+' min'"
    if f["f"] in ("r", "h"): return f"STR(ROUND({v},1))"
    return f"STR(ROUND({v},0))"
pon("K_SegT", "CASE [Parameters].[Parameter 5] " + " ".join(f"WHEN '{o}' THEN IF ISNULL([K_{MAP_SEG[o]}_v]) THEN '' ELSE {seg_txt(o)} END" for o in OPC_SEG) + " END", "KPI elegido (texto)")

# detalle de llamadas entrantes
pon("LS_Cont", "IF [resultado_llamada]<>'Abandonada' THEN 1 ELSE 0 END", "Atendidas")
pon("LS_Talk", "IF [resultado_llamada]='Abandonada' THEN 1 ELSE 0 END", "Abandonadas")
pon("LS_Res", "[resultado_llamada]", "Tipificación")
OPC_H = ["Recibidas", "Atendidas", "Abandonadas", "% atención", "% abandono"]
pon("M_Hora", "CASE [Parameters].[Parameter 3] WHEN 'Recibidas' THEN SUM([LS_N]) WHEN 'Atendidas' THEN SUM([LS_Cont]) WHEN 'Abandonadas' THEN SUM([LS_Talk]) "
              "WHEN '% atención' THEN SUM([LS_Cont])/SUM([LS_N]) WHEN '% abandono' THEN SUM([LS_Talk])/SUM([LS_N]) END", "Métrica seleccionada")

# parámetros con las nuevas opciones
def param(nombre, opciones, defecto):
    global x
    def r(m):
        cab = re.sub(r"value='[^']*'", f"value='&quot;{esc(defecto)}&quot;'", m.group(1), count=1)
        mem = "".join(f"\n          <member value='&quot;{esc(o)}&quot;' />" for o in opciones)
        return (f"{cab}\n        <calculation class='tableau' formula='&quot;{esc(defecto)}&quot;' />\n        <members>{mem}\n        </members>\n      </column>")
    x = re.sub(rf"(<column caption='[^']*' datatype='string' name='\[{re.escape(nombre)}\]'[^>]*>)\s*<calculation[^>]*/>\s*<members>.*?</members>\s*</column>", r, x, flags=re.S)
param("Parameter 9", OPC_DIR, "Nivel de servicio")
param("Parameter 5", OPC_SEG, "Nivel de servicio")
param("Parameter 3", OPC_H, "Recibidas")
x = x.replace("caption='KPI (canal)'", "caption='KPI'")

# "¿Cuánto entra cada día?": recibidas en lugar de llamadas salientes
i = x.index("<worksheet name='Tendencia llamadas'"); j = x.index("</worksheet>", i)
x = x[:i] + x[i:j].replace("llamadas_salientes_dia", "recibidas_dia").replace("llamadas_contestadas_dia", "atendidas_dia").replace("pago_dia", "abandonadas_dia") + x[j:]


# "¿Rápido o a tiempo?": dispersión de asesores con TMO y nivel de servicio
i = x.index("<worksheet name='Asesores dispersión'"); j = x.index("</worksheet>", i)
w = x[i:j].replace("K_Llam_", "K_Cont_").replace("K_Pago_", "K_PTP_")
x = x[:i] + w + x[j:]
x = x.replace("⚖️ ¿Volumen o calidad?", "⚖️ ¿Rápido o a tiempo?")
x = x.replace("Cada punto es un asesor: abandonadas (horizontal) contra recibidas (vertical).", "Cada punto es un asesor: TMO (horizontal) contra nivel de servicio (vertical). Arriba a la izquierda = rápido y a tiempo.")

# ================= 3. Tarjetas: título, formato y tooltip =================
def tooltip(fam, f):
    q = lambda s: f"<![CDATA[<[{DSR}].[usr:K_{fam}_{s}:qk]>]]>"
    br = "<run>Æ&#10;</run>"
    sec = lambda t, color, cuerpo: (f"<run bold='true' fontcolor='#1b1f23' fontsize='11'>▸ </run><run bold='true' fontcolor='{color}' fontsize='10'>{t}</run>{br}"
                                    f"<run fontcolor='#3d464d' fontsize='10'>{esc(cuerpo)}</run>{br}")
    canales = "".join(f"<run bold='true' fontcolor='{c}' fontsize='11'>■ </run><run fontcolor='#1b1f23' fontsize='11'>Canal {k}: </run>"
                      f"<run bold='true' fontcolor='#1b1f23' fontsize='11'>{q('c' + str(k))}</run>{br}"
                      for k, c in ((1, "#09a2ab"), (2, "#056368"), (3, "#0b1f3a")))
    leer = "Bajar es mejorar: ▼ en verde." if f["inv"] else "Subir es mejorar: ▲ en verde."
    return ("<customized-tooltip>\n            <formatted-text>"
            f"<run bold='true' fontcolor='#2e7d32' fontsize='14'>{esc(f['t'])}</run>{br}"
            f"<run fontcolor='#757575' fontsize='10'>ℹ️ {esc(f['q'])}</run>{br}"
            f"<run fontcolor='#1b1f23' fontsize='11'>📆 Rango seleccionado: </run><run bold='true' fontcolor='#1b1f23' fontsize='12'>{q('v')}</run>{br}"
            f"<run fontcolor='#1b1f23' fontsize='11'>↩️ Periodo previo: </run><run bold='true' fontcolor='#1b1f23' fontsize='12'>{q('p')}</run>{br}"
            f"<run fontcolor='#1b1f23' fontsize='11'>🗓️ 7 días previos: </run><run bold='true' fontcolor='#1b1f23' fontsize='12'>{q('s')}</run>{br}{br}"
            f"<run bold='true' fontcolor='#1b1f23' fontsize='11'>🧱 Por canal — {esc(f['t'].lower())}</run>{br}{canales}"
            f"<run fontcolor='#c9d1d6' fontsize='8'>────────────────────────</run>{br}"
            + sec("🔎 QUÉ MIDE", "#1f4e79", f["q"]) + sec("🧮 CÓMO SE CALCULA", "#9a5a00", f["c"])
            + sec("🧭 CÓMO LEERLO", "#6f42c1", f"Número grande = rango elegido; abajo, la comparación contra el periodo previo y contra 7 días antes. {leer}")
            + sec("🎯 PARA QUÉ SIRVE ESTA VISTA", "#2e7d32", "Ver de un vistazo si la operación cumple y si va mejorando.")
            + "<run fontcolor='#757575' fontsize='9'>Respeta los filtros Periodo y Canal de arriba.</run>"
            "</formatted-text>\n          </customized-tooltip>")

for hoja in re.findall(r"<worksheet name='(KPI [A-Za-z]+)'>", x):
    fam = hoja.split()[1]; f = F.get(fam)
    if not f: continue
    i = x.index(f"<worksheet name='{hoja}'"); j = x.index("</worksheet>", i); w = x[i:j]
    w = re.sub(r"<title>.*?</title>", f"<title>\n          <formatted-text>\n            <run bold='true' fontcolor='#ffffff' fontsize='13'>{f['e']} {esc(f['t'])}</run>\n            <run>Æ&#10;</run>\n            <run fontcolor='#d6e6f2' fontsize='10'>{esc(f['sub'])}</run>\n          </formatted-text>\n        </title>", w, count=1, flags=re.S)
    w = re.sub(r"\s*<format attr='text-format' (?:field='[^']*' )?value='[^']*' />", "", w)   # usa el formato del cálculo
    w = re.sub(r"(<run bold='true' fontalignment='1' fontcolor=')#\w+(' fontsize='28')", r"\1#007f84\2", w)
    w = re.sub(r"<customized-tooltip>.*?</customized-tooltip>", lambda m: tooltip(fam, f), w, count=1, flags=re.S)
    x = x[:i] + w + x[j:]

# ================= 4. Textos visibles =================
TEXTOS = [
 ("{Cliente} · ¿Cómo va la campaña?", "{Cliente} · ¿Cómo va el servicio?"),
 ("{Cliente} · ¿Qué hay que corregir hoy?", "{Cliente} · ¿Qué hay que corregir hoy?"),
 ("{Cliente} · ¿Quién cumple la meta y a quién hay que apoyar?", "{Cliente} · ¿Cómo rinde cada asesor?"),
 ("🔻 ¿Dónde se pierde?", "🔻 ¿Dónde se pierden las llamadas?"),
 ("asignados → gestionados → con contacto → promesas.", "recibidas → atendidas → en nivel de servicio → tipificadas."),
 ("🎯 ¿Qué canal tiene cartera sin tocar?", "🎯 ¿Cómo atiende cada canal?"),
 ("Por canal: cuánta cartera se trabaja, cuánto contesta, cuánto promete y cuánto recupera en el periodo", "Por canal: cuántas llamadas entran, qué tan rápido se atienden y cuánto se abandona en el periodo"),
 ("🧩 ¿Cuánto aporta cada canal?", "🧩 ¿Cómo va cada canal en el KPI elegido?"),
 ("¿Qué canal recupera más cada día?", "¿Qué canal cumple cada día?"),
 ("🧩 ¿Qué canal recupera más?", "🧩 ¿Qué canal recibe más?"),
 ("Cada rebanada es lo que aporta un canal al pago del periodo.", "Cada rebanada es lo que aporta un canal a las llamadas del periodo."),
 ("🕒 ¿En qué horas contestan los titulares?", "🕒 ¿A qué hora entra más y cuándo nos falta gente?"),
 ("¿En qué horas contestan los titulares?", "¿A qué hora entra más y cuándo nos falta gente?"),
 ("Casos asignados, llamadas, % promesa, % conexión y monto recuperado por asesor en el periodo.", "Llamadas, nivel de servicio, TMO y tiempos por asesor en el periodo."),
 ("📞 ¿Qué está pasando en las llamadas?", "📞 ¿Por qué llaman?"),
 ("Cómo terminó cada llamada marcada, de mayor a menor y apilada por canal.", "Motivo con que se cerró cada llamada, de mayor a menor y apilado por canal."),
 ("📞 ¿Cuántas llamadas llegan a promesa?", "📞 ¿Cuántas llamadas se atienden a tiempo?"),
 ("Marcadas → contestadas → conversaciones. Muestra cuánto de la marcación se pierde antes de hablar con el cliente.", "Recibidas → atendidas → en nivel de servicio → tipificadas."),
 ("⏰ ¿A qué horas se trabaja más?", "⏰ ¿A qué horas entran más llamadas?"),
 ("Llamadas marcadas por hora del día, apiladas por canal. Detecta horas muertas y picos de marcación.", "Llamadas recibidas por hora del día, apiladas por canal. Detecta picos y horas con poca gente."),
 ("👥 ¿Quién marca más?", "👥 ¿Quién atiende más?"),
 ("Llamadas realizadas por cada asesor en el periodo.", "Llamadas atendidas por cada asesor en el periodo."),
 ("⚖️ ¿Esfuerzo o resultado?", "⚖️ ¿Volumen o calidad?"),
 ("Cada punto es un asesor: llamadas (horizontal) contra monto recuperado (vertical). Abajo a la derecha = mucho esfuerzo, poco resultado.", "Cada punto es un asesor: abandonadas (horizontal) contra recibidas (vertical)."),
 ("📈 ¿Cuánto se marca cada día?", "📈 ¿Cuánto entra cada día?"),
 ("Cada celda es un canal en un día; más oscuro = más llamadas.", "Cada celda es un canal en un día; más oscuro = más llamadas recibidas."),
 ("🎯 ¿Quién cumple la meta cada día?", "🎯 ¿Cómo rinde cada asesor cada día?"),
 ("📋 Seguimiento por asesor", "📋 Rendimiento por asesor"),
 ("Monto, cartera, promesas, KP, llamadas y faltantes contra la meta diaria, del periodo elegido (como el reporte diario).", "Llamadas, servicio, tiempos y conexión por asesor en el periodo elegido."),
 ("¿Cómo va la cobranza?", "¿Cómo va el servicio?"),
 ("Monto recuperado, promesas y contacto; mapa de calor por canal y día, embudo, KPI día a día y tabla por canal.", "Recibidas, atendidas, nivel de servicio, abandono, ASA y TMO; mapa de calor por canal y día, embudo y tabla por canal."),
 ("A qué hora contestan y cuál es la mejor hora, tipificaciones y qué asesor necesita apoyo.", "A qué hora entra más, por qué llaman y qué asesor necesita apoyo."),
 ("¿Quién cumple?", "¿Cómo rinde cada asesor?"),
 ("Metas por asesor y por día: 4,000 llamadas, casos asignados y vueltas; mapa de cumplimiento.", "Atendidas, nivel de servicio, TMO y tiempos por asesor y por día."),
 ("Fuente: reporte diario de llamadas.", "Fuente: {reporte de llamadas entrantes}."),
 ("Clic en un asesor, hora, día o tipificación filtra toda la vista", "Clic en un asesor, hora, día o tipificación filtra toda la vista"),
]
for a, b_ in TEXTOS:
    x = x.replace(esc(a) if "&" in esc(a) and a not in x else a, b_)

# Guía y glosario: glosario de ATC (tres columnas)
def bloque(items):
    br = "<run>Æ&#10;</run>"
    return "".join(f"<run bold='true' fontcolor='{c}' fontsize='11'>{esc(t)}:</run><run fontcolor='#1b1f23' fontsize='11'> {esc(d)}</run>{br}"
                   f"<run fontcolor='#757575' fontsize='9'>      {esc(k)}</run>{br}{br}" for t, d, k, c in items)
G1 = [("📞 Recibidas", "llamadas únicas que entraron.", "Atendidas + abandonadas.", "#007f84"),
      ("🎧 Atendidas", "contestadas por un asesor.", "Terminadas por el asesor o el cliente, o transferidas.", "#007f84"),
      ("🚪 Abandonadas", "el cliente colgó antes de ser atendido.", "En cola, timbrando o sin respuesta.", "#007f84"),
      ("⌛ Demoradas", "atendidas con espera mayor a 20 s.", "Espera = tiempo en cola + pendiente.", "#007f84")]
G2 = [("✅ Nivel de servicio", "llamadas atendidas a tiempo.", "1 − demoradas ÷ atendidas. Meta 90 %: verde ≥ 90 %, rojo < 90 %.", "#0b1f3a"),
      ("📶 Nivel de atención", "qué parte de lo que entra se atiende.", "Atendidas ÷ recibidas.", "#0b1f3a"),
      ("🚪 % Abandono > 5 s", "clientes que colgaron tras esperar.", "Abandonadas con espera > 5 s ÷ recibidas. Meta 5 %.", "#0b1f3a"),
      ("⏱️ ASA", "espera promedio antes de ser atendido.", "(Cola + pendiente) ÷ atendidas. Meta 20 s.", "#0b1f3a"),
      ("🕒 TMO", "duración promedio de una llamada atendida.", "(Pendiente + conversación + espera + post-llamada) ÷ atendidas. Meta 10 min.", "#0b1f3a")]
G3 = [("👥 Personas conectadas", "asesores distintos con actividad.", "Conteo de asesores con actividad en el periodo.", "#55657a"),
      ("👤 Atendidas por asesor", "promedio diario por asesor.", "Atendidas ÷ días-asesor.", "#55657a"),
      ("🟢 Horas disponibles", "tiempo listo para recibir llamadas.", "Suma de horas en estado disponible.", "#55657a"),
      ("☕ Horas en auxiliares", "tiempo en estados no disponibles.", "Baño, comida, etc.", "#55657a"),
      ("🏷️ % Tipificación", "llamadas cerradas con un motivo.", "Tipificadas ÷ atendidas.", "#55657a")]
i = x.index("<dashboard name='Guía y glosario'"); j = x.index("</dashboard>", i); d = x[i:j]
for viejo, nuevo in [("💰 Cartera y pagos", "📞 Llamadas"), ("📞 Gestión y contacto", "✅ Servicio"), ("🎯 Metas y productividad", "👥 Equipo")]:
    d = d.replace(viejo, nuevo)
cuerpos = [m for m in re.finditer(r"(<zone [^>]*type-v2='text'[^>]*>\s*<formatted-text>)(.*?)(</formatted-text>)", d, re.S)
           if any(k in m.group(2) for k in ("Monto recuperado:", "% cartera gestionada", "Pago por llamada:"))]
for m, items in sorted(zip(cuerpos, (G1, G2, G3)), key=lambda t: -t[0].start()):
    d = d[:m.start(2)] + bloque(items) + d[m.end(2):]
d = d.replace("🧩 Canales", "🧩 Canales (colas)")
x = x[:i] + d + x[j:]


# ================= 4b. Tooltips de las demás hojas =================
CAP = {}
for m in re.finditer(r"<column caption='([^']*)' datatype='\w+'[^>]*name='\[([^\]]+)\]'", x):
    CAP.setdefault(m.group(2), html.unescape(m.group(1)))
CAP.update({"Calc_Asesor": "Asesor", "Calc_Canal": "Canal", "LS_Canal": "Canal", "LS_Hora": "Hora", "LS_Fecha": "Día",
            "fecha_dt": "Día", "LS_N": "Recibidas", "LS_Res": "Tipificación", "LS_Cont": "Atendidas", "LS_Talk": "Abandonadas",
            "recibidas_dia": "Recibidas", "atendidas_dia": "Atendidas", "abandonadas_dia": "Abandonadas"})
EMO = {"Asesor": "👤", "Canal": "🧩", "Día": "📅", "Hora": "⏰", "Tipificación": "🏷️"}
HOJAS = {
 "Asesores dispersión": ("Asesor: rapidez y servicio", "Cada punto es un asesor.", "El TMO y el nivel de servicio de cada asesor.", "Cálculo del periodo por asesor.", "Arriba a la izquierda = rápido y a tiempo; abajo a la derecha = necesita apoyo.", "Ver quién atiende rápido y a tiempo, y quién necesita apoyo."),
 "Asesores llamadas": ("Atendidas por asesor", "Llamadas atendidas por cada asesor.", "Cuántas llamadas atendió cada asesor en el rango.", "Suma de llamadas atendidas por asesor.", "De mayor a menor; clic en un asesor filtra la vista.", "Ver quién sostiene la operación y quién necesita apoyo."),
 "Asesores tabla": ("Resumen por asesor", "Una fila por asesor con sus llamadas, nivel de servicio y tiempos.", "Llamadas, nivel de servicio y tiempos de cada asesor.", "Cada columna es una métrica del periodo; la última fila es el total.", "Compara cada asesor contra el total y contra la meta.", "Detectar quién necesita apoyo hoy."),
 "Comparativo canal": ("KPI elegido por canal y día", "El KPI del selector, para un canal en un día.", "El KPI elegido por canal y día.", "Cada celda calcula el KPI con las llamadas de ese canal en ese día.", "Más oscuro = valor más alto. Clic en una celda filtra la vista.", "Ver qué canal y qué día se salen de la meta."),
 "Cumplimiento por asesor": ("KPI elegido por asesor", "El KPI del selector, por asesor en el periodo.", "El KPI elegido por asesor.", "Cálculo del periodo completo por asesor.", "Más largo = valor más alto.", "Comparar asesores con la misma métrica."),
 "Cumplimiento por día": ("KPI por asesor y día", "El KPI del selector para cada asesor y cada día.", "El KPI elegido por asesor y por día.", "Cada celda calcula el KPI de ese asesor en ese día.", "Más oscuro = valor más alto; celda vacía = sin actividad.", "Ver qué asesor y qué día se salen de lo normal."),
 "Embudo de casos": ("Embudo de llamadas", "De lo que entra a lo que se atiende a tiempo.", "Cuántas llamadas pasan cada etapa: recibidas, atendidas, en nivel de servicio y tipificadas.", "Suma de cada etapa en el periodo, por canal.", "Mira dónde cae más la barra.", "Saber en qué etapa se pierden las llamadas."),
 "Embudo de llamadas": ("Embudo de llamadas", "De lo que entra a lo que se atiende a tiempo.", "Cuántas llamadas pasan cada etapa: recibidas, atendidas, en nivel de servicio y tipificadas.", "Suma de cada etapa en el periodo, por canal.", "Mira dónde cae más la barra.", "Saber en qué etapa se pierden las llamadas."),
 "Intensidad canal": ("Resumen por canal", "Una fila por canal con sus llamadas, servicio y tiempos.", "Las métricas de servicio de cada canal.", "Cada columna es una métrica del periodo; la última fila es el total.", "Compara cada canal contra el total y contra la meta.", "Ver qué canal necesita más atención."),
 "Llamadas por hora": ("Llamadas por hora", "Llamadas que entran en cada hora del día, por canal.", "El volumen de llamadas por hora.", "Conteo de llamadas por hora de entrada.", "Las barras más altas son las horas pico.", "Planear cuánta gente se necesita en cada hora."),
 "Mapa de calor hora": ("Mapa de calor por hora", "La métrica elegida, hora por hora y día por día.", "Recibidas, atendidas, abandonadas o sus porcentajes por hora y día.", "Cada celda es una hora de un día.", "Más oscuro = valor más alto. Clic en una celda filtra la vista.", "Detectar las horas en que falta gente."),
 "Seguimiento tabla": ("Rendimiento por asesor", "Una fila por asesor con todas sus métricas.", "Llamadas, servicio, tiempos y conexión de cada asesor.", "Cada columna es una métrica del periodo; la última fila es el total.", "Ordena por la columna que te interese.", "Dar seguimiento diario a cada asesor."),
 "Tendencia conexión": ("KPI elegido por día", "El KPI del selector, día por día.", "El KPI elegido por día.", "Cálculo de cada día del periodo.", "Busca los días que se salen de la tendencia.", "Ver cómo evoluciona el servicio."),
 "Tendencia llamadas": ("Llamadas por canal y día", "Cada celda es un canal en un día.", "Las llamadas recibidas por canal y día.", "Suma diaria de recibidas por canal.", "Más oscuro = más llamadas. Clic en una celda filtra la vista.", "Ver qué días y canales concentran el volumen."),
 "Tendencia pago": ("Llamadas por día y canal", "Una línea por canal.", "Las llamadas de cada canal por día.", "Suma diaria por canal.", "Picos = días de mucho volumen.", "Ver cómo evoluciona el volumen por canal."),
 "Tendencia pago por llamada": ("KPI elegido por canal", "El KPI del selector por canal en el periodo.", "El KPI elegido por canal.", "Cálculo del periodo completo por canal.", "Más largo = valor más alto.", "Comparar canales con la misma métrica."),
 "Tendencia promesas": ("KPI elegido por día", "El KPI del selector, día por día.", "El KPI elegido por día.", "Cálculo de cada día del periodo.", "Busca los días que se salen de la tendencia.", "Ver cómo evoluciona el servicio."),
 "Tipificaciones": ("Tipificación de la llamada", "Motivo con que se cerró cada llamada.", "Cuántas llamadas hubo por cada motivo.", "Conteo de llamadas por tipificación, apilado por canal.", "De mayor a menor; clic en una barra filtra la vista.", "Saber por qué llaman los clientes."),
}
def tooltip_hoja(w, datos):
    tit, info, que, como, leer, sirve = datos
    br = "<run>Æ&#10;</run>"
    refs = []
    for m in re.finditer(r"<(?:color|text|lod|size|tooltip) column='(\[[^\]]+\]\.\[[^\]]+\])' />", w):
        refs.append(m.group(1))
    for m in re.finditer(r"<(?:rows|cols)>(.*?)</(?:rows|cols)>", w, re.S):
        refs += re.findall(r"\[federated\.[^\]]+\]\.\[(?:none|tdy|usr|sum):[^\]]+\]", m.group(1))
    lineas, vistos = "", set()
    for r in refs:
        ref = r if r.startswith("[federated") else r
        mm = re.search(r"\.\[(?:none|tdy|usr|sum|avg|cnt|ctd):([A-Za-z_0-9]+):", ref)
        if not mm or ref in vistos: continue
        cap = CAP.get(mm.group(1))
        if not cap or re.search(r"\(texto\)|· [psgrn]|\(color\)|periodo previo|7 días", cap): continue
        vistos.add(ref)
        lineas += (f"<run fontcolor='#1b1f23' fontsize='11'>{EMO.get(cap, '🔹')} {esc(cap)}: </run>"
                   f"<run bold='true' fontcolor='#1b1f23' fontsize='12'><![CDATA[<{ref}>]]></run>{br}")
    sec = lambda t, color, cuerpo: (f"<run bold='true' fontcolor='#1b1f23' fontsize='11'>▸ </run><run bold='true' fontcolor='{color}' fontsize='10'>{t}</run>{br}"
                                    f"<run fontcolor='#3d464d' fontsize='10'>{esc(cuerpo)}</run>{br}")
    return ("<customized-tooltip>\n            <formatted-text>"
            f"<run bold='true' fontcolor='#2e7d32' fontsize='14'>{esc(tit)}</run>{br}"
            f"<run fontcolor='#757575' fontsize='10'>ℹ️ {esc(info)}</run>{br}{lineas}"
            f"<run fontcolor='#c9d1d6' fontsize='8'>────────────────────────</run>{br}"
            + sec("🔎 QUÉ MIDE", "#1f4e79", que) + sec("🧮 CÓMO SE CALCULA", "#9a5a00", como)
            + sec("🧭 CÓMO LEERLO", "#6f42c1", leer) + sec("🎯 PARA QUÉ SIRVE ESTA VISTA", "#2e7d32", sirve)
            + "<run fontcolor='#757575' fontsize='9'>Respeta los filtros Periodo y Canal de arriba.</run>"
            "</formatted-text>\n          </customized-tooltip>")
for hoja, datos in HOJAS.items():
    if f"<worksheet name='{hoja}'>" not in x: continue
    i = x.index(f"<worksheet name='{hoja}'"); j = x.index("</worksheet>", i); w = x[i:j]
    w = re.sub(r"<customized-tooltip>.*?</customized-tooltip>", lambda m: tooltip_hoja(w, datos), w, flags=re.S)
    x = x[:i] + w + x[j:]
x = x.replace("📈 ¿Cómo evoluciona el pago?", "📈 ¿Cómo evoluciona el volumen?")
x = re.sub(r"Una línea por canal; cada punto es el pago aplicado ese día\. Picos = días de pagos grandes\.", "Una línea por canal; cada punto son las llamadas de ese día. Picos = días de mucho volumen.", x)
i = x.index("<dashboard name='Asesores'"); j = x.index("</dashboard>", i); d = x[i:j]
d = re.sub(r"Elige el KPI: cumplimiento de llamadas, casos o vueltas, llamadas, monto, promesas, KP, conexión y más\.?",
           "Elige el KPI: atendidas, nivel de servicio, TMO, tipificación, atendidas por hora u horas.", d)
d = re.sub(r"Metas por asesor y por día \(del reporte diario\): 4,000 llamadas[^<]*", "Métricas por asesor y por día del periodo elegido. Haz clic en un asesor y el resto de la vista se filtra.", d)
x = x[:i] + d + x[j:]

# Control "Descripciones: Mostrar / Ocultar" sobre los tooltips nuevos
import importlib.util as _ilu
_sp = _ilu.spec_from_file_location("descripciones", pathlib.Path(__file__).with_name("descripciones.py")); _de = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_de)
x = _de.agregar(x, colocar="plantilla")

# ================= 5. Empaquetar =================
nombre = "plantilla_atc_binatsa"
with zipfile.ZipFile(out / f"{nombre}.twbx", "w", zipfile.ZIP_DEFLATED) as zz:
    zz.writestr(f"{nombre}.twb", x.encode("utf-8"))
    zz.writestr("Data/datos/resumen_diario.csv", csv_res)
    zz.writestr("Data/datos/detalle_llamadas.csv", csv_lla)
    for n_ in zin.namelist():
        if n_.startswith("Image/"):
            zz.writestr(n_, zin.read(n_))
print("ok", out / f"{nombre}.twbx", len(fil), "filas de resumen,", len(fl), "llamadas")
