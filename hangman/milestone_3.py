def check_guess(guess, word):
    """Check if the guessed letter is in the word."""
    guess = guess.lower()  # Convert the guess into lower case
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False


def ask_for_input(word):
    """Ask the user to input a letter and validate it."""
    while True:  # Continue to ask for a letter until the user inputs a valid one
        guess = input("Guess a letter: ")  # Prompt the user for a guess
        if len(guess) == 1 and guess.isalpha():  # Check if guess is a single alphabetical character
            if check_guess(guess, word):  # If the guess is in the word
                break  # Exit the loop
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


# Assuming the secret word is 'apple' for the example
secret_word = "apple"

# Start the user input process
ask_for_input(secret_word)
