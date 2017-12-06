# dictionary.py

import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

def trans(word):
    word = word.lower()
    key = get_close_matches(word, data.keys())
    if word in data:
        return data[word]

    elif word.title() in data: #If user inputs "texas" it will check for "Texas"
        return data[word.title()]

    elif len(key) > 0:
        new =  input("Did you mean %s instead? y/n: " % key[0])
        if new == "y":
            return data[key[0]]
        elif new == "n":
            return "That word isn't in this dictionary. Please double check the spelling."
        else:
            return "We didn't understand your entry."


    else:
        return "That word isn't in this dictionary. Please double check the spelling."

word = input("Enter a word to define: ")
output = trans(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
