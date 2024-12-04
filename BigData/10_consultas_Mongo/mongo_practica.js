//! use VideogamesDB
//! Problema 1
//*Crea una colección llamada `series` dentro de la base de datos `mongo_practica`.
db.games.insertMany([
    {
      title: "The Legend of Zelda: Breath of the Wild",
      genre: ["Action", "Adventure"],
      platform: ["Nintendo Switch", "Wii U"],
      releaseYear: 2017,
      rating: 9.4
    },
    {
      title: "The Witcher 3: Wild Hunt",
      genre: ["Action", "RPG"],
      platform: ["PlayStation", "Xbox", "PC"],
      releaseYear: 2015,
      rating: 9.2
    },
    {
      title: "Minecraft",
      genre: ["Survival", "Adventure"],
      platform: ["PC", "PlayStation", "Xbox", "Mobile"],
      releaseYear: 2011,
      rating: 8.7
    },
    {
      title: "Fortnite",
      genre: ["Battle Royale"],
      platform: ["PC", "PlayStation", "Xbox", "Mobile"],
      releaseYear: 2017,
      rating: 8.0
    },
    {
      title: "Dark Souls III",
      genre: ["Action", "RPG"],
      platform: ["PlayStation", "Xbox", "PC"],
      releaseYear: 2016,
      rating: 8.9
    },
    {
      title: "Red Dead Redemption 2",
      genre: ["Action", "Adventure"],
      platform: ["PlayStation", "Xbox", "PC"],
      releaseYear: 2018,
      rating: 9.8
    },
    {
      title: "Super Mario Odyssey",
      genre: ["Platform"],
      platform: ["Nintendo Switch"],
      releaseYear: 2017,
      rating: 8.9
    },
    {
      title: "Overwatch",
      genre: ["FPS", "Action"],
      platform: ["PlayStation", "Xbox", "PC"],
      releaseYear: 2016,
      rating: 8.5
    },
    {
      title: "Grand Theft Auto V",
      genre: ["Action", "Adventure"],
      platform: ["PlayStation", "Xbox", "PC"],
      releaseYear: 2013,
      rating: 9.5
    },
    {
      title: "Dota 2",
      genre: ["MOBA"],
      platform: ["PC"],
      releaseYear: 2013,
      rating: 8.4
    },
    {
      title: "League of Legends",
      genre: ["MOBA"],
      platform: ["PC"],
      releaseYear: 2009,
      rating: 8.7
    },
    {
      title: "Call of Duty: Modern Warfare",
      genre: ["FPS"],
      platform: ["PlayStation", "Xbox", "PC"],
      releaseYear: 2019,
      rating: 8.2
    },
    {
      title: "Animal Crossing: New Horizons",
      genre: ["Simulation"],
      platform: ["Nintendo Switch"],
      releaseYear: 2020,
      rating: 8.5
    },
    {
      title: "Halo 3",
      genre: ["FPS"],
      platform: ["Xbox 360"],
      releaseYear: 2007,
      rating: 9.2
    },
    {
      title: "Elden Ring",
      genre: ["Action", "RPG"],
      platform: ["PlayStation", "Xbox", "PC"],
      releaseYear: 2022,
      rating: 9.5
    }
  ])

//! Problema 2
//1. Encuentra todos los videojuegos cuyo género incluya "Action".
db.games.find({"genre":"Action"})

//2. Encuentra el videojuego con el título "Fortnite" y actualiza su calificación a 8.5.
db.games.update({"title":"Fortnite"},{$set:{"rating":8.5}})

//3. Encuentra todos los videojuegos con una calificación mayor a 9.0 y ordénalos de forma descendente según su año de lanzamiento.
db.games.find({"rating":{$gte:9}}).sort({"releaseYear":-1})

//4. Encuentra todos los videojuegos que tengan una calificación mayor a 8.7 y que pertenezcan al género "Adventure".
db.games.find({$and:[{"rating":{$gt:8.7}}, {"genre":"Adventure"}]})

//5. Encuentra el videojuego con el título más largo en la colección.
db.games.aggregate([
  {
    $project: {
      title: 1,
      titleLength: { $strLenCP: "$title" }
    }
  },
  {
    $sort: { titleLength: -1 }
  }
])

//6. Encuentra todos los videojuegos lanzados en o después de 2017.
db.games.find({"releaseYear":{$gte:2017}})

