# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:36:20 2019

@author: DPM
"""
def countupperandlowercase():
    sentence=input("enter the sentence:")
    upper=0
    lower=0
    for i in sentence:
        if(i>="A" and i<="Z"):
            upper=upper+1
        if(i>="a" and i<="z"): 
            lower=lower+1
    print("upper case:",upper)  
    print("lower case:",lower)
countupperandlowercase()   
sentence=input("enter the sentence:")
string=sentence.lower()
print(string)
count=0
list=['a','e','i','o','u']
for char in string:
    if char in list:
        count=count+1
print("number of vowels in given sentence is:",count)        