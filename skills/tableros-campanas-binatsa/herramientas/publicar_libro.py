#!/usr/bin/env python3
"""Publica un libro de Tableau (.twbx o .twb) en Tableau Cloud con un token de acceso personal.

NO PROBADO contra un sitio real: probarlo primero con un libro de prueba en un proyecto de pruebas.

Variables de entorno (las configura el usuario; nunca se escriben en archivos ni en el chat):
  TABLEAU_SERVER      servidor, sin https://   (ej. 10ax.online.tableau.com)
  TABLEAU_SITE        contentUrl del sitio     (vacío si es el sitio Default)
  TABLEAU_PAT_NAME    nombre del token
  TABLEAU_PAT_SECRET  secreto del token

Uso:
  python publicar_libro.py --listar-proyectos
  python publicar_libro.py libro/mi_libro_v3.twbx --proyecto "Pruebas" --nombre "Mi libro"            (simula)
  python publicar_libro.py libro/mi_libro_v3.twbx --proyecto "Pruebas" --nombre "Mi libro" --publicar (publica)

Por seguridad: sin --publicar solo simula; y si el proyecto no tiene "prueba" en su nombre, publicar
exige además --confirmo-produccion.
"""
import argparse
import datetime
import os
import pathlib
import sys

import tableauserverclient as TSC

REQUERIDAS = ["TABLEAU_SERVER", "TABLEAU_PAT_NAME", "TABLEAU_PAT_SECRET"]


def error(mensaje, codigo=2):
    print(f"ERROR: {mensaje}", file=sys.stderr)
    sys.exit(codigo)


def main():
    ap = argparse.ArgumentParser(description="Publica un libro de Tableau en Tableau Cloud.")
    ap.add_argument("libro", nargs="?", help="ruta del .twbx o .twb")
    ap.add_argument("--proyecto", help="nombre del proyecto de destino")
    ap.add_argument("--nombre", help="nombre del libro en Tableau (por defecto, el del archivo)")
    ap.add_argument("--listar-proyectos", action="store_true", help="solo lista los proyectos que ve el token")
    ap.add_argument("--publicar", action="store_true", help="publica de verdad (sin esto, solo simula)")
    ap.add_argument("--confirmo-produccion", action="store_true",
                    help="obligatorio para publicar en un proyecto que no sea de pruebas")
    args = ap.parse_args()

    faltan = [v for v in REQUERIDAS if not os.environ.get(v)]
    if faltan:
        error("faltan variables de entorno: " + ", ".join(faltan) + ". No se escriben en archivos ni en el chat.")

    servidor = TSC.Server("https://" + os.environ["TABLEAU_SERVER"], use_server_version=True)
    auth = TSC.PersonalAccessTokenAuth(
        os.environ["TABLEAU_PAT_NAME"], os.environ["TABLEAU_PAT_SECRET"],
        site_id=os.environ.get("TABLEAU_SITE", ""))

    try:
        with servidor.auth.sign_in(auth):
            proyectos = {p.name: p for p in TSC.Pager(servidor.projects)}

            if args.listar_proyectos:
                print("Proyectos que ve este token:")
                for nombre in sorted(proyectos):
                    print("  -", nombre)
                return

            if not args.libro or not args.proyecto:
                error("indica el libro y --proyecto (o usa --listar-proyectos).")
            ruta = pathlib.Path(args.libro)
            if not ruta.is_file() or ruta.suffix.lower() not in (".twbx", ".twb"):
                error(f"el libro no existe o no es .twbx/.twb: {ruta}")
            if args.proyecto not in proyectos:
                error(f"no existe el proyecto '{args.proyecto}'. Proyectos visibles: " + ", ".join(sorted(proyectos)))

            nombre = args.nombre or ruta.stem
            proyecto = proyectos[args.proyecto]
            es_pruebas = "prueba" in args.proyecto.lower()

            opciones = TSC.RequestOptions()
            opciones.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                           TSC.RequestOptions.Operator.Equals, nombre))
            existentes = [w for w in TSC.Pager(servidor.workbooks, opciones) if w.project_id == proyecto.id]
            modo = TSC.Server.PublishMode.Overwrite if existentes else TSC.Server.PublishMode.CreateNew
            accion = "SOBRESCRIBIRÍA el libro existente" if existentes else "CREARÍA un libro nuevo"
            print(f"Libro: {ruta}  |  Proyecto: {args.proyecto}  |  Nombre: {nombre}")
            print(f"Esto {accion}.")

            if not args.publicar:
                print("Simulación: no se publicó nada. Agrega --publicar para publicar.")
                return
            if not es_pruebas and not args.confirmo_produccion:
                error("el proyecto no parece de pruebas. Confirma con el usuario y agrega --confirmo-produccion.")

            libro = TSC.WorkbookItem(project_id=proyecto.id, name=nombre)
            publicado = servidor.workbooks.publish(libro, str(ruta), modo)
            print(f"Publicado. id: {publicado.id}")
            url = getattr(publicado, "webpage_url", None)
            if url:
                print(f"URL: {url}")

            registro = pathlib.Path("publicaciones.log")
            with registro.open("a", encoding="utf-8") as f:
                f.write(f"{datetime.datetime.now().isoformat(timespec='seconds')}\t{ruta}\t{args.proyecto}\t{nombre}\t{publicado.id}\n")
    except TSC.ServerResponseError as e:
        error(f"Tableau respondió con un error: {e.code} {e.summary}. Revisa permisos del usuario del token.", 1)
    except Exception as e:  # nunca imprimir las variables de entorno
        error(f"no se pudo completar: {type(e).__name__}. Revisa el servidor, el sitio y la conexión.", 1)


if __name__ == "__main__":
    main()
