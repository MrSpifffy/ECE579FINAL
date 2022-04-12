# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:45:31 2022

@author: khenn
"""

class Bottle:
    def __init__(self, composition, capacity):
        # Composition (String): glass or plastic
        # Capacity (Int): 4 or 6 gallons
        self.composition = composition
        self.capacity = capacity
        
    def show(self):
        print("Type:", self.composition)
        print("Capacity:", self.capacity)