# 05. **Información de Alumnos**
# Datos sobre estudiantes, incluyendo nombre, edad, calificación y ciudad.
# Inserta al menos 10 alumnos al fichero JSON.
# Filtrar alumnos aprobados, calcular la edad promedio, agregar y eliminar alumnos.
'''  JSON = 
{
    "alumnos": [
        {"nombre": "Carlos", "edad": 20, "calificacion": 85, "ciudad": "Madrid"},
        {"nombre": "Lucía", "edad": 22, "calificacion": 90, "ciudad": "Barcelona"}
    ]
}
'''
import json

registro_alumnos = {
    "alumnos": [
        {"nombre": "Carlos", "edad": 20, "calificacion": 85, "ciudad": "Madrid"},
        {"nombre": "Lucía", "edad": 22, "calificacion": 90, "ciudad": "Barcelona"},
    ]}

def agregar_alumno(nombre, edad, calificacion, ciudad):
    nuevo_alumno = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion,
        "ciudad": ciudad
    }
    registro_alumnos["alumnos"].append(nuevo_alumno)
    return "Alumno añadido"

def encontrar_alumno(nombre):
    for alumno in registro_alumnos["alumnos"]:
        if alumno["nombre"].lower() == nombre.lower():
            return alumno
    return None

def eliminar_alumno(nombre):
    alumno_encontrado = encontrar_alumno(nombre)
    if alumno_encontrado:
        registro_alumnos["alumnos"].remove(alumno_encontrado)
        return "Alumno eliminado"
    return "Alumno no encontrado"

def filtrar_aprobados(min_calificacion=49.9):
    alumnos_aprobados = []
    for alumno in registro_alumnos["alumnos"]:
        if alumno["calificacion"] >= min_calificacion:
            alumnos_aprobados.append(alumno)
    return alumnos_aprobados

def calcular_edad_promedio():
    total_edad = sum(alumno["edad"] for alumno in registro_alumnos["alumnos"])
    promedio = total_edad / len(registro_alumnos["alumnos"])
    return promedio

def guardar_informacion():
    with open("jsons/05_alumnos.json", "w") as archivo:
        json.dump(registro_alumnos, archivo, indent=2)

# pereza repetirlo 10 veces/bucle
print('agregar_alumno("Elena", 20, 82, "Cádiz"): ',
      agregar_alumno("Elena", 20, 82, "Cádiz"))
print('eliminar_alumno("Raúl"): ', eliminar_alumno("Raúl"))
print('filtrar_aprobados(): ', filtrar_aprobados())
print('calcular_edad_promedio(): ', calcular_edad_promedio())
guardar_informacion()