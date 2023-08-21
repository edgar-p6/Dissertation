# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:00:55 2023

@author: EdgarPereira
"""

import pandas as pd
import numpy as np

# Read the Excel file with some data (GDP, CA and PV:GE were added manually in Excel)
df_data = pd.read_excel('data.xlsx')
df_data = df_data.drop('Unnamed: 5', axis=1)
# Assign missing values as NaN
df_data = df_data.replace('..',np.NaN)

# Read FX Reserves data
df_reserves = pd.read_excel('FXReserves.xlsx')
df_reserves = df_reserves.drop(range(145,150))
FXRes_list = df_reserves['Country Name'].tolist()

# Get the countries' list from the database and delete duplicates
country_list = df_data['Country'].tolist()
country_list = list(dict.fromkeys(country_list))

#Compare both countries's lists
res = [x for x in country_list + FXRes_list if x not in country_list or x not in FXRes_list]
#Harmonize countries names
df_data = df_data.replace('Congo, Democratic Republic of the', 'Congo, Dem. Rep.', regex=True)
df_data = df_data.replace('Congo, Republic of', 'Congo, Rep.', regex=True)
df_data = df_data.replace("Côte d'Ivoire", "Cote d'Ivoire", regex=True)
df_data = df_data.replace("Egypt", "Egypt, Arab Rep.", regex=True)
df_data = df_data.replace("Iran", "Iran, Islamic Rep.", regex=True)
df_data = df_data.replace("Korea", "Korea, Rep.", regex=True)
df_data = df_data.replace("Lao P.D.R.", "Lao PDR", regex=True)
df_data = df_data.replace("Macedonia, FYR", "North Macedonia", regex=True)
df_data = df_data.replace("Montenegro, Rep. of", "Montenegro", regex=True)
df_data = df_data.replace("Russia", "Russian Federation", regex=True)
df_data = df_data.replace("São Tomé and Príncipe", "Sao Tome and Principe", regex=True)
df_data = df_data.replace("Syria", "Syrian Arab Republic", regex=True)
df_data = df_data.replace("Turkey", "Turkiye", regex=True)
df_data = df_data.replace("Venezuela", "Venezuela, RB", regex=True)
df_data = df_data.replace("Yemen", "Yemen, Rep.", regex=True)
df_reserves = df_reserves[df_reserves['Country Name'] != 'Oman']

#Check if the countries names are harmonized
country_list = df_data['Country'].tolist()
country_list = list(dict.fromkeys(country_list))
FXRes_list = df_reserves['Country Name'].tolist()

res = [x for x in country_list + FXRes_list if x not in country_list or x not in FXRes_list]

#Rearrange reserves data to fit the df_data framework
df_temp = df_reserves.iloc[:,2:47].transpose()
df_temp.columns = df_temp.iloc[0]
df_temp = df_temp.iloc[2:45, :]
#Sort the countries alphabetically
df_temp = df_temp.sort_index(axis=1)
#Insert all values in just one column (to copy it to the df_data)
df_temp1 = pd.melt(df_temp, value_name='Tres')

#Insert column for the Reserves data in df_data
df_data['TRes'] = 0
#Sort the countries alphabetically
df_data = df_data.sort_values(by = ['Country', 'Year'], ascending = [True, True], ignore_index=True)
#Insert the reserves data in the TRes column
df_data['TRes'] = df_temp1['Tres']
# Assign missing values as NaN
df_data = df_data.replace('..',np.NaN)
