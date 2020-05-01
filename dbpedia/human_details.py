import requests

url = 'https://query.wikidata.org/sparql'
query = """
SELECT ?human ?ethnic_group ?ethnic_groupLabel ?given_name ?given_nameLabel ?family_name ?family_nameLabel WHERE {
  ?human wdt:P31 wd:Q5;
  ?human wdt:P21 wd:Q6581072 .
  #   wdt:P172 ?ethnic_group;
  #   wdt:P735 ?given_name.
  # ?human wdt:P734 ?family_name.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""
query = """
SELECT ?human WHERE {
  ?human wdt:P31 wd:Q5 .
  ?human wdt:P21 wd:Q6581072 .
      wdt:P172 ?ethnic_group;
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
}
"""
query = """
SELECT ?human ?gender ?genderLabel ?ethnic_group ?ethnic_groupLabel ?given_name ?given_nameLabel ?family_name ?family_nameLabel WHERE {
  ?human wdt:P31 wd:Q5;
    wdt:P21 ?gender;
    wdt:P172 ?ethnic_group;
    wdt:P735 ?given_name.
  ?human wdt:P734 ?family_name.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],fr,ar,be,bg,bn,ca,cs,da,de,el,en,es,et,fa,fi,he,hi,hu,hy,id,it,ja,jv,ko,nb,nl,eo,pa,pl,pt,ro,ru,sh,sk,sr,sv,sw,te,th,tr,uk,yue,vec,vi,zh". }
}
"""

q="""
#Humans with given name, family name, gender, and ethnic group
#Contributed on 22nd October, 2019 by Shubhanshu Mishra (https://shubhanshu.com)
#Given name, Surname with gender, ethnic_group in any language label
SELECT ?human ?name ?nameLabel WHERE {
  ?human wdt:P31 wd:Q5 .
  ?name wdt:P735 ?given_name;
        rdfs:label ?nameLabel.
         FILTER(LANG(?nameLabel) = "en").
         FILTER(STRSTARTS(?nameLabel, "Aa")).
  ?gender wdt:P21 wd:Q6581072 .
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
} LIMIT 10
"""
# query = """DESCRIBE <https://www.wikidata.org/wiki/Q42>"""
req = requests.get(url, params={'format': 'json', 'query': query})

data = req.json()
# from pprint import pprint
# pprint(data)
print('Entering to pdb::::', req)
import pdb;

pdb.set_trace()
