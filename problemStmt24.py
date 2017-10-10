# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:23:27 2017

@author: User
"""


str=raw_input("enter the string: ")
string=list(str)
result=[]
for w in string:
    if w.isdigit():
        result.append(w)

print result
