# DATA FRAME USING LIST
import pandas as pd
Roll_no=[1,2,3,4,5]
Name=["Taran","aman","ayush","aditya","saurabh"]
Math=[56,87,67,98,45]
Science=[67,87,56,98,78]
Statistics=[56,78,67,98,45]
dict={'Roll_no':Roll_no,'Name':Name,'Math':Math,'Science':Science,'Statistics':Statistics}
df=pd.DataFrame(dict)
print("***************ATTENDANCE RECORD***********")
print(df)