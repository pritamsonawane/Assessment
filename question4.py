# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:28:14 2017

@author: User
"""

def sumOfDigits():
    s=0
    num =input("enter the value: ")
    while num >0:
        digit=num%10
        s=s+digit
        num=num/10
    print s
    
    