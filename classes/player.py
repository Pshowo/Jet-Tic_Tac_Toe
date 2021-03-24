import re
import random
import numpy as np

class Player:
    """ Represents player on the game. """

    def __init__(self, tup):
        """[summary]

        Parameters
        ----------
        tup : tuple
            Tuple of type (user, easy, medium or hard) and mark (X or O).
        """
        self.type = tup[0]
        self.mark = tup[1]

    def __str__(self):
        if self.type != "user":
            return f'Making move level "{self.type}"'
        else:
            return ""

    def user_input(self, grid):
        """Menu to insert the coodrinates by user.

        Parameters
        ----------
        grid : list
            Main sequences of grid.

        Returns
        -------
        tuple int
            A tuple with coordinates where the mark will be insert (X, Y)
        """
        i = 0
        while i < 1:
            xy = input("Enter the coordinates:")

            out_range = re.search(r"[1-3] [1-3]", xy)
            not_digit = re.search(r"[^\s,\d]", xy)
            if not_digit is None:
                if out_range is not None:
                    x, y = xy.split()
                    x = int(x) - 1
                    y = int(y) - 1

                    if grid[x][y] == 'X' or grid[x][y] == 'O':
                        print("This cell is occupied! Choose another one!")
                    else:
                        # grid[x][y] = self.mark
                        i += 1
                        return (x, y)
                else:
                    print("Coordinates should be from 1 to 3!")
                    continue
            else:
                print("You should enter numbers!")
                continue

    def easy_mode(self, grid):
        """
        Inserts into the random cell the mark. If the cell is occupied, tries again.

        Parameters
        ----------
        mark : str
            The mark which use in the game.

        Returns
        -------

        """
        i = 0
        while i < 1:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if grid[x][y] == 'X' or grid[x][y] == 'O':
                continue
            else:
                # print('Making move level "{}"'.format(self.mode))
                i += 1
                return (x, y)
        return grid

    def medium_mode(self, grid):
        """
        - If it already has two in a row and can win with one further move, it does so.
        - If its opponent can win with one move, it plays the move necessary to block this.
        - Otherwise, it makes a random move.

        Parameters
        ----------
        mark : str
            The mark which use in the game.

        grid : list
            The list of sequences grid.

        Returns
        -------

        """
        contr_mark = "O" if self.mark == "X" else "X"

        # convert grid into np array with 0 and 1
        ar = np.char.count(np.array(grid), contr_mark)
        ar2 = np.multiply(np.char.count(np.array(grid), "O"), -1)
        ar = np.add(ar, ar2)
        del ar2

        ar_d1 = ar.diagonal().sum()  # checks first diagonal
        ar_d2 = np.flip(ar, 1).diagonal().sum()  # checks secondary diagonal
        a1 = [np.sum(ar[0]), np.sum(ar[1]), np.sum(ar[2])]  # check all rows
        a2 = [np.sum(ar.T[0]), np.sum(ar.T[1]), np.sum(ar.T[2])]  # check all columns

        # diagonal
        if ar_d1 == 2:
            for i in range(0, 3):
                a = grid[i][i]
                if grid[i][i] == ' ' or grid[i][i] == '_':
                    return (i, i)
                else:
                    continue
        # Secondary diagonal
        elif ar_d2 == 2:
            if grid[0][2] == ' ':
                return (0, 2)
            elif grid[1][1] == ' ':
                return (1, 1)
            elif grid[2][0] == ' ':
                return (2, 0)

        else:
            # rows
            if 2 in a1:
                for ind, val in enumerate(a1):
                    if val == 2:
                        for k in range(0, 3):
                            if grid[ind][k] == ' ':
                                return (ind, k)
            # columns
            elif 2 in a2:
                for ind, val in enumerate(a2):
                    if val == 2:
                        row = True
                        for k in range(0, 3):
                            if grid[k][ind] == ' ' or grid[k][ind] == '_':
                                return (k, ind)
            else:
                return self.easy_mode(grid)
        return None
    
    def make_move(self, grid):
        """Insterts a mark into an empty cell. 

        Parameters
        ----------
        x : int
            x coordinates, start with 1
        y : int
            y coordinates, start with 1
        grid : list
            grid list

        """
        if self.type == "user":
            coord = self.user_input(grid)
        elif self.type == "easy":
            coord = self.easy_mode(grid)
        elif self.type == "medium":
            coord = self.medium_mode(grid)

        if grid[coord[0]][coord[1]] == " ": 
            grid[coord[0]][coord[1]] = self.mark
        else:
            print("This cell is occupied")