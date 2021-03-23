from classes.game import Game
from classes.player import Player, User

def main():
    game = Game()
    players = game.menu()
    first_player = Player(players[0])
    second_player = Player(players[1])
    game.draw(game.empty_grid)

    while True:
        # get input and move first player
        # print grid
        # check if someone wins, if true exit
        
        # get input and move second player
        # print grid
        # check if someone wins, if true exit
        break

if __name__ == "__main__":
    # main()
    user = User(("user", "X"))
    game = Game()
    grid = game.empty_grid
    print(grid)
    print(user.mark)
    print(user.type)
    print(user)
    user.make_move(user.user_input(grid), grid)
    print(grid)
    user.make_move(user.user_input(grid), grid)
    print(grid)

