# ECE 479/579 Final Project
  
  Authors: Kale Henning, Jason Heiman, Rosemary Kingsley
  
  ECE 479/579

  Final Project

  4/21/2022

Summary

Our project solves the TSP for the 5 ThirstAID customers using the A* algorithm. The GUI is text-based and output in the interpreter console. The project is designed using an object oriented approach using the Customers, Robot, WaterColumn, Bottle, and Shelf as objects with properties manipulated throughout each day. The initialization phase asks for distance input of each customer from the user while the specifications of the water column and bottles are randomized. The project simulates the changing of states via a day cycle where the user can input any key press to progress to the next day, pressing q will terminate the program. The passing of the day cycle will randomly generate a drop in water level of each customer by ⅕ to ⅘ of a gallon to simulate a change in the state of each customer’s water stand. The report of each Customer’s ThirstAID system status is reported after each day. Leaks are also randomly generated and have a 3% chance of occurring at each customer’s house, resulting in the water jug inside of the water column to be empty (set to 0) and an alarm is signaled to fix the leak the same day. If the user happens to only have one bottle left at the time of a leak, they will also be replenished upon the ‘fix-leak’ signal being raised. The bottles are replenished when 1 bottle is left on the full bottle stand and there is less than a quarter of a gallon left in the water column. When this occurs there is a notification through the GUI and 2 water bottles are dropped off at the customer’s house where the robot, which implements the 4 operations: pickup, putdown, stack and unstack,  arranges the full bottle shelf by first taking off the old single bottle, placing the two new bottles on the shelf and finally putting the old bottle on top. The empty shelf is cleared out after the full bottle shelf arrangement process has been completed. The robot is also used for the replacement process where the bottle in the water column is removed once empty, placing it on the empty shelf, and a new full bottle is unstacked from the full shelf and placed in the water column.

Requirements

The requirements for running the program are to open the files provided in the main folder. We have been using Visual Studio code as our IDE for this project but any environment holding Python 3.7+ standard libraries will work. Running the Main.py program will begin the program with a prompt for each customer’s distance in the console. The user will input a value between 1 and 100, any other values will prompt the user to try again. After this the day cycle will begin, progressed by key input (i.e. enter) and reports changes in customer’s systems indefinitely, or until q is pressed to exit.

