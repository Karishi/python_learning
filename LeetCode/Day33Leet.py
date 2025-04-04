def searchMatrix(matrix: list[list[int]], target: int):
    index = 0
    row = 0
    while matrix[row][len(matrix[row])-1] <= target:
        print(f"Not present in row {row}. Searching row {row+1}...")
        if matrix[row][len(matrix[row])-1] == target:
            return True
        print(f"{matrix[row][len(matrix[row])-1]} is less than {target}.")
        if row == len(matrix):
            return False
        row += 1
    while matrix[row][index] <= target:
        if matrix[row][index] == target:
            return True
        else:
            print(f"{matrix[row][index]} is less than {target}.")
            index += 1

    return False

testMatrix = [[1,3,5,7], [10,11,16,20], [23,30,34, 60]]
value = 32

if searchMatrix(testMatrix, value):
    print(f"{value} is present in the matrix.")
else:
    print(f"{value} is not present.")