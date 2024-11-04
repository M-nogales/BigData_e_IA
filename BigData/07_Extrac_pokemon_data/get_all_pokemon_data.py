import json
import requests

# Ruta del archivo JSON original con las URLs de los Pokémon
input_file_path = 'data/pokemons_api_url.json'
output_file_path = 'data/pokemons_data.json'

# Cargar el archivo JSON
with open(input_file_path, 'r') as file:
    pokemons_data = json.load(file)

# Lista donde guardaremos la información completa de cada Pokémon
pokemon_details = []

# Recorrer cada Pokémon y hacer la consulta a la API
for pokemon in pokemons_data['pokemons']:
    nombre = pokemon['nombre']
    url = pokemon['url']
    
    # Realizar la solicitud a la API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        pokemon_info = response.json()
        
        # Agregar la información obtenida a la lista
        pokemon_details.append(pokemon_info)
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {nombre}: {e}")

# Estructura del JSON en el formato solicitado
output_data = {
    "pokemons": pokemon_details
}

# Guardar la información completa en un nuevo archivo JSON
with open(output_file_path, 'w') as file:
    json.dump(output_data, file, indent=4)

print(f"Datos de los Pokémon guardados en {output_file_path}")
