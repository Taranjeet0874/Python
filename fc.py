import pandas as pd
import numpy as np

df=pd.read_excel("fc.xlsx",header=[0,1],index_col=0)
print(df)

s=df.max()
print(s)

df1=df.groupby([('term1','fc')])
for i,i_df in df1:
    print(i)
df1.plot.bar()
plt.show()
print(df[('term1','fc')].agg([np.mean,np.sum,min,max,np.std]))
    