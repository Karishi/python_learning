import pytest
from src.currency import win, lose
from src.blackjack_main import choose_hit_or_stay

def test_win():
    value = win(100,10)
    assert value == 110

def test_lose():
    value = lose(100,10)
    assert value == 90

def test_choose_hit_or_stay():
    victory = choose_hit_or_stay(blackjack_main.stay)
    assert victory == None
