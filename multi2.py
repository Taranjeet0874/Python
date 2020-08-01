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

d=df5.loc['Viplav']
print(d)
# visualising sub1 marks
x = name_1
y = df5['sub1']
plt.title("name vs sub1 Bar Graph")
plt.xlabel("name")
plt.ylabel("Sub1 marks")
plt.bar(x,y)
plt.show()

#subject 2 and subject 3 correlation
x = df5['sub2']
y = df5['sub3']
plt.title("Sub2 And Sub3 Relation")
plt.scatter(x,y)
plt.show()

# Data to plot
labels = name_1

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue']


y=df5["Total"]
plt.pie(y, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('graph of Student total marks  ')

plt.axis('equal')
plt.show()

#simple line graph

x=name_1
y=df5['Average']
plt.title("name vs sub1 Line Graph")
plt.xlabel("name")
plt.ylabel("Average marks")
plt.plot(x,y)
plt.show()


