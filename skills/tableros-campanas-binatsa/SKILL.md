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
0. **Preparación (una vez):** cuenta dedicada en Tableau Cloud con un solo token (ver Seguridad). Libros plantilla BINATSA en `plantillas/`: Cobranza en `plantilla_cobranza_binatsa.twbx` (marcadores y pendientes en `LEEME_plantilla_cobranza.md`); para los giros sin plantilla, construir desde cero siguiendo `referencias/diseno.md`.
1. **Arranque:** el usuario conecta la carpeta `BINATSA-Tableros/<cliente>/<campaña>/` con el logo del cliente en PNG y da el link del libro publicado. Crear `marca/`, `libro/`, `datos/`, `capturas/`, `video/` y copiar `brief.md` de `plantillas/`. Si ya existe `brief.md`, leerlo primero y no repetir lo que ya está respondido.
2. **Libro:** descargarlo con `herramientas/descargar_libro.py --con-fuentes` (trae el extracto y, si el libro usa fuentes publicadas, también esas fuentes con sus datos); si no se puede, pedirlo al usuario en `libro/`. Guardar el original intacto (`<nombre>_v0_original.twbx`) y trabajar siempre en copias (`v1`, `v2`…).
3. **Revisión y preguntas:** leer la estructura del libro sin abrir datos (vistas, hojas, fuentes, fórmulas, parámetros); sacar la paleta del logo y revisar el contraste; entregar un resumen (qué datos hay, qué reglas se encontraron, qué falta); hacer las preguntas con respuesta propuesta. Después, leer el extracto con sumas y conteos (`referencias/datos.md`).
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

## Qué va dónde
- **Repositorio público** (Vuneit450/binatsa-tableros-skill): solo lo que sirve para cualquier campaña: la skill, plantillas vacías, `herramientas/`, `marca-binatsa/` (logo, paleta y cierre del video) y ejemplos con datos inventados.
- **Carpeta privada del proyecto** (`BINATSA-Tableros/<cliente>/<campaña>/`): todo lo del cliente: logo y paleta (`marca/`), `brief.md`, libros, datos, capturas y el motor del video. Nunca se sube al repositorio de la skill.
- **Repositorio de videos de BINATSA:** solo el MP4 final de cada video guía (máximo 100 MB), por decisión de BINATSA (`referencias/video-guia.md`).
- Antes de cualquier commit al repositorio, revisar el cambio: no puede llevar nombres de clientes, campañas, personas, tablas, servidores ni direcciones IP, ni siquiera como ejemplo.

## Seguridad
**Cuenta y token**
1. Una cuenta dedicada en Tableau Cloud (por ejemplo "claude-bi"), con rol para publicar pero no para administrar el sitio y, si se puede, sin permiso de borrar. Un solo token, creado desde esa cuenta. Nunca un token de una cuenta personal o de administrador.
2. Acceso por proyecto: el usuario le da a la cuenta acceso al proyecto de pruebas y al del cliente al iniciar, y se lo quita al terminar.
3. El token vive solo como variable de entorno en la computadora del usuario. Nunca se escribe en archivos ni en el chat, y nunca se corren comandos que muestren variables de entorno (`env`, `printenv`, `echo $TABLEAU_PAT_SECRET`).
4. Si el usuario pega un token o una contraseña en el chat: no usarlo, pedirle que lo revoque y cree otro.
5. Las contraseñas de las fuentes de datos las captura siempre el usuario.
6. Si el usuario pide un acceso más amplio, advertir estos riesgos antes de seguir.

**Datos**
7. BINATSA ya autorizó leer los extractos de los libros de sus clientes para construir y validar; no se vuelve a preguntar, salvo que el `brief.md` del cliente diga lo contrario. Los libros se publican siempre con extracción ("Libros con extracción" en `referencias/datos.md`).
8. Explorar y validar con sumas y conteos (por día, segmento, canal o asesor), sin imprimir filas con datos de clientes finales. Si el caso de control exige ver registros: pedir confirmación, pocas filas y no guardarlas.
9. Muestra anonimizada = sin nombres, teléfonos, RFC, CURP, direcciones ni correos; contrato reemplazado por un código consecutivo.

**Tableau**
10. Nunca borrar libros, fuentes, extractos ni tareas de actualización, aunque la herramienta lo permita, salvo que el usuario lo pida en ese momento. En el servidor MCP, deshabilitar las herramientas de borrado.
11. Nunca modificar consultas ni fuentes; solo ocultar campos sin uso.
12. Producción se toca solo en el paso 8, con confirmación del usuario en ese momento.

## Tableau: cómo se trabaja
- **Publicar, verificar y registrar:** ver "Publicación" en `referencias/publicacion.md` (siempre sobre el libro existente, simular primero y revisar la contraseña incrustada después).
- **Edición web:** autoguarda como borrador y "Publicar" sobrescribe; no deja ajustar anchos arrastrando; las hojas ocultas se abren desde "Ir a hoja".
- **Herramientas** (probar cada una primero en el proyecto de pruebas): servidor MCP oficial (leer fuentes publicadas y consultar cifras agregadas); `tableauserverclient` (descargar y publicar); API de Hyper (leer extractos en local); navegador (la revisión visual, lo único que muestra el tablero tal como lo ve el usuario).
