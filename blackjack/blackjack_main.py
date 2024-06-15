from deck_dict import deck
import random
from dealer import *
from currency import *

def game_continues(stay, score):
    if stay == False and score <= 21:
        return True

warchest = 100
bet_value = 10
stay = False
card_total = 0
player_drawn = {}
dealer_drawn = {} # For printing out the dealer's visible cards

# Set up the dealer's cards
dealer_visible, dealer_hidden, dealer_val = initialize_dealer(deck)
dealer_drawn[dealer_visible[0]] = dealer_visible[1]

bet_value = bet(warchest, bet_value)
print(f"You bet {bet_value}.")

# The while loop keeps us going as long as we hit and don't bust
while game_continues(stay, card_total):
    drawn_card = random.choice(list(deck.items()))
    player_drawn[drawn_card[0]] = drawn_card[1]
    del deck[drawn_card[0]]
    card_total += drawn_card[1]
    # Print out all the cards drawn by the player
    for key, value in player_drawn.items():
        print('You have the ' + str(key))
    print('Your current value is ' + str(card_total))
    # The player has the option to make an Ace worth 11 instead of 1.
    if drawn_card[1] == 1 and (card_total + 10) <= 21:
        reply_bad = True
        # Replies other than Y, N, y, n, yes, no, Yes, or No will be re-prompted.
        while reply_bad == True:
            reply = input('Do you want your Ace to be worth 11 instead of 1? Y/N > ')
            if reply.capitalize() == 'Y' or reply.capitalize() == 'Yes':
                card_total += 10
                reply_bad = False
            elif reply.capitalize() == 'N' or reply.capitalize() == 'No':
                reply_bad = False
    if card_total > 21:
        print('Sorry, that\'s a bust!')
        lose(warchest, bet_value)
        quit
    else:
        reply_bad = True #These two lines cause the program
        while reply_bad: #to re-ask if you give bad input
            hit_or_stay = input('Do you want to Hit or Stay? H/S > ')
            if hit_or_stay.capitalize() == 'S' or hit_or_stay.capitalize() == 'Stay':
                print('You decided to stay at ' + str(card_total) + '.')
                print('The dealer reveals that the hidden card was the ' + str(dealer_hidden[0]) + '.')
                for key, value in dealer_drawn.items():
                    print("The dealer also had the " + str(key) + ".")
                print("This gives the dealer a total of " + str(dealer_val) + ".")
                if dealer_val >= card_total and dealer_val <= 21:
                    print('Sorry, the house wins.')
                    lose(warchest, bet_value)
                elif dealer_val > 21:
                    print("The dealer went bust! You win!")
                    win(warchest, bet_value)
                else:
                    print('Your total of ' + str(card_total) + ' beats the house!')
                    win(warchest, bet_value)
                stay = True
                reply_bad = False
            elif hit_or_stay.capitalize() == 'H' or hit_or_stay.capitalize() == 'Hit':
                reply_bad = False
        # The dealer is required to hit if below 17, and required to stay if at 17+.
        if dealer_val < 17:
            card = dealer_draw(deck)
            if (dealer_val + 11) <= 21 and card[1] == 1:
                dealer_val += 11
            else:
                dealer_val += card[1]
            dealer_drawn[card[0]] = card[1]
            # The main reason the hidden card isn't included in the dictionary is
            # so the reveal of visible cards can be easily iterated over.
            print("The dealer's visible cards are:")
            for key, value in dealer_drawn.items():
                print(str(key))
# If the player doesn't bust in the middle, the game ends when the loop ends:
# when the results of staying where they do are revealed.
quit

