import io
from classes.player import Player, User
from classes.game import Game
from test.test_sample import *
import unittest
from unittest.mock import patch
from io import StringIO

class test_Player(unittest.TestCase):

    def setUp(self):
        self.user = Player(("user", "X"))

    def test_repr(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(self.user)
            self.assertEqual(fake_out.getvalue(), '\n')
        
        self.user = Player(("easy", "X"))
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(self.user)
            self.assertEqual(fake_out.getvalue(), 'Making move level "easy"\n')

    def test_make_move(self):

        with patch("builtins.input", return_value="2 2") as fake_out:
            g = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            self.user.make_move(g)
            print(g)
            self.assertEqual(g, [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']])

        with patch("builtins.input", return_value="1 1") as fake_out:
            g = [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            self.user.make_move(g)
            print(g)
            self.assertEqual(g, [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

        with patch("builtins.input", return_value="3 3") as fake_out:
            user = Player(("user", "O"))
            g = [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            user.make_move(g)
            print(g)
            self.assertEqual(g, [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']])
