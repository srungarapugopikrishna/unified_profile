import json
import requests
from pprint import pprint
from collections import defaultdict
import time

def extract_property(prop_type, property_value):
    # print(prop_type, property)
    property_val = None
    # if "http://www.w3.org/2000/01/rdf-schema#" in property:
    if "#" in property_value:
        property_index = property_value.find("#")+1
        property_val = property_value[property_index:]
    elif "http://dbpedia.org/ontology/" in property_value:
        property_val = property_value.replace("http://dbpedia.org/ontology/", "")

    elif "http://dbpedia.org/property/" in property_value:
        property_val = property_value.replace("http://dbpedia.org/property/", "")

    elif "http://xmlns.com/foaf/0.1/" in property_value:
        property_val = property_value.replace("http://xmlns.com/foaf/0.1/", "")

    elif "http://purl.org/dc/terms/" in property_value:
        property_val = property_value.replace("http://purl.org/dc/terms/", "")
    elif "http://wikidata.dbpedia.org/resource/" in property_value:
        property_val = property_value.replace("http://wikidata.dbpedia.org/resource/", "")
    # print(property_val)
    return property_val


data = []
with open('./dbpedia_data.json') as json_file:
    data = json.load(json_file)
    # import pdb; pdb.set_trace()
fin_result = []
i = 0
for rec in data[:1000]:
    # rec = data[23]
    i+=1
    print(i)
    try:
        final_result = defaultdict(list)
        person_uri = rec['person']
        person = person_uri.replace('http://dbpedia.org/resource/', '')
        query = "http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F%3E%0D%0APREFIX+dbpedia2%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fproperty%2F%3E%0D%0APREFIX+dbpedia%3A+%3Chttp%3A%2F%2Fdbpedia.org%2F%3E%0D%0APREFIX+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0D%0ASELECT+%3Fproperty+%3FhasValue+%3FisValueOf+WHERE+%7B%7B%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F{}%3E+%3Fproperty+%3FhasValue%7D+UNION+%7B%3FisValueOf+%3Fproperty+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F{}%3E+%7D%7D&output=json".format(person, person)
        req = requests.get(query)
        req_data = req.json()
        data = req_data['results']['bindings']
        for rec in data:
            try:
                prop = extract_property('Prop:', rec['property']['value'])
                if 'hasValue' in rec.keys():
                    val = extract_property('Value:', rec['hasValue']['value'])
                    ab = rec['hasValue']['value']
                elif 'isValueOf' in rec.keys():
                    val = extract_property('Value:', rec['isValueOf']['value'])
                    ab = rec['isValueOf']['value']
            except KeyError as e:
                print('Key error:', e, rec)
            final_result[prop].append(ab if val is None else val)
        fin_result.append(final_result)
        time.sleep(2)
    except Exception as e:
        print("Exception:::", e)
        json_object = json.dumps(fin_result)
        with open("dbpedia_to_mongo_1_1000.json", "w") as outfile:
            outfile.write(json_object)
        import pdb; pdb.set_trace()
    json_object = json.dumps(fin_result)
with open("dbpedia_to_mongo_success_1_1000.json", "w") as outfile:
    outfile.write(json_object)
import pdb;

pdb.set_trace()