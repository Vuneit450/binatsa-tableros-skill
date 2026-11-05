# Datos · Tableros de campañas BINATSA

Este módulo va antes de construir: sin datos completos y reglas acordadas por escrito, las cifras no cuadran.

## Principio
Pedir los datos a detalle (un registro por evento) con la llave común del giro (contrato en Cobranza, identificador de llamada en ATC), en formato texto. Los porcentajes y las razones no se piden: se calculan a partir del detalle. Las reglas que hoy viven dentro de consultas o fórmulas se acuerdan por escrito, para que la fuente nueva dé las mismas cifras.

## Libros con extracción (siempre)
- Todo libro de cliente se publica con extracción y actualización programada, no con conexión en vivo. Así, al descargar el `.twbx` los datos vienen dentro y la sesión puede trabajar con ellos.
- Si el libro usa una fuente publicada en Tableau Cloud, los datos viven en esa fuente y no en el `.twbx`: descargar también la fuente publicada con su extracción (`herramientas/descargar_libro.py --con-fuentes`) y guardarla en `datos/`.
- Si un libro llega con conexión en vivo, convertirlo a extracción en Tableau Desktop (Datos → Extraer datos) antes de publicarlo, y avisar al usuario.

## Permiso y cuidado de los datos
BINATSA ya autorizó leer los extractos de los libros de sus clientes para construir y validar los tableros, así que no se vuelve a preguntar en cada proyecto, salvo que el `brief.md` del cliente diga lo contrario. Siempre:
- Explorar y validar con sumas y conteos (por día, segmento, canal o asesor); nunca imprimir filas con datos de clientes finales.
- Los datos se quedan en la carpeta privada del proyecto; nunca se suben al repositorio ni se copian a otra parte.

## Primer acercamiento a los datos
En la carpeta del proyecto (paso 2 y 3 del flujo en `SKILL.md`):
1. Leer la estructura del `.twb`: fuentes, campos, cálculos y parámetros.
2. Leer el extracto (`.hyper` dentro del `.twbx` o de la fuente publicada en `datos/`) con la API de Hyper, solo con consultas de sumas y conteos.
3. Llenar el diccionario de datos desde `plantillas/diccionario-datos.md`: por cada tabla, sus campos con tipo y significado, y las reglas acordadas.
4. Si no hay extracto, pedir una muestra anonimizada en CSV por tabla (por ejemplo una semana); la definición de "anonimizada" está en Seguridad, en `SKILL.md`.
5. Con eso se calcula por código el caso de control y se compara con lo que muestra el tablero.

## Datos mínimos y reglas de negocio
Cada giro define sus tablas mínimas y sus reglas por acordar en `referencias/giros/<giro>.md`. Se confirma con el usuario cuáles cubre el cliente, se piden las que existan desde la primera carga y cada regla acordada se registra en `brief.md`, en el glosario y en el tooltip "Cómo se calcula".

Reglas generales, para todos los giros:
1. Catálogo de asesores (login o ID → nombre completo): siempre.
2. Días laborables: qué días cuentan como hábiles y cómo se tratan los festivos.
3. Zona horaria de fechas y horas.
4. Qué cuenta como registro único (llamada, cuenta o caso) y en qué fecha se cuenta cada evento.

## Carga y formato
- Carga diaria, completa y sin intervención manual, con una hora de corte acordada antes del envío al cliente.
- Histórico mínimo: el mes en curso más el mes anterior, para comparativos.
- Sin fechas escritas a mano: las consultas toman el periodo en automático.
- Llaves como texto, fechas en un solo formato y la zona horaria acordada con el cliente.
- Un responsable por cada fuente, para atender faltantes o cambios.

## Validación de cifras (caso de control)
1. Replicar un día completo del reporte actual en el tablero nuevo y comparar indicador por indicador.
2. Correr en paralelo (reporte actual y tablero) hasta que las cifras cuadren varios días seguidos.
3. Toda diferencia se explica por una regla acordada; si no, la regla falta o está mal escrita.
4. Registrar en `brief.md` el día de control, sus cifras y quién lo validó. Es el caso de control que pide el checklist de publicación.

## Extracto y rendimiento (propuesto)
- Las hojas de trabajo van ocultas (ver `referencias/cliente-limpieza.md`). No hay un límite de hojas por tablero ni por libro.
- Los conteos únicos sobre llaves construidas por concatenación, repetidos en cada tarjeta, son lo más pesado: marcar el cálculo a nivel de fila una vez y contar sobre esa marca.
- Cuando algo sea lento, medir antes de cambiar: grabar el rendimiento de Tableau y atacar lo que más tarda.

## Seguridad por usuario (por confirmar con el usuario)
- Si un mismo tablero lo ven personas con alcance distinto (por ejemplo varias campañas o clientes), restringir los datos por usuario con seguridad a nivel de fila, o usar libros separados. No basta con ocultar filtros.
- Para el acceso de la sesión (token, servidor MCP o API), aplicar Seguridad en `SKILL.md`.
