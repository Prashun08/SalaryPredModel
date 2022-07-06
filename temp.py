# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

data=pd.read_csv("C:/Users/pchakrabor24/OneDrive - DXC Production/Desktop/Data_Science/Salary_Data.csv")

# Showing statistics of the dataframe
data.describe()

# Creating First Regression

# Defining Variables
y = data['Salary']
x1 = data['YearsExperience']

#Explore Data
plt.scatter(x1,y)
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Regression itself
x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary() 

#Plotting Regression
plt.scatter(x1,y)
yhat = 2.579*pow(10,4)+9449.9623*x1
fig=plt.plot(x1,yhat,lw=4,c='orange',label='regression line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

