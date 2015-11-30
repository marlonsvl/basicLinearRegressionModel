
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:46:09 2015

@author: marlon
"""
import numpy as numpyp
import pandas as pandas
import statsmodels.api
import statsmodels.formula.api as smf

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

#call in data set
data = pandas.read_csv('/Users/utpl/Documents/RegressionModelingInPractice/gapminder.csv')

# convert variables to numeric format using convert_objects function
data['breastcancerper100th'] = pandas.to_numeric(data['breastcancerper100th'], errors='coerce')
data['co2emissions'] = pandas.to_numeric(data['co2emissions'], errors='coerce')

############################################################################################
# BASIC LINEAR REGRESSION
############################################################################################
scat1 = seaborn.regplot(x="co2emissions", y="breastcancerper100th", scatter=True, data=data)
plt.xlabel('Co2 Emissions')
plt.ylabel('Breast cancer per 100 TH')
plt.title ('Scatterplot for the Association Between Co2 Emissions and Breast per 100 TH')
print(scat1)

print ("OLS regression model for the association between Co2 Emissions and Breast cancer per 100 TH")
reg1 = smf.ols('breastcancerper100th ~ co2emissions', data=data).fit()
print (reg1.summary())



