# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 13:07:24 2017

@author: User
"""
# find user name from Email Id
def userName():
    EmailId = raw_input("enter your Email id: ")
    x=EmailId.split('@')
    UserName = x[0]
    print "UserName is %s"%(UserName)
    