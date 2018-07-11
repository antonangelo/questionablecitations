from apikey import apikey
import json, requests, urllib

'''
A function which runs a search query in SCOPUS. Request number is
set to 100. Start can be adjusted if there are more records
'''
def search(query,start):    
    articles = requests.get("http://api.elsevier.com/content/search/index:SCOPUS?query=" + query + '&count=100' + '&start=' + str(start),headers={'Accept':'application/json','X-ELS-APIKey':apikey})
    json = articles.json()
    return json


'''
A function that opens a file, writes results to it, and then closes it
'''
def results(string):
    f = open("results.json", "a", encoding="utf8")
    f.write(json.dumps(string))
    f.close

j = open("testjournals.txt", "r", encoding="utf8")


for line in j:
    print(line)
    journal =urllib.parse.quote(line)
    print(journal)
    searchtext ="refsrctitle("+journal+")"
    print(searchtext)
    resultJson = search(searchtext,"1")
    results(resultJson)
j.close
