# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:36:26 2017

@author: User
"""


try:
    x =int(input("enter the value: "))
    ans = 200/x
    print "ans is %d" % ans
except ZeroDivisionError :
    print "x should not be zero(runtime error)"
except ValueError:
    print "x is not a number"