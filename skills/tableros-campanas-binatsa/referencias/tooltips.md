# Tooltips · Tableros de campañas BINATSA

Obligatorios en todo gráfico, tabla y tarjeta. Formato de 5 secciones del tablero de referencia más reciente; igual en todas las hojas, en este orden (referencia visual: `ejemplos/tooltip.png`):
1. Título: 14 pt, negrita, verde `#2E7D32`.
2. Línea de contexto (opcional): "ℹ️" y una frase corta de lo que representa la fila o la marca, 10 pt, gris `#757575`.
3. Datos: una línea por dato, con emoji + etiqueta (11 pt) + valor dinámico en negrita (12 pt), en color de texto `#1B1F23` (por ejemplo "👤 Asesor: …", "💵 Monto recuperado: …"). El asesor siempre por su nombre, nunca por login o ID.
4. Línea divisoria de guiones largos ("────────────────────────"), 8 pt, gris claro `#C9D1D6`.
5. Si la hoja tiene la categoría del giro (por ejemplo segmentos o buckets), desglose: encabezado en negrita "📊 Por <categoría> — <métrica>" y una línea por categoría con ■ en su color (el mismo de las gráficas), su nombre y el valor en negrita.
6. Cinco secciones, cada una con "▸" en negrita (11 pt), su emoji y su título en negrita de 10 pt; el cuerpo, de 1 a 3 líneas, en 10 pt color `#3D464D`:
   - "▸ 🔎 QUÉ MIDE": qué valor cuenta. Título en `#1F4E79`.
   - "▸ 🧮 CÓMO SE CALCULA": fórmula en palabras, cómo se compone y, si la métrica tiene semáforo, sus umbrales (por ejemplo "verde ≤ 20 s"). Título en `#9A5A00`. Un detalle más largo puede ir debajo en 9 pt gris `#757575`.
   - "▸ 📖 TÉRMINOS QUE APARECEN AQUÍ": viñetas con el término en negrita y su definición corta. Título en `#1F4E79`. Si la hoja no usa siglas ni términos nuevos, esta sección puede omitirse.
   - "▸ 🧭 CÓMO LEERLO": cómo interpretar la vista (orden, qué buscar). Título en `#6F42C1`.
   - "▸ 🎯 PARA QUÉ SIRVE ESTA VISTA": la decisión que ayuda a tomar. Título en `#2E7D32`.
7. Notas al final, en gris `#757575`: la leyenda de rangos de las categorías (9 pt, por ejemplo "A = 06-30 días · B = 31-60 · C = 61-90", según el cliente); una nota "⚠️ Ojo: …" para limitaciones de los datos (9 pt, `#8A5A00`); una nota de contexto de la campaña (8 pt); y "Respeta los filtros … de arriba" (9 pt). Sin pie de campaña adicional.

Los colores de las secciones son decoración de lectura; el verde y el ámbar repiten los del semáforo de `referencias/diseno.md` (el ámbar en su variante oscura para texto pequeño). Gris de notas: `#757575` (4.6:1 con blanco), no uno más claro. Palabras prohibidas: "Texto visible" en `referencias/diseno.md`.

## Control "Descripciones: Mostrar / Ocultar"
Cada vista con tooltips lleva un control "💬 Descripciones" (Mostrar / Ocultar) en la fila de filtros del encabezado, al final, junto al último filtro y con su mismo formato (título, fuente, color, contenedor y separador). Nunca flotando encima de otros objetos: para hacerle espacio se acorta el título. Las vistas sin tooltips de secciones (Guía y glosario, por ejemplo) no lo llevan. Con "Ocultar" el tooltip deja solo el título y los datos; las secciones (de la línea divisoria hacia abajo) desaparecen sin borrarse. Se aplica con `herramientas/descripciones.py` (cada texto de sección pasa a un cálculo que solo se muestra con "Mostrar", con el mismo formato). Por defecto: "Mostrar".

## En XML (.twb)
- `<customized-tooltip><formatted-text><run …>` dentro del pane de cada worksheet.
- Salto de línea = `<run>Æ&#10;</run>`.
- Campos dinámicos como runs CDATA `<[datasource].[campo]>`.
- Trabajar en una copia versionada del .twbx; reempaquetar con el .twb, Data/Extracts y Image intactos. Publica quien diga "Quién publica" en `SKILL.md`.
