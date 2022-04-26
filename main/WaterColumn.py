# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:27:58 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""
import copy

class WaterColumn:
    def __init__(self, bottle):
        # We can make stand a trait instead of a type, I just though inheritance might be the way to go for identification
        self.bottle = bottle
        
    def getBottle(self):
        # Do Something
        return self.bottle
    
    def getBottleType(self):
        bott = copy.copy(self.bottle)
        return bott

    def setBottle(self, newBottle):
        self.bottle = newBottle
        
class Chilled(WaterColumn):
    def __init__(self, bottle):
        self.temperature = 42
        self.type = 'Chilled'
        super(Chilled, self).__init__(bottle)
    
    def getTemp(self):
        return round(self.temperature, 2)
    
    def setTemp(self, temp):
        self.temperature = temp

    def getType(self):
        return self.type
    
    def status(self):
        # Do Something
        self.bottle.show()
        print("Temperature:", self.temp())

class Regular(WaterColumn):
    def __init__(self, bottle):
        self.type = 'Regular'
        super(Regular, self).__init__(bottle)
    
    def getType(self):
        return self.type
    
        
        
