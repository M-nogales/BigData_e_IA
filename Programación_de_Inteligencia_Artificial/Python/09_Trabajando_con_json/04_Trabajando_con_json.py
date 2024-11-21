# 04. **Registro de Ventas**
# Información sobre ventas, incluyendo producto, cantidad vendida, precio y fecha.
# Incorpora al menos 10 ventas al registro. 
# Calcular el total de ventas,filtrar por fecha o producto, agregar nuevas ventas.
'''  JSON = 
{
    "ventas": [
        {"producto": "Laptop", "cantidad": 2, "precio": 1000, "fecha": "2024-10-28"},
        {"producto": "Teclado", "cantidad": 5, "precio": 50, "fecha": "2024-10-27"}
    ]
}
'''
import json

registro_ventas = {
    "ventas": [
        {"producto": "Laptop", "cantidad": 2, "precio": 1000, "fecha": "2024-10-28"},
        {"producto": "Teclado", "cantidad": 5, "precio": 50, "fecha": "2024-10-27"},
    ]}

def agregar_venta(producto, cantidad, precio, fecha):
    nueva_venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "fecha": fecha
    }
    registro_ventas["ventas"].append(nueva_venta)
    return "Venta añadida"

def calcular_total_ventas():
    total = 0
    for venta in registro_ventas["ventas"]:
        total += venta["cantidad"] * venta["precio"]
    return total

def filtrar_ventas(fecha=None, producto=None):
    ventas_filtradas = []
    for venta in registro_ventas["ventas"]:
        if (fecha and venta["fecha"] == fecha) or (producto and venta["producto"].lower() == producto.lower()):
            ventas_filtradas.append(venta)
    return ventas_filtradas

def guardar_registro():
    with open("jsons/04_ventas.json", "w") as archivo:
        json.dump(registro_ventas, archivo, indent=2)

# pereza repetirlo 10 veces/bucle
print('agregar_venta("Tablet", 3, 300, "2024-10-30"): ',
      agregar_venta("Tablet", 3, 300, "2024-10-30"))
print('calcular_total_ventas(): ', calcular_total_ventas())
print('filtrar_ventas(fecha="2024-10-28"): ', filtrar_ventas(fecha="2024-10-28"))
print('filtrar_ventas(producto="Mouse"): ', filtrar_ventas(producto="Mouse"))
print('filtrar_ventas(producto="Tablet"): ', filtrar_ventas(producto="Tablet"))

guardar_registro()