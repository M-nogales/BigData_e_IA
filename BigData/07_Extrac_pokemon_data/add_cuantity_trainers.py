import json

trainers_path = 'data/trainers.json'

with open(trainers_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

cantidad_entrenadores = len(data['entrenadores'])

data['cantidad'] = cantidad_entrenadores

with open(trainers_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"{cantidad_entrenadores} entrenadores añadidos a {trainers_path} como 'cantidad'")
