# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:41:18 2017

@author: User
"""

#.Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area. 
import math
class Circle:
    Area=0
    def __init__(self,radius):
        self.radius=radius
        
    def circleArea(self):
        Circle.Area = math.pi * self.radius **2
        print "area of the circle is %f" %(Circle.Area)
        


c1=Circle(12)
c1.circleArea()