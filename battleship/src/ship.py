import random

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

def get_unused(board):
        start_point = random.choice(board.unused)
        return start_point

def place_ship(myShip, myBoard):
    myShip.direction_picker = random_direction()
    for letter in myShip.direction_picker:
        myShip.direction = letter
        if check_full_ship(myShip,myBoard):
            x_shift,y_shift = translate_direction(myShip.direction)
            x,y = myShip.coordinate
            for i in range(myShip.size):
                myBoard.spaces[x+i*x_shift][y+i*y_shift] = name_ship(myShip)
                if (y+i*y_shift,x+i*x_shift) in myBoard.unused:
                    myBoard.unused.remove((y+i*y_shift,x+i*x_shift))

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
    x,y = ship.coordinate
    x_shift,y_shift = translate_direction(ship.direction)
    if  x + x_shift * (ship.size-1) < 0 or \
        x + x_shift * (ship.size-1) > board.width or \
        y + y_shift * (ship.size-1) < 0 or \
        y + y_shift * (ship.size-1) > board.height:
        print("This is going off the edge!")
        return False
    else:
        print(f"Edge in direction {ship.direction} found to be usable")
        return True

def check_full_ship(ship,the_board):
    if edge_check(ship,the_board):
        for i in range(ship.size):
            x_shift,y_shift = translate_direction(ship.direction)
            x = ship.coordinate[0]
            y = ship.coordinate[1]
            if the_board.spaces[x+x_shift*i][y+y_shift*i] != "o":
                return False
        return True
    else:
        return False
    
