# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:10:51 2022

@author: khenn
"""
from WaterColumn import Chilled, Regular
from Bottle import Bottle
from Robot import Robot
from Shelf import Shelf

# MAIN #
C = Chilled(Bottle("glass", 4), 42)
C.status()
