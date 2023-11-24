# milestone_3.py

# This loop will run indefinitely until a valid single alphabetical character is entered.
while True:
    guess = input("Guess a letter: ")  # Prompt the user to guess a letter

    # Check if the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():
        print(f"Good guess! You entered: {guess}")  # If valid, acknowledge the good guess
        break  # Exit the loop
    else:
        # If the input is invalid, inform the user and continue the loop
        print("Invalid letter. Please, enter a single alphabetical character.")
