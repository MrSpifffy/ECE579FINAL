# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:45:31 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""

class Bottle:
    def __init__(self, composition, capacity):
        # Composition (String): glass or plastic
        # Capacity (Int): 4 or 6 gallons
        self.composition = composition
        self.capacity = capacity
        self.level = 0

    def getWaterLevel(self):
        return round(self.level, 1)

    def setWaterLevel(self, newLevel):
        self.level = newLevel

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, capacity):
        self.level = capacity

    def getType(self):
        return self.composition
        
    def show(self):
        print("Type: ", self.composition)
        print("Capacity: ", self.capacity)
        print("Level: ", self.level)