import requests
import json

url = 'https://api.ejemplo.com/data'
poke_url="https://pokeapi.co/api/v2/pokemon?limit=100000"

response_poke = requests.get(poke_url)

if response_poke.status_code == 200:

    data = response_poke.json()
    cantidad_resultados = data.get("count")
    pokemones = data.get("results")

    resultado = {
        "cantidad": cantidad_resultados,
        "pokemones": [{"nombre": pokemon["name"], "url": pokemon["url"]} for pokemon in pokemones]
    }

    output_file_path = "data/pokemons_api_url.json"
    
    with open(output_file_path, "w") as archivo:
        json.dump(resultado, archivo, indent=4)

    print("Los datos se han guardado en pokemons_api_url.json")
else:
    print(f"Error al hacer la solicitud: {response_poke.status_code}")

