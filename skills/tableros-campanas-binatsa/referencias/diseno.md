# Estructura y estilo · Dashboards de Cobranza BINATSA

## Estructura estándar
Como mínimo dos vistas, Dirección y Operación; el proyecto puede agregar más (por ejemplo un seguimiento por asesor). Todas llevan el título principal, el ícono del cliente, el logo de BINATSA, los controles de arriba y los botones de navegación hacia las demás vistas, con el mismo formato.

### Logos
Dos logos, en la misma fila del título principal y siempre en la misma posición en todas las vistas:
- Ícono del cliente, arriba a la izquierda: imagen cuadrada de unos 88 x 80 px.
- Logo de BINATSA (`marca-binatsa/binatsa.svg`; en PNG si Tableau no acepta SVG), arriba a la derecha y pegado a la esquina: unos 272 x 80 px, con alto proporcional sin deformar, sobre una tarjeta blanca porque sus letras azul marino no se leen sobre la franja oscura. Referencia visual: `ejemplos/encabezado.png` (ilustración con datos inventados).

### Título principal del dashboard
Texto de 20 pt en negrita, color blanco, sobre una franja del color oscuro de la marca del cliente (ver Contraste), sin borde, de unos 660 x 80 px, arriba a la izquierda junto al ícono del cliente. Formato del texto: "Cobranza <Cliente> · <Vista>" (por ejemplo "Cobranza <Cliente> · Dirección") y, debajo, un subtítulo de 10 pt con la pregunta que responde la vista (por ejemplo "¿Cómo va la campaña?"). Es el texto más grande del dashboard: los títulos de bloque (13 pt) quedan por debajo.
El encabezado (título principal, ícono, controles y logo) tiene una sola franja de fondo completo, a todo el ancho, con esquina recta. Los filtros y parámetros del encabezado NO llevan fondo ni borde propios: el fondo que se ve detrás de ellos es el de la franja. En Tableau, una forma de lograrlo es poner todo el encabezado en un contenedor horizontal con el fondo de la franja y dejar sin fondo ni borde cada objeto de adentro (validar en el primer dashboard de cada cliente).

### Botones de navegación
Objeto Botón de navegación de tipo texto, uno por cada vista de destino, en una fila debajo del encabezado:
- Tamaño fijo de 164 x 36 px, uno junto a otro y sin espacio entre ellos; la fila va pegada a la izquierda, bajo el título principal.
- Fuente Tableau Bold de 11 pt, texto blanco.
- Texto: "Ir a <Vista> →", con flecha. Ejemplos: "Ir a Operación →", "Ir a Seguimiento →".
- Color por destino: Dirección en el color primario del cliente, Operación en su color secundario, las demás vistas en el color oscuro de la marca (negro o azul marino). Cada color debe llegar a 4.5:1 con el texto blanco; si el color de marca no llega (muchos rosas y turquesas se quedan en 3 a 3.7:1), usar su tono oscuro.
- Botón "📖 Glosario" en gris `#55657A` (llega a 5.9:1 con texto blanco), presente en todas las vistas menos en la Guía de uso, y lleva a la Guía de uso.
- En la Guía de uso, los botones hacia las demás vistas ocupan el ancho completo, repartido en partes iguales.

## Vistas estándar
Obligatorias: Dirección y Operación (arriba). Recomendada en todo proyecto: Guía de uso. Opcional, según el proyecto: Seguimiento. Cualquier otra vista adicional se define con el usuario. Todas llevan el mismo título principal, ícono del cliente, logo de BINATSA y botones de navegación (hacia todas las demás vistas).

### Guía de uso (recomendada)
Referencia visual: `ejemplos/guia-uso.png`.
Vista de solo texto, sin gráficos, con el mismo estilo de títulos de bloque. Se abre desde el botón "📖 Glosario" de las demás vistas; no hay una vista de glosario aparte. Contiene, en este orden:
1. Para qué sirve cada vista: una línea por vista con la pregunta que responde.
2. Cómo usar el tablero: las 5 reglas (los filtros de arriba afectan todo; clic en una gráfica filtra el resto; otro clic quita el filtro; pasa el mouse y te explica; los selectores cambian la gráfica).
3. Glosario: cada métrica con su definición, tomadas del glosario de `referencias/giros/cobranza.md` y de las reglas de negocio acordadas, sin términos técnicos.
4. Segmentos de cartera del cliente: nombre y rango de cada uno.
5. Actualización: frecuencia real de los datos y el día del último dato.
6. A quién avisar si algo no cuadra.

