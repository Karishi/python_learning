from node import initialize_full
import random
from player import Player, initialize_deck
from event import initialize_timeline


class Game:
    event_list = []
    def __init__(self) -> None:
        self.win_loss = None
    initialize_full(random(3,5))
    timeline = initialize_timeline(random(100,200))

my_game = Game
my_player = Player

    

def query_card(hand):
    card_number = 0
    for card in hand:
        card_number += 1
        print(f"Option ({card_number})")
        print(card.description)
        # TODO: Generate card descriptions for each card type.
    selected_number = input("Please select a card. > ")
    return hand[selected_number-1]




def main():
    initialize_full(3)
    deck = initialize_deck(my_player)
    my_player.deck = deck
    while my_game.win_loss is not None:
        event = my_game.event_list[0]
        event.event_effect(my_player)
        if my_game.num_incomplete <= 0:
            my_game.win_loss = "Win"
    if my_game.win_loss == "Win":
        print("Congratulations, you completed the craft. You are crafty!")
        quit
    elif my_game.win_loss == "Lose":
        print("Sorry, you ran out of time for your craft. Alas!")
        quit
    else:
        print("Win/Loss state is not working properly.")
        quit

main()