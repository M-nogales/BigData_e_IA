from pymongo import MongoClient
import gridfs
import requests
import mimetypes

# Variables para conectarse a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

# función para guardar los sprites en GridFS y actualizar la colección de Pokémon para relaciones imgs/sprites-pokemon
def save_pokemon_sprites_to_gridfs(pokemon_collection, database_name='pokemon'):
    # conexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    pokemon_col = db[pokemon_collection]
    
    fs = gridfs.GridFS(db, collection="sprites")
    
    # iterar la colección de Pokémon
    for pokemon in pokemon_col.find():
        name = pokemon.get('name', 'Unknown')
        sprites = pokemon.get('sprites', {})

        updated_sprites = {}

        # Iterar sobre sprites en el nivel principal
        for sprite_key, sprite_url in sprites.items():
            # el value de sprite es una `url` o null?
            if isinstance(sprite_url, str) and sprite_url:
                filename = f"{name}_{sprite_key}"
                # guardar el sprite y obtener el _id
                file_id = guardar_sprite_en_gridfs(sprite_url, filename, fs)
                if file_id:
                    updated_sprites[sprite_key] = {
                        "file_name": filename,
                        "_id": file_id
                    }
        
        # acceder y procesar "showdown" dentro de "other", si existe
        showdown_sprites = sprites.get("other", {}).get("showdown", {})
        for showdown_key, showdown_url in showdown_sprites.items():
            # el value de sprite es una `url` o null?
            if isinstance(showdown_url, str) and showdown_url:
                filename = f"{name}_showdown_{showdown_key}"
                # Guardar el sprite y obtener el _id
                file_id = guardar_sprite_en_gridfs(showdown_url, filename, fs)
                if file_id:
                    if "showdown" not in updated_sprites:
                        updated_sprites["showdown"] = {}
                    updated_sprites["showdown"][showdown_key] = {
                        "file_name": filename,
                        "_id": file_id
                    }
        
        # si se han guardado los sprites añade las relaciones sprite-pokemon
        if updated_sprites:
            pokemon_col.update_one(
                {"_id": pokemon["_id"]},
                {"$set": {"sprites": updated_sprites}}
            )
            print(f"Sprites para el Pokémon '{name}' actualizados en la colección.")

    client.close()
    print("Todos los sprites han sido procesados y los documentos de Pokémon han sido actualizados.")

def guardar_sprite_en_gridfs(url, filename, fs):
    # descargar la img
    response = requests.get(url)
    
    if response.status_code == 200:
        # detectar el tipo MIME del archivo
        tipo_mime, _ = mimetypes.guess_type(url)
        
        # guardar el archivo en MongoDB utilizando GridFS
        with fs.new_file(filename=filename, contentType=tipo_mime) as file:
            file.write(response.content)
        
        print(f"El archivo '{filename}' (tipo {tipo_mime}) se ha guardado exitosamente en GridFS.")
        # devolver el id de la imagen
        return file._id
    else:
        print(f"Error al descargar el archivo desde la URL: {url}")
        return None

# función para guardar los sprites en GridFS y actualizar la colección de Pokémon para relaciones imgs/sprites-pokemon
save_pokemon_sprites_to_gridfs(pokemon_collection='pokemons')
