# 07. **Catálogo de Libros**
# Contiene libros con título, autor, género y año de publicación.
# Insertar al menos 10 libros en el catálogo. Filtrar por género o autor,
# agregar nuevos libros, listar libros recientes.
'''  JSON = 
{
    "libros": [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Ficción", "año": 1967},
        {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "año": 1605}
    ]
}
'''

import json

catalogo = {
    "libros": [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Ficción", "año": 1967},
        {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "año": 1605},
    ]}

def agregar_libro(titulo, autor, genero, año):
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "año": año
    }
    catalogo["libros"].append(nuevo_libro)
    return "Libro añadido"

def filtrar_libros(autor=None, genero=None):
    libros_filtrados = []
    for libro in catalogo["libros"]:
        if (autor and libro["autor"] == autor) or (genero and libro["genero"].lower() == genero.lower()):
            libros_filtrados.append(libro)
    return libros_filtrados

def listar_libros_recientes(anio):
    libros_recientes = []
    for libro in catalogo["libros"]:
        if libro["año"] >= anio:
            libros_recientes.append(libro)
    return libros_recientes

def guardar_catalogo():
    with open("jsons/07_libros.json", "w") as archivo:
        json.dump(catalogo, archivo, indent=2)

# pereza repetirlo 10 veces/bucle
print('agregar_libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 1937): ',
      agregar_libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 1937))
print('filtrar_por_genero("Ficción"): ', filtrar_libros(genero = "Ficción"))
print('filtrar_por_autor("Gabriel García Márquez"): ', filtrar_libros(autor = "Gabriel García Márquez"))
print('listar_libros_recientes(1980): ', listar_libros_recientes(1980))
guardar_catalogo()