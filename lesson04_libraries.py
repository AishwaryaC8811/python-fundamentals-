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

seed = 65936
result_1 = seed * seed 
print("Result 1: ", result_1)
result_2 = result_1 * 15
print("Result 2: ", result_2)
result_3 = result_2 // 6
print("Result 3: ", result_3)

