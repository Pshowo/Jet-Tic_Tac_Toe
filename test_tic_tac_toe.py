import io
import tic_tac_toe as app
from test.test_sample import *
import unittest
from unittest.mock import patch
from io import StringIO

class test_app(unittest.TestCase):
    
    def test_check_gamer(self):
        self.assertEqual(app.check_gamer("X____O__X"), "O")
        self.assertEqual(app.check_gamer("X__O_O__X"), "X")

    def test_matrix(self):
        self.assertEqual(app.matrix("__X_O___X"), [["_", "_", "X"], ["_", "O", "_"], ["_", "_", "X"]])
        self.assertEqual(app.matrix("_________"), [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]])
        # self.assertEqual(app.matrix("________"), None) # Todo

    def test_game_board(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test0["in"]))
            self.assertEqual(fake_out.getvalue(), test0["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test1["in"]))
            self.assertEqual(fake_out.getvalue(), test1["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test2["in"]))
            self.assertEqual(fake_out.getvalue(), test2["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test3["in"]))
            self.assertEqual(fake_out.getvalue(), test3["out"])
            
        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test4["in"]))
            self.assertEqual(fake_out.getvalue(), test4["out"])

if __name__ == "__main__":
    unittest.main()