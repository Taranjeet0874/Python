# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:52:58 2019

@author: Dell
"""
a=int(input("enter rows"))
for i in range(1,a+1):
    print(" "*(a-i)+"* "*i+" "*(2*a-2*i)+"* "*(i-1))
for i in range(a-1,0,-1):
    print(" "*(a-i)+"* "*i+" "*(2*a-2*i)+"* "*(i-1))    
    