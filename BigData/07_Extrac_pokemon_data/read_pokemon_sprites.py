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

        # Crear un diccionario para almacenar los sprites actualizados
        updated_sprites = {}

        # Iterar sobre todas las claves de sprites en el nivel principal
        for sprite_key, sprite_url in sprites.items():
            if isinstance(sprite_url, str) and sprite_url:  # Proceder si es una URL
                filename = f"{name}_{sprite_key}"
                file_id = guardar_sprite_en_gridfs(sprite_url, filename, fs)  # Guardar el sprite y obtener el _id
                if file_id:
                    updated_sprites[sprite_key] = {
                        "file_name": filename,
                        "_id": file_id
                    }
        
        # Acceder y procesar el subdiccionario "showdown" dentro de "other", si existe
        showdown_sprites = sprites.get("other", {}).get("showdown", {})
        for showdown_key, showdown_url in showdown_sprites.items():
            if isinstance(showdown_url, str) and showdown_url:  # Proceder si es una URL
                filename = f"{name}_showdown_{showdown_key}"
                file_id = guardar_sprite_en_gridfs(showdown_url, filename, fs)  # Guardar el sprite y obtener el _id
                if file_id:
                    if "showdown" not in updated_sprites:
                        updated_sprites["showdown"] = {}
                    updated_sprites["showdown"][showdown_key] = {
                        "file_name": filename,
                        "_id": file_id
                    }
        
        # Si se han actualizado los sprites, guardarlos en el documento de Pokémon
        if updated_sprites:
            pokemon_col.update_one(
                {"_id": pokemon["_id"]},
                {"$set": {"sprites": updated_sprites}}
            )
            print(f"Sprites para el Pokémon '{name}' actualizados en la colección.")

    # Cerrar la conexión
    client.close()
    print("Todos los sprites han sido procesados y los documentos de Pokémon han sido actualizados.")

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
        return file._id  # Retornar el _id del archivo guardado
    else:
        print(f"Error al descargar el archivo desde la URL: {url}")
        return None

# Llamada a la función para guardar los sprites en GridFS y actualizar la colección de Pokémon
save_pokemon_sprites_to_gridfs(pokemon_collection='pokemons')
