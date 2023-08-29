# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 13:46:52 2023

@author: EdgarPereira
"""

import pandas as pd
import numpy as np

#Import the main database (df_crisis) from excel
df_crisis = pd.read_excel('df_crisis.xlsx')
df_crisis = df_crisis.drop('Unnamed: 0', axis=1)

#Add a variable with the number of past defaults in the period
df_crisis['# of past defaults'] = df_crisis.groupby('Country').cumcount()
#Add a dummy variable for the past defaults (0 for the first default in the period, 1 for the others)
df_crisis['Dummy for past default'] = 0
for i in range(0,len(df_crisis)):
    if df_crisis['# of past defaults'].iloc[i] > 0:
        df_crisis['Dummy for past default'].iloc[i] = 1
        
##############################################################################

#Import the database with the variables
df_data = pd.read_excel('data.xlsx')
df_data = df_data.drop('Unnamed: 0', axis=1)

df_crisis = df_crisis.rename({'Start': 'Year'}, axis=1)

# Create an empty dataframe (temporary)
merged_df = pd.DataFrame()
# Iterate through each row in the df_crisis dataframe and merge data from df_data, with 1 year of antecipation
for _, row in df_crisis.iterrows():
    temp_df = df_data[(df_data['Country'] == row['Country']) & (df_data['Year'] == row['Year'] - 1)].copy()
    temp_df['Year'] = row['Year']  
    merged_df = pd.concat([merged_df, temp_df])
    
#Merge it back into df_crisis
df_crisis1 = df_crisis.merge(merged_df, on=['Country', 'Year'], how='left')

df_crisis1 = df_crisis1.rename({'Year': 'Start'}, axis=1)

# Create an empty dataframe (temporary)
merged_df2 = pd.DataFrame()
# Iterate through each row in the df_crisis dataframe and merge data from df_data, with 2 years of antecipation
for _, row in df_crisis.iterrows():
    temp_df2 = df_data[(df_data['Country'] == row['Country']) & (df_data['Year'] == row['Year'] - 2)].copy()
    temp_df2['Year'] = row['Year']  
    merged_df2 = pd.concat([merged_df2, temp_df2])
    
#Merge it back into df_crisis
df_crisis2 = df_crisis.merge(merged_df2, on=['Country', 'Year'], how='left')

df_crisis2 = df_crisis2.rename({'Year': 'Start'}, axis=1)

#Export both datasets to Excel
df_crisis1.to_excel('df_crisis1.xlsx')
df_crisis2.to_excel('df_crisis2.xlsx')

