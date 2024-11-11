import json

trainers_path = 'data/trainers.json'
villains_path = 'data/villains.json'

with open(trainers_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# filtrar los entrenadores que son villanos
villains = [trainer for trainer in data['trainers'] if trainer.get('villains')]

# estructura para villains.json
villains_data = {
    "quantity": len(villains),
    "villains": villains
}

with open(villains_path, 'w', encoding='utf-8') as file:
    json.dump(villains_data, file, ensure_ascii=False, indent=4)

print(f"{len(villains)} villanos guardados en {villains_path}")
