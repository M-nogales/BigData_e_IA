import json

persona = {
    "nombre": "Elena",
    "apellido": "Cerezo",
    "edad": 20,
    "ciudad":"Barcelona",
    "coches":[
        {"modelo": "BMW","consumo":3},
        {"modelo": "Dacia","consumo":6}
    ],
    "casada": True
}

json_datos = json.dumps(persona, indent=4)
print('json_datos: ', json_datos)

#guardar fichero
with open("ejemplo.json","w") as fichero:
    json.dump(json_datos,fichero,indent=4)


#lectura de json
with open("ejemplo.json","r") as fichero_lectura:
    datos = json.load(fichero_lectura)
    
print('datos: ', datos)

