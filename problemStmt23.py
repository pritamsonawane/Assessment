# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:45:59 2017

@author: User
"""

lst=[121,23,1,34,93,45,53,45,34,3]
lst=sorted(lst)


def search(lst):
    value=input("enter the value :")
    lower = 0
    upper = len(lst)
    
    while lower < upper:
        x = lower + (upper - lower) // 2
        a = lst[x]
        if value == a:
            print "value is found index no is %d"% x
            break
        elif value > a:
            if lower == x:   
                break        
            lower = x
        elif value < a:
            upper = x
    


search(lst)