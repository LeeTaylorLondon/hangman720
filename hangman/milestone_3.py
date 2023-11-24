# milestone_3.py

# Assuming the secret word is 'apple' for the example
secret_word = "apple"

# This loop will run indefinitely until a valid single alphabetical character is entered.
while True:
    guess = input("Guess a letter: ")  # Prompt the user to guess a letter

    # Check if the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        # If the letter guessed by the user is in the secret word
        if guess in secret_word:
            print(f"Good guess! {guess} is in the word.")  # Acknowledge the correct guess
            break  # Exit the loop after a correct guess
        else:
            # Inform the user if the guess is not in the word
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        # Inform the user of invalid input and continue the loop
        print("Invalid letter. Please, enter a single alphabetical character.")
