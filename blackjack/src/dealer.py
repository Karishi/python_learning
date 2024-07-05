# A dealer's basic AI for Blackjack
import random

# Sets up the dealer's faceup and facedown card at the start of the game,
# including removing them from the main deck.
def initialize_dealer(deck):
    visible_card = random.choice(list(deck.items()))
    dealer_value = visible_card[1]
    # The dealer always treats an Ace that won't bust them as 11.
    # Thus, the dealer always counts a first-draw Ace as 11
    if dealer_value == 1:
        dealer_value += 10
    del deck[visible_card[0]]
    print('The dealer has drawn the ' + str(visible_card[0]) + " face up and another card face down.")
    print('You are certain you must beat at least ' + str(dealer_value + 1) + '.') 
    hidden_card = random.choice(list(deck.items()))
    dealer_value += hidden_card[1]
    del deck[hidden_card[0]]
    return visible_card, hidden_card, dealer_value

# Helps handle the times the dealer hits during the game.
def dealer_draw(deck):
    visible_card = random.choice(list(deck.items()))
    del deck[visible_card[0]]
    return visible_card

def discard_dealer(dealer_cards, discard_pile, dealer_hidden):
    while len(dealer_cards) > 0:
        drawn_card = random.choice(list(dealer_cards.items()))
        discard_pile[drawn_card[0]] = drawn_card[1]
        del dealer_cards[drawn_card[0]]
    drawn_card = dealer_hidden
    # "Move" the hidden card from hidden to discard pile
    discard_pile[drawn_card[0]] = drawn_card[1]
    del dealer_cards[drawn_card[0]]
    return drawn_card