//7. Encuentra dos videojuegos cuyo título comience con la letra "T".
db.games.find({"title":/^T/}).limit(2)

//8. Encuentra todos los videojuegos lanzados después de 2015 y con una calificación mayor o igual a 8.5.
db.games.find({$and:[{"rating":{$gte:8.5}}, {"releaseYear":{$gt:2015}} ]})

//9. Encuentra todos los videojuegos cuyo género incluya "RPG" y que tengan plataforma "PC".
db.games.find({$and:[{"genre":"FPS"}, {"platform":"PC"}]})

//10. Encuentra el videojuego con el menor número de plataformas.
db.games.aggregate([
    {
      $group:{
        _id:"$title",
        minPlatforms:{$min:{$size:"$platform"}}
      },
    },
    {
      $sort:{"minPlatforms":1}
    }
  
])

//11. Encuentra todos los videojuegos cuyo género incluya "FPS" y se lanzaron después de 2010.
db.games.find({$and:[{"genre":"MOBA"}, {"rating":{$gte:8.5}}]})

//12. Encuentra y actualiza el título "The Witcher 3: Wild Hunt" para agregar un nuevo género "Fantasy".
db.games.updateOne({"title":"The Witcher 3: Wild Hunt"},{$push:{"genre":"Fantasy"}})

// tambien se  puede:
db.games.updateOne({"title":"The Witcher 3: Wild Hunt"},{$set:{"genre":["Action", "RPG", "Fantasy"]}})

//13. Encuentra videojuegos que estén disponibles en más de una plataforma y tengan una calificación de 9.0 o superior.
db.games.find({$and:[{"platform":{$not:{$size:1}}}, {"rating":{$gte:9}}]})

//14. Encuentra todos los videojuegos que incluyan en su título la palabra "New".
db.games.find({"title":/New/})

//15. Encuentra el videojuego con el rating más bajo y actualiza su calificación añadiendo 0.5 puntos.
//db.games.find().sort({ rating: 1 })
db.games.updateOne({ rating: {$lte:8.2} }, { $inc: { rating: 0.5 } })

//! Problema 3
//1. Actualiza el número de plataformas del videojuego "Minecraft" agregando "Nintendo Switch".
db.games.updateOne({"title":"Minecraft"},{$push:{"platform":"Nintendo Switch"}})

//2. Actualiza el rating del videojuego "Red Dead Redemption 2" a 9.9.
db.games.updateOne({"title":"Red Dead Redemption 2"},{$set:{"rating":"9.9"}})

//3. Agrega el género "Strategy" al videojuego "Dota 2".
db.games.updateOne({"title":"Dota 2"},{$push:{"genre":"Strategy"}})

//4. Incrementa en 1 la cantidad de plataformas del videojuego "The Witcher 3: Wild Hunt" añadiendo "Nintendo Switch".
db.games.updateOne({"title":"The Witcher 3: Wild Hunt"},{$push:{"platform":"Nintendo Switch"}})

//5. Actualiza "Minecraft" para incluir una sinopsis descriptiva del juego.
db.games.updateOne({"title":"Minecraft"},{$set:{"description":"Minecraft is a 3D sandbox adventure game developed by Mojang Studios where players can interact with a fully customizable three-dimensional world made of blocks and entities"}})

//6. Cambia el título de "League of Legends" a "LoL" y su año de lanzamiento a 2010.
db.games.updateOne({"title":"League of Legends"},{$set:{"title":"LOL","releaseYear":2010}})

//7. Añade la plataforma "Nintendo Switch" a "League of Legends".
db.games.updateOne({"title":"LOL"},{$push:{"platform":"Nintendo Switch"}})

//8 Incrementa en 1 el rating de todos los videojuegos que tienen un rating inferior a 8.0.
db.games.updateMany({"rating":{$lt:8.0}},{$inc:{"rating":1}})

//! Problema 4
//! aquí descubrí que no hace falta poner "" para los campos .-.

//1. Elimina el documento del videojuego con el título "Fortnite" de la colección.
db.games.deleteOne({ title: "Fortnite" });

//2. Elimina el campo de calificación del videojuego "Dark Souls III".
db.games.updateOne({ title: "Dark Souls III" },{ $unset: { rating: "" } });

//3. Elimina todos los videojuegos que tengan un rating inferior a 8.0.
//! no hay ninguno con menos de 8, min es 8
db.games.deleteMany({ rating: { $lt: 8.0 } });

