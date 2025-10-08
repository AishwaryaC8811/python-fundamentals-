# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o
second_letter = greeting[1]
print(second_letter)

# 0 1 2
# A d a

message = greeting + " " + name + "!"
print("Concatenated message: ", message)

print()

word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter ", word[0])
print("Last letter ", word[-1])
print("Range of letters (non-inclusive):", word[-7:-2])
print(word[:5])
print("Last seven letters:", word[-7:])
print("Step through every second character:", word[::2])
print("Reversed, stepping every third letter:", word[::-1])

# Built in functions 

country = "Bahamas"
length_of_word = len(country)
print(length_of_word)

character = "SpOnGEbOB sQuaREPanTs"
print("\nUppercase:", character.upper())
print("\nLowercase:", character.lower())
print("Capitalized:", character.capitalize())
print("Title Format:", character.title())

print()

#Find and replace text 
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
print(sentence)
print(new_sentence)

# FORMATTED STRINGS IN PYTHON
# f-strings allow variables and expressions inside strings

print("\n--- Formatted Strings ---")

name = "Bob" 
age = 70
city = "Miami"

print(f"Hello, my name is {name}. I am {age} years old and live in {city}.")

# f-strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}, My name in uppercase is {name.upper()}.")