from pymongo import MongoClient
import gridfs
import os

# Datos de conexión
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

# Conectar a la base de datos MongoDB
client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client["pokemon"]
pokemon_col = db["pokemons"]
fs = gridfs.GridFS(db, collection="sprites")

def recuperar_y_guardar_sprites(folder="sprites",limit = 10):
    # Crear el directorio de destino si no existe
    os.makedirs(folder, exist_ok=True)
    
    # Iterar sobre cada documento en la colección de Pokémon
    for pokemon in pokemon_col.find().limit(limit):
        pokemon_name = pokemon.get("name", "Unknown")  # Obtener el nombre del Pokémon
        sprites = pokemon.get("sprites", {})           # Obtener los datos de sprites del documento
        
        # Procesar sprites en el nivel principal
        for sprite_key, sprite_info in sprites.items():
            if isinstance(sprite_info, dict) and "_id" in sprite_info:
                file_id = sprite_info["_id"]
                file_name = sprite_info.get("file_name", f"{pokemon_name}_{sprite_key}")
                guardar_imagen_por_id(file_id, folder, file_name)
        
        # Procesar sprites en subdirectorios (por ejemplo, "showdown")
        for sub_key, sub_sprites in sprites.get("showdown", {}).items():
            if isinstance(sub_sprites, dict) and "_id" in sub_sprites:
                file_id = sub_sprites["_id"]
                file_name = sub_sprites.get("file_name", f"{pokemon_name}_showdown_{sub_key}")
                guardar_imagen_por_id(file_id, folder, file_name)

def guardar_imagen_por_id(file_id, folder, file_name):
    # Recuperar la imagen desde GridFS
    image = fs.get(file_id)
    mime_type = image.content_type

    # Determinar la extensión del archivo basada en el tipo MIME
    if mime_type == "image/png":
        extension = ".png"
    elif mime_type == "image/svg+xml":
        extension = ".svg"
    elif mime_type == "image/gif":
        extension = ".gif"
    else:
        extension = ""  # Asignar una extensión vacía si no se reconoce el tipo MIME

    # Definir la ruta completa del archivo de destino
    final_path = os.path.join(folder, f"{file_name}{extension}")

    # Guardar la imagen en la ruta de destino
    with open(final_path, "wb") as f:
        f.write(image.read())
    
    print(f"La imagen '{file_name}' se ha recuperado y guardado en '{final_path}'.")

# Llamada a la función para recuperar y guardar los sprites
recuperar_y_guardar_sprites("sprites", limit=1)