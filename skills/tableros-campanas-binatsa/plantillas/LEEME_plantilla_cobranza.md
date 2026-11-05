# Plantilla BINATSA · Cobranza (versión 0.4.2)

Hecha a partir del tablero de referencia de Cobranza más reciente. Todo lo del cliente se reemplazó por datos y nombres inventados.

## Qué trae
- Vistas: Dirección, Operación, Asesores y Guía y glosario, en 2300 x 1300.
- Datos inventados dentro del libro (`Data/datos/`):
  - `resumen_diario.csv`: 15 asesores ficticios, 3 canales y 120 días hasta la fecha en que se generó.
  - `detalle_llamadas.csv`: 30 días de llamadas.
- Logo de cliente genérico (`Image/logo-cliente.png`) y logo de BINATSA.

## Ya aplicado
- Fondo blanco.
- Franja y botones en azul marino BINATSA (`#0b1f3a`), que se cambia por el color oscuro del cliente.
- Botones "<Vista> →" y "📖 Guía y glosario".
- Dirección con 6 tarjetas por fila.
- Semáforo oscuro (verde `#2e7d32`, rojo `#c62828`).
- Resaltar al pasar el mouse por Canal y por Asesor en cada vista, sin las tarjetas.
- Enlace "▶ Manual en video" con dirección de marcador.

## Marcadores que se cambian en cada proyecto
| Marcador | Dónde | Por qué se cambia |
|---|---|---|
| `{Campaña}` | Título de cada vista | Nombre de la campaña |
| `{Cliente}` | Textos | Nombre del cliente |
| `Canal 1`, `Canal 2`, `Canal 3` y `CANAL_1…3` | Parámetro Canal, cálculo Canal, textos | Canales o segmentos reales |
| `https://URL-DEL-VIDEO` | Enlace "▶ Manual en video" | Dirección del video de ese tablero |
| `{Fuente 1}`, `{Fuente 2}`, `{frecuencia}`, `{fecha}` | Guía y glosario, "Fuentes y límites" | Fuentes y actualización reales |
| `{limitación de los datos, si la hay}` | Una nota de tooltip | Limitación real, si existe |
| `{Contexto de la campaña…}` y `{Descripción del canal}` | Tooltips y Guía y glosario | Qué cartera es y qué significa cada canal |
| Catálogo de asesores | Cálculo "Asesor" | Logins → nombres reales |
| Metas de ejemplo (4,000 llamadas, casos, vueltas) | Vista Asesores | Metas del cliente, o quitar la vista si no hay |
| `logo-cliente.png` | Arriba a la izquierda | Logo del cliente |
| `#0b1f3a` y colores de canales | Franja, botones y gráficas | Paleta del cliente |

## Probada
La v0.1 se abrió en Tableau y funcionó (Dirección, Asesores y Guía). La v0.2 corrige lo que se vio:
- Quitada una nota de contexto del cliente que quedaba en 34 tooltips (ahora `{Contexto de la campaña…}`).
- Títulos "· Asesores" y "· Guía y glosario"; subtítulo "{Cliente} · <pregunta>".
- Saltos de línea de "Fuentes y límites" (ya no muestra "Æ").

## Versión 0.3
- Deltas: "-" cuando no hay periodo para comparar; "0.0%" o "0.0 pp" en gris cuando el cambio redondeado es cero (antes salía ▼ 0.0 en rojo).
- Sin ejes ni títulos de ejes en ninguna hoja (los valores se leen con etiquetas).
- "¿Quién cumple la meta cada día?": solo color, sin número (las celdas eran demasiado angostas).
- Canales con la rampa BINATSA (`#09a2ab`, `#056368`, `#0b1f3a`), iguales en las dos fuentes de datos.

## Versión 0.4
- Línea ℹ️ junto a los botones en Dirección, Operación y Asesores.
- Operación: "¿Cuánto se marca cada día?" es un mapa de calor canal × día (antes, barras).
- Clic en un día (respaldo acordado): filtra los gráficos de la vista, pero no las tarjetas, para que sus deltas no se rompan.
- Guía y glosario: línea "Si algo no cuadra, avisar a {contacto}".
- "vs 7 días previos" (etiqueta y valor) solo aparece con rangos de más de 7 días.

## Para activar "Día seleccionado" (opción completa) en Tableau Desktop
Hace que las tarjetas también muestren el día elegido contra el día anterior y contra 7 días antes. Se activa a mano porque su ajuste de "limpiar selección" no se puede verificar sin Tableau.
1. Crear el parámetro "Día seleccionado" (fecha, valor actual 01/01/1900).
2. En los cálculos "Desde (periodo)" y "Hasta (periodo)" de las dos fuentes, envolver la fórmula: `IF [Día seleccionado] > #1900-01-01# THEN [Día seleccionado] ELSE (fórmula actual) END`.
3. Dashboard → Acciones → Agregar acción → Cambiar valor del parámetro, en cada gráfico con días: campo de origen = Día; parámetro = Día seleccionado; al borrar la selección: "Establecer valor en" 01/01/1900.
4. En las acciones de filtro de esos gráficos, volver a poner las tarjetas como destino.
5. Probar: clic en un día → tarjetas de ese día; clic fuera → todo regresa al periodo.

## Pendiente
- Selector de métrica en "¿Cuánto se marca cada día?" (hoy muestra llamadas).
- Probar en Tableau la v0.4 completa.
