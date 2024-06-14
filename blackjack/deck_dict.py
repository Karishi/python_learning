# A constructor for a deck dict, filling it with names ("Value of Suit")
# and integer values. Aces - detected as "if value == 1" - will offer the
# option to count them as 11 instead during play.
import random
from dealer import *

deck = {}
for suit_num in range(0,4):
    if suit_num == 0:
        suit = "Spades"
    elif suit_num == 1:
        suit = "Hearts"
    elif suit_num == 2:
        suit = "Clubs"
    else:
        suit = "Diamonds"
# Nested for loops because the suits are identical except for suit name
    for title_num in range(1, 14):
        if title_num == 1:
            title = "Ace"
            value = 1
        elif title_num == 11:
            title = "Jack"
            value = 10
        elif title_num == 12:
            title = "Queen"
            value = 10
        elif title_num == 13:
            title = "King"
            value = 10
        # For 2-10 the number is the title and value, so they can be lumped together
        else:
            title = str(title_num)
            value = title_num
        card_title = title + " of " + suit
        deck[card_title] = value

