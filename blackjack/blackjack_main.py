from deck_dict import deck
import random
from dealer import *
from currency import *

stay = False
card_total = 0
player_drawn = {}
dealer_faceup_cards = {}
discard_pile = {}
dealer_visible, dealer_hidden, dealer_val = initialize_dealer(deck)
dealer_faceup_cards[dealer_visible[0]] = dealer_visible[1]

def round_continues(stay, score):
    if stay == False and score <= 21:
        return True
    
def discard(player_cards, dealer_cards):
    for key, value in player_cards:
        discard_pile[player_cards[key]] = player_cards[value]
        del player_cards[key]
    dealer_discard(dealer_cards, discard_pile, dealer_hidden)
    
def draw_a_card():
    drawn_card = random.choice(list(deck.items()))
    player_drawn[drawn_card[0]] = drawn_card[1]
    del deck[drawn_card[0]]
    return drawn_card

def reveal_player_cards():
    for key, value in player_drawn.items():
        print('You have the ' + str(key))
    print('Your current value is ' + str(card_total))

def upgrade_ace(card_total):
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
            
def bust():
    print('Sorry, that\'s a bust!')
    lose(warchest, bet_value)

def choose_hit_or_stay(stay):
    reply_bad = True #These two lines cause the program
    while reply_bad: #to re-ask if you give bad input
        hit_or_stay = input('Do you want to Hit or Stay? H/S > ')
        if hit_or_stay.capitalize() == 'S' or hit_or_stay.capitalize() == 'Stay':
            print('You decided to stay at ' + str(card_total) + '.')
            print('The dealer reveals that the hidden card was the ' + str(dealer_hidden[0]) + '.')
            for key, value in dealer_faceup_cards.items():
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

def dealer_hit(dealer_val):
    if dealer_val < 17:
        card = dealer_draw(deck)
        if (dealer_val + 11) <= 21 and card[1] == 1:
            dealer_val += 11
        else:
            dealer_val += card[1]
        dealer_faceup_cards[card[0]] = card[1]
        # The main reason the hidden card isn't included in the dictionary is
        # so the reveal of visible cards can be easily iterated over.
        print("The dealer's visible cards are:")
        for key, value in dealer_faceup_cards.items():
            print(str(key))

def choose_leave_or_continue():
    reply_bad = True #These two lines cause the program
    while reply_bad: #to re-ask if you give bad input
        leave_or_continue = input(f"You have ${warchest} left. Do you want to Leave or Continue playing? > ")
        if leave_or_continue.capitalize() == 'L' or leave_or_continue.capitalize() == 'Leave':
            if warchest > 100:
                print(f"You came out with ${warchest-100} more than you came in with! Good job beating the house!")
                quit
            elif warchest == 100:
                print("You broke even exactly. Getting to play a couple rounds 'for free' is kind of a moral victory.")
                quit
            else:
                print(f"You lost ${100-warchest} to the house. Hopefully you had fun regardless.")
            reply_bad = False
            quit
        elif leave_or_continue.capitalize() == 'C' or leave_or_continue.capitalize() == 'Continue':
            reply_bad = False

def lost_it_all():
    print('Sorry, you lost it all. The house wins...entirely.')
    quit

warchest = 100
bet_value = 10

while warchest >= 10:
    stay = False
    card_total = 0
    discard(player_drawn, dealer_faceup_cards)

    dealer_visible, dealer_hidden, dealer_val = initialize_dealer(deck, discard_pile)
    dealer_faceup_cards[dealer_visible[0]] = dealer_visible[1]

    bet_value = bet(warchest, bet_value)

    while round_continues(stay, card_total):
        drawn_card = draw_a_card()
        card_total += drawn_card[1]
        reveal_player_cards()
        # The player has the option to make an Ace worth 11 instead of 1.
        upgrade_ace(card_total)
        if card_total > 21:
            bust()
        else:
            choose_hit_or_stay(stay)
            # The dealer is required to hit if below 17, and required to stay if at 17+.
            dealer_hit(dealer_val)
    # If the player doesn't bust in the middle, the game ends when the loop ends:
    # when the results of staying where they do are revealed.
    choose_leave_or_continue()
lost_it_all()
