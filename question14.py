# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:21:37 2017

@author: User
"""


def isPowerOf2(num):
    flag = 0
    tempNum = num
    while(tempNum!=1):
        if(tempNum%2!=0):
            flag=1
            return flag
            break
        tempNum=tempNum/2
    return flag
    
    
def check():
    num = int(input("enter the value: "))
    if isPowerOf2(num):
        print "number is not power of 2"
    else:
        print "number is power of 2"
    















#      

   
    
    

