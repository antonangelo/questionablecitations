#this processes the results from questionablecitations.py

import json
from pprint import pprint
import csv
import os



with open("results\Academic Research Reviews.json") as f:
    data = json.load(f)

#pprint(data)

print(data["search-results"]["opensearch:totalResults"])

entry = data["search-results"]["entry"]

#pprint(entry)
with open('results.csv', 'w', newline='') as csvfile:
    for filename in os.listdir(path="results/"):
        i = 0
        for value in entry:
            entryList = []
            entryList.append(filename)
            if "prism:doi" in  entry[i].keys():
                entryList.append(entry[i]["prism:doi"])
            if "dc:identifier" in  entry[i].keys():
                entryList.append(entry[i]["dc:identifier"])
            if "dc:title" in  entry[i].keys():
                entryList.append(entry[i]["dc:title"])
            if "dc:creator" in  entry[i].keys():
                entryList.append(entry[i]["dc:creator"])
            if "prism:publicationName" in  entry[i].keys():
                entryList.append(entry[i]["prism:publicationName"])
            if "prism:issn" in  entry[i].keys():
                entryList.append(entry[i]["prism:issn"])
            if "prism:volume" in  entry[i].keys():
                entryList.append(entry[i]["prism:volume"])
            if "prism:issueIdentifier" in  entry[i].keys():
                entryList.append(entry[i]["prism:issueIdentifier"])
            if "prism:pageRange" in  entry[i].keys():
                entryList.append(entry[i]["prism:pageRange"])
            if "prism:coverDate" in  entry[i].keys():
                entryList.append(entry[i]["prism:coverDate"])
            if "pubmed-id" in  entry[i].keys():
                entryList.append(entry[i]["pubmed-id"])
            if "prism:aggregationType" in  entry[i].keys():
                entryList.append(entry[i]["prism:aggregationType"])
            if "subtypeDescription" in  entry[i].keys():
                entryList.append(entry[i]["subtypeDescription"])
            if "openaccess" in  entry[i].keys():
                entryList.append(entry[i]["openaccess"])
            i = i + 1
            pprint(entryList)

            resultswriter = csv.writer(csvfile, delimiter='|')
            resultswriter.writerow(entryList)
csvfile.close()




