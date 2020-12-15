# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:45:34 2020

@author: Yash
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Import dataset 
data = pd.read_excel(r'Dot_Com_Bubble.xlsx')  # change
pd.set_option("display.precision", 2)
event = "Housing Crisis"  # change

# Find peak in dataset 
max_index = np.argmax(data.VIX)

# Divide dataset into runup and recovery
# Runup 
runup = data.VIX[:max_index + 1].to_numpy()  # converts to numpy array
runup_length = len(runup)  # Length of runup
runup_days = np.linspace(1, runup_length, num=runup_length)  # x-data

# Recovery
recovery = data.VIX[max_index:].to_numpy()  # converts to numpy array
recovery_length = len(recovery)  # Length of recovery
recovery_days = np.linspace(1, recovery_length, num=recovery_length)  # y-data

# Transformation Fit for Initial Guess 
# Unweighted linear regression fit after transformation 
# Runup
trans_fit_param_run = np.polyfit(runup_days, np.log(runup), 1)
param_trans_run = np.exp(trans_fit_param_run[1]), trans_fit_param_run[0]

# Recovery
trans_fit_param_rec = np.polyfit(recovery_days, np.log(recovery), 1)
param_trans_rec = np.exp(trans_fit_param_rec[1]), trans_fit_param_rec[0]


# Define exponential function
def exponential(x, a, b):
    return a * np.exp(b * x)


# Exponential Fit
# Uses curve fit to fix an exponential 
# Using the transformation fit parameters as initial guess
# Runup
param_exp_run, cov_run = curve_fit(f=exponential, xdata=runup_days, ydata=runup, p0=param_trans_run)
stdevs_param_run = np.sqrt(np.diag(cov_run))

# Recovery
param_exp_rec, cov_rec = curve_fit(f=exponential, xdata=recovery_days, ydata=recovery, p0=param_trans_rec)
stdevs_param_rec = np.sqrt(np.diag(cov_rec))


# Calculate R-squared Function
def r_squared(xdata, ydata, params):
    residuals = ydata - exponential(xdata, *params)
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
    r_sq = 1 - (ss_res / ss_tot)
    return r_sq


# R-Squares for Fits
# Runup
rsq_run_fit1 = r_squared(runup_days, runup, param_trans_run)
rsq_run_fit2 = r_squared(runup_days, runup, param_exp_run)

if rsq_run_fit2 > rsq_run_fit1:
    print("For the run-up, the exponential curve fit was better than the transformed fit.")
else:
    print("For the run-up, the transformed fit was better than the exponential curve fit.")

# Recovery
rsq_rec_fit1 = r_squared(recovery_days, recovery, param_trans_rec)
rsq_rec_fit2 = r_squared(recovery_days, recovery, param_exp_rec)

if rsq_rec_fit2 > rsq_rec_fit1:
    print("For recovery, the exponential curve fit was better than the transformed fit.")
else:
    print("For recovery, the transformed fit was better than the exponential curve fit.")


# Plotting Fits
def plot_fits(xdata, ydata, param_fit1, param_fit2, cat):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(xdata, ydata)  # Plot VIX data
    ax.plot(exponential(xdata, *param_fit1), label='Transformed Fit', color='r')  # Plot transformed fit
    ax.plot(exponential(xdata, *param_fit2), label='Exponential Fit', color='g')  # Plot exponential fit
    ax.set_title(cat + event)
    ax.set_xlabel("Days")
    ax.set_ylabel("VIX")
    plt.legend()
    plt.show()


# Plotting Residuals
def plot_residuals(xdata, ydata, param_fit, cat):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(1, 1, 1)
    residuals = ydata - exponential(xdata, *param_fit)
    ax.scatter(xdata, residuals)
    ax.set_title("Residuals of " + cat)
    ax.set_xlabel("Days")
    ax.set_ylabel("Residuals")
    plt.show()


# Runup 
plot_fits(runup_days, runup, param_trans_run, param_exp_run, "Run-up of ")
plot_residuals(runup_days, runup, param_exp_run, "Run-up")
print(("For run-up, the growth parameter was {:.4f} \u00B1 {:.4f}, and the R-squared was {:.3f}.").format(
    param_exp_run[1], stdevs_param_run[1], rsq_run_fit2, ))

# Recovery
plot_fits(recovery_days, recovery, param_trans_rec, param_exp_rec, "Recovery of ")
plot_residuals(recovery_days, recovery, param_exp_rec, "Recovery")
print(("For recovery, the decay parameter was {:.5f} \u00B1 {:.5f}, and the R-squared was {:.3f}.").format(
    param_exp_rec[1], stdevs_param_rec[1], rsq_rec_fit2, ))
