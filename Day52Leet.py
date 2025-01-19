import math
# Without reusing a slot in nums, add 4 values from nums that sum to match a target.
# Return all unique quartets of values that can achieve this.
def threeSumClosest(nums, target):
    answers = set()
    for i in range(len(nums)-3):
        for j in range(i+1, len(nums)-2):
            for k in range(j+1, len(nums)-1):
                for l in range(k+1, len(nums)):
                    attempt = nums[i] + nums[j] + nums[k] + nums[l]
                    if attempt == target:
                        answers.add((nums[i], nums[j], nums[k], nums[l]))
                        
    return answers

test = [1,0,-1,0,-2,2]

print(threeSumClosest(test, 0))