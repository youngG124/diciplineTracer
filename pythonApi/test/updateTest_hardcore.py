import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]

def add_day(discipline_name) :
    discipline_search = {"name":discipline_name}
    find_one_result = collection.find_one(discipline_search)

    a = find_one_result.get("yes_or_no")
    a.insert(0, {"yes_or_no":0, "comment":""})

    result = collection.update_one({"name":discipline_name}, {"$set": {"yes_or_no": a}})

disciplines = ["read", "run", "clean", "push-ups", "cold shower"]

for i in disciplines :
    add_day(i)