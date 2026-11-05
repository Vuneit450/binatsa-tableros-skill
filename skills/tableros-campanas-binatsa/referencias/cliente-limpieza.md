# Vista del cliente y limpieza · Tableros de campañas BINATSA

## Vista del cliente
- **Qué ve:** por defecto, todas las vistas del tablero (Dirección, Operación, Asesores, Guía y glosario y las del giro), salvo las que el usuario marque como internas (pregunta 12 de `SKILL.md`).
- **Asesores:** el desglose por asesor se muestra, por nombre, por defecto; confirmar con el usuario.
- **Solo su campaña:** el cliente nunca ve datos de otras campañas ni de otros clientes. Si un libro tiene varias campañas, cada vista se comparte solo con quien corresponde; si eso no se puede garantizar con permisos, separar en libros o usar seguridad por usuario ("Seguridad por usuario" en `referencias/datos.md`).
- **Permisos:** los configura el usuario en Tableau Cloud, a nivel de proyecto o de vista; confirmar con él antes de compartir.
- **Hojas de trabajo:** ocultas; el cliente solo ve los tableros.
- **Revisar como lo verá el cliente** (filtros por defecto, sin marcas seleccionadas), antes de compartir:
  - ningún marcador sin llenar (`{…}`);
  - ninguna nota interna ni la palabra "pendiente";
  - el enlace "▶ Manual en video" funciona.

## Limpieza de huérfanos (cuando el usuario la pida)
1. **Inventariar:** hojas sin uso en ningún tablero, cálculos sin referencias, parámetros sin uso y orígenes de datos sin hojas.
2. **Cruzar referencias en el XML** (`.twb`) antes de quitar: un cálculo puede usarse dentro de otro, en acciones, filtros o tooltips.
3. **Hojas y cálculos:** ocultar las hojas que el cliente no consulta (no borrar si hay duda); quitar solo lo confirmado sin referencias.
4. **Campos:** solo ocultar (`hidden='true'`), sin tocar consultas. No ocultar campos que el tablero usa o usará aunque hoy no tengan datos. Ocultar no reduce el tamaño del extracto.
5. **Orígenes de datos sin uso:** se reportan, no se quitan, salvo que el usuario lo confirme (nunca se modifican fuentes ni consultas).
6. **Restos del libro original:** como el estilo viene de la plantilla, revisar que no queden hojas, cálculos ni textos del libro anterior del cliente.
7. Hacerlo en una copia versionada, entregar un resumen de lo quitado y ocultado, y publicar según `referencias/publicacion.md`.
