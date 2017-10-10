# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:37:17 2017

@author: User
"""

str="";    
for r in range(0,7):    
    for c in range(0,7):     
        if (c == 1 or ((r == 0 or r == 6) and (c > 1 and c < 5)) or (c == 5 and r != 0 and r != 6)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n" 
    
    
    
print(str);