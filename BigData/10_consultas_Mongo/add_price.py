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

# Actualizar todos los documentos para añadir el campo precio
result = collection.update_many({}, { '$set': { 'price': get_random_price() } })

print(f'{result.modified_count} documentos actualizados')

# Cerrar la conexión
client.close()