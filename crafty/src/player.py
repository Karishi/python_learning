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

def initialize_deck(player):
    thorough_cut = Thorough_Card("Thorough Cut", 3, 5, "X", 0)
    thorough_mix = Thorough_Card("Thorough Mix", 3, 5, "S", 0)
    thorough_arrange = Thorough_Card("Thorough Arrange", 3, 5, "A", 0)
    thorough_join = Thorough_Card("Thorough Join", 3, 5, "D", 0)
    thorough_bind = Thorough_Card("Thorough Bind", 3, 5, "Y", 0)
    thorough_sort = Thorough_Card("Thorough Sort", 3, 5, "O", 0)
    player.deck.append(thorough_arrange)
    player.deck.append(thorough_bind)
    player.deck.append(thorough_cut)
    player.deck.append(thorough_join)
    player.deck.append(thorough_mix)
    player.deck.append(thorough_sort)
    return player.deck