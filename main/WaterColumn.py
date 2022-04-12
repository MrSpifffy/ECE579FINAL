# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:27:58 2022

@author: khenn
"""


class WaterColumn:
    def __init__(self, bottle):
        # We can make stand a trait instead of a type, I just though inheritance might be the way to go for identification
        self.bottle = bottle;
        
    def status(self):
        # Do Something
        self.bottle.show()
        
class Chilled(WaterColumn):
    def __init__(self, bottle, temperature):
        self.temperature = temperature
        super(Chilled, self).__init__(bottle)
    
    def temp(self):
        return self.temperature
    
    def status(self):
        # Do Something
        self.bottle.show()
        print("Temperature:", self.temp())

class Regular(WaterColumn):
    def __init__(self, bottle):
        super(Chilled, self).__init__(bottle)
    
        
        
