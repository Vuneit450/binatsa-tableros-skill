# binatsa-tableros-skill

Recursos de BINATSA para trabajar con Claude: la skill de tableros de campañas de call center en Tableau Cloud, la marca de BINATSA y ejemplos.

## Contenido

```
marca-binatsa/
  binatsa.svg                 logo vectorial
  paleta-binatsa.md           colores derivados del logo, con contraste y rampa de segmentos
  Preferences-BINATSA.tps     paletas para cargar en Tableau Desktop
  cierre-video.png            tarjeta de cierre fija de los videos guía (logo + eslogan)
skills/
  tableros-campanas-binatsa/   UNA skill para tableros de campañas de call center
    SKILL.md                   entrada: arranque, preguntas, flujo y seguridad
    referencias/               datos, diseño, tooltips, cliente y limpieza, publicación, video guía
      giros/                   métricas y reglas por tipo de campaña (cobranza; ATC, ventas y retenciones por llenar)
    plantillas/                plantilla de Cobranza (.twbx con datos inventados), brief, diccionario y paleta del cliente
    herramientas/              publicar_libro.py, crear_libro_prueba.py y cómo aplicar reglas en Tableau
ejemplos/                      ilustraciones y libro de prueba, todo con datos inventados
```

## Cómo usar la skill

Se usa la carpeta `skills/tableros-campanas-binatsa/` completa: `SKILL.md` es la entrada y dice en qué paso abrir cada referencia. Para usarla desde otra cuenta de Claude, copiar o subir esa carpeta.

## Qué va aquí y qué no

El repositorio es público. Aquí va solo lo que sirve para cualquier campaña: la skill, plantillas vacías, scripts, la marca de BINATSA y ejemplos con datos inventados. Todo lo de un cliente (logo, paleta, brief, reglas, libros, datos, capturas y video) va en la carpeta privada de cada proyecto, `BINATSA-Tableros/<cliente>/<campaña>/`, y nunca se sube.

## Paleta en Tableau

Copiar `marca-binatsa/Preferences-BINATSA.tps` a `Mi repositorio de Tableau/Preferencias/Preferences.tps` y reiniciar Tableau Desktop. Es el método de Desktop 2025.2 y anteriores; en 2026.1 puede no funcionar, y entonces se crean las paletas dentro de Tableau con los hex de `marca-binatsa/paleta-binatsa.md`. Detalles ahí.
