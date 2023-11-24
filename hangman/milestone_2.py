import random

# Step 1: Ask the user to enter a single letter
guess = input("Enter a single letter: ")

word_list = ["banana", "orange", "apple", "pear", "grapes"]

# Using random.choice to select a random word from the list
word = random.choice(word_list)

# Printing the randomly selected word
print(word)
