# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:55:43 2023

@author: EdgarPereira
"""

import pandas as pd
import matplotlib.pyplot as plt

#Read GDP (after HP) data
df_gdp = pd.read_excel('GDP_HP.xlsx')
df_gdp = df_gdp.drop('Unnamed: 0', axis=1)

#Define the data for the plots
years = df_gdp['Year'].tolist()
years = list(dict.fromkeys(years))

ALG_GDP = df_gdp[df_gdp['Country'] == 'Algeria']['GDP']
ARG_GDP = df_gdp[df_gdp['Country'] == 'Argentina']['GDP']
POR_GDP = df_gdp[df_gdp['Country'] == 'Portugal']['GDP']
ZMB_GDP = df_gdp[df_gdp['Country'] == 'Zimbabwe']['GDP']

ALG_GDPtrend = df_gdp[df_gdp['Country'] == 'Algeria']['GDPtrend']
ARG_GDPtrend = df_gdp[df_gdp['Country'] == 'Argentina']['GDPtrend']
POR_GDPtrend = df_gdp[df_gdp['Country'] == 'Portugal']['GDPtrend']
ZMB_GDPtrend = df_gdp[df_gdp['Country'] == 'Zimbabwe']['GDPtrend']

# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

#Plot Algeria
axs[0,0].plot(years, (ALG_GDP/1e11), label='Actual GDP')
axs[0,0].plot(years, (ALG_GDPtrend/1e11), label='GDP Trend')
axs[0,0].axvspan(1984, 1985,color='gray', alpha=0.3)
axs[0,0].axvspan(1991, 2000,color='gray', alpha=0.3)
axs[0,0].set_ylabel('GDP (1e11)')
axs[0,0].set_title('Algeria')
axs[0,0].legend()
#Plot Argentina
axs[0,1].plot(years, (ARG_GDP/1e11), label='Actual GDP')
axs[0,1].plot(years, (ARG_GDPtrend/1e11), label='GDP Trend')
axs[0,1].axvspan(2008, 2009,color='gray', alpha=0.3)
axs[0,1].axvspan(2012, 2015,color='gray', alpha=0.3)
axs[0,1].axvspan(2018, 2021,color='gray', alpha=0.3)
axs[0,1].set_ylabel('GDP (1e11)')
axs[0,1].set_title('Argentina')
axs[0,1].legend()
#Plot Portugal
axs[1,0].plot(years, (POR_GDP/1e11), label='Actual GDP')
axs[1,0].plot(years, (POR_GDPtrend/1e11), label='GDP Trend')
axs[1,0].axvspan(1983, 1985,color='gray', alpha=0.3)
axs[1,0].axvspan(2011, 2014,color='gray', alpha=0.3)
axs[1,0].set_ylabel('GDP (1e11)')
axs[1,0].set_title('Portugal')
axs[1,0].legend()
#Plot Zimbabwe
axs[1,1].plot(years, (ZMB_GDP/1e10), label='Actual GDP')
axs[1,1].plot(years, (ZMB_GDPtrend/1e10), label='GDP Trend')
axs[1,1].axvspan(1983, 1984,color='gray', alpha=0.3)
axs[1,1].axvspan(1992, 1993,color='gray', alpha=0.3)
axs[1,1].axvspan(1995, 1996,color='gray', alpha=0.3)
axs[1,1].axvspan(2000, 2009,color='gray', alpha=0.3)
axs[1,1].axvspan(2012, 2013,color='gray', alpha=0.3)
axs[1,1].set_ylabel('GDP (1e10)')
axs[1,1].set_title('Zimbabwe')
axs[1,1].legend()

#Set labels and title
for ax in axs.flat:
    ax.set(xlabel='Years')

#Add a legend
ax.legend()

#Adjust layout
plt.tight_layout()

#Save the plot
plt.savefig('GDPvsGDPtrend.jpg', format='jpg')

# Show the plot
plt.show()
