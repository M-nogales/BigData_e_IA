import json
from pymongo import MongoClient

def insert_data_to_mongodb(collection_name, file_path, json_array_name, database_name='test'):
    # conexión a MongoDB
    mongo_user = "root"
    mongo_password = "example"
    mongo_host = "localhost"
    mongo_port = 27017

    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]  # Usar la base de datos proporcionada o 'test' por defecto
    collection = db[collection_name]  # Si no existe, se creará automáticamente

    # leer el JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
        return
    except json.JSONDecodeError:
        print(f"Error al leer el archivo JSON {file_path}. Asegúrate de que tenga un formato válido.")
        return

    if json_array_name in data:
        items_to_insert = data[json_array_name]

        # insertar los json en la colección de MongoDB
        # Verificar que el contenido es una lista
        if isinstance(items_to_insert, list):
            result = collection.insert_many(items_to_insert)
            print(f'Se han insertado {len(result.inserted_ids)} elementos en la colección "{collection_name}" de la base de datos "{database_name}".')
        else:
            print(f"{json_array_name} no es una lista.")
    else:
        print(f"{json_array_name} no se encontró en el JSON.")
    client.close()

def delete_mongodb_db(database_name='test'):
    mongo_user = "root"
    mongo_password = "example"
    mongo_host = "localhost"
    mongo_port = 27017

    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")

    # eliminar la base de datos dada o 'test' por defecto
    client.drop_database(database_name)
    client.close()

# insert_data_to_mongodb(database_name="pokemon", collection_name='professors', file_path='data/professors.json', json_array_name='professors')
# insert_data_to_mongodb(database_name="pokemon", collection_name='trainers', file_path='data/trainers.json', json_array_name='trainers')
# insert_data_to_mongodb(database_name="pokemon", collection_name='villains', file_path='data/villains.json', json_array_name='villains')
# insert_data_to_mongodb(database_name="pokemon", collection_name='regions', file_path='data/regions_data.json', json_array_name='regions')
# insert_data_to_mongodb(database_name="pokemon", collection_name='gyms', file_path='data/gyms.json', json_array_name='gyms')
# insert_data_to_mongodb(database_name="pokemon", collection_name='pokemons', file_path='data/pokemons_data.json', json_array_name='pokemons')
# insert_data_to_mongodb(database_name="pokemon", collection_name='types', file_path='data/types.json', json_array_name='types')
# insert_data_to_mongodb(database_name="pokemon", collection_name='moves', file_path='data/moves_data.json', json_array_name='moves')