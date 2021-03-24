import io
from classes.game import Game
from classes.player import Player
from test.test_sample import *
import unittest
from unittest.mock import patch
from io import StringIO

class test_game(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    # @patch("builtins.input", return_value="start user user")
    # def test_menu(self, mock_input):
    #     players = self.game.menu()
    #     self.assertEqual(players, (("user", "X"),("user", "O")))

    def test_menu(self):
        with patch("builtins.input", return_value="start user user") as fake_out:
            players = self.game.menu()
            self.assertEqual(players, (("user", "X"),("user", "O")))

        with patch("builtins.input", return_value="start easy medium") as fake_out:
            players = self.game.menu()
            self.assertEqual(players, (("easy", "X"),("medium", "O")))

    def test_draw(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.game.draw([['O', 'X', ' '], ['X', 'O', 'O'], ['O', 'X', 'X']])
            self.assertEqual(fake_out.getvalue(), "---------\n| O X   |\n| X O O |\n| O X X |\n---------\n")

        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.game.draw([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
            self.assertEqual(fake_out.getvalue(), "---------\n|       |\n|       |\n|       |\n---------\n")

    def test_check(self):
        self.assertEqual(self.game.check([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]), False)
        self.assertEqual(self.game.check([[' ', 'X', ' '], [' ', 'O', ' '], [' ', 'X', ' ']]), False)
        self.assertEqual(self.game.check([['O', 'X', 'X'], ['X', 'O', 'O'], ['O', 'X', 'O']]), True)
        self.assertEqual(self.game.check([['X', 'X', 'X'], ['O', ' ', 'O'], [' ', ' ', ' ']]), True)
        self.assertEqual(self.game.check([['X', ' ', 'X'], ['O', 'O', 'O'], [' ', ' ', ' ']]), True)
        self.assertEqual(self.game.check([['X', ' ', 'O'], ['O', ' ', 'O'], ['X', 'X', 'X']]), True)
        self.assertEqual(self.game.check([['X', ' ', 'O'], ['X', ' ', 'O'], ['X', 'O', 'X']]), True)
        self.assertEqual(self.game.check([['O', 'X', 'O'], [' ', 'X', 'O'], [' ', 'X', ' ']]), True)
        self.assertEqual(self.game.check([['O', ' ', 'O'], [' ', 'X', 'O'], ['X', 'X', 'O']]), True)
        self.assertEqual(self.game.check([['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]), "Imposible")

# if __name__ == "__main__":
#     unittest.main()