//4. Elimina todos los videojuegos que tengan menos de 3 plataformas.
//! size + $gt-$lt nope
//db.games.deleteMany({ platform: { $size: { $lt: 3 } } });
db.games.find({
  $or: [
    { platform: { $size: 0 } },
    { platform: { $size: 1 } },
    { platform: { $size: 2 } }
  ]
});

//5. Elimina todos los videojuegos que sean del género "MOBA".
db.games.deleteMany({ genre: "MOBA" });

//6. Elimina el campo de género de todos los videojuegos que tengan un rating inferior a 8.0.
//!no hay ninguno con menos de 8
db.games.updateMany(
  { rating: { $lt: 8.0 } },
  { $unset: { genre: "" } }
);

//7. Elimina todos los videojuegos lanzados antes de 2010.
db.games.deleteMany({ releaseYear: { $lt: 2010 } });

//8. Elimina el videojuego con el menor número de plataformas.
//Encontrar el videojuego en concreto
db.games.aggregate([
  {
      $addFields: { platformCount: { $size: "$platform" } } // Calcula el tamaño del array platform
  },
  {
      $sort: { platformCount: 1 }
  },
  {
      $limit: 1
  },
  {
      $merge: {
          into: "games_delete", 
          whenMatched: "merge",
          whenNotMatched: "insert"
      }
  }
]);

// Después, elimina el videojuego identificado
db.games.deleteOne(
  { _id: { $in: db.games_delete.distinct("_id") } }
);

//! Problema 5

//1. Crea un índice de texto en el campo "title".
db.games.createIndex({ title: "text" });

//2. Crea un índice compuesto en los campos "genre" y "rating".
db.games.createIndex({ genre: 1, rating: 1 },{name:"genders and ratings"});

//3. Crea un índice descendente en el campo "title" y ascendente en el campo "releaseYear".
db.games.createIndex({ title: -1, releaseYear: 1 });

//4. Crea un índice de texto en el campo "platform".
// para crear un index del mismo tipo, hay que eliminar el anterior dropIndex()
db.games.createIndex({ platform: text });
// MongoServerError[IndexOptionsConflict]: An equivalent index already exists with a different name and options. Requested index: { v: 2, key: { _fts: "text", _ftsx: 1 }, name: "platform_text", weights: { platform: 1 }, default_language: "english", language_override: "language", textIndexVersion: 3 }, existing index: { v: 2, key: { _fts: "text", _ftsx: 1 }, name: "title_text", weights: { title: 1 }, default_language: "english", language_override: "language", textIndexVersion: 3 }

//* db.games.getIndexes() | db.games.getIndices()

//! Problema 6
//*Inserta los siguientes documentos en la colección `users`:
db.users.insertMany([{
  username: "SuperCoder123",
  first_name: "Super",
  last_name: "Coder"
},
{
  username: "TechGuru99",
  full_name: {
    first: "Tech",
    last: "Guru"
  }
}])
//
db.posts.insertMany([{
  username: "SuperCoder123",
  title: "Solves a coding challenge",
  body: "Optimizes the algorithm and achieves maximum efficiency."
},
{
  username: "SuperCoder123",
  title: "Shares coding tutorials",
  body: "Helps aspiring coders with step-by-step guides and examples."
},
{
  username: "TechGuru99",
  title: "Discovers a software vulnerability",
  body: "Reports it to the developers for prompt fixing."
},
{
  username: "TechGuru99",
  title: "Creates an innovative tech product",
  body: "Introduces a groundbreaking invention to simplify everyday tasks"
}])
// para saber los ids de los posts dados los titulos
db.posts.find({ title: "Solves a coding challenge" }, { _id: 1 });
//
db.comments.insertMany([
  {
    username: "SuperCoder123",
    comment: "Hope you got a good deal!",
    post: ObjectId("674f2946e965c82c1f64d870")
  },
  {
    username: "SuperCoder123",
    comment: "What's mine is yours!",
    post: ObjectId("674f2946e965c82c1f64d872")
  },
  {
    username: "SuperCoder123",
    comment: "Don't violate the licensing agreement!",
    post: ObjectId("674f2946e965c82c1f64d871")
  },
  {
    username: "TechGuru99",
    comment: "It still isn't clean",
    post: ObjectId("674f2946e965c82c1f64d870")
  },
  {
    username: "TechGuru99",
    comment: "Denied your PR because I found a hack",
    post: ObjectId("674f2946e965c82c1f64d871")
  }
]);

