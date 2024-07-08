# Initialize a starting board state
rows, cols = (6,7)
header_row = [str(i) for i in range(1,cols+1)]
array2D = [["O" for i in range(cols)] for j in range(rows)]
victory = False
class player:
    def __init__(self, title, score):
        self.title = title
        self.score = score

p1 = player("A", 0)
p2 = player("B", 0)

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
    return current_player

def drop_piece(array2D, column, current_player):
    column -= 1
    if array2D[0][column] is not 'O':
        print("That space is illegal. Please choose another.")
        return False, -1
    else:
        for row in range(0, 6):
            if row is 5:
                array2D[row][column] = current_player.title
                return True, row               
            if array2D[row+1][column] is not 'O':
                array2D[row][column] = current_player.title
                return True, row
    return True, row

def check_for_victory(array2D, row, column, player_turn):
    dist = 1 
    connect = 1
    print(f"Latest piece dropped into {column},{row}")
    # Check vertical
    if row < 3: # Can only happen with a piece placed in the top 3 rows
        for i in range(0, 4):
            if row+dist <= 5 and array2D[row+dist][column] == player_turn:
                dist += 1
                connect += 1
                print("+1 on the vertical")
                if connect == 4:
                    return True
            else:
                dist = 1
                connect = 1
                break
    # Check horizontal
    for i in range(0, 4):
        if column+dist > 6 or array2D[row][column+dist] != player_turn:
            dist = 1
            break
        else:
            dist += 1
            connect += 1
            print("+1 to the right")
            if connect == 4:
                return True
    for column in range(0, 4):
        if column - dist < 0 or array2D[row][column-dist] != player_turn:
            dist = 1
            connect = 1
            break
        else:
            dist += 1
            connect += 1
            print("+1 to the left")
            if connect == 4:
                return True
    # Check left diagonal
    for i in range(0, 4):
        if column+dist > 6 or row+dist > 5 or array2D[row+dist][column+dist] != player_turn:
            dist = 1
            break
        else:
            dist += 1
            connect += 1
            print("+1 to the lower right")
            if connect == 4:
                return True
    for i in range(0, 4):
        if column-dist < 0 or row - dist < 0 or array2D[row-dist][column-dist] != player_turn:
            dist = 1
            connect = 1
            break
        else:
            dist += 1
            connect += 1
            print("+1 to the upper left")
            if connect == 4:
                return True
    # Check right diagonal
    for i in range(0, 4):
        if column+dist > 6 or row - dist < 0 or array2D[row-dist][column+dist] != player_turn:
            dist = 1
            break
        else:
            dist += 1
            connect += 1
            print("+1 to the upper right")
            if connect == 4:
                return True
    for i in range(0, 4):
        if column - dist < 0 or row + dist > 5 or array2D[row+dist][column-dist] != player_turn:
            dist = 1
            connect = 1
            break
        else:
            dist += 1
            connect += 1
            print("+1 to the lower left")
            if connect == 4:
                return True
    return False

count = 0
while victory == False:
    display_board()
    current_player = swap_turns(current_player)
    print(f"It is {current_player.title}'s turn.")
    valid_reply = False
    while valid_reply == False:
        valid_reply = True
        column = int(input("Choose a column 1-7 to drop your letter into. > "))
        if column > 7 or column < 1:
            valid_reply = False
        else: 
            valid_reply, row = drop_piece(array2D, column, current_player)
    victory = check_for_victory(array2D, row, column, current_player.title)

print(f"Victory for {current_player.title}! The score is now {p1.score} for {p1.title} and {p2.score} for {p2.title}.")
    