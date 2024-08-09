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
    first_char = coordinate_set[1]
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
    destroyer = Ship(2,random.choice(board.unused),"",0,"D")
    Ship.place_ship(destroyer,board)
    submarine = Ship(3,random.choice(board.unused),"",0,"S")
    Ship.place_ship(submarine,board)
    cruiser = Ship(3,random.choice(board.unused),"",0,"R")
    Ship.place_ship(cruiser,board)
    battleship = Ship(4,random.choice(board.unused),"",0,"B")
    Ship.place_ship(battleship,board)
    carrier = Ship(5,random.choice(board.unused),"",0,"C")
    Ship.place_ship(carrier,board)

class game:
    my_board = Board.board(10,10)
    title = "Joe-Bob"
    score = 0
    player = Player.player(title, score)
    place_basic_ships(my_board)
    shown_board, header = Board.make_board(my_board)
    Board.print_board(shown_board,header)

game()
