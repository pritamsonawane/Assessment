# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:44:37 2017

@author: User
"""

def DogAge():
    humAge=input("enter dog age in human years: ")
    if humAge <=2.0:
        print "dog age is 10.5 years"
    else:
        dogAge = float((humAge-2) * 4 +(10.5))
        print "dog age is %f years"% (dogAge)