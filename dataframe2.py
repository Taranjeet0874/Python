# DATA FRAME USING DICTIONARY
# ATTENDANCE RECORD OF STUDENTS
import pandas as pd
print(" ************ATTENDANCE RECORD**************** ")
dict={'ROLL_NO':[1,2,3,4,5],'NAME':["taran","aman","ayush","muskan","yash"],'MATH':[89,78,67,86,45],'SCIENCE':[45,67,87,45,98],'STATISTICS':[69,89,76,45,67]}
df=pd.DataFrame(dict)
print(df)