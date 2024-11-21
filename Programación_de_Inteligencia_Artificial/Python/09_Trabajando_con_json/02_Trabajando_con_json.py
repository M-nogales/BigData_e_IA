# 02. **Inventario de Productos**
# Listado de productos en una tienda con nombre, categoría, precio y cantidad en stock.
# Insertar al menos 10 productos en el inventario.
# Filtrar productos por categoría, calcular el valor total del inventario, actualizar stock.
'''  JSON = 
{
    "productos": [
        {"nombre": "Laptop", "categoria": "Electrónica", "precio": 1000, "stock": 15},
        {"nombre": "Teclado", "categoria": "Accesorios", "precio": 50, "stock": 30}
    ]
}
'''

import json

inventario = {
    "productos": [
        {"nombre": "Laptop", "categoria": "Electrónica", "precio": 1000, "stock": 15},
        {"nombre": "Teclado", "categoria": "Accesorios", "precio": 50, "stock": 30}
    ]
}

def agregar_producto(nombre, categoria, precio, stock):
    new_producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    inventario["productos"].append(new_producto)
    return "Producto añadido"

def calcular_valor_total():
    total = 0
    for producto in inventario["productos"]:
        total += producto["precio"] * producto["stock"]
    return total

def actualizar_stock(nombre, cantidad):
    for producto in inventario["productos"]:
        if producto["nombre"].lower() == nombre.lower():
            producto["stock"] += cantidad
            return True
    return "Producto no encontrado"

def filtrar_por_categoria(categoria):
    productos_filtrados = []
    for producto in inventario["productos"]:
        if producto["categoria"].lower() == categoria.lower():
            productos_filtrados.append(producto)
    return productos_filtrados

def guardar_inventario():
    with open("jsons/02_inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=2)


# pereza repetirlo 10 veces/bucle
print('agregar_producto("Mouse", "Accesorios", 20, 50): ',
       agregar_producto("Mouse", "Accesorios", 20, 50))

print('calcular_valor_total(): ', calcular_valor_total())
print('actualizar_stock("Laptop", 5): ', actualizar_stock("Laptop", 5))
print('filtrar_por_categoria("Electrónica"): ', filtrar_por_categoria("Electrónica"))
guardar_inventario()