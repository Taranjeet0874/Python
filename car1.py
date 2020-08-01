import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.read_excel("car.xlsx")
print(df)


df.set_index(['category','name'],inplace=True)
print(df)
t=df.groupby(['name'])[('q1','q2','q3','q4')].sum()
t.plot.bar()
plt.show()

t.plot()
plt.show()
e=df.groupby(['name'])['q1'].sum()
e.plot.pie(autopct="%1.1f%%")
plt.show()


#2.	Find most economical vehicle type
d=df.sum(axis=1)
print(d)
df['total']=d
print(df)

c=df.groupby(['name'])['total'].sum()
c.plot.bar()

#3	Find average income from each quarter for each vehicle type

f=df.groupby(['category'])['q1','q2','q3','q4'].mean()
print(f)

#4
l=df.groupby(['name'])['hy'].sum()
l.plot.bar()

