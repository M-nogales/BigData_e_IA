# Objetivos

- Uso básico de Docker
- Uso básico de Docker Compose
- Creación de infraestructuras básicas con Docker y Docker Compose

# Conceptos

Todos los conceptos y experimentos vistos en clase están en el material de GitBook.

# Bibliografía Básica

- Web del software: [https://www.docker.com/](https://www.docker.com/)
- Documentación oficial: [docker.com/get-started/](https://docker.com/get-started/)
- Hub de Docker: [docker.com/](https://docker.com/)
- Yaml: 
  - [redhat.com/es/topics/automation/what-is-yaml](https://www.redhat.com/es/topics/automation/what-is-yaml)
  - [redhat.com/sysadmin/yaml-beginners](https://www.redhat.com/sysadmin/yaml-beginners)
- Guía no oficial: [com/](https://com/)

# Ejercicios

### EJ1. (10 mins.) Repaso conceptos básicos

Responde a las siguientes cuestiones, adjuntando una o varias capturas de pantalla para demostrar la validez de tu respuesta.

1. ¿Cómo sabemos cuál es la versión de Docker que tenemos instalada?
2. ¿Cuántos contenedores hay funcionando en tu PC?
3. Pon a funcionar un contenedor usando la imagen de Debian.
4. Detén el contenedor que has creado.
5. Elimina el contenedor que has creado.

### EJ2. (20 mins.)

Crea un contenedor Debian, accede a él desde dos puntos simultáneamente, luego ejecuta un comando sobre él, deténlo y elimínalo. Usa los comandos: `create`, `start`, `attach`, `exec`, `stop` y `rm`.

- Nombre el contenedor como "test1" con la opción `--name`.
- Publica esta imagen en tu DockerHub.

Adjunta una o varias capturas de pantalla para demostrar la validez de tu respuesta y el enlace a tu imagen en DockerHub.

# Problemas

Debes documentar paso a paso cómo realizar los siguientes problemas, usando despliegue orquestado e imágenes oficiales, en nuestro DockerHub:

### P1. (20 mins.) Crear un back-end de gestión de BBDD con phpMyAdmin y MySQL

Enlace de utilidad: [https://hub.docker.com/r/phpmyadmin/phpmyadmin/](https://hub.docker.com/r/phpmyadmin/phpmyadmin/)

### P2. (90 mins.)

Crear las pilas (X)AMP y (X)EMP para despliegue de proyectos web usando:

- Para XAMP: (X=cualquier OS), Apache Server, MySQL con phpMyAdmin y PHP.
- Para XEMP: (X=cualquier OS), Nginx, MySQL con phpMyAdmin y PHP.

Enlaces de utilidad:
- [Infraestructura LAMP con Docker Compose](https://openwebinars.net/blog/infraestructura-lamp-con-docker-compose/)
- Documentación de la imagen nginx en: [https://hub.docker.com/nginx/](https://hub.docker.com/nginx/)
- Configuración del servidor nginx: [http://nginx.org/en/docs/beginners_guide.html#conf_structure](http://nginx.org/en/docs/beginners_guide.html#conf_structure)

### P3. (100 mins.)

Crear un servidor Tomcat con MySQL-phpMyAdmin para despliegue de aplicaciones web con Java. Se despliega un `.war` (necesitarás uno de prueba).

Enlace de utilidad: [https://devops4solutions.com/deploy-a-tomcat-application-using-docker-compose/](https://devops4solutions.com/deploy-a-tomcat-application-using-docker-compose/)

**Nota**: Debe poderse demostrar el correcto funcionamiento de PHP/Java y MySQL interconectados, es decir, que se debe hacer al menos una consulta simple a la base de datos desde la aplicación, tal y como se describe en los enlaces de utilidad.
