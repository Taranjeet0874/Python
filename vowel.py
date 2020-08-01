# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:18:45 2019

@author: DPM
"""

#def countvowels():      
string=input("enter the string:")
alpabets=digits=special=0
for i in range(len(string)):
    if(string[i].isalpha()):
        alpabets=alpabets+1
    elif(string[i].isdigit()) :
        digits=digits=1
    else:
        special=special+1
print("\n total no of special charachters in this string are:",special)        