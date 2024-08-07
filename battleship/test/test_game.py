import random

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

def random_ships(numExtraShips):
    ship_arrangement = [2,3,3,4,5]
    for i in range(numExtraShips):
        size = random.choice in ship_arrangement
        newShip = ship(size, (), random_direction(), {}, "Y")
        newShip.name = name_ship(newShip)
        place_ship(newShip)

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