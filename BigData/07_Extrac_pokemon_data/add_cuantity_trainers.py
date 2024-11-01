import json

# Definir la ruta del archivo
trainers_path = 'data/trainers.json'

# Leer el archivo trainers.json
with open(trainers_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Contar la cantidad de entrenadores
cantidad_entrenadores = len(data['entrenadores'])

# Añadir la cantidad al diccionario principal
data['cantidad'] = cantidad_entrenadores

# Guardar los cambios en el mismo archivo trainers.json
with open(trainers_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"{cantidad_entrenadores} entrenadores añadidos a {trainers_path} como 'cantidad'")
