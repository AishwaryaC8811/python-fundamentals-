# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

print("Functions (Procedures)")

print("\nExample 1")

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi()
say_bye()
say_bye()
say_hi()

print("\nExample 2")

def express_this(e):    # e is called a PARAMETER, which is a placeholder for an ARGUMENT 
    return e

expression1 = express_this(1 + 2) # the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER
print(expression1)
expression2 = express_this(45 * 6)
print(expression2)

print("\nExample 3")

def greeter(n): # n is the parameter
    return f"HI {n}!"
first = greeter("Aishwarya")
second = greeter("Gabi")
third = greeter("Bella")

print(first, second, third)

print("\nExample 4")

def remainder(a,b):
    return a % b

result = remainder(3,2)
print("Remainder:", result)

print("\nExample 5")

def is_far(distance):
    # INSERT BASE CASE

    if distance < 1:
        return "Error"
    if distance >= 100:
        return "That's far"
    elif distance < 100 and distance >= 20:
        return "That's not too far"
    elif distance < 20: 
        return "That's nearby"
    
    
print(is_far(-40))
print(is_far(324))
print(is_far(55))
print(is_far(2))

print("\nExample 6")

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number

def double_sequencer(number, times):
    value = number
    sequence = []

    for i in range(times):
        value = value * 2
        sequence.append(value)
    return sequence
result = double_sequencer(1, 10)
print(result)

# CHALLENGE 1

# def calculator(e):
        #return(e)
#expression1 = (a + b)
#print(expression1)
#expression2 = (a - b)
#print(expression2)
#expression3 = (a * b)
#print(expression3)
#expression4 = (a // b)
#print(expression4)


def calculator(e):
    return (e)
expression1 = calculator(1 + 1)
print(expression1)
expression2 = calculator(1 - 1)
print(expression2)
expression3 = calculator(2 * 2)
print(expression3)
expression4 = calculator(6 // 2)
print(expression4)


# CHALLENGE 2

# def average_that(a,b,c):
        # return(a,b,c)
# average = ((1 + 2 + 3) / 3)
#print(average)

def average_that(a,b,c):
    return(a,b,c)
average = ((7 + 7 + 7) // 3)
print(average)

#CHALLENGE 3

# def is_even(a):
        #return(a)

#if a % 2 = 1
    #print("odd")
#else:
    #print("even")

def is_even(number):
    return(number)

number = (6)

if number % 2 == 1:
    print("odd")
else:
    print("even")

#CHALLENGE 4

def analyze_word(string):
    return(string)

string = ("apple")
vowelCount = 0
consonantCount = 0
increment = 1

for letter in string:
    if letter == "a" or letter =="e" or letter == "i" or letter == "o" or letter == "u":
        vowelCount = vowelCount + increment
    else:
        consonantCount = consonantCount + increment
print("Vowel Count: ", vowelCount)
print("Consonant Count: ", consonantCount)




