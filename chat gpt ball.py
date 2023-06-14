# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:28:42 2023

@author: King Vann
"""

def calculate_max_height(v0, g):
    # Calculate the time taken to reach the highest point
    t = v0 / g
    
    # Calculate the maximum height using the formula h = v0 * t - 0.5 * g * t^2
    h = v0 * t - 0.5 * g * t ** 2
    
    return h

# Get the inputs from the user
v0 = 50  # Initial velocity of the ball in ft/sec
g = 32.8  # force of gravity in ft/sec^2

# Calculate the maximum height
max_height = calculate_max_height(v0, g)

print("The maximum height reached by the ball is", max_height, "ft.")
