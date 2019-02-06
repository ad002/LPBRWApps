
import json
import difflib
from difflib import get_close_matches

#JSON or JavaScript Object Notationm is a minimal, readable (for both humans
# and computers) format for structuring data. It mainly has two things, a
#key and a value associated with the key.

#The important thing here: We'll load the data in json Format, but it will be
#stored in the 'data' variable as python dictionary data format.

#Loading the json data as python dictionary
#Try typing 'type(data)' in terminal after executing the first two lines
#of this snippet
data=json.load(open('dictionary.json'))

#print(type(data))
#out: <class 'dict'>

#Function for retrieving definition
def retrieve_definition(word):
    #Alle Wörter erstmal in LowerCase, weil unsere Daten in dem Format sind
    word = word.lower()

    #Abfrage, ob das Wort existiert

#Check for non existing words
#1st elif: To make sure program return the definitions of words that start with
#a capital letter like (Delhi, Texas etc.)

#2nd elif: To make sure program return the words with capital letters (USA, NASA)

#Wenn das wort vorkommt
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

#3rd elif: To find a similar word
#-- len > 0 because we can print only whe the word has 1 or more close matches
#-- in the return statement, the last [0] represents the first element from
#the list of close matches!

    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " %get_close_matches(word, data.keys())[0])

        if (action == "y"):
            return data[get_close_matches(word,data.keys())[0]]
        elif (action == "n"):
            return("Word doesn't exist, yet.")


    else:
        return("We don't understand your entries. Sorry")


word_user = input("Enter a word to get definition: ")

#retrieve the definition using function and print the result
output = retrieve_definition(word_user)

#If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-",item)
    #For words having single definition
else:
    print("-", output)
