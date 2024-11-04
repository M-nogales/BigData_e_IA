from pymongo import MongoClient

# Variables para conectarse a MongoDB
mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_professors_region(professors_collection, regions_collection, database_name='test'):
    # Configura la conexión a MongoDB
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    professors_col = db[professors_collection]
    region_col = db[regions_collection]

    # Iterar sobre todos los documentos en la colección professor
    for professor in professors_col.find():
        updated = False
        new_regions = []
        region_name = professor.get('region')
        if region_name:
            # Buscar el correspondiente en la colección 'region'
            region = region_col.find_one({'name': region_name.lower()})  # Convertimos a minúsculas para asegurarnos de que coincida
            if region:
                # Crear un nuevo documento de región con el '_id' y 'name'
                new_region_entry = {
                        '_id': region['_id'],
                        'name': region['name']
                }
                new_regions.append(new_region_entry)
                updated = True
            else:
                new_regions.append({
                    '_id': None,
                    'name': region_name
                })
            if updated:
                # Actualizar el documento en MongoDB
                professors_col.update_one({'_id': professor['_id']}, {'$set': {'region': new_regions}})

    # Cerrar la conexión
    client.close()

update_professors_region(database_name="pokemon", professors_collection='professors',regions_collection="regions")