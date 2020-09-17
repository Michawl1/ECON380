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
od_matrix = np.random.randint(1000, 3000)

'''
#1.4 same modal share across all regione (1)
alpha_vec = np.full(len(n_j),1) 
#1.5 same transmission rate across all regions
beta_vec = 
#1.6 same recover rate  across all regions
gamma_vec = 
#1.7 normal o-d flow
od_flow = 
#1.8 Have 300 iterations
days = 300



#=============================================================================
#Section 2. define the initial status table
#=============================================================================
# assume in the beginning, no recover or died yet, 
# infected proportion in areas are:
# areaA: 1%; areaB: 0.5%; areaC:0.1%; arerD:0%, areaE:0%

def start_detect(n_j,detect,immune):
    sir = np.zeros(shape=(5, 4))  

    return sir
sir = start_detect()


#=============================================================================
#Section 3. Define a function to simulate the epidemic in this big region
#=============================================================================
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

def epidemic_sim(n_j, initial_status,od_flow, 
                 alpha_vec,beta_vec,fatality_vec,gamma_vec,days):
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
     
    #3.1 make copy of the initial sir table
    sir_sim = 

    #3.2 create empty list to keep tracking the changes
    susceptible_pop_norm = []
    infected_pop_norm = []
    recovered_pop_norm = []
    dead_pop_norm = []
    
    #3.3. use total_days as the interator
    total_days = 
    for day in total_days:
        
        ##3.4 figure out where those infected people go
        
        # normalize the sir table by calculating the percentage of each group
   
        # assuming the infected people travel to all ares with the same probability:  

        # od_infected gives the flow of infected people. i.e., where they go         


        # "inflow infected" are those who will spread the disease to susceptible    
        inflow_infected =  # total infected inflow in each area
        inflow_infected =  # consider population density

        #3.5 calculate new_infect    
        new_infect = 
 
        #3.6 set upper limit of the infected group (total susceptible)          
        new_infect = 
    
        #3.7 calculate total number of people recovered        
        new_recovered = 

    
        
        #3.8 remove new infections from susceptible group      


        #3.9 add new infections into infected group, 
        # also remove recovers from the infected group


        #3.10 add recovers to the recover group       



        #3.11 set lower limits of the groups (0 people)        
        sir_sim = np.where(sir_sim<0,0,sir_sim)

                 
        #3.12 compute the normalized SIR matrix on aggregate level
        region_sum = sir_sim.sum(axis=0)


        
    return [infected_pop_norm, susceptible_pop_norm, recovered_pop_norm,
            dead_pop_norm]





#3.13 call the function to simulate the epidemic
outcome = epidemic_sim(n_j,sir,od_flow, alpha_vec,beta_vec,fatality_vec,
                        gamma_vec,days=days)

#=============================================================================
#Section 4. define a function to visualize the simulation result
#=============================================================================
def sir_simulation_plot(outcome,days):
    fig = plt.figure(figsize=(10,8))

sir_simulation_plot(outcome,days=days)

#=============================================================================
#Section 5. Policy evaluation
#=============================================================================
# Using the simulation model to evaluate the following policy targets
# Visualize the results, organize the plots in a 2x2 figure, each outcome on 
# one subplot.

#Policy 1. do nothing (this should have been done in )
#Policy 2. reduce the o-d flow by 50%, all other arguments stay unchanged
#Policy 3. reduce the o-d flow by 80%, all other arguments stay unchanged
#Policy 4. reduce the o-d flow by 80%, reduce beta by 50%, all other the same
'''
