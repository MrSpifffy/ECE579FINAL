# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:38:02 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""

class Robot:
    def __init__(self, location):
        self.location = location
        self.bottle = None

    def getLocation(self):
        return self.location
    
    def setLocation(self, local):
        self.location = local
        
    def pickup(self, bott):
        self.bottle = bott #puts bottle in Robot's hand

    def putdown(self):
        bot = self.bottle
        self.bottle = None
        return bot #puts bottle down, removes bottle from Robot's hand
    
    def stack(self, shelf):
        shelf.append(self.bottle) #add bottle to the top of the stack
        self.bottle = None #Remove bottle from Robot's hand
        return shelf

    def unstack(self, shelf):
        self.bottle = shelf[-1] #gets the top bottle from shelf, puts in Robot's hand
        shelf.pop() #remove top bottle on shelf
        return shelf    
        