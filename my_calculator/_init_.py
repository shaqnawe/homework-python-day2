# Question 2
# 2) Create a Module in Visual Studio Code and Import It
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a room
# 2) Has a function to calculate the circumference of a circle

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

from math import pi

def calculate():
    print("Please enter circle for circumference of circle or room for square footage of room")
    value = input("Do you want to calculate the square footage of a room or circumferece of a circle? ")
    if value == 'room':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        # result stores the square footage of the room
        result = length*width
        #print(result)
    elif value == 'circle':
        radius = float(input("Enter the radius of circle: "))
        # result stores the circumference of the circle
        result = 2*pi*radius
        #print(result)
    else:
        print("You have entered an incorrect value, please try again!")
    return result
# calculate()