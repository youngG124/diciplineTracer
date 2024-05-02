import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["disciplineTracer"]
collection = db["discipline"]


# diciplines done
discipline_booleans = []

a = {"date" : "", "comment" : ""}
# discipline_booleans.append(a)

dcpln1 = {"icon":"📚", 
          "name":"read", 
          "explain":"read at least 30m", 
          "tracing": discipline_booleans}

dcpln2 = {"icon":"🏃🏻‍♂️", 
          "name":"running",
          "explain":"5k run around 20m",
          "tracing": discipline_booleans}

dcpln3 = {"icon":"🧹", 
          "name":"cleaning", 
          "explain":"clean floor or toilet", 
          "tracing": discipline_booleans}

dcpln4 = {"icon":"💪🏼", 
          "name":"push-ups", 
          "explain":"40-35-30-25-20 for 15m", 
          "tracing": discipline_booleans}

dcpln5 = {"icon":"🥶", 
          "name":"cold shower", 
          "explain":"just cold shower and concentrate on pain", 
          "tracing": discipline_booleans}

# Insert a single document
for i in [dcpln1, dcpln2, dcpln3, dcpln4, dcpln5] :
    collection.insert_one(i)