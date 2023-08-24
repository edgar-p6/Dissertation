# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:00:49 2023

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

#Read the commodity prices data (oil and food prices)
df_commodity = pd.read_excel('CommodityPrices.xlsx')
df_commodity = df_commodity.iloc[1:44,:]

#Merge the CommodityPrices data into df_data based on the year
df_data = pd.merge(df_data, df_commodity, on='Year', how="left")

############################################################################

#Read the Global Variables data (GDP growth in U.S. and China and real interest rate in the U.S.)
df_global = pd.read_excel('GlobalVariables.xlsx')
df_global = df_global.iloc[0:3,:]
#Change the name of the variables to add the country name
var_list = ['GDP growth USA (annual %)', 'Real interest rate USA (%)', 'GDP growth China (annual %)']
df_global['Series Name'] = var_list

#Rearrange the data to fit in df_data
df_global = df_global.transpose()
df_global.columns = df_global.iloc[2]
df_global = df_global.iloc[4:47,:]
df_global = df_global.reset_index()
df_global = df_global.rename(columns={'index': 'Year'})
df_global['Year'] = list(range(1980,2023))

#Merge the GlobalVariables data into df_data based on the year
df_data = pd.merge(df_data, df_global, on='Year', how="left")
#Assign missing values as NaN
df_data = df_data.replace('..',np.NaN)

############################################################################

#Read the Banking Crisis Database
df_bank = pd.read_excel('Panics and bank failures database.xlsx', sheet_name=1)
#Delete the rows of countries not present in the list
for i in range(0,len(df_bank)):
    if df_bank['Country'][i] in country_list:
        pass
    else:
        df_bank = df_bank.drop(i)
df_bank = df_bank.reset_index()
#Delete the rows of banking crisis previous to 1980
for i in range(0,len(df_bank)):
    if (df_bank['BVX Year'][i] < 1980):
        df_bank = df_bank.drop(i)
#Keep only the necessary columns
df_bank = df_bank[['Country', 'BVX Year', 'BVX list: UNION OF TWO TYPES']]
df_bank = df_bank.rename(columns={'BVX Year': 'Year', 'BVX list: UNION OF TWO TYPES': 'Banking Crisis Dummy'})

#Merge the databse into df_data based on the common country name and year
df_data = pd.merge(df_data, df_bank, on=['Country', 'Year'], how="left")

#Export to the Excel file
df_data.to_excel("data.xlsx")

