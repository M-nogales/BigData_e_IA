from pymongo import MongoClient

# Variables para conectarse a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_gym_types(gym_collection, types_collection, database_name='test'):
    # conexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    gyms_col = db[gym_collection]
    types_col = db[types_collection]

    for gym in gyms_col.find():
        updated = False
        new_types = []
        gym_type = gym.get('type').lower()
        type = types_col.find_one({'name': gym_type})
        if type:
            # poner la relación a types
            new_type_entry = {
                    '_id': type['_id'],
                    'name': type['name']
            }
            new_types.append(new_type_entry)
            updated = True
        
        if updated:
            # Actualizar el documento en MongoDB
            gyms_col.update_one({'_id': gym['_id']}, {'$set': {'type': new_types}})

    client.close()

update_gym_types(database_name="pokemon", gym_collection='gyms',types_collection="types")