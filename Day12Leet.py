# For a list of numbers, find the highest positive disparity between
# any number and those to its right.

list = [1,2,3,4,5,6,7,8,0]


def buyLowSellHigh(list):
    onlyup = sorted(list)
    maxGains = 0
    if list.index(onlyup[0]) < list.index(onlyup[-1]):
        return onlyup[-1] - onlyup[0]
    else:
        leftside = 0
        rightside = len(list)-1
        offset = 1
        success = False
        rightBest = 0
        leftBest = 0
        while leftside < rightside:
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
            leftside += 1
            rightside -= 1
        return 0

                
        
print(buyLowSellHigh(list))