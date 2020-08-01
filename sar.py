import pandas as pd

import matplotlib.pyplot as plt

df=pd.read_excel("41a.xlsx",index_col=[0,1])
print(df)

a=df.loc[2009]
a.plot.bar()
plt.show()
print(a)


#using groupby visualise yearwise rainfall
groups = df.groupby(["year"])["rainfall"].sum()
print(groups)
groups.plot.bar(color="blue")
plt.show()


#using groupby visualise yearwise rainfall

groups = df.groupby(["year"])["temperature"].mean()
print(groups)
groups.plot.bar(color="blue")
plt.show()

#visualise all possible ways
m=df.loc[:,"rainfall"]
print(m)

#f=df.groupby([('year','june')])

#for i,i_df in f:
  #  print(i)
