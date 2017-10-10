# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:07:56 2017

@author: User
"""


str=raw_input("enter the string: ")
string=list(str)
for w in string:
    x=string.count(w)
    print "%c : %d" % (w,x)











