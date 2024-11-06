from pymongo import MongoClient

# Variables para conectarse a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_villains_gym(villains_collection, gym_collection, database_name='test'):
    # Configura la conexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    villains_col = db[villains_collection]
    gym_col = db[gym_collection]

    # Iterar sobre todos los documentos en la colección villain

    for villain in villains_col.find():
        updated = False
        new_gym = []
        gym_name = villain.get('gym')        
        if gym_name:
            # Buscar el correspondiente en la colección 'gym'
            gym = gym_col.find_one({'name': gym_name})  # Convertimos a minúsculas para asegurarnos de que coincida
            if gym:
                # Crear un nuevo documento de región con el '_id' y 'name'
                new_gym_entry = {
                        '_id': gym['_id'],
                        'name': gym['name']
                }
                new_gym.append(new_gym_entry)
                updated = True
            else:
                new_gym.append({
                    '_id': None,
                    'name': gym_name
                })
            if updated:
                # Actualizar el documento en MongoDB
                villains_col.update_one({'_id': villain['_id']}, {'$set': {'gym': new_gym}})

    # Cerrar la conexión
    client.close()

update_villains_gym(database_name="pokemon", villains_collection='villains',gym_collection="gyms")