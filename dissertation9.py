# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 09:57:21 2023

@author: Sony Vaio
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

#Read data from excel
df_data = pd.read_excel('data.xlsx')
df_data = df_data.drop('Unnamed: 0', axis=1)

#Keep only GDP data
df_dep = pd.DataFrame()
df_dep['Country'] = df_data['Country']
df_dep['Year'] = df_data['Year']
df_dep['GDP'] = df_data.iloc[:,-2]
df_dep['GDPgrowth'] = df_data.iloc[:,-3]

#Split the data by country, having one dataframe per country
df_dep_split = np.array_split(df_dep, 144)
#Delete missing values in GDP data
for i in range(0,len(df_dep_split)):
    df_dep_split[i] = df_dep_split[i].dropna(subset=['GDP'])

#Delete Venezuela since it doesn't have any GDP data
del df_dep_split[139]

#Apply Hodrick-Prescott filter to GDP data to extract the trend (for each country)
for i in range(0,len(df_dep_split)):
    cycle, trend = sm.tsa.filters.hpfilter(df_dep_split[i].GDP, lamb=6.25)
    df_dep_split[i]['GDPtrend'] = trend
    df_dep_split[i]['GDPcycle'] = cycle
    
#Join the dataframes back together
column_list = df_dep_split[0].columns.tolist()
df_dep1 = pd.DataFrame(np.concatenate(df_dep_split))
df_dep1 = df_dep1.set_axis(column_list, axis=1)
df_dep1[['GDP', 'GDPgrowth', 'GDPtrend', 'GDPcycle']] = df_dep1[['GDP', 'GDPgrowth', 'GDPtrend', 'GDPcycle']].apply(pd.to_numeric)    
df_dep1 = df_dep1.drop(['GDP', 'GDPgrowth'], axis=1)

#Merge it into the original dataframe, to have all the years (with or without value)
df_dep = pd.merge(df_dep, df_dep1, on=['Country', 'Year'], how="left")

#Export to Excel
df_dep.to_excel('GDP_HP.xlsx')

#Import main datasets (df_crisis)
df_crisis1 = pd.read_excel('df_crisis1.xlsx')
df_crisis1 = df_crisis1.drop('Unnamed: 0', axis=1)
df_crisis2 = pd.read_excel('df_crisis2.xlsx')
df_crisis2 = df_crisis2.drop('Unnamed: 0', axis=1)

# Create an empty dataframe 
merged_df = pd.DataFrame()

# Iterate through each row in df_crisis1 and calculate the sum of the GDPcycle during the crisis episodes
for _, row in df_crisis1.iterrows():
    temp_df = df_dep[(df_dep['Country'] == row['Country']) & (df_dep['Year'] >= row['Start']) & (df_dep['Year'] <= row['End'])].copy()
    sum_GDPcycle = temp_df['GDPcycle'].sum()
    merged_df = pd.concat([merged_df, pd.DataFrame({
        'Country': [row['Country']],
        'Start': [row['Start']],
        'End': [row['End']],
        'Sum_GDPcycle': [sum_GDPcycle],
    })])

# Merge the original dataset df_crisis1 with the merged data
df_crisis1 = df_crisis1.merge(merged_df, on=['Country', 'Start', 'End'], how='left')

# Create an empty dataframe 
merged_df2 = pd.DataFrame()

# Iterate through each row in df_crisis2 and calculate the sum of the GDPcycle during the crisis episodes
for _, row in df_crisis2.iterrows():
    temp_df = df_dep[(df_dep['Country'] == row['Country']) & (df_dep['Year'] >= row['Start']) & (df_dep['Year'] <= row['End'])].copy()
    sum_GDPcycle = temp_df['GDPcycle'].sum()
    merged_df2 = pd.concat([merged_df2, pd.DataFrame({
        'Country': [row['Country']],
        'Start': [row['Start']],
        'End': [row['End']],
        'Sum_GDPcycle': [sum_GDPcycle],
    })])

# Merge the original dataset df_crisis2 with the merged data
df_crisis2 = df_crisis2.merge(merged_df2, on=['Country', 'Start', 'End'], how='left')

#Assign 0 in the sum_GDPcycle variable as NaN
df_crisis1['Sum_GDPcycle'] = df_crisis1['Sum_GDPcycle'].replace(0,np.NaN)
df_crisis2['Sum_GDPcycle'] = df_crisis2['Sum_GDPcycle'].replace(0,np.NaN)

#Export both datasets to Excel
df_crisis1.to_excel('df_crisis1.xlsx')
df_crisis2.to_excel('df_crisis2.xlsx')
