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
            if board[i][j] != ".":
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
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))