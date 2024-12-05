# For a list of numbers, find the highest positive disparity between
# any number and those to its right.

list = [1,2,3,4,5,6,7,8,0]


def buyLowSellHigh(list):
    onlyup = sorted(list)
    leftside = 0
    rightside = len(list)-1
    offset = 1
    success = False
    rightBest = 0
    leftBest = 0

    while leftside < rightside:
        # Finds the smallest and largest value in the list.
        # Checks whether they're in the right order.
        if list.index(onlyup[leftside]) < list.index(onlyup[rightside]):
            return onlyup[rightside] - onlyup[leftside]
        # If not, compares the second-smallest to largest vs smallest to second-largest
        # If one of them is in the right order, the one with the greatest value is the answer.
        if list.index(onlyup[leftside]) < list.index(onlyup[rightside - offset]):
            leftBest = onlyup[rightside - offset] - onlyup[leftside]
            success = True
        if list.index(onlyup[leftside + offset]) < list.index(onlyup[rightside]):
            rightBest = onlyup[rightside] - onlyup[leftside + offset]
            success = True
        if success:
            if rightBest > leftBest:
                return rightBest
            else:
                return leftBest
        # If not, remove the highest and lowest from the search area and move toward the middle.
        leftside += 1
        rightside -= 1
    return 0

                
        
print(buyLowSellHigh(list))