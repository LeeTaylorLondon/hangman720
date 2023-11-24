class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman class with given word list and number of lives."""
        import random

        self.word = random.choice(word_list)  # Randomly pick a word from the word list
        self.word_guessed = ['_' for _ in self.word]  # Initialize word_guessed with underscores
        self.num_letters = len(set(self.word))  # Number of unique letters in the word
        self.num_lives = num_lives  # Set the number of lives
        self.word_list = word_list  # Store the word list
        self.list_of_guesses = []  # Initialize an empty list for guesses


# Example usage:
word_list = ["apple", "banana", "orange"]
game = Hangman(word_list)
