def countSmaller(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
        nums[i] = count
    return nums

nums = [5,2,6,1]

print(countSmaller(nums))