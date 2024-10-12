from player import Player
from node import print_board
import random

class Event:
    def __init__(self, time: int) -> None:
        self.time_value = time

    def event_effect(player):
        pass

class Energy_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)

    def event_effect(player):
        player.energy += 5

class Loss_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)

    def event_effect(player):
        print("Too late! You didn't complete the craft.")
        quit()

class Player_Turn_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)
        tiebreaker = random.randint(1,100)

    def event_effect(player):
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