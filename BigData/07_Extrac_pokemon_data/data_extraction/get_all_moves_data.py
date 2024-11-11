import json
import requests

moves_api_path = 'data/moves_api_url.json'
moves_data_path = 'data/moves_data.json'

with open(moves_api_path, 'r', encoding='utf-8') as file:
    moves_data = json.load(file)

# lista de movimientos y la cantidad de movimientos
movimientos = moves_data['moves']
cantidad_movimientos = moves_data['quantity']

# lista para almacenar los datos detallados de cada movimiento
moves_detailed_data = []

# realizar solicitudes a cada URL para obtener los datos de cada movimiento
for move in movimientos:
    move_name = move['name']
    move_url = move['url']
    
    try:
        # hacer la solicitud a la URL del movimiento
        response = requests.get(move_url)
        # verificar si hubo un error en la solicitud
        response.raise_for_status()
        move_info = response.json()
        
        # añadir movimientos a la lista
        moves_detailed_data.append(move_info)
        print(f"Datos de {move_name} obtenidos correctamente.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {move_name}: {e}")

# estructura para moves_data.json
moves_data_output = {
    "quantity": cantidad_movimientos,
    "moves": moves_detailed_data
}

with open(moves_data_path, 'w', encoding='utf-8') as file:
    json.dump(moves_data_output, file, ensure_ascii=False, indent=4)

print(f"Datos de {cantidad_movimientos} movimientos guardados en {moves_data_path}")
