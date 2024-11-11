from pymongo import MongoClient

mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_villains_gym(villains_collection, gym_collection, database_name='test'):
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    villains_col = db[villains_collection]
    gym_col = db[gym_collection]


    for villain in villains_col.find():
        updated = False
        new_gym = []
        gym_name = villain.get('gym')

        if gym_name:
            gym = gym_col.find_one({'name': gym_name})
            if gym:

                new_gym_entry = {
                        '_id': gym['_id'],
                        'name': gym['name']
                }

                new_gym.append(new_gym_entry)
                updated = True
            else:
                new_gym.append({
                    '_id': None,
                    'name': gym_name
                })
            if updated:
                villains_col.update_one({'_id': villain['_id']}, {'$set': {'gym': new_gym}})

    client.close()

update_villains_gym(database_name="pokemon", villains_collection='villains',gym_collection="gyms")