# Video guía · Tableros de campañas BINATSA

## Qué es y cuándo se hace
Último paso del flujo, cuando el tablero ya está publicado y probado (`referencias/publicacion.md`). Es un video que enseña a una persona nueva a usar el tablero: qué es, qué hay en cada vista, dónde se filtra, qué afecta cada filtro y qué pasa al hacer clic o pasar el mouse. Cada tablero tiene su propio video. El tiempo de producción no importa; importa que quede bien explicado y que se vea de primer nivel.

## Decisiones fijas de BINATSA
- **Dónde vive:** en el repositorio de videos de BINATSA (el mismo de los demás manuales), servido como página web. Es público: cualquiera con el enlace lo ve. Por decisión de BINATSA se graba con el tablero real tal cual; aun así, nunca deben aparecer otros clientes, notas internas, logins ni palabras de la lista prohibida.
- **Peso máximo: 100 MB por archivo** (límite del repositorio). Todo lo demás está permitido.
- **Con voz sintética** (ver Audio). **Sin límite de duración**, siempre dentro de los 100 MB.
- Al publicarlo, poner su enlace en "▶ Manual en video" del tablero y volver a publicar el tablero.

## Preguntas iniciales
Con las reglas de preguntas de `SKILL.md`:
1. Formato: "Horizontal 16:9 (recomendado)", "Vertical 9:16 para redes" o "Los dos".
2. Imágenes: "Las tomo con código del tablero abierto en el navegador (HD)" (recomendada), "Te paso las capturas" o "No hay acceso: réplica dibujada con código (se avisa)".
3. Qué cubre: "Todas las vistas" (recomendada) o una lista.
4. La ficha de variables (sección siguiente), con una propuesta para cada una.

## ADN del video (igual en todos)
Lo que hace que se reconozca como un video BINATSA:
- **Una sola cámara, un solo viaje.** Sin cortes de montaje: cada cambio de escena se explica con movimiento (seguir la línea, acercarse a un botón, atravesar una vista).
- **El hilo de luz BINATSA:** una línea turquesa (`#00B3B8` con núcleo brillante y halo suave) recorre el tablero, enciende lo que se explica y lleva a la siguiente vista. Es la firma visual.
- **Tres energías que se alternan:** explosiva (gancho e impactos), fluida (recorridos) y contemplativa (cuando hay que leer un número). Nunca la misma intensidad todo el tiempo.
- **Movimiento con intención:** nada importante aparece o desaparece solo con transparencia; todo entra con una acción. Nada de movimiento lineal ni de velocidad constante: anticipación, aceleración y aterrizaje.
- **Microanimaciones discretas:** el botón se hunde al presionarlo, la tarjeta vibra un poco al aterrizar, el número cuenta hasta su valor. No todo rebota.
- **Prohibido:** flashes, sacudidas constantes, destellos repetidos, partículas al azar, glow excesivo, textos deformados y transiciones genéricas.
- **Seguridad:** nada parpadea más de 3 veces por segundo.
- **Claridad antes que espectáculo:** si un efecto estorba la lectura, se quita.

## Ficha de variables (cambia en cada video)
Se llena por tablero, se registra en `video/guion.md` y el usuario la aprueba antes de producir. Con dos o tres variables distintas ya se siente otro video, con el mismo estilo.
| # | Variable | Ejemplo |
|---|---|---|
| 1 | Identidad del cliente | Su logo y su paleta; fondo muy oscuro derivado de su color |
| 2 | Metáfora del giro (qué "viaja" la línea) | Cobranza: cuenta → contacto → promesa → pago, y la línea llena la barra de recuperación. ATC: la llamada entra → espera → se atiende → se resuelve |
| 3 | Gancho | Una pregunta del banco: "¿Sabes qué asesor necesita apoyo hoy?", "¿A qué hora contestan tus clientes?" |
| 4 | Momento héroe | El hallazgo más fuerte de ese tablero: el mapa de calor que se enciende, el ranking que sube, el contador de $ recuperado |
| 5 | Recorrido | Las vistas reales de ese tablero y su orden |
| 6 | Luz por vista | La iluminación toma el color del botón de cada vista (Dirección = primario, Operación = secundario…) |
| 7 | Música | Misma instrumentación y carácter; cambian el tempo (90-110 BPM) y la tonalidad |
| 8 | Frase final | Una línea por cliente antes del cierre fijo (por ejemplo "Un solo tablero. Todas tus respuestas.") |
| 9 | Semilla visual | Un número que decide la trayectoria exacta de la cámara, la línea y los detalles; otra semilla, otro recorrido |

