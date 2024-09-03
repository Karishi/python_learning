import random
from src.board import *
from src.player import *
from src.ship import *

def alph_to_num(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,len(alphabet)):
        test_let = slice(i,i+1)
        if letter.capitalize() == alphabet[test_let]:
            return i
    return -1

def split_coordinates(coordinate_set):
    first_char = coordinate_set[0]
    letter = alph_to_num(first_char)
    end_chars = coordinate_set[1:]
    number = int(end_chars)
    return letter, number

def random_ships(numExtraShips, my_board):
    ship_arrangement = [2,3,3,4,5]
    for i in range(numExtraShips):
        size = random.choice in ship_arrangement
        my_ship = Ship(size, (), Ship.random_direction(), {}, "Y")
        my_ship.name = name_ship(my_ship)
        place_ship(my_ship, my_board)

    
def place_basic_ships(board):
    destroyer = Ship(2, random.choice(board.unused), "D")
    place_ship(destroyer,board)
    submarine = Ship(3, random.choice(board.unused), "S")
    place_ship(submarine,board)
    cruiser = Ship(3, random.choice(board.unused), "R")
    place_ship(cruiser,board)
    battleship = Ship(4, random.choice(board.unused), "B")
    place_ship(battleship,board)
    carrier = Ship(5, random.choice(board.unused), "C")
    place_ship(carrier,board)

# Usable during testing to see what's going on.
# Disable for real play by changing instances to print_board(visible).
def print_both(hidden, visible):
    print_board(hidden.spaces, hidden.header)
    print_board(visible.spaces, visible.header)

def fire_torpedo(target, hidden, visible):
    x, y = split_coordinates(target)
    if hidden.spaces[x][y-1] != "o":
        visible.spaces[x][y-1] = hidden.spaces[x][y-1]
        sink_ship(hidden, visible, x, y)
    else:
        visible.spaces[x][y-1] = "X"

def aim_torpedo(target, visible):
    x, y = split_coordinates(target)
    if visible.spaces[x][y-1] != "o":
        return True
    else:
        return False

def target(visible):
    attempt = input("Where will you fire? > ")
    while aim_torpedo(attempt, visible):
        attempt = input("You've already shot there! Where will you aim? > ")
    return attempt

def loop_until_win(hidden, visible):
    while hidden.unsunk > 0:
        print_both(hidden, visible)
        print(f"There are {hidden.unsunk} ships remaining.")
        fire_torpedo(target(visible), hidden, visible)
    print("Congratulations, you win!")

class game:
    hidden_board = Board(10,10)
    visible_board = Board(hidden_board.width, hidden_board.height)
    title = "Joe-Bob"
    score = 0
    player = Player(title, score)
    fill_standard_board(hidden_board)
    loop_until_win(hidden_board, visible_board)

game()