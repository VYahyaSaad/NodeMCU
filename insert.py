from conn import collections as coll

a = coll.insert_one({"status": [{"led1": 0}]})
print(a)