## Estructura estándar
1. **Gancho** (variable 3), con energía explosiva. 5 a 6 s.
2. **Mapa de las vistas:** qué pregunta responde cada una, con sus botones "<Vista> →", "📖 Guía y glosario" y "▶ Manual en video".
3. **Lo común, una sola vez:** filtros y qué afectan (demostrando el cambio), cómo se leen las tarjetas, pasar el mouse (los datos hermanos se iluminan), clic (filtra la vista; clic en un día) y selectores.
4. **Recorrido por vista:** una sección por cada vista del tablero (Dirección, Operación, Asesores, las del giro), no por cada hoja oculta. Cada sección con su tarjeta de título y solo lo propio de esa vista. Aquí va el momento héroe (variable 4).
5. **¿Dudas?:** la Guía y glosario.
6. **Las 5 reglas,** a modo de resumen, y la frase final (variable 8).
7. **Cierre fijo de BINATSA.**
Al terminar, entregar la lista de capítulos con su minuto, una por vista.

## Guion base de lo común
- Filtros: decir dónde están y qué opciones hay (Periodo; Desde y Hasta, que solo cuentan con "Personalizado"; y el control del giro), y siempre qué afectan ("afectan todo el tablero: tarjetas, mapas, gráficas y tablas").
- Demostración de cada control: se cambia en pantalla y se muestra el estado de antes y el de después, resaltando lo que cambió. Los dos estados son capturas reales; no se inventan cifras. Un solo cambio por control.
- Tarjetas: número grande = el periodo elegido; ▲ verde mejora, ▼ rojo empeora; "pp" = puntos porcentuales; "-" = no hay periodo para comparar; comparación contra el periodo previo y contra 7 días antes (con rangos de 7 días o menos, solo la primera).
- Pasar el mouse: lo que comparte el dato (el mismo canal o asesor) se ilumina en todas las gráficas.
- Tooltip: mostrar uno largo a pantalla completa, con datos de un caso, recorriendo sus cinco secciones.
- Clic ("regla de oro"): un clic en una marca filtra el resto de la vista; otro clic lo quita.
- Selectores (por ejemplo KPI o Métrica): cambian la gráfica.
- Las 5 reglas: 1) los filtros de arriba afectan todo; 2) clic en una gráfica filtra el resto; 3) otro clic quita el filtro; 4) pasa el mouse y te explica; 5) los selectores cambian la gráfica. Añadir la frecuencia de actualización solo si es cierta.
- Para cada vista: la pregunta de negocio que responde, qué hay en ella y qué hace un clic ahí. Lo deducido por el nombre de un botón se marca "por confirmar" en el reporte.

## Estilo
- Cuerpo del video con la identidad del cliente: sus colores, su ícono y los colores reales de las gráficas del tablero. El cierre es siempre de BINATSA.
- Textos grandes que entran palabra por palabra, emojis, marcos que resaltan lo explicado, cursor con onda al hacer clic, listas desplegables que se abren solas, un chip con el nombre de la escena y una barra de progreso.
- Tipografías de licencia abierta (por ejemplo Anton y Space Grotesk; confirmar su licencia) o las del cliente.
- Texto: en una franja angosta debajo de la captura, nunca encima del tablero; siempre completo y con contraste de al menos 4.5:1. En vertical, dejar libre alrededor del 10 % arriba y del 18 % abajo (controles de las apps de redes).
- Cámara: encuadra siempre lo que se explica, con esta prioridad: lista desplegable o tooltip, luego elemento resaltado, luego cursor.

## Composición del cuadro (16:9, 1920 x 1080)
Medidas de un lienzo de 1920 x 1080 que se dibuja en 3840 x 2160 y se reduce a la mitad. Para vertical (9:16) se recalculan con el mismo principio. El tablero se mide en un lienzo propio de 960 unidades de ancho; si el motor usa otra base, escalar en proporción.

Principio: la captura del tablero es la protagonista. El marco es lo más grande posible y es el mismo en todas las escenas. El texto va en una franja delgada abajo; para ir más grande habría que poner el texto encima de la captura, y eso no se hace.

### Marco estándar (idéntico en todas las escenas)
- Posición: a 128 px del borde izquierdo y 8 del superior.
- Tamaño: 1664 px de ancho por 976 de alto. Sale de ancho = 1.6 x 1040 y alto = 1.6 x 610, donde 610 es el alto de la cámara. Es el máximo que deja espacio para la franja inferior.
- Se usa igual en la escena de arranque. El marco no se agranda ni se achica según la vista.

### Franja de texto (escenas guiadas)
- Una sola fila abajo: a 60 px del borde izquierdo y 994 del superior, de 1800 px de ancho.
- En este orden: etiqueta de capítulo (que no se corte en dos líneas), título de 40 px en una línea sin cortes, y frase de apoyo de 28 px.
- Burbuja de estado (por ejemplo "Un asesor"): a la derecha, a 1560 px del borde izquierdo y 996 del superior, con letra de 30 px.
- La barra de progreso va al fondo.

