# Cómo aplicar en Tableau las reglas que el XML no puede

Pasos escritos a partir de la documentación y del uso general de Tableau; **no se probaron en Tableau**. Los nombres de los menús pueden variar según el idioma y la versión. Validar en el primer dashboard de cada cliente.

## Encabezado con una franja de fondo completo
1. Poner el logo del cliente, el título, los controles y el logo de BINATSA dentro de **un contenedor horizontal** a todo el ancho, de 80 px de alto.
2. Darle al contenedor el color oscuro de la marca.
3. En cada objeto de adentro (logo, título, controles), panel **Diseño**: fondo y borde en ninguno. Entre controles, un objeto en blanco angosto del mismo color de la franja.
4. Solo el logo de BINATSA lleva fondo blanco, para que se lea.

## Un guion "-" para valores 0 o nulos en tablas
- **Nulos:** clic derecho en la medida, **Formato**, pestaña **Panel**, **Valores especiales**, y escribir `-` en el texto.
- **Ceros:** en el formato de número, elegir **Personalizado** y escribir `#,##0;-#,##0;"-"` (el tercer bloque es el cero). Para porcentajes, `0.0%;-0.0%;"-"`.

## Sin etiqueta para valores 0 o nulos en gráficos
En **Etiqueta**, formato de número personalizado con el tercer bloque vacío: `#,##0;-#,##0;`. Los valores nulos no dibujan marca, así que tampoco etiqueta.

## Delta sin periodo previo
En el cálculo, devolver nulo cuando no hay valor previo (por ejemplo `IF ISNULL([Valor previo]) OR [Valor previo]=0 THEN NULL ELSE ... END`) y usar el valor especial `-` del formato. Formato del delta: `▲ +0.0%;▼ -0.0%;0.0%`.

## Botones de navegación
Un botón por vista de destino: 164 x 36 px, texto `<Vista> →`, fuente de 11 pt en negrita, texto blanco. Colores por destino con contraste de al menos 4.5:1 (en el tono oscuro de la marca si el color no llega). El botón "📖 Glosario", en gris `#55657A`.

## Parámetros estándar y tamaño
Crear los parámetros Periodo, Desde, Hasta (y Canal o Segmento si aplica) con los nombres y opciones del módulo de estructura. Tamaño de cada vista: Fijo, 2300 x 1300 px.
