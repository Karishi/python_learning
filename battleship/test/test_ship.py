import random
from src.ship import *
from src.board import *

def test_trans_direction():
    direction = "N"
    ship_length = 3
    x_shift,y_shift = Ship.translate_direction(direction)
    my_board = Board(10,10)
    if x_shift == 0 and y_shift == 0:
        print("Error! Inaccurate input")
    x, y = get_unused(my_board)
    for i in range(ship_length):
        my_board.spaces[y+i*y_shift][x+i*x_shift] = "D"
    print_board(my_board.spaces, my_board.header)

def test_edge():
    myBoard = Board(10,10)
    myShip = Ship(3, (3,1), {}, "D")
    print(f"With coordinates 1,1 going North this returns {edge_check(myShip, myBoard)}.")
    myShip.direction = "E"
    print(f"With coordinates 1,1 going East this returns {edge_check(myShip, myBoard)}.")
    myShip.direction = "S"
    print(f"With coordinates 1,1 going South this returns {edge_check(myShip, myBoard)}.")
    myShip.direction = "W"
    print(f"With coordinates 1,1 going West this returns {edge_check(myShip, myBoard)}.")

def test_place_ship():
    myBoard = Board(10,10)
    myShip = Ship(3, get_unused(myBoard), {}, "D")
    place_ship(myShip, myBoard)
    print_board(myBoard.spaces, myBoard.header)
    myShip.coordinate = (myShip.coordinate[0]+1,myShip.coordinate[1]+1)
    print(f"The ship is at {myShip.coordinate} and pointed {myShip.direction}.")

def test_place_pips():
    myBoard = Board(10,10)
    myShip = Ship(4, (5,7), {}, "B")
    myShip.direction = "N"
    place_pips(myShip, myBoard)
    print_board(myBoard.spaces, myBoard.header)

test_place_pips()