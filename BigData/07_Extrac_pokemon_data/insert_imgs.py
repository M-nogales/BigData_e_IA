from pymongo import MongoClient
import gridfs
import requests
import mimetypes

# Datos de conexión
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

# Conectar a la base de datos MongoDB
client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client["pokemon"]

# Crear una instancia de GridFS con prefijo personalizado para las colecciones
fs = gridfs.GridFS(db, collection="sprites")

def guardar_archivo_en_mongodb(url):
    # Obtener el nombre del archivo a partir de la URL
    nombre_archivo = url.split("/")[-1]
    
    # Descargar el archivo
    response = requests.get(url)
    
    # Verificar si la descarga fue exitosa
    if response.status_code == 200:
        # Detectar el tipo MIME del archivo
        tipo_mime, _ = mimetypes.guess_type(url)
        
        # Guardar el archivo en MongoDB utilizando GridFS
        with fs.new_file(filename=nombre_archivo, contentType=tipo_mime) as file:
            file.write(response.content)
        
        print(f"El archivo '{nombre_archivo}' (tipo {tipo_mime}) se ha guardado exitosamente en MongoDB.")
    else:
        print("Error al descargar el archivo.")

# URLs de ejemplo para guardar un archivo GIF y un archivo SVG
url_gif = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/1.gif"
url_svg = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/1.svg"

# Ejecutar la función para guardar los archivos
guardar_archivo_en_mongodb(url_gif)
guardar_archivo_en_mongodb(url_svg)
