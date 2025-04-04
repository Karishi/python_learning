import math

def findMin(nums):
    startIndex = len(nums)-1
    shift = len(nums) //2
    min = math.inf
    if nums[startIndex] > nums[shift]:
        min = nums[shift]
        startIndex = shift
    else:
        min = nums[startIndex]
    while shift > 2 and startIndex > 0:
        print(nums[startIndex])
        shift = shift // 2 + 1
        if min > nums[startIndex-1] or min > nums[startIndex-shift]:
            if nums[startIndex-1] > nums[startIndex-shift]:
                min = nums[startIndex-shift]
                startIndex = startIndex-shift
            else:
                min = nums[startIndex-1]
                startIndex = startIndex-1
    print(min)

test = []
for i in range(700):
    test.append(i)

findMin(test)


    