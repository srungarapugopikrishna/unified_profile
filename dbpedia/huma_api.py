import requests
url = 'http://dbpedia.org/snorql'
query = """
SELECT ?person WHERE {
?person dbo:birthPlace :Berlin .
?person dbo:birthDate ?birth .
?person foaf:name ?name . 
?person dbo:deathDate ?death .}
"""
query_prefix = """?default-graph-uri=http://dbpedia.org&"""
query_prefix += """PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX : <http://dbpedia.org/resource/>
PREFIX dbpedia2: <http://dbpedia.org/property/>
PREFIX dbpedia: <http://dbpedia.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""
query = """PREFIX+owl:+<http://www.w3.org/2002/07/owl#>
PREFIX+xsd:+<http://www.w3.org/2001/XMLSchema#>
PREFIX+rdfs:+<http://www.w3.org/2000/01/rdf-schema#>
PREFIX+rdf:+<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX+foaf:+<http://xmlns.com/foaf/0.1/>
PREFIX+dc:+<http://purl.org/dc/elements/1.1/>
PREFIX+:+<http://dbpedia.org/resource/>
PREFIX+dbpedia2:+<http://dbpedia.org/property/>
PREFIX+dbpedia:+<http://dbpedia.org/>
PREFIX+skos:+<http://www.w3.org/2004/02/skos/core#>
SELECT+?name+?person+WHERE+{?person+a+dbo:Person+.+?person+foaf:name+?name+.}"""
# req = requests.get(url, params={'default-graph-uri': 'http://dbpedia.org', 'output': 'json', 'query': query})
req= requests.get("http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F%3E%0D%0APREFIX+dbpedia2%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fproperty%2F%3E%0D%0APREFIX+dbpedia%3A+%3Chttp%3A%2F%2Fdbpedia.org%2F%3E%0D%0APREFIX+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0D%0ASELECT+%3Fname+%3Fperson+WHERE+%7B%3Fperson+a+dbo%3APerson+.+%3Fperson+foaf%3Aname+%3Fname+.%7D&output=json")
req = req.json()
from pprint import pprint
print(req)
import pdb; pdb.set_trace()
