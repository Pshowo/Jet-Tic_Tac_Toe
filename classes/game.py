class Game:
    """Represents the game, menu, draws game board. """
    
    def __init__(self):
        self.empty_grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]  
        self.allow_options = ["user", "easy", "medium", "hard"]
    
    def menu(self):
        """The game menu. Avaiable only 6 commands: "user", "easy", "medium", "hard", "start", "exit".
        To start the game commands must start on "start" command. Incorrect commands printed "Bad parameters!"

        Returns
        -------
        touple
            Touple with chooses type of players and marks.

        Example
        -------
        >>> Input command: start user hard
        (("user", "X"), ("hard", "O"))
        """
        while True:
            command = input("Input command:") 
            if command == "exit":
                exit()
            elif command.startswith("start") and " " in command and len(command.split(" ")) == 3:
                players = command.split(" ")
                players.pop(0)
                if players[0] in self.allow_options and players[1] in self.allow_options:
                    first_player = players[0]
                    second_player = players[1]
                    return ((first_player, "X"),(second_player, "O"))
                else:
                    print("Bad parameters!")
            else:
                print("Bad parameters!")

    def draw(self, x):
        """Draws the board game on the console.

        Parameters
        ----------
        x : list
            List with sequence of chars

        Examples
        --------
        >>> game_board([['O', 'X', '_'], ['X', 'O', 'O'], ['O', 'X', 'X']])
        ---------
        | O X   |
        | X O O |
        | O X X |
        ---------     
        """
        for i in range(3):
            for j in range(3):
                if x[i][j] == "_":
                    x[i][j] = " "
        print("---------")
        print(f"| {x[0][0]} {x[0][1]} {x[0][2]} |")
        print(f"| {x[1][0]} {x[1][1]} {x[1][2]} |")
        print(f"| {x[2][0]} {x[2][1]} {x[2][2]} |")
        print("---------")
        
