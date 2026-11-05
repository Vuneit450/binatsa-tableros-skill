# Registro de cambios

## 1.1 · 5 de noviembre de 2026
- Plantillas: Cobranza v0.4.4 y ATC v0.1.3 (nueva, generada con `herramientas/crear_plantilla_atc.py`), probadas en Tableau.
- Giros: `atc.md` completo (metas estándar NS 90 %, abandono 5 %, ASA 20 s, TMO 10 min) y `retenciones.md` (parcial).
- Interactividad: una sola acción de resaltar al pasar el mouse por vista, por su campo de categoría, sin tarjetas ni hojas que no tienen el campo; Periodo arranca en "Personalizado".
- Tooltips: control "💬 Descripciones" (Mostrar / Ocultar) al final de la fila de filtros, con el formato de los demás filtros (`herramientas/descripciones.py`).
- Nueva `herramientas/interactividad.py` para llevar lo anterior a libros que ya existen.
- Datos: libros siempre con extracción y descarga de fuentes publicadas (`descargar_libro.py --con-fuentes`).
- Video guía: ADN fijo, ficha de variables, voz sintética, máximo 100 MB, alojado en el repositorio de videos.

## 1.0 · 5 de noviembre de 2026
Primera versión en este repositorio, a partir de los módulos `dashboards-cobranza-*` de `binatsa-recursos`.
- Una sola skill, `skills/tableros-campanas-binatsa/`: `SKILL.md` de entrada y referencias que se abren por paso (datos, diseño, tooltips, cliente y limpieza, publicación y video guía).
- Métricas y reglas por tipo de campaña en `referencias/giros/` (Cobranza; ATC, Ventas y Retenciones por llenar).
- Plantillas vacías (brief, diccionario de datos y paleta del cliente) y herramientas (publicación con token y libro de prueba) dentro de la skill.
- Todo lo del cliente vive en la carpeta privada del proyecto, `BINATSA-Tableros/<cliente>/<campaña>/`; `.gitignore` bloquea libros, datos, registros y credenciales.
