import random
from source import _board
import _player
import _ship

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
        newShip = _ship(size, (), _ship.random_direction(), {}, "Y")
        newShip.name = name_ship(newShip)
        _ship.place_ship(newShip)

def name_ship(ship):
    if ship.size == 2:
        return "D"
    elif ship.size == 3:
        return "S"
    elif ship.size == 4:
        return "B"
    elif ship.size == 5:
        return "C"
    else:
        return "Y"
    
def place_basic_ships(board):
    destroyer = _ship(2,random.choice(board.unused),"",0,"D")
    _ship.place_ship(destroyer,board)
    submarine = _ship(3,random.choice(board.unused),"",0,"S")
    _ship.place_ship(submarine,board)
    cruiser = _ship(3,random.choice(board.unused),"",0,"R")
    _ship.place_ship(cruiser,board)
    battleship = _ship(4,random.choice(board.unused),"",0,"B")
    _ship.place_ship(battleship,board)
    carrier = _ship(5,random.choice(board.unused),"",0,"C")
    _ship.place_ship(carrier,board)

class game:
    my_board = _board.board(10,10)
    title = "Joe-Bob"
    score = 0
    player = _player.player(title, score)
    place_basic_ships(my_board)
    shown_board, header = _board.make_board(my_board)
    _board.print_board(shown_board,header)

game()
