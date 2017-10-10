# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:09:24 2017

@author: User
"""
# list comprehension

lst=[12,24,35,70,88,120,155]
result=[]
result=[lst[x] for x in range(0,len(lst)) if x%2==0]
print result





