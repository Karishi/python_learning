from node import progress_node, node_list
from game import check_victory, my_game

class Card:
    def __init__(self, title: str, time_cost: int, impact: int, element: str, bonus_energy_cost: int, target: int) -> None:
        self.title = title
        self.cost = time_cost
        self.impact = impact
        self.element = element
        self.bonus = bonus_energy_cost
        self.target = target


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
