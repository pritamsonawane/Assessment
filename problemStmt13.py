# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:57:44 2017

@author: User
"""

vowel=['A','E','I','O','U']

def checkAlpha():
    alphabet =raw_input("enter the character: ")
    if alphabet.upper() in vowel:
        print "%c is a vowel" % (alphabet)
    else:
        print "%c is consonant" % (alphabet)