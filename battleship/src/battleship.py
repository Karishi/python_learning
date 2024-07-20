class player:
    def __init__(self, title, score):
        self.title = title
        self.score = score

class ship:
    def __init__(self, size, coordinate, direction, state):
        self.size = size
        self.coordinate = coordinate
        self.direction = direction
        self.state = state

class game:
    title = input("What's your name? ")
    score = 0
    player = player(title, score)
    cols = 10
    rows = 10
    header_row = [str(i) for i in range(rows+1)]
    board = list[cols][rows]
    for cols in board:
        for rows in board:
            board[cols][rows] = "O"
    print(header_row)
    for row in board:
        print(row)
game()