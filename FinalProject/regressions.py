#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:05:30 2020

@author: ZainKhawaja
"""

# Import Python Packages; statsmodels.formula.api is the regression package
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import numpy as np
import statsmodels.formula.api as sm

# Set the start and end dates
style.use("ggplot")
start = dt.datetime(2019, 1, 1)
end = dt.date.today()

# Get the data from yahoo finance (this is the pandas_datareader package)
df1 = web.get_data_yahoo('CL=F', start, end)
df2 = web.get_data_yahoo('CADUSD=X', start, end)

# Drop unecessary variables
df1 = df1.drop(['High', 'Low', 'Open', 'Volume', 'Adj Close'], axis=1)
df2 = df2.drop(['High', 'Low', 'Open', 'Volume', 'Adj Close'], axis=1)

# Create column for the natural log for % change
df2['lnCADUSD'] = np.log(df2['Close'])

# Combine the 2 dfs into a single df
df2['CADUSD'] = df2['Close']
df2['WTI'] = df1['Close']

# Run regression (OLS regression)
result = sm.ols(formula="lnCADUSD ~ WTI", data=df2).fit()
print(result.params)
print(result.summary())
