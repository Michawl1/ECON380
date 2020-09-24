#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 5. In this project, you will apply Object Oriented Programming to 
simulate the market demand/supply model.

Due on: September 28 2020. 11:59 PM

"""
import 

random.seed(380)
#=============================================================================
# Section 1. Define classes
#=============================================================================
# 1.1. define a class Econ_agent
# attributes: id_number, budget
# methods: introduce_me(self):
# print out agent's id number and budget in sentences.


class Econ_agent:

    def __init__(self, id_number, budget):

    def introduce_me(self):


# 1.2 define  "Consumer" as a child class of Econ_agent;
# 1.2.1 the Consumer class inherits all attributes and methods from Econ_agent;
# 1.2.2 additional attributes:
    # (1) 'preference', indicates how much the consumer like the product
    # 0 means does not like at all, 1 means wiling to spend whole budget on it
    
    # (2).  wtp (i.e.,willingness to pay). 
    # the wtp is the product of budget and preference
    
# 1.2.3 additional methods:
    #buying(self,price)
    # the buying method defines the consumer's purchasing decision
    # it takes two parameter, the first one is self, the second one is 'price'
    # when wtp is smaller than price, the consumer won't buy 
    # when wtp is greater or equal to price, the consumer will buy 1 unit.
    # the buying method returns if the consumer decide to buy.


class Consumer(Econ_agent):


# 1.3 define "Producer" as a child class of Econ_agent;
# 1.3.1 the Producer class inherits all attributes and methods from Econ_agent;
# 1.3.2 additional attributes:
    # 1. 'opp_cost', indicate the opp_cost of producing and selling one unit
    # assume opp_cost is a constant for each producer.
# 1.3.3. additional methods:
    # selling(self,price)
    # the selling method defines the producer's decision
    # it takes two parameter, the first one is self, the second one is 'price'
    #when opp_cost is greater than price, the producer won't produce 
    # when opp_cost or equal to price, the consumer will produce 
    # the quantity supplied depends on the ratio between the producer's budget 
    # and the the opp_cost. i.e., quantity supplied = budget/opp_cost
    # the method returns total amount a producer made.


class Producer(Econ_agent):
    

#=============================================================================
# Section2. generate objects
#=============================================================================
# 2.1 generate a list of 200 consumer
# each has a unique id number
# budget is determined by a random draw from a normal distribution
#   set the normal distribution mean = 500, s.d. = 100
# preference is determined by a random draw from a uniform distribution [0,1]
consumers = []

#2.2 generate a list of 200 producers
# each has a unique id number
# budget is determined by a random draw from a UNIFORM distribution [10,800]
# opp_cost is determined by  a drandom draw from uniform distribution [100,200]
producers = [] 

#=============================================================================
# Section 3. Simulate the market mechanism, and find the equilibrium
#=============================================================================

# Specifically, find the market equilibrium price and quantity (i.e., you 
# may not be able to find a point where  Q = S exactly. Let's consider the 
# market is in equilibrium as long as the difference between D and S is smaller 
# than 5 units)

# Hint: you will need to think the process through before coding.

while abs(total_demand -total_supply)>5:

#=============================================================================
# Section4. Define the demand curve and supply curve 
#=============================================================================
# 4.1. Define the demand curve when price ranging from 100 to 200
def demand():

# 4.2. Define the supply curve when price ranging from 100 to 200
def supply():


# 4.3 visualize the demand and supply, see if it makes sense.


#=============================================================================
# Section 5. Changes in supply
#=============================================================================
# imagine there is a technology improvement, reduce the average opp_cost by 10%
# run a simulation to find the new market equilibrium
# visualize the change graphically 


#=============================================================================
# Section 6 (OPTIONAL). Is the demand elastic or inelastic? 
#=============================================================================
"""
Which line (or lines) of code determined this outcome? Explain your answer with 
Economic intuition. Type in your answer below.


Your answer:

    

"""