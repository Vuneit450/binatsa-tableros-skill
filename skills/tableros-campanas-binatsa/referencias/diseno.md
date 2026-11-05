# Diseño · Tableros de campañas BINATSA

Estilo tomado del tablero de referencia más reciente de BINATSA (Cobranza), con ajustes acordados.

## Encabezado (igual en todas las vistas)
Una sola franja de 80 px de alto, a todo el ancho, en el color oscuro de la marca del cliente, con esquina recta. De izquierda a derecha:
1. **Logo del cliente** (unos 88 x 80 px): el PNG con proporción fija, nunca estirado.
2. **Título** (unos 1050 px de ancho): "<Campaña> · <Vista>", 20 pt, Tableau Bold, blanco. Debajo, subtítulo de 10 pt en gris claro (`#d0d0d0`): "<Cliente> · <pregunta que responde la vista>". Es el texto más grande del tablero.
3. **Controles** (Periodo, Desde, Hasta y el control del giro), de 196 a 236 px de ancho cada uno, sin fondo ni borde propios: se ve la franja detrás. Entre control y control, una separación delgada del mismo color de la franja.
4. **Logo de BINATSA** (unos 272 x 80 px), pegado a la derecha, sobre una tarjeta blanca porque sus letras azul marino no se leen sobre la franja.
Cómo lograrlo en Tableau: un contenedor horizontal con el fondo de la franja y cada objeto de adentro sin fondo ni borde (ver `herramientas/aplicar-reglas-en-tableau.md`).

## Botones de navegación
Fila pegada a la izquierda, debajo del encabezado. Un botón por cada vista de destino:
- Botón de texto de 164 x 36 px, todos iguales y sin espacio entre ellos.
- Texto: "<Vista> →" (por ejemplo "Dirección →", "Operación →", "Asesores →"), Tableau Bold 11 pt, blanco.
- Color por destino: Dirección en el primario del cliente, Operación en su secundario, las demás vistas en el color oscuro de la marca. Cada uno debe llegar a 4.5:1 con el texto blanco; si no llega, usar su tono oscuro.
- "📖 Guía y glosario" en gris `#55657A` (5.9:1 con blanco), en todas las vistas menos en la propia Guía.
- Libro con varias campañas: los botones que llevan a otra campaña van en el color de esa campaña, para diferenciarlas.
- Al final de la fila, el enlace "▶ Manual en video" (12 pt, negrita, en el color de acento del cliente) al video guía de ese tablero. Cada tablero tiene su propio video; el enlace se agrega cuando el video está publicado (ver `referencias/video-guia.md`).
- En el resto de la fila, una línea "ℹ️" de 8 pt en gris `#44546a` con la instrucción corta de la vista y las definiciones clave (por ejemplo "ℹ️ Filtra periodo y canal arriba · Nivel de servicio = atendidas ≤20 s ÷ atendidas").

## Vistas
Todas llevan el mismo encabezado y botones hacia todas las demás. Los nombres de las vistas comunes son fijos en todos los giros, para que todo tablero BINATSA se reconozca.

| Vista | Botón | Pregunta que responde | Regla |
|---|---|---|---|
| Dirección | Dirección → | ¿Cómo va la campaña? | Obligatoria |
| Operación | Operación → | ¿Qué hay que corregir hoy? | Obligatoria |
| Guía y glosario | 📖 Guía y glosario | ¿Cómo se usa y qué significa cada dato? | Obligatoria |
| Asesores | Asesores → | ¿Cómo rinde cada asesor? | Recomendada |
| Vistas del giro | las define `giros/<giro>.md` | — | Según el giro |
| Corte general | Corte general → | ¿Cómo van todas las campañas juntas? | Solo en libros con varias campañas |

### Guía y glosario
Vista de solo texto, sin gráficos, pero con estilo: secciones con franja, columnas de colores, emojis y jerarquía tipográfica. Nunca una lista plana de definiciones. Mismo encabezado y botones que las demás vistas. De arriba hacia abajo:

