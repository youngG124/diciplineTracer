import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]

data = {"name": "John", "age": 30, "city": "New York"}

# Insert a single document
result = collection.insert_one(data)
print("Inserted document ID:", result.inserted_id)