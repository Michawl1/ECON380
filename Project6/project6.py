#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 6. In this project, you will use Agent-based modeling to simulate 
people's cooperation decision and the consequence of social interactions. 
In particular. We will replicate the in-class experiment we did on Septembe 29th. 

Very Briefly:

• In this experiment, we will play a “matching fund game”.
 Each of you start with X points as initial endowment.

• You can contribute any amount from 0 to X to a “fund pool”. 
I will double the total contributions to this fund.

• I will then divide the doubled amount equally among all the players 
regardless of their contribution.

Due: October 5th 11:59 PM
    
"""

import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(380)

#=============================================================================
# Section 1. Define classes
#=============================================================================
# 1.1. Define a class "Player". For the player class
# Attribute: endowment. this is the initial endowment of the player
# Methods: 
#   self_introduction(self). Tell other people how much endowmment one has
#   contribute(self). This method defines the players decision making rule.
#   The default rule is to randomly contribute a proportion of endowment.

class Player:

       
# 1.2. Define "Free_rider" as a child class of "Player"
# overwrite the contribute method. The free-rider never contribute.
# (optional): introduce some "randomness" to the decision rule
class Free_rider(Player):

# 1.3. Define "Strong_cooperator" as a child class of "Player"
# overwrite the contribute method. The strong cooperators always give ALL.
# (optional): introduce some "randomness" to the decision rule
class Strong_cooperator(Player):


# 1.4. Define "Conditional_cooperator" as a child class of "Player"
# overwrite the contribute method. The conditional cooperator's contribution 
# depends on how much other people contributed---Their contribution always equal
# to 80% of the average contribution of the previous round.
# In the first round, they contribute as the parent class "Player".
# (optional): introduce some "randomness" to the decision rule
class Conditional_cooperator(Player):


#=============================================================================
# Section 2. Simulating Social Interaction
#=============================================================================

# Simulate three public goods contribution scenarios.


# 2.1. Scenario One. Interaction among conditional Cooperators
# Simulate a society with 30 conditional cooperator.
# Each person start with 100 points as initial endowment.
# Every round is a new game (i.e., start with another 100 points)
# The game lasts 20 rounds

free_riders = []
for i in range():
    free_riders.append(Free_rider())

strong_cooperators = []
for i in range():
    strong_cooperators.append(Strong_cooperator())

conditional_cooperators = []
for i in range():
    conditional_cooperators.append())

society = free_riders + strong_cooperators + conditional_cooperators


def experiment(society,num_periods):

# 2.2. Scenario Two. Interaction with free riders
# repeat Scenario 1 with 2 free-riders, and 28 conditional cooperators

# 2.3. Scenario Three. Different starting point.
# repeat Scenario 1 with 2 strong cooperators, and 28 conditional cooperators


#=============================================================================
# Section 3. Result visualization and interpretation
#=============================================================================
# 3.1 visualize the simulation results by ploting the average contribution 
# overtime (Three scenarios on the same figure). 


def plot_avg_contribution(outcome1, outcome2, outcome3):


"""
3.2. Compare the results of Scenario 2 to Scenario 1, what is the net loss in 
total social welfare (percentage change)?
* Show your calculation and results below.
"""


"""
3.3. Compare the results of Scenario 3 to Scenario 1, what is the net gain in 
total social welfare (percentage change)?
* Show your calculation and results below
"""


#=============================================================================
#Section 4 (optional). Think about what decision rule(s) you used during the 
#experiment (I guess it would be much complex than the above ones). Add yourself 
#into the "society" in scenario one, and use simulation method to figure out 

#(1). What your total earnings would be?
#(2). Can you influencing the group outcome?