1. **📘 Para qué sirve cada vista.** Franja oscura con el título y un subtítulo corto ("cada botón de arriba lleva a una vista"). Debajo, una columna por vista, todas del mismo ancho:
   - Cabecera de la columna en el color del botón de esa vista, con su emoji y nombre en blanco.
   - La pregunta que responde, en negrita (por ejemplo "¿Cómo va la campaña?").
   - Una o dos líneas, en gris, de lo que contiene.
2. **Dos bloques lado a lado:**
   - **🧭 Cómo usar el tablero:** las 5 reglas numeradas, cada número dentro de un cuadrito del color oscuro de la marca: 1) los filtros de arriba afectan todo; 2) un clic en una barra o celda filtra el resto; 3) otro clic quita el filtro; 4) pasa el mouse y te explica qué mide y cómo se calcula; 5) los selectores cambian lo que muestra la gráfica.
   - **Categorías del giro** (por ejemplo "⏳ Buckets" o segmentos): un recuadro por categoría con su nombre en blanco sobre su color (el mismo de las gráficas), y debajo su rango en ese color (por ejemplo "31 a 60 días"). Un recuadro gris "General" para todos juntos.
3. **📖 Glosario.** Franja oscura con el título y el subtítulo "qué significa cada dato y cómo se calcula". Debajo, tres columnas por tema (por ejemplo "Cartera y cobertura", "Contacto y promesas", "Pagos y productividad"; los temas los define el giro), cada una con su cabecera de color y emoji. Cada término:
   - Línea 1: emoji + **término en el color del tema** + ": " + definición simple en texto oscuro (11 pt).
   - Línea 2: cómo se calcula, en gris y más chico (9 pt), con sangría (por ejemplo "Cuentas gestionadas ÷ cuentas asignadas").
   - Si tiene semáforo, sus umbrales al final de la línea 2 (por ejemplo "verde ≥ 95 %").
4. **📒 Notas para leer los datos.** Franja oscura y viñetas cortas: qué significa cada canal, reglas de conteo acordadas, de dónde salen los datos (con el nombre del reporte, nunca de la base), cada cuándo se actualizan, el día del último dato y a quién avisar si algo no cuadra.

Las definiciones salen de `referencias/giros/<giro>.md` y de las reglas acordadas en `brief.md`, sin términos técnicos. Aplica la lista de palabras prohibidas ("Texto visible").

### Asesores (recomendada)
Tabla por asesor con sus indicadores, mapa de calor con selectores de KPI y de periodo, y barras. Clic en un asesor filtra todo; otro clic regresa a todos. Las metas no son estándar: solo si el cliente las tiene, se agregan y se marca con ✓ en verde del semáforo lo que las cumple.

## Layout
- Tamaño: modo Fijo, 2300 x 1300 px, igual en todas las vistas.
- Todo en contenedores en mosaico (no flotante). Margen exterior de 8 px.
- Fondo del tablero: blanco. La información no lleva borde ni fondo propio: gráficos, números de tarjetas, filtros y contenedores van transparentes.
- Solo llevan fondo: la franja del título principal, los títulos de cada hoja (franja del color oscuro de la marca), los botones, el panel de controles y la fila de botones (ver Encabezado).
- Esquinas rectas en todo.
- Todo va centrado (gráficos, tablas, números y deltas de tarjetas, texto "Cómo leer"), excepto los títulos, que van a la izquierda, y los botones, pegados a la izquierda.

## Títulos de cada hoja
El título va sobre una franja del color oscuro de la marca, alineado a la izquierda:
- Línea 1: "<emoji> <pregunta que responde>" (por ejemplo "🔥 ¿Qué canal recupera más cada día?"), 13 pt, Tableau Semibold, blanco.
- Línea 2: cómo se lee o se calcula, en una línea, 10 pt, Tableau Light, en un tono claro (`#d6e6f2`).
- En tarjetas KPI, la línea 1 lleva el nombre de la métrica.

