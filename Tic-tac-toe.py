import re


def game_board(x):
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
    if abs(sum_X - sum_O) >= 2 or any(x_wins) == True and any(o_wins)== True:
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
            print("Game not finished")

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


def user_input():
    global matrix_board
    global gamer

    i = 0
    while i < 1:
        xy = input("Enter the coordinates:")

        out_range = re.search(r"[1-3] [1-3]", xy)
        not_digit = re.search(r"[^\s,\d]", xy)
        if not_digit is None:
            if out_range is not None:
                y, x = xy.split()
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
                    matrix_board[x][y] = gamer
                    game_board(matrix_board)
                    i += 1
                    if gamer == 'X':
                        gamer = 'O'
                    elif gamer == "O":
                        gamer = 'X'
                    continue
            else:
                print("Coordinates should be from 1 to 3!")
                continue
        else:
            print("You should enter numbers!")
            continue


# === GAME ===
word = "         "
gamer = 'X'
# generate matrix board
matrix_board = matrix(word)

while True:
    # print the game board
    game_board(matrix_board)

    # user input coordinates
    user_input()

    # check the game
    check_game(matrix_board)



