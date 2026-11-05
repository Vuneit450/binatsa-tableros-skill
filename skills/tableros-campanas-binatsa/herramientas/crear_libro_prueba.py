#!/usr/bin/env python3
"""Crea un libro de prueba (.twbx) con datos INVENTADOS para probar la publicación en Tableau Cloud.

Solo usa la biblioteca estándar de Python. No necesita Tableau Desktop.

Uso:
  python skills/tableros-campanas-binatsa/herramientas/crear_libro_prueba.py                 (lo deja en ejemplos/libro-prueba/)
  python skills/tableros-campanas-binatsa/herramientas/crear_libro_prueba.py --salida otra/carpeta

El libro trae:
  - Data/datos/cobranza_prueba.csv  (20 filas inventadas: segmento, asesor, saldo, recuperado)
  - Hoja "Saldo por segmento" (barras horizontales, rampa de la paleta BINATSA)
  - Dashboard "Prueba de publicación" (1200x800 fijo) con la hoja y un título
"""
import argparse
import csv
import io
import pathlib
import random
import zipfile

NOMBRE = "prueba_publicacion"
DS = "federated.0binatsaprueba"
TXT = "textscan.0binatsaprueba"
SEGMENTOS = [("Al corriente", "#09A2AB"), ("1-30 días", "#078289"), ("31-60 días", "#056368"),
             ("61-90 días", "#04474A"), ("Más de 90 días", "#0B1F3A")]
ASESORES = ["Asesor A", "Asesor B", "Asesor C", "Asesor D"]


def datos():
    rnd = random.Random(42)  # siempre los mismos números inventados
    filas = []
    for seg, _ in SEGMENTOS:
        for asesor in ASESORES:
            saldo = rnd.randint(50, 400) * 1000
            filas.append([seg, asesor, saldo, int(saldo * rnd.uniform(0.2, 0.9))])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["Segmento", "Asesor", "Saldo", "Recuperado"])
    w.writerows(filas)
    return buf.getvalue()


def twb():
    colores = "\n".join(
        f"            <map to='{hexa}'><bucket>&quot;{seg}&quot;</bucket></map>" for seg, hexa in SEGMENTOS)
    return f"""<?xml version='1.0' encoding='utf-8' ?>
<workbook original-version='18.1' source-build='2023.1.0 (20231.23.0310.1045)' source-platform='win' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
  <preferences>
    <preference name='ui.encoding.shelf.height' value='24' />
    <preference name='ui.shelf.height' value='26' />
  </preferences>
  <datasources>
    <datasource caption='cobranza_prueba' inline='true' name='{DS}' version='18.1'>
      <connection class='federated'>
        <named-connections>
          <named-connection caption='cobranza_prueba' name='{TXT}'>
            <connection class='textscan' directory='Data/datos' filename='cobranza_prueba.csv' password='' server='' />
          </named-connection>
        </named-connections>
        <relation connection='{TXT}' name='cobranza_prueba.csv' table='[cobranza_prueba#csv]' type='table'>
          <columns character-set='UTF-8' header='yes' locale='es_MX' separator=','>
            <column datatype='string' name='Segmento' ordinal='0' />
            <column datatype='string' name='Asesor' ordinal='1' />
            <column datatype='integer' name='Saldo' ordinal='2' />
            <column datatype='integer' name='Recuperado' ordinal='3' />
          </columns>
        </relation>
      </connection>
      <aliases enabled='yes' />
      <column caption='Saldo' datatype='integer' name='[Saldo]' role='measure' type='quantitative' />
      <column caption='Recuperado' datatype='integer' name='[Recuperado]' role='measure' type='quantitative' />
      <column datatype='string' name='[Segmento]' role='dimension' type='nominal' />
      <column datatype='string' name='[Asesor]' role='dimension' type='nominal' />
      <layout dim-ordering='alphabetic' measure-ordering='alphabetic' show-structure='true' />
      <style>
        <style-rule element='mark'>
          <encoding attr='color' field='[none:Segmento:nk]' type='palette'>
{colores}
          </encoding>
        </style-rule>
      </style>
    </datasource>
  </datasources>
  <worksheets>
    <worksheet name='Saldo por segmento'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontcolor='#14202e' fontname='Inter' fontsize='14' bold='true'>Saldo por segmento (datos de prueba)</run>
          </formatted-text>
        </title>
      </layout-options>
      <table>
        <view>
          <datasources>
            <datasource caption='cobranza_prueba' name='{DS}' />
          </datasources>
          <datasource-dependencies datasource='{DS}'>
            <column datatype='string' name='[Segmento]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Saldo]' role='measure' type='quantitative' />
            <column-instance column='[Segmento]' derivation='None' name='[none:Segmento:nk]' pivot='key' type='nominal' />
            <column-instance column='[Saldo]' derivation='Sum' name='[sum:Saldo:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
            <encodings>
              <color column='[{DS}].[none:Segmento:nk]' />
              <text column='[{DS}].[sum:Saldo:qk]' />
            </encodings>
            <style>
              <style-rule element='mark'>
                <format attr='mark-labels-show' value='true' />
              </style-rule>
            </style>
          </pane>
        </panes>
        <rows>[{DS}].[none:Segmento:nk]</rows>
        <cols>[{DS}].[sum:Saldo:qk]</cols>
      </table>
      <simple-id uuid='{{6F1C2A10-0B1F-4A3A-9B00-00B3B8000001}}' />
    </worksheet>
  </worksheets>
  <dashboards>
    <dashboard name='Prueba de publicación'>
      <style />
      <size maxheight='800' maxwidth='1200' minheight='800' minwidth='1200' />
      <zones>
        <zone h='100000' id='1' type-v2='layout-basic' w='100000' x='0' y='0'>
          <zone h='10000' id='2' type-v2='text' w='100000' x='0' y='0'>
            <formatted-text>
              <run fontcolor='#007f84' fontname='Inter' fontsize='20' bold='true'>BINATSA · Libro de prueba</run>
            </formatted-text>
          </zone>
          <zone h='90000' id='3' name='Saldo por segmento' w='100000' x='0' y='10000' />
        </zone>
      </zones>
      <simple-id uuid='{{6F1C2A10-0B1F-4A3A-9B00-00B3B8000002}}' />
    </dashboard>
  </dashboards>
  <windows source-height='30'>
    <window class='worksheet' name='Saldo por segmento'>
      <simple-id uuid='{{6F1C2A10-0B1F-4A3A-9B00-00B3B8000003}}' />
    </window>
    <window class='dashboard' maximized='true' name='Prueba de publicación'>
      <viewpoints>
        <viewpoint name='Saldo por segmento' />
      </viewpoints>
      <active id='-1' />
      <simple-id uuid='{{6F1C2A10-0B1F-4A3A-9B00-00B3B8000004}}' />
    </window>
  </windows>
</workbook>
"""


def main():
    ap = argparse.ArgumentParser(description="Crea un .twbx de prueba con datos inventados.")
    raiz = pathlib.Path(__file__).resolve().parents[3]  # raíz del repo
    ap.add_argument("--salida", default=str(raiz / "ejemplos" / "libro-prueba"))
    carpeta = pathlib.Path(ap.parse_args().salida)
    carpeta.mkdir(parents=True, exist_ok=True)
    destino = carpeta / f"{NOMBRE}.twbx"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{NOMBRE}.twb", twb())
        z.writestr("Data/datos/cobranza_prueba.csv", datos())
    print(f"Listo: {destino}")


if __name__ == "__main__":
    main()
