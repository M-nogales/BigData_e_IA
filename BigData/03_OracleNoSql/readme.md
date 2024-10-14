Comandos para crear un contenedor en docker con Oracle NoSql database
```powershell
docker pull ghcr.io/oracle/nosql:latest-ce
docker tag ghcr.io/oracle/nosql:latest-ce oracle/nosql:ce
docker run -d --name=kvlite --hostname=kvlite --env KV_PROXY_PORT=8080 -p 8080:8080 oracle/nosql:ce

```
Comprobar el estado del contenedor con un ping 
```powershell
docker run --rm -ti --link kvlite:store oracle/nosql:ce java -jar lib/kvstore.jar ping -host store -port 5000
```
ejemplo de consulta en la base de datos
```powershell
PS C:\Users\Manuel Nogales> docker run --rm -ti --link kvlite:store oracle/nosql:ce java -jar lib/kvstore.jar runadmin -host store -port 5000 -store kvstore

kv-> execute "CREATE TABLE myTable1 (id INTEGER, name STRING, age INTEGER, PRIMARY KEY(id))"
Statement completed successfully
```
Los comandos están diseñados para configurar y gestionar una instancia de Oracle NoSQL utilizando imágenes de contenedores.

### Primer bloque de comandos:
```powershell
docker pull ghcr.io/oracle/nosql:latest-ce
```
**Explicación:**  
Este comando descarga una imagen de Docker desde un registro remoto, en este caso desde el registro GitHub Container Registry (GHCR) con la imagen de Oracle NoSQL. Específicamente, está obteniendo la versión más reciente de la edición "Community Edition" (CE) de Oracle NoSQL (`latest-ce`).  
**Conceptos clave:**
- `docker pull`: Comando para descargar una imagen de Docker desde un registro.
- `ghcr.io/oracle/nosql:latest-ce`: La ubicación en el registro y el nombre de la imagen, seguido de la etiqueta `latest-ce`, que indica que se está descargando la última versión de la edición comunitaria.

---

```powershell
docker tag ghcr.io/oracle/nosql:latest-ce oracle/nosql:ce
```
**Explicación:**  
Este comando renombra (o reetiqueta) la imagen descargada en tu máquina local. Está asignando un alias más corto (`oracle/nosql:ce`) para que sea más fácil referirse a la imagen en los siguientes pasos.  
**Conceptos clave:**
- `docker tag`: Comando que asigna una nueva etiqueta (o alias) a una imagen ya existente.
- `ghcr.io/oracle/nosql:latest-ce`: Imagen original que se descargó desde el registro.
- `oracle/nosql:ce`: Nueva etiqueta asignada a la imagen para referenciarla más fácilmente.

---

```powershell
docker run -d --name=kvlite --hostname=kvlite --env KV_PROXY_PORT=8080 -p 8080:8080 oracle/nosql:ce
```
**Explicación:**  
Este comando ejecuta la imagen de Oracle NoSQL en un contenedor de Docker. A continuación te explico cada parte en detalle:

- `docker run`: Crea y ejecuta un contenedor basado en la imagen especificada.
- `-d`: Ejecuta el contenedor en segundo plano (modo "detached"). El proceso de NoSQL funcionará sin bloquear la terminal.
- `--name=kvlite`: Asigna el nombre `kvlite` al contenedor, facilitando su referencia en otros comandos.
- `--hostname=kvlite`: Define el nombre de host dentro del contenedor como `kvlite`.
- `--env KV_PROXY_PORT=8080`: Configura una variable de entorno dentro del contenedor para definir que el puerto del proxy de Oracle NoSQL será el 8080.
- `-p 8080:8080`: Mapea el puerto 8080 del contenedor al puerto 8080 del sistema host, permitiendo acceder al servicio desde fuera del contenedor.
- `oracle/nosql:ce`: Especifica la imagen que se utilizará para crear el contenedor (en este caso, la imagen que renombraste anteriormente).

---

### Segundo bloque de comandos (ver estado haciendo un ping):
```powershell
docker run --rm -ti --link kvlite:store oracle/nosql:ce java -jar lib/kvstore.jar ping -host store -port 5000
```
**Explicación:**

Este comando verifica el estado del contenedor de Oracle NoSQL ejecutando un "ping" a la base de datos. Aquí te explico cada parte:

- `docker run`: Crea y ejecuta un contenedor.
- `--rm`: Elimina automáticamente el contenedor cuando el comando termina. Esto es útil para contenedores que solo se utilizan temporalmente.
- `-ti`: Combina `-t` (asigna una pseudo-terminal) y `-i` (mantiene la entrada estándar abierta). Esto permite que interactúes con el contenedor en modo interactivo.
- `--link kvlite:store`: Conecta este contenedor temporal con el contenedor `kvlite`, asignándole el alias `store`. Esto permite que el contenedor actual se comunique con `kvlite`.
- `oracle/nosql:ce`: Especifica que se utilizará la misma imagen de Oracle NoSQL.
- `java -jar lib/kvstore.jar ping`: Ejecuta una aplicación Java desde la imagen para hacer un "ping" al servicio de Oracle NoSQL, utilizando el archivo `kvstore.jar`.
- `-host store -port 5000`: Define que la conexión se realiza al host `store` (alias para `kvlite`) en el puerto 5000, donde normalmente opera el servicio de NoSQL.

Este comando básicamente envía una señal de "ping" a la base de datos para verificar si está activa y funcionando correctamente en el puerto 5000.

---

### Tercer bloque de comandos (creación de tabla):
```powershell
docker run --rm -ti --link kvlite:store oracle/nosql:ce java -jar lib/kvstore.jar runadmin -host store -port 5000 -store kvstore
```
**Explicación:**

Este comando ejecuta la consola administrativa de Oracle NoSQL para realizar operaciones en la base de datos. Vamos por partes:

- `docker run`: Ejecuta un contenedor.
- `--rm`: Elimina el contenedor cuando termina la ejecución.
- `-ti`: Ejecuta en modo interactivo con una terminal.
- `--link kvlite:store`: Conecta este contenedor con el contenedor `kvlite`, para poder acceder a la base de datos en ejecución.
- `oracle/nosql:ce`: Usa la imagen de Oracle NoSQL.
- `java -jar lib/kvstore.jar runadmin`: Ejecuta la herramienta de administración (`runadmin`) proporcionada por Oracle NoSQL.
- `-host store -port 5000`: Se conecta al servicio de NoSQL ejecutándose en el host `store` (alias para `kvlite`) en el puerto 5000.
- `-store kvstore`: Especifica que se trabajará con el almacén de datos llamado `kvstore`.

Después de conectarse a la consola administrativa, puedes ejecutar comandos SQL para gestionar la base de datos. En este caso, ejecutas el siguiente comando para crear una tabla:
```sql
CREATE TABLE myTable1 (id INTEGER, name STRING, age INTEGER, PRIMARY KEY(id))
```
**Explicación del SQL:**  
Crea una tabla llamada `myTable1` con tres columnas:
- `id`: Un entero que actúa como clave primaria (única).
- `name`: Un campo de texto (STRING).
- `age`: Otro entero.

El comando `Statement completed successfully` confirma que la tabla se creó correctamente.