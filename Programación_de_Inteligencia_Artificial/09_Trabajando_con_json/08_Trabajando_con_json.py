# 08. **Agenda de Eventos**
# Listado de eventos con información como título, fecha, ubicación y organizador.
# Filtrar eventos por fecha o ubicación, agregar eventos futuros, eliminar eventos pasados.
'''  JSON = 
{
    "eventos": [
        {"titulo": "Conferencia Python", "fecha": "2024-11-15", "ubicacion": "Madrid", "organizador": "PyCon España"},
        {"titulo": "Taller de IA", "fecha": "2024-12-01", "ubicacion": "Barcelona", "organizador": "TechFest"}
    ]
}
'''
import json
from datetime import datetime

agenda_eventos = {
    "eventos": [
        {"titulo": "Conferencia Python", "fecha": "2024-11-15", "ubicacion": "Madrid", "organizador": "PyCon España"},
        {"titulo": "Taller de IA", "fecha": "2024-12-01", "ubicacion": "Barcelona", "organizador": "TechFest"},
    ]}

def agregar_evento(titulo, fecha, ubicacion, organizador):
    nuevo_evento = {
        "titulo": titulo,
        "fecha": fecha,
        "ubicacion": ubicacion,
        "organizador": organizador
    }
    agenda_eventos["eventos"].append(nuevo_evento)
    return "Evento añadido"

def filtrar_eventos(fecha=None, ubicacion=None):
    eventos_filtrados = []
    for evento in agenda_eventos["eventos"]:
        if (fecha and evento["fecha"] == fecha) or (ubicacion and evento["ubicacion"].lower() == ubicacion.lower()):
            eventos_filtrados.append(evento)
    return eventos_filtrados

def eliminar_eventos_pasados():
    fecha_actual = datetime.now().date().strftime("%Y-%m-%d")
    for evento in agenda_eventos["eventos"]:
        if evento["fecha"] < fecha_actual:
            agenda_eventos["eventos"].remove(evento)
    return "Eventos pasados eliminados"

def guardar_agenda():
    with open("jsons/08_eventos.json", "w") as archivo:
        json.dump(agenda_eventos, archivo, indent=2)

# pereza repetirlo 10 veces/bucle
print('agregar_evento("Maratón de Programación", "2024-11-30", "Madrid", "CodeFest"): ',
      agregar_evento("Maratón de Programación", "2024-11-30", "Madrid", "CodeFest"))
print('agregar_evento("Charla de Ciberseguridad", "2024-12-15", "Valencia", "CyberSec"): ',
      agregar_evento("Charla de Ciberseguridad", "2020-12-15", "Valencia", "CyberSec"))

print('filtrar_eventos(fecha="2024-11-15"): ', filtrar_eventos(fecha="2024-11-15"))
print('filtrar_eventos(ubicacion="Madrid"): ', filtrar_eventos(ubicacion="Madrid"))
print('eliminar_eventos_pasados()(fecha actual): ', eliminar_eventos_pasados())
guardar_agenda()
