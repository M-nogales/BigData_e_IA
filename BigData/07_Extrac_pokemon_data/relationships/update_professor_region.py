from pymongo import MongoClient

mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_professors_region(professors_collection, regions_collection, database_name='test'):
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    professors_col = db[professors_collection]
    region_col = db[regions_collection]

    for professor in professors_col.find():
        updated = False
        new_regions = []
        region_name = professor.get('region')

        if region_name:
            region = region_col.find_one({'name': region_name.lower()})  # Convertimos a minúsculas para asegurarnos de que coincida
            if region:

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
                professors_col.update_one({'_id': professor['_id']}, {'$set': {'region': new_regions}})

    client.close()

update_professors_region(database_name="pokemon", professors_collection='professors',regions_collection="regions")