# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:12:35 2023

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

#Read the file with new data from the World Bank
df_wdi = pd.read_excel('WDI_data.xlsx')
#Sort the dataframe by variable
df_wdi = df_wdi.sort_values(by = ['Series Name', 'Country Name'], ignore_index=True)
#Delete the rows of countries not present in the list
for i in range(0,len(df_wdi)):
    if df_wdi['Country Name'][i] in country_list:
        pass
    else:
        df_wdi = df_wdi.drop(i)
#Save the name of the variables in a list
var_list = df_wdi['Series Name'].tolist()
var_list = list(dict.fromkeys(var_list))
#Create new coluns in df_data for the new variables
df_data = df_data.reindex(columns=list(df_data.columns)+var_list, fill_value=0)

#Split the WDI dataframe by variable, creating a dataframe for each variable
df_wdi_split = np.array_split(df_wdi, 36)

#Rearrange data to fit the df_data framework
var = []
for i in range(0,len(df_wdi_split)):
    var.insert(i, df_wdi_split[i]['Series Name'].iloc[0])
    df_wdi_split[i] = df_wdi_split[i].transpose()
    df_wdi_split[i].columns = df_wdi_split[i].iloc[0]
    df_wdi_split[i] = df_wdi_split[i].iloc[4:47, :]
    df_wdi_split[i] = pd.melt(df_wdi_split[i], value_name=var[i])
    
#Insert data into df_data
j = 0
for i in range(6,len(df_data.columns)):
    df_data.iloc[:,i] = df_wdi_split[j].iloc[:,1]
    j += 1
#Assign missing values as NaN
df_data = df_data.replace('..',np.NaN)

#Export to the Excel file
df_data.to_excel("data.xlsx")


