
import pandas as pd

from matplotlib import pyplot as plt
name_1=["Viplav" ,"Viplav","Aakash","Aakash","Vikash","Vikash","Ashutosh","Ashutosh","Kamal","Kamal"]
sem=["sem-1","sem-2","sem-1","sem-2","sem-1","sem-2","sem-1","sem-2","sem-1","sem-2"]

subject={'sub1':[23,92,67,52,45,58,34,34,24,96],'sub2':[44,69,68,66,58,87,85,96,96,45],'sub3':[98,39,66,67,49,96,38,58,78,24],'grades':["A","A","B","A","C","B","B","B","A","A"]}
df5=pd.DataFrame(data=subject,index=[name_1,sem],columns=['sub1','sub2','sub3','grades'])
print(df5)
#average marks of subject
sa=df5.mean(axis=1)
df5['Average']=sa

#total marks of subject
ta=df5.sum(axis=1)
df5['Total']=ta
print(df5)

v=df5.loc[:,"sub1"]
print(v)
v.plot.bar()
plt.show()
v.plot.pie(autopct='%1.1f%%')
plt.show()
t=df5.loc["Viplav",:]
t.plot.bar(color=['blue','green','red','cyan','pink'])
plt.show()
plt.scatter(name_1,v)
plt.show()