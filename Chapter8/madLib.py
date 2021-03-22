#!python3

#madLib.py - This script will ask the user for certain parts of speech and then fill them into a sentence to create a comedic sentnce.
#The script will display the sentence to the user and save it to a .txt file. 

import re, sys

# TODO: Set up the sentence
madLib = 'The ADJECTIVE panda walked to the NOUN and then VERB. A neadby NOUN was unaffected by these events'

madLibFile = open('madLib.txt', 'w')  #Open the file to save to. 




#TODO: Get the words from the user

adjective = input('Enter an Adjective:')
noun1 = input('Enter a Noun:')
verb = input('Enter a Verb:')
noun2 = input('Enter another Noun:')


#TODO: Add in user words


#TODO: Output to screen and save to .txt file