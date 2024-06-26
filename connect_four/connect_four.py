# Initialize a starting board state
rows, cols = (6,7)
header_row = [str(i) for i in range(1,cols+1)]
array2D = [["O" for i in range(cols)] for j in range(rows)]
victory = False
player_turn = 'B'

def display_board():
    print(header_row)
    for row in array2D:
        print(row)

def swap_turns(player_turn):
    if player_turn == 'B':
        player_turn = 'A'
    else:
        player_turn = 'B'
    return player_turn

def drop_piece(array2D, column, player_turn):
    if array2D[0][column] is not 'O':
        print("That space is illegal. Please choose another.")
        return False
    for row in range(0, 5):
        if array2D[row+1][column] is not 'O' or array2D[row+1][column] is None:
            array2D[row][column] = player_turn
            return True
    array2D[5][column] = player_turn
    return True, row

def check_for_victory(array2D, row, column, player_turn):
    dist = 1 
    connect = 1
    # Check vertical
    if row < 3:
        for i in range(0, 4):
            if array2D[row+dist][column] == player_turn:
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
    player_turn = swap_turns(player_turn)
    print(f"It is {player_turn}'s turn.")
    valid_reply = False
    while valid_reply == False:
        valid_reply = True
        column = int(input("Choose a column 1-7 to drop your letter into. > "))
        if column > 7 or column < 1:
            valid_reply = False
        valid_reply, row = drop_piece(array2D, column, player_turn)
    victory = check_for_victory(array2D, row, column, player_turn)

print(f"Victory for {player_turn}!")
    