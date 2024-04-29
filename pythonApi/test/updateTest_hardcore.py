import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]


data = {"name":"read"}

find_one_result = collection.find_one(data)

a = find_one_result.get("yes_or_no")
a.insert(0, {"yes_or_no":1, "comment":"second time"})

result = collection.update_one({"name":"read"}, {"$set": {"yes_or_no": a}})