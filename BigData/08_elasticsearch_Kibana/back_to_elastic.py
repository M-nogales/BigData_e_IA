import json

# Abrimos y leemos el archivo restaurantes_formatted.json
with open('restaurantes_formatted.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Abrir un archivo de salida para el formato de Elasticsearch
with open('restaurantes_bulk.json', 'w', encoding='utf-8') as output_file:
    for entry in data:
        # Definir la acción de indexación
        action = {
            "index": {
                "_index": "restaurantes",  # Nombre del índice
                "_id": entry['document']['ID']  # ID único del restaurante
            }
        }
        
        # Escribir la acción y el documento
        output_file.write(json.dumps(action, ensure_ascii=False) + '\n')
        output_file.write(json.dumps(entry['document'], ensure_ascii=False) + '\n')

print("Archivo de transformación a formato Elasticsearch creado: restaurantes_bulk.json")
