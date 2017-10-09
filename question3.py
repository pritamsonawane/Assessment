# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 11:32:12 2017

@author: User
"""
# List declaration
List1=[('x','y','z'),('a','b','c'),('p','q','r'),('e','f','g')]

def Keyvalue(i):
        return i[-1]#return last value of tuple
    
def sort(l):
     return sorted(l,key=Keyvalue)#return sorted list

print sort(List1)#function call




