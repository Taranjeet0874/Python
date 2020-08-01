import pandas as pd
from matplotlib import pyplot as pt
import numpy as np
sum=0
k=[0,1,2,3]
roll_no=[1,2,3,4]
sub=['s1','s2','s3','s4']
s=[56,78,65,78,98,45,54,34,56,87,56,76]
a=np.array(s)
a.resize(4,3)
df=pd.DataFrame(data=a,index=['r1','r2','r3','r4'],columns=['s1','s2','s3'])
print(df)

# 1 PROJECT A GIVEN STUDENT PERFORMANCE
a=int(input(" Enter the roll no of student [0-r1,1-r2,2-r3,3-r4]"))
p=df.iloc[a,:]
print(p)

# 2 VISUALISE PERFORMANCE OF STUDENT IN EACH SUBJECT

s=int(input(" Enter the subject [0-s1,1-s2,2-s3]"))
d=df.iloc[:,s]
pt.bar(roll_no,d)
pt.show()

 #3 AVERAGE ATTENDANCE OF STUDENTS IN ALL SUBJECTS
j=int(input(" Input the subject [0-s1,1-s2,2-s3] "))
for i in range(0,4):
    v=df.iloc[i,j]
    sum=sum+v
average=sum/4
print("average=",average)

#4 TOP 2 STUDENTS
h=int(input(" Input the subject [0-s1,1-s2,2-s3] "))
jk=[]
for i in range(4):
        f=df.iloc[i,h]
        jk.append(f)
jk.sort()
print(jk)
print("first",jk[3])
print("second",jk[2])       


