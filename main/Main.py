# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:10:51 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""
import array
import copy
from multiprocessing.pool import TERMINATE
import random

from WaterColumn import Chilled, Regular
from Bottle import Bottle
from Robot import Robot
from Shelf import Shelf
from Customer import Customer

customers = [None] * 5
dayCycle = ''

def initializeCustomers(customers):
    customers[0] = Customer('A', 0, Chilled(Bottle('glass', 6)), Robot("Fixed"))
    customers[1] = Customer('B', 0, Regular(Bottle('plastic', 6)), Robot("Mobile"))
    customers[2] = Customer('C', 0, Regular(Bottle('plastic', 4)), Robot("Mobile"))
    customers[3] = Customer('D', 0, Chilled(Bottle('plastic', 6)), Robot("Fixed"))
    customers[4] = Customer('E', 0, Regular(Bottle('glass', 4)), Robot("Mobile"))

    for c in customers:
        newBottle = c.getWaterColumn().getBottleType()
        if(newBottle.getCapacity() == 6):
            newBottle.setWaterLevel(6)
        else:
            newBottle.setWaterLevel(4)

        newBottle2 = copy.copy(newBottle)
        c.addFullBottle(newBottle) #Start with 1 bottle in waterColumn and 2 in full shelf, none in empty shelf
        c.addFullBottle(newBottle2)

        correctInput = False
        while (correctInput == False):
            val = input("Please enter a distance (1-100) for Customer " + c.name + ": \n")

            try:
                num = int(val)
                
                if (num > 0 and num <= 100):
                    c.distance = num
                    correctInput = True
                else:
                    print("Invalid distance input, try again.\n")
                    correctInput = False

            except ValueError:
                print("Invalid distance input, try again.\n")
                correctInput = False

    return customers

def optimalPath(customers):
    print("\n" + "-"*40 + "\n")

    #TO DO

    print("The Optimal Delivery is path is: ")
    print("\n" + "-"*40 + "\n")

def replace(c):
    #TO DO
    fullShelf = c.getFullBottleShelf() # Fill the copied bottles in 
    emptyShelf = c.getEmptyBottleShelf()
    robot = c.getRobot()

    try:
        robot.pickup(c.getWaterColumn().getBottle())
        emptyShelf = robot.stack(emptyShelf)

        fullShelf = robot.unstack(fullShelf) #Pickup Bottle from top of full Bottle shelf
        c.getWaterColumn().setBottle(robot.putdown()) #Place full Bottle into Water Column

        c.setFullBottleShelf(fullShelf)
        c.setEmptyBottleShelf(emptyShelf)
    except:
        print("Bottle Replacement Failed")

    return c

def replenish(c):
    #TO DO
    i = 0
    return c

def waterConsumption():
    for c in customers:
        i = random.randrange(1, 5, 1)
        w = i / 5
        old = c.getWaterColumn().getBottle().getWaterLevel()
        newLevel = old - w
        if(newLevel < .25): #Replenish or replace
            if(len(c.getFullBottleShelf()) < 2):
                c = replenish(c) #Technician drops off two full bottles, the robot picks ups 
                print("Customer " + c.name + "'s Water is being Replenished")
            else:
                c = replace(c)# Robot stacks empty bottle in shelf, picks up top bottle from full shelf and places it inside the waterColumn
                print("Customer " + c.name + "'s Water Bottle has been replaced. Water Level: " + str(c.getWaterColumn().getBottle().getWaterLevel()))
        else:
            c.getWaterColumn().getBottle().setWaterLevel(newLevel)
            if (c.getWaterColumn().getType() == 'Chilled'):
                try:
                    t = random.randrange(-40, 40, 1)
                    t = t / 21
                    t = t + 42
                    c.getWaterColumn().setTemp(t)
                    print("Customer " + c.name + "'s Water Level: " + str(c.getWaterColumn().getBottle().getWaterLevel()) + ", Temperature: " + str(c.getWaterColumn().getTemp()) + " F")
                except ValueError:
                    print("Invalid WaterColumn")
            else:
                try:
                    print("Customer " + c.name + "'s Water Level: " + str(c.getWaterColumn().getBottle().getWaterLevel()))
                except ValueError:
                    print("Invalid WaterColumn")
    print("\n")

def fillWater():
    print("Filling Up Customers Water Columns\n")
    
    for c in customers:
        size = c.getWaterColumn().getBottle().getCapacity()
        c.getWaterColumn().getBottle().setWaterLevel(size) 
        print("Customer " + c.name + "'s Water Column is " + str(c.getWaterColumn().getType()) + ", bottle is " + 
        str(c.getWaterColumn().getBottle().getType()) + " and holds " + str(c.getWaterColumn().getBottle().getCapacity()) + " gallons")
        print("Water Level: " + str(c.getWaterColumn().getBottle().getWaterLevel()) + "\n")
   
    print("\n")

def printDay(day):
    print("\n" + "-"*40 + "\n")
    print("\nDay Number: " + str(day) + "\n")
        


########## MAIN ##########
customers = initializeCustomers(customers)
day = 0

# Right now we're just asking for distance input but we could also ask for chilled/regular stands, bottle capacities etc.
# Just takes a while to fill in every time so I currently have customers 1-5 preset with pseudo-random water specs

#Compute & Print Optimal distances to each customer
optimalPath(customers)

#Load each customer's water stand
printDay(day)
fillWater()
day += 1

#Simulate passing of time by user input, one key press is the passing of one day
#Results of the time passing are displayed after each cycle
while(dayCycle != 'q'):
    printDay(day)

    #Randomly generate a drop in water level between 1/5 to 4/5 of a gallon for each customer each day cycle
    waterConsumption()


    dayCycle = input("Press 'q' to quit, or any other key to progress to the next day: \n")
    day += 1

    print("\n" + "-"*40 + "\n")

print("You ended the simulation on Day: " + str(day - 1))
exit