//1. Encuentra todos los usuarios.
db.users.find()

//2. Encuentra todas las publicaciones.
db.posts.find()

//3. Encuentra todas las publicaciones escritas por "SuperCoder123".
db.users.find({ username: "SuperCoder123" })

//4. Encuentra todas las publicaciones escritas por "TechGuru99".
db.posts.find({ username: "TechGuru99" })

//5. Encuentra todos los comentarios.
db.comments.find()

//6. Encuentra todos los comentarios escritos por "SuperCoder123".
db.comments.find({ username: "SuperCoder123" })

//7. Encuentra todos los comentarios escritos por "TechGuru99".
db.comments.find({ username: "TechGuru99" })

//8. Encuentra todos los comentarios pertenecientes a la publicación “Shares coding tutorials"
db.users.find({ title: "Shares coding tutorials" }, { _id: 1 });
db.comments.find({ post: ObjectId("674f2946e965c82c1f64d871") });

//! Problema 7

/*
1. Encuentra todos los videojuegos cuyo título contiene la palabra 'Legend'.
   - Encuentra los videojuegos cuyo título termine con la letra 'e'.
   - Ordena los videojuegos encontrados por el año de lanzamiento en orden descendente.
*/
db.games.find({
  $or: [
    { title: /Legend/ },
    { title: /e$/ }
  ]
})
.sort({ releaseYear: -1 })

/*
2. Encuentra todos los videojuegos con más de dos géneros.
   - Filtra los videojuegos que tengan más de tres plataformas.
   - Encuentra el videojuego con más géneros en su lista.

*/
// https://www.mongodb.com/docs/manual/reference/operator/query/expr/
db.games.aggregate([
  { 
    $match: { 
      $expr: { 
        $gt: [{ $size: "$platform" }, 3]  // Más de tres plataformas
      }
    }
  },
  { 
    $project: { 
      title: 1, 
      numGenres: { $size: "$genre" }  // Contamos cuántos géneros tiene el videojuego
    }
  },
  { 
    $sort: { numGenres: -1 }  // Ordenamos por el número de géneros en orden descendente
  }
])

/*
3. Encuentra videojuegos cuya plataforma incluye 'PlayStation' y 'PC'.
   - Encuentra videojuegos que tengan exactamente estas dos plataformas.
   - Ordena los resultados por calificación en orden descendente. 
*/
//! no da resultado, solo existe con las plataformas ['Nintendo Switch', 'Wii U']
//https://www.mongodb.com/docs/manual/reference/operator/query/all/
db.games.find({
  platform: { $size: 2, $all: ['PlayStation', 'PC'] }
})
.sort({ rating: -1 })

/*
4. Encuentra videojuegos lanzados después de 2015 que sean de género 'Action' o 'RPG'.
   - Encuentra cuántos videojuegos cumplen esta condición.
   - Calcula el promedio de calificaciones para estos videojuegos.
*/
db.games.aggregate([
  {
    $match: { 
      releaseYear: { $gt: 2015 },  // Videojuegos lanzados después de 2015
      genre: { $in: ['Action', 'RPG'] }  // Género 'Action' o 'RPG'
    }
  },
  {
    $group: { 
      _id: "$title",  // Agrupamos por el título del videojuego
      avgRating: { $avg: "$rating" }  // Calculamos el promedio de calificación
    }
  },
  //db.games
  {
    $group: {
      games: { $push: { title: "$_id", avgRating: "$avgRating" } },  // Guardamos los títulos y promedios
      totalCount: { $sum: 1 }  // Calculamos el total de videojuegos
    }
  }
])

//! Problema 8

//1. Encuentra el promedio de calificaciones y el total de videojuegos por género.
db.games.aggregate([
  {
    $unwind: "$genre"
  },
  {
    $group: {
      _id: "$genre",
      averageRating: { $avg: "$rating" },
      totalGames: { $sum: 1 }
    }
  }
])

//2. Calcula también el año más reciente de lanzamiento por género.
db.games.aggregate([
  {
    $unwind: "$genre"
  },
  {
    $group: {
      _id: "$genre",
      mostRecentGame: { $max: "$releaseYear" }
    }
  }
])

//3. Encuentra los géneros con un promedio de calificación superior a 9.0.
db.games.aggregate([
  {
    $unwind: "$genre"
  },
  {
    $group: {
      _id: "$genre",
      avgRating: { $avg: "$rating" }
    }
  },
  {
    $match:{
      avgRating: {$gt:9.0}
    }
  }
])

