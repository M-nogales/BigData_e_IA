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
db = client["test"]
fs = gridfs.GridFS(db, collection="metadata")

def recuperar_imagen_desde_mongodb(nombre_imagen, ruta_destino):
    # Crear el directorio si no existe
    os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
    
    # Buscar la imagen en GridFS
    imagen = fs.find_one({"filename": nombre_imagen})
    if imagen:
        with open(ruta_destino, "wb") as f:
            f.write(imagen.read())
        print(f"La imagen '{nombre_imagen}' se ha recuperado y guardado en '{ruta_destino}'.")
    else:
        print("Imagen no encontrada en la base de datos.")

# Recuperar la imagen y guardarla en la carpeta 'sprites'
recuperar_imagen_desde_mongodb("1.svg", "sprites/bulba.svg")
