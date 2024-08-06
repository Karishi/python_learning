import random
import ship

def make_board(board):
    for x in range(board.height):
        for y in range(board.width):
            board.unused.append((x,y))
    return [['o' for count in range(board.height)] for rows in range(board.width)], [str(i) for i in range(1,board.width+1)]

class board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaces, self.header = make_board(self)
        self.unused = []

def print_board(board, header):
    print(' '.join(header))
    for row in board:
        print(' '.join(row))
    print('')

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
    x,y = split_coordinates(user_input)
    my_board.spaces[x][y-1] = "X"
    print_board(my_board.spaces, my_board.header)

def check_against_unused(ship):
    if ship.coordinate not in board.unused:
        return False
    else:
        board.unused.remove(ship.coordinate)
        return True
    
def test_unusable_check():
    myship = ship(3, (5,5), random_direction(), 0, "D")
    print(f"On the first test it returns {check_against_unused(myship)}")
    print(f"On the second test it returns {check_against_unused(myship)}")

def test_map_coords():
    my_board = board(10,10)
    test_board,header = make_board(my_board)
    for i in range(0,my_board.width):
        for j in range(0,my_board.height):
            test_board[i][j] = f"{i},{j}"
    print_board(test_board, header)

