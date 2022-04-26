# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:45:31 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""

class Customer:
        def __init__(self, name, distance, waterColumn, robot) -> None:
            self.name = name
            self.distance = distance
            self.waterColumn = waterColumn
            self.fullBottleShelf = []
            self.emptyBottleShelf = []
            self.robot = robot
            pass

        def getFullBottleShelf(self):
            return self.fullBottleShelf
        
        def setFullBottleShelf(self, shelf):
            self.fullBottleShelf = shelf

        def addFullBottle(self, bott):
            self.fullBottleShelf.append(bott)

        def getEmptyBottleShelf(self):
            return self.emptyBottleShelf
        
        def setEmptyBottleShelf(self, shelf):
            self.emptyBottleShelf = shelf

        def addEmptyBottle(self, bott):
            self.emptyBottleShelf.append(bott)

        def getWaterColumn(self):
            return self.waterColumn
        
        def getName(self):
            return self.name
        
        def getRobot(self):
            return self.robot