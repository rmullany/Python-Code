# Program to get a definition of a word from data.json
# by Ruth Mullany
#
# This program is based on Application-1
# from Udemy:The Python Mega Course: Build 10 Real World Applications
# by Ardit Suice
#
# Changes to the program is to capture the word to be translated
# The correct word is passed in the 1st position (index [0]) of the translate function
# The word is repeated back and print as part of the result in a structure manner
#
import json
from difflib import get_close_matches
#
data = json.load(open("data.json"))
#
def translate(word):
    if word in data:
        cword = word
        return cword,data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        ans = input ("Did you mean %s? (y/n)" %get_close_matches(word,data.keys())[0])
        ans = str.lower(ans)
        if ans == "y":
            cword = get_close_matches(word,data.keys())[0]
            return cword,data[get_close_matches(word,data.keys())[0]]
        else:
            cword = ""
            return (cword,"Sorry, please try again.")
    else:
        cword = ""
        return (cword,"Word do not exist, please try again")
#
word = input("Please input a word requiring definition ")
#
result = (translate(str.lower(word)))
cword = result[0]
definition = result[1]
#
if result[0] != "":
    print ("\n","Definition for: ",cword,"\n")
    count = 0
    for item in definition:
        count = count + 1
        print (count,". ",item,"\n")
else:
    print (definition)
