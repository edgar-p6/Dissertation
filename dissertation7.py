# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 21:13:45 2023

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
df_gdp_new = pd.read_excel('GDP.xlsx')
#Sort the dataframe by variable
df_gdp_new = df_gdp_new.sort_values(by = ['Series Name', 'Country Name'], ignore_index=True)
#Delete the rows of countries not present in the list
for i in range(0,len(df_gdp_new)):
    if df_gdp_new['Country Name'][i] in country_list:
        pass
    else:
        df_gdp_new = df_gdp_new.drop(i)
#Save the name of the variables in a list
var_list = df_gdp_new['Series Name'].tolist()
var_list = list(dict.fromkeys(var_list))
#Create new coluns in df_data for the new variables
df_data = df_data.reindex(columns=list(df_data.columns)+var_list, fill_value=0)

#Split the dataframe by variable, creating a dataframe for each of the two variables
df_split = np.array_split(df_gdp_new, 2)

#Rearrange data to fit the df_data framework
var = []
for i in range(0,len(df_split)):
    var.insert(i, df_split[i]['Series Name'].iloc[0])
    df_split[i] = df_split[i].transpose()
    df_split[i].columns = df_split[i].iloc[0]
    df_split[i] = df_split[i].iloc[4:47, :]
    df_split[i] = pd.melt(df_split[i], value_name=var[i])
    
#Insert data into df_data
df_data['GDP (constant 2015 US$)'] = df_split[0]['GDP (constant 2015 US$)']
df_data['GDP per capita (constant 2015 US$)'] = df_split[1]['GDP per capita (constant 2015 US$)']

#Assign missing values as NaN
df_data = df_data.replace('..',np.NaN)

#Delete previously retrieved GDP and GDP per capita data
df_data = df_data.drop(['GDP', 'GDP per capita, PPP (constant 2017 international $)'], axis=1)

#Export to the Excel file
df_data.to_excel("data.xlsx")


