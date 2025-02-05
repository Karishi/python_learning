def sudokuSolve(board):
    sudokuOptions = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                sudokuOptions[(i, j)] = [1,2,3,4,5,6,7,8,9]
            else:
                sudokuOptions[(i, j)] = [int(board[i][j])]
    
    altered = True
    while altered:
        altered = False
        # Trim 1: If a space is solved, remove its value from all spaces matching
        # its row, column, and square.
        for i in range(9):
            for j in range(9):
                if len(sudokuOptions[(i, j)]) == 1:
                    val = sudokuOptions[(i, j)][0]
                    for key in sudokuOptions:
                        if (key[0] == i or \
                            key[1] == j or \
                            (key[0]//3 == i//3 and key[1]//3 == j//3)) \
                            and val in sudokuOptions[key] and len(sudokuOptions[key]) > 1:
                            sudokuOptions[key] = [x for x in sudokuOptions[key] if x != val]
                            altered = True
        # Trim 2: Check each row, column, and square to see whether there is any
        # value 1-9 appearing only once. If so, set that space to that value
        for i in range(1,10):
             for j in range(9):
                if trim2cols(i, j, sudokuOptions) or trim2rows(i, j, sudokuOptions) or trim2squares(i, j, sudokuOptions):
                    altered = True

        # if trim3(sudokuOptions):
            # altered = True
    
    for i in range(9):
        for j in range(9):
            if len(sudokuOptions[(i, j)]) == 1:
                board[i][j] = str(sudokuOptions[(i, j)][0])
    for row in board:
        print(row)
                        
def trim2rows(i, j, sudokuOptions):
    firstFoundCoordinate = None
    isTheOnlyOne = True
    for key in sudokuOptions:
        if i in sudokuOptions[key] and key[0] == j:
            if firstFoundCoordinate is None:
                firstFoundCoordinate = key
            else:
                isTheOnlyOne = False
                break
    if firstFoundCoordinate is not None and isTheOnlyOne and len(sudokuOptions[firstFoundCoordinate]) > 1:
        sudokuOptions[firstFoundCoordinate] = [i]
        return True
    else:
        return False

def trim2cols(i, j, sudokuOptions):
    hold = None
    solo = True
    for key in sudokuOptions:
        if i in sudokuOptions[key] and key[1] == j:
            if hold is None:
                hold = key
            else:
                solo = False
                break
    if hold is not None and solo and len(sudokuOptions[hold]) > 1:
        sudokuOptions[hold] = [i]
        return True
    else:
        return False

def trim2squares(i, j, sudokuOptions):
    squares = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)
    }
    hold = None
    solo = True
    for key in sudokuOptions:
        if i in sudokuOptions[key] and (key[0]//3, key[1]//3) == squares[j]:
            if hold is None:
                hold = key
            else:
                solo = False
                break
    if hold is not None and solo and len(sudokuOptions[hold]) > 1:
        sudokuOptions[hold] = [i]
        return True
    else:
        return False

def trim3(sudokuOptions):
    # TODO: Trim 3 is to search for pairs. If any space has exactly 2 options, search row, col, and square
    # for another space that has the exact same two options. If found, these 2 options can be removed
    # from the possibility space of all other spaces in the same row, col, or square as the paired spaces.
    altered = False
    for key in sudokuOptions:
        if len(sudokuOptions[key]) == 2:
            matchedPair = []
            matchedPair.append(sudokuOptions[key[0]][0])
            matchedPair.append(sudokuOptions[key[1]][0])

            for key2 in sudokuOptions:
                if key2 is not key \
                and len(sudokuOptions[key]) == 2 \
                and sudokuOptions[key2[0]] in matchedPair \
                and sudokuOptions[key2[1]] in matchedPair:
                # Search rows
                    if key[0] == key2[0]:
                        for rowkey in sudokuOptions:
                            if rowkey is not key and rowkey is not key2 \
                            and rowkey[0] == key[0] \
                            and matchedPair[0] in sudokuOptions[rowkey] \
                            or matchedPair[1] in sudokuOptions[rowkey]:
                                sudokuOptions[key] = [x for x in sudokuOptions[key] if x not in matchedPair]
                                altered = True
                # Search columns
                    if key[1] == key2[1]:
                        for rowkey in sudokuOptions:
                            if rowkey is not key and rowkey is not key2 \
                            and rowkey[1] == key[1] \
                            and matchedPair[0] in sudokuOptions[rowkey] \
                            or matchedPair[1] in sudokuOptions[rowkey]:
                                sudokuOptions[key] = [x for x in sudokuOptions[key] if x not in matchedPair]
                                altered = True
                # Search squares
                    elif (key[0]//3, key[1]//3) == (key2[0]//3, key2[1]//3):
                        for rowkey in sudokuOptions:
                            if rowkey is not key and rowkey is not key2 \
                            and (rowkey[0]//3, rowkey[1]//3) == (key[0]//3, key[1]//3) \
                            and matchedPair[0] in sudokuOptions[rowkey] \
                            or matchedPair[1] in sudokuOptions[rowkey]:
                                sudokuOptions[key] = [x for x in sudokuOptions[key] if x not in matchedPair]
                                altered = True
    return altered

                    
def guessSudoku(board):
    coords = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                coords.append((i,j))
    
    def tryNums(complete, index = 0, attempt = 1):    
        if index >= len(coords):
            complete = [[] for row in board]
            for row in range(len(board)):
                for item in range(len(board[row])):
                    complete[row].append(board[row][item])
            return complete
        if attempt == 10:
            board[coords[index][0]][coords[index][1]] = "."
            return complete
        

        board[coords[index][0]][coords[index][1]] = str(attempt)

        #time.sleep(.08)

        if isValidSudoku(board):
            complete = tryNums(complete, index + 1, 1)
        complete = tryNums(complete, index, attempt + 1)
        return complete
    
    complete = tryNums([])
    for row in complete:
        print(row)
        
        



def isValidSudoku(board):
    squareList = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            base = []
            for k in range(3):
                for l in range(3):
                    base.append(board[i + k][j + l])
            squareList.append(base)

    def testRow(index):
        row = board[index[0]]
        if row[index[1]] != "." and row[index[1]] in row[index[1] + 1:]:
            return False
    
    def testCol(index):
        for col in range(index[0] + 1, len(board)):
            if board[index[0]][index[1]] != "." and board[col][index[1]] == board[index[0]][index[1]]:
                return False
    
    def testSqu(index):
        row = squareList[index[0]]
        if row[index[1]] != "." and row[index[1]] in row[index[1] + 1:]:
            return False

    for i in range(9):
        for j in range(9):
            #if board[i][j] != ".":
            if testRow((i, j)) == False:
                print("Found false on Rows")
                return False
            
            if testCol((i, j)) == False:
                print("Found false on Columns")
                return False

            if testSqu((i, j)) == False:
                print("Found false on Squares")
                return False
    
    return True

board = [
    [".","1",".",".",".",".",".","7","."],
    ["4","9","5",".","7",".","2",".","."],
    [".",".","6",".",".",".",".","5","1"],
    [".","4",".",".",".",".",".",".","5"],
    ["8",".","7",".",".","3",".","9","4"],
    [".",".",".","8",".",".","7","6","."],
    ["7","3",".",".","4",".","6","2","."],
    [".","8",".",".",".",".",".",".","."],
    ["9",".","2",".","8","7",".",".","."]
    ]

sudokuSolve(board)