# 01. **Directorio Telefónico**
# Contiene contactos con campos como nombre, apellidos, teléfono y correo electrónico.
#  Insertar al menos 10 registros telefónicos.
#  Búsqueda de contacto por nombre, actualización de número de teléfono,
#  agregar o eliminar un contacto.
'''  JSON = 
{
    "contactos": [
        {"nombre": "Juan", "apellidos": "Pérez", "telefono": "612345678", "correo": "juan@example.com"},
        {"nombre": "Laura", "apellidos": "Gómez", "telefono": "623456789", "correo": "laura@example.com"}
    ]
}
'''

import json
import os

directorio = {
    "contactos": [
        {"nombre": "Juan", "apellidos": "Pérez", "telefono": "612345678", "correo": "juan@example.com"},
        {"nombre": "Laura", "apellidos": "Gómez", "telefono": "623456789", "correo": "laura@example.com"},
    ]
}

def buscar_contacto(nombre):
    for contacto in directorio["contactos"]:
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return "Contacto no encontrado"

def actualizar_telefono(nombre, nuevo_telefono):
    contacto = buscar_contacto(nombre)
    if contacto:
        contacto["telefono"] = nuevo_telefono
        return True
    return "Contacto no encontrado"

def agregar_contacto(nombre, apellidos, telefono, correo):
    nuevo_contacto = {
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo
    }
    directorio["contactos"].append(nuevo_contacto)
    return "Contacto agregado"

def eliminar_contacto(nombre):
    contacto = buscar_contacto(nombre)
    if contacto:
        directorio["contactos"].remove(contacto)
        return True
    return "Contacto no encontrado"

def guardar_directorio():
    # Guardar el directorio en un archivo JSON
    with open("jsons/01_directorio.json", "w") as archivo:
        json.dump(directorio, archivo, indent=2)

# pereza repetirlo 10 veces/bucle
print("Agregar contacto:",agregar_contacto("María", "García", "634567890", "maria@yopmail.com"))
print("Buscar contacto: ", buscar_contacto("Juan"))
print("Actualizar teléfono: ", actualizar_telefono("Juan", "612345679"))
guardar_directorio()  
eliminar_contacto("Juan")
print("Buscar_contacto('Juan'):", buscar_contacto("Juan"))
# guardar_directorio() 
