# Libro de prueba para publicar en Tableau Cloud

`prueba_publicacion.twbx` sirve solo para comprobar que el token y el script `skills/tableros-campanas-binatsa/herramientas/publicar_libro.py` funcionan. **Todos los datos son inventados** (20 filas: segmento, asesor, saldo, recuperado), así que puede estar en este repo público.

Contenido:
- Una hoja, "Saldo por segmento": barras horizontales con la rampa de segmentos de la paleta BINATSA.
- Un dashboard, "Prueba de publicación", de 1200×800.
- El CSV va empaquetado dentro del `.twbx`, así que no pide credenciales de ninguna base de datos.

Se regenera con:
```bash
python skills/tableros-campanas-binatsa/herramientas/crear_libro_prueba.py
```

## Publicarlo (desde tu computadora, con las variables del token ya guardadas)

Desde la carpeta del repo:
```bash
python skills/tableros-campanas-binatsa/herramientas/publicar_libro.py --listar-proyectos
```
```bash
python skills/tableros-campanas-binatsa/herramientas/publicar_libro.py ejemplos/libro-prueba/prueba_publicacion.twbx --proyecto "Pruebas" --nombre "BINATSA prueba de publicacion"
```
```bash
python skills/tableros-campanas-binatsa/herramientas/publicar_libro.py ejemplos/libro-prueba/prueba_publicacion.twbx --proyecto "Pruebas" --nombre "BINATSA prueba de publicacion" --publicar
```
1. El primero confirma que el token conecta y muestra los proyectos.
2. El segundo solo simula.
3. El tercero publica e imprime la URL.

Después, abre la URL y confirma que se ve la gráfica. Si Tableau marca un error al abrir el libro (y no al publicarlo), el problema está en el XML del libro de prueba y no en el token: avísale a Claude con el mensaje exacto.

Este libro se generó a mano en XML, sin Tableau Desktop. **No se ha abierto todavía en Tableau.**
