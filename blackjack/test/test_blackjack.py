import pytest
from src.currency import win, lose
from src.blackjack_main import choose_hit_or_stay, discard

def test_win():
    value = win(100,10)
    assert value == 110

def test_lose():
    value = lose(100,10)
    assert value == 90

def test_choose_hit_or_stay():
    victory = choose_hit_or_stay(blackjack_main.stay)
    assert victory == None

def test_discard():
    player_cards = {'King of Hearts': 10, 'Queen of Spades': 10, 'Ace of Hearts': 1}
    dealer_cards = {'2 of Diamonds': 2, '8 of Hearts': 8, '8 of Clubs': 8}
    discard_copy = {**player_cards, **dealer_cards}
    discard_pile = discard(player_cards, dealer_cards)
    assert discard_pile == discard_copy
