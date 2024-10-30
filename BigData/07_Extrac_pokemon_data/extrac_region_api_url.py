import json
import requests  # Asegúrate de tener esta librería instalada

# Aquí debes colocar la URL de tu API
url_regions = 'https://pokeapi.co/api/v2/region'

# Realizar la solicitud a la API
response_regions = requests.get(url_regions)

# Verificar si la solicitud fue exitosa
if response_regions.status_code == 200:
    data = response_regions.json()  # Convertir respuesta a JSON
    cantidad_resultados = data.get("count")  # Obtener el total de Pokémon
    regiones = data.get("results")  # Obtener la lista de Pokémon

    resultado = {
        "cantidad": cantidad_resultados,
        "regiones": [{"nombre": region["name"], "url": region["url"]} for region in regiones]
    }

    output_file_path = "data/regions_api_url.json"
    with open(output_file_path, "w") as archivo:
        json.dump(resultado, archivo, indent=4)

    print(f"Los datos se han guardado en {output_file_path}")
else:
    print(f"Error al hacer la solicitud: {response_regions.status_code}")
