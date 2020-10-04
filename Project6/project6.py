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


# =============================================================================
# Section 1. Define classes
# =============================================================================
# 1.1. Define a class "Player". For the player class
# Attribute: endowment. this is the initial endowment of the player
# Methods: 
#   self_introduction(self). Tell other people how much endowmment one has
#   contribute(self). This method defines the players decision making rule.
#   The default rule is to randomly contribute a proportion of endowment.

class Player:
    def __init__(self, _endowment):
        self._endowment = _endowment

    def self_introduction(self):
        return self._endowment

    def contribute(self):
        return self._endowment * random.random()


# 1.2. Define "Free_rider" as a child class of "Player"
# overwrite the contribute method. The free-rider never contribute.
# (optional): introduce some "randomness" to the decision rule
class Free_rider(Player):
    def __init__(self, _endowment):
        super().__init__(_endowment)

    def contribute(self):
        return 0


# 1.3. Define "Strong_cooperator" as a child class of "Player"
# overwrite the contribute method. The strong cooperators always give ALL.
# (optional): introduce some "randomness" to the decision rule
class Strong_cooperator(Player):
    def __init__(self, _endowment):
        super().__init__(_endowment)

    def contribute(self):
        return self._endowment


# 1.4. Define "Conditional_cooperator" as a child class of "Player"
# overwrite the contribute method. The conditional cooperator's contribution 
# depends on how much other people contributed---Their contribution always equal
# to 80% of the average contribution of the previous round.
# In the first round, they contribute as the parent class "Player".
# (optional): introduce some "randomness" to the decision rule
class Conditional_cooperator(Player):
    def __init__(self, _endowment):
        super().__init__(_endowment)
        self._prev_average_contribution = super().contribute()

    def contribute(self):
        return self._prev_average_contribution * 0.8

    def set_prev_average_contribution(self, _prev_average_contribution):
        self._prev_average_contribution = _prev_average_contribution


# =============================================================================
# Section 2. Simulating Social Interaction
# =============================================================================

# Simulate three public goods contribution scenarios.


# 2.1. Scenario One. Interaction among conditional Cooperators
# Simulate a society with 30 conditional cooperator.
# Each person start with 100 points as initial endowment.
# Every round is a new game (i.e., start with another 100 points)
# The game lasts 20 rounds

def make_free_riders(num):
    free_riders = []
    for i in range(0, num):
        free_riders.append(Free_rider(100))

    return free_riders


def make_strong_cooperators(num):
    strong_cooperators = []
    for i in range(0, num):
        strong_cooperators.append(Strong_cooperator(100))

    return strong_cooperators


def make_conditional_cooperators(num):
    conditional_cooperators = []
    for i in range(0, num):
        conditional_cooperators.append(Conditional_cooperator(100))

    return conditional_cooperators


def experiment(_society, _num_periods):
    contributions = []

    for i in range(0, _num_periods):
        contribution_total = 0
        for member in _society:
            contribution_total += member.contribute()

        average_amount = (contribution_total / _num_periods)

        for member in _society:
            try:
                member.set_prev_average_contribution(average_amount)
            except AttributeError:
                None
        contributions.append(average_amount * 2)

    return contributions


society1 = make_conditional_cooperators(30)
result1 = experiment(society1, 20)

society2 = make_conditional_cooperators(28) + make_free_riders(2)
result2 = experiment(society2, 20)

society3 = make_conditional_cooperators(28) + make_strong_cooperators(2)
result3 = experiment(society3, 20)


# 2.2. Scenario Two. Interaction with free riders
# repeat Scenario 1 with 2 free-riders, and 28 conditional cooperators

# 2.3. Scenario Three. Different starting point.
# repeat Scenario 1 with 2 strong cooperators, and 28 conditional cooperators


# =============================================================================
# Section 3. Result visualization and interpretation
# =============================================================================
# 3.1 visualize the simulation results by ploting the average contribution 
# overtime (Three scenarios on the same figure). 


def plot_avg_contribution(outcome1, outcome2, outcome3):
    iterations = np.linspace(1, len(outcome1), num=len(outcome1))
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(iterations, outcome1, label="outcome 1", color='b')
    ax.plot(iterations, outcome2, label="outcome 2", color='r')
    ax.plot(iterations, outcome3, label="outcome 3", color='g')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Average Contribution')
    plt.legend()
    plt.show()


plot_avg_contribution(
    result1,
    result2,
    result3)

"""
3.2. Compare the results of Scenario 2 to Scenario 1, what is the net loss in 
total social welfare (percentage change)?
* Show your calculation and results below.
"""


def diff(_result1, _result2):
    diff = []
    for i in range(0, len(_result1)):
        diff.append(_result1[i] / _result2[i] * 100)
    return diff


iterations = np.linspace(1, len(result1), num=len(result1))
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
ax.plot(iterations, diff(result1, result2), label="difference in social welfare by percent", color='b')
ax.set_xlabel('Iterations')
ax.set_ylabel('Average Contribution Difference by Percent')
plt.legend()
plt.show()

"""
3.3. Compare the results of Scenario 3 to Scenario 1, what is the net gain in 
total social welfare (percentage change)?
* Show your calculation and results below
"""
iterations = np.linspace(1, len(result1), num=len(result1))
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
ax.plot(iterations, diff(result1, result3), label="difference in social welfare by percent", color='b')
ax.set_xlabel('Iterations')
ax.set_ylabel('Average Contribution Difference by Percent')
plt.legend()
plt.show()

# =============================================================================
# Section 4 (optional). Think about what decision rule(s) you used during the
# experiment (I guess it would be much complex than the above ones). Add yourself
# into the "society" in scenario one, and use simulation method to figure out

# (1). What your total earnings would be?
# (2). Can you influencing the group outcome?
