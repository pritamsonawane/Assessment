# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:41:29 2017

@author: User
"""

result=[]
for x in range (1500,2700):
    if x%7==0 and x%5==0:
        result.append(x)

print result