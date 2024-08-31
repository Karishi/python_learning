import random
from src.main import *

def test_alph():
    num = alph_to_num("z")
    print(f"Number is {num}.")

def test_split():
    user_input = "F4"
    my_board = Board(10,10)
    x,y = split_coordinates(user_input)
    my_board.spaces[x][y-1] = "X"
    print_board(my_board.spaces, my_board.header)

def test_fire_torpedo():
    hidden_board = Board(10, 10)
    fill_standard_board(hidden_board)
    visible_board = Board(10, 10)
    fire_torpedo("E5", hidden_board, visible_board)
    print_both(hidden_board, visible_board)

def test_loop_to_win():
    hidden = Board(10, 10)
    visible = Board(10, 10)
    battleship = Ship(4, (5,5), "B")
    place_ship(battleship, hidden, "S")
    loop_until_win(hidden, visible)

test_loop_to_win()