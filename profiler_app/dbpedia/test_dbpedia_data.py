import json
from pprint import pprint
with open('dbpedia_to_mongo_success_1.json') as json_file:
    data = json.load(json_file)
keys = []
for rec in data:
    for key in rec.keys():
        if key not in keys:
            keys.append(key)
print(len(keys))
print(keys)
