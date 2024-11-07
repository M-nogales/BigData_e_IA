import json
import re
from datetime import datetime

def cargar_datos_vehiculos(nombre_archivo):
    with open(nombre_archivo, "r") as f:
        return json.load(f)

def patron_matricula(matricula):
    patron = r'^\d{4}[A-Z]{3}$'
    return re.match(patron, matricula) is not None

def patron_ano(ano):
    anio_actual = datetime.now().year
    return 1900 <= ano <= anio_actual

def patron_email_propietario(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, email) is not None

vehiculos = cargar_datos_vehiculos("jsons/02_vehiculos.json")
for vehiculo in vehiculos:
    if patron_matricula(vehiculo['matricula']):
        print(f"La matrícula del vehículo {vehiculo['modelo']} es válida.")
    else:
        print(f"La matrícula del vehículo {vehiculo['modelo']} no es válida.")
    
    if patron_ano(vehiculo['aÃ±o']):
        print(f"El año del vehículo {vehiculo['modelo']} es válido.")
    else:
        print(f"El año del vehículo {vehiculo['modelo']} no es válido.")
    
    if patron_email_propietario(vehiculo['propietario_email']):
        print(f"El email del propietario del vehículo {vehiculo['modelo']} es válido.")
    else:
        print(f"El email del propietario del vehículo {vehiculo['modelo']} no es válido.")
