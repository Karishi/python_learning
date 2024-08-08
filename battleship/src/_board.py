import random
import _ship

def make_board(board):
    for x in range(board.height):
        for y in range(board.width):
            board.unused.append((x,y))
    return [['o' for count in range(board.height)] for rows in range(board.width)], [str(i) for i in range(1,board.width+1)]

class board:
    unused = []
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaces, self.header = make_board(self)
        


def print_board(board, header):
    print(' '.join(header))
    for row in board:
        print(' '.join(row))
    print('')

