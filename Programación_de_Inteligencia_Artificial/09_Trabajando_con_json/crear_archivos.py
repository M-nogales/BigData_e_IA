# Lista de títulos y descripciones para cada ejercicio
titulos = [
    "Directorio Telefónico",
    "Inventario de Productos",
    "Agenda de Tareas",
    "Registro de Ventas",
    "Información de Alumnos",
    "Concesionario de Coches",
    "Catálogo de Libros",
    "Agenda de Eventos",
    "Catálogo de Películas",
    "Red de Superhéroes"
]

descripciones = [
    "Contiene contactos con campos como nombre, apellidos, teléfono y correo electrónico. Insertar al menos 10 registros telefónicos. Búsqueda de contacto por nombre, actualización de número de teléfono, agregar o eliminar un contacto.",
    "Listado de productos en una tienda con nombre, categoría, precio y cantidad en stock. Insertar al menos 10 productos en el inventario. Filtrar productos por categoría, calcular el valor total del inventario, actualizar stock.",
    "Contiene una lista de tareas con detalles como descripción, fecha de vencimiento y estado. Insertar al menos 10 tareas al fichero. Agregar nuevas tareas, actualizar el estado de una tarea, filtrar tareas completadas.",
    "Información sobre ventas, incluyendo producto, cantidad vendida, precio y fecha. Incorpora al menos 10 ventas al registro. Calcular el total de ventas, filtrar por fecha o producto, agregar nuevas ventas.",
    "Datos sobre estudiantes, incluyendo nombre, edad, calificación y ciudad. Inserta al menos 10 alumnos al fichero JSON. Filtrar alumnos aprobados, calcular la edad promedio, agregar y eliminar alumnos.",
    "Lista de coches disponibles en un concesionario con detalles como marca, modelo, precio y año. El registro del concesionario debe contener al menos 10 vehículos. Filtrar por marca, calcular el valor promedio de los coches, actualizar precios.",
    "Contiene libros con título, autor, género y año de publicación. Insertar al menos 10 libros en el catálogo. Filtrar por género o autor, agregar nuevos libros, listar libros recientes.",
    "Listado de eventos con información como título, fecha, ubicación y organizador. Filtrar eventos por fecha o ubicación, agregar eventos futuros, eliminar eventos pasados.",
    "Incluye películas con título, director, año de lanzamiento y género. Filtrar por género, listar directores únicos, agregar nuevas películas.",
    "Contiene superhéroes con su alias, habilidades, ciudad de origen y equipo. Filtrar por ciudad o equipo, agregar nuevos superhéroes, listar habilidades únicas."
]

# JSON para cada ejercicio
jsons = [
    """{
    "contactos": [
        {"nombre": "Juan", "apellidos": "Pérez", "telefono": "612345678", "correo": "juan@example.com"},
        {"nombre": "Laura", "apellidos": "Gómez", "telefono": "623456789", "correo": "laura@example.com"}
    ]
}""",
    """{
    "productos": [
        {"nombre": "Laptop", "categoria": "Electrónica", "precio": 1000, "stock": 15},
        {"nombre": "Teclado", "categoria": "Accesorios", "precio": 50, "stock": 30}
    ]
}""",
    """{
    "tareas": [
        {"descripcion": "Estudiar Python", "vencimiento": "2024-11-01", "estado": "pendiente"},
        {"descripcion": "Revisar proyecto", "vencimiento": "2024-10-29", "estado": "completada"}
    ]
}""",
    """{
    "ventas": [
        {"producto": "Laptop", "cantidad": 2, "precio": 1000, "fecha": "2024-10-28"},
        {"producto": "Teclado", "cantidad": 5, "precio": 50, "fecha": "2024-10-27"}
    ]
}""",
    """{
    "alumnos": [
        {"nombre": "Carlos", "edad": 20, "calificacion": 85, "ciudad": "Madrid"},
        {"nombre": "Lucía", "edad": 22, "calificacion": 90, "ciudad": "Barcelona"}
    ]
}""",
    """{
    "coches": [
        {"marca": "Toyota", "modelo": "Corolla", "precio": 20000, "año": 2023},
        {"marca": "Ford", "modelo": "Focus", "precio": 18000, "año": 2022}
    ]
}""",
    """{
    "libros": [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Ficción", "año": 1967},
        {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "año": 1605}
    ]
}""",
    """{
    "eventos": [
        {"titulo": "Conferencia Python", "fecha": "2024-11-15", "ubicacion": "Madrid", "organizador": "PyCon España"},
        {"titulo": "Taller de IA", "fecha": "2024-12-01", "ubicacion": "Barcelona", "organizador": "TechFest"}
    ]
}""",
    """{
    "peliculas": [
        {"titulo": "El Laberinto del Fauno", "director": "Guillermo del Toro", "año": 2006, "genero": "Fantasía"},
        {"titulo": "Mar Adentro", "director": "Alejandro Amenábar", "año": 2004, "genero": "Drama"}
    ]
}""",
    """{
    "superheroes": [
        {"alias": "El Cid", "habilidades": ["esgrima", "estrategia"], "ciudad": "Burgos", "equipo": "Los Defensores"},
        {"alias": "La Dama de Plata", "habilidades": ["manipulación de metales"], "ciudad": "Toledo", "equipo": "Los Defensores"}
    ]
}"""
]

# Crear archivos con el formato requerido
for i in range(len(titulos)):
    numero = f'{i + 1:02}'  # Formato de número de dos dígitos
    titulo = titulos[i]
    descripcion = descripciones[i]
    json_content = jsons[i]
    
    # Formato del contenido del archivo
    contenido = f"# {numero}. **{titulo}**\n# {descripcion}\n\'\'\'  JSON = \n{json_content}\n\'\'\'\n"
    
    # Nombre del archivo
    nombre_archivo = f"{numero}_Trabajando_con_json.py"
    
    # Crear el archivo y escribir el contenido
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)

print("Archivos creados con éxito.")
