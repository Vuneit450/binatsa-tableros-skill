# KPIs · Dashboards de Cobranza BINATSA

## Tarjetas de Cobranza
Formato y reglas de los deltas: "Tarjetas KPI" en `referencias/diseno.md`.
- Preferir métricas que ayuden a decidir: cobertura, % contacto con titular, promesas, % promesa, $ recuperado, pagos, sin gestión, intentos por cuenta.
- Descartar métricas descriptivas sin acción: día de mayor volumen, franja más cargada, pico de personas, peso del fin de semana, días con operación.

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
