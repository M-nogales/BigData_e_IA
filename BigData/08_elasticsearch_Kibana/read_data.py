import json

# Abrimos y leemos el archivo restaurantes.json
with open('restaurantes.json', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Crear una lista de diccionarios con la estructura adecuada
json_objects = []
for i in range(0, len(lines), 2):
    action = json.loads(lines[i])  # Indexación (acción)
    document = json.loads(lines[i + 1])  # Documento de datos
    # Agregar el documento bajo la acción de indexación
    json_objects.append({
        "index": action["index"],  # Mantenemos el índice
        "document": document  # El documento con los datos
    })

# Guardar el resultado en un archivo de salida, por ejemplo, 'restaurantes_formatted.json'
with open('restaurantes_formatted.json', 'w', encoding='utf-8') as output_file:
    json.dump(json_objects, output_file, ensure_ascii=False, indent=4)

# Si prefieres ver la salida en consola
formatted_json = json.dumps(json_objects, indent=4, ensure_ascii=False)
print(formatted_json)
