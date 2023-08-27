# Dissertation
Code used in the elaboration of the dissertation with the title "Can Early Warning Indicators Explain the Depth and Severity of Sovereign Debt Crises?" for the Master in Economics at FEP, by Edgar Pereira, supervised by Professor Manuel Duarte Rocha

--------------------------------------------------------------------------------------------------------------------------------------------

## Guide to the code files:

### Code to build the datasets

 **dissertation1.py:** initializes and organizes the format for the databases, with the countries, years and crisis episodes

 **dissertation2.py:** after manually adding three variables in Excel (GDP, Current Account, and Political Variable: Government Effectiveness), organizes the database to add the variable Total Reserves (TRes), with code replicable for further variables

 **dissertation3.py:** adapting and using part of the code used in dissertation2.py, reads, organizes and adds to the database 36 new variables retrieved from The World Bank

 **dissertation4.py:** reads, organizes and adds to the database variables retrieved from the IMF Fiscal Monitor

 **dissertation5.py:** reads, organizes and adds to the database variables on commodity prices (oil and food), global variables (GDP growth in USA and China, real interest rate in USA), and banking crisis dummy

 **dissertation6.py:** reads, organizes and adds to the database data on GDP growth, retrieved from The World Bank

**dissertation7.py:** reads, organizes and adds to the database data on GDP and GDP per capita (constant 2015 US$), removing previously retrieved GDP and GDP per capita data (constant 2017 international $), due to having less missing values

 **dissertation8.py:** adds data on default history in the period (dummy for past default and number of past defaults), and merges all the data retrieved into the main database, for the years with crisis episodes, creating two datasets (1 year antecipation vs 2 years antecipation)

 **dissertation9.py:** applies Hodrick-Prescott filter to GDP data (creating variables trendGDP and cycleGDP), and computes the cumulative difference between actual GDP and trend GDP for each crisis episode (dependent variable "Cumulative_diff"), during the length of the crisis, with the length being as in the original Moreno Badia et al (2022) dataset, computing as well the mean difference per year of crisis, by dividing this variable by the length of the crisis

 ### Code used for the regressions

 **dissertation10.py:** performs the bivariate OLS regressions on the mean difference between actual GDP and trendGDP per year of crisis with 1-year antecipation in the independent variables, performing the White test for heteroskedasticity (and correcting it when needed). Detailed results of all the regressions are in **"bivariate_regression_results_GDPmean_1Y.pdf"**

 **dissertation11.py:** performs the bivariate OLS regressions on the mean difference between actual GDP and trendGDP per year of crisis with 2-years antecipation in the independent variables, performing the White test for heteroskedasticity (and correcting it when needed). Detailed results of all the regressions are in **"bivariate_regression_results_GDPmean_2Y.pdf"**

 **dissertation12.py:** performs the bivariate OLS regressions on the length of the crisis with 1-year antecipation in the independent variables, performing the White test for heteroskedasticity (and correcting it when needed). Detailed results of all the regressions are in **"bivariate_regression_results_length_1Y.pdf"**

 **dissertation13.py:** performs the bivariate OLS regressions on the length of the crisis with 2-years antecipation in the independent variables, performing the White test for heteroskedasticity (and correcting it when needed). Detailed results of all the regressions are in **"bivariate_regression_results_length_2Y.pdf"**

 **dissertation14.py:** performs the bivariate OLS regressions on the cumulative difference between actual GDP and trendGDP during the crisis with 1-year antecipation in the independent variables, performing the White test for heteroskedasticity (and correcting it when needed). Detailed results of all the regressions are in **"bivariate_regression_results_GDPcumulative_1Y.pdf"**

 **dissertation15.py:** performs the bivariate OLS regressions on the cumulative difference between actual GDP and trendGDP during the crisis with 2-years antecipation in the independent variables, performing the White test for heteroskedasticity (and correcting it when needed). Detailed results of all the regressions are in **"bivariate_regression_results_GDPcumulative_2Y.pdf"**

 ## Guide to the data files

 **data.xlsx:** auxiliary dataset, used to create the main datasets, with data on the used variables for the countries from 1980-2022

**df_crisis1.xlsx:** main dataset to be directly used in the empirical analysis, with data of the crisis episodes, with independent variables having a 1-year antecipation

**df_crisis2.xlsx:** main dataset to be directly used in the empirical analysis, with data of the crisis episodes, with independent variables having a 2-year antecipation



