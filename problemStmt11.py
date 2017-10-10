# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:13:06 2017

@author: User
"""


str="";    
for r in range(0,7):    
    for c in range(0,7):     
        if (((c == 0 or c == 6 ) and r != 0) or ((r == 3 or r==2 or r==6) and (c < 3 and c > 3)) or (r==4) and (c==3)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n" 

print str