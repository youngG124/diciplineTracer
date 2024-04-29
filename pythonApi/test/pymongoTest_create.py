import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]


# diciplines done
discipline_booleans = []

a = {"yes_or_no" : 0, "comment" : ""}
discipline_booleans.append(a)

dcpln1 = {"icon":"📚", 
          "name":"read", 
          "explain":"read at least 30m", 
          "yes_or_no": discipline_booleans}

dcpln2 = {"icon":"🏃🏻‍♂️", 
          "name":"running",
          "explain":"5k run around 20m",
          "yes_or_no": discipline_booleans}

dcpln3 = {"icon":"🧹", 
          "name":"cleaning", 
          "explain":"clean floor or toilet", 
          "yes_or_no": discipline_booleans}

dcpln4 = {"icon":"💪🏼", 
          "name":"push-ups", 
          "explain":"40-35-30-25-20 for 15m", 
          "yes_or_no": discipline_booleans}

dcpln5 = {"icon":"🥶", 
          "name":"cold shower", 
          "explain":"just cold shower and concentrate on pain", 
          "yes_or_no": discipline_booleans}

# Insert a single document
collection.insert_one(dcpln1)
collection.insert_one(dcpln2)
collection.insert_one(dcpln3)
collection.insert_one(dcpln4)
collection.insert_one(dcpln5)