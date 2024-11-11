import json
import requests

url_regions = 'https://pokeapi.co/api/v2/region'

response_regions = requests.get(url_regions)

if response_regions.status_code == 200:
    data = response_regions.json()
    cantidad_resultados = data.get("count")
    regiones = data.get("results")
    
    resultado = {
        "quantity": cantidad_resultados,
        "regions": [{"name": region["name"].lower(), "url": region["url"]} for region in regiones]
    }

    output_file_path = "data/regions_api_url.json"
    with open(output_file_path, "w") as archivo:
        json.dump(resultado, archivo, indent=4)

    print(f"Los datos se han guardado en {output_file_path}")
else:
    print(f"Error al hacer la solicitud: {response_regions.status_code}")
