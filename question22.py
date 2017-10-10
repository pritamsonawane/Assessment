# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:31:23 2017

@author: User
"""
countChr=0
countDgt=0
string=raw_input("enter the string: ")
for w in string:
    if w.isalpha():
        countChr +=1
    elif w.isdigit():
        countDgt +=1

print "Latters = %d"% (countChr)
print "Digits = %d" % (countDgt)