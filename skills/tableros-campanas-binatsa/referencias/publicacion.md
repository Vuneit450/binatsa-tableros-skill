# Publicación y monitoreo · Tableros de campañas BINATSA

Las reglas de diseño están en `referencias/diseno.md`; aquí solo se verifican.

## Checklist antes de publicar
**Estado**
- [ ] Sin marcas seleccionadas; parámetros en su valor por defecto (en edición web quedan guardados en el borrador).
- [ ] Tamaño fijo, 2300 x 1300 px, en todas las vistas.

**Encabezado y botones**
- [ ] Título "<Campaña> · <Vista>" y subtítulo "<Cliente> · <pregunta>"; logo del cliente a la izquierda y de BINATSA a la derecha, igual en todas las vistas.
- [ ] Botones "<Vista> →" que funcionan, con color por destino (texto blanco a 4.5:1), y "📖 Guía y glosario".
- [ ] "▶ Manual en video" con el enlace real al video de este tablero (no el marcador).
- [ ] Línea ℹ️ junto a los botones.

**Vistas**
- [ ] Dirección, Operación y Guía y glosario presentes (más las del giro que se acordaron).
- [ ] Dirección con el mapa de calor y su selector KPI; Operación con sus cinco hojas obligatorias.

**Tarjetas**
- [ ] 6 por fila, hasta 2 filas.
- [ ] Deltas correctos: "-" sin periodo para comparar; "0.0" en gris cuando no hay cambio; ▲▼ con el semáforo oscuro e invertidos cuando bajar es bueno.
- [ ] "vs 7 días previos" oculto con rangos de 7 días o menos. Probado con un rango corto y uno largo.

**Estilo**
- [ ] Sin ejes ni títulos de ejes; ceros vacíos en gráficos y "-" en tablas.
- [ ] Tablas centradas y con totales.
- [ ] Categorías (canales, segmentos) con la paleta del cliente, iguales en todas las hojas.
- [ ] Asesores por nombre, nunca por login o ID.
- [ ] Todo % con símbolo; dinero con $ y miles.

**Textos**
- [ ] Tooltips de 5 secciones en todas las hojas visibles.
- [ ] Ningún texto visible usa palabras de la lista única ("Texto visible" en `referencias/diseno.md`).
- [ ] Ningún marcador sin llenar: buscar `{` en títulos, tooltips y Guía y glosario (`{Campaña}`, `{Cliente}`, `{Fuente 1}`, etc.).

**Datos**
- [ ] Todas las fuentes con extracción (no en vivo) y actualización programada, para que el libro descargado traiga datos.
- [ ] Caso de control cuadrado contra la fuente (`referencias/datos.md`).
- [ ] Prueba de interacción hecha y reportada (sección siguiente).

## Prueba de interacción (obligatoria)
Probarla en el tablero abierto en el navegador, en todas las vistas. No darla por hecha.
1. Hacer la lista de hojas visibles de la vista (gráficos, tablas y tarjetas).
2. **Clic:** en cada gráfico, hacer clic en una marca y anotar qué hojas se actualizan, incluidas las tarjetas (su valor y sus deltas deben seguir la selección).
3. **Clic en un día:** los gráficos se filtran; las tarjetas no cambian (o, si se activó "Día seleccionado", muestran ese día y ocultan el delta de 7 días).
4. **Clic en la categoría principal** (segmento o canal): además del filtro, cambia el parámetro de arriba.
5. **Pasar el mouse:** los datos hermanos se iluminan en todas las hojas que tienen el campo; las tarjetas no se apagan.
6. **Limpiar** (otro clic o clic fuera): todo vuelve al estado inicial.
7. Corregir lo que no responda (campo de enlace faltante o acción mal configurada) y repetir.
8. Reportar al usuario en una tabla corta: hoja, ¿filtra a las demás?, ¿responde a las demás? Declarar cuáles no interactúan y por qué; deben ser la minoría.
9. Dejar el tablero sin marcas seleccionadas.

## Publicación
- **Siempre sobre el libro existente** (mismo nombre y proyecto), para conservar la programación y las credenciales. Con otro nombre se pierde la programación.
- **Quién publica:** la sesión, con `herramientas/publicar_libro.py`. Primero sin `--publicar` (simula y dice si crearía o sobrescribiría), después con `--publicar`. Fuera del proyecto de pruebas exige `--confirmo-produccion` y la confirmación del usuario en ese momento. Si no hay token, publica el usuario desde Tableau.
- **Contraseña de la fuente:** solo se incrusta desde Tableau Desktop con "Incrustar contraseña", y la captura siempre el usuario. Después de publicar por API, revisar en la pestaña Conexiones que siga incrustada; si se perdió, el usuario la vuelve a incrustar desde Desktop.
- **Registro:** anotar en `brief.md` la fecha, el archivo, el proyecto y qué cambió.
- **Después de publicar:** revisar vistas, fuentes, hora de "Modificado" y que la actualización corra ("Ejecutar ahora").

## Mantenimiento después de la entrega
1. Todo cambio se hace en una copia versionada del libro, nunca directo sobre el publicado.
2. Pasar el checklist y la prueba de interacción antes de publicar.
3. Registrar el cambio en `brief.md`: fecha, qué cambió y quién lo pidió.
4. Si cambia una métrica o una regla de negocio, actualizar a la vez el giro (`referencias/giros/<giro>.md`), la Guía y glosario y los tooltips, y repetir el caso de control.
5. Si el cambio afecta lo que muestra el video guía, rehacer las escenas afectadas, entregar una versión nueva y actualizar el enlace "▶ Manual en video" (`referencias/video-guia.md`).

## Monitoreo de la actualización
- Revisar en la pestaña de actualizaciones del libro: estado, hora de la última corrida y programación activa.
- Causas típicas de fallo: contraseña no incrustada, credenciales vencidas o un cambio en la fuente. Cinco fallos seguidos suspenden la programación.
- Alertas: ofrecer automatizar el aviso al canal que eligió el usuario (por ejemplo, el correo de Tableau reenviado al canal de Slack) y una revisión programada si la pide; si se crea, usar las herramientas de tareas programadas, no cron local.
