#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:26:14 2020

@author: ZainKhawaja
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import numpy as np
import statsmodels.formula.api as sm


#Set graphing parameters.
style.use("ggplot")
start = dt.datetime(2015,1,1)
end = dt.date.today()



df1 = web.get_data_yahoo("SPY", start, end)
df2 = web.get_data_yahoo('DX-Y.NYB', start, end)

#Generate Daily Percent Change
df1['Percent_Change'] = df1['Close'].pct_change()
df2['Percent_Change'] = df2['Close'].pct_change()


#Add daily percent changes using cumsum() function to get percent change over time
df1['Cum_Pct_Change'] = df1['Percent_Change'].cumsum()
df2['Cum_Pct_Change'] = df2['Percent_Change'].cumsum()



plt.plot(df1['Cum_Pct_Change'], label='SPY')
plt.plot(df2['Cum_Pct_Change'], label='USD')


#Drop Unecessary Variables
df1 = df1.drop(['High', 'Low', 'Open', 'Volume', 'Adj Close'], axis=1)
df2 = df2.drop(['High', 'Low', 'Open', 'Volume', 'Adj Close'], axis=1)



#Plot the graphs
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.title(' ')
plt.xlabel("Date")
plt.ylabel("% Return")
plt.show()







