import random

# Ask for a single letter input
guess = input("Enter a single letter: ")

# Check if input is valid
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# Select a random word
word_list = ["banana", "orange", "apple", "pear", "grapes"]
word = random.choice(word_list)

# Print the random word
print(word)
