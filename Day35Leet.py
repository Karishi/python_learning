import math

def minPathSum(grid):
    def find_least(coordSet):
        best = math.inf
        coords = (-1,-1)
        for c in coordSet:
            attempt = bestPath[c[1]][c[0]]
            if attempt < best:
                best = attempt
                coords = c
        return coords
        
    
    processed = []
    bestPath = [[math.inf] * len(grid[y]) for y in range(len(grid))]
    bestPath[0][0] = grid[0][0]

    def printProcess():
        for row in bestPath:
            print(row)
    
    printProcess()
    
    coord = (0,0)
    processed.append(coord)
    finalSpace = (len(grid[0])-1, len(grid)-1)

    process = 0
    while finalSpace not in processed and process < 10:
        coord = processed.pop(0)
        current = bestPath[coord[1]][coord[0]]

        if coord[0] < len(grid[0])-1:
            right = grid[coord[1]][coord[0]+1]
            bestRight = bestPath[coord[1]][coord[0]+1]
            movingRight = current + right
            if movingRight < bestRight:
                bestPath[coord[1]][coord[0]+1] = movingRight
                processed.append((coord[0]+1, coord[1]))

        if coord[1] < len(grid)-1:
            down = grid[coord[1]+1][coord[0]]
            bestDown = bestPath[coord[1]+1][coord[0]]
            movingDown = current + down
            if movingDown < bestDown:
                bestPath[coord[1]+1][coord[0]] = movingDown
                processed.append((coord[0], coord[1]+1))
        
        print()
        printProcess()
    return bestPath[len(grid[0])-1][len(grid)-1]

test = [[1,3,1],
        [1,5,1],
        [4,2,1]]

print(minPathSum(test))