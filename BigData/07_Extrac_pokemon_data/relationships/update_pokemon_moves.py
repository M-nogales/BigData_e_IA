from pymongo import MongoClient

mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_pokemon_moves(pokemon_collection, moves_collection, database_name='test'):
    #nconexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    pokemon_col = db[pokemon_collection]
    moves_col = db[moves_collection]

    # Iterar sobre todos los pokemon
    for pokemon in pokemon_col.find():
        updated = False
        new_moves = []
        moves = pokemon.get('moves', [])
        
        # iterar sobre cada movimiento de movimientos del Pokémon
        for move_entry in moves:
            move_name = move_entry.get('move', {}).get('name')
            if move_name:
                # buscar el movimiento en 'moves'
                move_doc = moves_col.find_one({'name': move_name})
                if move_doc:
                    # asegurarse de que 'power' sea un número (si no lo es, asignamos 0)
                    power = move_doc.get('power')
                    if power is None:
                        power = 0  # asignar valor por defecto 0 si 'power' es None
                    elif not isinstance(power, (int, float)):
                        power = 0  # si power no es un número, asignamos 0

                    # relación nueva con '_id', 'name' y 'power' del movimiento
                    new_move_entry = {
                        '_id': move_doc['_id'],
                        'name': move_doc['name'],
                        'power': power,
                    }
                    new_moves.append(new_move_entry)
                    updated = True
                else:
                    # si el movimiento no se encuentra,añadirlo `vacio`
                    new_moves.append({'_id': None, 'name': move_name, 'power': 0})

        if updated:
            # actualizar el documento en MongoDB
            pokemon_col.update_one({'_id': pokemon['_id']}, {'$set': {'moves': new_moves}})

    client.close()

update_pokemon_moves(database_name="pokemon", pokemon_collection='pokemons', moves_collection="moves")