## Medidas estándar (en 2300 x 1300 px)
| Elemento | Medida |
|---|---|
| Margen exterior del tablero | 8 px |
| Encabezado | 80 px de alto (detalle en Encabezado) |
| Botones de navegación | 164 x 36 px |
| Tarjetas KPI | 6 por fila, de igual ancho (unos 380 x 190 px), margen de 6 px y relleno de 6 px. Máximo 2 filas |
| Gráficos y tablas | margen de 6 px y relleno de 6 px; los principales entre 350 y 400 px de alto, los de apoyo entre 150 y 230 px |
| Selector de ancho completo (por ejemplo de KPI) | 40 px de alto |
| Pie "Cómo leer" | ancho completo, 52 px de alto, 9 pt |

Las imágenes de `ejemplos/` son del estilo anterior (1910 x 1300 y otro encabezado): sirven solo como idea general hasta que se actualicen.

## Interactividad
- **Clic en una marca filtra su vista.** Cada gráfico y tabla es origen de una acción de filtro al seleccionar, con destino todas las hojas de su misma vista (incluidas las tarjetas KPI) y "todos los campos" en común. Las tablas por asesor filtran solo por Asesor. Las acciones no pasan a otras vistas.
- **Otro clic, o un clic fuera de las marcas, quita el filtro** y todo regresa al estado inicial.
- **Las tarjetas KPI reciben, nunca son origen.**
- **Pasar el mouse resalta los "datos hermanos".** Una acción de resaltar al pasar el mouse, a nivel de la vista, ilumina en todas las hojas lo que comparte el valor señalado y apaga lo demás. Campos: los de categoría del giro (por ejemplo Bucket o Segmento, Canal y Asesor en Cobranza; Campaña, Tipificación, Franja y Asesor en ATC; la lista va en `referencias/giros/<giro>.md`). Las tarjetas KPI quedan fuera del destino, para que no se apaguen. Para que dos hojas se iluminen juntas deben usar el campo con el mismo nombre.
- **Clic en la categoría principal** (por ejemplo un bucket o segmento) además cambia ese parámetro de arriba con una acción de parámetro, para que todo lo que depende de él se ajuste.
- **Clic en un día (acción de parámetro).** Los gráficos con la fecha en el eje no usan acción de filtro, porque dejaría a las tarjetas sin periodo previo y los deltas saldrían mal. Un clic en un día llena el parámetro "Día seleccionado"; al limpiar la selección, el parámetro vuelve a vacío. Todos los cálculos de periodo (ver `referencias/giros/<giro>.md`) usan [Desde efectivo] y [Hasta efectivo], que toman ese día si hay uno elegido. Así las tarjetas muestran el día elegido contra el día anterior y contra 7 días antes.
- **Respaldo:** si en la plantilla la acción de parámetro no se limpia bien o los demás gráficos no responden al día, usar una acción de filtro normal en esos gráficos de fecha y quitar de su destino las tarjetas KPI. Avisar al usuario cuál quedó.
- Quedan fuera solo las hojas que no comparten campos (por ejemplo, una encuesta de otra fuente). Se declaran en el reporte de la prueba de interacción con su motivo; deben ser la minoría.
- Verificación obligatoria: "Prueba de interacción" en `referencias/publicacion.md`.
- En edición web no dejar marcas seleccionadas ni parámetros cambiados antes de publicar.

## Parámetros estándar
Los controles de arriba son parámetros, no filtros: Tableau no permite leer el valor de un filtro dentro de un cálculo, y los deltas lo necesitan. Cada hoja lleva el filtro "En rango" = Verdadero (fecha entre [Desde efectivo] y [Hasta efectivo]).
- **Periodo** (lista), solo estas 13 opciones: Mes actual, Mes anterior, Trimestre actual, Trimestre anterior, Semestre actual, Semestre anterior, Año actual, Año anterior, Últimos 7 días, Últimos 30 días, Últimos 12 meses, Todo el historial y Personalizado. Por defecto: "Año actual".
- **Desde** y **Hasta** (fecha): solo cuentan con Periodo en "Personalizado"; Hasta no puede pasar de hoy.
- **Día seleccionado** (fecha): vacío por defecto; lo llena el clic en un día.
- **Control del giro**: lo define `referencias/giros/<giro>.md` (por ejemplo Segmento o Canal en Cobranza).
- **Selectores de métrica** (por ejemplo "KPI" o "Métrica del mapa de calor"): listas con las métricas que muestra la gráfica.

