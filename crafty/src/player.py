from card import draw_hand, Card
from node import print_board
from game import my_player
from complete_cards import Complete_Card
from deductive_cards import Deductive_Card
from desperate_cards import Desperate_Card
from gentle_cards import Gentle_Card
from patient_cards import Patient_Card
from thorough_cards import Thorough_Card

class Player:
    def __init__(self) -> None:
        self.time = 0
        self.hand = []
        self.deck = []
        self.discard = []
        self.status = []
        self.energy = 0

    def take_a_turn(hand, deck):
        draw_hand(hand, deck, 4)
        print_board()

def initialize_deck():
    thorough_cut = Thorough_Card("Thorough Cut", 3, 5, "X", 0)
    thorough_mix = Thorough_Card("Thorough Mix", 3, 5, "S", 0)
    thorough_arrange = Thorough_Card("Thorough Arrange", 3, 5, "A", 0)
    thorough_join = Thorough_Card("Thorough Join", 3, 5, "D", 0)
    thorough_bind = Thorough_Card("Thorough Bind", 3, 5, "Y", 0)
    thorough_sort = Thorough_Card("Thorough Sort", 3, 5, "O", 0)
    my_player.deck.append(thorough_arrange)
    my_player.deck.append(thorough_bind)
    my_player.deck.append(thorough_cut)
    my_player.deck.append(thorough_join)
    my_player.deck.append(thorough_mix)
    my_player.deck.append(thorough_sort)
    return my_player.deck