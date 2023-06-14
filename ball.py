# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:13:46 2023

@author: sherr
"""

def calculate_max_height(v0, g):
    max_height = (v0 ** 2) / (2 * g)
    return max_height

def main():
    v0 = float(input("Enter the initial velocity of the ball (ft/sec): "))
    g = 32.8  # force of gravity in ft/sec^2

    max_height = calculate_max_height(v0, g)

    print("The maximum height reached by the ball is: {:.2f} ft".format(max_height))

if __name__ == '__main__':
    main()
    