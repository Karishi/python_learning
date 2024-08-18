from src.board import *

def test_make():
    myBoard = Board(10,10)
    spaces = myBoard.spaces
    header = myBoard.header
    spaces[3][4] = "D"
    print_board(spaces,header)
    assert spaces[3][3] == "o"
    assert spaces[3][4] == "o"
#Should give one success and one failure

def test_unused():
    myBoard = Board(10,10)
    assert len(myBoard.unused) == 100
    spaces = myBoard.spaces
    header = myBoard.header
    x = 10
    y = 10
    if (x,y) in myBoard.unused:
        myBoard.spaces[y-1][x-1] = "X"
        myBoard.unused.remove((x,y))
    print_board(spaces, header)
    if (x,y) in myBoard.unused:
        print("Error")

def test_print():
    myBoard = Board(10,10)
    myBoard.spaces[9][1] = "X"
    print_board(myBoard.spaces, myBoard.header)

test_unused()