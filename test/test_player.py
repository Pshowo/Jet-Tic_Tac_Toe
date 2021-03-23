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
            self.assertEqual(fake_out.getvalue(), 'Making move level "user"\n')

    def test_make_move(self):
        g = Game()
        self.user.make_move((1, 1), g.empty_grid)
        self.assertEqual(g.empty_grid, [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']])
        self.user.make_move((0, 2), g.empty_grid)
        self.assertEqual(g.empty_grid, [['_', '_', 'X'], ['_', 'X', '_'], ['_', '_', '_']])

class test_User(unittest.TestCase):
    def setUp(self):
        self.user = User(("user", "X"))
        self.g = Game()

    def test_user_input(self):
        with patch("builtins.input", return_value="2 2") as fake_out:
            coord = self.user.user_input(self.g.empty_grid)
            print(">> coord", coord)
            self.assertEqual(coord, (1, 1))

        with patch("builtins.input", return_value="3 1") as fake_out:
            coord = self.user.user_input(self.g.empty_grid)
            print(">> coord", coord)
            self.assertEqual(coord, (2, 0))

        with patch("builtins.input", return_value="1 3") as fake_out:
            coord = self.user.user_input(self.g.empty_grid)
            print(">> coord", coord)
            self.assertEqual(coord, (0, 2))
