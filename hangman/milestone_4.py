class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman class with a given word list and number of lives."""
        import random
        self._word = random.choice(word_list)
        self._word_guessed = ['_' for _ in self._word]
        self._num_letters = len(set(self._word))
        self.num_lives = num_lives
        self.word_list = word_list
        self._list_of_guesses = []

    def _update_word_guessed(self, guess):
        """Update the guessed word representation based on the user's guess."""
        for index, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[index] = guess

    def _is_guess_correct(self, guess):
        """Check if the guessed letter is in the word."""
        return guess in self._word

    def _handle_correct_guess(self, guess):
        """Handle actions needed when the guess is correct."""
        print(f"Good guess! {guess} is in the word.")
        self._update_word_guessed(guess)
        self._num_letters -= 1

    def _handle_incorrect_guess(self, guess):
        """Handle actions needed when the guess is incorrect."""
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _check_guess(self, guess):
        """Check the guessed letter and respond accordingly."""
        if self._is_guess_correct(guess):
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        """Prompt the user for a letter and validate it."""
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self._list_of_guesses:
                print("You already tried that letter!")
            else:
                self._check_guess(guess.lower())
                self._list_of_guesses.append(guess)
                break


# Example usage
word_list = ["apple", "banana", "orange"]
game = Hangman(word_list)
game.ask_for_input()
