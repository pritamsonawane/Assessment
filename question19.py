# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:45:57 2017

@author: User
"""

#Write a Program to Create a Class in which One Method Accepts a String from 
#the User and Another Prints it

class String:
    str=""
    def WriteStr(self):
        String.str=raw_input("enter the string: ")
    
    def read(self):
        print "string= "+ String.str


s1=String()
s1.WriteStr()
s1.read()