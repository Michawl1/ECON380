#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:15:39 2020

@author: ZainKhawaja
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader as web
import numpy as np

#Set the start and end dates
style.use("ggplot")
start = dt.datetime(2019,6,12)
end = dt.date.today()





df = web.get_data_yahoo('^NDX', start, end)


df.to_csv('msdata.csv')
