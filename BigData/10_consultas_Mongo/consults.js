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
//6
db.games.find({"releaseYear":{$gte:2017}})
//7
db.games.find({"title":/^T/}).limit(2)
//8
db.games.find({$and:[{"rating":{$gte:8.5}}, {"releaseYear":{$gt:2015}} ]})
//9
db.games.find({$and:[{"genre":"FPS"}, {"platform":"PC"}]})
//10
//todo
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
//15Encuentra el videojuego con el rating más bajo y actualiza su calificación añadiendo 0.5 puntos.
//todo

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
    post: ObjectId("674996f5eb04addc01260af3")
  },
  {
    username: "SuperCoder123",
    comment: "What's mine is yours!",
    post: ObjectId("674996f5eb04addc01260af5")
  },
  {
    username: "SuperCoder123",
    comment: "Don't violate the licensing agreement!",
    post: ObjectId("674996f5eb04addc01260af4")
  },
  {
    username: "TechGuru99",
    comment: "It still isn't clean",
    post: ObjectId("674996f5eb04addc01260af3")
  },
  {
    username: "TechGuru99",
    comment: "Denied your PR because I found a hack",
    post: ObjectId("674996f5eb04addc01260af4")
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
db.comments.find({ post: ObjectId("674996f5eb04addc01260af4") });

//! 7
//1
//2
//3
//4

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
    $addFields: {
      revenue: { $multiply: [1000, "$price"] }
    }
  },
  {
    $group: {
      _id: "$platform",
      totalRevenue: { $sum: "$revenue" }
    }
  }
])
/*
db.games.aggregate([
  {
    $unwind: "$platform"
  },
  {
    $addFields: {
      revenue: { $multiply: [1000, "$price"] }
    }
  },
  {
    $group: {
      _id: "$platform",
      totalRevenue: { $sum: "$revenue" }
    }
  }
])
*/

//5
db.games.aggregate([
  // Step 1: Unwind platforms array
  { $unwind: "$platform" },

  // Step 2: Calculate revenue for each platform
  {
    $group: {
      _id: "$platform", // Group by platform
      totalRevenue: { $sum: { $multiply: ["$price", 1000] } } // Sum up revenues for each platform
    }
  },

  // Step 3: Determine the maximum revenue
  {
    $group: {
      _id: null,
      maxRevenue: { $max: "$totalRevenue" },
      platforms: {
        $push: {
          platform: "$_id",
          revenue: "$totalRevenue"
        }
      }
    }
  },

  // Step 4: Filter platforms with maximum revenue
  {
    $project: {
      platformsWithMaxRevenue: {
        $filter: {
          input: "$platforms",
          as: "platform",
          cond: { $eq: ["$$platform.revenue", "$maxRevenue"] }
        }
      }
    }
  }
]);

//6//?

//7
//8
//9

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
db.games.find({ rating: { $gt: 9.0 } }).explain("executionStats")
//8
//9

//!10
//1
//2
//3
//4
//5
//6
//7
//8
//9

//!11
//1
//2
//3
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

//! cambiar games por series