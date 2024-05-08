import pymongo
import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]

now = datetime.datetime.now()

def add_day(discipline_name, comment) :
    discipline_search = {"name":discipline_name}
    find_one_result = collection.find_one(discipline_search)

    a = find_one_result.get("tracing")
    a.insert(0, {"date":now.strftime('%y-%m-%d'), "comment":comment})

    result = collection.update_one({"name":discipline_name}, {"$set": {"tracing": a}})

add_day("cold shower", "")