#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weekly project 2. The Gale-Shapley algorithm
Due on: September 07, 11:59 PM
"""


def get_best_guy(galpreference, new_guy, old_guy):
    for guy in galpreference:
        if guy is new_guy:
            return new_guy, old_guy
        elif guy is old_guy:
            return old_guy, new_guy
        return None, None


# Section 1. Preparation
# 1-1. import all the necessary python modules
import json

# 1-2. import the datasets
with open('project2_data.json') as f:
    json_data = json.load(f)

# Section 2 Extract information from the dataset, 
# 2-1. create a dictionary 'guyprefer' contains mens' preferences
guyprefers = json_data['men_preference']

# 2-2. create a dictionary 'galprefer' contains women's preferences
galprefers = json_data['women_preference']

# 2-3. create a list contains guys who are currently not engaged, 
# sort alphabetically
free_guy = list(guyprefers)
free_guy.sort()

# 2-4. generate an empty dictionary 'engage_book' to store result
engage_book = {}

# 2-5. make copies of guyprefers and gal refers
guypreference = guyprefers.copy()
galpreference = galprefers.copy()

# Section 3. Impletement the Gale-Shapley algorithm
# Follow the algorithm flowchart, it should be very helpful

while free_guy:
    # pop the first guy in the free_guy list, let him take the move
    a_brave_guy = free_guy.pop(0)
    # get his preference list
    mylist = guypreference[a_brave_guy].copy()
    # let this guy take the move
    while mylist:
        # Let's propose to my favorate lady!
        my_girl = mylist.pop(0)
        # YOU WILL NEED TO DO THE REST, GOOD LUCK AND HAVE FUN!.

        if engage_book.__contains__(my_girl):
            favorite_guy, not_favorite_guy = get_best_guy(galpreference[my_girl], a_brave_guy, engage_book[my_girl])
            if favorite_guy is not None:
                engage_book[my_girl] = favorite_guy
                free_guy.append(not_favorite_guy)
        else:
            engage_book[my_girl] = a_brave_guy
            break

print(engage_book)
# Section 4 (optional). Stability check
# define stability: there are no two people of opposite sex who would both
# rather have each other than their current partners.
