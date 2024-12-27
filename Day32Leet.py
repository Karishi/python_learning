def setZeroes(matrix: list[list[int]]):
    xs = []
    ys = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                xs.append(x)
                ys.append(y)
    
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if x in xs or y in ys:
                matrix[y][x] = 0

testMatrix = [[1,1,1], [1,0,1], [1,1,1]]
for row in testMatrix:
    print(row)
setZeroes(testMatrix)
print("Fixed it...")
for row in testMatrix:
    print(row)
