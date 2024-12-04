# Objetivos

- Instalación y familiarización con MongoDB
- Operaciones CRUD con MongoDB
- Indexación con MongoDB
- Relaciones entre colecciones en MongoDB

# Conceptos

Todos los conceptos y experimentos vistos en clase están en las diapositivas relativas a la EPD4.

# Bibliografía

- MongoDB Documentación Oficial:  
  [https://www.mongodb.com/docs/manual/](https://www.mongodb.com/docs/manual/)

- MongoDB: Notes for Professionals. GoalKicker – Free Programming Books:  
  [https://books.goalkicker.com/MongoDBBook/](https://books.goalkicker.com/MongoDBBook/)

# Problema 0: Puesta en marcha del entorno MongoDB

Instalar MongoDB en una instancia contenerizada utilizando Docker.

Encontrará un archivo `.yml` necesario en el campus virtual y las explicaciones necesarias en el material del GitBook de la asignatura. Una vez creada, conéctese a una instancia de mongo en ejecución, cree una base de datos llamada `mongo_practica`.

Debe utilizar la Shell de MongoDB para realizar los siguientes Problemas de la práctica.

A partir de ahora, documente todas sus consultas en un archivo JavaScript para usar como referencia.

# Problema 1: Inserción

Crea una colección llamada `series` dentro de la base de datos `mongo_practica`.

Inserta los siguientes documentos en la colección `videojuegos`:

```javascript
// Documento 1
{
  title: "The Legend of Zelda: Breath of the Wild",
  genre: ["Action", "Adventure"],
  platform: ["Nintendo Switch", "Wii U"],
  releaseYear: 2017,
  rating: 9.4
}

// Documento 2
{
  title: "The Witcher 3: Wild Hunt",
  genre: ["Action", "RPG"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2015,
  rating: 9.2
}

// Documento 3
{
  title: "Minecraft",
  genre: ["Survival", "Adventure"],
  platform: ["PC", "PlayStation", "Xbox", "Mobile"],
  releaseYear: 2011,
  rating: 8.7
}

// Documento 4
{
  title: "Fortnite",
  genre: ["Battle Royale"],
  platform: ["PC", "PlayStation", "Xbox", "Mobile"],
  releaseYear: 2017,
  rating: 8.0
}

// Documento 5
{
  title: "Dark Souls III",
  genre: ["Action", "RPG"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2016,
  rating: 8.9
}

// Documento 6
{
  title: "Red Dead Redemption 2",
  genre: ["Action", "Adventure"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2018,
  rating: 9.8
}

// Documento 7
{
  title: "Super Mario Odyssey",
  genre: ["Platform"],
  platform: ["Nintendo Switch"],
  releaseYear: 2017,
  rating: 8.9
}

// Documento 8
{
  title: "Overwatch",
  genre: ["FPS", "Action"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2016,
  rating: 8.5
}

// Documento 9
{
  title: "Grand Theft Auto V",
  genre: ["Action", "Adventure"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2013,
  rating: 9.5
}

// Documento 10
{
  title: "Dota 2",
  genre: ["MOBA"],
  platform: ["PC"],
  releaseYear: 2013,
  rating: 8.4
}

// Documento 11
{
  title: "League of Legends",
  genre: ["MOBA"],
  platform: ["PC"],
  releaseYear: 2009,
  rating: 8.7
}

// Documento 12
{
  title: "Call of Duty: Modern Warfare",
  genre: ["FPS"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2019,
  rating: 8.2
}

// Documento 13
{
  title: "Animal Crossing: New Horizons",
  genre: ["Simulation"],
  platform: ["Nintendo Switch"],
  releaseYear: 2020,
  rating: 8.5
}

// Documento 14
{
  title: "Halo 3",
  genre: ["FPS"],
  platform: ["Xbox 360"],
  releaseYear: 2007,
  rating: 9.2
}

// Documento 15
{
  title: "Elden Ring",
  genre: ["Action", "RPG"],
  platform: ["PlayStation", "Xbox", "PC"],
  releaseYear: 2022,
  rating: 9.5
}
```
# Problema 2: Búsqueda

1. Encuentra todos los videojuegos cuyo género incluya "Action".
2. Encuentra el videojuego con el título "Fortnite" y actualiza su calificación a 8.5.
3. Encuentra todos los videojuegos con una calificación mayor a 9.0 y ordénalos de forma descendente según su año de lanzamiento.
4. Encuentra todos los videojuegos que tengan una calificación mayor a 8.7 y que pertenezcan al género "Adventure".
5. Encuentra el videojuego con el título más largo en la colección.
6. Encuentra todos los videojuegos lanzados en o después de 2017.
7. Encuentra dos videojuegos cuyo título comience con la letra "T".
8. Encuentra todos los videojuegos lanzados después de 2015 y con una calificación mayor o igual a 8.5.
9. Encuentra todos los videojuegos cuyo género incluya "RPG" y que tengan plataforma "PC".
10. Encuentra el videojuego con el menor número de plataformas.
11. Encuentra todos los videojuegos cuyo género incluya "FPS" y se lanzaron después de 2010.
12. Encuentra y actualiza el título "The Witcher 3: Wild Hunt" para agregar un nuevo género "Fantasy".
13. Encuentra videojuegos que estén disponibles en más de una plataforma y tengan una calificación de 9.0 o superior.
14. Encuentra todos los videojuegos que incluyan en su título la palabra "New".
15. Encuentra el videojuego con el rating más bajo y actualiza su calificación añadiendo 0.5 puntos.

# Problema 3: Actualización

1. Actualiza el número de plataformas del videojuego "Minecraft" agregando "Nintendo Switch".
2. Actualiza el rating del videojuego "Red Dead Redemption 2" a 9.9.
3. Agrega el género "Strategy" al videojuego "Dota 2".
4. Incrementa en 1 la cantidad de plataformas del videojuego "The Witcher 3: Wild Hunt" añadiendo "Nintendo Switch".
5. Actualiza "Minecraft" para incluir una sinopsis descriptiva del juego.
6. Cambia el título de "League of Legends" a "LoL" y su año de lanzamiento a 2010.
7. Añade la plataforma "Nintendo Switch" a "League of Legends".
8. Incrementa en 1 el rating de todos los videojuegos que tienen un rating inferior a 8.0.

# Problema 4: Eliminación

1. Elimina el documento del videojuego con el título "Fortnite" de la colección.
2. Elimina el campo de calificación del videojuego "Dark Souls III".
3. Elimina todos los videojuegos que tengan un rating inferior a 8.0.
4. Elimina todos los videojuegos que tengan menos de 3 plataformas.
5. Elimina todos los videojuegos que sean del género "MOBA".
6. Elimina el campo de género de todos los videojuegos que tengan un rating inferior a 8.0.
7. Elimina todos los videojuegos lanzados antes de 2010.
8. Elimina el videojuego con el menor número de plataformas.

# Problema 5: Indexación

1. Crea un índice de texto en el campo "title".
2. Crea un índice compuesto en los campos "genre" y "rating".
3. Crea un índice descendente en el campo "title" y ascendente en el campo "releaseYear".
4. Crea un índice de texto en el campo "platform".

# Problema 6: Relaciones

Inserta los siguientes documentos en la colección `users`:

```javascript
{
  username: "SuperCoder123",
  first_name: "Super",
  last_name: "Coder"
}

{
  username: "TechGuru99",
  full_name: {
    first: "Tech",
    last: "Guru"
  }
}
```

Inserta los siguientes documentos en la colección posts:

```javascript
{
  username: "SuperCoder123",
  title: "Solves a coding challenge",
  body: "Optimizes the algorithm and achieves maximum efficiency."
}

{
  username: "SuperCoder123",
  title: "Shares coding tutorials",
  body: "Helps aspiring coders with step-by-step guides and examples."
}

{
  username: "TechGuru99",
  title: "Discovers a software vulnerability",
  body: "Reports it to the developers for prompt fixing."
}

{
  username: "TechGuru99",
  title: "Creates an innovative tech product",
  body: "Introduces a groundbreaking invention to simplify everyday tasks"
}
```

Inserta los siguientes documentos en la colección comments:

```javascript
{

 username: "SuperCoder123",

 comment: "Hope you got a good deal!",

 post: ObjectId("post_obj_id")

}

Donde post_obj_id es el ObjectId del documento de publicación “Solves a coding challenge ".

{

 username: "SuperCoder123",

 comment: "What's mine is yours!",

 post: ObjectId("post_obj_id")

}

Donde post_obj_id es el ObjectId del documento de publicación “Discovers a software vulnerability ".

{

 username: "SuperCoder123",

 comment: "Don't violate the licensing agreement!",

 post: ObjectId("post_obj_id")

}

Donde post_obj_id es el ObjectId del documento de publicación “Shares coding tutorials".

{

 username: "TechGuru99",

 comment: "It still isn't clean",

 post: ObjectId("post_obj_id")

}

Donde post_obj_id es el ObjectId del documento de publicación “Solves a coding challenge ".

{

 username: "TechGuru99",

 comment: "Denied your PR because I found a hack",

 post: ObjectId("post_obj_id")

}

Donde post_obj_id es el ObjectId del documento de publicación “Shares coding tutorials ".

```

1. Encuentra todos los usuarios.
2. Encuentra todas las publicaciones.
3. Encuentra todas las publicaciones escritas por "SuperCoder123".
4. Encuentra todas las publicaciones escritas por "TechGuru99".
5. Encuentra todos los comentarios.
6. Encuentra todos los comentarios escritos por "SuperCoder123".
7. Encuentra todos los comentarios escritos por "TechGuru99".
8. Encuentra todos los comentarios pertenecientes a la publicación “Shares coding tutorials"

# Problema 7: Consultas avanzadas

1. Encuentra todos los videojuegos cuyo título contiene la palabra 'Legend'.
   - Encuentra los videojuegos cuyo título termine con la letra 'e'.
   - Ordena los videojuegos encontrados por el año de lanzamiento en orden descendente.

2. Encuentra todos los videojuegos con más de dos géneros.
   - Filtra los videojuegos que tengan más de tres plataformas.
   - Encuentra el videojuego con más géneros en su lista.

3. Encuentra videojuegos cuya plataforma incluye 'PlayStation' y 'PC'.
   - Encuentra videojuegos que tengan exactamente estas dos plataformas.
   - Ordena los resultados por calificación en orden descendente.

4. Encuentra videojuegos lanzados después de 2015 que sean de género 'Action' o 'RPG'.
   - Encuentra cuántos videojuegos cumplen esta condición.
   - Calcula el promedio de calificaciones para estos videojuegos.

# Problema 8: Operaciones de agrupación y agregación

1. Encuentra el promedio de calificaciones y el total de videojuegos por género.
2. Calcula también el año más reciente de lanzamiento por género.
3. Encuentra los géneros con un promedio de calificación superior a 9.0.
4. Supón que cada videojuego se vende 1,000 veces. Calcula el ingreso total por plataforma.
5. Encuentra la plataforma que genera los mayores ingresos.
6. Calcula también el promedio de ingresos por plataforma.
7. Combina las colecciones `series` y `users` para encontrar los nombres de usuarios que compraron juegos de género 'RPG'.
8. Encuentra también los usuarios que compraron videojuegos con calificación mayor a 9.0.
9. Genera un listado de usuarios con los títulos de los videojuegos que han comprado.

# Problema 9: Uso de índices

1. Crea un índice compuesto en `title` (texto) y `releaseYear` (descendente).
2. Realiza una consulta que utilice este índice y analiza su rendimiento con `explain()`.
3. Verifica si este índice mejora las consultas que filtran por ambos campos.
4. Usa el método `explain()` para analizar el uso del índice en una consulta que filtre videojuegos por palabras clave en el título.
5. Prueba la consulta con y sin el índice.
6. Compara el tiempo de ejecución y el número de documentos examinados.
7. Crea un índice parcial para incluir solo los videojuegos con calificación mayor a 9.0.
8. Realiza una consulta que filtre videojuegos con calificación mayor a 9.0 y analiza su rendimiento.
9. Encuentra los videojuegos con el índice parcial que pertenezcan al género 'Adventure'.

# Problema 10: Relaciones complejas

1. Inserta una nueva compra para un usuario existente.
2. Encuentra todos los usuarios que han realizado compras.
3. Actualiza el historial de compras de un usuario para incluir un nuevo videojuego.
4. Inserta más comentarios relacionados con los posts de los usuarios.
5. Encuentra todos los comentarios realizados por un usuario específico.
6. Cuenta el número total de comentarios por usuario.
7. Encuentra todas las publicaciones con sus respectivos comentarios.
8. Encuentra las publicaciones con más de dos comentarios.
9. Ordena las publicaciones por el número de comentarios de forma descendente.

# Problema 11: Persistencia

1. Persiste los resultados de videojuegos agrupados por género en una nueva colección llamada `genre_analysis`.
2. Añade también el campo de género con el número de plataformas promedio por género.
3. Encuentra los géneros que tienen más de cinco videojuegos y persiste solo esos resultados.
4. Exporta la colección `users` en formato JSON.
5. Exporta también la colección `series` en formato JSON.
6. Genera un archivo JSON con los videojuegos que tienen calificación superior a 9.0.

# Problema 12: Ejecución de scripts

1.  Documenta todas las consultas realizadas en un archivo `mongo_practica.js` para ejecutarlas directamente desde la shell.
2.  Divide las consultas en secciones según el problema que resuelven.
3.  Incluye comentarios en cada consulta explicando su propósito.
4.  Crea una función en JavaScript que permita buscar videojuegos según condiciones específicas pasadas como parámetro.
5.  Extiende la función para incluir un parámetro opcional que ordene los resultados.
6.  Agrega un límite de resultados en la función para devolver solo los primeros `n` documentos encontrados.

# Datos de la Práctica

## Estimación temporal:

### Parte presencial: 240 minutos.
- Explicación y resolución de dudas: 90 minutos.
- Creación del entorno y primer contacto: 30 minutos.

### Parte no presencial: 5-10 horas dependiendo de la destreza técnica del alumno.
- Lectura y estudio del guión y bibliografía básica: 60-90 minutos.
- Problemas: 10 h.
