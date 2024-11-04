import json

# Definir las rutas de los archivos
trainers_path = 'data/trainers.json'
villains_path = 'data/villains.json'

# Leer el archivo trainers.json
with open(trainers_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Filtrar los entrenadores que son villanos
villains = [trainer for trainer in data['trainers'] if trainer.get('villains')]

# Crear la estructura para el archivo villains.json
villains_data = {
    "quantity": len(villains),
    "villains": villains
}

# Guardar los villanos en villains.json
with open(villains_path, 'w', encoding='utf-8') as file:
    json.dump(villains_data, file, ensure_ascii=False, indent=4)

print(f"{len(villains)} villanos guardados en {villains_path}")
