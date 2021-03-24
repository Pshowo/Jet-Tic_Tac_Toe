import re
import random

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

        if grid[coord[0]][coord[1]] == " ": 
            grid[coord[0]][coord[1]] = self.mark
        else:
            print("This cell is occupied")