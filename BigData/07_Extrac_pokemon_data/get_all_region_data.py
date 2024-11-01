import json
import requests

# Definir las rutas de los archivos
regions_path = 'data/regions_api_url.json'
regions_data_path = 'data/regions_data.json'

# Leer el archivo regions_api_url.json
with open(regions_path, 'r', encoding='utf-8') as file:
    regions_data = json.load(file)

# Obtener la lista de regiones
regions = regions_data['regiones']
cantidad_regiones = regions_data['cantidad']

# Crear una lista para almacenar los datos de cada región
regions_detailed_data = []

# Realizar solicitudes a cada URL para obtener los datos de cada región
for region in regions:
    region_name = region['nombre']
    region_url = region['url']
    
    try:
        # Hacer la solicitud a la URL de la región
        response = requests.get(region_url)
        response.raise_for_status()  # Verificar si hubo un error en la solicitud
        region_info = response.json()  # Convertir la respuesta en JSON
        
        # Añadir los datos de la región a la lista
        regions_detailed_data.append({
            "nombre": region_name,
            "datos": region_info
        })
        print(f"Datos de {region_name} obtenidos correctamente.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de {region_name}: {e}")

# Crear el diccionario final para el archivo regions_data.json
regions_data_output = {
    "cantidad": cantidad_regiones,
    "regiones": regions_detailed_data
}

# Guardar los datos en regions_data.json
with open(regions_data_path, 'w', encoding='utf-8') as file:
    json.dump(regions_data_output, file, ensure_ascii=False, indent=4)

print(f"Datos de {cantidad_regiones} regiones guardados en {regions_data_path}")
