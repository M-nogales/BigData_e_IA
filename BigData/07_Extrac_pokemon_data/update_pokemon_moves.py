from pymongo import MongoClient

# Variables para conectarse a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_pokemon_moves(pokemon_collection, moves_collection, database_name='test'):
    # Configura la conexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    pokemon_col = db[pokemon_collection]
    moves_col = db[moves_collection]

    # Iterar sobre todos los documentos en la colección pokemon
    for pokemon in pokemon_col.find():
        updated = False
        new_moves = []
        moves = pokemon.get('moves', [])
        
        # Iterar sobre cada movimiento en el arreglo de movimientos del Pokémon
        for move_entry in moves:
            move_name = move_entry.get('move', {}).get('name')  # Obtener el nombre del movimiento
            if move_name:
                # Buscar el movimiento en la colección 'moves'
                move_doc = moves_col.find_one({'name': move_name})
                if move_doc:
                    # Asegurar que 'power' sea un número (si no lo es, asignamos 0)
                    power = move_doc.get('power')
                    if power is None:
                        power = 0  # Asignar valor por defecto 0 si 'power' es None
                    elif not isinstance(power, (int, float)):
                        power = 0  # Si power no es un número, asignamos 0

                    # Crear la entrada para el movimiento con '_id', 'name' y 'power'
                    new_move_entry = {
                        '_id': move_doc['_id'],
                        'name': move_doc['name'],
                        'power': power,  # Asegurarnos de que power es un número
                    }
                    new_moves.append(new_move_entry)
                    updated = True
                else:
                    # Si el movimiento no se encuentra, agregarlo con 'power' = 0
                    new_moves.append({'_id': None, 'name': move_name, 'power': 0})

        if updated:
            # Actualizar el documento en MongoDB con la lista de nuevos movimientos
            pokemon_col.update_one({'_id': pokemon['_id']}, {'$set': {'moves': new_moves}})

    # Cerrar la conexión
    client.close()

# Llamada a la función para actualizar los movimientos
update_pokemon_moves(database_name="pokemon", pokemon_collection='pokemons', moves_collection="moves")
