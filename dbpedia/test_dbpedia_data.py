import json
from pprint import pprint
with open('./dbpedia_to_mongo_success_1.json') as json_file:
    data = json.load(json_file)
pprint(data[0])