class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman class."""
        import random
        self._word = random.choice(word_list)
        self._word_guessed = ['_' for _ in self._word]
        self._num_letters = len(set(self._word))
        self.num_lives = num_lives
        self._list_of_guesses = []

    def _is_guess_valid(self, guess):
        """Check if the guess is valid."""
        return len(guess) == 1 and guess.isalpha()

    def _is_guess_new(self, guess):
        """Check if the guess has not been tried before."""
        return guess not in self._list_of_guesses

    def _update_word_guessed(self, guess):
        """Update the guessed word representation based on the user's guess."""
        for index, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[index] = guess

    def _handle_guess(self, guess):
        """Handle the user's guess."""
        guess = guess.lower()
        self._list_of_guesses.append(guess)

        if guess in self._word:
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
            self._num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Prompt the user for a letter and handle the input."""
        while True:
            guess = input("Guess a letter: ")

            if not self._is_guess_valid(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif not self._is_guess_new(guess):
                print("You already tried that letter!")
            else:
                self._handle_guess(guess)
                break


def play_game(word_list):
    """Function to play the Hangman game."""
    game = Hangman(word_list)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game._num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


# Sample word list to test the game
word_list = ["apple", "banana", "orange"]

# Call the play_game function to start the game
play_game(word_list)
