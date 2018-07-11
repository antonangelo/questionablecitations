#this processes the results from questionablecitations.py

import json
from pprint import pprint

with open("results.json") as f:
    data = json.load(f)

pprint(data)


