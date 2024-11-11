from pymongo import MongoClient

mongo_user = "root"
mongo_password = "example"
mongo_host = "localhost"
mongo_port = 27017

def update_trainers_gym(trainers_collection, gym_collection, database_name='test'):
    client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
    db = client[database_name]
    trainers_col = db[trainers_collection]
    gym_col = db[gym_collection]


    for trainer in trainers_col.find():
        updated = False
        new_gym = []
        gym_name = trainer.get('gym')

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
                trainers_col.update_one({'_id': trainer['_id']}, {'$set': {'gym': new_gym}})

    client.close()

update_trainers_gym(database_name="pokemon", trainers_collection='trainers',gym_collection="gyms")