### Escena de arranque
- Mismo marco que las demás escenas. Cada vista se escala al ancho del marco y se centra en vertical. Sin zoom lento que recorte las orillas.
- Franja de abajo:
  - Etiqueta "Guía rápida" y título de 46 px en una fila: a 60 px del borde izquierdo y 996 del superior.
  - Los selectores de las vistas (Dirección, Operación y las demás del proyecto), a la derecha con escala 0.62: a 1180 px del borde izquierdo y 1000 del superior.
  - Logo de BINATSA en la esquina: a 1660 px del borde izquierdo y 992 del superior, en un recuadro de 210 x 66.
- No llevan frase de apoyo ni etiqueta de la vista activa, para que quepa todo.

### Cámara
- Ancho visible mínimo: 400 unidades del tablero (que mide 960). Con el marco grande da unas 4 veces de zoom.
- Ancho visible = el mayor de: ancho del círculo de resalte x 1.12; alto del círculo x 1.12 x (1040 / alto del recuadro de cámara); y 400.
- Los planos generales solo se usan al abrir una escena (t = 0), a 960 unidades.
- Los círculos y el zoom usan las posiciones medidas del propio tablero.

### Elementos anchos: un solo paso, sin repetir
- Si el elemento enfocado mide más de 340 unidades de ancho, se enfoca UNA sola vez con un barrido continuo de izquierda a derecha. El ancho visible durante el barrido es de 440 unidades.
- No se parte en varios pasos.
- En la configuración de cada paso se guardan la vista inicial y la final. La cámara va de una a otra desde el final de la transición hasta 0.15 s antes del siguiente paso, con aceleración suave. El paso siguiente arranca desde la vista final.

### Regla para no repetir gráficos
- Cada elemento se resalta con círculo una sola vez por escena.
- En el plano de apertura (t = 0) se quita el círculo si ese mismo elemento se resalta después.
- Se conservan a propósito dos repeticiones: el segundo clic que quita un filtro, y el mismo gráfico mostrado después de que cambió la métrica o el filtro.

## Imágenes y datos
- Capturas reales del tablero, hechas con código para que sean HD: un navegador automatizado abre el tablero (la persona inicia sesión; las credenciales nunca se escriben) y captura con un factor de escala de 2 o más, para poder acercar sin que se pixelen. Cada vista se captura completa, y las zonas que se acercan, a mayor resolución.
- Réplica dibujada con código solo si no hay acceso al tablero, y avisarlo: se ve menos real. Debe usar los mismos colores y el mismo estilo del tablero real.
- El tablero mide 2300 x 1300 px (proporción cercana a 1.77:1, casi la del video 16:9). El plano general de apertura lo muestra completo y después la cámara lo recorre por zonas (ver "Composición del cuadro").
- Para cada segmentador que se demuestra, capturar el tablero en el estado de antes y en el de después de un solo cambio.
- No inventar cifras: lo que no se lee en la captura no se rellena. Si un dato solo existe para un día, decirlo en pantalla.

## Audio
**Voz (siempre):** síntesis de alta calidad (por ejemplo ElevenLabs o equivalente). Voz femenina, joven y optimista, español latinoamericano natural, con sonrisa perceptible; sin tono robótico ni entonación publicitaria forzada. Grabar el guion como una sola interpretación continua, hacer dos o tres tomas y elegir la más natural; no acelerar la voz.
**Música:** original, generada por código (sin derechos de autor); moderna, optimista y rítmica, sin ser infantil. Instrumentación base: marimba, percusión melódica, teclados suaves, subgrave redondo, bombo, palmas y shaker. Tempo y tonalidad según la ficha (variable 7). Los impactos coinciden con momentos musicales.
**Efectos:** propios, organizados por familia (movimiento, materiales, energía, interfaz), con jerarquía: los momentos importantes resaltan porque los secundarios son discretos.
**Mezcla:** voz siempre inteligible; música al menos 12 dB por debajo de la voz mientras se habla; integrado final −14 LUFS; pico real máximo −1 dBTP; revisar en mono y en altavoces de teléfono. Escuchar el audio completo antes de entregar.
**MP4:** la música empieza desde el inicio. Reproductor web: arranca en silencio con un botón de sonido visible.

## Reglas de contenido
- Hablar a un usuario nuevo: frases cortas, una idea por plano, y siempre decir qué afecta cada filtro o clic.
- Texto visible: aplicar la lista única de palabras prohibidas ("Texto visible" en `referencias/diseno.md`), incluidos los textos en pantalla y las capturas. Decir "los datos se actualizan solos".
- No presentar dos veces lo mismo; si ya se mostró un tooltip, no repetirlo.
- Las capturas pueden traer palabras prohibidas en los botones o los títulos del tablero: recortarlas, difuminarlas o taparlas.

