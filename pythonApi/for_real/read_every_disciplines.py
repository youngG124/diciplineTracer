import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]

cursor = collection.find({})

for document in cursor:
    print(document.get("name"))