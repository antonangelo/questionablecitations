#this processes the results from questionablecitations.py

import json, os, csv
from pprint import pprint

resultsdir ='results/'

#pprint(entry)
with open('results.csv', 'w', newline='', encoding="utf8") as csvfile:
    for filename in os.listdir(path=resultsdir):
        if "json" in filename:
            with open(resultsdir+filename) as f:
                try:
                    data = json.load(f)
                    entry = data["search-results"]["entry"]
                    #print("data loaded "+ filename)

                
                    citations = int(data["search-results"]["opensearch:totalResults"])
                    if citations > 0:
                        i = 0
                        for value in entry:
                            entryList = []
                            entryList.append(filename)
                            if "prism:doi" in  entry[i].keys():
                                entryList.append(entry[i]["prism:doi"])
                            else:
                                entryList.append("")

                            if "dc:identifier" in  entry[i].keys():
                                entryList.append(entry[i]["dc:identifier"])
                            else:
                                entryList.append("")
                            
                            if "dc:title" in  entry[i].keys():
                                entryList.append(entry[i]["dc:title"])
                            else:
                                entryList.append("")
                            
                            if "dc:creator" in  entry[i].keys():
                                entryList.append(entry[i]["dc:creator"])
                            else:
                                entryList.append("")
                            
                            if "prism:publicationName" in  entry[i].keys():
                                entryList.append(entry[i]["prism:publicationName"])
                            else:
                                entryList.append("")
                            
                            if "prism:issn" in  entry[i].keys():
                                entryList.append(entry[i]["prism:issn"])
                            else:
                                entryList.append("")
                            
                            if "prism:volume" in  entry[i].keys():
                                entryList.append(entry[i]["prism:volume"])
                            else:
                                entryList.append("")
                            
                            if "prism:issueIdentifier" in  entry[i].keys():
                                entryList.append(entry[i]["prism:issueIdentifier"])
                            else:
                                entryList.append("")
                            
                            if "prism:pageRange" in  entry[i].keys():
                                entryList.append(entry[i]["prism:pageRange"])
                            else:
                                entryList.append("")
                            
                            if "prism:coverDate" in  entry[i].keys():
                                entryList.append(entry[i]["prism:coverDate"])
                            else:
                                entryList.append("")
                            
                            if "pubmed-id" in  entry[i].keys():
                                entryList.append(entry[i]["pubmed-id"])
                            else:
                                entryList.append("")
                            
                            if "prism:aggregationType" in  entry[i].keys():
                                entryList.append(entry[i]["prism:aggregationType"])
                            else:
                                entryList.append("")
                            
                            if "subtypeDescription" in  entry[i].keys():
                                entryList.append(entry[i]["subtypeDescription"])
                            else:
                                entryList.append("")
                            
                            if "openaccess" in  entry[i].keys():
                                entryList.append(entry[i]["openaccess"])
                            else:
                                entryList.append("")
                            resultswriter = csv.writer(csvfile, delimiter='|')
                            resultswriter.writerow(entryList)
                            
                except Exception as e:
                    print("type error: "+ str(e)+ " in file: "+ filename)
                i = i + 1
                        # pprint(entryList)


csvfile.close()




