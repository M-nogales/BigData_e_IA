from pymongo import MongoClient
import gridfs
import os

# conexión a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client["pokemon"]
fs = gridfs.GridFS(db, collection="sprites")

# función para recuperar las primeras 10 IMÁGENES y guardarlas en la carpeta 'sprites'
def recuperar_primeras_imagenes_desde_mongodb(folder, limit=10):
    # crear el folder de destino si no existe
    os.makedirs(folder, exist_ok=True)
    
    # obtener `limit` imágenes de MongoDB con GridFS
    images = fs.find().limit(limit)
    
    for image in images:
        # coger el nombre de la imagen y su tipo MIME
        image_name = image.filename
        mime_type = image.content_type
        
        # determinar la extensión del archivo basada en el tipo MIME
        if mime_type == "image/png":
            extension = ".png"
        elif mime_type == "image/svg+xml":
            extension = ".svg"
        elif mime_type == "image/gif":
            extension = ".gif"
        else:
            extension = ""

        final_path = os.path.join(folder, f"{image_name}{extension}")
        
        # guardar la imagen
        with open(final_path, "wb") as f:
            f.write(image.read())
        
        print(f"La imagen '{image_name}' se ha recuperado y guardado en '{final_path}'.")

# función para recuperar las primeras 10 IMÁGENES y guardarlas en la carpeta 'sprites'
recuperar_primeras_imagenes_desde_mongodb("sprites")
