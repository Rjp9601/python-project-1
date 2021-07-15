import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def getdefns(word):
   if word.lower() in data:
        return data[word.lower()]
   elif word.upper() in data:
        return data[word.upper()]
   elif word.title() in data:
        return data[word.title()]
   elif len(get_close_matches(word, data.keys())) > 0 :
        q=input("Do you mean %s instead?\nEnter 'Y' for Yes and 'N' for No: " % get_close_matches(word, data.keys())[0])
        if q=='Y':
           return data[get_close_matches(word, data.keys())[0]]
        elif q=='N':
           return "Word doesn't exist."
        else:
           return "Invalid choice Entered.Try Again"
   else: 
           return "Word doesn't exist."

w=input("Enter your word: ")
defs= getdefns(w)
if type(defs)==list:
  for i in defs:
   print(i)
else:
   print(defs)
   