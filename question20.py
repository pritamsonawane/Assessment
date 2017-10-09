# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 19:25:49 2017

@author: User
"""
count=0
s="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
string=s.split(' ')
dict={}
for w in string:
    x=string.count(w)
    dict[w]=x

print dict