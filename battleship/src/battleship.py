alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class player:
    def __init__(self, title, score):
        self.title = title
        self.score = score

class ship:
    def __init__(self, size, coordinate, direction, state):
        self.size = size
        self.coordinate = coordinate
        self.direction = direction
        self.state = state

def make_board(x,y):
    return [['o' for count in range(x)] for rows in range(y)], [str(i) for i in range(1,y+1)]

def print_board(board, header):
    print(' '.join(header))
    for row in board:
        print(' '.join(row))
    print('')

class game:
    title = input("What's your name? ")
    score = 0
    player = player(title, score)
    myboard, header = make_board(10,10)
    print_board(myboard, header)

game()