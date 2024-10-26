from card import draw_hand
from node import print_board

class Player:
    def __init__(self) -> None:
        self.time = 0
        self.hand = []
        self.deck = []
        self.discard = []
        self.status = []
        self.energy = 100

    def take_a_turn(hand, deck):
        draw_hand(hand, deck, 4)
        print_board()

