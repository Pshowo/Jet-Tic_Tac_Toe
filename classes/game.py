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
        
    def check(self, chars):
        # counts how many chars appears in the list
        sum_X = sum([chars[x].count("X") for x in range(0, 3)])
        sum_O = sum([chars[x].count("O") for x in range(0, 3)])

        # add all a chars into the list in a specific order to check the columns [ [col1], [col2], [col3] ]
        check_columns = [[chars[j][i] for j in range(3)] for i in range(3)]

        # list with columns wins
        x_wins=[check_columns[x] for x in range(3) if check_columns[x] == list('XXX')]
        o_wins=[check_columns[x] for x in range(3) if check_columns[x] == list('OOO')]

        # Impossible
        if abs(sum_X - sum_O) >= 2 or any(x_wins) == True and any(o_wins) == True:
            print("Imposible")
            return "Imposible"
        else:
            # X win configuration
            if any([chars[x] for x in range(3) if chars[x] == list('XXX')]):
                print("X wins")  # X wins any rows
                return True
            elif any(x_wins) == True:
                print("X wins")  # X wins any columns
                return True
            elif chars[2][0] == "X" and chars[1][1] == "X" and chars[0][2] == "X":
                print("X wins")  # x wins cross (bottom left - top right)
                return True
            elif chars[0][0] == "X" and chars[1][1] == "X" and chars[2][2] == "X":
                print("X wins")  # x wins cross (top left - bottom right)
                return True

            # O win configuration
            elif any([chars[x] for x in range(3) if chars[x] == list('OOO')]): # O win configuration
                print("O wins")  # O wins any row
                return True
            elif any(o_wins)== True:
                print("O wins")  # O wins any columns
                return True
            elif chars[2][0] == "O" and chars[1][1] == "O" and chars[0][2] == "O":
                print("O wins")  # O wins cross (bottom left - top right)
                return True
            elif chars[0][0] == "O" and chars[1][1] == "O" and chars[2][2] == "O":
                print("O wins")  # O wins cross (top left - bottom right)
                return True

            # Game not finished
            elif "_" in chars[0] or "_" in chars[1] or "_" in chars[2]:
                # print("Game not finished")
                return False

            # Draw
            elif "_" not in chars[0] and "_" not in chars[1] and "_" not in chars[2]:
                print("Draw")
                return True
        return False