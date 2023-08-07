

#Author: Matt Harris
#Start Date: Aug 5, 2023
#Project: Wall Area Calculator
#Notes: This is my first attempt at making a program that will calculate wall area in decimal sqft from length of wall, and stored parameter of height of wall.


import time

repeat = False



floor_1 = 0
floor_2 = 0
floor_3 = 0
floor_4 = 0
floor_5 = 0






#Have user input height of walls for levels 1-5 and save to variables
floor_1 = int(input("How tall is level 1 in decimal feet? "))
floor_2 = int(input("How tall is level 2 in decimal feet? "))
floor_3 = int(input("How tall is level 3 in decimal feet? "))
floor_4 = int(input("How tall is level 4 in decimal feet? "))
floor_5 = int(input("How tall is level 5 in decimal feet? "))
print("Thank you!")

#Begin loop
while repeat == False:

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    print("What would you like to do?")
    print("1. Change floor heights")
    print("2. Change working floor")
    print("3. Quit")
    print("4. Calculate wall height for working floor")
    selection = int(input("Please enter the menu number of the option you desire. "))


    if selection == 3:
        print("Thank you for using Wall Area Calculator")
        repeat = True
    
    elif selection == 2:
        list_of_working_floors = [floor_1, floor_2, floor_3, floor_4, floor_5]

        working_floor = int(input("Which floor would you like to work on now? "))
        working_floor = working_floor - 1  

    elif selection == 1:
        floor_1 = int(input("How tall is level 1 in decimal feet? "))
        floor_2 = int(input("How tall is level 2 in decimal feet? "))
        floor_3 = int(input("How tall is level 3 in decimal feet? "))
        floor_4 = int(input("How tall is level 4 in decimal feet? "))
        floor_5 = int(input("How tall is level 5 in decimal feet? "))
        print("Thank you!")      

        list_of_working_floors = [floor_1, floor_2, floor_3, floor_4, floor_5]

    elif selection == 4:
        wall_length = int(input("How long is the wall you are measuring? "))
        print(wall_length)

        wall_area = wall_length * list_of_working_floors[working_floor]
        print("The area of the wall is .....",wall_area)

    else:
        print("Please enter a valid number.")



print("")
print("")
print("")
print("")
print("")
print("")


























