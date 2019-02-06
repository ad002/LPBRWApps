#STEP I
#Import the JSON Library and print out definition

#STEP II
#Wir erweitern die Funktion retrieve_definition um die Abfrage, ob das Wort
#überhaupt in dem Dictionary existiert und geben es nur dann aus, wenn
#es auch da ist

#STEP III
#Wir erweitern die Funktion so, dass Nutzer 'Rain' oder 'rain' eingeben und
#trotzdem den gleichen output bekommen, using lower()
#Nutzer können jetzt also schreiben, wie sie wollen, also z.B
#'football', 'Football' oder 'FOOTBALL' eingeben und kriegen trd die passende
#definition ausgegeben, sofern sie denn existiert ('else') und der Input
#keinen Tippfehler enthält

import json

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
    if word in [data]:
        return data[word]

    #Aus dem kleingeschriebenen fragen wir jetzt ab, ob es im Datensatz das
    #Wort mit großem Anfangsbuchstaben gibt. Also z.B. Delhi oder Texas.
    #Wenn ja, geben wir die Definition des Worts aus.
    elif word.title() in data:
        return data[word.title()]

    #Jetzt transformieren wir das LowerCase Wort in UPPERCASE (komplett) und
    #prüfen, ob es dieses WORT im Datensatz gibt, um auch Akronyme wie USA, NATO
    #mit einzubeziehen. Wenn ja, geben wir die Definition des WORTS aus.
    elif word.upper() in data:
        return data[word.upper()]

    else:
        return("Word doesn't exist, please double check it.")

#Input from user:
word_user = input("Enter a word to get definition: ")
print(retrieve_definition(word_user))
