#this processes the results from questionablecitations.py

import json
from pprint import pprint

with open("results\Academic Research Reviews.json") as f:
    data = json.load(f)

#pprint(data)

print(data["search-results"]["opensearch:totalResults"])

entry = data["search-results"]["entry"]

#pprint(entry)

i = 0
for value in entry:
    doi = entry[i]["prism:doi"]
    identifier = entry[i]["dc:identifier"]
    title = entry[i]["dc:title"]
    creator = entry[i]["dc:creator"]
    publicationName = entry[i]["prism:publicationName"]
    issn = entry[i]["prism:issn"]
    volume = entry[i]["prism:volume"]
    issue = entry[i]["prism:issueIdentifier"]
    pageRange = entry[i]["prism:pageRange"]
    coverDate = entry[i]["prism:coverDate"]
    citedByCount = entry[i]["citedby-count"]
    i = i + 1


