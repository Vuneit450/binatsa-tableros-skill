#!/usr/bin/env python3
"""Descarga un libro publicado en Tableau Cloud (.twbx) con un token de acceso personal.

NO PROBADO contra un sitio real: probarlo primero con el libro de prueba.

Variables de entorno (las configura el usuario; nunca se escriben en archivos ni en el chat):
  TABLEAU_SERVER, TABLEAU_SITE, TABLEAU_PAT_NAME, TABLEAU_PAT_SECRET   (ver herramientas/README.md)

Uso:
  python descargar_libro.py --listar-libros --proyecto "Cliente X"
  python descargar_libro.py --proyecto "Cliente X" --nombre "Cobranza Tarjetas" --carpeta libro/
  python descargar_libro.py --proyecto "Cliente X" --nombre "Cobranza Tarjetas" --con-fuentes   (también las fuentes publicadas, en datos/)

Guarda el libro como <carpeta>/<nombre>_v0_original.twbx y nunca sobrescribe un archivo existente.
Si el libro trae extracto, baja datos reales: la carpeta de destino debe ser la carpeta privada del
proyecto, nunca el repositorio.
"""
import argparse
import os
import pathlib
import re
import sys

import tableauserverclient as TSC

REQUERIDAS = ["TABLEAU_SERVER", "TABLEAU_PAT_NAME", "TABLEAU_PAT_SECRET"]


def error(mensaje, codigo=2):
    print(f"ERROR: {mensaje}", file=sys.stderr)
    sys.exit(codigo)


def main():
    ap = argparse.ArgumentParser(description="Descarga un libro de Tableau Cloud.")
    ap.add_argument("--proyecto", required=True, help="nombre del proyecto donde está el libro")
    ap.add_argument("--nombre", help="nombre del libro en Tableau")
    ap.add_argument("--carpeta", default="libro", help="carpeta de destino (por defecto libro/)")
    ap.add_argument("--listar-libros", action="store_true", help="solo lista los libros del proyecto")
    ap.add_argument("--con-fuentes", action="store_true",
                    help="también descarga, con su extracción, las fuentes publicadas que usa el libro")
    ap.add_argument("--carpeta-datos", default="datos", help="carpeta para las fuentes publicadas (por defecto datos/)")
    args = ap.parse_args()

    faltan = [v for v in REQUERIDAS if not os.environ.get(v)]
    if faltan:
        error("faltan variables de entorno: " + ", ".join(faltan) + ". Pide al usuario el archivo en la carpeta.")

    servidor = TSC.Server("https://" + os.environ["TABLEAU_SERVER"], use_server_version=True)
    auth = TSC.PersonalAccessTokenAuth(
        os.environ["TABLEAU_PAT_NAME"], os.environ["TABLEAU_PAT_SECRET"],
        site_id=os.environ.get("TABLEAU_SITE", ""))

    try:
        with servidor.auth.sign_in(auth):
            proyectos = {p.name: p for p in TSC.Pager(servidor.projects)}
            if args.proyecto not in proyectos:
                error(f"el token no ve el proyecto '{args.proyecto}'. Proyectos visibles: " + ", ".join(sorted(proyectos)))
            proyecto = proyectos[args.proyecto]
            libros = [w for w in TSC.Pager(servidor.workbooks) if w.project_id == proyecto.id]

            if args.listar_libros:
                print(f"Libros en '{args.proyecto}':")
                for w in sorted(libros, key=lambda w: w.name):
                    print("  -", w.name)
                return

            if not args.nombre:
                error("indica --nombre (o usa --listar-libros).")
            encontrados = [w for w in libros if w.name == args.nombre]
            if not encontrados:
                error(f"no existe el libro '{args.nombre}' en '{args.proyecto}'.")

            carpeta = pathlib.Path(args.carpeta)
            carpeta.mkdir(parents=True, exist_ok=True)
            seguro = re.sub(r"[^\w\-]+", "_", args.nombre).strip("_")
            destino = carpeta / f"{seguro}_v0_original.twbx"
            if destino.exists():
                error(f"ya existe {destino}; no se sobrescribe el original.")

            libro = encontrados[0]
            ruta = servidor.workbooks.download(libro.id, filepath=str(destino), include_extract=True)
            print(f"Descargado: {ruta}")

            servidor.workbooks.populate_connections(libro)
            publicadas = {c.datasource_id: c.datasource_name for c in libro.connections
                          if c.connection_type == "sqlproxy" and c.datasource_id}
            if publicadas and not args.con_fuentes:
                print("Aviso: el libro usa fuentes publicadas; sus datos no vienen en el .twbx. "
                      "Vuelve a correr con --con-fuentes para descargarlas.")
            if args.con_fuentes:
                cdat = pathlib.Path(args.carpeta_datos); cdat.mkdir(parents=True, exist_ok=True)
                for fid, fnombre in publicadas.items():
                    seguro_f = re.sub(r"[^\w\-]+", "_", fnombre or fid).strip("_")
                    dest_f = cdat / f"{seguro_f}_v0_original.tdsx"
                    if dest_f.exists():
                        print(f"Ya existe {dest_f}; no se sobrescribe."); continue
                    rf = servidor.datasources.download(fid, filepath=str(dest_f), include_extract=True)
                    print(f"Fuente publicada descargada: {rf}")
                if not publicadas:
                    print("El libro no usa fuentes publicadas: los datos ya vienen en el .twbx (si tiene extracción).")
    except TSC.ServerResponseError as e:
        error(f"Tableau respondió con un error: {e.code} {e.summary}. Revisa que el token tenga permiso de descarga. "
              "Si no se puede, pide al usuario el archivo en la carpeta.", 1)
    except Exception as e:  # nunca imprimir las variables de entorno
        error(f"no se pudo completar: {type(e).__name__}. Pide al usuario el archivo en la carpeta.", 1)


if __name__ == "__main__":
    main()
