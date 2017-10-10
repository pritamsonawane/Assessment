# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:17:45 2017

@author: User
"""

a=[12,24,35,24,88,120,155,88,120,155]
result=[]
for x in reversed(a):
    if x in result:
        pass
    else:
        result.append(x)

print result

