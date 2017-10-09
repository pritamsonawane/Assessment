# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:13:32 2017

@author: User
"""

def last(lst):
        return lst[-1]


def ListSort():
    lst =input("enter the elements of the list: ")
    print sorted(lst,key=last)
   