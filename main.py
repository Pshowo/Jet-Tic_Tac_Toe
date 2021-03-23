from classes.game import Game
from classes.player import Player

def main():
    game = Game()
    players = game.menu()
    first_player = Player(players[0])
    second_player = Player(players[1])
    game.draw(game.empty_grid)

    while True:
        # move first player
        # print grid
        # check if someone 
        
        # move second player
        # print grid
        # check if someone wins
        break

if __name__ == "__main__":
    main()
