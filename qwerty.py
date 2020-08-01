import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.DataFrame(np.arange(12).reshape(4,3),index=[['FY','FY','SY','SY'],['SEM1','SEM2','SEM1','SEM2']],columns=['MATH','SCIENCE','CS'])
print(df)
f=df.loc[("FY","SEM2"),:]
g=['MATH','SCIENCE','CS']
plt.plot(g,f)
plt.title(" Sale of pune in year 2008 ")
plt.xlabel("category")
plt.ylabel("sale")
plt.show()