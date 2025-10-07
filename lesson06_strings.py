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

phrase = "SpOnGEbOB"
print("\nUppercase:", phrase.upper())
print("\nLowercase:", phrase.lower())
print("Capitalized:", phrase.capitalize())