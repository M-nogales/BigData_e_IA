from pymongo import MongoClient
import gridfs
import requests
import mimetypes

# Variables para conectarse a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def save_pokemon_sprites_to_gridfs(pokemon_collection, database_name='pokemon'):
    # Configura la conexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    pokemon_col = db[pokemon_collection]
    
    # Crear una instancia de GridFS para guardar los sprites
    fs = gridfs.GridFS(db, collection="sprites")
    
    # Iterar sobre todos los documentos en la colección de Pokémon
    for pokemon in pokemon_col.find():
        name = pokemon.get('name', 'Unknown')  # Usa 'Unknown' si no tiene nombre
        sprites = pokemon.get('sprites', {})   # Extrae los sprites o un diccionario vacío
        
        # Procesar cada sprite URL dentro del diccionario
        guardar_sprites_recursivo(name, sprites, fs)
    
    # Cerrar la conexión
    client.close()
    print("Sprites de Pokémon guardados en GridFS.")

def guardar_sprites_recursivo(pokemon_name, sprite_dict, fs, prefix=""):
    for key, value in sprite_dict.items():
        # Si el valor es un diccionario, llamamos a la función recursivamente
        if isinstance(value, dict):
            new_prefix = f"{prefix}_{key}" if prefix else key
            guardar_sprites_recursivo(pokemon_name, value, fs, new_prefix)
        
        # Si el valor es una URL, la guardamos
        elif isinstance(value, str) and value:
            filename = f"{pokemon_name}_{prefix}_{key}".strip('_')
            guardar_sprite_en_gridfs(value, filename, fs)

def guardar_sprite_en_gridfs(url, filename, fs):
    # Descargar el archivo
    response = requests.get(url)
    
    # Verificar si la descarga fue exitosa
    if response.status_code == 200:
        # Detectar el tipo MIME del archivo
        tipo_mime, _ = mimetypes.guess_type(url)
        
        # Guardar el archivo en MongoDB utilizando GridFS
        with fs.new_file(filename=filename, contentType=tipo_mime) as file:
            file.write(response.content)
        
        print(f"El archivo '{filename}' (tipo {tipo_mime}) se ha guardado exitosamente en GridFS.")
    else:
        print(f"Error al descargar el archivo desde la URL: {url}")

# Llamada a la función para guardar los sprites en GridFS
save_pokemon_sprites_to_gridfs(pokemon_collection='pokemons')
