# Add the following to disable specific linters
# pylint: disable=too-few-public-methods
# pylint: disable=missing-docstring

"""A game

Placeholder doc string

"""

from random import choice
import string
# import enchant
from collections import Counter

class Game:
    """A game
    Placeholder doc string
    """
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        # Turns out you don't need to check if the word is a valid Engish word
        # # therefore remove enchant portion
        # Get a dictionary with valid English words
        # dictionary = enchant.Dict("en_EN")

        # Get counters for the game grid and the words so they can be compared
        count_grid = Counter(self.grid)
        count_word = Counter(word)

        # Checking every letter in the word
        for key in count_word:
            # if the letter is not in the grid return false
            if key not in count_grid:
                return False
            # if the letter is used more time than it appears in the grid return false
            if count_word[key] > count_grid[key]:
                return False
        # Otherwise check the word is in the dictionary
        return True
        # return dictionary.check(word)

    # Added this to experiment with poetry run pylint
    # def is_longest_word(self, word: str) -> bool:
    #     """Placeholder"""
    #     print(word)
    #     return True
