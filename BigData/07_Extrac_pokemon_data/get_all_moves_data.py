import json
import requests

# Definir las rutas de los archivos
moves_api_path = 'data/moves_api_url.json'
moves_data_path = 'data/moves_data.json'

# Leer el archivo moves_api_url.json
with open(moves_api_path, 'r', encoding='utf-8') as file:
    moves_data = json.load(file)

# Obtener la lista de movimientos y la cantidad de movimientos
movimientos = moves_data['moves']
cantidad_movimientos = moves_data['quantity']

# Crear una lista para almacenar los datos detallados de cada movimiento
moves_detailed_data = []

# Realizar solicitudes a cada URL para obtener los datos de cada movimiento
for move in movimientos:
    move_name = move['name']
    move_url = move['url']
    
    try:
        # Hacer la solicitud a la URL del movimiento
        response = requests.get(move_url)
        response.raise_for_status()  # Verificar si hubo un error en la solicitud
        move_info = response.json()  # Convertir la respuesta en JSON
        
        # Añadir los datos del movimiento a la lista
        moves_detailed_data.append(move_info)
        print(f"Datos de {move_name} obtenidos correctamente.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {move_name}: {e}")

# Crear el diccionario final para el archivo moves_data.json
moves_data_output = {
    "quantity": cantidad_movimientos,
    "moves": moves_detailed_data
}

# Guardar los datos en moves_data.json
with open(moves_data_path, 'w', encoding='utf-8') as file:
    json.dump(moves_data_output, file, ensure_ascii=False, indent=4)

print(f"Datos de {cantidad_movimientos} movimientos guardados en {moves_data_path}")
