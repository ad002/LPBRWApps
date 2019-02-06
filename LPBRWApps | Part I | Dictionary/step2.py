#STEP I
#Import the JSON Library and print out definition

#STEP II
#Wir erweitern die Funktion retrieve_definition um die Abfrage, ob das Wort
#überhaupt in dem Dictionary existiert und geben es nur dann aus, wenn
#es auch da ist

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

    #Das hier ist die Abfrage, ob es das Wort überhaupt gibt
    if word in [data]:
        #Wenn ja, spuck es aus
        return data[word]
    else:
        #Wenn nicht, sag ihm dass es nicht da ist und beende das Programm 
        return("Word doesn't exist, please double check it.")

#Input from user:
word_user = input("Enter a word to get definition: ")
print(retrieve_definition(word_user))
