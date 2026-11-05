---
name: tableros-campanas-binatsa
description: "Tableros de campañas de call center de BINATSA en Tableau Cloud (Cobranza, ATC, Ventas, Retenciones) con el estilo BINATSA. Usar al crear, rehacer, modificar, revisar o publicar un tablero o dashboard de una campaña; al recibir un .twbx o un link de Tableau Cloud de un cliente de BINATSA; al descargar o publicar con token, servidor MCP o API de Tableau; o al hacer el video guía de un tablero."
---

# Tableros de campañas BINATSA
Responder en español, corto y directo.

Objetivo: que cada tablero se reconozca como de BINATSA a primera vista. El estilo es fijo; por proyecto solo cambian los datos, las métricas del giro y los colores del cliente. Del libro del cliente se toman los datos y las reglas, nunca su diseño.

- Una campaña = un libro = un tablero (si hay más, el usuario lo indica).
- "Propuesto" en cualquier referencia = aplicarlo por defecto, avisarlo y marcarlo "por confirmar".

## Qué abrir en cada paso
| Paso | Abrir |
|---|---|
| Datos, reglas y caso de control | `referencias/datos.md` + `referencias/giros/<giro>.md` |
| Construcción | `referencias/diseno.md`, `referencias/tooltips.md` y el giro |
| Pruebas y publicación | `referencias/publicacion.md`, `referencias/cliente-limpieza.md` |
| Video guía | `referencias/video-guia.md` |
| Descargar o publicar con token | `herramientas/README.md` |

Giros: `cobranza.md` y `atc.md` (completos); `retenciones.md` (parcial); Ventas sin archivo. Si el giro no está completo, avisar y armarlo con el usuario a partir de las reglas generales.

## Flujo
0. **Preparación (una vez):** cuenta dedicada en Tableau Cloud con un solo token (ver Seguridad). Libro plantilla BINATSA en `plantillas/` (mientras no exista, construir desde cero siguiendo `referencias/diseno.md`).
1. **Arranque:** el usuario conecta la carpeta `BINATSA-Tableros/<cliente>/<campaña>/` con el logo del cliente en PNG y da el link del libro publicado. Crear `marca/`, `libro/`, `datos/`, `capturas/`, `video/` y copiar `brief.md` de `plantillas/`. Si ya existe `brief.md`, leerlo primero y no repetir lo que ya está respondido.
2. **Libro:** descargarlo con `herramientas/descargar_libro.py`; si no se puede, pedirlo al usuario en `libro/`. Guardar el original intacto (`<nombre>_v0_original.twbx`) y trabajar siempre en copias (`v1`, `v2`…).
3. **Revisión y preguntas:** leer la estructura del libro sin abrir datos (vistas, hojas, fuentes, fórmulas, parámetros); sacar la paleta del logo y revisar el contraste; entregar un resumen (qué datos hay, qué reglas se encontraron, qué falta); hacer las preguntas con respuesta propuesta. Antes de abrir datos reales, pedir permiso (ver Seguridad).
4. **Reglas y caso de control:** acordar las reglas generales y las del giro, registrarlas en `brief.md` y fijar el caso de control (un día del reporte actual con sus cifras).
5. **Construcción:** desde la plantilla, reemplazar la fuente de datos y ajustar colores, logo, nombres y métricas del giro. Orden: vistas, tarjetas, mapas de calor, hojas de Operación, tooltips, Guía y glosario. Proponer al usuario los gráficos adicionales.
6. **Pruebas (solo en el proyecto de pruebas):** publicar y revisar contra el checklist, la prueba de interacción y el caso de control. Cada casilla que no cumple es un pendiente con su contador. En cada vuelta se corrigen juntos todos los pendientes abiertos y se publica una vez; un pendiente que llega a 5 intentos se aparta y se reporta; lo que se rompa al corregir entra como pendiente nuevo. Termina cuando no queda ningún pendiente abierto con menos de 5 intentos. Reportar qué se cumplió, qué quedó apartado y qué debe decidir el usuario.
7. **Revisión del usuario:** visto bueno o cambios (cambios = vuelve al paso 5).
8. **Publicación final:** solo con confirmación del usuario en ese momento. Publicar sobre el libro de producción (mismo nombre y proyecto); verificar que la contraseña de la fuente siga incrustada, que la programación de actualización corra ("Ejecutar ahora") y que haya alertas de fallo. Preparar la vista del cliente (`referencias/cliente-limpieza.md`).
9. **Video guía:** hacerlo, entregarlo y agregar al tablero el enlace "▶ Manual en video" (`referencias/video-guia.md`).
10. **Cierre:** recordar al usuario quitar a la cuenta dedicada el acceso al proyecto; registrar en `brief.md` la versión publicada y la fecha.

