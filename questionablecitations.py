from apikey import apikey
import json, requests, urllib, time

'''
A function which runs a search query in SCOPUS. Request number is
set to 200. Start can be adjusted if there are more records
'''
def search(query,start):    
    articles = requests.get("http://api.elsevier.com/content/search/index:SCOPUS?query=" + query + '&count=200' + '&start=' + str(start),headers={'Accept':'application/json','X-ELS-APIKey':apikey})
    json = articles.json()
    return json


'''
A function that opens a file, writes results to it, and then closes it
'''
def results(filename, string):
    filename = "results/"+filename+".json"
    f = open(filename, "a", encoding="utf8")
    print("Writing to: "+filename )
    f.write(json.dumps(string))
    f.close

j = open("journals.txt", "r", encoding="utf8")


for line in j:
    journalname = line.rstrip()
    print("searching "+journalname)
    journal = urllib.parse.quote('"'+journalname+'"')
#    print(journal)
    searchtext ="refsrctitle("+journal+")"
#    print(searchtext)
    resultJson = search(searchtext,"1")
    results(journalname, resultJson)
    time.sleep(10)
j.close
