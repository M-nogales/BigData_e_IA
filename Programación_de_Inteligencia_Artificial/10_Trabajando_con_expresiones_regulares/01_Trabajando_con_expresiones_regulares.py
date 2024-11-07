import json
import re

def cargar_datos_alumnos(nombre_archivo):
    with open(nombre_archivo, "r") as f:
        return json.load(f)

# Validación de Alumnos
def patron_email(email):
    # Validación de un email simple
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, email) is not None

def patron_telefono(telefono):
    # Validación de un teléfono que comience con 6, 7 o 9 y tenga 9 dígitos
    patron = r'^[679]\d{8}$'
    return re.match(patron, telefono) is not None

def patron_codigo_postal(codigo_postal):
    # Validación de un código postal con 5 dígitos
    patron = r'^\d{5}$'
    return re.match(patron, codigo_postal) is not None

alumnos = cargar_datos_alumnos("jsons/01_alumnos.json")

for alumno in alumnos:
    if patron_email(alumno['email']):
        print(f"El email de {alumno['nombre']} es válido.")
    else:
        print(f"El email de {alumno['nombre']} no es válido.")
    
    if patron_telefono(alumno['telefono']):
        print(f"El teléfono de {alumno['nombre']} es válido.")
    else:
        print(f"El teléfono de {alumno['nombre']} no es válido.")
    
    if patron_codigo_postal(alumno['codigo_postal']):
        print(f"El código postal de {alumno['nombre']} es válido.")
    else:
        print(f"El código postal de {alumno['nombre']} no es válido.")