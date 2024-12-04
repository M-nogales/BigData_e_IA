async function findGames(query, sort = null, limit = null) {
  const { MongoClient } = require("mongodb");

  // Datos de conexión
  const mongoUser = "root";
  const mongoPassword = "example";
  const mongoHost = "localhost";
  const mongoPort = 27017;
  const dbName = "VideogamesDB";

  // Crear la conexión
  const uri = `mongodb://${mongoUser}:${mongoPassword}@${mongoHost}:${mongoPort}/`;
  const client = new MongoClient(uri);

  try {
    // Conectar a la base de datos
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection("games");

    // Construir la consulta
    let pipeline = [];

    // Agregar condiciones de búsqueda
    if (query) {
      pipeline.push({ $match: query });
    }

    // Agregar ordenamiento si se especifica
    if (sort) {
      pipeline.push({ $sort: sort });
    }

    // Agregar límite si se especifica
    if (limit) {
      pipeline.push({ $limit: limit });
    }

    // Ejecutar la consulta
    const results = await collection.aggregate(pipeline).toArray();
    console.log("Resultados encontrados:", results);
    return results;
  } catch (error) {
    console.error("Error buscando videojuegos:", error);
    throw error;
  } finally {
    // Cerrar la conexión
    await client.close();
  }
}

(async () => {
  const query = { rating: { $gt: 8.5 } };
  const sort = { price: -1 }; // Descendente
  const limit = 5;

  const games = await findGames(query, sort, limit);
  console.log("Juegos encontrados:");
  console.log(games);
})();

