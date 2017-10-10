# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:43:58 2017

@author: User
"""

tpl1=(1,2,3,4,5,6,7,8,9,10)
a=[]
for x in tpl1:
    if x%2==0:
        a.append(x)
result=tuple(a)
print result