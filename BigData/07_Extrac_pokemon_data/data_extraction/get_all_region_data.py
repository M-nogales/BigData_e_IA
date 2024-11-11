import json
import requests

regions_path = 'data/regions_api_url.json'
regions_data_path = 'data/regions_data.json'

with open(regions_path, 'r', encoding='utf-8') as file:
    regions_data = json.load(file)

regions = regions_data['regions']
cantidad_regiones = regions_data['quantity']

regions_detailed_data = []

for region in regions:
    region_name = region['name'].lower()
    region_url = region['url']
    
    try:
        response = requests.get(region_url)
        response.raise_for_status()
        region_info = response.json()
        
        regions_detailed_data.append(region_info)
        print(f"Datos de {region_name} obtenidos correctamente.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {region_name}: {e}")

regions_data_output = {
    "quantity": cantidad_regiones,
    "regions": regions_detailed_data
}

with open(regions_data_path, 'w', encoding='utf-8') as file:
    json.dump(regions_data_output, file, ensure_ascii=False, indent=4)

print(f"Datos de {cantidad_regiones} regiones guardados en {regions_data_path}")
