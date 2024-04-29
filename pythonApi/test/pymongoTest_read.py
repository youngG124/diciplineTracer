import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]

data = {"name":"read"}


# Insert a single document
result = collection.find_one(data)
print("Inserted document ID:", result)