//4. Supón que cada videojuego se vende 1,000 veces. Calcula el ingreso total por plataforma.
//añadir precios a los juegos add_price.py
db.games.aggregate([
  {
    $unwind: "$platform"
  },
  {
    $group: {
      _id: "$platform",
      totalRevenue: { $sum: {$multiply: [1000, "$price"]} }
    }
  },
  {
    $sort: { totalRevenue: -1 }
  }
])

//5. Encuentra la plataforma que genera los mayores ingresos.
db.games.aggregate([
  {
    $unwind: "$platform"
  },
  {
    $group: {
      _id: "$platform",
      totalRevenue: { $sum: {$multiply: [1000, "$price"]} }
    }
  },
  {
    $sort: { totalRevenue: -1 }
  }
])

//6. Calcula también el promedio de ingresos por plataforma.
db.games.aggregate([
  {
    $unwind: "$platform"
  },
  {
    $group: {
      _id: "$platform",
      totalRevenue: { $sum: {$multiply: [1000, "$price"]} },
      avgRevenue: { $avg: {$multiply: [1000, "$price"]} }
    }
  },
  {
    $sort: { totalRevenue: -1 }
  }
])

//7. Combina las colecciones `series` y `users` para encontrar los nombres de usuarios que compraron juegos de género 'RPG'.
//add_purchased_games.py
db.users.aggregate([
  {
    $lookup: {
      from: "games", // Colección de juegos
      localField: "purchased_games._id", // Referencias de los juegos comprados
      foreignField: "_id", // Campo correspondiente en la colección de juegos
      as: "game_details" // Nombre del campo donde se guardarán los detalles de los juegos
    }
  },
  {
    $unwind: "$game_details" // Descompone el array `game_details` para trabajar con cada juego
  },
  {
    $match: {
      "game_details.genre": "RPG" // Filtra juegos cuyo género es 'RPG'
    }
  },
  {
    $project: {
      username: 1,
      "game_details.title": 1
    }
  }
])

//8. Encuentra también los usuarios que compraron videojuegos con calificación mayor a 9.0.
db.users.aggregate([
  {
    $lookup: {
      from: "games", // Colección de juegos
      localField: "purchased_games._id", // Referencias de los juegos comprados
      foreignField: "_id", // Campo correspondiente en la colección de juegos
      as: "game_details" // Nombre del campo donde se guardarán los detalles de los juegos
    }
  },
  {
    $unwind: "$game_details" // Descompone el array `game_details` para trabajar con cada juego
  },
  {
    $match: {
      "game_details.rating": { $gt: 9.0 } // Filtra juegos con calificación mayor a 9.0
    }
  },
  {
    $project: {
      username: 1,
      "game_details.title": 1,
      "game_details.rating": 1
    }
  }
])

//9. Genera un listado de usuarios con los títulos de los videojuegos que han comprado.
db.users.aggregate([
  {
    $lookup: {
      from: "games", // Colección de juegos
      localField: "purchased_games._id", // Referencias de los juegos comprados
      foreignField: "_id", // Campo correspondiente en la colección de juegos
      as: "game_details" // Nombre del campo donde se guardarán los detalles de los juegos
    }
  },
  {
    $unwind: "$game_details" // Descompone el array `game_details` para trabajar con cada juego
  },
  {
    $project: {
      username: 1,
      "game_details.title": 1
    }
  }
])

//! Problema 9

//1. Crea un índice compuesto en `title` (texto) y `releaseYear` (descendente).
//! hay que eliminar el indice de texto anterior para añadir este
db.games.createIndex({ title: "text", releaseYear: -1 })

//2. Realiza una consulta que utilice este índice y analiza su rendimiento con `explain()`.
db.games.find({ $text: { $search: "Legend" } }).sort({ releaseYear: -1 }).explain("executionStats")
//db.games.explain().find({ $text: { $search: "Legend" } }).sort({ releaseYear: -1 })

/*
3. Verifica si este índice mejora las consultas que filtran por ambos campos.
4. Usa el método `explain()` para analizar el uso del índice en una consulta que filtre videojuegos por palabras clave en el título.
5. Prueba la consulta con y sin el índice.

*/
//*Si ves un IXSCAN en lugar de un COLLSCAN, significa que el índice está siendo utilizado
//*totalKeysExamined, totalDocsExamined, y executionTimeMillis indican cuántas claves y documentos se examinaron y cuánto tiempo tomó la consulta.
db.games.dropIndex( "title_text_releaseYear_-1")

