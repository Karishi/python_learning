import random
from src.board import print_board
from multipledispatch import dispatch

list_of_ships = []

class Ship:
    def __init__(self, size, coordinate, name):
        self.size = int(size)
        self.coordinate = coordinate
        self.direction = "N"
        self.damage = 0
        self.name = name
        self.direction_picker = ""
        list_of_ships.append(self)

def name_ship(my_ship):
    if my_ship.size == 2:
        return "D"
    elif my_ship.size == 3:
        return "S"
    elif my_ship.size == 4:
        return "B"
    elif my_ship.size == 5:
        return "C"
    else:
        return "Y"

standard_ships = [Ship(2, (0,0), "D"), Ship(3, (0,0), "S"), Ship(3, (0,0), "R"), Ship(4, (0,0), "B"), Ship(5, (0,0), "C")]

def get_unused(my_board):
        start_point = random.choice(my_board.unused)
        return start_point

def place_ship(my_ship, my_board):
    my_ship.direction_picker = random_direction()
    for letter in my_ship.direction_picker:
        my_ship.direction = letter
        if check_full_ship(my_ship,my_board):
            place_pips(my_ship, my_board)
            return True
    print(f"All directions from point {my_ship.coordinate} failed")
    return False

def place_ship(my_ship, my_board, direction):
    my_ship.direction = direction
    place_pips(my_ship, my_board)
    return True

def place_pips(my_ship, my_board):
    x_shift, y_shift = translate_direction(my_ship.direction)
    x,y = my_ship.coordinate
    for i in range(my_ship.size):
        my_board.spaces[y + i*y_shift][x + i*x_shift] = my_ship.name
        if (x + i*x_shift, y + i*y_shift) in my_board.unused:
            my_board.unused.remove((x + i*x_shift, y + i*y_shift))
            print(f"Removed {(x + i*x_shift, y + i*y_shift)}")

def random_direction():
    directions = ['NESW','ESWN','SWNE','WNES']
    return random.choice(directions)

def translate_direction(direction):
    if direction.capitalize() == "N":
        print("It's pointed North")
        return 0,-1
    elif direction.capitalize() == "S":
        print("It's pointed South")
        return 0,1
    elif direction.capitalize() == "W":
        print("It's pointed West")
        return -1,0
    elif direction.capitalize() == "E":
        print("It's pointed East")
        return 1,0
    else:
        return 0,0
    
def edge_check(my_ship,my_board):
    y,x = my_ship.coordinate
    y_shift,x_shift = translate_direction(my_ship.direction)
    if  x + x_shift * (my_ship.size-1) < 0 or \
        x + x_shift * (my_ship.size-1) > my_board.width-1 or \
        y + y_shift * (my_ship.size-1) < 0 or \
        y + y_shift * (my_ship.size-1) > my_board.height-1:
        print("This is going off the edge!")
        return False
    else:
        print(f"Edge in direction {my_ship.direction} acceptable from {my_ship.coordinate}")
        return True

def check_full_ship(my_ship, my_board):
    if edge_check(my_ship, my_board):
        x_shift,y_shift = translate_direction(my_ship.direction)
        x = my_ship.coordinate[0]
        y = my_ship.coordinate[1]
        for i in range(my_ship.size):
            print(f"checking space ({y+y_shift*i}, {x+x_shift*i})")
            if my_board.spaces[y+y_shift*i][x+x_shift*i] != "o":
                print('This hits a ship')
                return False
        return True
    else:
        return False

def fill_standard_board(my_board):
    for the_ship in standard_ships:
        print(f"Now attempting ship {the_ship.name}")
        the_ship.coordinate = get_unused(my_board)
        successful_place = False
        print(len(my_board.unused))
        while successful_place == False and len(my_board.unused) > 0:
            successful_place = place_ship(the_ship, my_board, "S")
            list_of_ships.append(the_ship)
        print_board(my_board.spaces, my_board.header)

def sink_ship(visible, x, y, unsunk):
    for ship in list_of_ships:
        if ship.name == visible.spaces[x][y-1]:
            ship.damage += 1
            if ship.damage >= ship.size:
                unsunk -= 1
                print(f"Ship {ship.name} sunk!")