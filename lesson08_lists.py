# LISTS IN PYTHON   [0, 1 , 2, 3]
# Lists store multiple values in one variable.  (Collection of elements)
# They are ordered, mutable (changeable), and allow duplicates.

print()
print("--- Lists in Python ---")

animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print()
print()
print("--- Indexing: how to access the elements of a list ---")
print("First Element:", animals[0])
print("Second Element:", animals[1])
print("Last Element:", animals[-1])

print()
print("--- Modifying Lists ---")

animals[0] = "babirusa"
print(animals)

# .append() - To add it to the end of a list

animals.append("glass frog")
print(animals)

# Inserts element at specific index
# .insert( , '..')  - takes two arguments
animals.insert(3,'aye-aye')
animals.insert(1, 'camel')
print("Inserted another animal:", animals)

animals.remove("babirusa")
print(animals)

# .pop removed last element but stores it into the variable 
last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)

print()
print("--- Useful List Functions ---")


