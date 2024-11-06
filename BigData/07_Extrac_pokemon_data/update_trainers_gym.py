from pymongo import MongoClient

# Variables para conectarse a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_trainers_gym(trainers_collection, gym_collection, database_name='test'):
    # Configura la conexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    trainers_col = db[trainers_collection]
    gym_col = db[gym_collection]

    # Iterar sobre todos los documentos en la colección trainer

    for trainer in trainers_col.find():
        updated = False
        new_gym = []
        gym_name = trainer.get('gym')        
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
                trainers_col.update_one({'_id': trainer['_id']}, {'$set': {'gym': new_gym}})

    # Cerrar la conexión
    client.close()

update_trainers_gym(database_name="pokemon", trainers_collection='trainers',gym_collection="gyms")