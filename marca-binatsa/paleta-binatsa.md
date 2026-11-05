# Paleta BINATSA

Sale de los dos colores del logo (`marca-binatsa/binatsa.svg`). Lo demás son derivados.

## Colores de marca

| Nombre | Hex | Uso |
|---|---|---|
| Azul marino (secundario) | `#0B1F3A` | Texto de marca, segmento más oscuro de la rampa, acentos |
| Turquesa (PRIMARIO) | `#00B3B8` | Color principal de la marca y del logo. Sobre blanco da 2.6:1: no usarlo tal cual en barras, líneas, números ni como fondo de texto blanco; para eso, su tono oscuro |
| Turquesa oscuro (tono oscuro del primario) | `#007F84` | Franjas de encabezado de zona y de título de tarjeta (texto blanco, 4.8:1), barra destacada (la más alta), líneas, selección, número de las tarjetas KPI y texto sobre fondo claro |

## Neutros (con matiz hacia el azul marino, no gris puro)

| Nombre | Hex | Uso |
|---|---|---|
| Texto principal | `#14202E` | Casi negro, nunca `#000000` |
| Texto secundario | `#55657A` | Subtítulos, etiquetas de ejes |
| Barras no destacadas | `#8093A8` | Todas las barras menos la destacada (3.2:1 con blanco) |

Fondos: todo transparente (regla del módulo de estructura).

## Rampa de segmentos de cartera (menos mora = más claro)

Un solo color por segmento, igual en TODAS las hojas. Máximo 6 pasos; esta rampa tiene 5. Todos los pasos llegan a 3:1 con blanco (mínimo para gráficos sobre fondo transparente); por eso el paso 1 no es un turquesa pastel.

| Paso | Hex | Para |
|---|---|---|
| 1 (más claro) | `#09A2AB` | Segmento con menos mora |
| 2 | `#078289` | |
| 3 | `#056368` | |
| 4 | `#04474A` | |
| 5 (más oscuro) | `#0B1F3A` | Segmento con más mora |

Si el cliente tiene menos segmentos, tomar pasos salteados (por ejemplo 3 segmentos: 1, 3 y 5).

## Semáforo (fijo, no depende de la marca)

| Estado | Hex |
|---|---|
| Mejora | `#2e7d32` |
| Empeora | `#c62828` |
| Alerta (marcas, flechas y números grandes) | `#C77700` |
| Alerta (texto pequeño) | `#9A5A00` |

Siempre acompañar el color con el símbolo ▲ / ▼, para que se entienda sin distinguir colores.

## Contraste (texto blanco sobre el color)

| Color | Contraste | Resultado |
|---|---|---|
| `#0B1F3A` | 16.5:1 | Cumple |
| `#007F84` | 4.8:1 | Cumple |
| `#00B3B8` | 2.6:1 | **No cumple**: no poner texto blanco encima |

Sobre turquesa `#00B3B8` el texto legible es azul marino `#0B1F3A` (6.4:1).

## Para Tableau

`Preferences-BINATSA.tps` trae tres paletas: categórica, secuencial de segmentos y semáforo divergente. Es el método clásico: copiarlo a `Mi repositorio de Tableau/Preferencias/Preferences.tps` y reiniciar Tableau Desktop. La documentación de Tableau lo presenta como el método de Desktop 2025.2 y anteriores; no está confirmado que Tableau 2026.1 lo siga leyendo, así que probarlo primero.

Si no aparecen las paletas: desde Tableau 2025.3 se pueden crear dentro de Desktop (tarjeta Color de Marcas, o menú Formato del libro). Crear tres paletas con los mismos nombres y los hex de este documento (categórica, secuencial de segmentos y semáforo).
