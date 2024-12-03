//! use VideogamesDB

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
//1
db.games.find({"genre":"Action"})
//2
db.games.update({"title":"Fortnite"},{$set:{"rating":8.5}})
//3
db.games.find({"rating":{$gte:9}}).sort({"releaseYear":-1})
//4
db.games.find({$and:[{"rating":{$gt:8.7}}, {"genre":"Adventure"}]})
//5 Encuentra el videojuego con el título más largo en la colección.
//todo
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

//6
db.games.find({"releaseYear":{$gte:2017}})
//7
db.games.find({"title":/^T/}).limit(2)
//8
db.games.find({$and:[{"rating":{$gte:8.5}}, {"releaseYear":{$gt:2015}} ]})
//9
db.games.find({$and:[{"genre":"FPS"}, {"platform":"PC"}]})
//10
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

//11
db.games.find({$and:[{"genre":"MOBA"}, {"rating":{$gte:8.5}}]})
//12
db.games.updateOne({"title":"The Witcher 3: Wild Hunt"},{$push:{"genre":"Fantasy"}})
// tambien se  puede:
db.games.updateOne({"title":"The Witcher 3: Wild Hunt"},{$set:{"genre":["Action", "RPG", "Fantasy"]}})
//13 //todo not size 1
db.games.find({$and:[{"platform":{$not:{$size:1}}}, {"rating":{$gte:9}}]})
//14
db.games.find({"title":/New/})
//15
//db.games.find().sort({ rating: 1 })
db.games.updateOne({ rating: {$lte:8.2} }, { $inc: { rating: 0.5 } })
//! Problema 3
//1
db.games.updateOne({"title":"Minecraft"},{$push:{"platform":"Nintendo Switch"}})
//2
db.games.updateOne({"title":"Red Dead Redemption 2"},{$set:{"rating":"9.9"}})
//3
db.games.updateOne({"title":"Dota 2"},{$push:{"genre":"Strategy"}})
//4
db.games.updateOne({"title":"The Witcher 3: Wild Hunt"},{$push:{"platform":"Nintendo Switch"}})
//5
db.games.updateOne({"title":"Minecraft"},{$set:{"description":"Minecraft is a 3D sandbox adventure game developed by Mojang Studios where players can interact with a fully customizable three-dimensional world made of blocks and entities"}})
//6
db.games.updateOne({"title":"League of Legends"},{$set:{"title":"LOL","releaseYear":2010}})
//7
db.games.updateOne({"title":"LOL"},{$push:{"platform":"Nintendo Switch"}})
//8 Incrementa en 1 el rating de todos los videojuegos que tienen un rating inferior a 8.0.
db.games.updateMany({"rating":{$lt:8.0}},{$inc:{"rating":1}})

//! Problema 4
//! aquí descubrí que no hace falta poner "" para los campos .-.
//1
db.games.deleteOne({ title: "Fortnite" });
//2
db.games.updateOne({ title: "Dark Souls III" },{ $unset: { rating: "" } });
//3 //! no hay ninguno con menos de 8, min es 8
db.games.deleteMany({ rating: { $lt: 8.0 } });
//4//todo size + $gt-$lt nope
//db.games.deleteMany({ platform: { $size: { $lt: 3 } } });
db.games.find({
  $or: [
    { platform: { $size: 0 } },
    { platform: { $size: 1 } },
    { platform: { $size: 2 } }
  ]
});
//5
db.games.deleteMany({ genre: "MOBA" });
//6 //!no hay ninguno con menos de 8
db.games.updateMany(
  { rating: { $lt: 8.0 } },
  { $unset: { genre: "" } }
);
//7
db.games.deleteMany({ releaseYear: { $lt: 2010 } });
//8 //todo

//! Problema 5
//1
db.games.createIndex({ title: "text" });
//2
db.games.createIndex({ genre: 1, rating: 1 },{name:"genders and ratings"});
//3
db.games.createIndex({ title: -1, releaseYear: 1 });
//4 //? todo
db.games.createIndex({ platform: text });
// MongoServerError[IndexOptionsConflict]: An equivalent index already exists with a different name and options. Requested index: { v: 2, key: { _fts: "text", _ftsx: 1 }, name: "platform_text", weights: { platform: 1 }, default_language: "english", language_override: "language", textIndexVersion: 3 }, existing index: { v: 2, key: { _fts: "text", _ftsx: 1 }, name: "title_text", weights: { title: 1 }, default_language: "english", language_override: "language", textIndexVersion: 3 }

//* db.games.getIndexes() | db.games.getIndices()

