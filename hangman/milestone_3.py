def is_letter_in_word(letter, target_word):
    """Check if the guessed letter is present in the target word."""
    letter = letter.lower()  # Normalize the letter to lower case
    if letter in target_word:
        print(f"Good guess! '{letter}' is in the word.")
        return True
    else:
        print(f"Sorry, '{letter}' is not in the word. Try again.")
        return False


def prompt_user_guess():
    """Prompt the user for a valid single alphabetical letter guess."""
    while True:
        user_input = input("Guess a letter: ")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter a single alphabetical letter.")


def start_guessing_game(word_to_guess):
    """Start the guessing game, asking the user to guess letters of a given word."""
    while True:
        guessed_letter = prompt_user_guess()  # Get a valid user guess
        if is_letter_in_word(guessed_letter, word_to_guess):
            break  # Exit the loop if the guess is correct


# Assuming the secret word is 'apple' for the example
secret_word = "apple"

# Begin the letter guessing game
start_guessing_game(secret_word)
