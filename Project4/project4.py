#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is an example of virus epidemic
"""

import numpy as np
import matplotlib.pyplot as plt

### beta and gamma are the same as last week


# =============================================================================
# Section 1. set the model parameters
# =============================================================================
# 1.1 set the random seed to 380 (pseudo randomness)
np.random.seed(380)  # DO NOT CHANGE THE SEED

# 1.2 create a population vector with five areas, population in areas are:
# areaA: 18000. areaB: 22000, areaC:50100,areaD,21010, areaE:25000
n_j = np.array([18000, 22000, 50100, 21010, 25000])

# 1.3 use the random integer generation function in numpy to create a 5 x 5
# Origination-Destination flow matrix
# Set the lower limit to 1000, upper limit to 3,000
od_matrix = np.random.randint(1000, 3001, (5, 5))
# 1.4 same modal share across all regions (1)
alpha_vec = np.full(len(n_j), 1)
# 1.5 same transmission rate across all regions
beta_vec = np.full(len(n_j), 0.8)
# 1.6 same recover rate  across all regions
gamma_vec = np.full(len(n_j), 0.05)
# 1.7 normal o-d flow
od_flow = 1
# 1.8 Have 300 iterations
days = 300

fatality_vec = np.zeros(5)


# =============================================================================
# Section 2. define the initial status table
# =============================================================================
# assume in the beginning, no recover or died yet, 
# infected proportion in areas are:
# areaA: 1%; areaB: 0.5%; areaC:0.1%; arerD:0%, areaE:0%

def start_detect(n_j, infected, immune):
    sir = np.zeros(shape=(3, 5))

    for i in range(0, n_j.size):
        sir[1][i] = infected[i] * n_j[i]
        sir[0][i] = n_j[i] - sir[1][i]
        sir[2][i] = immune[i]

    return sir


sir = start_detect(n_j, [0.01, 0.005, 0.01, 0, 0], [0, 0, 0, 0, 0])

# =============================================================================
# Section 3. Define a function to simulate the epidemic in this big region
# =============================================================================
# function input should include:
# n_j:              population vector
# initial status:   the initial status of the epidemic
# od_flow:          the 5 x 5 o-d matrix
# alpha_vec:        population density in each region
# beta_vec:         transmission rate in each region
# gamma_vec:        daily recover rate in each region
# days: total       iterations

# function return:
# susceptible_pop_norm: changes in the proportion of S group (aggregated)
# infected_pop_norm: changes in the proportion of  I group (aggregated)
# recovered_pop_norm: changes in the proportion of R group (aggregated)

def epidemic_sim(n_j, initial_status, od_flow,
                 alpha_vec, beta_vec, fatality_vec, gamma_vec, days):
    """
    Parameters
    ----------
    n_j : 5 x1 array
        total population in each area.
    initial_status : 5 x 3 array
        initial status
    alpha : 5 x 1 array
        modal share in each area
    beta : 5 x 1 array
        transmission rate in each area
    fatality: 5 x 1 array 
        daily fatality rate in each area
    gamma : 5 x 1 array
        recover rage in each area
    days: int
        total iterations

    Returns
    -------
    infected_pop_norm : List
        DESCRIPTION.
    susceptible_pop_norm : List
        DESCRIPTION.
    recovered_pop_norm : List
        DESCRIPTION.

    """

    # 3.1 make copy of the initial sir table
    sir_sim = initial_status.copy()

    # 3.2 create empty list to keep tracking the changes
    susceptible_pop_norm = []
    infected_pop_norm = []
    recovered_pop_norm = []
    dead_pop_norm = []

    # 3.3. use total_days as the iterator
    for j in range(0, days):
        s = []
        inf = []
        r = []
        d = []

        for i in range(0, n_j.size):
            new_infect = sir_sim[0, i] * beta_vec[i]
            if new_infect > sir_sim[0, i]:
                new_infect = sir_sim[0, i]

            new_recovered = sir_sim[1, i] * gamma_vec[i]
            sir_sim[0, i] -= new_infect
            sir_sim[1, i] += new_infect
            sir_sim[1, i] = sir_sim[0, 1] - new_recovered

            sir_sim[2, i] += new_recovered
            if sir_sim[0, i] < 0:
                sir_sim[0, i] = 0
            if sir_sim[1, i] < 0:
                sir_sim[1, i] = 0
            if sir_sim[2, i] < 0:
                sir_sim[2, i] = 0

            s.append(sir_sim[0, i] / n_j[i])
            inf.append(sir_sim[1, i] / n_j[i])
            r.append(sir_sim[2, i] / n_j[i])
            d.append(0)

        susceptible_pop_norm.append(sum(s) / len(s))
        infected_pop_norm.append(sum(inf) / len(inf))
        recovered_pop_norm.append(sum(r) / len(r))
        dead_pop_norm.append(sum(d) / len(d))


    return [susceptible_pop_norm, infected_pop_norm, recovered_pop_norm,
            dead_pop_norm]


# 3.13 call the function to simulate the epidemic
outcome = epidemic_sim(n_j, sir, od_flow, alpha_vec, beta_vec, fatality_vec,
                       gamma_vec, days=days)


# =============================================================================
# Section 4. define a function to visualize the simulation result
# =============================================================================
def sir_simulation_plot(outcome, days):
    fig = plt.figure(figsize=(10, 8))

    ax = fig.add_subplot(1, 1, 1)
    days = np.linspace(1, days, num=days)
    susceptible = np.array(outcome[0]) * 100
    infected = np.array(outcome[1]) * 100
    recovered = np.array(outcome[2]) * 100
    dead = np.array(outcome[3]) * 100
    ax.plot(days, susceptible, label='susceptible', color='y')
    ax.plot(days, infected, label='infected', color='r')
    ax.plot(days, recovered, label='recovered', color='g')
    ax.plot(days, dead, label='dead', color='b')
    ax.set_xlabel('Days')
    ax.set_ylabel('Proportion of the population')
    ax.set_title("SIR Model Simulation")

    plt.legend()
    plt.show()


sir_simulation_plot(outcome, days)

# =============================================================================
# Section 5. Policy evaluation
# =============================================================================
# Using the simulation model to evaluate the following policy targets
# Visualize the results, organize the plots in a 2x2 figure, each outcome on 
# one subplot.

# Policy 1. do nothing (this should have been done in )
# Policy 2. reduce the o-d flow by 50%, all other arguments stay unchanged
# Policy 3. reduce the o-d flow by 80%, all other arguments stay unchanged
# Policy 4. reduce the o-d flow by 80%, reduce beta by 50%, all other the same

outcome1 = epidemic_sim(n_j, sir, od_flow, alpha_vec, beta_vec, fatality_vec,
                       gamma_vec, days=days)
outcome2 = epidemic_sim(n_j, sir, 0.5, alpha_vec, beta_vec, fatality_vec,
                       gamma_vec, days=days)
outcome3 = epidemic_sim(n_j, sir, 0.8, alpha_vec, beta_vec, fatality_vec,
                       gamma_vec, days=days)
outcome4 = epidemic_sim(n_j, sir, 0.8, alpha_vec, np.full(len(n_j), 0.4), fatality_vec,
                       gamma_vec, days=days)

fig, axs = plt.subplots(2, 2)

days = np.linspace(1, days, num=days)
susceptible = np.array(outcome1[0]) * 100
infected = np.array(outcome1[1]) * 100
recovered = np.array(outcome1[2]) * 100
dead = np.array(outcome1[3]) * 100
axs[0, 0].plot(days, susceptible, label='susceptible', color='y')
axs[0, 0].plot(days, infected, label='infected', color='r')
axs[0, 0].plot(days, recovered, label='recovered', color='g')
axs[0, 0].plot(days, dead, label='dead', color='b')
axs[0, 0].set_xlabel('Days')
axs[0, 0].set_ylabel('Proportion of the population')
axs[0, 0].set_title("SIR Model Simulation")

susceptible = np.array(outcome2[0]) * 100
infected = np.array(outcome2[1]) * 100
recovered = np.array(outcome2[2]) * 100
dead = np.array(outcome2[3]) * 100
axs[1, 0].plot(days, susceptible, label='susceptible', color='y')
axs[1, 0].plot(days, infected, label='infected', color='r')
axs[1, 0].plot(days, recovered, label='recovered', color='g')
axs[1, 0].plot(days, dead, label='dead', color='b')
axs[1, 0].set_xlabel('Days')
axs[1, 0].set_ylabel('Proportion of the population')
axs[1, 0].set_title("SIR Model Simulation")

susceptible = np.array(outcome3[0]) * 100
infected = np.array(outcome3[1]) * 100
recovered = np.array(outcome3[2]) * 100
dead = np.array(outcome3[3]) * 100
axs[0, 1].plot(days, susceptible, label='susceptible', color='y')
axs[0, 1].plot(days, infected, label='infected', color='r')
axs[0, 1].plot(days, recovered, label='recovered', color='g')
axs[0, 1].plot(days, dead, label='dead', color='b')
axs[0, 1].set_xlabel('Days')
axs[0, 1].set_ylabel('Proportion of the population')
axs[0, 1].set_title("SIR Model Simulation")

susceptible = np.array(outcome4[0]) * 100
infected = np.array(outcome4[1]) * 100
recovered = np.array(outcome4[2]) * 100
dead = np.array(outcome4[3]) * 100
axs[1, 1].plot(days, susceptible, label='susceptible', color='y')
axs[1, 1].plot(days, infected, label='infected', color='r')
axs[1, 1].plot(days, recovered, label='recovered', color='g')
axs[1, 1].plot(days, dead, label='dead', color='b')
axs[1, 1].set_xlabel('Days')
axs[1, 1].set_ylabel('Proportion of the population')
axs[1, 1].set_title("SIR Model Simulation")

plt.show()