# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:17:23 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""

class Shelf:
    def __init__(self):
        self.bottles = []
        
    def addBottles(self, bottle):
        self.bottles.append(bottle)