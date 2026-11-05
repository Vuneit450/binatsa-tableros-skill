# Ejemplos visuales

Ilustraciones de referencia para los skills. Reproducen el estilo del tablero de referencia (franjas negras, tarjetas, botones, mapa de calor, tooltip) con **datos inventados**: no hay cifras, nombres de asesores, nombres de clientes ni identificadores reales.

**No son capturas de Tableau.** Están dibujadas con código: la tipografía y los detalles de render difieren un poco de los de Tableau. Sirven para ver la estructura, las proporciones y el estilo; las medidas exactas están en `skills/tableros-campanas-binatsa/referencias/diseno.md`.

## Archivos
| Archivo | Qué muestra | Módulo que lo usa |
|---|---|---|
| `encabezado.png` | Ícono del cliente, título, controles, logo de BINATSA y botones | estructura |
| `tarjeta-kpi.png` | Una tarjeta KPI: título en franja, número y deltas | kpis |
| `franja-bloque.png` | Franja de título de bloque con su subtítulo | estructura |
| `tooltip.png` | Un tooltip completo, con sus cinco secciones | tooltips |
| `mapa-calor.png` | Mapa de calor con su selector de KPI | estructura |
| `tabla-asesores.png` | Tabla por asesor | estructura |
| `vista-direccion.png` | Vista Dirección completa | estructura |
| `vista-operacion.png` | Vista Operación completa | estructura |
| `guia-uso.png` | Vista Guía de uso | estructura |

## Reglas para agregar o cambiar imágenes
- El repositorio es PÚBLICO: ninguna imagen puede mostrar nombres de clientes, cifras reales de cobranza, identificadores de asesores ni credenciales. Usar datos de ejemplo.
- Si el estilo del tablero cambia, regenerar las ilustraciones sin alterar su estilo y actualizar este archivo.
- Recortar al elemento que se ilustra; peso máximo de 1 MB por imagen.
- Cada módulo que use una imagen la enlaza junto a la regla y deja la descripción en texto al lado, para que sirva aunque quien lee no pueda ver imágenes.
