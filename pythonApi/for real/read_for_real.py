import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]

disciplines = ["read", "run", "clean", "push-ups", "cold shower"]

for i in disciplines :
    result = collection.find_one({"name" : i})

    print(result)