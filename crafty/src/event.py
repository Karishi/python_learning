from player import Player
from node import print_board

class Event:
    def __init__(self, time: int) -> None:
        self.time_value = time
    
    def energy_gain(player):
        player.energy += 5

    def lose(player):
        print("Too late! You didn't complete the craft.")
        quit()

    def player_turn(player):
        print_board()

player_turn = Event(0)

def initialize_timeline(duration):
    timeline = []
    timeline.append(player_turn)
    time_count = 5
    for i in range(int(duration/5)):
        energy_event = Event(time_count)
        time_count += 5
        timeline.append(energy_event)
    loss_event = Event(duration)
    timeline.append(loss_event)