import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]

data = {"name":"read"}

result = collection.find_one(data)

print(result.get("icon"))
print(result.get("name"))