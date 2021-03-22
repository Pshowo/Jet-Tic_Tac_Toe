import random
import re


def game_board(x):
    """
    Draws the board game on the console
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


def check_game(chars):

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
    else:  
        # X win configuration
        if any([chars[x] for x in range(3) if chars[x] == list('XXX')]):
            print("X wins")  # X wins any rows
            exit()
        elif any(x_wins) == True:
            print("X wins")  # X wins any columns
            exit()
        elif chars[2][0] == "X" and chars[1][1] == "X" and chars[0][2] == "X":
            print("X wins")  # x wins cross (bottom left - top right)
            exit()
        elif chars[0][0] == "X" and chars[1][1] == "X" and chars[2][2] == "X":
            print("X wins")  # x wins cross (top left - bottom right)
            exit()

        # O win configuration
        elif any([chars[x] for x in range(3) if chars[x] == list('OOO')]): # O win configuration
            print("O wins")  # O wins any row
            exit()
        elif any(o_wins)== True:
            print("O wins")  # O wins any columns
            exit()
        elif chars[2][0] == "O" and chars[1][1] == "O" and chars[0][2] == "O":
            print("O wins")  # O wins cross (bottom left - top right)
            exit()
        elif chars[0][0] == "O" and chars[1][1] == "O" and chars[2][2] == "O":
            print("O wins")  # O wins cross (top left - bottom right)
            exit()

        # Game not finished
        elif " " in chars[0] or " " in chars[1] or " " in chars[2]:
            # print("Game not finished")
            return None

        # Draw
        elif " " not in chars[0] and " " not in chars[1] and " " not in chars[2]:
            print("Draw")
            exit()


def matrix(x):
    board = []
    for i in range(3):
        if i == 0:
            list_a = []
            for j in range(0, 3):
                list_a.append(x[j])
            board.append(list_a)
        elif i == 1:
            list_a = []
            for j in range(3, 6):
                list_a.append(x[j])
            board.append(list_a)
        elif i == 2:
            list_a = []
            for j in range(6, len(x)):
                list_a.append(x[j])
            board.append(list_a)

    return board


def user_input(mark):
    global matrix_board
    # global gamer

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

                if matrix_board[x][y] == 'X' or matrix_board[x][y] == 'O':
                    print("This cell is occupied! Choose another one!")
                else:
                    matrix_board[x][y] = mark
                    game_board(matrix_board)
                    i += 1
                    # if gamer == 'X':
                    #     gamer = 'O'
                    # elif gamer == "O":
                    #     gamer = 'X'
                    continue
            else:
                print("Coordinates should be from 1 to 3!")
                continue
        else:
            print("You should enter numbers!")
            continue


def easy_mode(mark):
    global matrix_board

    i = 0
    while i < 1:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if matrix_board[x][y] == 'X' or matrix_board[x][y] == 'O':
            continue
        else:
            print(f"x: {x}\ty:{y}")
            matrix_board[x][y] = mark
            print('Making move level "easy"')
            game_board(matrix_board)
            i += 1
            break


def check_gamer(word):
    count_x = word.count("X")
    count_o = word.count("O")
    if count_x == count_o:
        return "X"
    elif count_x > count_o:
        return "O"
    else:
        return "X"


class Player:

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'Making move level "{self.type}"'


def menu():
    allow_options = ["user", "easy", "medium", "hard"]
    command = input("Input command:")
    if command == "exit":
        exit()
    elif command.startswith("start"):
        try:
            command = command.split(" ")
            command.pop(0)
            if len(command) > 1:
                first_player = command[0]
                second_player = command[1]
            else:
                print("Bad parameters!")
                return None

        except ValueError:
            print("Bad parameters!")
            return None

        if first_player in allow_options and second_player in allow_options:
            print(" First player is: {}, second player is: {}".format(first_player, second_player))
            return first_player, second_player
        else:
            print("Bad parameters!")
            return None
    else:
        print("Bad parameters!")
        return None


# === GAME ===
if __name__ == "__main__":

    word = "_________"
    # gamer = check_gamer(word)
    gamer = "X"
    # generate matrix board

    # print the game board
    while True:
        try:
            first_player, second_player = menu()
        except TypeError:
            continue
        else:
            matrix_board = matrix(word)
            game_board(matrix_board)
            if first_player == "user" and second_player == "easy":
                while True:
                    user_input("X")
                    check_game(matrix_board)
                    easy_mode("O")
                    check_game(matrix_board)
            elif first_player == "easy" and second_player == "easy":
                while True:
                    easy_mode("X")
                    check_game(matrix_board)
                    easy_mode("O")
                    check_game(matrix_board)
            elif first_player == "easy" and second_player == "user":
                while True:
                    easy_mode("X")
                    check_game(matrix_board)
                    user_input("O")
                    check_game(matrix_board)
