
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel("city.xlsx")
print(df)
df.plot.bar('year')
plt.show()

q=df.set_index(['year','type'])
print(q)
s=df.loc['year1']
print(s)
v=df.groupby(['year'])['city1'].mean()
g=df.groupby(['year'])['city1'].sum()
v.plot.bar(color='green')
plt.show()
v.plot()
plt.show()
g.plot.pie(startangle=90)
plt.show()
#print(v)
#p=df.groupby(['year'])['city1'].sum()
#print(p)

s=[1,6,1,2,5,2,3,4,3,4,3,4,5,2,5,6,1,6,1,2,8,2,3,9,3,4,7]

gf=pd.DataFrame(np.array(s).reshape(9,3),index=[['year1','year1','year1','year2','year2','year2','year3','year3','year3'],['hacking','offfraud','dos','hacking','offfraud','dos','hacking','offfraud','dos']],columns=['city1','city2','city3'])
print(gf)
m=gf.loc[('year1'),:'city1']
print(m)
m.plot.bar(color='blue')
plt.show()
p=['hacking','offfraud','dos']
plt.scatter(p,m)
plt.show()
n=gf.loc[('year1'),:]
n.plot.bar(color=['green','blue','cyan'])
plt.show()
f=gf.loc[('year1','hacking'),:].max()
print(f)
