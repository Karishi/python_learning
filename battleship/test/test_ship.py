import random
import ship
import board

def test_unused_check():
    myship = ship(3, (5,5), ship.random_direction(), 0, "D")
    print(f"On the first test it returns {ship.check_against_unused(myship)}")
    print(f"On the second test it returns {ship.check_against_unused(myship)}")

def test_place_ship():
    ship.random_ships(1)

def test_trans_direction():
    direction = "N"
    ship_length = 3
    x_shift,y_shift = ship.translate_direction(direction)
    my_board = board.Board(10,10)
    if x_shift == 0 and y_shift == 0:
        print("Error! Inaccurate input")
    x, y = ship.randomize_ship_start(my_board)
    for i in range(ship_length):
        my_board.spaces[y+i*y_shift][x+i*x_shift] = "D"
    board.print_board(my_board.spaces, my_board.header)

def test_edge():
    myBoard = board.Board(10,10)
    myShip = ship.Ship(3, (1,1), "N", {}, "D")
    print(f"With coordinates 1,1 going North this returns {ship.edge_check(myShip, myBoard)}.")
    myShip.direction = "E"
    print(f"With coordinates 1,1 going East this returns {ship.edge_check(myShip, myBoard)}.")
    myShip.direction = "S"
    print(f"With coordinates 1,1 going South this returns {ship.edge_check(myShip, myBoard)}.")
    myShip.direction = "W"
    print(f"With coordinates 1,1 going West this returns {ship.edge_check(myShip, myBoard)}.")

def test_place_ship():
    myBoard = board.Board(10,10)
    myShip = ship.Ship(3, ship.get_unused(myBoard), ship.random_direction(), {}, "D")
    ship.place_ship(myShip, myBoard)
    board.print_board(myBoard.spaces, myBoard.header)

test_place_ship()