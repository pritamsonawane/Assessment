# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 15:48:48 2017

@author: User
"""


s=(6, 6, 12, 18, 30,48)#input sequence
def AdditiveSeq(s):
    for i in range(len(s)-2):
        a=s[i]
        b=s[i+1]
        if (a+b)==s[i+2]:
            pass
        else:
            print "sequence is not additive"
            return False
    return True        
    
def check():
    if AdditiveSeq(s):
        print "sequence is additive"











