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
//1

//2
//3
//4
//5
//6
//7
//8
/*
db.nombre_de_tu_coleccion.deleteOne({ title: "Fortnite" });

// Elimina el campo de calificación del videojuego "Dark Souls III"
db.nombre_de_tu_coleccion.updateOne(
  { title: "Dark Souls III" },
  { $unset: { rating: "" } }
);

// Elimina todos los videojuegos que tengan un rating inferior a 8.0
db.nombre_de_tu_coleccion.deleteMany({ rating: { $lt: 8.0 } });

// Elimina todos los videojuegos que tengan menos de 3 plataformas
db.nombre_de_tu_coleccion.deleteMany({ platform: { $size: { $lt: 3 } } });

// Elimina todos los videojuegos que sean del género "MOBA"
db.nombre_de_tu_coleccion.deleteMany({ genre: "MOBA" });

// Elimina el campo de género de todos los videojuegos que tengan un rating inferior a 8.0
db.nombre_de_tu_coleccion.updateMany(
  { rating: { $lt: 8.0 } },
  { $unset: { genre: "" } }
);

// Elimina todos los videojuegos lanzados antes de 2010
db.nombre_de_tu_coleccion.deleteMany({ releaseYear: { $lt: 2010 } });

// Elimina el videojuego con el menor número de plataformas
db.nombre_de_tu_coleccion.find().sort({ platform: 1 }).limit(1).forEach(function(doc) {
  db.nombre_de_tu_coleccion.deleteOne({ _id: doc._id });
});
*/

//! Problema 5
//1
//2
//3
//4

//! Problema 6
//1
//2
//3
//4
//5
//6
//7
//8