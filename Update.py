from conn import collections as coll
from bson import ObjectId

# update = coll.find_one_and_update({"_id": ObjectId('633e71d56a6159ca64d7bafb')}, {"$set":{"led1":{"LedStatus": 0}})
update = coll.find_one_and_update({"_id": ObjectId('633e95c0fe5ca619d1036596')},
                                  {"$set": {"$push": {"status": {"led2": 0}}}})
print(update)
