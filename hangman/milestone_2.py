import random


def get_single_letter():
    """Prompt the user for a single alphabetical character."""
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        return guess
    else:
        print("Oops! That is not a valid input.")
        return None


def choose_random_word(words):
    """Choose and return a random word from the given list."""
    return random.choice(words)


# Define a list of fruits for the word choice
fruits = ["banana", "orange", "apple", "pear", "grapes"]

# Main execution
user_guess = get_single_letter()
if user_guess:
    selected_word = choose_random_word(fruits)
    print(f"Randomly selected word: {selected_word}")
else:
    print("No valid guess was made.")
