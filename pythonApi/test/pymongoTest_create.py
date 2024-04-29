import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]


# diciplines done
discipline_booleans = []

for i in range(365) :
    discipline_booleans.append(0)

# comments everyday
discipline_comments = []

for i in range(365) :
    discipline_comments.append("")


data = {"icon":"📚", "name":"read", "yes_or_no": discipline_booleans, "comment": discipline_comments}


# Insert a single document
result = collection.insert_one(data)
print("Inserted document ID:", result.inserted_id)