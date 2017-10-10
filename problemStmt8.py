# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:46:49 2017

@author: User
"""

str="";    
for r in range(0,7):    
    for c in range(0,7):     
        if (((c == 1 ) and r != 0) or ((r == 0 or r == 3 or r==6) and (c > 0 and c < 5))):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n" 

print str