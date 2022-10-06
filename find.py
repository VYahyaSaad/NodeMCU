from conn import collections as coll
from bson import ObjectId
from bson.json_util import dumps
import json
a = coll.find_one({'_id':ObjectId("633e9d02c53dcece1b822124")})
a = json.loads(dumps(a))
print(a["status"])