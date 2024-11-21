# 03. **Agenda de Tareas**
# Contiene una lista de tareas con detalles como descripción, fecha de vencimiento y estado.
# Insertar al menos 10 tareas al fichero.
# Agregar nuevas tareas, actualizar el estado de una tarea, filtrar tareas completadas.
'''  JSON = 
{
    "tareas": [
        {"descripcion": "Estudiar Python", "vencimiento": "2024-11-01", "estado": "pendiente"},
        {"descripcion": "Revisar proyecto", "vencimiento": "2024-10-29", "estado": "completada"}
    ]
}
'''

import json

agenda = {
    "tareas": [
        {"descripcion": "Estudiar Python", "vencimiento": "2024-11-01", "estado": "pendiente"},
        {"descripcion": "Revisar proyecto", "vencimiento": "2024-10-29", "estado": "completada"},
    ]
}

def agregar_tarea(descripcion, vencimiento, estado="pendiente"):
    nueva_tarea = {
        "descripcion": descripcion,
        "vencimiento": vencimiento,
        "estado": estado
    }
    agenda["tareas"].append(nueva_tarea)
    return "Tarea añadida"

def actualizar_estado_tarea(descripcion, nuevo_estado):
    for tarea in agenda["tareas"]:
        if tarea["descripcion"].lower() == descripcion.lower():
            tarea["estado"] = nuevo_estado
            return True
    return "Tarea no encontrada"

def filtrar_tareas_completadas():
    tareas_completadas = []
    for tarea in agenda["tareas"]:
        if tarea["estado"] == "completada":
            tareas_completadas.append(tarea)
    return tareas_completadas

def guardar_agenda():
    with open("jsons/03_agenda.json", "w") as archivo:
        json.dump(agenda, archivo, indent=2)

# pereza repetirlo 10 veces/bucle
print('agregar_tarea("Preparar presentación", "2024-11-12"): ',
      agregar_tarea("Preparar presentación", "2024-11-12"))

print('actualizar_estado_tarea("Estudiar Python", "completada"): ',
      actualizar_estado_tarea("Estudiar Python", "completada"))

print('filtrar_tareas_completadas(): ', filtrar_tareas_completadas())
guardar_agenda()