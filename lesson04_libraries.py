# Python libraries are repositories of code that you can use in your own files 

import math 
print("\n--- Math Library ---\n")

print("Square root: ", math.sqrt(25))
print("Round down to an integer: ", math.floor(4.2))
print("Round up to an integer: ", math.ceil(4.2))
print("Power: ", math.pow(2, 5))
print("Pi: ", math.pi)


#RANDOM LIBRARY 
# Pseudorandom Number Generator (PRNG) (Pseudo = Fake)
#True Random Generator 

print("\n--- Random Library ---\n")
import math
seed = 659.36
result_1 = seed * seed 
print("Result 1: ", result_1)
result_2 = result_1 * 15
print("Result 2: ", result_2)
result_3 = result_2 // 6
print("Result 3: ", result_3)
result = math.floor(result_3)
print(result)

result_4 = result_3 % 10
result1 = math.floor(result_4)
print(result1)

print("\n--- Random Library ---\n")

import random

# meathods:

print("Random integer: ", random.randint(1, 7))
print(random.random()) #RANDOM FLOAT BETWEEN 0 and 1

# FOR LISTS - mylist = ["1", "2", "3"]
my_favs = ["taco", "burrito", "enchilada", "quesadilla"]
print(random.choice(my_favs))    
random.shuffle(my_favs)
print(my_favs)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

radius = 14 / 2
circle_area = math.py * radius ** 2
print(circle_area)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

die_roll = random.randint(1, 6)
print("Die Roll: ", die_roll)
