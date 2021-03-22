import random
import re
import numpy as np


def game_board(x):
    """
    Draws the board game on the console.

    Parameters
    ----------
    x : list
        List with sequence of chars

    Returns
    -------
    Prints game board on the console.

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


def check_game(chars):
    """[summary]

    Parameters
    ----------
    chars : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
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
        c1 = abs(sum_X - sum_O) >= 2
        c2 = any(x_wins) == True
        c3 = any(o_wins) == True
        print("Imposible")
        return False
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
            return True

        # Draw
        elif " " not in chars[0] and " " not in chars[1] and " " not in chars[2]:
            print("Draw")
            exit()


def matrix(x):
    """
    Converts sequence of chars into a list with chars.

    Parameters
    ----------
    x : str
        Sequence of chars

    Returns
    -------
    out : list
        list of marks

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> matrix("OX_XOOOXX")
    [['O', 'X', '_'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    """
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


def user_input(mark, matrix_board):
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
    return matrix_board


def easy_mode(mark, mode, chars):
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
        if chars[x][y] == 'X' or chars[x][y] == 'O':
            continue
        else:
            chars[x][y] = mark
            print('Making move level "{}"'.format(mode))
            # game_board(chars)
            i += 1
            break
    return chars


def medium_mode(mark, chars):
    """
    - If it already has two in a row and can win with one further move, it does so.
    - If its opponent can win with one move, it plays the move necessary to block this.
    - Otherwise, it makes a random move.

    Parameters
    ----------
    mark : str
        The mark which use in the game.

    chars : list
        The list of sequences chars.

    Returns
    -------

    """
    contr_mark = "O" if mark == "X" else "X"

    # convert chars into np array with 0 and 1
    ar = np.char.count(np.array(chars), contr_mark)
    ar2 = np.multiply(np.char.count(np.array(chars), "O"), -1)
    ar = np.add(ar, ar2)
    del ar2

    ar_d1 = ar.diagonal().sum()  # checks first diagonal
    ar_d2 = np.flip(ar, 1).diagonal().sum()  # checks secondary diagonal
    a1 = [np.sum(ar[0]), np.sum(ar[1]), np.sum(ar[2])]  # check all rows
    a2 = [np.sum(ar.T[0]), np.sum(ar.T[1]), np.sum(ar.T[2])]  # check all columns

    # diagonal
    if ar_d1 == 2:
        for i in range(0, 3):
            a = chars[i][i]
            if chars[i][i] == ' ' or chars[i][i] == '_':
                chars[i][i] = mark
                break
            else:
                continue
    # Secondary diagonal
    elif ar_d2 == 2:
        chars[0][2] = mark if chars[0][2] == ' ' or chars[0][2] == '_' else chars[0][2]
        chars[1][1] = mark if chars[1][1] == ' ' or chars[1][1] == '_' else chars[1][1]
        chars[2][0] = mark if chars[2][0] == ' ' or chars[2][0] == '_' else chars[2][0]

    else:
        # rows
        if 2 in a1:
            for ind, val in enumerate(a1):  # if next(ar_rows) == 2:
                if val == 2:
                    row = True
                    for k in range(0, 3):
                        if chars[ind][k] == ' ' or chars[ind][k] == '_':
                            chars[ind][k] = mark
                            break
                else:
                    row = False
        # columns
        elif 2 in a2:
            for ind, val in enumerate(a2):
                if val == 2:
                    row = True
                    for k in range(0, 3):
                        if chars[k][ind] == ' ' or chars[k][ind] == '_':
                            chars[k][ind] = mark
                            break
                else:
                    cols = False
        else:
            chars = easy_mode(mark, "medium", chars)
    return chars


def check_gamer(word):
    """
    Checks which player starts the game.
    :param word: starting sequence
    :return: X or O
    """
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
    gamer = "X"

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
                    matrix_board = user_input("X", matrix_board)
                    check_game(matrix_board)
                    matrix_board = easy_mode("O", "easy", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
            elif first_player == "easy" and second_player == "easy":
                while True:
                    matrix_board = easy_mode("X", "easy", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
                    matrix_board = easy_mode("O", "easy", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
            elif first_player == "easy" and second_player == "user":
                while True:
                    matrix_board = easy_mode("X", "easy", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
                    matrix_board = user_input("O", matrix_board)
                    check_game(matrix_board)
            elif first_player == "user" and second_player == "medium":
                while True:
                    matrix_board = user_input("X", matrix_board)
                    check_game(matrix_board)
                    matrix_board = medium_mode("O", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
            elif first_player == "medium" and second_player == "user":
                while True:
                    matrix_board = medium_mode("X", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
                    matrix_board = user_input("O", matrix_board)
                    check_game(matrix_board)
            elif first_player == "medium" and second_player == "medium":
                while True:
                    matrix_board = medium_mode("X", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
                    matrix_board = medium_mode("O", matrix_board)
                    game_board(matrix_board)
                    check_game(matrix_board)
