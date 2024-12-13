# Task: Find the volume of water on a map surrounding an island.

class waterNode:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def findExteriorWater(matrixList):
    waterTotal = 0
    processList = []
    seen = []
    if 0 in matrixList[0]:
        for node in range(len(matrixList)):
            if node == 0:
                processList.append(waterNode(node, 0))
                seen.append(waterNode(node, 0))
    for space in range(1, len(matrixList)-2):
        if matrixList[space][0] == 0:
            processList.append(waterNode(0, space))
            seen.append(waterNode(0, space))
        if matrixList[space][-1] == 0:
            processList.append(waterNode(len(matrixList[space])-1, space))
            seen.append(waterNode(len(matrixList[space])-1, space))
    if 0 in matrixList[-1]:
        for node in range(len(matrixList)):
            if node == 0:
                processList.append(waterNode(node, len(matrixList[space])-1))
                seen.append(waterNode(node, len(matrixList[space])-1))
    while len(processList) > 0:
        waterTotal += 1
        current = processList.pop()
        x, y = current.x, current.y
        print(f"seen contains {seen}")
        # Check East
        if x < len(matrixList[y])-1 and matrixList[y][x+1] == 1:
            if (x+1, y) not in seen:
                seen.append((x+1, y))
                node = waterNode(x+1, y)
                processList.append(node)
        # Check South
        if y < len(matrixList)-1 and matrixList[y+1][x] == 1:
            if (x, y+1) not in seen:
                seen.append((x, y+1))
                node = waterNode(x, y+1)
                processList.append(node)
        # Check West
        if x > 0 and matrixList[y][x-1] == 1:
            if (x-1, y) not in seen:
                seen.append((x-1, y))
                node = waterNode(x-1, y)
                processList.append(node)
        # Check North
        if y > 0 and matrixList[y-1][x] == 1:
            if (x, y-1) not in seen:
                seen.append((x, y-1))
                node = waterNode(x, y-1)
                processList.append(node)
    
        
    return waterTotal

def findWater(matrixList):
    y = 0
    x = 0
    if 0 in matrixList[y]:
        while matrixList[y][x] != 0:
            x += 1
    else:
        y += 1
        while matrixList[y][0] != 0 and matrixList[y][-1] != 0 and y < len(matrixList) - 2:
            y += 1
        
    return x, y
    
list1 = [0,0,0,0,0]
list2 = [0,1,1,1,0]
list3 = [0,1,1,1,0]
list4 = [0,0,1,0,0]
list5 = [0,0,1,0,0]
matrix = [list1, list2, list3, list4, list5]

print(findExteriorWater(matrix))