**Cambios después de la entrega:** leer `brief.md`, hacer el cambio en una copia nueva y seguir desde el paso 6 ("Mantenimiento" en `referencias/publicacion.md`).
**Sesión sin usuario presente:** avanzar hasta el paso 6 marcando lo supuesto "por confirmar"; nunca publicar en producción ni compartir con el cliente.

## Preguntas
Con la herramienta de opción múltiple si existe (en Claude Code, AskUserQuestion); si no, en texto con opciones numeradas. Máximo 4 por tanda, cada una con una respuesta propuesta y marcada como recomendada. No preguntar lo que ya está en `brief.md` o en el chat. Cada respuesta se registra en `brief.md`.

**Tanda 1 · al terminar la revisión (paso 3), antes de construir:**
1. Cliente y campaña: nombres para el título "<Campaña> · <Vista>" y el subtítulo (propuestos a partir del libro).
2. Tipo de campaña: Cobranza, ATC, Ventas o Retenciones (propuesto según los campos del libro).
3. Paleta: la sacada del logo (mostrarla con su contraste), "Te paso los hex" o "Ajustar". Si no hay logo: "Solo texto con sus colores".
4. Vistas: Dirección, Operación y Guía y glosario (obligatorias) + Asesores (recomendada) + las vistas propias del giro que apliquen + "Otra (describirla)".

**Tanda 2 · reglas (paso 4):**
5. Categorías del giro: nombres y rangos (por ejemplo segmentos de mora, nunca asumir A/B/C) y si separa por canal o campaña.
6. Las reglas por acordar del giro que no se pudieron leer del libro (`referencias/giros/<giro>.md`).
7. Metas: en Cobranza, siempre del cliente ("No hay metas" o "Sí, las paso"); en ATC, las estándar salvo que pida otras.
8. Caso de control: qué día y de qué reporte salen las cifras para cuadrar.

**Tanda 3 · antes de la primera publicación (paso 6):**
9. Sitio, proyecto de pruebas y libro de producción (si no salen del link).
10. Horario, frecuencia y zona horaria de la actualización.
11. Canal de alertas de fallo: "Slack (¿cuál canal?)", "Correo", "Otro" o "Sin alertas". Nunca asumir uno.
12. Quién tiene acceso y qué vistas ve el cliente (por defecto todas; confirmar si alguna es solo interna).

