# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:27:17 2017

@author: User
"""


emailId=raw_input("enter the email Id: ")
lst=emailId.split('@')
string=lst[1]
companyName=string.split('.')
print "company name = %s"% (companyName[0])
       
 
