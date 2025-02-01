Here’s the provided statement converted into **Markdown** format:

---

# Despliegue de una Arquitectura Sharded Cluster en MongoDB con Docker - Almacenamiento y gestión de datos distribuidos

## Objetivo
El objetivo de esta actividad es desplegar una arquitectura de base de datos NoSQL MongoDB utilizando contenedores Docker. Se implementará una solución escalable y distribuida mediante la configuración de:

- Un **ReplicaSet de routers (mongos)** para distribuir las solicitudes de los clientes.
- Un **ReplicaSet de servidores de configuración (config server)** para gestionar la metadata del clúster.
- Un **Sharded Cluster** compuesto por tres ReplicaSet, cada uno con tres nodos, para el almacenamiento distribuido de datos.

Al finalizar la actividad, el estudiante comprenderá cómo funciona un entorno MongoDB sharded y será capaz de desplegarlo utilizando contenedores Docker.

---

## Requisitos previos
Antes de comenzar la actividad, asegúrese de contar con los siguientes requisitos:

1. Instalación de **Docker** y **Docker Compose** en su entorno de trabajo.
2. Conocimientos básicos de **MongoDB** y su arquitectura de sharding.
3. Conocimientos básicos de configuración de entornos en **Docker**.

---

## Instrucciones

### 1. Crear la estructura de archivos necesaria:
- Crear un directorio de trabajo denominado `mongo-sharded-cluster` o similar, un nombre descriptivo.
- Dentro del directorio, crear un archivo `docker-compose.yml` para definir los servicios.

### 2. Definir los servicios en Docker Compose:
- Configurar un servicio para el **ReplicaSet de configuración (configsvr)** con tres nodos.
- Configurar un servicio para el **ReplicaSet de routers (mongos)** con tres nodos.
- Configurar tres servicios para los **ReplicaSet de shards (shard1, shard2, shard3)**, cada uno con tres nodos.

### 3. Inicialización de los ReplicaSets:
- Acceder a cada contenedor e inicializar los ReplicaSets mediante el shell de MongoDB (`mongo`).
- Configurar los miembros de cada ReplicaSet.

---

## Entregables
El estudiante debe entregar:

1. **Archivo `docker-compose.yml`** con la configuración completa, los scripts necesarios de shell/bash.
2. **Capturas de pantalla** que evidencien:
   - La inicialización exitosa de los ReplicaSets.
   - La adición de shards en el router.
   - La consulta a la base de datos con particionamiento aplicado.
3. **Un informe** describiendo:
   - La estructura del clúster desplegado.
   - Los comandos utilizados paso a paso complementando con las capturas de pantalla.
   - Chunks, collections almacenadas y cómo se distribuyen y pruebas con datasets (aunque sean números).
   - Los desafíos encontrados y cómo fueron resueltos.


# Informe del Sharded Cluster de MongoDB desplegado con Docker Compose

## Estructura del Clúster

### Componentes del Clúster
1. **Routers (mongos):**
   - `mongos1`, `mongos2`, `mongos3`: Servicios que actúan como routers para dirigir las consultas a los shards adecuados.
   - Puertos: `27117`, `27118`, `27119` (externo) → `27017` (interno).
   - Configuración: Conectados al conjunto de réplicas de servidores de configuración (`rs-config-server`).

2. **Config Servers:**
   - `configsvr1`, `configsvr2`, `configsvr3`: Servidores de configuración que almacenan metadatos del clúster.
   - Puertos: `27121`, `27122`, `27123` (externo) → `27020` (interno).
   - Configuración: Conjunto de réplicas llamado `rs-config-server`.

3. **Shards:**
   - Cada shard es un conjunto de réplicas con tres nodos (`a`, `b`, `c`).
   - **Shard 1:** `shard1a`, `shard1b`, `shard1c`.
    - Puertos: `27131`, `27132`, `27133` (externo) → `27030` (interno).
   - **Shard 2:** `shard2a`, `shard2b`, `shard2c`. 
    - Puertos: `27134`, `27135`, `27136` (externo) → `27030` (interno).
   - **Shard 3:** `shard3a`, `shard3b`, `shard3c`. 
    - Puertos: `27137`, `27138`, `27139` (externo) → `27030` (interno).

4. **Red:**
   - Todos los servicios están conectados a la red Docker `big_sharded_cluster`.

### Diagrama del Clúster
Incluir un diagrama que ilustre la estructura del clúster.

![Diagrama del Clúster](imgs/sharded_cluster_diagram.png)

---

## Comandos Utilizados

En esta sección, se detallan los comandos utilizados para desplegar y configurar el clúster MongoDB sharded.

### Paso 1: Desplegar el Clúster con Docker Compose
```bash
docker-compose -f big_sharded_cluster.yml up
```

### Paso 2: Inicializar los Config Servers
Conectarse a uno de los servidores de configuración (ej. `configsvr1`) e inicializar el conjunto de réplicas y su script de inicialización:
```bash
docker exec configsvr1 sh -c "mongosh --port 27020 < /scripts/configserver-init.js"
```
Script de inicialización (automáticamente subido en docker usando volumenes):
```javascript
rs.initiate({
    _id: "rs-config-server",
    configsvr: true,
    members: [
      { _id: 0, host: "configsvr1:27020" },
      { _id: 1, host: "configsvr2:27020" },
      { _id: 2, host: "configsvr3:27020" }
    ]
  });
```

