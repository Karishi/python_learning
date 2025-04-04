def uniquePaths(grid):
    m = len(grid[0])
    n = len(grid)
    def recurse(grid, count = 0, x = 0, y = 0):
        print(f"Current space is {x}, {y}")
        if x == m - 1 and y == n - 1:
            return count + 1
        
        if x < m - 1:
            count = recurse(grid, count, x + 1, y)
        if y < n - 1:
            count = recurse(grid, count, x, y + 1)
        return count
    
    count = recurse(grid)

    return count

obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]

print(f"The number of unique paths is {uniquePaths(obstacleGrid)}")