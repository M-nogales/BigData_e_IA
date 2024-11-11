import json
import requests

# ruta del con las URLs de los Pokémon
input_file_path = 'data/pokemons_api_url.json'
output_file_path = 'data/pokemons_data.json'

with open(input_file_path, 'r') as file:
    pokemons_data = json.load(file)

pokemon_details = []

for pokemon in pokemons_data['pokemons']:
    name = pokemon['name']
    url = pokemon['url']
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        pokemon_info = response.json()
        
        pokemon_details.append(pokemon_info)
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {name}: {e}")

output_data = {
    "pokemons": pokemon_details
}

with open(output_file_path, 'w') as file:
    json.dump(output_data, file, indent=4)

print(f"Datos de los Pokémon guardados en {output_file_path}")
