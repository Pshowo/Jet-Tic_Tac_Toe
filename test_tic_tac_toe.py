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

    def test_game_board(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test00["in"]))
            self.assertEqual(fake_out.getvalue(), test00["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test01["in"]))
            self.assertEqual(fake_out.getvalue(), test01["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test02["in"]))
            self.assertEqual(fake_out.getvalue(), test02["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test03["in"]))
            self.assertEqual(fake_out.getvalue(), test03["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.matrix(test04["in"]))
            self.assertEqual(fake_out.getvalue(), test04["out"])


    def test_medium_mode(self):

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test07["in"])))
            self.assertEqual(fake_out.getvalue(), test07["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test08["in"])))
            self.assertEqual(fake_out.getvalue(), test08["out"])
        
        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test09["in"])) )
            self.assertEqual(fake_out.getvalue(), test09["out"])        
        
        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test10["in"])) )
            self.assertEqual(fake_out.getvalue(), test10["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test11["in"])) )
            self.assertEqual(fake_out.getvalue(), test11["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test12["in"])) )
            self.assertEqual(fake_out.getvalue(), test12["out"])  

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test13["in"])))
            self.assertEqual(fake_out.getvalue(), test13["out"]) 

        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.game_board(app.medium_mode("O", app.matrix(test14["in"])) )
            self.assertEqual(fake_out.getvalue(), test14["out"])
                                
        with patch("sys.stdout", new=StringIO()) as fake_out:
            a = app.matrix(test15["in"])
            app.game_board(app.medium_mode("O", a ))
            self.assertEqual(fake_out.getvalue(), test15["out"]) 

        with patch("sys.stdout", new=StringIO()) as fake_out:
            a = app.matrix(test16["in"])
            app.game_board(app.medium_mode("O", a ))
            self.assertEqual(fake_out.getvalue(), test16["out"])

        with patch("sys.stdout", new=StringIO()) as fake_out:
            a = app.matrix(test17["in"])
            app.game_board(app.medium_mode("O", a ))
            self.assertEqual(fake_out.getvalue(), test17["out"]) 

        with patch("sys.stdout", new=StringIO()) as fake_out:
            a = app.matrix(test18["in"])
            app.game_board(app.medium_mode("O", a ))
            self.assertEqual(fake_out.getvalue(), test18["out"])

if __name__ == "__main__":
    unittest.main()