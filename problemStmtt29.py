# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:24:17 2017

@author: User
"""

balance = 0
while 1:
#    balance = 1
    ch = input("enter the input(1,2,3,4) 1: Deposit,2: Withdrawl,3: view balance,4: exit :")
    if ch==1:
        amount= input("enter amount to deposit: ")
        if amount < 0:
            print "invalid amount"
        else:
            balance = balance +amount
            print "balance= %f"%(balance)
    elif ch==2:
        amount = input("enter the amount to withdraw :")
        if amount > balance:
            print "not enough balance"
        else:
            balance = balance-amount
            print "balance= %f"%(balance)
    elif ch==3:
        print "balance= %f"%(balance)
    elif ch ==4:
        break

