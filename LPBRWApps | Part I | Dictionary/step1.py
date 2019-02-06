#STEP I
#Import the JSON Library
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
    return data[word]

word_user = input("Enter a word to get definition: ")
print(retrieve_definition(word_user))
