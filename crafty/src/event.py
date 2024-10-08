from player import Player
from node import print_board

class Event:
    def __init__(self, time) -> None:
        self.time_value = time
    
    def energy_gain(player):
        player.energy += 5

    def lose(player):
        print("Too late! You didn't complete the craft.")
        quit()

    def player_turn(player):
        print_board()
        