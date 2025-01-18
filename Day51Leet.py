import math
# Without reusing a slot in nums, add 3 values from nums to get as close as possible to a target.
# Returns both the closest distance and the winning trio.
def threeSumClosest(nums, target):
    answers = set()
    bestDist = math.inf
    winner = (0,0,0)
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                attempt = abs(nums[i] + nums[j] + nums[k] - target)
                if attempt < bestDist:
                    bestDist = attempt
                    winner = (nums[i], nums[j], nums[k])
    return bestDist, winner

test = [-1,0,1,2,-1,-4]

print(threeSumClosest(test, 4))