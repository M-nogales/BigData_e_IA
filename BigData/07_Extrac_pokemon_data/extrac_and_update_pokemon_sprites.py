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
fs = gridfs.GridFS(db, collection="sprites")

def recuperar_primeras_imagenes_desde_mongodb(folder, limit=10):
    # Crear el directorio de destino si no existe
    os.makedirs(folder, exist_ok=True)
    
    # Obtener las primeras `limit` imágenes de GridFS
    images = fs.find().limit(limit)
    
    # Procesar cada imagen
    for image in images:
        # Obtener el nombre de la imagen y su tipo MIME
        image_name = image.filename
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
        final_path = os.path.join(folder, f"{image_name}{extension}")
        
        # Guardar la imagen en la ruta de destino
        with open(final_path, "wb") as f:
            f.write(image.read())
        
        print(f"La imagen '{image_name}' se ha recuperado y guardado en '{final_path}'.")

# Llamada a la función para recuperar las primeras 10 imágenes y guardarlas en la carpeta 'sprites'
recuperar_primeras_imagenes_desde_mongodb("sprites")
