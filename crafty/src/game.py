from node import initialize_full
from card import Gentle_Sort
import random


class Game:
    deck = []
    hand = []
    discard = []
    def __init__(self) -> None:
        self.max_time = 100
        self.time = 100
        self.num_incomplete = 0
        self.win_loss = None
    initialize_full(random(3,5))

my_game = Game
my_card = Gentle_Sort

def check_victory(game):
    if game.num_incomplete == 0:
        return True
    else:
        return None