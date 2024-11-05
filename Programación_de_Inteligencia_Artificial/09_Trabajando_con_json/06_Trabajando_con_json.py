# 06. **Concesionario de Coches**
# Lista de coches disponibles en un concesionario con detalles como marca,
# modelo, precio y año. El registro del concesionario debe contener al menos 10 vehículos.
# Filtrar por marca, calcular el valor promedio de los coches, actualizar precios.
'''  JSON = 
{
    "coches": [
        {"marca": "Toyota", "modelo": "Corolla", "precio": 20000, "año": 2023},
        {"marca": "Ford", "modelo": "Focus", "precio": 18000, "año": 2022}
    ]
}
'''

import json

registro_coches = {
    "coches": [
        {"marca": "Toyota", "modelo": "Corolla", "precio": 20000, "año": 2023},
        {"marca": "Ford", "modelo": "Focus", "precio": 18000, "año": 2022},
    ]}

def agregar_coche(marca, modelo, precio, año):
    nuevo_coche = {
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "año": año
    }
    registro_coches["coches"].append(nuevo_coche)
    return "Coche añadido"

def filtrar_por_marca(marca):
    coches_filtrados = []
    for coche in registro_coches["coches"]:
        if coche["marca"].lower() == marca.lower():
            coches_filtrados.append(coche)
    return coches_filtrados

def calcular_valor_promedio():
    if not registro_coches["coches"]:
        return 0
    total_precio = sum(coche["precio"] for coche in registro_coches["coches"])
    promedio = total_precio / len(registro_coches["coches"])
    return promedio

def actualizar_precio(marca, modelo, nuevo_precio):
    for coche in registro_coches["coches"]:
        if coche["marca"].lower() == marca.lower() and coche["modelo"].lower() == modelo.lower():
            coche["precio"] = nuevo_precio
            return "Precio actualizado"
    return "Coche no encontrado"

def guardar_informacion():
    with open("jsons/06_coches.json", "w") as archivo:
        json.dump(registro_coches, archivo, indent=2)

# pereza repetirlo 10 veces/bucle
print('agregar_coche("Tesla", "Model 3", 35000, 2023): ',
      agregar_coche("Tesla", "Model 3", 35000, 2023))
print('filtrar_por_marca("Toyota"): ', filtrar_por_marca("Toyota"))
print('calcular_valor_promedio(): ', calcular_valor_promedio())
print('actualizar_precio("Ford", "Focus", 17500): ', actualizar_precio("Ford", "Focus", 17500))
guardar_informacion()