db.videojuegos.find({ $text: { $search: "Overwatch" } }).sort({ releaseYear: -1 }).explain("executionStats")

/**
    executionTimeMillis: o,
    totalKeysExamined: 0,
    totalDocsExamined: 11,
    nReturned: 1,
    executionTimeMillisEstimate: 0,
*/

db.games.createIndex({ title: "text", releaseYear: -1 });

db.games.find({ $text: { $search: "Overwatch" } }).sort({ releaseYear: -1 }).explain("executionStats")

/**
    executionTimeMillis: 0,
    totalKeysExamined: 1,
    totalDocsExamined: 1,
    nReturned: 1,
    executionTimeMillisEstimate: 0,
*/

//7. Crea un índice parcial para incluir solo los videojuegos con calificación mayor a 9.0.
db.games.createIndex({ rating: 1 }, { partialFilterExpression: { rating: { $gt: 9.0 } } })

//8. Realiza una consulta que filtre videojuegos con calificación mayor a 9.0 y analiza su rendimiento.
db.games.find({ rating: { $gt: 9.0 } }).explain("executionStats")
/*
    executionTimeMillis: 2,
    totalKeysExamined: 4,
    totalDocsExamined: 4,
    nReturned: 4,
    executionTimeMillisEstimate: 0,
*/

//9. Encuentra los videojuegos con el índice parcial que pertenezcan al género 'Adventure'.
// usamos hint para forzar el uso del indice parcial, si no lo usamos, se usará el indice de genre y ratings
db.games.find({ genre: "Adventure" }).hint("rating_1").explain("executionStats")

//! Problema 10

//1. Inserta una nueva compra para un usuario existente.
db.users.updateOne(
  { "_id": ObjectId("674dedec961b46259ed9a9f8") },
  { 
    $push: { 
      "purchased_games": { "_id": ObjectId("67476f5a31510be117cf3e7a") }
    }
  }
)

//2. Encuentra todos los usuarios que han realizado compras.
db.users.find({
  "purchased_games": { $ne: [] } // Filtra aquellos usuarios que tienen juegos en su historial de compras
})

//3. Actualiza el historial de compras de un usuario para incluir un nuevo videojuego.
db.users.updateOne(
  { "_id": ObjectId("674dedec961b46259ed9a9f8") },
  { 
    $push: { 
      "purchased_games": { "_id": ObjectId("67476f5a31510be117cf3e86") }
    }
  }
)

//4. Inserta más comentarios relacionados con los posts de los usuarios.
db.comments.insertMany([
  {
    "username": "TechGuru99", 
    "comment": "This is an impressive optimization!",
    "post": ObjectId("674f2946e965c82c1f64d870")
  },
  {
    "username": "SuperCoder123", 
    "comment": "Can't wait to see this tech in action!",
    "post": ObjectId("674f2946e965c82c1f64d873") // Referencia al post de TechGuru99
  }
])

//5. Encuentra todos los comentarios realizados por un usuario específico.
db.comments.find({ username: "SuperCoder123" })

//6. Cuenta el número total de comentarios por usuario.
db.comments.aggregate([
  {
    $group: {
      _id: "$username",
      totalComments: { $sum: 1 }
    }
  }
])

//7. Encuentra todas las posts con sus respectivos comentarios.
db.posts.aggregate([
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "post",
      as: "comments"
    }
  }
])

//8. Encuentra las publicaciones con más de dos comentarios.
db.posts.aggregate([
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "post",
      as: "comments"
    }
  },
  {
    $match: {
      $expr: {
        $gt: [{ $size: "$comments" }, 2]
      }
    }
  }
])

//9. Ordena las publicaciones por el número de comentarios de forma descendente.
// puesto que sort no puede tener $size, creamos un campo con el tamaño de los comentarios y lo ordenamos
/* db.posts.aggregate([
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "post",
      as: "comments"
    }
  },
  {
    $sort: {
      $size: "$comments"
    }
  }
 ])
*/
db.posts.aggregate([
  {
    $lookup: {
      from: "comments", // Colección de comentarios
      localField: "_id", // Campo en `posts` que se compara
      foreignField: "post", // Campo en `comments` que se compara
      as: "comments" // Array que contendrá todos los comentarios relacionados
    }
  },
  {
    $addFields: {
      num_comments: { $size: "$comments" } // Cuenta el número de comentarios y lo agrega como nuevo campo
    }
  },
  {
    $sort: {
      num_comments: -1 // Ordena por el número de comentarios de forma descendente
    }
  },
  {
    $project: {
      title: 1,
      num_comments: 1
    }
  }
])


