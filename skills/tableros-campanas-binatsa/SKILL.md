---
name: tableros-campanas-binatsa
description: "Punto de partida para cualquier dashboard de Cobranza BINATSA en Tableau Cloud. Usar siempre primero cuando el usuario pida armar, crear, modificar, revisar o publicar un dashboard o tablero de cobranza en Tableau, o trabajar con un cliente de BINATSA: hace las preguntas iniciales, reúne los recursos y fija las reglas generales y el flujo. Después pasar a los módulos de datos, estructura, KPIs, tooltips, cliente/limpieza, publicación y video guía."
---

# Base · Dashboards de Cobranza BINATSA

Responde siempre en español, corto y directo. Quien usa este skill es del equipo de BINATSA; no asumir quién es.
Plantilla para cualquier cliente. Nada es específico de un proyecto; los datos de cada proyecto se preguntan al iniciar.

## Módulos relacionados
- `referencias/diseno.md`: Dirección, Operación, layout, estilo.
- `referencias/datos.md`: tablas, reglas de negocio, validación y seguridad; va ANTES de construir.
- `referencias/giros/cobranza.md`: tarjetas KPI y glosario.
- `referencias/tooltips.md`: descripciones emergentes.
- `referencias/cliente-limpieza.md`: vista del cliente y limpieza de huérfanos.
- `referencias/publicacion.md`: checklist, publicación y monitoreo.
- `referencias/video-guia.md`: video guía para un usuario nuevo; último paso, después de publicar.

## Recursos de BINATSA
- Repositorio de GitHub (público): Vuneit450/binatsa-tableros-skill. Solo lleva lo que sirve para cualquier campaña.
  - marca-binatsa/binatsa.svg: logo vectorial (turquesa #00B3B8, azul marino #0B1F3A). Usarlo siempre; si Tableau no acepta SVG en el objeto Imagen, generar un PNG desde el SVG.
  - marca-binatsa/paleta-binatsa.md y marca-binatsa/Preferences-BINATSA.tps: paleta de BINATSA (derivada del logo) y su versión para cargar en Tableau.
  - plantillas/: brief.md, diccionario-datos.md y paleta-cliente.md, vacías. Se copian a la carpeta privada del proyecto.
  - Si el repositorio no está conectado a la sesión, leerlo desde el navegador o pedir el archivo.
- Todo lo del cliente (logo, paleta, brief, reglas, libros, datos, capturas y video) vive en la carpeta privada del proyecto, `BINATSA-Tableros/<cliente>/<campaña>/`, y nunca se sube al repositorio.

## Preguntas obligatorias al iniciar un proyecto nuevo
Hacerlas con la herramienta de preguntas de opción múltiple si existe (en Claude Code, AskUserQuestion); si no, en texto con opciones numeradas. Cada tanda tiene máximo 4 preguntas, ofreciendo opciones concretas y una recomendada. No empezar a construir hasta tener las bloqueantes (1 a 4). Si el usuario ya las respondió en el chat, no repetirlas. Si la sesión es desatendida, elegir lo razonable, declararlo arriba y marcarlo "por confirmar".

Tanda 1 (bloqueantes, antes de construir):
1. Cliente y logo: nombre del cliente (va en el título "Cobranza <Cliente> · <Vista>") y logo. Su ícono va arriba a la izquierda del dashboard, junto al logo de BINATSA, y se usa también para sacar su paleta. Opciones del logo: "Lo subo ahora", "Ya está en la carpeta del cliente (marca/)", "No hay logo: usar solo texto con sus colores". Siempre confirmarlo, aunque ya exista en la carpeta.
2. Colores de marca del cliente: "Los paso (hex)", "Sácalos del logo", "Usa la paleta BINATSA por ahora". La paleta de encabezados, acentos y KPIs sale de aquí.
3. Fuente de datos: "Tabla/consulta existente", "Archivo (CSV/Excel)", "Aún no hay: usar datos de ejemplo". Confirmar campos disponibles: canales (llamadas, SMS, Mail, Blaster, WhatsApp, Visitas, Predictivo, Inbound), tipificaciones, asesor, zona, monto, promesas, pagos.
4. Vistas: Dirección y Operación son obligatorias y la Guía de uso es recomendada. Opciones: "Dirección, Operación y Guía de uso" (recomendada), "Agregar Seguimiento por asesor", "Otra vista (describirla)".

Tanda 2 (durante la construcción, no bloquea el arranque):
5. Segmentación de cartera del cliente (rangos de mora, nombres y días; no asumir A/B/C) y si el proyecto separa además por canal o producto.
6. Tarjetas KPI de Dirección y de Operación: "Las propuestas del skill" (recomendada, ajustadas al proyecto), "Las que defina el cliente", "Propongo yo según los campos disponibles".
7. Metas: las metas no son estándar. Preguntar siempre si el cliente tiene metas (por asesor, por día o por segmento) y cuáles: "No hay metas" o "Sí, las paso".

Tanda 3 (antes de publicar y de compartir con el cliente):
8. Workbook, proyecto y sitio de Tableau Cloud (publicar siempre sobre el workbook existente cuando ya hay uno).
9. Horario, frecuencia y zona horaria de actualización del extracto.
10. Canal de alertas de fallo de actualización: "Slack (¿cuál canal?)", "Correo", "Otro", "Sin alertas". Nunca asumir uno.
11. Quiénes tienen acceso. Por defecto el cliente ve las dos vistas (Dirección y Operación), con el desglose por asesor.

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

## Flujo de trabajo
1. Hacer la tanda 1 de preguntas. Si el usuario sube un .twbx, trabajar sobre ESE archivo (en copia versionada).
2. Revisar los datos y acordar las reglas de negocio (`referencias/datos.md`), con el primer acercamiento a los datos que describe ese módulo.
3. Construir, en este orden: estructura (vistas, encabezado, medidas y parámetros), KPIs (tarjetas y glosario), tooltips y Guía de uso. Hacer la tanda 2 de preguntas mientras se construye.
4. Cambios de XML (tooltips, campos ocultos): trabajar en copia versionada del .twbx (.twb + Data/Extracts/*.hyper + Image/), con nombre versionado; publica el usuario o la sesión según la sección anterior.
5. Cambios simples: edición web sin marcas seleccionadas y publicar sobre el mismo workbook.
6. Tanda 3 de preguntas, y limpieza de la vista del cliente (`referencias/cliente-limpieza.md`).
7. Para revisar dashboards publicados: usar el navegador (Claude in Chrome o el integrado con sesión del usuario); si pide contraseña, que el usuario inicie sesión.
8. Correr el checklist de publicación, incluida la prueba de interacción (la mayoría de los gráficos se comunican entre sí); verificar y reportar en 1-2 frases más la tabla de interacción.
9. Al terminar y publicar, hacer el video guía (`referencias/video-guia.md`): es el último paso de la entrega.
