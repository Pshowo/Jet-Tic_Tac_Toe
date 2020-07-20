
def game_board(x):
    print("---------")
    print(f"| {x[0]} {x[1]} {x[2]} |")
    print(f"| {x[3]} {x[4]} {x[5]} |")
    print(f"| {x[6]} {x[7]} {x[8]} |")
    print("---------")

def check_game(x):
    # Game not finished
    # Draw
    # X wins
    if x[0:3] == "XXX" or x[3:6] == "XXX":
        pass
    # O wins
    # Impossible

def matrix(x):
    board = []
    for i in range(4):
        if i == 0:
            list_a = []
            for j in range(1,4):
                list_a.append(x[j])
            board.append(list_a)
        elif i == 1:
            list_a = []
            for j in range(3,6):
                list_a.append(x[j])
            board.append(list_a)
        elif i == 2:
            list_a = []
            for j in range(6, len(x)):
                list_a.append(x[j])
            board.append(list_a)

    print(board)

# x = input("Enter cells: ")
# game_board(x)
matrix("XXXOO__O_")