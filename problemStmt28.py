# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:47:55 2017

@author: User
"""

import re
def validate(a):
    x=True
    while x:
        if len(a)<6 and len(a)>12:
            break
        elif not re.search("[A-Z]",a):
            break
        elif not re.search("[a-z]",a):
            break
        elif not re.search("[0-9]",a):
            break
        elif not re.search("[$#@]",a):
                             break
        else:
            print "password is Valid"
            x=False
    return x
#    x=True
#    while x:
        
                     
            
            
def main():
    s=raw_input("enter the password: ")
    lst=s.split(',')
    a=lst[0]
    if validate(a):
        print "Password is incorrect"