def make_board(board):
    for x in range(board.width):
        for y in range(board.height):
            board.unused.append((x,y))
    return [['o' for x in range(board.width)] for y in range(board.height)], [str(i) for i in range(1,board.width+1)]

class Board:
    unused = []
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaces, self.header = make_board(self)
        self.unsunk = 0

def print_board(board, header):
    print("X " + ' '.join(header))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let = 0
    for column in board:
        print(alphabet[let]+" " + ' '.join(column))
        let += 1
    print('')