### Seguimiento (opcional): ¿cómo rinde cada asesor?
Tabla por asesor con todos sus indicadores, mapa de calor con selectores de KPI y de periodo, y barras. Clic en un asesor filtra todo y deja ver solo su rendimiento; otro clic regresa a todos. Las metas NO son estándar: preguntar al usuario si el cliente tiene metas y cuáles; solo si las hay, agregar tarjetas de metas y marcar en azul oscuro lo que las cumple.

## Layout
- Todo en contenedores en MOSAICO (no flotante).
- Tamaño: modo Fijo, 1910 x 1300 px, igual en todas las vistas (incluida la Guía de uso). Las vistas adicionales usan la misma medida salvo que se defina otra con el usuario.
- La información no lleva borde ni color de fondo: todo transparente (gráficos, números de tarjetas KPI, filtros, parámetros, hojas y contenedores). Los ÚNICOS elementos que pueden llevar fondo o borde son los títulos (título principal, encabezados de zona, títulos de gráficos, de tablas y de tarjetas KPI: franja de color de marca) y los botones de navegación (fondo de color de marca).
- Esquinas redondeadas: los títulos de gráficos, tablas y tarjetas KPI, que son lo único con fondo dentro de cada bloque, llevan esquinas redondeadas (radio propuesto: 12 px). El encabezado (título principal) y los botones llevan esquina recta. El resto es transparente y sin borde, así que su radio no se ve. En Tableau 2026.1 o posterior, el radio se aplica en el panel de diseño a cada hoja; la franja del título queda con las esquinas de arriba redondeadas (validar en el primer dashboard de cada cliente). Revisar las exportaciones a PDF o imagen, que pueden mostrar las esquinas distinto.
- Todo va centrado (gráficos y tablas dentro de su zona, el contenido de las tablas, números y deltas de las tarjetas, filtros, parámetros, texto "Cómo leer") EXCEPTO los títulos, que van alineados a la izquierda (títulos de gráficos, de tablas y encabezados de zona), y los botones de navegación, que van pegados a la izquierda bajo el título principal.

## Medidas estándar
Tomadas del tablero de referencia de 1910 x 1300 px, igual para todas las vistas. Referencia visual de las dos vistas obligatorias: `ejemplos/vista-direccion.png` y `ejemplos/vista-operacion.png`; de la franja de título de bloque: `ejemplos/franja-bloque.png`; de las tablas por asesor: `ejemplos/tabla-asesores.png`.

| Elemento | Medida |
|---|---|
| Margen exterior del dashboard | 8 px |
| Fila del encabezado | 80 px de alto |
| Ícono del cliente | unos 88 x 80 px, arriba a la izquierda |
| Título principal | unos 660 x 80 px |
| Controles de arriba (Periodo, Desde, Hasta y Canal o Segmento) | entre 196 y 236 px de ancho y 80 px de alto |
| Logo de BINATSA | unos 272 x 80 px, arriba a la derecha |
| Botones de navegación | 164 x 36 px, debajo del encabezado, pegados a la izquierda, uno junto a otro |
| Franja de título de bloque | ancho completo, 54 px de alto |
| Tarjeta KPI | 271 x 190 px; el ancho se reparte en partes iguales (7 por fila en 1910 px); margen de 6 px y relleno de 6 px |
| Selector de ancho completo (por ejemplo de KPI) | ancho completo, 40 px de alto |
| Gráficos y tablas | margen de 6 px y relleno de 6 px; los principales entre 350 y 400 px de alto, los de apoyo entre 150 y 230 px |
| Pie "Cómo leer" | ancho completo, 52 px de alto |

