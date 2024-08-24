import random
from src.ship import *
from src.board import *

def test_trans_direction():
    direction = "N"
    ship_length = 3
    x_shift, y_shift = Ship.translate_direction(direction)
    my_board = Board(10,10)
    if x_shift == 0 and y_shift == 0:
        print("Error! Inaccurate input")
    x, y = get_unused(my_board)
    for i in range(ship_length):
        my_board.spaces[y+i*y_shift][x+i*x_shift] = "D"
    print_board(my_board.spaces, my_board.header)

def test_edge():
    myBoard = Board(10, 2)
    myShip = Ship(3, (0,1), 0, "D")
    print(f"With coordinates {myShip.coordinate} going North this returns {edge_check(myShip, myBoard)}.")
    myShip.direction = "E"
    print(f"With coordinates {myShip.coordinate} going East this returns {edge_check(myShip, myBoard)}.")
    myShip.direction = "S"
    print(f"With coordinates {myShip.coordinate} going South this returns {edge_check(myShip, myBoard)}.")
    myShip.direction = "W"
    print(f"With coordinates {myShip.coordinate} going West this returns {edge_check(myShip, myBoard)}.")
    place_ship(myShip, myBoard)
    print_board(myBoard.spaces, myBoard.header)

def test_place_ship():
    myBoard = Board(10, 10)
    myShip = Ship(3, get_unused(myBoard), "D")
    place_ship(myShip, myBoard)
    print_board(myBoard.spaces, myBoard.header)
    myShip.coordinate = (myShip.coordinate[0]+1, myShip.coordinate[1]+1)
    print(f"The ship is at {myShip.coordinate} and pointed {myShip.direction}.")

def test_place_pips():
    myBoard = Board(10, 10)
    myShip = Ship(4, (0, 5), "B")
    myShip.direction = "N"
    place_pips(myShip, myBoard)
    print_board(myBoard.spaces, myBoard.header)

def test_check_full_ship():
    myBoard = Board(11, 11)
    blockingShip = Ship(4, (1, 5), "B")
    blockingShip.direction = "N"
    crashingShip = Ship(5, (3, 3), "C")
    crashingShip.direction = "W"
    place_pips(blockingShip, myBoard)
    print(f"The check of the full ship reads as {check_full_ship(crashingShip, myBoard)}")
    crashingShip.coordinate = (5,3)
    print(f"The check of the full ship reads as {check_full_ship(crashingShip, myBoard)}")
    print_board(myBoard.spaces, myBoard.header)

def test_place_ship():
    myBoard = Board(10, 10)
    myShip = Ship(4, get_unused(myBoard), 0, "B")
    place_ship(myShip, myBoard)
    print_board(myBoard.spaces, myBoard.header)

def test_place_standard():
    myBoard = Board(10, 10)
    fill_standard_board(myBoard)
    print_board(myBoard.spaces, myBoard.header)

def test_off_1_check_full_placement():
    my_board = Board(10, 10)
    first_ship = Ship(4, (3, 3), "B")
    crashing_ship = Ship(4, (3, 6), "C")
    first_ship.direction = "N"
    crashing_ship.direction = "E"
    place_ship(first_ship, my_board)
    place_ship(crashing_ship, my_board)
    print_board(my_board.spaces, my_board.header)

test_off_1_check_full_placement()