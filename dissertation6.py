# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:31:24 2023

@author: EdgarPereira
"""

import pandas as pd
import numpy as np

#Read the data file previously made
df_data = pd.read_excel('data.xlsx')
df_data = df_data.drop('Unnamed: 0', axis=1)
#Create a list of the countries in the dataframe
country_list = df_data['Country'].tolist()
country_list = list(dict.fromkeys(country_list))

#Read the file with new data (GDP growth) from the World Bank
df_gdp = pd.read_excel('GDP_growth.xlsx')
df_gdp = df_gdp.drop(range(217,222))
#Drop countries not present in country_list
for i in range(0,len(df_gdp)):
    if df_gdp['Country Name'][i] in country_list:
        pass
    else:
        df_gdp = df_gdp.drop(i)
        
#Rearrange data to fit the df_data framework
df_gdp = df_gdp.iloc[:,2:47].transpose()
df_gdp.columns = df_gdp.iloc[0]
df_gdp = df_gdp.iloc[2:45, :]
#Sort the countries alphabetically
df_gdp = df_gdp.sort_index(axis=1)
#Insert all values in just one column (to copy it to the df_data)
df_gdp = pd.melt(df_gdp, value_name='GDP growth')

#Insert column for the GDP growth in df_data
df_data['GDP growth (annual %)'] = 0
#Insert the data in the new column
df_data['GDP growth (annual %)'] = df_gdp['GDP growth']
# Assign missing values as NaN
df_data = df_data.replace('..',np.NaN)

#Export to the Excel file
df_data.to_excel("data.xlsx")