## Interactividad
- La mayoría de los gráficos se comunican entre sí: clic en una marca filtra los demás. Cuáles quedan fuera depende del proyecto (por ejemplo, un gráfico con otra fuente de datos o sin campos en común) y se declaran en el reporte con el motivo. Las tarjetas KPI son destino, no origen.
- Patrón de comunicación de referencia (tomado de los tableros de referencia; no es exacto, cada proyecto lo adapta):
  - Cada gráfico o tabla es origen de una acción de filtro al seleccionar, con "todos los campos" que comparte con las demás hojas, y todas las demás hojas del dashboard como destino.
  - Las tarjetas KPI nunca son origen; solo reciben.
  - Orígenes típicos en Dirección: segmento, tendencia día a día, canal y promesas por día. En Operación: horas, asesores, resultados o tipificaciones, cobertura por segmento, sin gestión, gestiones por hora y visitas.
  - Se excluye como destino la hoja que viene de otra fuente de datos (por ejemplo, una encuesta que no comparte campos con las llamadas).
  - Clic en un segmento: además del filtro, una acción de parámetro llena el parámetro "Segmento", para que lo que depende del segmento elegido (tarjetas, métricas) se adapte.
  - Al pasar el mouse sobre un segmento se resalta ese segmento en todas las hojas (acción de resaltar al pasar el mouse, a nivel del dashboard).
- Implementación en las tarjetas KPI: los periodos se calculan con banderas por fila a partir de los parámetros de fecha (ver `referencias/giros/cobranza.md`) y cada KPI se calcula una vez por periodo con IF bandera THEN medida END. Así las tarjetas son destino normal de las acciones de filtro de segmento, asesor, canal, hora, tipificación y zona: esos filtros no tocan las fechas y el periodo previo sigue disponible, de modo que los deltas siguen la selección. La fecha es la excepción: si un clic filtrara por día, desaparecerían las filas de los demás periodos. Por eso el día NO va en una acción de filtro: un clic en un día dispara una acción de parámetro que llena "Día seleccionado" (fecha) y todo el dashboard usa [Desde efectivo] y [Hasta efectivo]. La parte del día seleccionado es un patrón propuesto: validarlo en el primer dashboard de cada cliente.
- La verificación obligatoria está en `referencias/publicacion.md` (Prueba de interacción).
- Preferir tipos de gráfico que admitan segmentador/parámetro.
- Controles globales arriba: Periodo, Desde, Hasta y, si el proyecto lo necesita, Canal o Segmento. Todos son PARÁMETROS, no filtros: Tableau no permite leer el valor de un filtro dentro de un cálculo, y los deltas y el periodo previo lo necesitan. Desde y Hasta solo cuentan cuando Periodo es "Personalizado". Un campo calculado "En rango" (fecha entre [Desde efectivo] y [Hasta efectivo]) va en los filtros de cada hoja, con valor Verdadero.
- En edición web NO dejar marcas seleccionadas ni parámetros cambiados antes de publicar.

## Parámetros estándar
Mismos nombres en todos los proyectos, en español y sin pistas entre paréntesis (la explicación va en la Guía de uso):
- Periodo (lista): Mes actual, Mes anterior, Trimestre actual, Trimestre anterior, Semestre actual, Semestre anterior, Año actual, Año anterior, Últimos 7 días, Últimos 30 días, Últimos 12 meses, Todo el historial y Personalizado. Valor por defecto: "Año actual" (el proyecto puede cambiarlo si el usuario lo pide).
- Desde (fecha) y Hasta (fecha): solo cuentan si Periodo es "Personalizado"; Hasta no puede pasar de hoy. Indicar el rango válido en la Guía de uso.
- Día seleccionado (fecha): vacío por defecto; lo llena la acción de parámetro al hacer clic en un día.
- Segmento (lista, "Todos"): segmentos de cartera del cliente. Si el proyecto separa por canal o producto, usar además Canal (lista, "Todos").
- KPI y Métrica del mapa de calor (listas): selectores de la métrica que muestran las gráficas.
Cualquier otro parámetro lo define el proyecto, con nombre en español y sin pistas entre paréntesis. Los cálculos que derivan de estos (Desde efectivo, Hasta efectivo, banderas de periodo) se nombran igual en todos los proyectos.

