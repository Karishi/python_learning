# Task: Find the perimeter of an island.

class landNode:
    def __init__(self, x: int, y: int, fromLandlocked = False):
        self.x = x
        self.y = y
        self.fromLandlocked = fromLandlocked

def findIslandPerimeter(matrixList):
    x, y = findLand(matrixList)
    perimeter = 0
    current = landNode(x, y, False)
    perimeterItemsList = [current]
    seen = [(x, y)]
    while len(perimeterItemsList) > 0:
        perimeterAdd = 4
        current = perimeterItemsList.pop()
        x, y = current.x, current.y
        print(f"seen contains {seen}")
        # Check East
        if x < len(matrixList[y])-1 and matrixList[y][x+1] == 1:
            perimeterAdd -= 1
            if (x+1, y) not in seen:
                seen.append((x+1, y))
                node = landNode(x+1, y)
                perimeterItemsList.append(node)
        # Check South
        if y < len(matrixList)-1 and matrixList[y+1][x] == 1:
            perimeterAdd -= 1
            if (x, y+1) not in seen:
                seen.append((x, y+1))
                node = landNode(x, y+1)
                perimeterItemsList.append(node)
        # Check West
        if x > 0 and matrixList[y][x-1] == 1:
            perimeterAdd -= 1
            if (x-1, y) not in seen:
                seen.append((x-1, y))
                node = landNode(x-1, y)
                perimeterItemsList.append(node)
        # Check North
        if y > 0 and matrixList[y-1][x] == 1:
            perimeterAdd -= 1
            if (x, y-1) not in seen:
                seen.append((x, y-1))
                node = landNode(x, y-1)
                perimeterItemsList.append(node)
    
        perimeter += perimeterAdd
        print(f"{(x, y)} adds {perimeterAdd} edge segments to the perimeter.")
    
    return perimeter

def findLand(matrixList):
    y = 0
    x = 0
    while 1 not in matrixList[y]:
        y += 1
    while matrixList[y][x] != 1:
        x += 1
    return x, y
    
list1 = [0,0,0,0,0]
list2 = [0,1,1,1,0]
list3 = [0,1,1,1,0]
list4 = [0,0,1,0,0]
list5 = [0,0,1,0,0]
matrix = [list1, list2, list3, list4, list5]

print(findIslandPerimeter(matrix))