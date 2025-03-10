import math

def calculateMinimumHP(dungeon):
    startValue = dungeon[0][0]

    def recurseTraverse(x = 0, y = 0, current = startValue, bestMinimum = -math.inf, lowPoint = startValue):
        if current < lowPoint:
            lowPoint = current
            print(f"A new low at {lowPoint}")

        if lowPoint < bestMinimum:
            print(f"Cut off early because {lowPoint} is lower than {bestMinimum}.")
            return bestMinimum
        if x == len(dungeon[0])-1 and y == len(dungeon)-1:
            if min(lowPoint, current) > bestMinimum:
                bestMinimum = lowPoint
                print(f"Our new best minimum is {bestMinimum}")
            return bestMinimum
        

        
        if x < len(dungeon[0])-1:
            print(current+dungeon[y][x+1])
            bestMinimum = recurseTraverse(x+1, y, current + dungeon[y][x+1], bestMinimum, lowPoint)
        if y < len(dungeon)-1:
            print(current+dungeon[y+1][x])
            bestMinimum = recurseTraverse(x, y+1, current + dungeon[y+1][x], bestMinimum, lowPoint)
        return bestMinimum
    
    
    return 1 - recurseTraverse()

test = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

print(calculateMinimumHP(test))