## Cierre fijo (siempre es lo último)
Mínimo 4 s. Referencia visual: `marca-binatsa/cierre-video.png`.
- Fondo en degradado azul petróleo oscuro, de `#0E3C4F` (arriba a la izquierda) a `#0B222F`.
- Tarjeta blanca centrada, de esquinas muy redondeadas y de unos dos tercios del ancho, con el logo de BINATSA (`marca-binatsa/binatsa.svg`, colores `#00B3B8` y `#0B1F3A`), dibujado con código para que se vea nítido.
- Debajo, "Soluciones para tu emprendimiento." en gris claro `#C0C7CC` y, más grande (unas 1.8 veces), "Datos que mueven decisiones" en negrita `#1AA6C8`.
- En vertical, el mismo cierre recompuesto en el lienzo 9:16, sin cambiar textos ni colores.

## Verificación antes de entregar
1. Guion aprobado por el usuario antes de renderizar: lista de escenas con su duración y su texto en pantalla.
2. Prueba automática de encuadres: cada 0.2 s, nada cortado ni tapado por el recuadro de texto.
3. Búsqueda automática de palabras prohibidas en el guion, más revisión visual de las capturas.
4. Ver el video completo en el reproductor, no solo cuadros sueltos; si es vertical, verlo en un teléfono.
5. Renderizar un cuadro a 3840 x 2160 y reducirlo a 1600 x 900. Comprobar tres cosas: que ningún texto se encima con la franja, que el círculo de resalte queda dentro del marco y que los cuadros a mitad de un barrido se ven fluidos. Esta prueba detecta, por ejemplo, un zoom exagerado, una franja cortada o una etiqueta de capítulo partida en dos líneas.
6. Escuchar el audio completo.
7. Privacidad: ningún nombre de otro cliente, nota interna, login ni palabra de la lista prohibida en las capturas (el video es público).
8. Peso: el MP4 pesa menos de 100 MB.
9. Control artístico: calificar cada escena del 1 al 10 en composición, movimiento, luz, narrativa y satisfacción; rehacer lo que tenga menos de 9 en un criterio importante, registrando el defecto y la corrección. No calificar sin ver el resultado real.
10. Reportar al usuario en pocas líneas: duración, peso, formato, vistas cubiertas, vistas sin cubrir y descripciones por confirmar.

## Entregables
- Nombre: `video-guia-<cliente>-v<N>.mp4`, con un registro de qué cambió en cada versión.
- Lista de capítulos con su minuto (una por vista).
- Opcional: versión corta de 60 s y guía escrita con las mismas 5 reglas.
- Código fuente del video (guion, motor y audio) guardado en un lugar seguro y privado: sin él, cambiar un texto obliga a rehacerlo todo.
- Dónde se guardan: en la carpeta del cliente, dentro de `video/`: `motor/` (el código), `versiones/` (los MP4, uno por versión), `guion.md` (escenas, duración y texto en pantalla) y `capitulos.md`. La sesión los guarda ahí en cada versión, SOLO si está conectada a esa carpeta y con permiso de escribir en ella.
- Si la sesión no tiene acceso a la carpeta (por ejemplo corre en la nube), no se guarda nada solo: entregar los archivos como adjuntos y avisar al usuario, en la misma respuesta, que no quedaron guardados y que debe copiarlos él, sobre todo el motor.
- El MP4 final va al repositorio de videos de BINATSA (decisión fija). El motor, el guion y las capturas nunca van ahí ni al repositorio de la skill: se quedan en `video/` de la carpeta privada.
- Al publicarlo, poner su enlace en "▶ Manual en video" del tablero.

## Producción (referencia)
Todo se dibuja como función del tiempo. Pasos: ajustar el guion y la ficha, generar la voz y fijar sus anclas de tiempo, sacar los instantes de cortes y clics para sincronizar el sonido, generar la música y los efectos, correr la prueba de encuadres, renderizar los cuadros en paralelo y unir cuadros y audio con ffmpeg.
- **Formato:** 1920 x 1080 (o 1080 x 1920 en vertical) a 30 fps; a 60 fps se necesita el doble de peso para la misma calidad.
- **Peso dentro de 100 MB:** codificar en H.264 a dos pasadas con una tasa de video ≈ 760 Mbit ÷ duración en segundos − 0.16 Mbit/s del audio (AAC 160 kbps). Por ejemplo, 2 min ≈ 6 Mbit/s y 3 min ≈ 4 Mbit/s. Comprobar el peso del archivo final.
- Cada escena dura un número exacto de compases (1 compás = 4 × 60 ÷ BPM segundos).
- Si solo cambia la música, no hace falta renderizar de nuevo: se mezcla el audio nuevo con el video existente. Si cambia la duración de una escena, hay que regenerar audio y cuadros.
- No usar `pkill -f` con un texto que aparezca en el propio comando: puede matar el shell.
