def findDuplicate(nums):
    numberMap = {}
    for num in nums:
        if num in numberMap:
            return num
        else:
            numberMap[num] = True

test = [3,1,3,4,2]

print(findDuplicate(test))