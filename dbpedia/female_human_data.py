import requests
url = 'https://query.wikidata.org/sparql'
query = """
SELECT ?human ?given_name ?given_nameLabel
WHERE
{
	?human wdt:P31 wd:Q5 .       #find humans
    ?human wdt:P21 wd:Q6581072 .
    ?human wdt:P735 ?given_name .
	SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
} limit 100000
"""

# query = """DESCRIBE <https://www.wikidata.org/wiki/Q42>"""
req = requests.get(url, params={'format': 'json', 'query': query})
# data = r.json()
# from pprint import pprint
# pprint(data)
f = open("testsuc.txt", "w+")
f.write(str(vars(req)))
f.close()
print('Entering to pdb::::')
import pdb; pdb.set_trace()


