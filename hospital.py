# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:52:24 2019

@author: Dell
"""


fp=open("hospital.txt",'w')

fp.write("name")
fp.write("   \t")
fp.write("viplav")
fp.write("   \t")
fp.write("akash")
fp.write("   \t")
fp.write("taranjeet")
fp.write("   \n")

fp.close()

fp=open("hospital.txt",'a')

fp.write("abc")
fp.write("   \t")
fp.write("vip")
fp.write("   \t")
fp.write("akas")
fp.write("   \t")
fp.write("taranje")
fp.write("   \n")
fp.close()

fp=open("hospital.txt",'r')
flag=index=0
search=str((input("enter to ")))
for line in fp:
    a=line.strip().split()
    if search in a:
        flag=1
        
    index=index+1
fp.close()
        
if(flag==1):
    print("word found at line{}".format(index))
    
    
fp=open("hospital.txt",'r')   
 
for line in fp:
    print(line)
     
fp.close()



