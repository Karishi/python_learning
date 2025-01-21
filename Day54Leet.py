def isValidSudoku(board):
    def testRow(index):
        row = board[index[0]]
        if row[index[1]] != "." and row[index[1]] in row[index[1]+1:]:
            return False
    
    def testCol(index):
        for row in range(index[1]+1, len(board)-1):
            if board[index[0]][index[1]] != "." and board[row][index[1]] == board[index[0]][index[1]]:
                return False
    
    def testSqu(index):
        pass

    if testRow((0,0)) == False:
        return False
    
    if testCol((0,0)) == False:
        return False
    
    return True

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".5","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))