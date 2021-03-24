from classes.game import Game
from classes.player import Player, User

def main():
    game = Game()
    players = game.menu()
    first_player = Player(players[0])
    second_player = Player(players[1])
    game.draw(game.empty_grid)
    grid = game.empty_grid
    
    while True:
        first_player.make_move(grid)
        print(first_player)
        game.draw(grid)
        if game.check(grid):
            break

        second_player.make_move(grid)
        print(second_player)
        game.draw(grid)
        if game.check(grid):
            break

if __name__ == "__main__":
    main()

