import json

persona = {
    "nombre": "Elena",
    "apellido": "Cerezo",
    "edad": "20",
    "ciudad":"Barcelona"
}

json_datos = json.dumps(persona)
print('json_datos: ', json_datos)
