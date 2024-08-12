import board

def test_make():
    myBoard = board.Board(10,10)
    spaces = myBoard.spaces
    header = myBoard.header
    spaces[3][4] = "D"
    board.print_board(spaces,header)
    assert spaces[3][3] == "o"
    assert spaces[3][4] == "o"
#Should give one success and one failure

def test_unused():
    myBoard = board.Board(10,10)
    assert len(myBoard.unused) == 100
    spaces = myBoard.spaces
    header = myBoard.header
    x = 3
    y = 4
    if (x,y) in myBoard.unused:
        myBoard.spaces[x][y] = "X"
        myBoard.unused.remove((x,y))
    board.print_board(spaces, header)
    if (x,y) in myBoard.unused:
        print("Error")

test_unused()