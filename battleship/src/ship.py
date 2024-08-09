import random
from src.board import *

class Ship:
    def __init__(self, size, coordinate, direction, state, name):
        self.size = int(size)
        self.coordinate = coordinate
        self.direction = direction
        self.state = state
        self.name = name


def name_ship(ship):
    if ship.size == 2:
        return "D"
    elif ship.size == 3:
        return "S"
    elif ship.size == 4:
        return "B"
    elif ship.size == 5:
        return "C"
    else:
        return "Y"

def check_against_unused(ship,board):
    if ship.coordinate not in board.unused:
        return False
    else:
        board.unused.remove(ship.coordinate)
        return True

def place_ship(ship,Board):
    ship.direction = random_direction()
    for letter in ship.direction:
        if check_full_ship(ship,Board):
            x_shift,y_shift = translate_direction(letter)
            x,y = ship.coordinate
            for i in range(ship.size):
                Board.spaces[(y+i*y_shift,x+i*x_shift)] = name_ship(ship)
                if (y+i*y_shift,x+i*x_shift) in Board.unused:
                    Board.unused.remove((y+i*y_shift,x+i*x_shift))
                break

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
    
