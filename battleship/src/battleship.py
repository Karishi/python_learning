class player:
    def __init__(self, title, score):
        self.title = title
        self.score = score

class game:
    def __init__(self, ship, board, turn):
        self.ship = ship
        self.board = board
        self.turn = turn

class ship:
    def __init__(self, size, coordinate, direction, state):
        self.size = size
        self.coordinate = coordinate
        self.direction = direction
        self.state = state
