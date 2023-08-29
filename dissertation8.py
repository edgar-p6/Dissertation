# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:16:09 2023

@author: EdgarPereira
"""

import pandas as pd
import numpy as np

#Read the database
df_data = pd.read_excel('data.xlsx')
df_data = df_data.drop('Unnamed: 0', axis=1)

#Split the database by country
df_split = np.array_split(df_data, 144)

#Create a column in the database for the annual % change of the Official exchange rate
for i in range(0,len(df_split)):
    df_split[i]['Official Exchange Rate (annual %)'] = (df_split[i]['Official exchange rate (LCU per US$, period average)'].pct_change())*100

#Merge the database back together
df_data = pd.concat([country for country in df_split], ignore_index=True)

#Export to the Excel file
df_data.to_excel('data.xlsx')
