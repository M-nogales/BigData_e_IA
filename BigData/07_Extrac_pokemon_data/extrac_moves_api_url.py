import requests
import json


moves_url="https://pokeapi.co/api/v2/move?limit=1000"

response_moves = requests.get(moves_url)

if response_moves.status_code == 200:

    data = response_moves.json()
    cantidad_resultados = data.get("count")
    moves = data.get("results")

    resultado = {
        "cantidad": cantidad_resultados,
        "movimientos": [{"nombre": move["name"], "url": move["url"]} for move in moves]
    }

    output_file_path = "data/moves_api_url.json"
    
    with open(output_file_path, "w") as archivo:
        json.dump(resultado, archivo, indent=4)

    print("Los datos se han guardado en moves_api_url.json")
else:
    print(f"Error al hacer la solicitud: {response_moves.status_code}")