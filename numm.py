

import numpy as np

l1=[]

n=int(input("enter number of element you want to enter"))

for i in range(0,n):
        l1.append(int(input("enter the value")))

c=np.array(l1)
e=np.array(l1)
print(c)
print("dimension=",c.ndim)
print("Shape=",c.shape)

#reshaping  and dimension changing
dimension=int(input("enter dimension in which you want to reshape it"))
l4=[]
print("enter shape")
for i in range(0,dimension):
    l4.append(int(input()))

d=len(l4)
a=1
for i in range(0,d):
    a=a*l4[i]
if(a==n):
    if(dimension==1):
        c.resize(l4[0])
        print(c)
    elif(dimension==2):
        c.resize(l4[0],l4[1])
        print(c)
    elif(dimension==3):
        c.resize(l4[0],l4[1],l4[2])
        print(c)
    elif(dimension==4):
        c.resize(l4[0],l4[1],l4[2],l4[3])
        print(c)
    else:
        print("print this program is only for up to dimension 4")

else:
    print("reshaping not possible")


print("dimension=",c.ndim)
print("Shape=",c.shape)


#for finding string which carry "0"
l3=[]
for i in range (0,n):

    t=str(e[i])
    m=len(t)

    for j in range(0,m):
        if(t[j]=="0"):
            l3.append(e[i])
            break
w=np.array(l3)
print("the array of number carrying 0 is{}".format(w))



#for finding repetitive value
l3=[]
for i in range (0,n):

    
    for j in range(i+1,n):
        
        
        if(e[j]==e[i]):
            count=0
            a=len(l3)
            for k in range(0,a):
                if(l3[k]==e[i]):
                    count=1
                    break
        
            if(count==0):
                l3.append(e[i])
                
w=np.array(l3)
print("the array of repetitive value are are{}".format(w))

#for replacing odd value with 0
for i in range(0,n):
    if((e[i]%2)!=0):
        e[i]=0
print(e)





    
    




