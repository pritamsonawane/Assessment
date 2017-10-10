# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:19:25 2017

@author: User
"""

import itertools
a=[1,2,3]

result=itertools.permutations(a)
print "permutation combinations of [1,2,3] are as follows:"
for lst in result:
    print lst