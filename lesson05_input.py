# USER INPUT IN PYTHON
# BY DEFAULT, ALWAYS A STRING

print("\n--- User Input Demonstration ---")

name = input("Enter your name: ")
print("Hello", name)

# age = int(input('Enter your age: ""))
age = int(input("Enter your age: "))
print(type(age))

age_number = int(age)
print("Next year, you will be:", age_number + 1)
print(type(age_number))

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")


# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

fav_color = input("Enter fav color: ")
print(fav_color, "is a nice color")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))    
sum = number_1 + number_2
print("if you add the two numbers, they equal", sum)        

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.

import math 
first_number = int(input("Enter a number to represent the diameter: "))
radius = first_number / 2
area = math.pi * radius ** 2
area_rounded =  math.floor(area)
print("The cirlce area using the diameter is", area_rounded)

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random
die_sides = int(input("Enter a number on how many sides the die should have: ") )
roll = random.randint(1, die_sides)
print("The die landed on", roll)
