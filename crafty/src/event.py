from player import Player
from node import print_board
import random
from game import my_game, query_card, query_node
from card import print_card

class Event:
    def __init__(self, time: int) -> None:
        self.time_value = time

    def event_effect(player):
        pass

class Energy_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)

    def event_effect(player, time):
        player.energy += 5
        Energy_Event.time += 5
        

class Loss_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)

    def event_effect(player):
        my_game.win_loss = "Lose"

class Player_Turn_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)

    def event_effect(player):
        print_board()
        count = 0
        query_card(player.hand)
        

player_turn = Event(0)

def initialize_timeline(duration):
    timeline = []
    timeline.append(player_turn)
    time_count = 5
    for i in range(int(duration/5)):
        energy_event = Event(time_count)
        time_count += 5
        timeline.append(energy_event)
    loss_event = Loss_Event(duration)
    timeline.append(loss_event)
    return timeline