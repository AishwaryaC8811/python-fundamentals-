# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")

print( 3 == 2 )
print( "Hello" == "Hi there" )
print( 7 != 4 )
print( 4 > 5 )

# if 
print()
num1 = 10
if num1 == 10: 
    print("Your number is equal to 10")

num2 = 5
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")
else: 
    print("Your number is greater than 12")

# If elif else
print()

temperature = 68 
if temperature >= 80 and temperature > 70:
    print("Its hot!")

elif temperature >= 60:
    print("Its nice!")
else:
    print("Its cold!")

print()

x = 20
y = 20

if x == y: 
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y: 
    print("x is less than y")
else: 
    print("error")

print()

# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 

age = 17
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

print()

# Using 'or' and 'not'
print("--- Using 'or' --- ")
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Its the weekend!")
elif day == "Monday" or day == "Tuesday":
    print("Its Monday or Tuesday")
else:
    print("Its wed, Thur, or Fri")

if day is not "Monday":
    print("Its not Monday")

