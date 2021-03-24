import io
from classes.player import Player
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

    def test_make_user_move(self):

        with patch("builtins.input", return_value="2 2") as fake_out:
            g = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            self.user.make_move(g)
            self.assertEqual(g, [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']])

        with patch("builtins.input", return_value="1 1") as fake_out:
            g = [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            self.user.make_move(g)
            self.assertEqual(g, [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

        with patch("builtins.input", return_value="3 3") as fake_out:
            user = Player(("user", "O"))
            g = [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            user.make_move(g)
            self.assertEqual(g, [[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']])

    def test_make_medium_move(self):

        user = Player(("medium", "O"))
        g = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        user.make_move(g)
        self.assertEqual(g, [['X', 'X', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']])

        g = [['O', ' ', ' '], ['X', ' ', 'X'], [' ', 'O', ' ']]
        user.make_move(g)
        self.assertEqual(g, [['O', ' ', ' '], ['X', 'O', 'X'], [' ', 'O', ' ']])

        g = [['X', ' ', ' '], [' ', ' ', ' '], [' ', 'O', 'X']]
        user.make_move(g)
        self.assertEqual(g, [['X', ' ', ' '], [' ', 'O', ' '], [' ', 'O', 'X']])

        g = [['O', ' ', 'X'], [' ', 'X', ' '], [' ', 'O', ' ']]
        user.make_move(g)
        self.assertEqual(g, [['O', ' ', 'X'], [' ', 'X', ' '], ['O', 'O', ' ']])

        g = [['X', ' ', 'O'], ['X', ' ', ' '], [' ', 'O', ' ']]
        user.make_move(g)
        self.assertEqual(g, [['X', ' ', 'O'], ['X', ' ', ' '], ['O', 'O', ' ']])

        g = [[' ', ' ', 'O'], [' ', 'X', ' '], ['O', 'X', ' ']]
        user.make_move(g)
        self.assertEqual(g, [[' ', 'O', 'O'], [' ', 'X', ' '], ['O', 'X', ' ']])

        g = [[' ', ' ', 'X'], [' ', 'O', 'X'], ['O', ' ', ' ']]
        user.make_move(g)
        self.assertEqual(g, [[' ', ' ', 'X'], [' ', 'O', 'X'], ['O', ' ', 'O']])

