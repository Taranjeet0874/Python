
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame(np.arange(1,19).reshape(9,2),index=[['2008','2008','2008','2009','2009','2009','2010','2010','2010'],['June','July','August','June','July','August','June','July','August']],columns=['Rainfall','Temperature'])
print(df)
groups = df.groupby(["2008","June"])["Rainfall"].sum()
print(groups)
groups.plot.bar(color="blue")

plt.show()