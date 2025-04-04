# Without reusing a slot in nums, add 3 values from nums to get 0.
# Return all 3-value options that sum to 0.
def threeSum(nums):
    answers = set()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    answers.add((nums[i], nums[j], nums[k]))
    return answers

test = [-1,0,1,2,-1,-4]

print(threeSum(test))