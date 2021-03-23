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
        return f'Making move level "{self.type}"'

    def make_move(self, x, y, grid):
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
        if grid[x][y] == " ": 
            grid[x][y] = self.type
        else:
            print("This cell is occupied")