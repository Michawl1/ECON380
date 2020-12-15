#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 7. optimization and consumer theory

In this project, you will be practicing on root finding and optimization problems
In addition, you will apply the computational method to solve the utility
maximization problem in economics.

Due Date: Oct 19 11:59 PM
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
from scipy.optimize import minimize


# =============================================================================
# Section 1. Root finding and optimization
# =============================================================================
# 1.1. define the function y = ln(x) + (x-6)^3 - 4x + 30
# hint: you can find the printed equation on Canvas: project 7.
def f(x):
    return np.log(x) + np.power((x - 6), 3) - (4 * x) + 30


# 1.2. plot the function on the domain [1, 12]
x = np.linspace(1, 12, 100)
y = f(x)


def plot_function(x, y):
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    plt.show()


plot_function(x, y)


# 1.3. derive and define the first-order derivative of the function
def fp(x):
    return (1 / x) + (3 * np.power((x - 6), 2)) - 4


# 1.4. plot it on the domain [1, 12]
plot_function(x, fp(x))


# 1.5. Define the Newton-Raphson algorithm (as a function)
def newton_raphson(f, fp, initial_guess, tolerance=1e-9, max_iteration=100):
    """
    This function will apply the Newton-Raphson method to find the root of a given function
    Parameters:
    ------------
    f : function
       The original function we wanted to find roots
    fp : function
        The first order derivative of the original function
    initial_guess: list
        A list of starting points. 
    tolerance : float, optional
        defines how close to zero needs to be
    max_iteration : int
        defines maximum iterations if not converge
    Return:
    roots : list
        a list of roots found
    """
    roots = []
    for x0 in initial_guess:
        x = x0
        fx = f(x)
        fpx = fp(x)
        iteration = 0

        while (abs(f(x)) > tolerance) and (iteration < max_iteration):
            x = x - fx / fpx
            fx = f(x)
            iteration += 1

        if abs(f(x)) < tolerance:
            roots.append(np.round(x, 3))

    return roots


# 1.6.Use the Newton-Raphson algorithm you defined to find the root of the function
# store the result in a list named as res_1

res_1 = newton_raphson(f, fp, x)

# 1.7. use the Newton-Raphson method to find the
# maximum value on the domain [4, 8], name the returned variable as res_2
res_2 = newton_raphson(f, fp, [4, 5, 6, 7, 8])

# 1.8. use the Newton-Raphson method to find the 
# minimum value on the domain [4, 8], name the returned variable as res_3
res_3 = 0

# 1.9. use the scipy.optimize library to 
# (a). find the root of f(x), store the result in variable res_4
res_4 = 0

# (b). find miniumn value of f(x) on the domain [4, 8],
# name the returned var as res_5
res_5 = 0

# (3). find maximum value of f(x) on the domain [4, 8], 
# name the returned var as res_6
res_6 = 0


# =============================================================================
# Section 2. Utiliyt Theory and the Application of Optimization
# =============================================================================

# Consider a utility function over bundles of A (apple) and B (banana)
#  U(B, A) =( B^alpha) * (A^(1-alpha))
# hint: you can find the printed equation on Canvas: project 7.

# 2.1. Define the given utility function
def utility(A, B, alpha):
    return np.power(B, alpha) * np.power(A, (1 - alpha))


# 2.2. Set the parameter alpha = 1/3,
# Assume the consumer always consume 1.5 units of B.
# plot the relationship between A (x-axis) and total utility (y-axis)
# set the range of A between 1 and 10
A = np.linspace(1, 10, 100)


def plot_utility(A, u_level):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(A, u_level)
    ax.set_xlabel("A")
    ax.set_ylabel("u_level")
    plt.show()


# 2.3.  plot the 3-dimensional utility function
# hint: in-class coding practice on Oct 06
# 3-d view of utility
A = np.linspace(1, 10, 100)
B = np.linspace(1, 10, 100).reshape((100, 1))
A, B = np.meshgrid(A, B)
u_level = utility(A, B, 1 / 3)


def plot_utility_3d(A, B, u_level):
    plt.show()


plot_utility_3d(A, B, u_level)

# 2.4.plot the utility curve on a "flatten view"
# hint: in-class coding practice on Oct 06

A = np.linspace(1, 10, 100)
B = np.linspace(1, 10, 100).reshape((100, 1))
u_level = utility(A, B, 1 / 3)


def plot_utility_flat(A, B, u_level):
    plt.show()


plot_utility_flat(A, B, u_level)


# 2.5. from the given utitlity function, derive A as a function of B, alpha, and U
# plot the indifferences curves for u=1 ,3,5,7,9 on the same figure.
# Put B on the x-axis, and A on the y-axis
def A_indifference(B, ubar, alpha=1 / 3):
    None


def plot_indifference_curves(ax, alpha=1 / 3):
    None


# fig, ax = plt.subplots()
# plot_indifference_curves(ax)


# 2.6.suppose pa = 2, pb = 1, Income W = 20, 
# Add the budget constraint to the  previous figure
def A_bc(B, W, pa, pb):
    None


def plot_budget_constraint(ax, W, pa, pb):
    None


# 2.7. find the optimized consumption bundle and maximized utility
def objective(B, W=20, pa=2, pb=1):
    None


res_8 = 0
optimal_B = 0
optimal_A = 0
optimal_U = 0

# 2.8. suppose price of A increased, to pa = 2
# repeat 2.6 and 2.7

res_8 = 0
optimal_B = 0
optimal_A = 0
optimal_U = 0
