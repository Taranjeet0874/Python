# DATA FRAME USING SERIES
import pandas as pd
l1=[1,2,3,4,5]
l2=[4,6,4,3,1]
l3=[4,2,3,4,7]
l4=[3,7,9,7,6]
l5=[2,6,4,5,3]
s=list(zip(l1,l2,l3,l4,l5))
i=['x1','x2','x3','x4','x5']
seri=pd.Series(s)

df=pd.DataFrame(data=seri)
print(df)
fp=open("sms.txt",'w')
fp.write(df)
fp.close()
