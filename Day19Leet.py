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
    seen = []
    while len(perimeterItemsList) > 0:
        perimeterAdd = 4
        current = perimeterItemsList.pop()
        seen.append((current.x, current.y))
        # Check East
        if current.x < len(matrixList[y])-1 and matrixList[y][x+1] == 1:
            print(f"East of {current.x},{current.y} is {(current.x+1, current.y)}")
            perimeterAdd -= 1
            if not current.fromLandlocked and (current.x+1, current.y) not in seen:
                node = landNode(current.x+1, current.y)
                perimeterItemsList.append(node)
        # Check South
        if current.y < len(matrixList)-1 and matrixList[y+1][x] == 1:
            perimeterAdd -= 1
            if not current.fromLandlocked and (current.x, current.y+1) not in seen:
                node = landNode(current.x, current.y+1)
                perimeterItemsList.append(node)
        # Check West
        if current.x > 0 and matrixList[y][x-1] == 1:
            perimeterAdd -= 1
            if not current.fromLandlocked and (current.x-1, current.y) not in seen:
                node = landNode(current.x-1, current.y)
                perimeterItemsList.append(node)
        # Check North
        if current.y > 0 and matrixList[y-1][x] == 1:
            perimeterAdd -= 1
            if not current.fromLandlocked and (current.x, current.y-1) not in seen:
                node = landNode(current.x, current.y-1)
                perimeterItemsList.append(node)
        
        # A space adds perimeter equal to the number of non-land spaces around it.
        if perimeterAdd > 0:
            perimeter += perimeterAdd
        # A landlocked space's adjacent spaces don't need to add anything.
        else:
            for i in range(4):
                perimeterItemsList[-i].fromLandlocked = True
    return perimeter

def findLand(matrixList):
    y = 0
    x = 0
    while 1 not in matrixList[y]:
        y += 1
    while matrixList[y][x] != 1:
        x += 1
    return x, y
    
list1 = [0,0,0,0]
list2 = [0,0,1,0]
list3 = [0,1,1,1]
list4 = [1,1,0,1]
matrix = [list1, list2, list3, list4]

print(findIslandPerimeter(matrix))