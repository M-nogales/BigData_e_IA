from pymongo import MongoClient

mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_pokemon_types(pokemon_collection, types_collection, database_name='test'):
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    pokemon_col = db[pokemon_collection]
    types_col = db[types_collection]

    for pokemon in pokemon_col.find():
        updated = False
        new_types = []
        for type_entry in pokemon.get('types', []):
            type_name = type_entry['type']['name']
            type = types_col.find_one({'name': type_name})
            
            if type:

                new_type_entry = {
                        '_id': type['_id'],
                        'name': type['name']
                }

                new_types.append(new_type_entry)
                updated = True
            
        if updated:
            pokemon_col.update_one({'_id': pokemon['_id']}, {'$set': {'types': new_types}})

    client.close()

update_pokemon_types(database_name="pokemon", pokemon_collection='pokemons',types_collection="types")