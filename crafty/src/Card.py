from node import progress_node, node_list
from game import check_victory, my_game

class Card:
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int, description: str) -> None:
        self.title = title
        self.cost = time_cost
        self.impact = impact
        self.element = element
        self.bonus = bonus_energy_cost
        self.target = target
        self.description = description

    def card_effect(game, node):
        pass


def standard_effect(card, game, node):
    game.time -= card.cost
    node_complete = progress_node(card.value, card.element, node)
    if node_complete:
        game.num_incomplete -= 1
        game.win_loss = check_victory(game)


def draw(hand, deck):
    hand.append(deck.pop(0))


def draw_hand(hand, deck, hand_size):
    for i in range(hand_size):
        draw(hand, deck)

def sample_deck_setup():
    deck = my_game.deck
    hand = my_game.hand

def print_card(card):
    print(f"{card.title} ({card.cost}) [{card.element}]")
    print(card.description)