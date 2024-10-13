from node import initialize_full
from card import Gentle_Sort
import random
from player import Player
from event import initialize_timeline


class Game:
    deck = []
    hand = []
    discard = []
    def __init__(self) -> None:
        self.time = 0
        self.num_incomplete = 0
        self.win_loss = None
    initialize_full(random(3,5))
    initialize_timeline(random(100,200))

my_game = Game
my_card = Gentle_Sort
my_player = Player

def check_victory(game):
    if game.num_incomplete == 0:
        return True
    else:
        return None