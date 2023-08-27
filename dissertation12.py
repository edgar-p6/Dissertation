# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:40:39 2023

@author: EdgarPereira
"""

import pandas as pd
import numpy as np
import re
import statsmodels.api as sm
import statsmodels.stats.diagnostic as diag
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#Import the crisis dataset
df_crisis1 = pd.read_excel('df_crisis1.xlsx')
df_crisis1 = df_crisis1.drop('Unnamed: 0', axis=1)

# Create a function to remove invalid characters from variables names
def sanitize_variable_name(name):
    invalid_characters = r'[\\/:*?"<>|]'
    sanitized_name = re.sub(invalid_characters, '', name)
    return sanitized_name

sanitized_name_mapping = {var: sanitize_variable_name(var) for var in df_crisis1.columns}

# Extract and define the dependent variable and independent variables
dependent_variable = 'length_db'
independent_variables = df_crisis1.columns.difference([dependent_variable, 'Country', 'Crisis', 'Start', 'End', 'Mean_diff', 'Cumulative_diff'])

# Define the independent variables for which to apply the natural logarithm
variables_to_log = ['Debt service on external debt, total (TDS, current US$)',
                    'GDP (constant 2015 US$)',
                    'GDP per capita (constant 2015 US$)',
                    'Net official aid received (current US$)',
                    'Official exchange rate (LCU per US$, period average)',
                    'TRes',
                    'Use of IMF credit (DOD, current US$)']

#Small constant to add to the variables that will be log-transformed, since some of them have a few values equal to 0
log_offset = 1e-25

# Remove an outlier identified in one of the independent variables
df_crisis1.loc[df_crisis1['Short-term debt (% of total reserves)'].idxmax(), 'Short-term debt (% of total reserves)'] = np.nan

# Create a PDF file to save results
pdf_filename = 'bivariate_regression_results_length_1Y.pdf'

# Perform bivariate regressions and save to PDF
with PdfPages(pdf_filename) as pdf:
    for ind_var in independent_variables:
        # Drop rows with missing values for the current pair of variables
        subset_df = df_crisis1[[dependent_variable, ind_var]].dropna()
        
        X = sm.add_constant(subset_df[ind_var])  # Add the intercept
        # Apply natural logarithm with offset to the specific independent variables
        if ind_var in variables_to_log:
            subset_df['ln_' + ind_var] = np.log(subset_df[ind_var] + log_offset)
            X = sm.add_constant(subset_df['ln_' + ind_var])
        
        y = subset_df[dependent_variable]
        
        model = sm.OLS(y, X).fit()
        
        # White test for heteroskedasticity
        white_test = diag.het_white(model.resid, exog=model.model.exog)
        
        # Use a robust estimator for the regressions where heteroskedasticity was found through the White test performed
        if white_test[1] < 0.1:  # Using 0.1 as the threshold, you can adjust this as needed
            model_robust = sm.OLS(y, X).fit(cov_type='HC3')
            summary = model_robust.summary()
            new_white_test = diag.het_white(model_robust.resid, exog=model_robust.model.exog)
        else:
            summary = model.summary()
            new_white_test = white_test
        
        # Save the summary as a text file
        sanitized_name = sanitized_name_mapping.get(ind_var, sanitize_variable_name(ind_var))
        summary_filename = f'{sanitized_name}_summary.txt'
        with open(summary_filename, 'w') as summary_file:
            summary_file.write(summary.as_text())
            summary_file.write('\nWhite Test Results:\n')
            summary_file.write(f'LM Statistic: {new_white_test[0]}\n')
            summary_file.write(f'LM P-Value: {new_white_test[1]}\n')
            summary_file.write(f'F Statistic: {new_white_test[2]}\n')
            summary_file.write(f'F P-Value: {new_white_test[3]}\n')
        
        # Create a figure and axis for the PDF plot
        fig, ax = plt.subplots(figsize=(8, 10))
        
        # Add a text annotation to the plot
        ax.text(0.1, 0.9, 'Regression Summary:', fontsize=12)
        ax.text(0.1, 0.88, summary.as_text(), fontsize=10, va='top', ha='left', linespacing=1.5)
        ax.text(0.1, 0.2, 'White Test Results:', fontsize=12)
        ax.text(0.1, 0.17, f'LM Statistic: {new_white_test[0]}\nLM P-Value: {new_white_test[1]}\nF Statistic: {new_white_test[2]}\nF P-Value: {new_white_test[3]}', fontsize=10, va='top', ha='left', linespacing=1.5)
        ax.axis('off')
        ax.axis('off')
        
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()

print('Regression results saved to bivariate_regression_results_length_1Y.pdf')
