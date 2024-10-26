from node import initialize_full, print_node
from card import Gentle_Sort
import random
from player import Player
from event import initialize_timeline


class Game:
    event_list = []
    def __init__(self) -> None:
        self.num_incomplete = 0
        self.win_loss = None
    initialize_full(random(3,5))
    timeline = initialize_timeline(random(100,200))

my_game = Game
my_card = Gentle_Sort
my_player = Player


def check_victory(game):
    if game.num_incomplete == 0:
        return True
    else:
        return None
    

def query_card(hand):
    card_number = 0
    for card in hand:
        card_number += 1
        print(f"Option ({card_number})")
        print(card.description)
        # TODO: Generate card descriptions for each card type.
    selected_number = input("Please select a card. > ")
    return selected_number


def query_node(node_list):
    node_number = 0
    for node in node_list:
        node_number += 1
        print(f"({node_number}): ", end = "")
        print_node(node)
    selected_number = input("Please select a target. > ")
    return selected_number

def main():
    while my_game.win_loss is not None:
        event = my_game.event_list[0]
        event.event_effect(my_player)
    if my_game.win_loss == "Win":
        print("Congratulations, you completed the craft. You are crafty!")
        quit
    elif my_game.win_loss == "Lose":
        print("Sorry, you ran out of time for your craft. Alas!")
        quit