**Nombres:** en español, sin pistas entre paréntesis (nada de "Desde (2000 = sin límite)" ni "Campaña (Parámetro)"). Solo se permite la unidad cuando hace falta, por ejemplo "Tolerancia (min)". La explicación de cada control va en la Guía y glosario. Los cálculos derivados se nombran igual en todos los proyectos: [Desde efectivo], [Hasta efectivo] y las banderas de periodo.

## Tarjetas KPI
Van arriba en Dirección y Operación: 6 por fila, hasta 2 filas (medidas en "Medidas estándar"). Las tarjetas reciben las acciones, nunca son origen. Qué métricas lleva cada una lo define `referencias/giros/<giro>.md`; cada tarjeta debe ayudar a decidir, no solo describir.

De arriba hacia abajo (todo centrado excepto el título):
1. **Título:** igual que cualquier hoja (ver "Títulos de cada hoja"): "<emoji> <métrica>" en 13 pt y, debajo, qué cuenta en 10 pt (por ejemplo "💰 Monto recuperado / Pagos aplicados, periodo elegido").
2. **Número:** 28 pt, Tableau Bold, en un tono del primario del cliente que llegue a 3:1 contra el blanco (en BINATSA, `#007F84`), o en color de semáforo si la métrica tiene meta.
3. **Dos deltas**, uno por línea:
   ```
   vs periodo previo: ▲ 4.2%
   vs 7 días previos: ▼ 1.1 pp
   ```
   La etiqueta en 10 pt gris `#6b7680`; el valor en 12 pt negrita, verde o rojo del semáforo según mejore o empeore (invertir cuando bajar es bueno, por ejemplo "Sin gestión").
4. Solo el título lleva fondo; el número y los deltas van sin borde ni fondo.

Reglas de los deltas:
- "Periodo previo" = el rango inmediatamente anterior de la misma duración que el rango efectivo. "7 días previos" = el mismo rango desplazado 7 días atrás.
- Siguen la selección: se calculan sobre el rango efectivo y con la misma selección (canal, asesor, segmento, etc.) en los dos periodos.
- Con un rango efectivo de 7 días o menos (incluido un día seleccionado), se oculta "vs 7 días previos" y queda solo "vs periodo previo".
- Sin periodo con el cual comparar (por ejemplo "Todo el historial"), el delta muestra "-", nunca "+0.0 %".
- Para métricas que ya son porcentaje, el delta va en puntos porcentuales (pp); para las demás, en %.
- Cálculo en Tableau: banderas de periodo y [Desde efectivo]/[Hasta efectivo], ver `referencias/giros/<giro>.md`.

## Estilo visual
- Títulos de hojas y tarjetas: ver "Títulos de cada hoja" y "Tarjetas KPI".
- Todo porcentaje con símbolo % (1 decimal). Dinero con $ y miles; M/K en cifras grandes. Si el % se corta en celdas angostas (p. ej. mapa de calor dentro del tablero), avisar y proponer sin decimales o ensanchar; nunca dejar el número sin %.
- Barras de un solo color: resaltar la más alta (acento) con su número arriba, resto neutro. Barras apiladas por una categoría ordenada del giro (por ejemplo segmentos de mora) usan el paso que le toca en la rampa (ver Paleta), igual en todas las hojas.
- Etiquetas de valor en gráficos: si el valor de una marca es 0 o nulo, no se muestra su etiqueta, para no saturar la gráfica con datos innecesarios. Aplica a barras, mapa de calor y demás gráficos; la marca o la celda, si existe, se queda sin número. (Las tarjetas KPI sin datos siguen mostrando "-", ver "Estados vacíos y datos parciales".)
- Tablas: todo el contenido centrado (encabezados y celdas) y siempre con totales (total general en filas y, si aplica, en columnas). Una celda con valor 0 o nulo muestra "-" en lugar del número.
- Sin ruido: nada de gráficos huérfanos, hojas visibles que el cliente no consulta (ocultas; acceso por "Ir a hoja"), ni calculados sin uso.
- Nombres de hojas: sin estándar; cada proyecto usa los suyos. Los parámetros sí son estándar (ver Parámetros estándar).
- Gráficos sin líneas y con fondo transparente: sin cuadrícula, líneas de cero, líneas de referencia sin uso, divisiones de fila y columna, ni líneas de eje. Los valores se leen con etiquetas en las marcas (en las barras, el número arriba).
- Ningún gráfico muestra títulos de ejes, ni del primero ni del segundo, para que no le quiten espacio al gráfico. Lo que mide cada eje se explica en el subtítulo de la hoja y en el tooltip "Cómo se calcula".

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

