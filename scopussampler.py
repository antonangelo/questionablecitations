from apikey import apikey
import json, requests, urllib, os, csv, random

def search(query):
    try:
        fullurl = 'https://api.elsevier.com/content/search/scopus?query=refsrctitle("'+query+'")' 
        articles = requests.get(fullurl,headers={'Accept':'application/json','X-ELS-APIKey':apikey})
        json = articles.json()
        entry = json["search-results"]["entry"]
        citations = int(json["search-results"]["opensearch:totalResults"])
    except Exception as e:
        errortext = "type error: "+ str(e)+ " in journal: "+ query
        citations = errortext
    return citations



resultsdir = "results/"
journallist ="originalData\ext_list_April_2018_2017_Metrics.txt" #full list, or test list.
sample=sorted(random.sample(range(1,37000),1000))
sampleresultsoutput = "scopuscitationsample.txt"

with open(sampleresultsoutput, 'w', newline='', encoding="utf8") as sampleresultsfile:
    resultswriter = csv.writer(sampleresultsfile, delimiter='\t')

    with open(journallist, 'r', newline='', encoding="utf8", ) as csvfile:
        journals = csv.reader(csvfile, delimiter="\t")
        i = 0
        j = 0
        for row in journals:
            i=i+1
            if i == sample[j]:
                entrylist=[]
                #print(i, j, " ",row[1])
                entrylist.append(row[1])
                entrylist.append(search(row[1]))
                j = j+1
                resultswriter.writerow(entrylist)

sampleresultsfile.close()

