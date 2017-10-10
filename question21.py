# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:21:47 2017

@author: User
"""

#Write a Program to Read the Contents of a File in Reverse Order

read=open("pks.txt",'r')
a=[]
def rev():
    for x in read:
        a.append(x)
         



def readRev():
    rev()
    for line in a[::-1]:
        print line
    
    
