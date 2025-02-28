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
    while shift > 0:
        print(nums[startIndex])
        shift = shift // 2
        if min > nums[startIndex-1] or min > nums[startIndex-shift]:
            if nums[startIndex-1] > nums[startIndex-shift]:
                min = nums[startIndex-shift]
                startIndex = startIndex-shift
            else:
                min = nums[startIndex-1]
                startIndex = startIndex-1
    print(min)

test = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,90,0,2,3,4,5,6,7]

findMin(test)


    