from pymongo import MongoClient
import random

# Conectar a la base de datos
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client.VideogamesDB
collection = db.games

# Generar un valor aleatorio entre 10 y 100 para el campo precio
def get_random_price():
    return random.randint(10, 100)

# Función para actualizar cada juego con un precio único
def update_game_price():
    # Buscar todos los juegos
    games = collection.find()

    for game in games:
        price = get_random_price()
        # Actualizar el documento de cada juego con un precio diferente
        collection.update_one({'_id': game['_id']}, {'$set': {'price': price}})

# Llamar a la función para actualizar los precios
update_game_price()

print("Precios actualizados para todos los juegos.")

# Cerrar la conexión
client.close()
