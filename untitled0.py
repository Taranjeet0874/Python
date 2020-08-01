# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:26:23 2020

@author: Dell
"""

import pandas as pd
import numpy as np

df1=pd.read_excel('Energy Indicators.xls', skiprows =17 , skipfooter=38 )
df1.columns=['a','b','c','d','e','f']
df1.drop(['a','b'], axis=1 , inplace=True)
df1.columns=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
df1.replace('...', np.nan,inplace = True)
df1['Energy Supply'] = df1['Energy Supply']*1000000
df1['Country'].replace({"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"} , inplace=True)
    
df2=pd.read_csv('world_bank.csv' , skiprows=4)
df2['Country Name'].replace({"Korea, Rep.": "South Korea", 
    "Iran, Islamic Rep.": "Iran",
    "Hong Kong SAR, China": "Hong Kong"} , inplace=True)
df2.rename(columns={"Country Name" : 'Country'} , inplace=True)
   
    
df3=pd.read_excel('scimagojr.xlsx')
df4=pd.merge(df2,df1 , how='inner', left_on = 'Country' , right_on = 'Country')
df5=pd.merge(df4,df3 , how ='inner' , left_on = 'Country' , right_on = 'Country')
#df5=df5.set_index('Çountry')

print(df5)

    