# Tooltips · Dashboards de Cobranza BINATSA

Obligatorios en todo gráfico, tabla y tarjeta. Formato tomado de los tooltips de las hojas visibles del libro de referencia más reciente; copiarlo en todas las hojas, en este orden (referencia visual: `ejemplos/tooltip.png`):
1. Título: 14 pt, negrita, verde `#2E7D32`.
2. Línea de contexto (opcional): "ℹ️" y una frase corta de lo que representa la fila o la marca, 10 pt, gris `#757575`.
3. Datos: una línea por dato, con emoji + etiqueta (11 pt) + valor dinámico en negrita (12 pt), en color de texto `#1B1F23` (por ejemplo "👤 Asesor: …", "💵 Monto recuperado: …").
4. Línea divisoria de guiones largos ("────────────────────────"), 8 pt, gris claro `#C9D1D6`.
5. Si la hoja tiene segmentos de cartera, desglose: encabezado en negrita "📊 Por segmento — <métrica>" y una línea por segmento con ■ en el color de ese segmento en la rampa de segmentos, el nombre del segmento y el valor en negrita.
6. Cinco secciones, cada una con "▸" en negrita (11 pt), su emoji y su título en negrita de 10 pt; el cuerpo, de 1 a 3 líneas, en 10 pt color `#3D464D`:
   - "▸ 🔎 QUÉ MIDE": qué valor cuenta. Título en `#1F4E79`.
   - "▸ 🧮 CÓMO SE CALCULA": fórmula en palabras, cómo se compone. Título en `#9A5A00`.
   - "▸ 📖 TÉRMINOS QUE APARECEN AQUÍ": viñetas con el término en negrita y su definición corta. Título en `#1F4E79`. Si la hoja no usa siglas ni términos nuevos, esta sección puede omitirse.
   - "▸ 🧭 CÓMO LEERLO": cómo interpretar la vista (orden, qué buscar). Título en `#6F42C1`.
   - "▸ 🎯 PARA QUÉ SIRVE ESTA VISTA": la decisión que ayuda a tomar. Título en `#2E7D32`.
7. Notas al final, en gris `#757575`: la leyenda de rangos de los segmentos (9 pt, por ejemplo "A = 06-30 días · B = 31-60 · C = 61-90", según el cliente); una nota "⚠️ Ojo: …" para limitaciones de los datos (9 pt, `#8A5A00`); una nota de contexto de la campaña (8 pt); y "Respeta los filtros … de arriba" (9 pt). Sin pie de campaña adicional.

Los colores de las secciones son decoración de lectura; el verde y el ámbar repiten los del semáforo de `referencias/diseno.md` (el ámbar en su variante oscura para texto pequeño). El libro de referencia usa gris `#8A949C` en las notas, pero da 3.1:1 con blanco; usar `#757575` (4.6:1). No poner en ningún tooltip nombres de servidores o tablas, "Excel" ni sistemas internos (ver "Texto visible" en `referencias/diseno.md`).

## En XML (.twb)
- `<customized-tooltip><formatted-text><run …>` dentro del pane de cada worksheet.
- Salto de línea = `<run>Æ&#10;</run>`.
- Campos dinámicos como runs CDATA `<[datasource].[campo]>`.
- Trabajar en copia del .twbx sobre el archivo que el usuario subió; reempaquetar con el .twb, Data/Extracts y Image intactos; el usuario publica.
