import pymongo

client = pymongo.MongoClient("mongodb://yahyasaad:y1a2h3y4a5@ac-ythypua-shard-00-00.3ed9vec.mongodb.net:27017,ac-ythypua-shard-00-01.3ed9vec.mongodb.net:27017,ac-ythypua-shard-00-02.3ed9vec.mongodb.net:27017/?ssl=true&replicaSet=atlas-llpfza-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["nodemcu"]
collections = db["status"]
