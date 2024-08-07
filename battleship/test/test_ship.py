import random

class ship:
    def __init__(self, size, coordinate, direction, state, name):
        self.size = int(size)
        self.coordinate = coordinate
        self.direction = direction
        self.state = state
        self.name = name

def check_against_unused(ship):
    if ship.coordinate not in board.unused:
        return False
    else:
        board.unused.remove(ship.coordinate)
        return True
    
def test_unused_check():
    myship = ship(3, (5,5), random_direction(), 0, "D")
    print(f"On the first test it returns {check_against_unused(myship)}")
    print(f"On the second test it returns {check_against_unused(myship)}")

def place_ship(ship,board):
    ship.direction = random_direction()
    for letter in ship.direction:
        if check_full_ship(ship,board):
            x_shift,y_shift = translate_direction(letter)
            x,y = ship.coordinate
            for i in range(ship.size):
                board.spaces[(y+i*y_shift,x+i*x_shift)] = name_ship(ship)
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
        test_board.spaces[y+i*y_shift][x+i*x_shift] = "D"
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

def check_full_ship(ship,the_board):
    if edge_check(ship,the_board):
        for i in range(ship.size):
            y_shift,x_shift = translate_direction(ship.direction)
            x = ship.coordinate[0]
            y = ship.coordinate[1]
            if the_board.spaces[(x+x_shift*i,y+y_shift*i)] != "o":
                return False
        return True
    else:
        return False
    
