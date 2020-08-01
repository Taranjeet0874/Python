import pandas as pd

dic={"name":['n1','n2','n3','n4','n5'],"Ls1":[1,2,3,4,5],"Ps1":[2,4,5,6,4],"Ls2":[1,2,3,4,5],"Ps2":[2,4,5,6,4]}
df=pd.DataFrame(data=dic)
print(df)
df.set_index(['name'],inplace=True)
print(df)

#l=df.loc['n1',:]
#l.plot()
y=df.groupby(['name'])[('Ls1')].mean()
print(y)
