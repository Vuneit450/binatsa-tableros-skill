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

## Datos mínimos y reglas de negocio
Cada giro define sus tablas mínimas y sus reglas por acordar en `referencias/giros/<giro>.md`. Se confirman con el usuario cuáles cubre el cliente, se piden las que existan desde la primera carga y cada regla acordada se registra en `brief.md`, en el glosario y en el tooltip "Cómo se calcula".

Reglas generales, para todos los giros:
1. Catálogo de asesores (login o ID → nombre completo): siempre.
2. Días laborables: qué días cuentan como hábiles y cómo se tratan los festivos.
3. Zona horaria de fechas y horas.
4. Qué cuenta como registro único (llamada, cuenta o caso) y en qué fecha se cuenta cada evento.

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
