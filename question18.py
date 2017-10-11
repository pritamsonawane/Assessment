# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:51:52 2017

@author: User
"""

#Write a Program to Append, Delete and Display Elements of a List Using Classes


class List:
    
    def __init__(self):
        self.lst=[]
    
    def append(self,element):
        self.lst.append(element)
    
    def delete(self,element):
        self.lst.remove(element)
    
    def Display(self):
        for x in self.lst:
            print x,
        
        


l1=List()# instance is created
# calling append function
l1.append(12)
l1.append(24)

l1.append(11)
l1.append(34)
l1.append(224)
l1.append(14)
l1.append(64)        
#calling display function
l1.Display()
#calling delete function
l1.delete(224)