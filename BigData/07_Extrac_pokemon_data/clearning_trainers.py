import json
import os

# Definir la ruta del archivo JSON
json_file_path = os.path.join('data', 'trainers.json')

# Cargar el archivo JSON
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Crear un nuevo diccionario para almacenar la relación entre entrenadores y generaciones
trainers_with_generation = {}

# Iterar sobre cada generación y agregar entrenadores a su respectivo objeto
for generation_key, trainers in data['entrenadores'].items():
    for trainer in trainers:
        trainer_name = trainer['nombre']
        
        # Si el entrenador ya está en el nuevo diccionario, agregar la generación
        if trainer_name in trainers_with_generation:
            trainers_with_generation[trainer_name]['generation'].append(generation_key)
        else:
            # Agregar un nuevo entrenador con la generación correspondiente
            trainers_with_generation[trainer_name] = {
                'nombre': trainer_name,
                'generation': [generation_key],  # Iniciar con la generación actual
                'gymnasio': trainer['gymnasio'],
                'alto_mando': trainer['alto_mando'],
                'villano': trainer['villano']
            }

# Convertir el diccionario a una lista
trainers_list = list(trainers_with_generation.values())

# Guardar el nuevo archivo JSON
output_file_path = os.path.join('data', 'trainers_with_generations.json')
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump({'entrenadores': trainers_list}, file, indent=4)

trainers_list