//! Problema 11
//1. Persiste los resultados de videojuegos agrupados por género en una nueva colección llamada `genre_analysis`.
db.games.aggregate([
  {
    $unwind: "$genre" // Descompone el array `genre` para que podamos agrupar por cada género
  },
  {
    $group: {
      _id: "$genre", // Agrupar por género
      games: {
        $push: {
          id: "$_id",
          title: "$title",
          genre: "$genre",
          platform: "$platform",
          releaseYear: "$releaseYear",
          rating: "$rating",
          price: "$price"
        }
      }
    }
  },
  {
    $merge: {
      into: "genre_analysis", // Nombre de la nueva colección
      whenMatched: "merge", // Si ya existe el documento, se fusiona
      whenNotMatched: "insert" // Si no existe, se inserta un nuevo documento
    }
  }
])

//2. Añade también el campo de género con el número de plataformas promedio por género.
db.games.aggregate([
  {
    $unwind: "$genre" // Descompone el array `genre` para que podamos agrupar por cada género
  },
  {
    $group: {
      _id: "$genre", // Agrupa por género
      games: {
        $push: {
          id: "$_id",
          title: "$title",
          genre: "$genre",
          platform: "$platform",
          releaseYear: "$releaseYear",
          rating: "$rating",
          price: "$price"
        }
      },
      avg_platforms: { $avg: { $size: "$platform" } } // Calcula el promedio de plataformas por juego
    }
  },
  {
    $merge: {
      into: "genre_analysis", // Nombre de la nueva colección
      whenMatched: "merge", // Si ya existe el documento, se fusiona
      whenNotMatched: "insert" // Si no existe, se inserta un nuevo documento
    }
  }
])

//3. Encuentra los géneros que tienen más de cinco videojuegos y persiste solo esos resultados.
// el genre es action
db.games.aggregate([
  {
    $unwind: "$genre" // Descompone el array `genre` para poder agrupar por cada género
  },
  {
    $group: {
      _id: "$genre", // Agrupa por género
      games: { $push: "$title" }, // Crea un array con los títulos de los videojuegos de cada género
      count: { $sum: 1 } // Cuenta cuántos videojuegos hay en cada género
    }
  },
  {
    $match: {
      count: { $gt: 5 } // Filtra los géneros que tienen más de 5 videojuegos
    }
  },
  {
    $project: {
      _id: 1, // Género
      games: 1, // Títulos de los juegos
      count: 1 // Número de juegos en ese género
    }
  },
  {
    $merge: {
      into: "genre_analysis2", // Nombre de la nueva colección donde se guardarán los resultados
      whenMatched: "merge", // Si ya existe un documento con el mismo género, se fusiona
      whenNotMatched: "insert" // Si no existe, se inserta un nuevo documento
    }
  }
])
//!los siguientes ejercicios de este problema se han de realizar en el terminal de docker que ejecute mongo, los .json se en este
//4. Exporta la colección `users` en formato JSON.
// mongoexport -u=root -p=example --authenticationDatabase=admin --host=localhost --port=27017 --db=VideogamesDB --collection=users --out=users.json --jsonArray

//5. Exporta también la colección `series` en formato JSON.
// mongoexport -u=root -p=example --authenticationDatabase=admin --host=localhost --port=27017 --db=VideogamesDB --collection=games --out=games.json --jsonArray

//6. Genera un archivo JSON con los videojuegos que tienen calificación superior a 9.0.
// mongoexport -u=root -p=example --authenticationDatabase=admin --host=localhost --port=27017 --db=VideogamesDB  --collection=games --query='{ "rating": { "$gt": 9.0 } }' --out=games_high_rating.json --jsonArray

//! Problema 12

//1.  Documenta todas las consultas realizadas en un archivo `mongo_practica.js` para ejecutarlas directamente desde la shell.
//2.  Divide las consultas en secciones según el problema que resuelven.
//3.  Incluye comentarios en cada consulta explicando su propósito.
// ejercicios 4,5 y 6 en ejercicio12.js 
// node ejercicio12.js