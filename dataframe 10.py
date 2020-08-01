import pandas as pd
import numpy as np
roll_no=[1,2,3,4]
sub=['sub1','sub2','sub3']
s=[56,78,45,78,78,45,54,34,56,54,39,67]
a=np.array(s)
a.resize(4,3)
df=pd.DataFrame(data=a,index=['Ex_1','Ex_2','Ex_3','Ex_4'],columns=['MATH','STATS','SCIENCE'])

su=df.sum(axis=1)

df['Total']=su
print("*****************************************************************************")


#df['RM']=df['MATH'].rank()
#df['RMmax']=df['MATH'].rank(method='max')
df['RMmin']=df['MATH'].rank(method='min')
df['RMd']=df['MATH'].rank(method='dense')

df['RST']=df['STATS'].rank()
#df['RSTmax']=df['STATS'].rank(method='max')
df['RSTmin']=df['STATS'].rank(method='min')
df['RSTd']=df['STATS'].rank(method='dense')

df['RS']=df['SCIENCE'].rank()
#df['RSmax']=df['SCIENCE'].rank(method='max')
df['RSmin']=df['SCIENCE'].rank(method='min')
df['RSd']=df['SCIENCE'].rank(method='dense')

df['RT']=df['Total'].rank()
#df['RTmax']=df['Total'].rank(method='max')
#df['RTd']=df['Total'].rank(method='dense')

print(df)
print("***************************************************************************")


