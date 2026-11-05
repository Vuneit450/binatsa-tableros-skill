# Herramientas para trabajar con Tableau desde una carpeta local

Contiene `publicar_libro.py` (publica) y `crear_libro_prueba.py` (genera un libro de prueba con datos inventados). `publicar_libro.py` que publica un libro en Tableau Cloud con un token de acceso personal. **No se ha probado contra un sitio real**: la primera vez, usar un libro de prueba en un proyecto de pruebas.

## Preparación (una sola vez)

### 1. Crear el token
1. En Tableau Cloud, abrir la configuración de tu cuenta (tu nombre, arriba a la derecha).
2. Pestaña **Configuración**, sección **Tokens de acceso personal**.
3. Escribir un nombre que diga para qué es (por ejemplo `USO-CLAUDE`) y pulsar **Crear token**.
4. Tableau muestra el **secreto una sola vez**. Copiarlo en ese momento a un lugar seguro. Si se pierde, hay que borrar el token y crear otro.
5. Anotar la fecha de caducidad que muestre Tableau y revocar el token al terminar el proyecto.

El token actúa como el usuario que lo creó: alcanza todo lo que esa cuenta puede ver y hacer, y no pide el segundo factor de autenticación. Por eso conviene crearlo desde una cuenta dedicada con acceso mínimo (ver "Permisos mínimos y datos sensibles" en `SKILL.md`).

### 2. Guardarlo como variables de entorno (nunca en un archivo ni en el chat)
Las cuatro variables, con estos nombres:

| Variable | Qué lleva |
|---|---|
| `TABLEAU_SERVER` | el servidor, sin `https://` (por ejemplo `10ax.online.tableau.com`) |
| `TABLEAU_SITE` | el nombre del sitio en la dirección (vacío si es el sitio Default) |
| `TABLEAU_PAT_NAME` | el nombre del token |
| `TABLEAU_PAT_SECRET` | el secreto |

En Windows (PowerShell), una variable por línea; después hay que cerrar y abrir la terminal:
```powershell
setx TABLEAU_SERVER "tu-servidor"
setx TABLEAU_SITE "tu-sitio"
setx TABLEAU_PAT_NAME "USO-CLAUDE"
setx TABLEAU_PAT_SECRET "el-secreto"
```
En macOS o Linux, agregar al perfil de la terminal (`~/.zshrc` o `~/.bashrc`):
```bash
export TABLEAU_SERVER="tu-servidor"
export TABLEAU_SITE="tu-sitio"
export TABLEAU_PAT_NAME="USO-CLAUDE"
export TABLEAU_PAT_SECRET="el-secreto"
```
Escribir esos comandos directamente en tu terminal, no en el chat con Claude.

### 3. Instalar lo necesario
```bash
pip install tableauserverclient
```
Opcional, para leer extractos `.hyper` en local: `pip install tableauhyperapi`.

### 4. Probar paso a paso
Para la primera prueba usa el libro con datos inventados `ejemplos/libro-prueba/prueba_publicacion.twbx` (instrucciones en `ejemplos/libro-prueba/README.md`).

```bash
python skills/tableros-campanas-binatsa/herramientas/publicar_libro.py --listar-proyectos
python skills/tableros-campanas-binatsa/herramientas/publicar_libro.py libro/mi_libro_v1.twbx --proyecto "Pruebas" --nombre "Mi libro"
python skills/tableros-campanas-binatsa/herramientas/publicar_libro.py libro/mi_libro_v1.twbx --proyecto "Pruebas" --nombre "Mi libro" --publicar
```
- El primero muestra los proyectos que ve el token: confirma que conecta y qué alcance tiene.
- El segundo solo simula y dice si crearía o sobrescribiría.
- El tercero publica. Si el proyecto no tiene "prueba" en su nombre, exige además `--confirmo-produccion`.
- Cada publicación se anota en `publicaciones.log` (fecha, archivo, proyecto, nombre e id; sin el token).

### 5. Después de publicar
Revisar el resultado en el navegador con tu sesión (la sesión de Claude no escribe tu contraseña). Las credenciales de la fuente de datos se incrustan desde Tableau Desktop, no por este script.
