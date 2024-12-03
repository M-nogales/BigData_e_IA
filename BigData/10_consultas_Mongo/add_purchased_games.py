from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Credenciales de la base de datos
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")

try:
    # Obtener la base de datos y colecciones
    db = client['VideogamesDB']
    users_collection = db['users']
    games_collection = db['games']

    # Asignar videojuegos a los usuarios
    for user in users_collection.find():
        purchased_games = []

        # Supongamos que el usuario 'SuperCoder123' compró los siguientes juegos
        if user['username'] == 'SuperCoder123':
            purchased_games.append(games_collection.find_one({"title": "The Legend of Zelda: Breath of the Wild"},{"_id":1}))
            purchased_games.append(games_collection.find_one({"title": "Super Mario Odyssey"},{"_id":1}))

        # Supongamos que el usuario 'TechGuru99' compró el siguiente juego
        if user['username'] == 'TechGuru99':
            purchased_games.append(games_collection.find_one({"title": "The Witcher 3: Wild Hunt"},{"_id":1}))

        # Actualizamos el usuario con el campo purchased_games
        users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"purchased_games": purchased_games}}
        )

    print("Usuarios actualizados con los videojuegos comprados.")

except ConnectionFailure as e:
    print(f"No se pudo conectar a MongoDB: {e}")
