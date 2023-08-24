# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:24:42 2023

@author: EdgarPereira
"""

import pandas as pd

# Read the Excel file with the crisis episodes and extract the country's names
df_crisis = pd.read_excel('Crisis_Episodes.xlsx')
countries = df_crisis.iloc[:145, 0].tolist()

# Create the DataFrame with the pair COUNTRY+YEAR as index columns
df_data = pd.DataFrame(columns=['Country', 'Year'])
df_data['Country'] = countries
df_data['Year'] = 2023-1980
df_data = df_data.loc[df_data.index.repeat(df_data.Year)]
years = [*range(1980,2023,1)]*144
df_data['Year'] = years
df_data = df_data.set_index(['Country','Year'])
# Export the dataframe to excel (data will be added manually on Excel)
df_data.to_excel("df_data.xlsx")

# From the Excel file (of crisis episodes), count how many crisis episodes each country had
df_crisis = df_crisis.rename(columns={'Crisis Episodes': 'CrisisEpisodes'})
df_crisis['CrisisEpisodes'] = df_crisis.CrisisEpisodes.apply(lambda x: x.strip('()').split(','))
df_crisis['NoCrisis'] = df_crisis['CrisisEpisodes'].apply(lambda x: len(x))
# Duplicate rows so that every crisis episode is a different row
df_crisis[['crisis1','crisis2','crisis3','crisis4','crisis5','crisis6']] = pd.DataFrame(df_crisis.CrisisEpisodes.tolist(), index= df_crisis.index)
crisis_columns = ['crisis1', 'crisis2', 'crisis3', 'crisis4', 'crisis5', 'crisis6']
df_crisis = pd.melt(df_crisis, id_vars=['Country', 'NoCrisis'], value_vars=crisis_columns, var_name='CrisisEpisode', value_name='Crisis')
df_crisis = df_crisis[df_crisis['Crisis'].notna()]
df_crisis = df_crisis.sort_values(by='Country').reset_index(drop=True)
df_crisis = df_crisis.drop(['NoCrisis', 'CrisisEpisode'], axis=1)
# Add a column with the length of the crisis (as per the database of Moreno Badia)
df_crisis[['Start', 'End']] = df_crisis['Crisis'].str.split('-', expand=True).astype(int)
df_crisis['length_db'] = df_crisis['End'] - df_crisis['Start']
df_crisis['Crisis'] = df_crisis['Start'].astype(str) + '-' + df_crisis['End'].astype(str)

#Export df_crisis to excel
df_crisis.to_excel('df_crisis.xlsx')

# Final result of this script:
    # df_data (indexed by country and year): database to add data on the variables for all countries and years, to be used to build the main database
    # df_crisis (indexed by country and crisis episode and with some information about the crisis episodes): main database of crisis episodes to be studied
