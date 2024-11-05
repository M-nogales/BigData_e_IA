# Lista de títulos y descripciones para cada ejercicio
titulos = [
    "Clase Libro",
    "Clase Persona",
    "Clase CuentaBancaria",
    "Clase Cafetera",
    "Clase Restaurante",
    "Clase Estudiante",
    "Clase Pelota",
    "Clase Smartphone",
    "Clase Mascota",
    "Clase Reloj"
]

descripciones = [
    "Crea una clase Libro con atributos como título, autor, número de páginas, editorial y año de publicación. Implementa métodos para mostrar información del libro y verificar si es largo o corto.",
    "Define una clase Persona con atributos como nombre, edad, género y altura. Implementa métodos que permitan saludar, verificar si es mayor de edad y mostrar su edad en 5 años.",
    "Crea una clase CuentaBancaria con atributos como titular, saldo y tipo de cuenta. Métodos para depositar, retirar dinero (sin permitir retiros si el saldo es insuficiente) y mostrar el saldo actual.",
    "Implementa una clase Cafetera con atributos como marca, capacidad máxima y nivel actual de café. Métodos para servir café, rellenar la cafetera y verificar si está vacía o llena.",
    "Crea una clase Restaurante con atributos como nombre, tipo de cocina y menú. Métodos para añadir un plato, mostrar el menú completo y tomar un pedido.",
    "Define una clase Estudiante con atributos como nombre, curso, notas y promedio. Métodos para añadir una nueva nota, calcular el promedio y verificar si el estudiante aprobó.",
    "Crea una clase Pelota con atributos como tipo de deporte, tamaño y presión de aire. Métodos para inflar, desinflar la pelota y mostrar el estado de la presión actual.",
    "Implementa una clase Smartphone con atributos como marca, modelo, memoria, batería y nivel de batería actual. Métodos para llamar a un contacto, cargar el teléfono y mostrar el nivel de batería.",
    "Crea una clase Mascota con atributos como nombre, tipo de animal y edad. Métodos para alimentar, jugar y mostrar la energía de la mascota.",
    "Define una clase Reloj con atributos como hora, minuto y segundo actual. Métodos que permitan ajustar la hora, avanzar un minuto o segundo, y mostrar la hora actual en formato hh:mm:ss."
]

# Crear archivos con el formato requerido
for i in range(len(titulos)):
    numero = f'{i + 1:02}'  # Formato de número de dos dígitos
    titulo = titulos[i]
    descripcion = descripciones[i]
    
    # Formato del contenido del archivo
    contenido = f"# {numero}. **{titulo}**\n# {descripcion}\n"
    
    # Nombre del archivo
    nombre_archivo = f"{numero}_Trabajando_con_clases_y_objetos.py"
    
    # Crear el archivo y escribir el contenido
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)

print("Archivos creados con éxito.")
