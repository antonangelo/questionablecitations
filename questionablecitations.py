#from apikey import apikey
import json, requests, urllib, os

resultsdir = 'results/'
journallist = 'journals.txt' #full list, or test list.
apikey='1057dc2c133aea3f1a32a48359b412a8'
'''
A function which runs a search query in SCOPUS. Request number is
set to 200. Start can be adjusted if there are more records
'''
def search(query):
    fullurl = 'https://api.elsevier.com/content/search/scopus?query=refsrctitle("'+query+'")' 
    articles = requests.get(fullurl,headers={'Accept':'application/json','X-ELS-APIKey':apikey})
    json = articles.json()
    return json


'''
A function that opens a file, writes results to it, and then closes it
'''
def results(filename, string):

    f = open(resultsdir+filename+".json", "a", encoding="utf8")
    f.write(json.dumps(string))
    f.close


j = open(journallist, "r", encoding="utf8")

#make sure there is a place for results to live

try:
    os.stat(resultsdir)
except:
    os.mkdir(resultsdir)

for line in j:
    journalname = line.rstrip()
    print("Journal: ",journalname)
    codedjournalname = urllib.parse.quote(journalname)
    print(codedjournalname)
    resultJson = search(codedjournalname)
    results(journalname, resultJson)

j.close
