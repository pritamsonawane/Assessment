# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:52:01 2017

@author: User
"""


str="";    
for r in range(0,7):    
    for c in range(0,7):     
        if ((c == 1 and r != 0 and r != 6) or ((r == 0 or r == 6) and c > 1 and c < 5) or (r == 3 and c > 2 and c < 6) or (c == 5 and r != 0 and r != 2 and r != 6)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n" 

print str




