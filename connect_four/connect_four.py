# Initialize a starting board state
rows, cols = (6,7)
header_row = [str(i) for i in range(1,cols+1)]
array2D = [["O" for i in range(cols)] for j in range(rows)]
victory_for_a = False
victory_for_b = False
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

while victory_for_a == False and victory_for_b == False:
    display_board()
    player_turn = swap_turns(player_turn)
    print(f"It is {player_turn}'s turn.")
    move = input("Choose a column 1-7 to drop your letter into. > ")
    victory_for_a = True
    