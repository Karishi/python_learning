warchest = 100
bet_value = 10

def bet():
    bet_value = input(f"Choose how much to bet, from 10 to your total of {warchest}.")
    if bet_value > warchest:
        bet_value = warchest
    elif bet_value < 10:
        bet_value = 10
    elif bet_value is not type(int):
        bet_value = 10


def win():
    warchest += bet_value
    print(f"Your victory when betting ${bet_value} brings you to ${warchest} total!")

def lose():
    warchest -= bet_value
    print(f"You lost ${bet_value}, leaving you with just ${warchest} left.")