# tests/test_game.py

import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)
# test_empty_word
    def test_empty_word(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)
# test_is_valid
    def test_is_valid(self):
        new_game = Game()
        new_game.grid=list('OQUWRBAZE')
        self.assertEqual(new_game.grid, list('BAROQUE'))
        self.assertIs(new_game.is_valid('OQUWRBAZE'), True)
# test_is_not_valid
    def test_is_not_valid(self):
        new_game = Game()
        new_game.grid=list('OQUWRBAZE')
        self.assertEqual(new_game.grid, list('TIKCHBILA'))
        self.assertIs(new_game.is_valid('OQUWRBAZE'), False)

# tests unknown word
    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertIs(new_game.is_valid('FEUN'), False)
