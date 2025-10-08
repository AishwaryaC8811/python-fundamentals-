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

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

quote = input("Enter your favorite quote: ")
length_of_quote = len(quote)
print("Your quote is", length_of_quote, "characters long")

# Challenge 2: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Output formatted name: Lovelace, Ada

first = input("Enter your first name :")
last = input("Enter your last name: ")
name = last + ", " + first
print("Concatenated message: ", name)

# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# Backwards: nohtyP

word = input("Enter a word:")
print("Backwards: ", word[::-1])
print("\nUppercase: ", word.upper())
print("\nLower: ", word.lower())