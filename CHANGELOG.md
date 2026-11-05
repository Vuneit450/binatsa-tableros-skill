# Registro de cambios

## 1.0 · 5 de noviembre de 2026
Primera versión en este repositorio, a partir de los módulos `dashboards-cobranza-*` de `binatsa-recursos`.
- Una sola skill, `skills/tableros-campanas-binatsa/`: `SKILL.md` de entrada y referencias que se abren por paso (datos, diseño, tooltips, cliente y limpieza, publicación y video guía).
- Métricas y reglas por tipo de campaña en `referencias/giros/` (Cobranza; ATC, Ventas y Retenciones por llenar).
- Plantillas vacías (brief, diccionario de datos y paleta del cliente) y herramientas (publicación con token y libro de prueba) dentro de la skill.
- Todo lo del cliente vive en la carpeta privada del proyecto, `BINATSA-Tableros/<cliente>/<campaña>/`; `.gitignore` bloquea libros, datos, registros y credenciales.
