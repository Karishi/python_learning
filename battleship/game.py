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
    letter = coordinate_set[first_char]
    end_chars = coordinate_set[1:]
    number = int(coordinate_set[end_chars])
    return alph_to_num(letter), number

def random_ships(numExtraShips):
    ship_arrangement = [2,3,3,4,5]
    for i in range(numExtraShips):
        size = random.choice in ship_arrangement
        newShip = Ship(size, (), Ship.random_direction(), {}, "Y")
        newShip.name = name_ship(newShip)
        Ship.place_ship(newShip)

    
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
    print(f"X is {x} and Y is {y}")
    if hidden.spaces[x][y] != "o":
        visible.spaces[x][y] = hidden.spaces[x][y]
    else:
        visible.spaces[x][y] = "X"

class game:
    hidden_board = Board(10,10)
    visible_board = Board(hidden_board.width, hidden_board.height)
    title = "Joe-Bob"
    score = 0
    player = Player(title, score)
    place_basic_ships(hidden_board)
    print_both(hidden_board, visible_board)

game()
