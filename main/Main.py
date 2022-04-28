# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:10:51 2022

@author: Kale Henning, Jason Heiman, Rosemary Kingsley
"""
import array
import copy
from distutils.command.sdist import sdist
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
        newBottle3 = copy.copy(newBottle)
        c.addFullBottle(newBottle) #Start with 1 bottle in waterColumn and 3 in the full shelf, none in empty shelf
        c.addFullBottle(newBottle2)
        c.addFullBottle(newBottle3)

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
    fullShelf = c.getFullBottleShelf() 
    emptyShelf = c.getEmptyBottleShelf()
    robot = c.getRobot()

    try:
        robot.pickup(c.getWaterColumn().getBottle())
        emptyShelf = robot.stack(emptyShelf)

        fullShelf = robot.unstack(fullShelf) #Pickup Bottle from top of full Bottle shelf
        c.getWaterColumn().setBottle(robot.putdown()) #Place full Bottle into Water Column

        c.setFullBottleShelf(fullShelf)
        c.setEmptyBottleShelf(emptyShelf)
        
        print("Customer " + c.name + "'s Water Bottle has been replaced. Water Level: " + str(c.getWaterColumn().getBottle().getWaterLevel()))
    except:
        print("Bottle Replacement Failed")

    return c

def arrangeFullShelf(c):
    fullShelf = c.getFullBottleShelf()
    robot = c.getRobot()

    newBottle = c.getWaterColumn().getBottleType()
    if(newBottle.getCapacity() == 6):
        newBottle.setWaterLevel(6)
    else:
        newBottle.setWaterLevel(4)
    newBottle2 = copy.copy(newBottle)

    try:
        fullShelf = robot.unstack(fullShelf) # Take the last remaining off of the fullBottleShelf and place on the floor
        oldBottle = robot.putdown()

        robot.pickup(newBottle) # Stack first bottle
        fullShelf = robot.stack(fullShelf)

        robot.pickup(newBottle2) # Stack second bottle
        fullShelf = robot.stack(fullShelf)

        robot.pickup(oldBottle) # Stack old bottle
        fullShelf = robot.stack(fullShelf)

    except:
        print("Bottle Replenishing Failed")
    
    return c


def replenish(c):
    #Add 2 full bottles and arrange fullBottleShelf
    c = arrangeFullShelf(c)
    #Clear emptyBottleShelf
    c.getEmptyBottleShelf().clear()
    
    print("Customer " + c.name + "'s Water is being Replenished")
    print("Full Shelf now has " + str(len(c.getFullBottleShelf())) + " bottles, empty shelf now has " + str(len(c.getEmptyBottleShelf())) + " bottles")
    print("") #New Line for formatting
    return c

def reportWaterLevel(c, newLevel):
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

def waterConsumption(day):
    for c in customers:
        leak = leakMonitor(c, day) #Monitor leaks
        if(leak == False):
            i = random.randrange(1, 5, 1)
            w = i / 5
            old = c.getWaterColumn().getBottle().getWaterLevel()
            newLevel = old - w
            if(newLevel < .25): #Replenish or replace
                if(len(c.getFullBottleShelf()) < 2):
                    c = replenish(c) #Technician drops off two full bottles, the robot picks ups 
                elif(newLevel <= 0):
                    c.getWaterColumn().getBottle().setWaterLevel(0)
                    c = replace(c)# Robot stacks empty bottle in shelf, picks up top bottle from full shelf and places it inside the waterColumn
                else:
                    reportWaterLevel(c, newLevel)
            else:
                reportWaterLevel(c, newLevel)

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

def alarm(customer):
    print("Dispatch has been sent to fix Leak")
    replace(customer) #Replace empty bottle from leak
    print("") #New Line for formatting

def leakMonitor(c, day):
    leak = False
    if (day > 4):
        #Generate probability of leak occuring after first few days, 3% chance
        chance = random.randrange(1, 34, 1)
        if(chance == 1):
            
            #A leak drains the current bottle
            c.getWaterColumn().getBottle().setWaterLevel(0)
            #Leak is found, signal alarm
            print("Customer " + c.name + " has a leak! Their water level is: " + str(c.getWaterColumn().getBottle().getWaterLevel()))

            #Dispatch someone to come fix the leak, bottle is replaced
            alarm(c)
            leak = True

    return leak
            

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
    waterConsumption(day)

    dayCycle = input("Press 'q' to quit, or any other key to progress to the next day: \n")
    day += 1

    print("\n" + "-"*40 + "\n")

print("You ended the simulation on Day: " + str(day - 1))
exit
