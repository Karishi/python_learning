from player import Player
from node import print_board, node_list
import random
from card import print_card



class Event:
    def __init__(self, time: int) -> None:
        self.time_value = time

    def event_effect(player):
        pass

class Energy_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)

    def event_effect(player, game):
        player.energy += 5
        Energy_Event.time += 5
        

class Loss_Event(Event):
    def __init__(self, time: int) -> None:
        super().__init__(time)

    def event_effect(player, game):
        game.win_loss = "Lose"

class Player_Turn_Event(Event):
    def __init__(self, time: int, player: int) -> None:
        super().__init__(time, player)

    def event_effect(player, game):
        print_board()
        chosen_card = game.query_card(player.hand)
        chosen_card.play_card(chosen_card)
        

player_turn = Player_Turn_Event(0, 1)

def initialize_timeline(duration, game):
    timeline = []
    timeline.append(player_turn)
    time_count = 5
    for i in range(int(duration/5)):
        energy_event = Event(time_count)
        time_count += 5
        timeline.append(energy_event)
    loss_event = Loss_Event(duration, game)
    timeline.append(loss_event)
    return timeline

