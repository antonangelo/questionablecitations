import re

regex = r"http://(.*?)[\"|/].*?blank\">(.*?)<.*?"

with open("originalData\\beallsListStandaloneJournals.html", "r") as originalHTML:
    data=originalHTML.read()
    #print(data)

matches = re.finditer(regex, data, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print(match.group(2)+"\t"+match.group(1))

