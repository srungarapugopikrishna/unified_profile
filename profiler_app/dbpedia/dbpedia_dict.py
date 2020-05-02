import json
from pprint import pprint
# Opening JSON file
final_data = []
with open('dbpedia_human_data.json') as json_file:
    data = json.load(json_file)
    bindings = data['results']['bindings']
    for item in bindings:
        # temp_dict = {'surname': None, 'name': None, 'givenName': None, 'birth': None, 'gender': None,
        #              'description': None, 'person': None}
        temp_dict = {}
        for key in item.keys():
            temp_dict[key] = item[key]['value']
        final_data.append(temp_dict)
    json_object = json.dumps(final_data)

    # Writing to sample.json
    with open("dbpedia_data.json", "w") as outfile:
        outfile.write(json_object)

    import pdb; pdb.set_trace()