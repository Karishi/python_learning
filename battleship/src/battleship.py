import random

class player:
    def __init__(self, title, score):
        self.title = title
        self.score = score

class ship:
    def __init__(self, size, coordinate, direction, state):
        self.size = int(size)
        self.coordinate = coordinate
        self.direction = direction
        self.state = state

class board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def alph_to_num(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,len(alphabet)):
        test_let = slice(i,i+1)
        if letter.capitalize() == alphabet[test_let]:
            return i
    return -1

def test_alph():
    num = alph_to_num("z")
    print(f"Number is {num}.")

def split_coordinates(coordinate_set):
    first_char = coordinate_set[1]
    letter = coordinate_set[first_char]
    end_chars = coordinate_set[1:]
    number = int(coordinate_set[end_chars])
    return alph_to_num(letter), number

def test_split():
    user_input = "F10"
    my_board = board(10,10)
    hidden_board, header = make_board(my_board)
    x,y = split_coordinates(user_input)
    hidden_board[x][y-1] = "X"
    print_board(hidden_board, header)

def translate_direction(direction):
    if direction.capitalize() == "N":
        return 0,-1
    elif direction.capitalize() == "S":
        return 0,1
    elif direction.capitalize() == "W":
        return -1,0
    elif direction.capitalize() == "E":
        return 1,0
    else:
        return 0,0
    
def randomize_ship_start(board):
    rand_x = random.randint(0,board.width)
    rand_y = random.randint(0,board.height)
    return rand_x, rand_y
    
def test_trans_direction():
    direction = "N"
    ship_length = 3
    x_shift,y_shift = translate_direction(direction)
    my_board = board(10,10)
    if x_shift == 0 and y_shift == 0:
        print("Error! Inaccurate input")
    test_board,header = make_board(my_board)
    x, y = randomize_ship_start(my_board)
    for i in range(ship_length):
        test_board[x+i*x_shift][y+i*y_shift] = "D"
    print_board(test_board, header)





def make_board(board):
    return [['o' for count in range(board.height)] for rows in range(board.width)], [str(i) for i in range(1,board.width+1)]

def print_board(board, header):
    print(' '.join(header))
    for row in board:
        print(' '.join(row))
    print('')

class game:
    title = input("What's your name? ")
    my_board = board(10,10)
    score = 0
    player = player(title, score)
    board, header = make_board(my_board)
    print_board(board, header)

test_trans_direction()
game()