## Estilo visual
- Encabezados de zona: franja de color de marca (en su tono oscuro si hace falta, ver Contraste), título blanco con emoji coherente + subtítulo de una línea con la pregunta de negocio.
- KPIs grandes con número en color (adaptar a la marca del cliente).
- Todo porcentaje con símbolo % (1 decimal). Dinero con $ y miles; M/K en cifras grandes. Si el % se corta en celdas angostas (p. ej. mapa de calor dentro del tablero), avisar y proponer sin decimales o ensanchar; nunca dejar el número sin %.
- Barras de un solo color: resaltar la más alta (acento) con su número arriba, resto neutro. Barras apiladas por segmento usan el paso que le toca a cada segmento en la rampa de segmentos (ver Paleta): la rampa es la jerarquía de mora y es la misma en todas las hojas.
- Etiquetas de valor en gráficos: si el valor de una marca es 0 o nulo, no se muestra su etiqueta, para no saturar la gráfica con datos innecesarios. Aplica a barras, mapa de calor y demás gráficos; la marca o la celda, si existe, se queda sin número. (Las tarjetas KPI sin datos siguen mostrando "-", ver "Estados vacíos y datos parciales".)
- Tablas: una celda con valor 0 o nulo muestra "-" (un guion) en lugar del número, para que la celda no quede vacía ni muestre un 0 que se lea como dato.
- Sin ruido: nada de gráficos huérfanos, hojas visibles que el cliente no consulta (ocultas; acceso por "Ir a hoja"), ni calculados sin uso.
- Nombres de hojas: sin estándar; cada proyecto usa los suyos. Los parámetros sí son estándar (ver Parámetros estándar).
- Ningún gráfico lleva líneas de fondo: quitar la cuadrícula, las líneas de cero, las líneas de referencia sin uso y las divisiones de fila y columna. Como la cuadrícula ya no ayuda a leer los valores, mostrar la etiqueta del valor en las marcas donde haga falta (en las barras, el número arriba, como ya pide la regla de la barra destacada).
- Ningún gráfico muestra el título del segundo eje (en gráficos de doble eje). Lo que mide el segundo eje se explica en el subtítulo de la zona y en el tooltip "Cómo se calcula".

## Formato regional
- Idioma: toda etiqueta y todo texto en español.
- Configuración regional del libro: Español (México), como en el tablero de referencia.
- Fechas en día/mes/año (por ejemplo 19/10/2026) y horas en formato de 24 h. Zona horaria acordada con el cliente (ver `referencias/datos.md`).
- Dinero con $ y separador de miles; si el proyecto maneja más de una moneda, indicar el código en la etiqueta.

## Estados vacíos y datos parciales (propuesto)
- Símbolo de "sin dato": siempre "-" (guion corto), igual en tarjetas, deltas y tablas.
- Una tarjeta sin datos muestra "-", nunca 0, con el subtítulo "Sin datos para este filtro". Una tarjeta cuyo valor es 0 de verdad muestra 0: el "-" es solo para cuando no hay datos.
- Un delta sin periodo con el cual comparar (por ejemplo con "Todo el historial") muestra "-", nunca "+0.0 %".
- Un gráfico sin datos muestra un mensaje centrado: "Sin datos con estos filtros".
- En un gráfico con datos, una marca con valor 0 o nulo no muestra etiqueta; en una tabla, la celda muestra "-" (ver "Etiquetas de valor en gráficos"). Si todo el gráfico está en 0 o nulo, se muestra el mensaje de "sin datos".
- Si un dato solo existe para parte del periodo (por ejemplo el detalle por hora de un solo día), decirlo en pantalla; no se rellena ni se estima.

## Texto visible
Ningún texto visible del dashboard (títulos, subtítulos, pies, tooltips y Guía de uso) puede mencionar nombres de servidores, bases de datos o tablas (por ejemplo Redshift), la palabra "servidor", "Excel", sistemas internos (por ejemplo WFM) ni "el más grande" o "el más completo". Para la fuente, usar el nombre del reporte o del área (por ejemplo "Fuente: reporte diario de llamadas"); para la actualización, "los datos se actualizan solos". Es la misma regla del video guía.

## Cuándo usar cada gráfico (propuesto)
- Barras: comparar categorías (canales, asesores, resultados), ordenadas de mayor a menor.
- Línea o barras por día: tendencia día a día.
- Mapa de calor: día contra hora, o día contra canal, con selector de métrica.
- Embudo: etapas de un proceso (cartera, gestionadas, contacto, promesa, pago).
- Tabla: detalle por asesor o por canal, con total general.
- Pastel o dona: solo para 2 a 5 partes de un todo (por ejemplo cuentas sin gestión por segmento), con el % a la vista; nunca para comparar.
- Mapa geográfico: solo cuando el dato tiene zona (por ejemplo visitas).

## Dispositivos
Los dashboards se diseñan solo para computadora (1910 x 1300 px). No se diseñan vistas para teléfono ni para tableta.

## Paleta y tipografía
Paleta de BINATSA (y modelo de cómo documentar la de un cliente): `marca-binatsa/paleta-binatsa.md`. Para cargarla en Tableau: ver la sección "Para Tableau" de ese mismo documento (el método depende de la versión).

