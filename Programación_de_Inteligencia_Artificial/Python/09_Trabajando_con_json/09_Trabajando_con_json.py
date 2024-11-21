# 09. **Catálogo de Películas**
# Incluye películas con título, director, año de lanzamiento y género.
# Filtrar por género, listar directores únicos, agregar nuevas películas.
'''  JSON = 
{
    "peliculas": [
        {"titulo": "El Laberinto del Fauno", "director": "Guillermo del Toro", "año": 2006, "genero": "Fantasía"},
        {"titulo": "Mar Adentro", "director": "Alejandro Amenábar", "año": 2004, "genero": "Drama"}
    ]
}
'''
import json

# Estructura del catálogo de películas
catalogo_peliculas = {
    "peliculas": [
        {"titulo": "El Laberinto del Fauno", "director": "Guillermo del Toro", "año": 2006, "genero": "Fantasía"},
        {"titulo": "Mar Adentro", "director": "Alejandro Amenábar", "año": 2004, "genero": "Drama"},
    ]}

def agregar_pelicula(titulo, director, año, genero):
    nueva_pelicula = {
        "titulo": titulo,
        "director": director,
        "año": año,
        "genero": genero
    }
    catalogo_peliculas["peliculas"].append(nueva_pelicula)
    return "Película añadida"

def filtrar_por_genero(genero):
    for pelicula in catalogo_peliculas["peliculas"]:
        if pelicula["genero"].lower() == genero.lower():
            peliculas_filtradas = pelicula
    return peliculas_filtradas

# Función para listar directores únicos
def listar_directores_unicos():
    for pelicula in catalogo_peliculas["peliculas"]:
        directores_unicos = set(pelicula["director"])
    return list(directores_unicos)

# Función para guardar el catálogo en un archivo JSON
def guardar_catalogo():
    with open("jsons/09_peliculas.json", "w") as archivo:
        json.dump(catalogo_peliculas, archivo, indent=2)

# Ejemplos de uso
print('agregar_pelicula("El Padrino", "Francis Ford Coppola", 1972, "Crimen"): ',
      agregar_pelicula("El Padrino", "Francis Ford Coppola", 1972, "Crimen"))

print('filtrar_por_genero("Fantasía"): ', filtrar_por_genero("Fantasía"))
print('listar_directores_unicos(): ', listar_directores_unicos())
guardar_catalogo()
# pereza repetirlo 10 veces/bucle