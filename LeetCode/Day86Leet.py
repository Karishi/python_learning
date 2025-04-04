def lengthOfLIS(nums):
    best = 0

    def recurse_higher(index, count, nums):
        if index == len(nums)-1:
            return count + 1
        
        if nums[index] < nums[index+1]:
            count = recurse_higher(index+1, count+1, nums)
        else:
            count = recurse_higher(index + 1, count, nums)
        return count
    
    for i in range(len(nums)):
        count = recurse_higher(i, 0, nums)
        if count > best:
            best = count

    return best

test = [1,2,3,4,10,5,6]

print(lengthOfLIS(test))