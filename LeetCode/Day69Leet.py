def maximumGap(nums):
    nums.sort()
    maxDiff = 0
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > maxDiff:
            maxDiff = nums[i+1] - nums[i]
    return maxDiff

test = [3,6,9,1]

print(maximumGap(test))