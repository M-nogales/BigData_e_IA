import json

# Función para normalizar los valores de PRECIO
def normalizar_precio(precio):
    # Normalizamos los tipos de precio
    if precio:
        precio = precio.strip().lower()  # Convertir a minúsculas y quitar espacios
        if 'económico' in precio:
            return 'Económico'
        elif 'medio' in precio:
            return 'Precio medio'
    return precio  # Si no se encuentra un valor que normalizar, lo dejamos tal cual

# Abrimos y leemos el archivo restaurantes_formatted.json
with open('restaurantes_formatted.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iteramos sobre cada entrada de restaurante y normalizamos el precio
for entry in data:
    # Normalizamos el campo PRECIO
    entry['document']['PRECIO'] = normalizar_precio(entry['document'].get('PRECIO', ''))

# Guardamos los cambios en el archivo restaurantes_formatted.json
with open('restaurantes_formatted.json', 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=4)

# Si prefieres ver los cambios en consola
formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
print(formatted_json)
