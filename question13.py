# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 16:49:01 2017

@author: User
"""

def question13():
    num = int(input("enter the input: "))
    while num>1:
        if num%2 == 0:
            print num
            num=num/2  
        else:
            print num
            num =3* num +1
        
        
print question13()