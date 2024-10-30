import json
import os

# Definir la ruta del archivo JSON con los entrenadores y sus generaciones
input_file_path = os.path.join('data', 'trainers_with_generations.json')

# Cargar el archivo JSON
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Filtrar entrenadores que son villanos
villains = [trainer for trainer in data['entrenadores'] if trainer['villano']]

# Guardar la lista de villanos en un nuevo archivo JSON
output_file_path = os.path.join('data', 'villains.json')
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump({'villains': villains}, file, indent=4)

# Mostrar la lista de villanos
villains
