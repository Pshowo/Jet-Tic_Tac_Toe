import re

def game_board(x):
    print("---------")
    print(f"| {x[0][0]} {x[0][1]} {x[0][2]} |")
    print(f"| {x[1][0]} {x[1][1]} {x[1][2]} |")
    print(f"| {x[2][0]} {x[2][1]} {x[2][2]} |")
    print("---------")


def check_game(chars):
    column_1 = [chars[x][0] for x in range(3)]
    column_2 = [chars[x][1] for x in range(3)]
    column_3 = [chars[x][2] for x in range(3)]

    sum_X = sum([chars[x].count("X") for x in range(0, 3)])
    sum_O = sum([chars[x].count("O") for x in range(0, 3)])
 
    # Impossible
    if abs(sum_X - sum_O) >= 2:
        print("Impossible")
    elif column_1 == list("XXX") and column_2 == list("OOO"):
        print("Impossible")
    elif column_2 == list("XXX") and column_3 == list("OOO"):
        print("Impossible")
    elif column_1 == list("OOO") and column_2 == list("XXX"):
        print("Impossible")
    elif column_2 == list("OOO") and column_3 == list("XXX"):
        print("Impossible")

    else:
    # win configuration
    # X wins
        if chars[0] == list("XXX") or chars[1] == list("XXX") or chars[2] == list("XXX"):
            print("X wins")
        elif chars[0][0] == "X" and chars[1][0] == "X" and chars[2][0] == "X":
            print("X wins")
        elif chars[0][1] == "X" and chars[1][1] == "X" and chars[2][1] == "X":
            print("X wins")
        elif chars[0][2] == "X" and chars[1][2] == "X" and chars[2][2] == "X":
            print("X wins")
        elif chars[0][0] == "X" and chars[1][1] == "X" and chars[2][2] == "X":
            print("X wins")
        elif chars[0][2] == "X" and chars[1][1] == "X" and chars[2][0] == "X":
            print("X wins")

    # O wins
        elif chars[0] == list('OOO') or chars[1] == list('OOO') or chars[2] == list('OOO'):
            print("O wins")
        elif chars[0][0] == "O" and chars[1][0] == "O" and chars[2][0] == "O":
            print("O wins")
        elif chars[0][1] == "O" and chars[1][1] == "O" and chars[2][1] == "O":
            print("O wins")
        elif chars[0][2] == "O" and chars[1][2] == "O" and chars[2][2] == "O":
            print("O wins")
        elif chars[0][0] == "O" and chars[1][1] == "O" and chars[2][2] == "O":
            print("O wins")
        elif chars[0][2] == "O" and chars[1][1] == "O" and chars[2][0] == "O":
            print("O wins")

    # Game not finished
        elif "_" in chars[0] or "_" in chars[1] or "_" in chars[2]:
            print("Game not finished")

    # Draw
        elif "_" not in chars[0] and "_" not in chars[1] and "_" not in chars[2]:
            print("Draw")


def matrix(x):
    board = []
    for i in range(4):
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

def user_input():
    global matrix_board
    i = 0
    while i < 3:
        i += 1
        xy = input("Enter the coordinates:")

        out_range = re.search(r"[1-3] [1-3]", xy)
        not_digit = re.search(r"[^\s,\d]", xy)
        if not_digit is None:
            if out_range is not None:
                x, y = xy.split()
                x = int(x)
                y = int(y)
                
                if x == 1:
                    x = 2 
                elif x == 2:
                    x = 1
                elif x == 3:
                    x = 0
                
                if y == 1:
                    y = 0
                elif y == 2:
                    y = 1
                elif y == 3:
                    y = 2 
                
                if matrix_board[x][y] == 'X' or matrix_board[x][y] == 'O':
                    print("This cell is occupied! Choose another one!")
                else:
                    matrix_board[x][y] = "X"
                    return game_board(matrix_board)
            else:
                print("Coordinates should be from 1 to 3!")
                continue
        else:
            print("You should enter numbers!")
            continue


# word = "XO_XO_XOX"
word = input("Enter cells: ")

# generate matrix board
matrix_board = matrix(word)

# print the game board
game_board(matrix_board)

# user input coordinates
user_input()

# check the game
# check_game(matrix_board)
