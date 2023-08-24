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

 **dissertation8.py:** adds data on default history in the period (dummy for past default and number of past defaults), and merges all the data retrieved into the main database, for the years with crisis episodes, creating two datasets (1 year antecipation vs 2 years antecipation
