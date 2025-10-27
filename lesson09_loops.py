# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.
print()
print("--- Loops in Python ---")

# The for-loop.
# A for-loop repeats for each element in a sequence (like a list or string).
import time



animals = ["lamb", "sheep", "cow", "goose", "donkey"]
print("\nOur animals:", animals)

print("\n--- For Loop: visiting each animal ---")


for animal in animals:
    print("Now petting a", animal)
    time.sleep(1.5)

    if animal == "sheep":
        print("Hi sheep!")
print("\nNow I have petted all the animals.")

print()

for num in range(2, 11, 2):
    print("Counting: ", num)

