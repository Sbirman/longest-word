# # game.py

import string
import random

class Game:

    def __init__(self):
        self.grid = []
        for i in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # get a shallow copy to avoid changing word
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True
