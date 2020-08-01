import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("prac.csv")
print(df)
f=df.loc[:,"pune"]
g=['horror','action','romantic','thriller','comedy']
#plt.plot(g,f)
#plt.title(" Sale of pune in year 2008 ")
#plt.xlabel("category")
#plt.ylabel("sale")
df.set_index(['category'],inplace=True)
print(df)
groups = df.groupby(["category"])["pune"].sum()
groups.plot.bar(color="blue")

plt.show()
