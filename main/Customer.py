# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:45:31 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""

class Customer:
        def __init__(self, distance, waterColumn, robot) -> None:
            self.name = ''
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
        
        def setName(self, nameVal):
            if(nameVal == 0):
                self.name = 'A'
            elif(nameVal == 1):
                self.name = 'B'
            elif(nameVal == 2):
                self.name = 'C'
            elif(nameVal == 3):
                self.name = 'D'
            elif(nameVal == 4):
                self.name = 'E'
           
        
        def getRobot(self):
            return self.robot