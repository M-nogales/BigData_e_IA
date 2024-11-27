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
db.games.find({"genre":"Action"})
