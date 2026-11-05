# Datos · Dashboards de Cobranza BINATSA

Responde siempre en español, corto y directo. Este módulo va ANTES de construir: sin datos completos y reglas acordadas por escrito, las cifras no cuadran.

## Principio
Pedir los datos a detalle (un registro por evento) con el número de contrato como llave común, en formato texto. Los porcentajes y las razones NO se piden: se calculan a partir del detalle. Las reglas que hoy viven dentro de consultas o fórmulas de un archivo se acuerdan por escrito, para que la fuente nueva dé las mismas cifras.

## Primer acercamiento a los datos
Para que la sesión conozca los datos antes de construir, en la carpeta del cliente (ver "Trabajo con una carpeta local" en `SKILL.md`):
1. El libro actual en `.twbx`: de su `.twb` se leen los campos, los cálculos y los parámetros, y de sus extractos `.hyper` se pueden leer los datos de forma local (por ejemplo con la API de Hyper de Tableau para Python).
2. Un diccionario de datos: por cada tabla, sus campos con tipo y significado, más las reglas de negocio acordadas (sección siguiente).
3. Si no hay extracto, una muestra pequeña anonimizada en CSV por tabla (por ejemplo una semana), con la misma estructura que las tablas mínimas.
4. Con eso se calcula por código el caso de control (ver "Validación de cifras") y se compara con lo que muestra el dashboard publicado.
Los datos reales se quedan en la carpeta local y nunca se suben al repositorio.

## Tablas mínimas
| # | Tabla | Nivel de detalle | Campos mínimos |
|---|---|---|---|
| 1 | Cartera / asignación | Una foto por cuenta por día | Fecha de corte, contrato, identificador de la solicitud, estatus de la cuenta, días de mora, fecha de asignación, saldos (vencido y actual), cola o campaña, tipo de producto, segmento |
| 2 | Gestiones | Un registro por intento o acción | Contrato, fecha y hora, ID de agente, tipo de marcación o canal (Preview, Predictivo, Inbound, WhatsApp…), medio, resultado de la gestión (tipificación), con quién hubo contacto, monto y fecha de promesa, estatus, segmento |
| 3 | Promesas | Una por promesa | Cuenta, fecha de captura, fecha compromiso, monto, empleado, campaña o canal |
| 4 | Pagos | Uno por pago | Folio, contrato, estatus, días de mora, canal, proveedor, monto, fecha de pago, fecha de posteo, tipo de pago, cola, segmento |
| 5 | Inbound / telefonía | Una por llamada entrante | Contrato o teléfono, fecha y hora, atendida o abandonada, tiempo de espera, agente, resultado |
| 6 | Envíos masivos | Uno por envío | Contrato, fecha y hora, canal (SMS, Email, Blaster, WhatsApp, Carteo), estatus de entrega; para WhatsApp, también los chats recibidos (contrato, fecha y hora de la respuesta y agente que atendió) |
| 7 | Visitas | Una por visita o evento | Contrato, fecha, resultado y, si aplica, promesa y evento de recuperación de bien |
| 8 | Headcount y calidad | Por día y por monitoreo | Personal disponible y capacidad por día; por monitoreo: agente, tipo, calificación y quejas |
| 9 | Catálogos | Tablas de referencia | Rangos de segmento, qué resultado cuenta como conectado, contacto con titular (RPC) o promesa, canales de inbound, calendario de días hábiles y festivos y, si el proyecto las tiene, metas |
No todas aplican a todos los proyectos: confirmar con el usuario cuáles cubre el cliente, pero pedir las que existan desde la primera carga.

## Indicadores que salen de esos datos
Por día y por segmento de cartera, según canal: cuentas asignadas, trabajadas y conectadas; intentos; contactos con titular (RPC); promesas tomadas y cumplidas; llamadas recibidas, abandonadas y contestadas dentro del tiempo objetivo; envíos y respuestas por canal (SMS, Email, Blaster, WhatsApp, cartas, recados); visitas; pagos y monto recuperado; personal y calidad. Definiciones: `referencias/giros/cobranza.md`.

## Reglas de negocio por acordar (por escrito, antes de construir)
1. Rangos de cada segmento: límites oficiales y si hay segmentos adicionales. Si distintas fuentes los escriben distinto, elegir uno.
2. Filtros de cartera: qué cuentas se excluyen (por estatus, por producto o por segmento) y confirmar que siguen vigentes.
3. Cuenta trabajada única: contrato más día, y qué canales cuentan.
4. Conectado y contacto con titular: qué resultado (tipificación) cuenta como cada uno; vive en el catálogo.
5. Contacto con titular total: si es la suma de salientes y entrantes.
6. Promesa cumplida: ventana de días en que se busca el pago desde la fecha de la promesa, y si cuenta el pago parcial.
7. Atribución de llamadas entrantes a un envío previo (SMS, email, etc.): regla y días de ventana.
8. Días laborables: qué días cuentan como hábiles y cómo se tratan los festivos.
9. Monto recuperado: por fecha de pago o por fecha de posteo.
Cada regla acordada se documenta en el glosario (`referencias/giros/cobranza.md`) y en el tooltip "Cómo se calcula".

## Carga y formato
- Carga diaria, completa y sin intervención manual, con una hora de corte acordada antes del envío al cliente.
- Histórico mínimo: el mes en curso más el mes anterior, para comparativos.
- Sin fechas escritas a mano: las consultas toman el periodo en automático.
- Contrato como texto, fechas en un solo formato y la zona horaria acordada con el cliente.
- Un responsable por cada fuente, para atender faltantes o cambios.

## Validación de cifras (caso de control)
1. Replicar UN día completo del reporte actual en el dashboard nuevo y comparar indicador por indicador.
2. Correr en paralelo (reporte actual y dashboard) hasta que las cifras cuadren en varios días seguidos.
3. Toda diferencia se explica por una regla de la lista anterior; si no, la regla falta o está mal escrita.
4. Dejar registrado el día de control, sus cifras y quién lo validó. Es el "caso de control" que pide el checklist de publicación.

## Extracto y rendimiento (propuesto)
- Preferir extracto con actualización programada sobre conexión en vivo para los dashboards de cliente.
- Las hojas de trabajo van ocultas (ver `referencias/cliente-limpieza.md`). No hay un límite de hojas por dashboard ni por libro.
- Los cálculos de conteo único sobre llaves construidas por concatenación, repetidos en cada tarjeta, son lo más pesado: preferible marcar el cálculo a nivel de fila una vez y contar sobre esa marca.
- Cuando algo sea lento, medir antes de cambiar: grabar el rendimiento de Tableau y atacar lo que más tarda.

## Seguridad por usuario (por confirmar con el usuario)
- Si un mismo dashboard lo ven personas con alcance distinto (por ejemplo varias campañas o clientes), restringir los datos por usuario con seguridad a nivel de fila, o usar libros separados. No basta con ocultar filtros.
- El cliente final no debe ver datos de otras campañas ni de otros clientes (ver `referencias/cliente-limpieza.md`).
- Las credenciales de la fuente las pone siempre el usuario; nunca se escriben.
- Para el acceso de la sesión (token, servidor MCP o API), aplicar "Permisos mínimos y datos sensibles" del módulo base: usuario dedicado, acceso mínimo, nunca borrar y datos agregados.
