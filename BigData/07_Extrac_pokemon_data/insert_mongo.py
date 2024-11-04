import json
from pymongo import MongoClient

def insert_data_to_mongodb(collection_name, file_path, json_array_name, database_name='test'):
    # Configura la conexión a MongoDB
    mongo_user = "root"
    mongo_password = "example"
    mongo_host = "localhost"
    mongo_port = 27017

    # Conectar a la base de datos de MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]  # Usar la base de datos proporcionada o 'test' por defecto
    collection = db[collection_name]  # Si no existe, se creará automáticamente

    # Leer el archivo JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Cargar el contenido del archivo JSON
    except FileNotFoundError:
        print(f"El archivo {file_path} no se encontró.")
        return
    except json.JSONDecodeError:
        print(f"Error al leer el archivo JSON {file_path}. Asegúrate de que tenga un formato válido.")
        return

    # Asegúrate de que el json_array_name está en el JSON
    if json_array_name in data:
        items_to_insert = data[json_array_name]  # Extraer el array especificado

        # Insertar los objetos en la colección de MongoDB
        if isinstance(items_to_insert, list):  # Verificar que el contenido es una lista
            result = collection.insert_many(items_to_insert)
            print(f'Se han insertado {len(result.inserted_ids)} elementos en la colección "{collection_name}" de la base de datos "{database_name}".')
        else:
            print(f"{json_array_name} no es una lista.")
    else:
        print(f"{json_array_name} no se encontró en el JSON.")

    # Cerrar la conexión
    client.close()

insert_data_to_mongodb(database_name="test_pokemon", collection_name='profesores', file_path='data/professors.json', json_array_name='profesores')
insert_data_to_mongodb(database_name="test_pokemon", collection_name='entrenadores', file_path='data/trainers.json', json_array_name='entrenadores')
insert_data_to_mongodb(database_name="test_pokemon", collection_name='villanos', file_path='data/villains.json', json_array_name='villanos')
insert_data_to_mongodb(database_name="test_pokemon", collection_name='regiones', file_path='data/regions_data.json', json_array_name='regiones')
insert_data_to_mongodb(database_name="test_pokemon", collection_name='gimnasios', file_path='data/gyms.json', json_array_name='gimnasios')
insert_data_to_mongodb(database_name="test_pokemon", collection_name='pokemons', file_path='data/pokemons_data.json', json_array_name='pokemons')
insert_data_to_mongodb(database_name="test_pokemon", collection_name='tipos', file_path='data/types.json', json_array_name='tipos')
insert_data_to_mongodb(database_name="test_pokemon", collection_name='movimientos', file_path='data/moves_data.json', json_array_name='movimientos')
