import random

unused = []

class player:
    def __init__(self, title, score):
        self.title = title
        self.score = score

def initialize_unused(my_board):
    for x in range(my_board.height):
        for y in range(my_board.width):
            unused.append((x,y))

class board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        initialize_unused(self)

def print_board(board, header):
    print(' '.join(header))
    for row in board:
        print(' '.join(row))
    print('')

def make_board(board):
    return [['o' for count in range(board.height)] for rows in range(board.width)], [str(i) for i in range(1,board.width+1)]



class ship:
    def __init__(self, size, coordinate, direction, state, name):
        self.size = int(size)
        self.coordinate = coordinate
        self.direction = direction
        self.state = state
        self.name = name

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

def check_against_unusable(ship):
    if ship.coordinate not in unused:
        return False
    else:
        unused.remove(ship.coordinate)
        return True
    
def test_unusable_check():
    myship = ship(3, (5,5), random_direction(), 0, "D")
    print(f"On the first test it returns {check_against_unusable(myship)}")
    print(f"On the second test it returns {check_against_unusable(myship)}")

def place_ship(ship,board):
    ship.direction = random_direction()
    for letter in ship.direction:
        if check_full_ship(ship,board):
            x_shift,y_shift = translate_direction(letter)
            x,y = ship.coordinates
            for i in range(ship.size):
                game.shown_board[y+i*y_shift][x+i*x_shift] = name_ship(ship)
                if (y+i*y_shift,x+i*x_shift) in unused:
                    unused.remove((y+i*y_shift,x+i*x_shift))
                break

def test_place_ship():
    random_ships(1)

def random_direction():
    directions = ['NESW','ESWN','SWNE','WNES']
    return random.choice(directions)

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
    print(f"{rand_y+1},{rand_x+1} coordinates")
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
        test_board[y+i*y_shift][x+i*x_shift] = "D"
    print_board(test_board, header)

def test_map_coords():
    my_board = board(10,10)
    test_board,header = make_board(my_board)
    for i in range(0,my_board.width):
        for j in range(0,my_board.height):
            test_board[i][j] = f"{i},{j}"
    print_board(test_board, header)





def edge_check(ship,board):
    x,y = ship.coordinate
    x_shift,y_shift = translate_direction(ship.direction)
    if  x + x_shift * (ship.size-1) < 0 or \
        x + x_shift * (ship.size-1) > board.width or \
        y + y_shift * (ship.size-1) < 0 or \
        y + y_shift * (ship.size-1) > board.height:
        return False
    else:
        return True

def test_edge():
    myShip = ship(3, (1,1), "N", {}, "D")
    print(f"With coordinates 1,1 going North this returns {edge_check(myShip)}.")
    myShip.direction = "E"
    print(f"With coordinates 1,1 going East this returns {edge_check(myShip)}.")
    myShip.direction = "S"
    print(f"With coordinates 1,1 going South this returns {edge_check(myShip)}.")
    myShip.direction = "W"
    print(f"With coordinates 1,1 going West this returns {edge_check(myShip)}.")

def random_ships(numExtraShips):
    ship_arrangement = [2,3,3,4,5]
    for i in range(numExtraShips):
        size = random.choice in ship_arrangement
        newShip = ship(size, (), random_direction(), {}, "Y")
        newShip.name = name_ship(newShip)
        place_ship(newShip)



def check_full_ship(ship,the_board):
    if edge_check(ship,the_board):
        for i in range(ship.size):
            y_shift,x_shift = translate_direction(ship.direction)
            x = ship.coordinate[0]
            y = ship.coordinate[1]
            if the_board[x+x_shift*i][y+y_shift*i] != "o":
                return False
        return True
    else:
        return False
    
def name_ship(ship):
    if ship.size == 2:
        return "D"
    elif ship.size == 3:
        return random.choice("S","R")
    elif ship.size == 4:
        return "B"
    elif ship.size == 5:
        return "C"
    else:
        return "Y"
    
def place_basic_ships(board):
    destroyer = ship(2,random.choice(unused),"",0,"D")
    place_ship(destroyer,board)
    submarine = ship(3,random.choice(unused),"",0,"S")
    place_ship(submarine,board)
    cruiser = ship(3,random.choice(unused),"",0,"R")
    place_ship(cruiser,board)
    battleship = ship(4,random.choice(unused),"",0,"B")
    place_ship(battleship,board)
    carrier = ship(5,random.choice(unused),"",0,"C")
    place_ship(carrier,board)

class game:
    my_board = board(10,10)
    title = "Joe-Bob"
    score = 0
    player = player(title, score)
    place_basic_ships(my_board)
    shown_board, header = make_board(my_board)
    print_board(shown_board,header)

game()