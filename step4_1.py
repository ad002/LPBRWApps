#STEP IV.1
#Falls man sich einen Tippfehler erlaubt, also z.B. 'mediium' anstatt 'medium'
#eintippt, soll das dictionary den 'closest match', also das Wort, das der
#Eingabe am nähesten kommt, nachschlagen. Dafür benutzen wir die SequenceMatcher
#Funktion, die 3 Parameter als Input nimmt: junk (if the word has blank spaces
# or white lines), in our case that's none. Second and third parameters are
#the words between which you want to find similarities. And append ratio method
#will give you the result in the number.

#Dafür checken wir 2 Funktionen. In diesem Schritt die Funktion SequenceMatcher,
#im nächsten (IV.2) eine andere und vergleichen dann die Perfomance
import json

import difflib
from difflib import SequenceMatcher
#This is a python library for 'Text Processing Services'


#JSON or JavaScript Object Notation is a minimal, readable (for both humans
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


#Run a Sequence Matcher
#First Parameter: Blank spaces
#Second and third: Words you want to find similarities in between
#Ratio is used to find how close two words are in numerical terms
value = SequenceMatcher(None, 'rainn', 'rain').ratio()
print(value)
#0.88888888

value= SequenceMatcher(None, 'lofe', 'love').ratio()
print(value)
#0.75

value= SequenceMatcher(None, 'hallo', 'gelo').ratio()
print(value)
#0.44444444
