# DATA FRAMES USING ARRAYS
import pandas as pd
import numpy as np
l=['x1','x2','x3','x4','x5']
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[2,5,3,7,8],[4,9,6,3,2],[6,4,3,8,6]])
df=pd.DataFrame(a,index=l)
print(df)