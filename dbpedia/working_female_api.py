import requests
url = 'https://query.wikidata.org/sparql'
query = """
SELECT ?human
WHERE
{
	?human wdt:P31 wd:Q5 .       #find humans
    ?human wdt:P21 wd:Q6581072 .
	SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
}
"""

# query = """DESCRIBE <https://www.wikidata.org/wiki/Q42>"""
r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
# from pprint import pprint
# pprint(data)
print('Entering to pdb::::')
import pdb; pdb.set_trace()


