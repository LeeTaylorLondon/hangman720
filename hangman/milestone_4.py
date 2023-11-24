class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman class with given word list and number of lives."""
        import random
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower()  # Convert to lower case
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # More logic will be added here in later tasks

    def ask_for_input(self):
        """Prompt the user for a letter and validate it."""
        while True:
            guess = input("Guess a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  # Call check_guess method
                self.list_of_guesses.append(guess)  # Append guess to list_of_guesses
                break


# Example usage
word_list = ["apple", "banana", "orange"]
game = Hangman(word_list)
game.ask_for_input()  # Testing the method
