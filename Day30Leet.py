def sortColors(nums):
    shoved = 0
    index = 0
    while index < len(nums) - shoved:
        print(nums)
        print(f"examining value {index}")
        if nums[index] == 0:
            nums.insert(0, nums.pop(index))
            index += 1
        elif nums[index] == 2:
            nums.insert(len(nums), nums.pop(index))
            shoved += 1
        else:
            index += 1

    return nums

testList = [2,2,1,1,0,0,1,0,1,2,1,0,1,2]

print(sortColors(testList))