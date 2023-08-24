# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:25:36 2023

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

#Read the data on fiscal variables retrieved from the IMF Fiscal Monitor
df_fiscal = pd.read_csv('IMF_FiscalMonitor.csv')
df_fiscal = df_fiscal.drop('Unnamed: 19', axis=1)
df_fiscal = df_fiscal.drop('Country Code', axis=1)
df_fiscal = df_fiscal.loc[:,~df_fiscal.columns.str.startswith('Status')]
#Sort the IMF database by alphabetical order (countries) and ascending order (time period)
df_fiscal = df_fiscal.sort_values(by = ['Country Name', 'Time Period'], ignore_index=True)
# Change columns' name to same as df_data + removing series name from the columns' names
new_columns = ['Country', 'Year',
       'Cyclically adjusted balance (% of potential GDP)',
       'Cyclically adjusted primary balance (% of potential GDP)',
       'Expenditure (% of GDP)',
       'Gross debt (% of GDP)',
       'Net debt (% of GDP)',
       'Net lending/borrowing (overall balance) (% of GDP)',
       'Primary net lending/borrowing (primary balance) (% of GDP)',
       'Revenue (% of GDP)']
df_fiscal = df_fiscal.set_axis(new_columns, axis='columns')

#Merge IMF databse into df_data based on the common country name and year
df_data = pd.merge(df_data, df_fiscal, on=['Country', 'Year'], how="left")

#Comparing similar variables retrieved from The World Bank and the IMF and deleting the one with more missing values
##Gross national expenditure (The World Bank) vs Expenditure (IMF Fiscal Monitor)
(df_data.iloc[:,26].isna().sum())/len(df_data) # 23,9% of missing data (The World Bank)
(df_data.iloc[:,-6].isna().sum())/len(df_data) # 40,9% of missing data
df_data = df_data.drop('Expenditure (% of GDP)', axis=1)

#Export to the Excel file
df_data.to_excel("data.xlsx")
