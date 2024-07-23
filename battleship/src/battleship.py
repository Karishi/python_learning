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
    first_char = slice(1)
    letter = coordinate_set[first_char]
    end_chars = slice(1,5)
    number = int(coordinate_set[end_chars])
    return alph_to_num(letter), number

def test_split():
    user_input = "F10"
    board, header = make_board(10,10)
    x,y = split_coordinates(user_input)
    board[x][y-1] = "X"
    print_board(board, header)


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

test_split()
game()