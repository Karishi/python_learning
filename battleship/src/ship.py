import random
from src.board import print_board

class Ship:
    def __init__(self, size, coordinate, state, name):
        self.size = int(size)
        self.coordinate = coordinate
        self.direction = "N"
        self.state = state
        self.name = name
        self.direction_picker = ""


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
    
standard_ships = [Ship(2, (0,0), {}, "D"), Ship(3, (0,0), {}, "S"), Ship(3, (0,0), {}, "R"), Ship(4, (0,0), {}, "B"), Ship(5, (0,0), {}, "C")]

def get_unused(board):
        start_point = random.choice(board.unused)
        return start_point

def place_ship(myShip, myBoard):
    myShip.direction_picker = random_direction()
    for letter in myShip.direction_picker:
        myShip.direction = letter
        if check_full_ship(myShip,myBoard):
            place_pips(myShip, myBoard)
            return True
    print(f"All directions from point {myShip.coordinate} failed")
    return False

def place_pips(myShip, myBoard):
    x_shift, y_shift = translate_direction(myShip.direction)
    x,y = myShip.coordinate
    for i in range(myShip.size):
        myBoard.spaces[y + i*y_shift][x + i*x_shift] = myShip.name
        if (x + i*x_shift, y + i*y_shift) in myBoard.unused:
            myBoard.unused.remove((x + i*x_shift, y + i*y_shift))
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
    
def edge_check(ship,board):
    y,x = ship.coordinate
    y_shift,x_shift = translate_direction(ship.direction)
    if  x + x_shift * (ship.size-1) < 0 or \
        x + x_shift * (ship.size-1) > board.width-1 or \
        y + y_shift * (ship.size-1) < 0 or \
        y + y_shift * (ship.size-1) > board.height-1:
        print("This is going off the edge!")
        return False
    else:
        print(f"Edge in direction {ship.direction} acceptable from {ship.coordinate}")
        return True

def check_full_ship(ship,the_board):
    if edge_check(ship,the_board):
        x_shift,y_shift = translate_direction(ship.direction)
        x = ship.coordinate[0]
        y = ship.coordinate[1]
        for i in range(ship.size):
            if the_board.spaces[y+y_shift*i-1][x+x_shift*i-1] != "o":
                print('This hits a ship')
                return False
        return True
    else:
        return False
    
def fill_standard_board(myBoard):
    for theShip in standard_ships:
        print(f"Now attempting ship {theShip.name}")
        theShip.coordinate = get_unused(myBoard)
        successful_place = False
        print(len(myBoard.unused))
        while successful_place == False and len(myBoard.unused) > 0:
            successful_place = place_ship(theShip, myBoard)
        print_board(myBoard.spaces, myBoard.header)