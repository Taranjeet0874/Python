# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:24:45 2019

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("time.xlsx",header=[0,1])
print(df)
df.set_index(["time"],inplace=True)
print(df)
print(df.swaplevel(0,1,axis=1))
print(df.stack())


p=df.groupby(["time"])['fb'].sum()
p.plot.bar()
plt.show()

#x=df.loc['time':,'fb']
#print(x)