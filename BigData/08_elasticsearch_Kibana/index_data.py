import json

# Abrimos y leemos el archivo restaurantes_formatted.json
with open('restaurantes_formatted.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Crear un conjunto para almacenar los tipos de precio únicos
precios = set()

# Iteramos sobre cada documento de restaurante
for entry in data:
    # Extraemos el precio del documento
    precio = entry['document'].get('PRECIO', None)
    
    # Si existe un precio, lo añadimos al conjunto
    if precio:
        precios.add(precio)

# Convertimos el conjunto a una lista y la ordenamos
precios_list = sorted(list(precios))

# Imprimimos el índice de precios encontrados
print("Índice de Tipos de Precio:")
for precio in precios_list:
    print(precio)