//! Problema 6
//0
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
//1
db.users.find()
//2
db.posts.find()
//3
db.users.find({ username: "SuperCoder123" })
//4
db.posts.find({ username: "TechGuru99" })
//5
db.comments.find()
//6
db.comments.find({ username: "SuperCoder123" })
//7
db.comments.find({ username: "TechGuru99" })
//8
db.users.find({ title: "Shares coding tutorials" }, { _id: 1 });
db.comments.find({ post: ObjectId("674f2946e965c82c1f64d871") });

//! 7
//1
db.games.find({
  $or: [
    { title: /Legend/ },
    { title: /e$/ }
  ]
})
.sort({ releaseYear: -1 })
//2
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

//3
//https://www.mongodb.com/docs/manual/reference/operator/query/all/
db.games.find({
  platform: { $size: 2, $all: ['PlayStation', 'PC'] }
})
.sort({ rating: -1 })
// no da resultado, solo existe con las plataformas ['Nintendo Switch', 'Wii U']
//4
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

//!8

//1
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

//2
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

//3
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

//4 Supón que cada videojuego se vende 1,000 veces. Calcula el ingreso total por plataforma.
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

//5
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

//6 Calcula también el promedio de ingresos por plataforma.
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
//todo users colection
//7
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
//8
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
//9
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

//!9
//1
// hay que eliminar el indice de texto anterior para añadir este
db.games.createIndex({ title: "text", releaseYear: -1 })
//2
db.games.find({ $text: { $search: "Legend" } }).sort({ releaseYear: -1 }).explain("executionStats")
//db.games.explain().find({ $text: { $search: "Legend" } }).sort({ releaseYear: -1 })
//3,4,5,6
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


//7
db.games.createIndex({ rating: 1 }, { partialFilterExpression: { rating: { $gt: 9.0 } } })
//8
db.games.find({ rating: { $gt: 9.0 } }).explain("executionStats")
/*
    executionTimeMillis: 2,
    totalKeysExamined: 4,
    totalDocsExamined: 4,
    nReturned: 4,
    executionTimeMillisEstimate: 0,
*/
//9
// usamos hint para forzar el uso del indice parcial, si no lo usamos, se usará el indice de genre y ratings
db.games.find({ genre: "Adventure" }).hint("rating_1").explain("executionStats")

//!10
//1
db.users.updateOne(
  { "_id": ObjectId("674dedec961b46259ed9a9f8") },
  { 
    $push: { 
      "purchased_games": { "_id": ObjectId("67476f5a31510be117cf3e7a") }
    }
  }
)
//2
db.users.find({
  "purchased_games": { $ne: [] } // Filtra aquellos usuarios que tienen juegos en su historial de compras
})
//3
db.users.updateOne(
  { "_id": ObjectId("674dedec961b46259ed9a9f8") },
  { 
    $push: { 
      "purchased_games": { "_id": ObjectId("67476f5a31510be117cf3e86") }
    }
  }
)
//4 Inserta más comentarios relacionados con los posts de los usuarios.
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
  
//5
db.comments.find({ username: "SuperCoder123" })
//6
db.comments.aggregate([
  {
    $group: {
      _id: "$username",
      totalComments: { $sum: 1 }
    }
  }
])
//7 Encuentra todas las posts con sus respectivos comentarios.
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
//8 Encuentra las publicaciones con más de dos comentarios.
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
//9 Ordena las publicaciones por el número de comentarios de forma descendente.
// puesto que sort no puede tener $size, creamos un campo con el tamaño de los comentarios y lo ordenamos
// db.posts.aggregate([
//   {
//     $lookup: {
//       from: "comments",
//       localField: "_id",
//       foreignField: "post",
//       as: "comments"
//     }
//   },
//   {
//     $sort: {
//       $size: "$comments"
//     }
//   }
// ])
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


//!11
//1
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

//2
db.games.aggregate([
  {
    $unwind: "$genre" // Descompone el array `genre` para que podamos agrupar por cada género
  },
  {
    $group: {
      _id: "$genre", // Agrupa por género
      games: {
        $push: {
          id: "$_id", // Incluye el _id del juego
          title: "$title", // Incluye el título del juego
          genre: "$genre", // Incluye el género
          platform: "$platform", // Incluye la plataforma del juego
          releaseYear: "$releaseYear", // Incluye el año de lanzamiento (opcional)
          rating: "$rating", // Incluye la calificación (opcional)
          price: "$price" // Incluye el precio (opcional)
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

//3 //? sobre las consultas anteriores?
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
      into: "genre_analysis", // Nombre de la nueva colección donde se guardarán los resultados
      whenMatched: "merge", // Si ya existe un documento con el mismo género, se fusiona
      whenNotMatched: "insert" // Si no existe, se inserta un nuevo documento
    }
  }
])

//4
//5
//6

//!12
//1
//2
//3
//4
//5
//6