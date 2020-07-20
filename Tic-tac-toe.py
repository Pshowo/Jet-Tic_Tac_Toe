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
    print(column_1)
    print(column_2)
    print(column_3)
    sum_X = sum([chars[x].count("X") for x in range(0, 3)])
    sum_O = sum([chars[x].count("O") for x in range(0, 3)])

    # Impossible
    if abs(sum_X - sum_O) >= 2:
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

while True:
    word = input("Enter cells: ")
    # word = "XO_XO_XOX"
    matrix_board = matrix(word)
    game_board(matrix_board)
    check_game(matrix_board)
