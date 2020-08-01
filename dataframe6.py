import pandas as pd
dict={'MP':[10,11],'UP':[13,12]}
df=pd.DataFrame(dict,index=['2001','2002'])
print(df)
df.index=['t','s']  # METHOD 1
print(df)
df.reindex(['a','b'])  #METHOD 2
print(df)