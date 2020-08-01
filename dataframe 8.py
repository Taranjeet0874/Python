import pandas as pd
import numpy as np

s=[56,78,65,78,98,45,54,34,56,87,67,54,89,76,43,78,78,56,76,54,34,66,88,99,22,33,66,34,56,78,90,12]
a=np.array(s)
a.resize(4,8)
df=pd.DataFrame(data=a,index=[['g1','g1','g2','g2'],['r1','r2','r3','r4']],
                columns=[['s1','s1','s1','s2','s2','s3','s3','s3'],['L','P','T','L','P','L','P','T']])
print(df)

#operation1 project given stua-dent performance
# 1 PROJECT A GIVEN STUDENT PERFORMANCE
a=int(input(" Enter the roll no of student [0-r1,1-r2,2-r3,3-r4]"))
p=df.iloc[a,:]
print(p)
# 2 VISUALISE PERFORMANCE OF STUDENT IN EACH SUBJECT
roll_no=[1,2,3,4]

s=int(input(" Enter the subject [0-s1,1-s2,2-s3]"))
d=df.iloc[:,s]
pt.bar(roll_no,d)
pt.show()


