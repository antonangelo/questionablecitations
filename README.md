# questionablecitations

A set of tools to query scopus to look for articles that cite articles in journals included in Beall's List.

Add a file apikey.pi with the following line, including an Elsevier API key from [https://dev.elsevier.com/user/login]

```python
apikey=YOURAPIKEY
```

The list of Beall's predatory journals was taken from [https://beallslist.weebly.com/standalone-journals.html]

Two programs, 

- questionablecitations.py gathers citations and writes them into json files
- resultsprocessor.py reads the above json files and puts them into a csv ready to import into ... R?  Open Refine?  This is less developed.  By less developed, I mean broken (so far)