## Texto visible (lista única de palabras prohibidas)
Aplica a todo lo que ve el cliente: títulos, subtítulos, pies, la línea ℹ️, tooltips, Guía y glosario, nombres de parámetros y el video guía. Ningún texto puede mencionar:
- nombres de servidores, bases de datos, esquemas o tablas (por ejemplo Redshift o "esquema.tabla"), ni la palabra "servidor";
- "Excel" ni otra herramienta interna de trabajo;
- sistemas internos (por ejemplo WFM, el CRM por su nombre);
- "el más grande" o "el más completo";
- cualquier frase que el usuario haya pedido omitir.
Para la fuente, usar el nombre del reporte o del área (por ejemplo "Fuente: reporte diario de llamadas"); para la actualización, "los datos se actualizan solos". Los demás archivos de la skill remiten a esta lista; si cambia, se cambia solo aquí.

## Cuándo usar cada gráfico (propuesto)
- Barras: comparar categorías (canales, asesores, resultados), ordenadas de mayor a menor.
- Línea o barras por día: tendencia día a día.
- Mapa de calor: día contra hora, o día contra canal, con selector de métrica.
- Embudo: etapas de un proceso (cartera, gestionadas, contacto, promesa, pago).
- Tabla: detalle por asesor o por canal, con total general.
- Pastel o dona: solo para 2 a 5 partes de un todo (por ejemplo cuentas sin gestión por segmento), con el % a la vista; nunca para comparar.
- Mapa geográfico: solo cuando el dato tiene zona (por ejemplo visitas).

## Dispositivos
Los dashboards se diseñan solo para computadora (2300 x 1300 px). No se diseñan vistas para teléfono ni para tableta.

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
- Etiquetas de ejes y marcas: 9 pt (mínimo 8 en web). Deltas de tarjeta: etiqueta 10 pt, valor 12 pt negrita. Contenido de tablas: 10 pt; encabezados de tabla: 10 pt en Semibold. Pie "Cómo leer": 9 pt en el color de texto secundario.
- Tooltip: título 14 pt, etiquetas 11 pt, valores 12 pt, secciones y cuerpo 10 pt, notas 9 y 8 pt (ver `referencias/tooltips.md`).
- Valores marcados como "propuestos" hasta que el usuario los confirme en la primera revisión de cada cliente.

## Patrón del mapa de calor con selector de métrica
Referencia visual: `ejemplos/mapa-calor.png`.
Escala de color: la define el proyecto, con la paleta del cliente, de claro a oscuro. El texto de cada celda cambia de color según el fondo (oscuro sobre fondo claro, blanco sobre fondo oscuro) para que el número se lea siempre con al menos 4.5:1.
Parámetro de texto "Métrica del mapa de calor" (Gestiones, Contactos con titular, Promesas, Cuentas distintas, % contacto, % promesa, Monto recuperado). Un cálculo "Métrica seleccionada" (CASE sobre el parámetro) para el color y otro "Métrica (texto)" para la etiqueta que agrega % cuando la métrica es porcentual. Etiqueta mínima 8 pt en web.
