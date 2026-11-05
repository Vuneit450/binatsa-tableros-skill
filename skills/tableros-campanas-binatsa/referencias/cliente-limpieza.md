# Vista del cliente y limpieza · Dashboards de Cobranza BINATSA

## Vista del cliente
- Por defecto el cliente ve las dos vistas, Dirección y Operación. Confirmar con el usuario si algún cliente debe ver menos.
- Las hojas de trabajo van ocultas; el cliente solo ve lo que se le comparte.
- Dar permisos a nivel de vista/proyecto solo a esa vista (lo configura el usuario en Tableau Cloud; confirmar con él antes de compartir).
- Cuidar que la vista del cliente no muestre datos de otras campañas ni notas internas. El desglose por asesor SIEMPRE se muestra.
- Probar la vista como la verá el cliente (filtros por defecto, sin marcas seleccionadas).

## Limpieza de huérfanos (cuando el usuario la pida)
1. Inventariar: hojas sin uso en ningún dashboard, orígenes de datos sin hojas, cálculos sin referencias, parámetros sin uso.
2. Cruzar referencias en el XML (.twb) antes de quitar; un cálculo puede usarse dentro de otro, en acciones, filtros o tooltips.
3. Ocultar hojas que el cliente no consulta (no borrar si hay duda); quitar solo lo confirmado sin referencias.
4. Campos: solo ocultar (hidden='true'), sin tocar consultas. No ocultar campos que el reporte usa o usará aunque hoy no tengan datos. Ocultar no reduce el tamaño del extracto.
5. Hacerlo en copia versionada, entregar un resumen de lo quitado/ocultado y que el usuario publique.
