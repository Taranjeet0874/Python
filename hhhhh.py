# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:35:22 2019

@author: Dell
"""

# ZIP 
import pandas as pd
l=['Roll_no','Name','Math','science','statistics']
Roll_no=[1,2,3,4,5]
Name=["Taran","aman","ayush","aditya","saurabh"]
Math=[56,87,67,98,45]
Science=[67,87,56,98,78]
Statistics=[56,78,67,98,45]
a=list(zip(Roll_no,Name,Math,Science,Statistics))
df=pd.DataFrame(data=a,index=l)
print(df)
fp=open("sms.txt",'w')
fp.write(df)
fp.close()