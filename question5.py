# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:55:13 2017

@author: User
"""
result=[]

inputList = input("enter the value in list: ")
x=1
for i in inputList:
    if(i==x):
        x=x+1
    else:
        result.append(x)
        x=x+1

print "missing number ="+ str(result)
        