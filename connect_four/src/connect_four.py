# Initialize a starting board state
rows, cols = (6,7)
header_row = [str(i) for i in range(1,cols+1)]
array2D = [["O" for i in range(cols)] for j in range(rows)]
victory = False
row = -1
column = -1
class player:
    def __init__(self, title, score, turn):
        self.title = title
        self.score = score
        self.turn = turn

p1 = player("A", 0, 0)
p2 = player("B", 0, 0)

class game:
    def __init__(self, column, row, player, array2D):
        self.column = column
        self.row = row
        self.player = player
        self.board = array2D

current_player = p2

def display_board():
    print(header_row)
    for row in array2D:
        print(row)

def swap_turns(current_player):
    if current_player == p2:
        current_player = p1
    else:
        current_player = p2
    current_player.turn += 1
    return current_player

def drop_piece(array2D, column, current_player):
    column -= 1
    if array2D[0][column] != 'O':
        print("That space is illegal. Please choose another.")
        return False, -1
    else:
        for row in range(0, 6):
            if row == 5:
                array2D[row][column] = current_player.title
                return True, row
            if array2D[row+1][column] != 'O':
                array2D[row][column] = current_player.title
                return True, row
    return True, row

def victory_vertical(loc):
    if loc.row < 3: # Can only happen with a piece placed in the top 3 rows
        connect = 1
        for dist in range(1, 4):
            if loc.row+dist <= 5 and loc.board[loc.row+dist][loc.column] == current_player.title:
                connect += 1
                print(f"Matching piece {dist} below")
                if connect == 4:
                    print("That's connect 4 vertical!")
                    return True
            else:
                return False
    else:
        return False

def victory_horizontal(loc):
    connect = 1
    for dist in range(1,4):
        if loc.column+dist <= 6 and loc.board[loc.row][loc.column+dist] == current_player.title:
            connect += 1
            print(f"Matching piece {dist} to the right")
        else:
            break
    for dist in range(1,4):
        if loc.column-dist >= 0 and loc.board[loc.row][loc.column-dist] == current_player.title:
            connect += 1
            print(f"Matching piece {dist} to the left")
        else:
            break
    if connect >= 4:
        print("That's connect 4 horizontal!")
        return True
    else:
        return False

def victory_l_diagonal(loc):
    connect = 1
    for dist in range(1, 4):
        if loc.column+dist <= 6 and loc.row+dist <= 5 and loc.board[loc.row+dist][loc.column+dist] == current_player.title:
            connect += 1
            print(f"Matching piece {dist} to the lower right")
        else:
            break
    for dist in range(1, 4):
        if loc.column-dist >= 0 and loc.row - dist >= 0 and loc.board[loc.row-dist][loc.column-dist] == current_player.title:
            connect += 1
            print(f"Matching piece {dist} to the upper left")
        else:
            break
    if connect >= 4:
        print("That's connect 4 diagonal (left up)!")
        return True
    else:
        return False

def victory_r_diagonal(loc):
    connect = 1
    for dist in range(1, 4):
        if loc.column+dist <= 6 and loc.row - dist >= 0 and loc.board[loc.row-dist][loc.column+dist] == current_player.title:
            connect += 1
            print(f"Matching piece {dist} to the upper right")
        else:
            break
    for dist in range(1, 4):
        if loc.column - dist >= 0 and loc.row + dist <= 5 and loc.board[loc.row+dist][loc.column-dist] == current_player.title:
            connect += 1
            print(f"Matching piece {dist} to the lower left")
        else:
            break
    if connect >= 4:
        print("That's connect 4 diagonal (right up)!")
        return True
    else:
        return False


def check_for_victory(loc):
    loc.column -= 1
    print(f"Latest piece dropped into {column},{row}")
    # Check vertical
    if victory_vertical(loc):
        return True
    # Check horizontal
    if victory_horizontal(loc):
        return True
    # Check left diagonal
    if victory_l_diagonal(loc):
        return True
    # Check right diagonal
    if victory_r_diagonal(loc):
        return True
    return False

count = 0
while victory == False:
    row = -1
    column = -1
    display_board()
    current_player = swap_turns(current_player)
    print(f"It is {current_player.title}'s turn.")
    valid_reply = False
    while valid_reply == False:
        column = int(input("Choose a column 1-7 to drop your letter into. > "))
        if column > 7 or column < 1:
            valid_reply = False
        else:
            valid_reply, row = drop_piece(array2D, column, current_player)
    if current_player.turn < 4:
        print(f"Player {current_player.title} cannot win yet because they have only taken {current_player.turn} turn(s).")
    else:
        location = game(column, row, current_player.title, array2D)
        victory = check_for_victory(location)

current_player.score += 1
display_board()
print(f"Victory for {current_player.title}! The score is now {p1.score} for {p1.title} and {p2.score} for {p2.title}.")
    