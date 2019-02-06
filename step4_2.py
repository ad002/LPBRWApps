#STEP IV.2
#We'll check the second function (get_close_matches) on its performance

import json

import difflib
from difflib import get_close_matches

#Let's load the same data again
data = json.load(open("dictionary.json"))

#Before we dive in, the basic template of this function is as follows:
#get_close_matches(word, posibilities, n=3, cutoff=0.66)

#First parameter: The word for wich you want to find closets matches
#Second parameter: A list of sequences against which to match the word
#[optional] Third is maximum number of close matches
#[optional] Where to stop considering a word a match (0.99 being the closest to
# word )

output = get_close_matches('rain', ['help', 'mate', 'rainy'], n=1, cutoff=0.75)
#So we check rain against help, mate and rainy, with max. 1 closest match with
#minimum 0.75 certainity

#Print out output, any guesses?
print(output)

#Output is: rainy
