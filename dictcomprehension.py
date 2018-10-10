#!/usr/bin/python 

from string import ascii_lowercase 

lettermap=dict((c,k) for k,c in enumerate(ascii_lowercase,1))

print(lettermap)

""" 1 in the forloop for starting the iteration from 1 instead of 0 
       as we're checking alphabets here """