<!-- Secciones siguientes: por reescribir (flujo, preguntas, seguridad) -->
## Recursos de BINATSA
- Repositorio de GitHub (público): Vuneit450/binatsa-tableros-skill. Solo lleva lo que sirve para cualquier campaña.
  - marca-binatsa/binatsa.svg: logo vectorial (turquesa #00B3B8, azul marino #0B1F3A). Usarlo siempre; si Tableau no acepta SVG en el objeto Imagen, generar un PNG desde el SVG.
  - marca-binatsa/paleta-binatsa.md y marca-binatsa/Preferences-BINATSA.tps: paleta de BINATSA (derivada del logo) y su versión para cargar en Tableau.
  - plantillas/: brief.md, diccionario-datos.md y paleta-cliente.md, vacías. Se copian a la carpeta privada del proyecto.
  - Si el repositorio no está conectado a la sesión, leerlo desde el navegador o pedir el archivo.
- Todo lo del cliente (logo, paleta, brief, reglas, libros, datos, capturas y video) vive en la carpeta privada del proyecto, `BINATSA-Tableros/<cliente>/<campaña>/`, y nunca se sube al repositorio.

## Reglas generales (Tableau Cloud)
1. NUNCA mover ni modificar consultas/fuentes. Solo ocultar campos huérfanos que ningún reporte use ni vaya a usar.
2. Las credenciales las captura SIEMPRE el usuario; nunca escribir contraseñas.
3. Publicar SOBRE el workbook existente (mismo nombre y proyecto) para conservar programación y credenciales; con otro nombre se pierde la programación.
4. Edición web: autoguardado como "Borrador"; Publicar sobrescribe. Arrastrar anchos de columna no funciona. Hojas ocultas se abren desde el icono "Ir a hoja" de la zona del dashboard.
5. Alertas de fallo: canal elegido por el usuario para cada proyecto; lo configura el usuario en Tableau.
6. Permisos mínimos y datos sensibles: ver la sección "Permisos mínimos y datos sensibles" más abajo. Se aplica siempre que la sesión use un token, el servidor MCP o la API de Tableau.

## Permisos mínimos y datos sensibles
Un token de acceso personal actúa como el usuario que lo creó: alcanza todo lo que ese usuario puede ver y hacer. Por eso:
1. Usuario dedicado: el token se crea desde una cuenta propia para este trabajo (por ejemplo "claude-bi"), nunca desde la cuenta personal ni la de un administrador del sitio.
2. Acceso mínimo: esa cuenta ve solo los proyectos que hacen falta (el de pruebas y el del cliente en curso), con un rol que permita publicar pero no administrar el sitio. Si se puede separar, sin permiso de borrado.
3. Nunca borrar: la sesión no borra libros, fuentes de datos, extractos ni tareas de actualización, aunque la herramienta lo permita, salvo que el usuario lo pida expresamente en ese momento. En el servidor MCP, deshabilitar las herramientas de borrado antes de conectarlo.
4. Datos agregados: para explorar y validar, consultar sumas y conteos por día, segmento o canal. No traer registros con nombres, teléfonos ni identificadores de clientes finales. Si un caso de control exige ver registros, pedir confirmación, limitar a unas pocas filas y no guardarlas en archivos, capturas ni en el repositorio.
5. Política: antes de consultar datos reales, confirmar con el usuario qué permiten la empresa y el cliente sobre pasar datos por una herramienta externa.
6. Vida del token: no escribirlo en archivos ni en el chat; revisar su expiración y revocarlo al terminar el proyecto.
7. Registro: anotar en `brief.md` qué cuenta y qué alcance se usaron, sin el token.
8. Si el usuario pide dar un acceso más amplio, advertir los riesgos de esta sección antes de continuar.

## Herramientas de Tableau para trabajar sin pasar por la web (por validar con el sitio del usuario)
- Servidor MCP de Tableau (el oficial): lee fuentes de datos ya publicadas, sus metadatos y permite consultar datos. Sirve para explorar y para el caso de control. No diseña dashboards. Antes de conectarlo, revisar su lista real de herramientas y deshabilitar las de borrado; usar un token con los permisos mínimos que haga falta.
- Biblioteca `tableauserverclient` (Python) o la API REST: publicar libros con la opción de sobrescribir activada y autenticación con el token del usuario.
- API de Hyper: leer los extractos `.hyper` en local.
- Navegador: solo para la revisión visual, porque ninguna de las anteriores devuelve el dashboard tal como lo ve el usuario.
- Antes de depender de cualquiera, probarla una vez con un libro de prueba en un proyecto de pruebas.

## Trabajo con una carpeta local
Cuando la sesión está conectada a una carpeta de la computadora del usuario (por ejemplo en el escritorio), se trabaja así:
- Estructura sugerida, una carpeta por cliente: `libro/` (el libro actual y sus versiones: v1, v2…), `datos/` (el extracto o la muestra y el diccionario de datos), `marca/` (logo y colores del cliente), `capturas/` (las capturas HD para el video), `video/` (el motor, las versiones del video y el guion; ver el módulo de video guía) y `brief.md` (las respuestas a las preguntas iniciales y las reglas de negocio acordadas, para no volver a preguntarlas).
- Los datos reales se quedan en esa carpeta: nunca se suben al repositorio de BINATSA, que es público.
- Ciclo hasta cumplir todo: 1) editar una copia versionada del libro en la carpeta; 2) publicarla; 3) revisar el resultado publicado en el navegador con la sesión del usuario; 4) corregir lo que no cumpla el checklist; 5) repetir desde el paso 1.
- Quién publica: la sesión, por la línea de comandos o la API de Tableau, con un token de acceso personal que el usuario configuró antes como variable de entorno (con permiso de publicar en el proyecto). El token o la contraseña nunca se escriben en archivos ni en el chat. Si no hay token, publica el usuario desde Tableau. Para incrustar credenciales en el extracto, publicar desde Tableau Desktop (ver publicación).
- Objetivo y tope: el ciclo termina cuando todas las casillas del checklist de publicación están cumplidas y la prueba de interacción pasa. Se limita a 5 vueltas (propuesto); si no se cumple, se reporta qué falta y se detiene, sin seguir publicando.
- Antes de la primera publicación sobre un libro de producción, confirmar con el usuario. Cada publicación deja registrada la versión que se subió, para poder volver a la anterior.
