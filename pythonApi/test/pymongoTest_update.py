import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]


result = collection.update_one({"name":"read"}, {"$set": {"name": "read"}})

print(result)