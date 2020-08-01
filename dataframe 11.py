import pandas as pd
import numpy as np
roll_no=[1,2,3,4]
sub=['sub1','sub2','sub3']
s=[56,78,45,78,78,45,54,34,6,4,9,1]
a=np.array(s)
a.resize(4,3)
df1=pd.DataFrame(data=a,index=['0','1','2','3'],columns=['A','B','C'])
print(df1)
print("**********************************************************")
k=[4,6,7,2,6,4,9,1]
b=np.array(k)
b.resize(4,2)
df2=pd.DataFrame(data=b,index=['4','5','6','7'],columns=['C','D'])
print(df2)
print("**********************************************************")
df3=pd.merge(df1,df2,on='C',how='outer')
df4=pd.merge(df1,df2,on='C',how='inner')
#df3=pd.concat([df1,df2])
print(df3)
print(df4)
print("**********************************************************")


