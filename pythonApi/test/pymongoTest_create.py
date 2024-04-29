import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]


# diciplines done
discipline_booleans = []

for i in range(365) :
    a = {"yes_or_no" : 0, "comment" : ""}
    discipline_booleans.append(a)






data = {"icon":"📚", "name":"read", "yes_or_no": discipline_booleans}


# Insert a single document
result = collection.insert_one(data)
print("Inserted document ID:", result.inserted_id)