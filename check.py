from bson.json_util import dumps
from conn import collections as coll
import json

change_stream = coll.watch()
id = "633e95c0fe5ca619d1036596"
for change in change_stream:
    changes = json.loads(dumps(change))
    print(changes)
    print("---------------------------")
    if changes['operationType'] == 'update':
        if id == changes["documentKey"]['_id']['$oid']:
            print(changes["updateDescription"]["updatedFields"])

