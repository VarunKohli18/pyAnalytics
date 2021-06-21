# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:37:09 2021

@author: Varun Kohli

denco Case Study
"""

##Objectives:
#Expand business by encouraging repeated sales
#Maximise revenue from high value parts

##Info Required:
#Who are the loyal customers - improve repeated sales, target customers with low sales volumes
#Which customers contribtes most to revenue - how do i retain these customers and target incentives
#What part numbers bring in to significant portion of revenue - maximise revenue from high value parts
#What parts have highest profit margin - what parts are driving profits and what parts need to build further

#%% Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dencoDF = pd.read_csv('denco.csv')
dencoDF
dir(dencoDF)

#%% Import method 2

url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
dencoDF2 = pd.read_csv(url)
dencoDF2

#%% Dataset properties

dencoDF.shape #dimensions
dencoDF.columns #column names
len(dencoDF) #number of columns
dencoDF.dtypes #datatypes in each column

dencoDF.head(3) #first 3 rows
dencoDF.tail(3) #last 3 rows
dencoDF.describe()

pd.options.display.float_format = '{:2f}'.format
dencoDF.describe()

dencoDF['region'] = dencoDF['region'].astype('category')
dencoDF.describe()

dencoDF.region.value_counts()
dencoDF.region.value_counts().plot(kind='bar')

#%% who are the most loyal customers

dencoDF.value_counts().sort_values(ascending=False).head(5)

# revenue total per customer
dencoDF.groupby('custname').revenue.sum().sort_values(ascending=False).head(5) 

dencoDF.groupby('custname').aggregate({'revenue':[np.sum,max,min,'count']}).sort_values(by=('revenue','count'))
dencoDF.groupby('custname')['revenue'].aggregate([np.sum,max,min,'count']).sort_values(by='count')

# what part numbers bring in the significant portion of revenue

# top revenue items
dencoDF.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum',ascending=False).head(5)
# bottom revenue items
dencoDF.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum',ascending=False).tail(5)

# top profit making items

dencoDF.groupby('partnum')['margin'].aggregate([np.sum]).sort_values(by='sum',ascending=False).head(5)

# most sold items

dencoDF.groupby('partnum').size().sort_values(ascending=False).head(5)

# which region gives maximum revenue

dencoDF.groupby('region')['revenue'].aggregate([np.sum]).sort_values(by='sum', ascending=False).head(5)