### Paso 3: Inicializar los Shards
Conectarse a cada shard e inicializar el conjunto de réplicas. Por ejemplo, para `shard1` y `shard2`:
```bash
docker exec shard1a sh -c "mongosh --port 27030 < /scripts/shard1-init.js"

docker exec shard2a sh -c "mongosh --port 27030 < /scripts/shard2-init.js"
```
Script de inicialización (automáticamente subido en docker usando volumenes):
```javascript
rs.initiate({
    _id: "shard1",
    members: [
      { _id: 0, host: "shard1a:27030" },
      { _id: 1, host: "shard1b:27030" },
      { _id: 2, host: "shard1c:27030" }
    ]
  });
```
Repetir este proceso para `shard3`.

### Paso 4: Agregar Shards al Router (mongos)
Conectarse a uno de los routers (ej. `mongos1`):
```bash
docker exec mongos1 sh -c "mongosh --port 27017 < /scripts/router-init.js"
```
Scrip para añadir los nodos al cluster:
```javascript
sh.addShard("shard1/shard1a:27030");
sh.addShard("shard2/shard2a:27030");
sh.addShard("shard3/shard3a:27030");
```

### Capturas de Pantalla

![docker con todos los contenedores funcionando](imgs/compose_up.png)
![docker exec configsvr1 sh -c "mongosh --port 27020 < /scripts/configserver-init.js"](imgs/configserver_init.png)
![docker exec mongos1 sh -c "mongosh --port 27017 < /scripts/router-init.js"](imgs/shards_added.png)
![docker exec -it mongos1 mongosh --port 27017 and use bigdatabase](imgs/use_bigdatabase.png)
![check of sharding working 30% each shard](imgs/test_sharding.png)


### Comprobación del estado
`sh.status()` nos proporciona un informe del estado de nuestro sharded cluster
```bash
docker exec -it mongos1 mongosh --port 27017
sh.status()
```
---

## Chunks, Collections y Distribución de Datos

En esta sección, se describen los chunks, collections, y cómo se distribuyen los datos en el clúster.

### Habilitar Sharding para una Base de Datos y Colección
Conectarse a un router (`mongos`) y habilitar el sharding para una base de datos y colección:
```javascript
use bigdatabase;
sh.enableSharding("bigdatabase");
sh.shardCollection("bigdatabase.testCollection", { _id: "hashed" });
```
in case that an error like the following appears create an index for the id
*MongoServerError[InvalidOptions]: Please create an index that starts with the proposed shard key before sharding the collection.*

### Distribución de Datos
- **Chunks:** Los datos se dividen en chunks basados en el shard key (`_id` en este caso).
- **Shards:** Los chunks se distribuyen entre los shards (`shard1`, `shard2`, `shard3`).

### Pruebas con Datasets
- **Dataset de Prueba:** Insertar datos en la colección `bigdatabase`.
- **Resultados:** Verificar la distribución de datos entre los shards.

```javascript
use bigdatabase;

for (let i = 0; i < 25000; i++) {
    db.testCollection.insert({
        _id: i,
        value: "A".repeat(10000), // Campo de texto con 10 KB
        metadata: {
            description: "Texto adicional para aumentar el tamaño del documento",
            data: "B".repeat(20000) // Otro campo con 20 KB
        }
    });
}
```

Verificar la distribución:
```javascript
db.testCollection.getShardDistribution()
```
o
```javascript
sh.status()
```
---

## Desafíos Encontrados y Soluciones

En esta sección, se describen los desafíos encontrados durante el despliegue y configuración del clúster, y cómo fueron resueltos.

### Desafío 1: Problema de Inicialización de los Config Servers
- **Descripción:** Los servidores de configuración no se inicializaban correctamente, los puertos del script y el docker compose no eran los mismos.
- **Solución:** Verificar que todos los contenedores estén en ejecución y que la red Docker esté configurada correctamente.

### Desafío 2: Errores al Agregar Shards
- **Descripción:** Al agregar shards al router, se producían errores de conexión.
- **Solución:** Asegurarse de que los shards estén correctamente inicializados y que los nombres de los hosts sean accesibles desde el router.

### Desafío 3: flags
- **Descripción:** desconocimiento de las flags necesarias para realizar la tarea
- **Solución:** 
    1. **`--port <XXXX>:`**
        Specifies the port on which the mongos router listens (default MongoDB port).
    2. **`--configdb <replicaSetName/containerName:port>`**
        Specifies the configuration server replica set (rs-config-server) and its member.
    3. **`--configsvr`**
        Enables config server mode.
    4. **`--bind_ip_all`**
        Binds the mongos process to all available IP addresses, allowing connections from any network interface.
    5. **`--replSet <name>`**
        Specifies the name of the replica set.
    6. **`--shardsvr`**
        Enables shard server mode.
---

## Conclusión

El clúster MongoDB sharded fue desplegado exitosamente utilizando Docker Compose. Se realizaron pruebas con datasets para validar su funcionamiento, y los desafíos encontrados fueron resueltos satisfactoriamente.

---

## Anexos

- **Scripts de Inicialización:** 
    - router-init
        - mongos-init.js
    - shard-init
        - shard1-init.js
        - shard2-init.js
        - shard3-init.js
    - configserver-init.js
- **Referencias:** 
    - https://phoenixnap.com/kb/mongodb-sharding
    - https://medium.com/@yasasvi/mongodb-sharding-with-docker-c8b18bee32eb

---------

docker run -d --name shard4a --net big_sharded_cluster -p 27140:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all

docker run -d --name shard4b --net big_sharded_cluster -p 27141:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all

docker run -d --name shard4c --net big_sharded_cluster -p 27142:27030 mongo --replSet shard4 --shardsvr --port 27030 --bind_ip_all

---------