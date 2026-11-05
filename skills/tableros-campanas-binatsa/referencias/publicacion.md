# Publicación y monitoreo · Dashboards de Cobranza BINATSA

## Checklist antes de publicar
- [ ] Sin marcas seleccionadas y parámetros en su valor por defecto (en web quedan guardados en el borrador).
- [ ] Controles por defecto correctos (segmento como filtro; Desde y Hasta como parámetros de fecha).
- [ ] Todos los % con símbolo; dinero con $ y miles.
- [ ] Tooltips completos en todas las hojas, con las cinco secciones.
- [ ] Ningún texto visible menciona servidores, tablas, Excel ni sistemas internos.
- [ ] Tarjetas KPI con los dos deltas y color de ▲▼ correcto (con rango de 7 días o menos, solo "vs periodo previo"; probar con un rango corto y uno largo).
- [ ] Título principal de 20 pt en negrita, blanco sobre franja, con el formato "Cobranza <Cliente> · <Vista>" y su subtítulo; títulos de bloque de 13 pt con subtítulo de 10 pt; medidas de la sección "Medidas estándar" respetadas.
- [ ] Botones de navegación funcionan y cumplen el formato (164 x 36 px, "Ir a <Vista> →", color por destino con texto blanco a 4.5:1, "📖 Glosario" en gris); ícono del cliente a la izquierda y logo de BINATSA a la derecha, en la misma posición en todas las vistas.
- [ ] Información sin bordes ni fondos (todo transparente; solo los títulos y los botones de navegación pueden llevarlos); mosaico.
- [ ] Todo centrado, menos los títulos (de gráficos, de tablas y encabezados de zona), a la izquierda.
- [ ] Ningún gráfico con líneas de fondo ni con el título del segundo eje; los valores se leen por etiquetas, sin etiqueta en los valores 0 o nulos de los gráficos y con "-" en las celdas 0 o nulas de las tablas.
- [ ] Tamaño: modo Fijo, 1910 x 1300 px en todas las vistas.
- [ ] Prueba de interacción hecha (ver sección siguiente) y reportada.
- [ ] Cifras cuadradas contra la fuente en al menos un caso de control.
- [ ] Publicar sobre el workbook existente; credenciales incrustadas (las pone el usuario desde Desktop).
- [ ] Después de publicar: vistas, fuentes, hora de Modificado y actualización de extracción OK.
- [ ] Dashboard publicado y probado: hacer el video guía (`referencias/video-guia.md`), último paso de la entrega.

## Prueba de interacción (obligatoria)
La mayoría de los gráficos deben interactuar entre sí; cuáles quedan fuera depende del proyecto. No darlo por hecho: probarlo en el dashboard abierto en el navegador, en todas las vistas (como mínimo Dirección y Operación).
1. Hacer una lista de las hojas visibles del dashboard (gráficos, tablas y tarjetas KPI).
2. Por cada gráfico, hacer clic en una marca y comprobar qué hojas se actualizan, incluidas las tarjetas KPI. En las tarjetas comprobar que el valor y los deltas siguen la selección (con un día seleccionado, el delta de 7 días se oculta). Anotar cuáles no respondieron.
3. Limpiar la selección (clic fuera de las marcas) y comprobar que todo vuelve al estado inicial.
4. Corregir lo que no responda (dimensión de enlace faltante, acción mal configurada) y repetir desde el paso 2.
5. Reportar al usuario en una tabla corta: hoja, ¿filtra a las demás?, ¿responde a las demás?. Declarar cuáles no interactúan y por qué; deben ser la minoría. Si son muchas, revisar antes de publicar.
6. Dejar el dashboard sin marcas seleccionadas antes de publicar.

## Publicación
- Publicar SOBRE el workbook existente (mismo nombre y proyecto) para conservar programación y credenciales; con otro nombre se pierde la programación.
- La contraseña incrustada solo se fija publicando desde Desktop con "Incrustar contraseña" (en web no hay campo). Las credenciales las captura siempre el usuario.

## Mantenimiento después de la entrega
1. Todo cambio pedido por el cliente se hace en una copia versionada del libro, nunca directo sobre el publicado.
2. Probar con el checklist antes de publicar, y publicar sobre el workbook existente.
3. Registrar el cambio: fecha, qué cambió y quién lo pidió.
4. Si cambia la definición de una métrica o una regla de negocio, actualizar a la vez el glosario, la Guía de uso y los tooltips, y repetir el caso de control (`referencias/datos.md`).
5. Si el cambio afecta lo que muestra el video guía, rehacer las escenas afectadas y entregar una versión nueva (`referencias/video-guia.md`).

## Monitoreo de actualización
- Revisar en la pestaña Actualizaciones de la extracción del workbook: estado, hora de la última corrida y programación activa.
- Tras cada publicación, verificar que la programación sigue vigente y lanzar "Ejecutar ahora" para confirmar que corre sin error.
- Causas típicas de fallo: contraseña no incrustada (fallo en "Insertado"), credenciales vencidas, cambio en la fuente. 5 fallos seguidos suspenden la programación.
- Alertas: ofrecer automatizar el aviso al canal que el usuario elija (correo de Tableau al correo del canal de Slack u otro) y una tarea programada de revisión si lo pide; si se crea, usar las herramientas de tareas programadas, no cron local.
