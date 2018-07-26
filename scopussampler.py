from apikey import apikey
import json, requests, urllib, os, csv

def search(query):
    try:
        fullurl = 'https://api.elsevier.com/content/search/scopus?query=refsrctitle("'+query+'")' 
        articles = requests.get(fullurl,headers={'Accept':'application/json','X-ELS-APIKey':apikey})
        json = articles.json()
        entry = json["search-results"]["entry"]
        citations = int(json["search-results"]["opensearch:totalResults"])
    except Exception as e:
        print("type error: "+ str(e)+ " in journal: "+ query)
        citations = "error"
    return citations



resultsdir = "results/"
journallist ="originalData\ext_list_April_2018_2017_Metrics_test.txt" #full list, or test list.

with open(journallist, 'r', newline='', encoding="utf8", ) as csvfile:
    journals = csv.reader(csvfile, delimiter="\t")
    for row in journals:
        print(row[1])
        print(search(row[1]))
