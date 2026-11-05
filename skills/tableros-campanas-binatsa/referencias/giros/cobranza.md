# KPIs · Dashboards de Cobranza BINATSA

## Tarjetas KPI
- Todas las vistas llevan tarjetas KPI con dos deltas: "vs periodo previo" (mismo rango anterior) y "vs 7 días previos", con ▲ verde / ▼ rojo (invertir color cuando bajar es bueno, ej. Sin gestión). Los deltas siguen la selección: se calculan sobre el rango efectivo (ver Glosario) y sobre la misma selección de segmento, asesor, canal, hora, tipificación y zona en los dos periodos. Excepción: cuando el rango efectivo es de 7 días o menos, se oculta "vs 7 días previos" (coincide con el periodo previo o lo repite) y la tarjeta muestra solo "vs periodo previo". Con 8 días o más se muestran los dos.
- Cada tarjeta debe ayudar a decidir. Descartar métricas descriptivas sin acción (día de mayor volumen, franja más cargada, pico de personas, peso fin de semana, días con operación). Preferir cobertura, % contacto titular, promesas, % promesa, $ recuperado, pagos, sin gestión, intentos por cuenta.

## Anatomía de la tarjeta (propuesta, confirmar en la primera revisión de cada cliente)
Referencia visual: `ejemplos/tarjeta-kpi.png`.
De arriba hacia abajo. Todo va centrado excepto el título, que va a la izquierda:
1. Título de la tarjeta (nombre de la métrica): 13 pt en Tableau Semibold, a la izquierda, sobre una franja de color de marca (en su tono oscuro si hace falta contraste, texto blanco) con esquinas redondeadas. Subtítulo opcional de 10 pt dentro de la misma franja (definición corta o periodo), en un tono claro de la misma familia de color.
2. Número grande, centrado: 28 pt en Tableau Bold, en un tono del primario que llegue a 3:1 contra el fondo (en BINATSA, turquesa oscuro `#007F84`; el turquesa del logo no llega) o en color de semáforo si la tarjeta tiene meta. Formato de módulo estructura: % con símbolo y 1 decimal, dinero con $ y miles.
3. Dos deltas, centrados, en una línea o en dos: "▲ 4.2% vs periodo previo" y "▼ 1.1 pp vs 7 días previos", 10 pt, verde o rojo según sea mejor o peor. Con rango de 7 días o menos, solo el primero (ver Tarjetas KPI).
4. Solo el título lleva fondo (la franja) y esquinas redondeadas (radio propuesto: 12 px, ver "Esquinas redondeadas" en `referencias/diseno.md`). El número y los deltas van SIN borde ni fondo, transparentes, por lo que el radio de la hoja solo se nota en el título. Requiere Tableau 2026.1 o posterior.
5. Medidas: 271 x 190 px; el ancho se reparte en partes iguales (7 por fila en 1910 px); margen de 6 px y relleno de 6 px. Misma altura y ancho en toda la fila.

## Glosario de KPIs (definiciones estándar; confirmar con el cliente si difieren)
Este glosario es la fuente de las definiciones que se publican en la vista Guía de uso (`referencias/diseno.md`) y en los tooltips. Si cambia una definición, se cambia aquí primero.
Contacto, promesa y los demás resultados se identifican SIEMPRE por la tipificación que registra el historial de llamadas. Cada cliente nombra sus tipificaciones distinto: al iniciar, mapear cuáles cuentan como contacto con titular y cuáles como promesa, y confirmarlo con el usuario.
- Cuentas asignadas: cuentas en la base del periodo/segmento.
- Gestión / cuentas gestionadas: cuentas con al menos una gestión en el periodo. % gestión (o % cartera gestionada) = gestionadas ÷ asignadas. % sin gestión = 1 − % gestión.
- Intentos (de llamada): número de gestiones/llamadas realizadas. Intentos por cuenta gestionada = intentos ÷ cuentas gestionadas.
- Contacto con titular: gestiones cuya tipificación en el historial de llamadas indica que se habló con el titular. % contacto = contactos con titular ÷ gestiones totales del historial.
- Promesa de pago: gestiones cuya tipificación en el historial de llamadas es de promesa. % promesa = promesas ÷ contactos con titular. Monto prometido = suma del monto de las promesas.
- Pago / pagos recibidos: número de pagos aplicados. $ recuperado = suma de pagos aplicados en el periodo.
- Rango efectivo: el que define el parámetro Periodo; si Periodo es "Personalizado", el que definen [Desde] y [Hasta] (parámetros, no filtros; ver `referencias/diseno.md`). Si hay un día seleccionado en un gráfico, el rango efectivo es ese día. En Tableau, dos cálculos: [Desde efectivo] y [Hasta efectivo]. Las selecciones que no son de fecha (segmento, asesor, canal, hora, tipificación, zona) no cambian el rango: se aplican igual al periodo actual y al previo.
- Banderas de periodo (en Tableau, booleanas por fila): "En rango actual" = fecha entre [Desde efectivo] y [Hasta efectivo]; "En rango anterior" = fecha en el rango de la misma duración inmediatamente anterior; "En rango hace 7 días" = fecha entre [Desde efectivo] - 7 y [Hasta efectivo] - 7. Cada KPI se calcula una vez por periodo con IF bandera THEN medida END (por ejemplo, tres cálculos: actual, anterior y hace 7 días), y el delta compara esos cálculos.
- Sin periodo previo: cuando el periodo elegido no tiene un periodo previo con datos (por ejemplo "Todo el historial", o el primer periodo del que hay datos), los dos deltas muestran "-", nunca "+0.0 %".
- Periodo previo: rango inmediatamente anterior de la misma duración que el rango efectivo.
- 7 días previos: el mismo rango desplazado 7 días atrás. Solo se calcula y se muestra si el rango efectivo dura más de 7 días; en Tableau, ocultar el delta con un cálculo que devuelva vacío cuando DATEDIFF('day', [Desde efectivo], [Hasta efectivo]) + 1 <= 7 (con un día seleccionado dura 1 día, así que ese delta se oculta).
- Delta: variación relativa en % contra la referencia; para métricas que ya son porcentaje, diferencia en puntos porcentuales (pp).
- Documentar siempre la definición real usada en el tooltip "Cómo se calcula" y avisar al usuario si el cliente la define distinto.