Paleta (derivarla de los colores del cliente; si solo hay logo, extraer 2 colores dominantes):
- Primario del cliente: encabezados de zona, selección y barra destacada (la más alta).
- Secundario del cliente: acentos y líneas.
- Neutro: barras no destacadas y texto secundario en gris con matiz hacia el primario (no gris puro). Texto principal casi negro, nunca #000 puro.
- Semáforo fijo, independiente de la marca: verde #2e7d32 (mejora), rojo #c62828 (empeora), ámbar #C77700 (alerta; en texto pequeño usar #9A5A00 para que se lea). Invertir cuando bajar es bueno. Nunca usar el color como única señal: acompañarlo siempre con ▲ / ▼ o con texto.
- Segmentos de cartera: una rampa del primario del cliente de claro a oscuro (menos mora = más claro); mismo color por segmento en TODAS las hojas. Todos los pasos deben llegar a 3:1 de contraste contra el fondo (el paso más claro no puede ser un tono pastel). Nunca más de 6 colores categóricos.
- Canales y otras categorías (por ejemplo producto): los colores los define el proyecto, con la paleta del cliente. Deben ser los mismos en todas las hojas, en los tooltips y en el video guía.
- Contraste: texto blanco sobre franja de color solo si el contraste es de al menos 4.5:1. Si el primario del cliente no llega (el turquesa de BINATSA da 2.6:1), usar su tono oscuro para la franja (en BINATSA, turquesa oscuro `#007F84`) y reservar el color claro del logo para acento decorativo. Toda barra, línea o número de color debe llegar a 3:1 contra el fondo; si el color de marca no llega (el turquesa del logo da 2.6:1), usar su tono oscuro. Sin fondos ni bordes en la información (todo transparente); solo los títulos y los botones de navegación pueden llevarlos.

Tipografía: familia Tableau en todos los proyectos (no usar la tipografía del cliente). Se juega con los pesos, no con otras familias:
- Tableau Bold: título principal, número de tarjeta KPI, valores en negrita (tooltips) y botones.
- Tableau Semibold: títulos de zona y de tarjeta, encabezados de tabla y textos destacados.
- Tableau Medium: etiquetas de ejes y marcas.
- Tableau Light: subtítulos.
- Tableau Book: cuerpo de texto y tooltips.
Tamaños:
- Número de tarjeta KPI: 28 pt en Tableau Bold, en un tono del primario que llegue a 3:1 contra el fondo (en BINATSA, turquesa oscuro `#007F84`) o en color de semáforo.
- Título principal del dashboard: 20 pt en negrita, blanco sobre franja.
- Título de bloque (zona, gráfico, tabla y tarjeta KPI): 13 pt en Tableau Semibold, blanco sobre franja; subtítulo de 10 pt en Tableau Light, en un tono claro del primario.
- Subtítulo bajo el título principal: 10 pt, en el color de texto secundario.
- Botón de navegación: Tableau Bold 11 pt, blanco sobre el color de marca.
- Etiquetas de ejes y marcas: 9 pt (mínimo 8 en web). Delta de tarjeta: 10 pt. Contenido de tablas: 10 pt; encabezados de tabla: 10 pt en Semibold. Pie "Cómo leer": 9 pt en el color de texto secundario.
- Tooltip: título 14 pt, etiquetas 11 pt, valores 12 pt, secciones y cuerpo 10 pt, notas 9 y 8 pt (ver `referencias/tooltips.md`).
- Valores marcados como "propuestos" hasta que el usuario los confirme en la primera revisión de cada cliente.

## Patrón del mapa de calor con selector de métrica
Referencia visual: `ejemplos/mapa-calor.png`.
Escala de color: la define el proyecto, con la paleta del cliente, de claro a oscuro. El texto de cada celda cambia de color según el fondo (oscuro sobre fondo claro, blanco sobre fondo oscuro) para que el número se lea siempre con al menos 4.5:1.
Parámetro de texto "Métrica del mapa de calor" (Gestiones, Contactos con titular, Promesas, Cuentas distintas, % contacto, % promesa, Monto recuperado). Un cálculo "Métrica seleccionada" (CASE sobre el parámetro) para el color y otro "Métrica (texto)" para la etiqueta que agrega % cuando la métrica es porcentual. Etiqueta mínima 8 pt en web.
