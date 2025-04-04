# Given an array of integers nums and an integer k, an element nums[i] is considered good if it is strictly greater than the elements at indices i - k and i + k (if those indices exist). If neither of these indices exists, nums[i] is still considered good.
def sumOfGoodNumbers(nums, k):
    total = 0
    for i in range(len(nums)):
        if (i - k < 0 or nums[i-k] < nums[i]) and (i + k >= len(nums) or nums[i+k] < nums[i]):
            total += nums[i]
    return total

nums = [2,1]
k = 1

print(sumOfGoodNumbers(nums, k))