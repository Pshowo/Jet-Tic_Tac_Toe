
def game_board(x):
    print("---------")
    print(f"| {x[0]} {x[1]} {x[2]} |")
    print(f"| {x[3]} {x[4]} {x[5]} |")
    print(f"| {x[6]} {x[7]} {x[8]} |")
    print("---------")

x = input("Enter cells: ")
game_board(x)