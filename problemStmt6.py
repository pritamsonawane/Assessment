# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:49:44 2017

@author: User
"""
    

str="";    
for r in range(0,7):    
    for c in range(0,7):     
        if ((c==1 or c==5) and (r>0 and r<7))and((r==1 or r==4) and (c>1 and c<5)):
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n" 
    
    
    
print(str);



  
(r>1 and r<7)