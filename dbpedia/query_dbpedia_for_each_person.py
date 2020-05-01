import json
import requests
from pprint import pprint

def extract_property(property):
    print(property)
    property_index = property.find("#")+1
    property_val = property[property_index:]
    
    print(property_val)

data = []
with open('./dbpedia_data.json') as json_file:
    data = json.load(json_file)
    # import pdb; pdb.set_trace()
# for rec in data:
rec = data[23]
person_uri = rec['person']
print(person_uri)
person = person_uri.replace('http://dbpedia.org/resource/', '')
query = "http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F%3E%0D%0APREFIX+dbpedia2%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fproperty%2F%3E%0D%0APREFIX+dbpedia%3A+%3Chttp%3A%2F%2Fdbpedia.org%2F%3E%0D%0APREFIX+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0D%0ASELECT+%3Fproperty+%3FhasValue+%3FisValueOf+WHERE+%7B%7B%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F{}%3E+%3Fproperty+%3FhasValue%7D+UNION+%7B%3FisValueOf+%3Fproperty+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F{}%3E+%7D%7D&output=json".format(person, person)
print(query)
req = requests.get(query)
req_data = req.json()
# pprint(req_data)
data = req_data['results']['bindings']
# pprint(data)
for rec in data:
    extract_property(rec['property']['value'])
# import pdb; pdb.set_trace()